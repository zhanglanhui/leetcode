# 装饰器就是把其他函数作为参数的函数
def my_new_decorator(xxx):
    # 在函数里面,装饰器在运行中定义函数: 包装.
    # 这个函数将被包装在原始函数的外面,所以可以在原始函数之前和之后执行其他代码..
    def the_wrapper_function():
        # 把要在原始函数被调用前的代码放在这里
        print("Before the function runs")

        # 调用原始函数(用括号)
        xxx()

        # 把要在原始函数调用后的代码放在这里
        print("After the function runs")

    # 在这里"a_function_to_decorate" 函数永远不会被执行
    # 在这里返回刚才包装过的函数
    # 在包装函数里包含要在原始函数前后执行的代码.
    return the_wrapper_function


# 加入你建了个函数,不想修改了
def a_stand_alone_function():
    print("I am a stand alone function, don't you dare modify me")


# a_stand_alone_function()
# 输出: I am a stand alone function, don't you dare modify me

# 现在,你可以装饰它来增加它的功能
# 把它传递给装饰器,它就会返回一个被包装过的函数.

# a_function_decorated = my_new_decorator(a_stand_alone_function)
# # 执行
# a_function_decorated()
# # 输出s:
# # Before the function runs
# # I am a stand alone function, don't you dare modify me
# # After the function runs


@my_new_decorator
def another_stand_alone_function():
    print("Leave me alone")

another_stand_alone_function()