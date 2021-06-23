class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    a = 1

    def __init__(self, *args, **kw):
        self.GG = [x for x in args]

    def getG(self):
        return self.GG


c1 = MyClass()
c2 = MyClass()

print(id(c1) == id(c2))
# print(c2.GG)
