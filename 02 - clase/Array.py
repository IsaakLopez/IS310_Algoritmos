# Implement an Array data structure as a simplified type of list. 
from random import *

class Array(object):
   def __init__(self, initialSize):    # Constructor
      self.__a = [0] * initialSize  # The array stored as a list
      self.__nItems = 0
      self.rellenar()                # No items in array initially

   def __len__(self):                  # Special def for len() func
      return self.__nItems             # Return number of items
   
   def get(self, n):                   # Return the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
         return self.__a[n]            # only return item if in bounds
   
   def set(self, n, value):            # Set the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
         self.__a[n] = value           # only set item if in bounds

   def rellenar(self):
      for i in range(0, 99):
         num_aleatorio = randint(1, 1000)
         self.push(num_aleatorio)
        

   def push(self, item):             # Insert item at end
      self.__a[self.__nItems] = item   # Item goes at current end
      self.__nItems += 1               # Increment number of items
         
   def pop (self):
      item = self.__a[self.__nItems]
      self.__a[self.__nItems] = None
      self.__nItems -= 1
      return item
      
   def popLeft(self):
      item = self.__a[0]
      del self.__a[0]
      self.__nItems -= 1
      return item

   def detParidad(self, valor):
    contPar = contImpar = sumaPar = sumaImpar = 0

    for i in range(0, 100):
        numberPop = self.pop() if valor == 1 else self.popLeft()
        if numberPop is not None:
            if numberPop % 2 == 0:
                contPar += 1
                sumaPar += numberPop
            else:
                contImpar += 1
                sumaImpar += numberPop

    return contImpar, contPar, sumaImpar, sumaPar


   def traverse(self): 
      
      a = []
      for j in range(self.__nItems):   # and apply a function
         a += [self.__a[j]]

      return a