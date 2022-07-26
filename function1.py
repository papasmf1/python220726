# function1.py 
#1)함수를 정의
def setValue(newValue):
    x = newValue
    print("내부에서 출력:", x)

#2)함수를 호출
retValue = setValue(5)
print(retValue)

#다중의 값을 리턴
def swap(x,y):
    return y,x 

#호출
result = swap(3,4)
print(result[0])
print(result[1])

#교집합 문자를 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #x라는 글자가 postlist에 있고 
        #그리고 x가 result에 포함되어있지 않다면
        if x in postlist and x not in result:
            result.append(x)
    return result 

#함수 호출
print(intersect("HAM","SPAM"))
