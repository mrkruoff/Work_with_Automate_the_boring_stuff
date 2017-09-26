def callatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1

print('please input an integer')
while True:
    try:
        number=int(input())
        break
    except ValueError:
        print('Invalid input, plesae input an integer')
    
while number!=1:
    number=callatz(number)
