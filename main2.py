# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
# print(factorial(5))

# def factorial2(x):
#     total = 5
#     for i in reversed(range(x)):
#        if(i > 0):
#         total *= i 
#     return total
# print(factorial2(5))



# def print_exception_tree(thisclass, nest = 0):
#     if nest > 1:
#         print("   |" * (nest - 1), end="")
#     if nest > 0:
#         print("   +---", end="")

#     print(thisclass.__name__)

#     for subclass in thisclass.__subclasses__():
#         print_exception_tree(subclass, nest + 1)


# print_exception_tree(BaseException)

# try:
#     raise Exception(1,2,3)
# except Exception as e:
#     print(len(e.args))

# class i:
#     def __init__(self):
#         self.s ='abc'
#         self.i = 0

#     def __iter__(self):
#         return self

#     def __next__(self) :
#         if self.i == len(self.s):
#             raise StopIteration
#         v = self.s[self.i]
#         self.i += 1
#         return v

# for x in i():
#     print(x, end='')    

# class A:

#     def __str__(self):
#         return 'a'    
# class B(A):    
#     def __str__(self):
#         return 'b'   
# class C(B):
#         pass    

# o = C()
# print(o)


# class A :
#     def __init__(self, v=1):
#         self.v =v 

#     def set(self, v):
#         self.v = v
#         return v

# a = A()
# print(a.set(a.v +1))      

# class A : 
#     def __init__(self,v) :
#         self.__a = v +1  
# a = A(0)
# print(a.__a)        

# class A:
#     x =0
#     def __init__(self, v=0) :
#         self.Y =v
#         A.x += v

# a = A()
# b = A(1)
# c =A(2)
# print(c.x) 


# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass  

# print(issubclass(C, A))

# class A :
#     def a(self):
#         print('a')

# class B :
#     def a(self):
#         print('b') 


# class C(B,A) :
#     def c(self):
#         self.a()              

# o =C()
# o.c()

# def f(x):
#     try:
#         x = x/x
#     except:
#         print('a', end='') 
#     else:
#         print('b', end='')
#     finally:
#         print('c',end='') 
# f(1)
# f(0)       


# class EX(Exception):
#     def __init__(self, msg) :
#         Exception.__init__(self, msg + msg)
#         self.args= (msg,)

# try:
#     raise EX('ex')
# except EX as e:
#     print(e)

# except Exception as e:
#     print(e)


the_list = []

for x in range(2):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)
