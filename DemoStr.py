# DemoStr.py
#print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.upper())
print(strA.lower())
print(strA.count("p"))
print(strA.count("p", 7))
print(strA.startswith("py"))
print(strA.endswith("ful"))

#고객 명단
names = ["전우치","이순신","김유신"]
for name in names:
    print("안녕하세요 {0}님 더운 여름입니다.".format(name))
    print("=" * 40)


