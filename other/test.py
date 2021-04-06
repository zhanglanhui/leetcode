# # i = 0
# for i in range(0, 5):
#     print("aaaa",i)
#     i += 10
#     print("bbbb",i)

# import random
# alist = [1,2,3,4,5]
# def randoms():
#     return 0.2
# random.shuffle(alist,randoms)
# print(alist)


a = [1, 2, 3, [4, 5, 6]]
b = a[:] # 与copy作用相同
b[3].append(7)
print("a:", a)
print("b:", b)
print("--------------------")
b.append(8)
print("a:", a)
print("b:", b)
