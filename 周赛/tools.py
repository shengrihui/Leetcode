import socket

import psutil
from lxml import etree


# def is_port_in_use(port):
#     """
#     检查指定端口是否已经被占用
#     """
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         try:
#             s.bind(('127.0.0.1', port))
#         except OSError:
#             return True
#         return False
#
#
# def kill_process_using_port(port):
#     """
#     杀掉占用指定端口的进程
#     """
#     for process in psutil.process_iter(attrs=['pid', 'name']):
#         try:
#             for conn in process.connections(kind='inet'):
#                 if conn.laddr.port == port:
#                     process.terminate()
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
import psutil

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


def find_real_xpath(bro, tag, parent_xpath):
    """
    bro：浏览器实例
    tag：要找的元素的标签
    parent_xpath：要找的元素的父元素或爷爷元素的xpath
    """
    tree = etree.HTML(bro.page_source)
    element_list = tree.xpath(parent_xpath)[0]
    # 为了找正确的xpath
    for element in element_list.iter():
        if element.tag == tag:
            print("标签:", element.tag)
            print("属性:", element.attrib)
            print("xpath:", problem_list.getroottree().getpath(element))
            print(etree.tostring(element, encoding="utf-8", pretty_print=True).decode("utf-8"))
            print("-" * 20)


if __name__ == "__main__":
    # target_port = 9999  # 你想要检查的端口号
    #
    # if is_port_in_use(target_port):
    #     print(f"端口 {target_port} 已经被占用，正在尝试关闭占用该端口的进程...")
    #     kill_process_using_port(target_port)
    #     if not is_port_in_use(target_port):
    #         print(f"端口 {target_port} 已成功释放")
    #     else:
    #         print(f"无法释放端口 {target_port}")
    # else:
    #     print(f"端口 {target_port} 未被占用")

    # 指定要检测的端口号
    port_to_check = 9999

    if is_port_in_use(port_to_check):
        print(f"Port {port_to_check} is in use.")
        kill_process_using_port(port_to_check)
    else:
        print(f"Port {port_to_check} is not in use.")
