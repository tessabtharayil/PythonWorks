# for-else
# ========
for i in range(1,6):
    print(i,end=" ")
else:   #it works only after the normal execution of loop
    print("hello")

for i in range(1,6):
    if i==3:
        break
    print(i,end=" ")
else:
    print("hello")
print()

#1). Check whether a number is prime or not
# -----------------------------------------
num=int(input("Enter a number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Not Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Number is neither prime nor composite")