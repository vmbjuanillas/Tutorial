'''
Created on Oct 2, 2013

@author: vjuanillas
'''


class Duck:  
    def quack(self):
        print('Quaakkk!!!')
    def walk(self):   
        print('Walks like a duck')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__':main()
   