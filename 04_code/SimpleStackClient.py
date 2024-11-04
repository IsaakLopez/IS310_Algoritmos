from SimpleStack import *

stack = Stack(10)

for word in ['May', 'the', 'force', 'be', 'with', 'you', 'is', 'stars', 'wars', 'right']:
   stack.push(word)

print('After pushing', len(stack), 
      'words on the stack, it contains:\n', stack)
print('Is stack full?', stack.isFull())

print('Popping items off the stack:')
while not stack.isEmpty():
   print(stack.pop(), end=' ')
print()

#Ejercicio 4.1
stack1 = Stack(4)
for test in ['aparentemente', 'no', 'te', 'quieren']:
   stack1.push(test)
print('Despues de poner', len(stack1), 'palabras a la pila de prueba, esta contiene:\n', stack1)
stack1.push('conmigo')


