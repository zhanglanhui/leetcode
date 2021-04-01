class Person:
    name = "aaa"


p1 = Person()
p2 = Person()
p1.name = "bbb"
print(p1.name)  # bbb
print(p2.name)  # aaa
print(Person.name)  # aaa


class Person1:
    name = []


p1 = Person1()
p2 = Person1()
p1.name.append(1)
print(p1.name)  # [1]
print(p2.name)  # [1]
print(Person1.name)  # [1]
