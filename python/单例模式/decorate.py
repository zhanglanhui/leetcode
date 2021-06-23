def singleton(cls):
    _instance = {}

    def getinstance(*args, **kw):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kw)
        return _instance[cls]

    return getinstance


@singleton
class MyClass(object):
    def __init__(self, *args, **kw):
        self.GG = [x for x in args]

    def getG(self):
        return self.GG


c1 = MyClass(1, doc=1)
c2 = MyClass(2, doc=3)


print(id(c1) == id(c2))
print(c2)
