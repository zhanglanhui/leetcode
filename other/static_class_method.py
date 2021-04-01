class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


x = "xx"
a = A()
a.foo(x)
a.class_foo(x)
a.static_foo(x)

print("----------------------")
A.foo(a, "ss")
A.class_foo(x)
A.static_foo(x)
