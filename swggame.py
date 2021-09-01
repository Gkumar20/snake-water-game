#snack Water Gun Game
import random
name=input("Enter player Name: ")
print("Your oppsite player Name: Computer")
swg=["Snack","Water","Gun"]
swg1=["Snack","Water"]
swg2=["Water","Gun"]
swg3=["Snack","Gun"]
result=[]
result1=[]
result2=[]
j=1
for i in swg:
    print(j,":",i)
    j+=1
n=0
while(n<10):
    n+=1
    choice1=random.choice(swg)
    choice2=swg[int(input("Enter your choice: "))-1]
    print(f"{name}'s choice is {choice2}\nComputer choice is {choice1}")
    result.append(choice1)
    result.append(choice2)
    if choice1==choice2:
        print(f"Dear {name} You Both choose Same So Draw")
        result1.append(0)
        result2.append(0)
    else:
        if set(swg1)==set(result):
            print("snack swimming on water so snack has win")
            if choice1=="Snack":
                result1.append(1)
            else:
                result2.append(1)
        elif set(swg2)==set(result):
            print("gun is dopped in water so water has win")
            if choice1=="Water":
                result1.append(1)
            else:
                result2.append(1)
        else:
            print("gun kill the snack so gun has win")
            if choice1=="Gun":
                result1.append(1)
            else:
                result2.append(1)
if result1.count(1)>result2.count(1):
    print(f"Conguratulation {name}\nYou Win the Game")
elif result1.count(1)==result2.count(1):
    print(f"Hey {name}\nDraw Game")
else:
    print(f"Sorry {name} \nYou Lost the Game")
