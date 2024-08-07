import pyinputplus as pipy
from random import choices

def main():
    with open("names.txt",encoding='utf-8') as file:
        content:str = file.read()
    
    names:list[str] = content.split()
    num_str:str = pipy.inputMenu(['1個','2個','3個','4個','5個'],
                   prompt = "請選擇需要的人名數量(請選擇1,2,3,4,5):\n",
                   numbered = True)
    num:int = int(num_str[0])
    selected_name:list[str] = choices(names,k=num)
    print("==========================")
    for i in selected_name:
        print(i)

if __name__ == '__main__':
    main()