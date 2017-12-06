# encoding=utf-8
import requests
import unittest
import json


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.baser_url = "http://192.168.1.234:8256/user/login"
        #self.auth_user = ('20161226135545','','selfmark')
       # self.auth_user = ()
    def tearDown(self):
        print(self.result)

    def test_login_success(self):
        '''登录成功'''
        payload = {'reqbase': {'timestamp': '20161226135545', 'token': '2c960363b72886024086324d59094c07',
                               'clientauthflag': '', 'reqorigin': 'selfmark'},
                   'reqparam': {'username': 'sandy','password': '123123'}}
        headers = {'Content-Type': 'application/json'}

        data_json = json.dumps(payload,indent=2) #将数据转换成字符串
        #data_json = json.loads(payload)
       #data_json = payload.json()

        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(self.result['status'],'true')
        self.assertEqual(self.result['respbase']['returncode'], '10000')
        self.assertEqual(self.result['respparam']['username'], 'sandy')
    def test_login_username_null(self):
        '''不传用户名字段'''
        payload = {'reqbase': {'timestamp': '20161226135545', 'token': '2c960363b72886024086324d59094c07',
                               'clientauthflag': '', 'reqorigin': 'selfmark'},
                   'reqparam': {'password': '123123'}}
        headers = {'Content-Type': 'application/json'}

        data_json = json.dumps(payload,indent=2) #将数据转换成字符串
        #data_json = json.loads(payload)
       #data_json = payload.json()

        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(self.result['status'],'true')
        self.assertEqual(self.result['respbase']['returncode'], '21001')
        self.assertEqual(self.result['respbase']['returnmsg'], '必要参数为空')
    def test_login_username_empty(self):
        '''用户名为空'''
        payload = {'reqbase': {'timestamp': '20161226135545', 'token': '2c960363b72886024086324d59094c07',
                               'clientauthflag': '', 'reqorigin': 'selfmark'},
                   'reqparam': {"username": "",'password': '123123'}}
        headers = {'Content-Type': 'application/json'}

        data_json = json.dumps(payload,indent=2) #将数据转换成字符串
        #data_json = json.loads(payload)
       #data_json = payload.json()

        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(self.result['status'],'true')
        self.assertEqual(self.result['respbase']['returncode'], '21001')
        self.assertEqual(self.result['respbase']['returnmsg'], '必要参数为空')
    def test_login_username_error(self):
        '''用户错误'''
        payload = {'reqbase': {'timestamp': '20161226135545', 'token': '2c960363b72886024086324d59094c07',
                               'clientauthflag': '', 'reqorigin': 'selfmark'},
                   'reqparam': {'username': 'test2','password': '123123'}}
        headers = {'Content-Type': 'application/json'}

        data_json = json.dumps(payload,indent=2) #将数据转换成字符串
        #data_json = json.loads(payload)
       #data_json = payload.json()

        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(self.result['status'],'true')
        self.assertEqual(self.result['respbase']['returncode'], '20000')
        self.assertEqual(self.result['respbase']['returnmsg'], '用户名或密码错误，请重新输入！')
    def test_login_password_null(self):
        '''不传password字段'''
        payload = {'reqbase': {'timestamp': '20161226135545', 'token': '2c960363b72886024086324d59094c07',
                               'clientauthflag': '', 'reqorigin': 'selfmark'},
                   'reqparam': {'username':'test1'}}
        headers = {'Content-Type': 'application/json'}

        data_json = json.dumps(payload,indent=2) #将数据转换成字符串
        #data_json = json.loads(payload)
       #data_json = payload.json()

        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(self.result['status'],'true')
        self.assertEqual(self.result['respbase']['returncode'], '21001')
        self.assertEqual(self.result['respbase']['returnmsg'], '必要参数为空')
    def test_login_password_empty(self):
        '''password为空'''
        payload = {'reqbase': {'timestamp': '20161226135545', 'token': '2c960363b72886024086324d59094c07',
                               'clientauthflag': '', 'reqorigin': 'selfmark'},
                   'reqparam': {"username": "",'password': ''}}
        headers = {'Content-Type': 'application/json'}

        data_json = json.dumps(payload,indent=2) #将数据转换成字符串
        #data_json = json.loads(payload)
       #data_json = payload.json()

        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(self.result['status'],'true')
        self.assertEqual(self.result['respbase']['returncode'], '21001')
        self.assertEqual(self.result['respbase']['returnmsg'], '必要参数为空')
    def test_login_password_error(self):
        '''密码错误'''
        payload = {'reqbase': {'timestamp': '20161226135545', 'token': '2c960363b72886024086324d59094c07',
                               'clientauthflag': '', 'reqorigin': 'selfmark'},
                   'reqparam': {'username': 'test1','password': 'abcabc'}}
        headers = {'Content-Type': 'application/json'}

        data_json = json.dumps(payload,indent=2) #将数据转换成字符串
        #data_json = json.loads(payload)
       #data_json = payload.json()

        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(self.result['status'],'true')
        self.assertEqual(self.result['respbase']['returncode'], '20000')
        self.assertEqual(self.result['respbase']['returnmsg'], '用户名或密码错误，请重新输入！')

if __name__ == '__main__':
    #test_data.init_data()
    unittest.main()