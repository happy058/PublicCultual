# encoding=utf-8
import requests
import unittest
import json
class MemberQueryTest(unittest.TestCase):
    def setUp(self):
        self.baser_url = "http://test.spider.com.cn:8001/selfmark-web/member/delete"
        #self.auth_user = ('20161226135545','','selfmark')
       # self.auth_user = ()
    def tearDown(self):
        print(self.result)

    def test_member_delete_success(self):
        '''查询成功'''
        payload = {'reqbase':{'timestamp':'20161226135545','token':'3B51BDAADC4F17909B49EB2EC7645ED4','clientauthflag':'','reqorigin':'selfmark'},
                  'reqparam':{'count':'true','page':'1','order':''},'reqparam':{'id':'58e757b8e4b050d3947b8657'}}
        headers = {'Content-Type': 'application/json'}

        data_json = json.dumps(payload,indent=2)
        #data_json = json.loads(payload)
       #data_json = payload.json()

        r = requests.post(self.baser_url,headers=headers,data=data_json)
        self.result = r.json()
        #self.assertEqual(result['status'],true)
        self.assertEqual(self.result['respbase']['returncode'], '10000')
        #self.assertEqual(self.result['respparam']['mobile'], '18591406352')

if __name__ == '__main__':
   # test_data.init_data()
    unittest.main()