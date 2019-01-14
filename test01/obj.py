class Student:
    pass

class MyStudent(Student):
    pass

print(type(MyStudent))
print(type(Student))

print(MyStudent.__bases__)
print(Student.__bases__)

#type的基类是object ， object的基类是空
print(type.__bases__)
print(object.__bases__)