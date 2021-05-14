import threading

class SingletonType(type):
    _instance_lock = threading.Lock()
    def __init__(self, *args, **kwargs):
        super(SingletonType, self).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):  # 这里的cls，即Foo类
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=SingletonType):  # 指定创建Foo的type为SingletonType
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)


obj1 = Foo('name')
obj2 = Foo('name')
print(obj1,obj2)
