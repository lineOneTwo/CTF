import hashlib

filename = '/fllllllllllllag'
cookie_secret ="6bf4f17e-9216-460c-a1e7-d359938ade06"

def getvalue(string):
    md5 = hashlib.md5()
    md5.update(string.encode('utf-8'))
    print(md5.hexdigest())
    return md5.hexdigest()

def merge():
    print(getvalue(cookie_secret + getvalue(filename)))

merge()
