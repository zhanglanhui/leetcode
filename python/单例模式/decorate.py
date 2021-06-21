def singleton(cls):
    _instance = {}

    def getinstance(*args, **kw):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kw)
        return _instance[cls]

    return getinstance


@singleton
class MyClass(object):
    def __init__(self):
        pass


c1 = MyClass()
c2 = MyClass()

print(id(c1) == id(c2))
