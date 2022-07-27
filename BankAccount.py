# BankAccount.py
#은행의 계정을 표현한 클래스 
class BankAccount:
    #대부분의 경우 내가 원하는 값으로 초기화 
    def __init__(self, id, name, balance):
        #이름숨김(이름변경)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    #인스턴스의 문자열을 요구하면 자동 호출 
    #ctrl + / 
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
#print(account1.__balance)
#변경된 이름 
print(account1._BankAccount__balance)
print(account1)



