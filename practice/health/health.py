class BMI():
    def __init__(self,n:str,h:float,w:float):
        self.__name = n
        self.__height = h
        self.__weight = w
        
    @property
    def name(self)->str:
        return self.__name
    @property
    def height(self)-> float:
        return self.__height
    @property
    def weight(self)->float:
        return self.__weight
    
    @classmethod
    def bmi(cls,height:float,weight:float)->float:
        bmi:float = weight/(height/100)**2
        return bmi
    @classmethod
    def status(cls,bmi:float)->str:
        if bmi < 18.5:
            rate = "體重過輕!"
        elif bmi < 24:
            rate = "體重正常!"
        elif bmi < 27:
            rate = "體重過重!"
        elif bmi < 30:
            rate = "輕度肥胖!"
        elif bmi <35:
            rate = "重度肥胖!"
        else:
            rate = "重度肥胖!"
            
        return rate
        