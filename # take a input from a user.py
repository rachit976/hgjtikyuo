# take a input from a user
num = int(input("ENTER A number:"))



#initialize sum
sum = 0



#find the sum of the cube of each digit 
temp = num
while temp  > 0:
    digit = temp% 10
    sum += digit  ** 3
    temp //= 10 
# display the result 
if num== sum:
    print(num,"IS  AN ARMStong")
else:
     print(num,"IS not AN ARMStong")