'''
Created on Oct 2, 2013

@author: vjuanillas
'''


class Duck: 
    #lets add object data
    def __init__(self, color = 'white'):
        self._color = color #tell self that variable "color" is local- cannot be accessed directly
    
    def quack(self):
        print('Quaakkk!!!')
    def walk(self):   
        print('Walks like a duck')
        
    #accessory methods
    #use to prevent side-effects
    #def set_color(self,color):    
    #    self._color = color
    #def get_color(self):
        
def main():
    donald = Duck()
    print(donald._color)
    
    # unless explicitly changed from outside, 
    # side-effects- this is hard to keep tracked
    #donald._color = 'blue'
    #print(donald._color)
    
    # use accessory methods
    #print(donald.get_color())
    #donald.set_color('blue')
    #print(donald.get_color())
    
if __name__ == '__main__':main()
   