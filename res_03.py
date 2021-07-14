from Crypto.PublicKey import RSA

n = 87924348264132406875276140514499937145050893665602592992418171647042491658461
e = 65537
d = 10866948760844599168252082612378495977388271279679231539839049698621994994673

prikey = RSA.construct((n, e, d), False)

with open('prikey.pem', 'wb') as f:
    key = prikey.export_key()
    print(key)
    f.write(key)
# with open('prikey.pem', 'w') as f:
#    key = prikey.export_key().decode('utf-8')
#    print(key)
#    f.write(key)
