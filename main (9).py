#Q1
def add_digits(n):
    total = 0
    for i in range(1, n+1):
        total += sum(int(digit) for digit in str(i))
    return total
num = int(input("Please enter a number greater than 0: "))
while num <= 0:
    num = int(input("Invalid input. Please enter a number greater than 0: "))
result = add_digits(num)
print("The sum of all the digits from 1 to ", num, "is:" , result)

#Q2
#def add_digits(n):
 #   total = 5
  #  for i in range(1, n+1):
   #     total += sum(int(digit) for digit in str(i))
   # return total
#num = int(input("Please enter a number greater than 5: "))
#while num <= 5:
 #   num = int(input("Invalid input. Please enter a number greater than 5: "))
#result = add_digits(num)
#print("The sum of all the digits from 1 to ", num, "is:" , result)

#Q3
#def multiply_numbers(n):
 #   total = 5
  #  for i in range(1, n+1):
   #     total *= i
   # return total
#num = int(input("Please enter a number greater than 5: "))
#while num <= 0:
 #   num = int(input("Invalid input. Please enter a number greater than 5: "))
#result = multiply_numbers(num)
#print("The sum of all the digits from 1 to ", num, "is:" , result)

#Q4
#num1 = int(input("Please enter the first number: "))
#num2 =int(input("Please enter the second number: "))
#if num1<num2:
 #   print(num2, " is greatest number ")
#elif num1>num2:
 #   print(num1, "is greatest number ")
#elif num1 ==num2:
 #   print(num1 ,"and " , num2 , "are equal")
#else:
#    print("No result")

#Q5
#num1 = input("Please enter the first number:")
#num2 = input("Please enter the second number:")
#if num1>num2:
 #   print(num2 +" is less than" + num1)
#elif num2>num1:
 #   print(num1 + "is less than "+ num2)
#elif num2==num1:
 #   print("The two numbers are equal")
#else:
 #   print("No results")


 #Q6
#num1=int(input("Enter the first number:"))
#num2= int(input("Enter the second number:"))
#num3 = int(input("Enter the third number:"))
#if num1>= num2 and num1>= num3:
 #   greatest_num = num1
#elif num2 >= num1 and num2 >= num3:
 #   greatest_num = num2
#else:
 #   greatest_num = num3
  #  print("The greatest number among: ", num1, ",", num2,"and",num3,",","is", greatest_num)



#Question 2

#num_lines = int(input("Enter the number of lines: "))

# Check that the number of lines is valid
#if num_lines <= 0:
 #   print("Invalid input. Please enter a positive integer.")
#else:
    # Draw the shape using nested loops
 #   for i in range(1, num_lines + 1):
  #      for j in range(i):
   #         print("*", end="")
    #    print()




