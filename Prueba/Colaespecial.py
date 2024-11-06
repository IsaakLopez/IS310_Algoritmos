
class cola(object):

    def __init__(self,size):
        self.__maxSize = size 
        self.__a = [None] * size
        self.__nItems = 0
        self.__front = 1
        self.__rear = 0 

    def isEmpty(self): 
        return self.__nItems == 0
    
    def isFull(self):  
        return self.__nItems == self.__maxSize
    
    def insert(self, item):
        
        if self.__maxSize > self.__nItems:
            self.__rear += 1
            if self.__rear == self.__maxSize:
                self.__rear = 0
            self.__a[self.__rear] = item
            self.__nItems += 1
            return True    
         
        if self.isFull:
            if self.__rear == self.__maxSize:
                self.__rear = self.__maxSize
            self.__a[self.__rear] = item
            self.__rear -= 1
            return True        

    def __str__(self):
      ans = "["
      for i in range(self.__nItems):
         if len(ans) > 1:
            ans += ", "
         j = i + self.__front
         if j >= self.__maxSize:
            j -= self.__maxSize
         ans += str(self.__a[j])
      ans += "]"
      return ans