'''
Created on Oct 2, 2013

@author: vjuanillas
@description: 
'''


class Duck:  
    def __init__(self, value):
        self._venice = value # we create a local variable "v" 
        #Encapsulation -> associated to the objects (donald or kevin) not the class
        
    
    def quack(self):
        print('Quaakkk!!!', self._venice)
    def walk(self):   
        print('Walks like a duck',self._venice)

def main():
    donald = Duck(100) 
    donald.quack()
    donald.walk()
    
    #create another object
    kevin = Duck(37)
    kevin.quack()
    kevin.walk()

if __name__ == '__main__':main()
   