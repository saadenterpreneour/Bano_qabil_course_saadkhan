# -*- coding: utf-8 -*-
"""saadkhan_midterm .py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TFZYqKTUPlu98eyZLnoUpNJ669UlgJ3z
"""

# Question no 1
# write a pyton program to do arithmetical operation addition and division.
num1 = int(input("Entet the first number"))
num2 = int(input("Enter the second number"))
s=num1+num2
print("sum :" ,s)

num3 = int(input("Enter the third number"))
num4 = int(input("Enter the fourth number"))
e=num3/num4
print("division :" ,e)

num5 = int(input("Enter the fifth number"))
num6 = int(input("Enter the sixth number"))
t=num5**num6
print("power :" ,t)

num7 = int(input("Enter the seventh number"))
num8 = int(input("Enter the eighth number"))
p=num7//num8
print("floor division :" ,p)

# Question no 2
# write a python program to find the area of triangle.
mi = float(input("Enter the length of the base of the triangle"))
im = float(input("Enter the height of the  triangle"))
BB=(mi*im)/2
print("Area of triangle :",BB)

# Question no 3
# Write a python program to convert celsius to Farenheit.
celsius = int(input("Enter the Temperature in celsius :/n"))
fahrenheit = (9/5 * celsius) + 32
print("Temperature in Fahrenheit :", fahrenheit)

#Qustion number 4
# write a python program that return all datatypes that we  discussed in the class.
m=5
print(f"Your first input type {m} is: {type(m)}")
n=5.6
print("Your second input type is " ,type(n))
o="saad khan"
print("Your third input type is" ,type(0))
r=True
print("your fourth input type is" ,type(r))
s=[1,23,5]
print("your fifth data type is" ,type(s))
y={1,2,3}
print("your sixth data type is" ,type(y))
i=(1,2,3)
print("your seven data type is" ,type(i))
