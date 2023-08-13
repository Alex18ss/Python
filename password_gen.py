import random


def randpass(a):
    stri = "`qwertyuiop[]a\sdfghjkl;'zxcvbnm,./1234567890-=!@#$%^&*()_+{}?><:QWERTYUIOPASDFGHJKLZXCVBNM"
    password = ''
    for i in range(a):
        g = random.choice(stri)
        password += g
    print(password)


randpass(100)
