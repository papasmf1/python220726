# DemoFile2.py 
#파일 쓰기(raw string notation)
f = open(r"c:\work\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close() 

#파일을 읽기
f = open("c:/work/demo.txt", "rt", encoding="utf-8")
#print(f.read())
#리스트에 담기 
lst = f.readlines()
print(lst)
f.close()

for item in lst:
    print(item)



