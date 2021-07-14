from Crypto.PublicKey import RSA

with open('key.pem', 'r') as f:
    key = f.read()
    pubkey = RSA.import_key(key)

print('n:', pubkey.n)
print('e:', pubkey.e)
# 解析pubkey.pem文件
