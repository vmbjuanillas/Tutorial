'''
Created on Oct 2, 2013

@author: vjuanillas
'''


class Duck: 
    def quack(self):
        print('Quaakkk!!!')
    def walk(self):   
        print('Walks like a duck')
        
    #to enable polymorphism, dog and duck must have similar interface
    def bark(self):
        print('The duck cannot bark')
    def fur(self):
        print('The duck has feathers.')

#let's add another class      
class Dog:
    def bark(self):
        print('Woof!')
    def fur(self):
        print('The dog has brown and white fur.')
    
    #to enable polymorphism, dog and duck must have similar interface
    def quack(self):
        print('Dog cannot quack')
    def walk(self):   
        print('Walks like a dog')
        
def main():
    donald = Duck()
    #donald.quack()
    #donald.walk()
    
    
    #instantiate a Dog object
    fido = Dog()
    #fido.bark()
    #fido.fur()
    
    #let's call the dog in the forest and the duck in the pond
    in_the_forest(donald)
    in_the_pond(fido)
    
'''
This will work as long as the dog and duck implements these interfaces
'''
    
#function expects a dog
def in_the_forest(dog):
    dog.bark()
    dog.fur()
    
def in_the_pond(duck):
    duck.quack()
    duck.walk()
    
#to show duck-typing
def in_the_forest(cat):
    cat.bark()
    cat.fur()

    
    #let's call all 4 functions
    #without concern of what type of object it is
    #assuming all methods exist
    #for o in (donald, fido):
    #    o.quack()
    #    o.walk()
    #    o.bark()
    #    o.fur()
        
    

if __name__ == '__main__':main()
   