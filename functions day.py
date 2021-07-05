#fizz_buzz
number1 = int(input("enter num: "))
for number1 in range(1,20):
    if(number1 % 3==0):
        print('fizz')
    elif(number1 % 5==0):
        print('buzz')
    elif(number1 %15==0):
         print('fizzbuzz')
    else:
        print(number1)
