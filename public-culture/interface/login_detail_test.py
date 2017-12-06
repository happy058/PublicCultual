# encoding=utf-8
import requests
import unittest
import json


class MemberAddTest(unittest.TestCase):

    def setUp(self):
        self.baser_url = "http://192.168.1.234:8256/user/detail"
        #self.auth_user = ('20161226135545','','selfmark')
       # self.auth_user = ()

    def tearDown(self):
        print(self.result)
    def test_login_detail_success(self):
        '''查询详情正确'''
        payload = {'reqbase':{'timestamp':'20161226135545','token':'2c960363b72886024086324d59094c07','clientauthflag':'','reqorigin':'selfmark'},
                  'reqparam':{'userId':'4e515b0fca06aab0743d60f9896aa605'}}
        headers = {'Content-Type': 'application/json'}

        data_json = json.dumps(payload,indent=2)
        #data_json = json.loads(payload)
       #data_json = payload.json()

        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(result['status'],true)
        self.assertEqual(self.result['respbase']['returncode'], '10000')
        self.assertEqual(self.result['respbase']['returnmsg'], '成功')

    def test_login_detail_false1(self):
        '''不传userId字段'''
        payload = {'reqbase':{'timestamp':'20161226135545','token':'2c960363b72886024086324d59094c07','clientauthflag':'','reqorigin':'selfmark'},
                  'reqparam':{}}
        headers = {'Content-Type': 'application/json'}
        data_json = json.dumps(payload,indent=2)
        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(result['status'],true)
        self.assertEqual(self.result['respbase']['returncode'], '21001')
        self.assertEqual(self.result['respbase']['returnmsg'], '必要参数为空')
    def test_login_detail_false2(self):
        '''userId为空'''
        payload = {'reqbase':{'timestamp':'20161226135545','token':'2c960363b72886024086324d59094c07','clientauthflag':'','reqorigin':'selfmark'},
                  'reqparam':{'userId':''}}
        headers = {'Content-Type': 'application/json'}
        data_json = json.dumps(payload,indent=2)

        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(result['status'],true)
        self.assertEqual(self.result['respbase']['returncode'], '21001')
        self.assertEqual(self.result['respbase']['returnmsg'], '必要参数为空')

    def test_login_detail_error(self):
        '''userId错误'''
        payload = {'reqbase':{'timestamp':'20161226135545','token':'2c960363b72886024086324d59094c07','clientauthflag':'','reqorigin':'selfmark'},
                  'reqparam':{'userId':'dkkdkdkd384848384kdfjdj#444ijjjj'}}
        headers = {'Content-Type': 'application/json'}
        data_json = json.dumps(payload,indent=2)

        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(result['status'],true)
        self.assertEqual(self.result['respbase']['returncode'], '20001')
        self.assertEqual(self.result['respbase']['returnmsg'], '抱歉,系统繁忙,请稍后重试.')

if __name__ == '__main__':
   # test_data.init_data()
    unittest.main()