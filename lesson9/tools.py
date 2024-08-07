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