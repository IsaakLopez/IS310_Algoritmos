# Implement an Array data structure as a simplified type of list. 

class Array(object):
   def __init__(self, initialSize):    # Constructor
      self.__a = [None] * initialSize  # The array stored as a list
      self.__nItems = 0                # No items in array initially

   def __len__(self):                  # Special def for len() func
      return self.__nItems             # Return number of items
   
   def get(self, n):                   # Return the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
         return self.__a[n]            # only return item if in bounds
   
   def set(self, n, value):            # Set the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
         self.__a[n] = value           # only set item if in bounds
      
   def insert(self, item):             # Insert item at end
      self.__a[self.__nItems] = item   # Item goes at current end
      self.__nItems += 1               # Increment number of items

   def find(self, item):               # Find index for item
      for j in range(self.__nItems):   # Among current items
         if self.__a[j] == item:       # If found,
            return j                   # then return index to item
      return -1                        # Not found -> return -1
   
   def search(self, item):             # Search for item
      return self.get(self.find(item)) # and return item if found

   def delete(self, item):             # Delete first occurrence
      for j in range(self.__nItems):   # of an item
         if self.__a[j] == item:       # Found item
            self.__nItems -= 1         # One fewer at end
            for k in range(j, self.__nItems):  # Move items from
               self.__a[k] = self.__a[k+1]     # right over 1
            return True                # Return success flag
      
      return False     # Made it here, so couldn't find the item   

   def traverse(self): # Traverse all items
      a = []
      for j in range(self.__nItems):   # and apply a function
         a += [self.__a[j]]
      return a

   def getMaxNum(self):
      maxNum = None

      for j in range(self.__nItems):
         if isinstance(self.__a[j], (int, float)):
            if maxNum is None or self.__a[j]>maxNum:
               maxNum = self.__a[j]
      return maxNum

   def getPromed(self):
      suma = 0
      Count = 0

      for j in range(self.__nItems):
         if isinstance(self.__a[j], (int, float)):
            suma += self.__a[j]
            Count += 1
      if Count > 0:
         return suma/Count
      return None

   def deleteMaxNUmber(self):
      #max_number = self.getMaxNum()

      return self.delete(self.getMaxNum())
   
   def getPair(Self, value):
      valores = []

      if value == 0 :
         for j in range(Self.__nItems):
            if isinstance(Self.__a[j], int):
               if Self.__a[j] % 2 == 0:
                  valores += [Self.__a[j]]
      if value == 1 :
         for j in range(Self.__nItems):
            if isinstance(Self.__a[j], int):
               if Self.__a[j] % 2 != 0:
                  valores += [Self.__a[j]]
      return valores
   
   def getWords(self):
      Words = []

      for j in range(self.__nItems):
         if isinstance(self.__a[j], str):
            Words += [self.__a[j]]
      return Words
   

   def eliminar_duplicados(self):
      elementos_unicos = set()         # Conjunto para almacenar elementos únicos
      nuevo_indice = 0                 # Índice para la lista sin duplicados

      for i in range(self.__nItems):
         if self.__a[i] not in elementos_unicos:  # Verifica los duplicados
            elementos_unicos.add(self.__a[i])
            self.__a[nuevo_indice] = self.__a[i]  # Mueve el elemento
            nuevo_indice += 1

        # Actualiza el número de elementos y establece None en las posiciones vacías restantes

      self.__nItems = nuevo_indice
      for i in range(nuevo_indice, len(self.__a)):
         self.__a[i] = None