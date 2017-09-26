#Says Hello and asks for name

print('Hello, welcome to my first Python program')
print('What is your name')
userName=input()
print('It is good to meet you '+userName)
print('Your name has '+str(len(userName))+' characters')
print('What is your age')
age=input()
age=int(age)
print('You will be ' + str(age+1)+' in 1 year, give or take')
print('Bye!')
