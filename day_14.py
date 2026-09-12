# decorators
# add additional features to an existing function

# def div(a,b):
#     print(a/b)

# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inner

# div1 = smart_div(div)
# div1(2,4)


# def hello_name(s):
#     print(s)


# def smart_hello(func):
#     def inner(s):
#         s1 = s.upper()
#         return func(s1)
#     return inner

# fun1 = smart_hello(hello_name)
# fun1('hello')


# def upper_decor(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper

# @upper_decor
# def hello_name():
#     return 'hello'

# print(hello_name())
# f = upper_decor(hello_name)
# print(f())
# print(upper_decor(hello_name)())



#generators

# def gen():
#     yield 1
#     yield 3
#     yield 4
#     yield 10
# num = gen()
# for i in num:
#     print(i)


def sqr_gen():
   for i in range(1,11):m
       yield i

sqr = sqr_gen()
for i in sqr:
    print(i*i)m





