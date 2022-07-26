# function2.py
print("---불변형---")
a = 1.2
print(id(a))
a = 2.3 
print(id(a))

print("---가변형---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))
