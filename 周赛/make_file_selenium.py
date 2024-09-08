import os
import re
import subprocess
from time import *

import psutil
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

py = """# {contest_id}
# 题目：{title}
# 题目链接：
# 竞赛：{contest_link}
# 题库：{leetcode_link}

from typing import List
import heapq
from bisect import *
from collections import Counter, defaultdict, deque
from functools import *
from heapq import *
from itertools import *
from math import comb, gcd, inf, isqrt, lcm, sqrt
from typing import List, Optional

{code}

s = Solution()
examples = [
    {examples}
]
for e, a in examples:
    print(a, e)
    print(s.{function_name}(**e))
"""

test_url = [
    "https://leetcode.cn/contest/biweekly-contest-136/problems/time-taken-to-mark-all-nodes/",
    "https://leetcode.cn/contest/biweekly-contest-136/problems/time-taken-to-mark-all-nodes/",
    "https://leetcode.cn/contest/weekly-contest-412/problems/final-array-state-after-k-multiplication-operations-ii/",
    "https://leetcode.cn/contest/weekly-contest-412/problems/count-almost-equal-pairs-i/",
    "https://leetcode.cn/contest/weekly-contest-412/problems/final-array-state-after-k-multiplication-operations-i/",
    "https://leetcode.cn/contest/weekly-contest-412/problems/count-almost-equal-pairs-ii/",
]
driver_dir = "E:/CS/PYTHON/08爬虫Chrome/"
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"


def get_examples_code(html):
    # 示例
    soup = BeautifulSoup(html, 'html.parser')
    soup_text = soup.text.split("\n")
    example_matches = [s for s in soup_text if
                       s.startswith("输入：") or s.startswith("输出：") or s.startswith("输入:") or s.startswith("输出:")]
    examples_list = []
    print(*example_matches, sep="\n")
    for j in range(0, len(example_matches), 2):
        inp = example_matches[j]
        out = example_matches[j + 1]
        print(inp, out)
        input_ = inp[3:].strip().replace("true", "True").replace("false", "False")
        output = out[3:].strip().replace("true", "True").replace("false", "False")
        examples_list.append(f"(dict({input_}),{output}),")
    examples = "\n    ".join(examples_list)
    print(examples)

    # 代码
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


def is_port_in_use(port):
    for conn in psutil.net_connections():
        if conn.laddr.port == port:
            return True
    return False


def kill_process_using_port(port):
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            connections = process.connections()
            for connection in connections:
                if connection.laddr.port == port:
                    print(f"Killing process with PID: {process.info['pid']} and port: {port}")
                    psutil.Process(process.info['pid']).terminate()
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


if __name__ == '__main__':
    competition_page_url = "https://leetcode.cn/contest/weekly-contest-414"
    # competition_page_url = "https://leetcode.cn/contest/biweekly-contest-138"
    coding_language = "Python3"
    remote_debugging_port = 9999

    if not is_port_in_use(remote_debugging_port):
        print("启动浏览器...")
        chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
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
        # bro.execute_script(f"window.open('{competition_page_url}');")
        bro.get(competition_page_url)
        sleep(1)
        # bro.switch_to.new_window('tab')
        bro.switch_to.window(bro.window_handles[-1])

    competition_title_element = WebDriverWait(bro, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="contest-app"]/div/div/div[1]/div[2]/div[1]')))
    competition_title_text = competition_title_element.text
    # competition_title_text = "第 666 场周赛"
    if not os.path.exists(competition_title_text):
        os.mkdir(competition_title_text)

    i = 5  # 题目a标签所在的li标签的xpath序号从2开始
    while i >= 2:
        # 如果不是这一场竞赛的页面，就新开一个，这样每一道题都是一页
        if not re.search(r"第(.*?)周赛", bro.title):
            print(re.search(r"第(.*?)周赛", bro.title))
            bro.execute_script("window.open('','_blank');")
            print("新开标签页")
            sleep(1)
            bro.switch_to.window(bro.window_handles[-1])
            bro.get(competition_page_url)
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
        # bro.get(test_url[i])  # 测试时候用
        # 问题的题目
        # problem_title_element = WebDriverWait(bro, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="base_content"]/div[1]/div/div/div[1]/h3')))
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
                file_content = py.format(contest_id=f"{competition_title_text} 第 {i - 1} 题", title=problem_title,
                                         contest_link=problem_contest_link, code=code,
                                         examples=examples, function_name=f_name,
                                         leetcode_link="https://leetcode.cn/problems/" +
                                                       problem_contest_link.strip("/").split("/")[-1])
                f.write(file_content)
        print(file_name)
        # bro.back()
        sleep(3)
        i -= 1
        # break

    sleep(1)
    # bro.close()
