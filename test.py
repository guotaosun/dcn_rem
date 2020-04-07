#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Testlink API Sample Python Client implementation
"""
import xmlrpclib
#import os
import win32api
class TestlinkAPIClient:
    # substitute your server URL Here
    SERVER_URL = "http://dcn.testlink/lib/api/xmlrpc/v1/xmlrpc.php"
    #SERVER_URL = "http://192.168.60.60/lib/api/xmlrpc/v1/xmlrpc.php"
    #global jobid
    global devKey
    global args
    global args_sub
    global jobid
    global data
    devKey = "6a2028c670368898490caa0c7d8f6ddb"
    jobid = "zhangjxp1542693112"
    args1={ 'testplanid': '64743','buildname': '7.0.3.5(R0217.0171)',  'buildnotes': 'S3026TSconfig'}
    args_sub='show version\n  S3026TS Device, Compiled on Aug 10 16:54:09 2018\n  sysLocation \xc9\xee\xdb\xda\xca\xd0\xc4\xcf\xc9\xbd\xc7\xf8\xbf\xc6\xbc\xbc\xd4\xb0\xb1\xb1\xc7\xf8\xd0\xc2\xce\xf7\xc2\xb75\xba\xc5\xd2\xf8\xba\xd3\xb7\xe7\xd4\xc6\xb4\xf3\xcf\xc3\n  CPU Mac 00:03:0f:aa:01:14\n  Vlan MAC 00:03:0f:aa:01:13\n  SoftWare Version 7.0.3.5(R0217.0171)\n  BootRom Version 7.1.3\n  HardWare Version N/A\n  CPLD Version N/A\n  Serial No.:N/A\n  Copyright (C) 2001-2018 by Galaxywind Limited.\n  All rights reserved\n  Last reboot is warm reset.\n  Uptime is 0 weeks, 0 days, 16 hours, 11 minutes\nS3026TS(config)#'
    args_sub=args_sub.decode('gb2312');
    args_sub=args_sub.encode('utf-8');
    args3={'buildname': '7.0.3.5(R0217.0171)', 'testplanid': '64743', 'devKey': '7b6bb5bf0c0544699a5513007dcddff7', 'buildnotes': 'show version\n  S3026TS Device, Compiled on Aug 10 16:54:09 2018\n  sysLocation \xc9\xee\xdb\xda\xca\xd0\xc4\xcf\xc9\xbd\xc7\xf8\xbf\xc6\xbc\xbc\xd4\xb0\xb1\xb1\xc7\xf8\xd0\xc2\xce\xf7\xc2\xb75\xba\xc5\xd2\xf8\xba\xd3\xb7\xe7\xd4\xc6\xb4\xf3\xcf\xc3\n  CPU Mac 00:03:0f:aa:01:14\n  Vlan MAC 00:03:0f:aa:01:13\n  SoftWare Version 7.0.3.5(R0217.0171)\n  BootRom Version 7.1.3\n  HardWare Version N/A\n  CPLD Version N/A\n  Serial No.:N/A\n  Copyright (C) 2001-2018 by Galaxywind Limited.\n  All rights reserved\n  Last reboot is warm reset.\n  Uptime is 0 weeks, 0 days, 16 hours, 11 minutes\nS3026TS(config)#'}
    args4={'buildname': '7.0.3.5(R0217.0171)', 'testplanid': '64743', 'devKey': '7b6bb5bf0c0544699a5513007dcddff7', 'buildnotes': args_sub}

    args5 = {'devKey':devKey,'testSuite': '\xe7\xa1\xae\xe8\xae\xa4\xe6\xb5\x8b\xe8\xaf\x952.0', 'productLine': '\xe4\xba\xa4\xe6\x8d\xa2\xe6\x9c\xba\xe4\xba\xa7\xe5\x93\x81\xe7\xba\xbf', 'testPlan': 'Aftersale-TSC RD043', 'testDevice': 'TSC-RD043-Carat5522-250', 'aftersaleVersion': '', 'scriptVersion': '', 'user': 'wujpd', 'continue_mode': '0', 'robot_path': 'E:\\Autotest\\Robot', 'aftersaleFlag': '0', 'stack': '0', 'overwrite': '0', 'result': 'p', 'testCase': '4.1.1_rocket', 'job_id': 'wujpd1536145170', 'notes': '', 'testBuild': '7.0.3.1(R0115.0039)'}

    args6 = {
            'devKey': devKey,
            'testSuite': '\xe7\xa1\xae\xe8\xae\xa4\xe6\xb5\x8b\xe8\xaf\x952.0',
            'productLine': '\xe4\xba\xa4\xe6\x8d\xa2\xe6\x9c\xba\xe4\xba\xa7\xe5\x93\x81\xe7\xba\xbf',
            'testPlan': 'Aftersale-TSC RD043',
            'testDevice': 'TSC-RD043-Carat5522-250',
            'aftersaleVersion': '',
            'scriptVersion': '',
            'user': 'wujpd',
            'continue_mode': '0',
            'robot_path': 'E:\\Autotest\\Robot',
            'aftersaleFlag': '0',
            'stack': '0',
            'overwrite': '0',
            'result': 'p',
            'testCase': '4.1.1_rocket',
            'job_id': 'wujpd1536145170',
            'notes': '',
            'testBuild': '7.0.3.1(R0115.0039)'
            }

    args7={'testSuite': '\xe7\xa1\xae\xe8\xae\xa4\xe6\xb5\x8b\xe8\xaf\x952.0', 'productLine': '\xe4\xba\xa4\xe6\x8d\xa2\xe6\x9c\xba\xe4\xba\xa7\xe5\x93\x81\xe7\xba\xbf', 'testPlan': 'Aftersale-6200', 'testDevice': 'CS6200-28X-HI-24F-266__Code_Ivy7.5_Helix4', 'aftersaleVersion': '', 'scriptVersion': '', 'user': 'wujpd', 'continue_mode': '0', 'robot_path': 'E:\\Autotest_trunk\\Robot', 'aftersaleFlag': '0', 'stack': '0', 'overwrite': '0', 'result': 'p', 'testCase': '4.1.1', 'job_id': 'wujpd1536140123', 'notes': '', 'testBuild': '7.5.3.0(R0010.0177)'}
    args8 = {'devKey': devKey,
            'productlinename': '\xe4\xba\xa4\xe6\x8d\xa2\xe6\x9c\xba\xe4\xba\xa7\xe5\x93\x81\xe7\xba\xbf',
            'testplanname': 'switch-Bluelake-20180930',
            'testcasename':'4.1.1'
            }
    args9 = {'testSuite': 'Am',
            'productLine': '\xe4\xba\xa4\xe6\x8d\xa2\xe6\x9c\xba\xe4\xba\xa7\xe5\x93\x81\xe7\xba\xbf',
            'testPlan': 'switch-Marvell-Bluelake-20180930',
            'testDevice': 'BlueLake-CS6200-52X-EI(V2)-362',
            'aftersaleVersion': '',
            'scriptVersion': '',
            'user': 'sungt',
            'continue_mode': '0',
            'robot_path': 'E:\\Autotest_trunk\\Robot',
            'aftersaleFlag': '0',
            'stack': '0',
            'overwrite': '1',
            'result': 'P',
            'testCase': '5.2.1',
            'job_id': jobid,
            'notes': 'sunguotao checked',
            'testBuild': '7.5.3.0(R0010.0184)'
            }
    args10 ={
    'devKey': devKey,
    'job_id': jobid,
    'productlinename': '交换机产品线',
    'stack': '0',
    'user' : 'zhangjxp',
    'status': 'p',
    'overwrite' : '0',
    'notes': '0',
    'platformid': '488',
    'testcaseid': '8996',
   'testsuiteid': '66666',
    'testplanid': '123673',
    'buildnotes': 'test',
    'buildid': '16698',
              }
    args = {
        'devKey': devKey,
        'job_id': jobid,
        'testsuiteid': '11179',
        'exe_time': '1000',
    }
    data1 = {
        'devKey': devKey,
        'productlinename': '交换机产品线',
        'testsuitename': 'Arm',
        'testcasename': '5.2.4.1',
    }

    data = {"devKey": devKey, 'productlinename':'交换机产品线', "testcasename": '5.2.1', "testsuitename": 'Am'}
    def __init__(self, devKey):
        self.server = xmlrpclib.Server(self.SERVER_URL)
        self.devKey = devKey
        print "devKey in init: %s" %devKey


    def getTestCaseIDByName(self, args):
        return self.server.tl.getTestCaseIDByName(args)

    def getTestCaseIDByName2(self, args):
        data = {"devKey": devKey, "testcasename": "4.1.1", "testsuitename": "5119"}
        return self.server.tl.getTestCaseIDByName(data)


    def reportTCResult_back(self, tcid, tpid, status):
        data = {"devKey":self.devKey, "tcid":tcid, "tpid":tpid, "status":status}
        return self.server.tl.reportTCResult(data)

    def reportTCResult(self,args):
        return self.server.tl.reportTCResult(args)

    def reportSuiteTime(self, args):
        return self.server.tl.reportSuiteTime(args)

    def reportTCResult1(self,args):
        return self.server.tl.reportTCResult1(args)

    def getInfo(self):
        return self.server.tl.about()

    def sayHello (self):
        return self.server.tl.sayHello()
    def getJobCases (self,jobid,status):
        data = {"devKey":self.devKey,"jobid":jobid,"status":status}
        return self.server.tl.getJobCases(data)
    def createBuild (self,args):

        return self.server.tl.createBuild(args)
    def getProjects (self, devKey):
        print "DevKey: %s" %devKey
        data = {"jobid":devKey}
        return self.server.tl.getProjects(data)

    def getJobEnv (self,jobid):
        data = {"devKey":self.devKey,"jobid":jobid}
        return self.server.tl.getJobEnv(data)

    def createBuild(self,testPlanID,buildNam,buildNotes):
        data = {"devKey": self.devKey, "testplanid":testPlanID,"buildname":buildNam,"buildnotes":buildNotes}
        return self.server.tl.createBuild(data)

    def getTestPlanByName(self,args):
        return self.server.tl.getTestCaseIDByName(args)

#productlinename, testsuitename, testcasename, testplanname, buildname, devicetype,result, user, overwrite=0, notes=',
    def reportTestResult(self, args):
        productlinename = args['productLine'].decode('utf8')
        testsuitename = args['testSuite']
        testcasename = args['testCase'].decode('utf8')
        testplanname = args['testPlan'].decode('utf8')
        buildname = args['testBuild'].decode('utf8')
        devicetype = args['testDevice'].decode('utf8')
        result = args['result']
        stack = args['stack']
        user = args['user']
        overwrite = args['overwrite']
        notes = args['notes'].decode('utf8')
        data = {"devKey": self.devKey, "testcasename": testcasename, "testsuitename": testsuitename, "testcasename1": user}
        testcase=self.getTestCaseIDByName(data)
        testcaseid = testcase[0].get('id')
        testsuiteid = testcase[0].get('parent_id')
        data2 = {"devKey": self.devKey, "productlinename": productlinename, "testplanname": testplanname,}
        testplanid = self.getTestPlanByName(data2)[0].get('id')
        buildnotes = ''
        buildid = self.createBuild(testplanid, buildname, buildnotes)[0].get('id')
        testlinkargs = {'devKey': self.devKey,
                   'job_id': jobid,
                   'testcaseid': testcaseid,
                   'testplanid': testplanid,
                   'testsuiteid': testsuiteid,
                   'status': result,
                   'buildid': buildid,
                   'stack': stack,
                   'notes': notes,
                   'platformname': devicetype,
                   'user': user,
                   'overwrite': overwrite
                     }
        return self.server.tl.reportTCResult(testlinkargs)



if __name__ == '__main__':

    # substitute your Dev Key Here
    client = TestlinkAPIClient (devKey)
    # get info about the server
    #print client.getInfo()
    #retval = client.createBuild(args)
    #retval = client.sayHello()
    #retval = client.getJobCases(jobid,0)
    #retval = client.getJobEnv(jobid)
    #retval = client.getProjects(devKey)
    #retval = client.getTestCaseIDByName(devKey)
    #os.system('c://testlink_dcnrdc//dcnrdc.exe jobid')
    #retval = client.getTestPlanByName(args)
    #retval = client.reportTestResult(args)
    #retval = client.getTestCaseIDByName(args)
    #retval = client.getTestCaseIDByName(args)
    #retval = client.reportTestResult(args)
    #retval  = client.getTestCaseIDByName(data)
    #retval = client.reportTCResult(args)
    retval = client.reportSuiteTime(args)
    print 'retval: ',  retval
   #win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 0)
   #win32api.ShellExecute(0, 'open', 'dcnrdc://huangmsa1533804649', '','',1)


