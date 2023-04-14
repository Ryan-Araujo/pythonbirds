def f():
    raise TypeError
    print('Nao foi executado')
try:
    f()
except TypeError:
    print('type error tratado')