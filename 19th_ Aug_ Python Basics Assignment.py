#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Declare two variables, x and y, and assign them integer values. Swap the values of these variables without using any temporary variable.


# In[1]:


# Step 1: Declare and initialize variables
x = 5
y = 10

# Step 2: Creating function to swap the variables
def swap_variables(x,y):
  print(f"Before swap x: {x} and y: {y}")
  x,y = y, x
  print(f"After swap x: {x} and y: {y}")

swap_variables(x,y)


# In[ ]:


#2. Create a program that calculates the area of a rectangle. Take the length and width as inputs from the user and store them in variables. Calculate and display the area.


# In[2]:


# Step 1: Get input from the user for length and width
length = float(input("Enter the length of the rectangle: ")) # Taking user input for length and converting it to a floating-point number
width = float(input("Enter the width of the rectangle: "))   # Taking user input for width and converting it to a floating-point number

# Step 2: Calculate the area of the rectangle using the formula: area = length * width
area = length * width # Calculating the area by multiplying length and width

# Step 3: Display the calculated area to the user
print("The area of the rectangle is:", area) # Printing the calculated area


# In[ ]:


#3. Write a Python program that converts temperatures from Celsius to Fahrenheit. Take the temperature in Celsius as input, store it in a variable, convert it to Fahrenheit, and display the result.


# In[3]:


# Step 1: Get the temperature in Celsius from the user
celsius_temperature = float(input("Enter temperature in Celsius: "))

# Step 2: Convert Celsius to Fahrenheit using the formula: (C * 9/5) + 32
fahrenheit_temperature = (celsius_temperature * 9/5) + 32

# Step 3: Display the converted temperature in Fahrenheit
print(f"{celsius_temperature} Celsius is equal to {fahrenheit_temperature:.2f} Fahrenheit")


# String based questions

# In[ ]:


1. Write a Python program that takes a string as input and prints the length of the string


# In[4]:


# Step 1: Get input from the user
input_string = input("Enter a string: ")

# Step 2: Calculate the length of the input string using the built-in len() function
string_length = len(input_string)

# Step 3: Print the length of the string
print("The length of the input string is:", string_length)


# In[ ]:


2. Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.


# In[5]:


# Step 1: Get input from the user
sentence = input("Enter a sentence: ")

# Step 2: Initialize a variable to count the vowels
vowel_count = 0

# Step 3: Iterate through each character in the sentence
for char in sentence:
    # Step 4: Convert the character to lowercase to handle both uppercase and lowercase vowels
    char_lower = char.lower()

    # Step 5: Check if the character is a vowel (a, e, i, o, u)
    if char_lower in "aeiou":
        # Step 6: If the character is a vowel, increment the vowel_count variable
        vowel_count += 1

# Step 7: Display the result
print("Number of vowels:", vowel_count)


# In[ ]:


3. Given a string, reverse the order of characters using string slicing and print the reversed string.


# In[6]:


# Step 1: Get the input string from the user
input_string = input("Enter a string: ")

# Step 2: Use string slicing to reverse the string
# Syntax: [start:end:step]
# Here, we start from the end of the string, move backward with step -1, and stop at the beginning.
reversed_string = input_string[::-1]

# Step 3: Print the reversed string
print("Reversed string:", reversed_string)


# In[ ]:


4. Write a program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards).


# In[7]:


# Step 1: Get input from the user
input_string = input("Enter a string: ")

# Step 2: Remove spaces and convert the input string to lowercase
cleaned_string = input_string.replace(" ", "").lower()

# Step 3: Reverse the cleaned string using slicing
reversed_string = cleaned_string[::-1]

# Step 4: Compare the cleaned string with its reverse to check for palindrome
if cleaned_string == reversed_string:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")


# In[ ]:


5. Create a program that takes a string as input and removes all the spaces from it. Print the modified string without spaces.


# In[8]:


# Step 1: Take input from the user
input_string = input("Enter a string: ")

# Step 2: Initialize an empty string to store the modified string without spaces
modified_string = ""

# Step 3: Iterate through each character in the input string
for char in input_string:
    # Step 4: Check if the character is not a space
    if char != " ":
        # Step 5: If not a space, append the character to the modified string
        modified_string += char

# Step 6: Print the modified string without spaces
print("Modified string without spaces:", modified_string)


# In[ ]:





# In[ ]:




