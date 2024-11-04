# A program to reverse the letters of a word

from SimpleStack import *

stack = Stack(100)          # Create a stack to hold letters


#Ejercicio 4.2
#word = input("Word to reverse: ") #para probar el ejercio de el libro comento el input
word = 'A man, a plan, a canal, Panama'
original = ''

for letter in word:         # Loop over letters in word 
   if letter.isalpha():
      original += letter.lower()
      if not stack.isFull():   # Push letters on stack if not full
         stack.push(letter.lower())
    
reverse = ''                # Build the reversed version

while not stack.isEmpty():  # by popping the stack until empty
   reverse += stack.pop()

if original == reverse:
   print("la palabra es palindrome")
else:
   print("la palabra no es palindrome")

print('The reverse of', word, 'is', reverse)

