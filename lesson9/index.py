#內建的變數__name__
import tools

def main()->None:
    name = input("Please enter your name:")
    height = float(input("Please enter your height(cm):"))
    weight = float(input("Please enter your weight(kg):"))
    print(f"Your name is {name}")
    print(f"Your height is {height} cm")
    print(f"Your weight is {weight} kg")
    bmi=tools.cal_bmi(height,weight)
    rate=tools.get_status(bmi)
    print(f"Your BMI value is {round(bmi,ndigits = 2)}")
    print(f"Your BMI range is {rate}.")

if __name__ == '__main__':
    '''
    print("被python執行的主程式")
    print(__name__)
    print(type(__name__))
    '''
    main()

