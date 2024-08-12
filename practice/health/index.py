from health import BMI
import pyinputplus as pipy

def main()->None:
    name = pipy.inputStr("請輸入姓名:")
    height = pipy.inputFloat("請輸入身高(cm):",min = 0)
    weight = pipy.inputFloat("請輸入體重(kg):",min = 0)
    
    data = BMI(name,height,weight)
    bmi = data.bmi(height,weight)
    status = data.status(bmi)
    
    print(f"{data.name}BMI值為{round(bmi,2)}")
    print(f"您的體重{status}")

if __name__ == '__main__':
    main()