# encoding=utf-8
import requests
import unittest
import json
class MemberQueryTest(unittest.TestCase):
    def setUp(self):
        self.baser_url = "http://test.spider.com.cn:8001/selfmark-web/member/qrymembers"
        #self.auth_user = ('20161226135545','','selfmark')
       # self.auth_user = ()
    def tearDown(self):
        print(self.result)

    def test_member_query_success(self):
        '''查询成功'''
        payload = {'reqbase':{'timestamp':'20161226135545','token':'783A81500600B28D5B51CF0B7FC2B086','clientauthflag':'','reqorigin':'selfmark'},
                  'reqparam':{'count':'true','page':'1','order':''},'reqparam':{'merchantid':'3'}}
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