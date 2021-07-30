bottleCapacity = 1000
sips = 0

print("Please drink")
res = True

while res==True :
    sipValue = int(input("Enter the common capacity of your sip:- "))
    intakeValue = bottleCapacity//sipValue 
    for i in range(0,intakeValue) :
        sipValue = int(input("Enter the capacity of each sip of urs :- "))
        intakeValue = bottleCapacity//sipValue
        sips+=1
        bottleCapacity-=sipValue
        print(sips,bottleCapacity)
    res = False

if bottleCapacity < 20 :
     print("Refill your bottle")