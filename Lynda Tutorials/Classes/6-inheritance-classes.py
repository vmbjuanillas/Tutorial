'''
Created on Oct 2, 2013

@author: vjuanillas
'''

#another class animal
class Animal:
    def talk(self):
        print('I have something to say')
    def walk(self):
        print('Hey! I''m walking here!')
    def clothes(self):
        print('I have nice clothes')
    def wings(self):
        print('I believe I can fly')
        
        
#Duck can inherit all the attributes of the Animal
class Duck(Animal): #Duck is an animal
    def quack(self):
        print('Quaakkk!!!')
    def walk(self):   
        #by default, uses the Duck method
        #by using super, method is overriden and superclass Animal method is used instead
        #super().walk()
        print('Walks like a duck')
        
#lets add another animal
class Dog(Animal):
    #pass
    def clothes(self):
        print('I have brown and white fur!')
    def wings(self):
        print('But I cannot fly')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    
    #let's invoke a method of it's parent
    #donald.clothes()
    
    fido = Dog()
    fido.walk()
    fido.clothes()
    fido.wings()
    

if __name__ == '__main__':main()
   