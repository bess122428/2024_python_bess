import random
import pyinputplus as pipy


min:int = 1
max:int = 100
count:int = 0

target:int = random.randint(min,max)
print("==========猜數字遊戲===========\n")

while(True):
    keyin:int = pipy.inputInt(f"猜數字範圍{min}~{max}:",min=min,max=max)
    count += 1
    if keyin == target:
        print(f"賓果!猜對了,答案是{keyin}")
        print(f"您猜了{count}次!")
        break
    elif(keyin > target):
        print("再小一些")
        max = keyin -1

    elif(keyin < target):
        print("再大一些")
        min = keyin +1
        
    print(f"您猜了{count}次!")

print("遊戲結束")