#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：dcnserver.py
import asyncio
import itertools
import os
import socket
import time
import threading
#import xmlrpclib
import testlink
import win32api
import psutil
import calendar
import logger
import requests
import json
server_ip='127.0.0.1'
server_port=9999
server_detail="无线自动化云端测试系统"
server_url = "http://dcn.testlink/lib/api/xmlrpc/v1/xmlrpc.php"
server_key = "6a2028c670368898490caa0c7d8f6ddb"
#c:\testlink_dcnrdc\\dcnrdc.exe //jobid
class DCNREMServer:
     def __init__(self, port):
        # 绑定服务器的ip地址和端口，注意以元组的形式
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("0.0.0.0", port))
        self.socket.listen(5)
        self.key = server_key
        print("正在监听 127.0.0.1 ：{}...".format(port))

     def tcplink(self, sock, addr):
        # 每次连接，开始前，先欢迎下。
        sock.send("你好，欢迎使用DCN自动化测试系统！".encode("utf-8"))
        sock.send(server_detail.encode("utf-8"))
        while True:
            data = sock.recv(1024).decode("utf-8")
            print(data)
            print(sock.getpeername())
            print(sock.getsockname())
            print(sock.fileno())
            username = data.split("::")[0]
            msg = data.split("::")[1]
            if msg == "exit":
                break
            if msg:
                print("【用户名"+username+"】接收任务的时间： "+time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
                print("aaaaaaaaaaaaaaaa")
                data1 = json.loads(msg)
                #转换为字典的格式
                jobid=data1['jobid']
                print("jobid是："+jobid)
                status=data1['status']
                print("status是：" + status)
                set_version= data1['trigger_build']
                print("测试的版本是：" + set_version)
                runtime = data1['runtime']
                print("测试时间是：" + runtime)
                test_time=self.string2sec(runtime)
                print("测试时间戳：" + str(test_time))
                current_time=int(time.time())
                print("当前时间戳：" + str(current_time))
                if test_time<=current_time:
                    print(" excuse the jobid")
                else:
                    print("wait for time excuse the jobid")
                response = self.get_response(msg)
                sock.send(response.encode("utf-8"))
        sock.close()
        print("与 {} 结束测试！".format(username))

     def get_response(self, info):

        """
        调用testlink xmlrpc API，获取jobid的信息
        """
        return "你发送的jobid是"+info

     def main(self):
        """
        主入口
        :return:
        """
        while True:
            sock, addr = self.socket.accept()
            t=threading.Thread(target=self.tcplink, args=(sock, addr))
            t.start()

     def kill_process_with_name(self,process_name):
         """
          create 20200319
         author sunguotao
         根据进程名杀死进程
         跨平台支持
         :param process_name: 进程名
         :return:
         """
         pid_list = psutil.pids()
         #print(pid_list)
         for pid in pid_list:
             try:
                 each_pro = psutil.Process(pid)
                 #print(each_pro.name())
                 if process_name.lower() in each_pro.name().lower():
                     #logger.info('find and kill %s' % process_name)
                     print(('find and kill %s' % process_name))
                     each_pro.terminate()
                     each_pro.wait(timeout=3)
             except Exception as error:
                 #psutil.NoSuchProcess, pid:
                 print(error)
                 print('没有此进程%s' % process_name)
                 pass

     def run_process_with_name(self,process_name):
         """
         create 20200319
         author sunguotao
         运行一个程序
         :param process_name: 程序名
         :return:
         """
         os.system(process_name)

     def get_current_time(self):
         """

         获取系统的当前时间
         :return:
         """
         ts = int(time.time())
         return ts

     def getversion(self,filename):
        """
        将文件转换为版本号
        :param filename: 升级的文件名
        :return: 版本号
        """
        firstlocal=filename.index('_')+1
        version=filename[firstlocal:]
        version=version.replace('.gz','')
        version = version.replace('.tar', '')
        version=version.strip().decode('utf-8')
        return version

     def string2sec(self,timestring):
         '''
         字符串时分秒转换成秒
         '''
         #timestring = '2020-03-28 23:40:00'
         timeArray = time.strptime(timestring, "%Y-%m-%d %H:%M:%S")
         timeStamp = int(time.mktime(timeArray))
         return timeStamp

     def find_newest_build_file(self,dir):
         '''
         查找目录下最新的版本文件
          dir = 'F:\\builds\\AP'
          find_new_file(dir)
         '''
         file_lists = os.listdir(dir)
         file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
         if not os.path.isdir(dir + "\\" + fn) else 0)
         print('AP最新的版本文件为： ' + file_lists[-1])
         file = os.path.join(dir, file_lists[-1])
         print('AP版本完整路径：', file)
         return file
     def build_exec(self,deviceid,build,job_deviceid,job_build):
         """
         根据版本来触发测试
         :return:
         """
         if deviceid== job_deviceid & build==job_build:
             #self.run_process_with_name('c:\testlink_dcnrdc\\dcnrdc.exe //jobid')
             os.system('c:\testlink_dcnrdc\\dcnrdc.exe //jobid')
         else:
             print('执行的版本不对，需要等待')


     def time_exec(self,jobid_time):
         """
         根据时间来触发测试
         :param time:
         :return:
         """
         current_time=int(time.time())
         if jobid_time<=current_time:
             #self.run_process_with_name('c:\testlink_dcnrdc\\dcnrdc.exe //jobid')
             os.system('c:\testlink_dcnrdc\\dcnrdc.exe //jobid')
         else:
             ts=current_time-jobid_time
             waittime=divmod(ts,60)
             print('执行时间未到，需要等待'+str(waittime))

     def exec_jobid(self,jobid):
         """
         获取jobid的信息
         :param jobid:
         :return:
         """



if __name__ == '__main__':
    cs = DCNREMServer(port=server_port)
    #tls = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
    #tls.countProjects()
    dir = 'F:\\builds\\ap'
    re=cs.find_newest_build_file(dir)
    print(re)
    cs.kill_process_with_name('FeiQ.exe')
    cs.main()

