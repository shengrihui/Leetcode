import os
import re
import subprocess
from time import *

import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conf import *
from tools import *


def get_examples_code(html):
    # 示例
    example_patten = r"<(?:strong|b)>输入：</(?:strong|b)>(.*?)<(?:strong|b)>输出：</(?:strong|b)>(.*?)<"
    example_matches = re.findall(example_patten, html, re.DOTALL)
    examples_list = []
    for example in example_matches:
        input_ = example[0].strip()
        output = example[1].strip()
        examples_list.append(f"(dict({input_}),{output}),")
    examples = "\n    ".join(examples_list)
    print(examples_list)

    # 代码
    soup = BeautifulSoup(html, 'html.parser')
    code_snippets = soup.select('.CodeMirror-line')
    code_list = []
    for code_snippet in code_snippets[:2]:
        code_list.append(code_snippet.text.strip())
    code_list[1] = "    " + code_list[1]
    code_list.append("        pass\n")
    code = "\n".join(code_list)

    # 函数名
    function_name_patten = r"def (.*?)\("
    function_name_match = re.search(function_name_patten, code)
    # print(function_name_match.group(1))
    return examples, code, function_name_match.group(1)


if __name__ == '__main__':
    competition_page_url = "https://leetcode.cn/contest/weekly-contest-375"
    # competition_page_url = "https://leetcode.cn/contest/biweekly-contest-119"
    coding_language = "Python3"
    remote_debugging_port = 9999


    if not is_port_in_use(remote_debugging_port):
        print("启动浏览器...")
        command = f'"{chrome_path}" --remote-debugging-port={remote_debugging_port} --user-data-dir="C:/Users/11200/AppData/Local/Google/Chrome/User Data"'
        # print(command)
        chrome_process = subprocess.Popen(command, shell=True)
        # chrome_process.wait()
        sleep(2)

    # 浏览器选项配置
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{remote_debugging_port}")

    try:
        print("尝试连接浏览器")
        service = Service()
        bro = webdriver.Chrome(service=service, options=chrome_options)
        # bro.set_window_rect(500, 0, 1920 * 0.9, 1040 * 0.9)
        bro.implicitly_wait(2)  # 之后操作都等3秒
        print("启动连接上了")
    except Exception as e:
        print("出现错误", e)
        # kill_process_using_port(remote_debugging_port)
        exit(0)

    # 是否已经开启了竞赛页面
    window_handles = bro.window_handles
    for i, handle in enumerate(window_handles):
        bro.switch_to.window(handle)
        # current_url = bro.current_url  # 打印当前窗口的URL
        cur_title = bro.title
        # 关闭空标签页
        # if "必应" == cur_title:
        #     bro.close()
        if re.search(r"第(.*?)周赛", cur_title):
            break
    else:
        print("打开竞赛页面")
        bro.execute_script(f"window.open('{competition_page_url}');")
        sleep(2)
        # bro.switch_to.new_window('tab')
        bro.switch_to.window(bro.window_handles[-1])

    competition_title_element = WebDriverWait(bro, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="contest-app"]/div/div/div[1]/div[2]/div[1]')))
    competition_title_text = competition_title_element.text
    # competition_title_text = "第 666 场周赛"
    if not os.path.exists(competition_title_text):
        os.mkdir(competition_title_text)

    i = 2  # 题目a标签所在的li标签的xpath序号从2开始
    while i <= 5:
        # 如果不是这一场竞赛的页面，就新开一个，这样每一道题都是一页
        if not re.search(r"第(.*?)周赛", bro.title):
            bro.execute_script(f"window.open('{competition_page_url}');")
            sleep(1)
            bro.switch_to.window(bro.window_handles[-1])
        while True:
            # 用while-try的形式，主要是为了还没到时间，问题列表还没刷新出来，用这样的方式刷新出来
            try:
                a_locator = (By.XPATH, f'//*[@id="contest-app"]/div/div/div[4]/div[1]/ul/li[{i}]/a')
                a_element = WebDriverWait(bro, 1).until(EC.presence_of_element_located(a_locator))
                # print(a_element.text)
                break
            except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                bro.get(competition_page_url)
                # bro.refresh()
                print("刷新")

        a_element.click()
        # bro.get(test_url[i - 2])  # 测试时候用
        # 问题的题目
        problem_title_element = WebDriverWait(bro, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="base_content"]/div[1]/div/div/div[1]/h3')))
        # 语言的选择
        language_element = WebDriverWait(bro, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-select-2--value-item"]')))
        if language_element.text != coding_language:
            print("语言不对")
            sleep(10)
        problem_contest_link = bro.current_url
        problem_title = problem_title_element.text
        file_name = f"{competition_title_text}/{i - 1}-{problem_title}.py"
        if not os.path.exists(file_name):
            examples, code, f_name = get_examples_code(bro.page_source)
            with open(file_name, "w", encoding="utf-8") as f:
                file_content = py.format(title=problem_title, contest_link=problem_contest_link, code=code,
                                         examples=examples, function_name=f_name,
                                         leetcode_link="https://leetcode.cn/problems/" +
                                                       problem_contest_link.strip("/").split("/")[-1])
                f.write(file_content)
        print(file_name)
        # bro.back()
        sleep(1)
        i += 1
        # break

    sleep(1)
    # bro.close()
