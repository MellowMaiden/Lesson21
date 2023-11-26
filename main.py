#Lesson 21
#Example 1
N=0
while True:
    N+=1
    print(N)

#Example 2
N=0
while True:
    N+=1
    print(N)
    if N==1000000:
        break

#Example 3
#We have 3 ways to do
#way 1
for n in range(1,11):
    print(n**2)
#way 2
n=1
while n<=10:
    print(n**2)
    n+=1
#way 3
n = 1
while True:
    if n > 10: # THE LOOP BREAK
        break
    print(n**2)
    n += 1
#Example 4
x=int(input("Give me a number x"))
y=int(input("Give me a number y"))
try:
    print(f"x divided y is : {x/y}")
except:
    print(f"Oh sorry but something gose wrong")

#Example 5
while True:
    try:
        x = float(input("Give me a number from 1 to 10: "))  # Get a number
        if x >= 1 and x <= 10:  # Check if it is between 1 and 10
            print("Thank you")  # good, say thank you
            break  # break out from the loop
        else:
            print("No that is not between 1 and 10")  # but if it is not then "complain"
    except:
        print("No, that is not a number")  # this runs if IT IS NOT AN NUMBER AND WOULD CRASH

print("Your number is", x)