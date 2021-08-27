from Crypto.PublicKey import RSA

with open('publickey2.pem', 'r') as f:
    key = f.read()
    pubkey = RSA.import_key(key)

print('n:', pubkey.n)
print('e:', pubkey.e)
# 解析pubkey.pem文件
