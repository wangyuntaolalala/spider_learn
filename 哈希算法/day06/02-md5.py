import hashlib

def md5_test2():
    md5 = hashlib.md5()
    md5.update('123123123'.encode('utf-8'))
    print(md5.hexdigest())  # c4ca4238a0b923820dcc509a6f75849b

def sha1_test2():
    sha1 = hashlib.sha512()
    sha1.update('1'.encode('utf-8'))
    print(sha1.hexdigest())


if __name__ == '__main__':
    md5_test2()
    sha1_test2()

