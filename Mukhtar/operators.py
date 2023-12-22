# Q1. Create a list of fruits
fruits = ['mangoes' , 'apples' , 'grapes' , 'watermelon' , 'oranges']
# Q2. Using the right opera'tor check if your list contains 'apple'. Your answer should be valid regardless of casing.
print('apples' in fruits)
# Q3. Remove the last item from the list and check if it contains the alphabet 'a'
print(fruits[-1])
print('a' in fruits[-1])
# or
# another_variable = fruits[-1]   
# print( another_variable )
# print('a'in another_variable )
# Q4. Create a variable to hold the value 5
x= 90
# Q6. Add 5 to the above variable
x+= 10
# Q7. Multply it by 6
x*= 6
# Q8. Check if the final value is less than 100 or if the list of fruits doesnt contain banana 
print(x < 100 or 'banana' in fruits)