#常數必須用大寫
PI = 3.1415926

#自訂的function
def cal_bmi(height:float,weight:float) -> float:
    bmi:float=weight/(height/100)**2
    return bmi

def get_status(bmi:float)->str:
    if bmi < 18.5:
        rate = "UnderWeight!"
    elif bmi < 24:
        rate = "Normal Weight!"
    elif bmi < 27:
        rate = "Too Heavy!"
    elif bmi < 30:
        rate = "Mild Obesity!"
    elif bmi < 35:
        rate = "Moderately Obese!"
    else:
        rate = "Severe Obesity!"
        
    return rate

#建立實體的attribute(屬性)
class Person():
    def __init__(self,n:str): #自訂的init
        self.name = n

    def __repr__(self) -> str:
        return f'我的名字叫{self.name}'
    
#繼承-實體的method()
class Student(Person):
    def __init__(self,n:str,ch:int,en:int,ma:int):
        super().__init__(n) #執行父類別的init
        self.__chinese = ch
        self.__english = en
        self.__math = ma


    @property
    def chinese(self) -> int:
        return self.__chinese
    
    @property
    def english(self) -> int:
        return self.__english
    
    @property
    def math(self) -> int:
        return self.__math
    
    def __repr__(self)-> str:
        message:str = super().__repr__() 
        message += "\n我是一個學生"
        return message
    
    def sum(self)->int:#實體的method
        return self.chinese+self.english+self.math
    
    def average(self)->float:#實體的method
        return round(self.sum()/3.0,ndigits=2)
    
def get_student(name:str,chinese:int,english:int,math:int)->Student:
    return Student(n=name,ch=chinese,en=english,ma=math)