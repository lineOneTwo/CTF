# coding:utf-8
with open('1.txt', 'r') as fp:
    date = fp.readlines()
    print(type(date))
word = ''.join(date)
# print(str)
cap_chars = ''
for char in word:
    if char.isupper():
        cap_chars += char
print(cap_chars)
