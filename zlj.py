# -*- coding:utf-8 -*-
import re
text = ""
with open("wheelcipher.txt", "r", encoding="GBK") as f:
    text = f.read()
code = []
code = re.findall(r"<(.*)<", text)
# 匹配以< 开头，以> 结尾的所有字符串 ，且只保留括号内的内容

for i in range(len(code)):
    code[i] = code[i].strip()
# 移除首尾的空格
codetext = "NFQKSEVOQOFNP"

codenum = "2,3,7,5,13,12,9,1,8,10,4,11,6"
codenum = codenum.split(",")  # 把这些数字都弄到一个里面去

a = 0
print("解密后的：")
for i in codenum:
    # 将codenum代表第几个轮子，index(codetext[a])代表每个轮子以字母对应的位置为开头
    # N F Q K S  E  V O Q O  F N  P
    # 2 3 7 5 13 12 9 1 8 10 4 11 6
    # 如：KPBELNACZDTRXMJQOYHGVSFUWI =》NACZDTRXMJQOYHGVSFUWIKPBEL
    index = code[int(i) - 1].index(codetext[a])
    a = a + 1
    code[int(i) - 1] = code[int(i) - 1][index:] + code[int(i) - 1][:index]
    print(code[int(i) - 1])

print("下面是每一列")
for i in range(len(code[0])):
    str = ""
    print("第{}列的是:".format(i), end="")
    # 按codenum的顺序取字母
    for j in codenum:
        str += code[int(j) - 1][i]
    # 大写转小写
    print(str.lower())
