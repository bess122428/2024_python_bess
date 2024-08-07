#內建的變數__name__
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

def main()->None:
    name = input("Please enter your name:")
    height = float(input("Please enter your height(cm):"))
    weight = float(input("Please enter your weight(kg):"))
    print(f"Your name is {name}")
    print(f"Your height is {height} cm")
    print(f"Your weight is {weight} kg")
    bmi=cal_bmi(height,weight)
    rate=get_status(bmi)
    print(f"Your BMI value is {round(bmi,ndigits = 2)}")
    print(f"Your BMI range is {rate}.")

if __name__ == '__main__':
    '''
    print("被python執行的主程式")
    print(__name__)
    print(type(__name__))
    '''
    main()

