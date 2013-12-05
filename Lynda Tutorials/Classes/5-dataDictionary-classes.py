'''
Created on Oct 2, 2013

@author: vjuanillas
'''


class Duck: 
    # add object data
    def __init__(self, **kwargs):
        #self._color = kwargs.get('color','white') #if color is not set, default is white
        self.variables = kwargs #store data to data dictionaries
        
    def quack(self):
        print('Quaakkk!!!')
    def walk(self):   
        print('Walks like a duck')
    #def set_color(self,color):    
    #    self.variables['color'] = color
    #def get_color(self):
    #    return self.variables.get('color', None)
    
    def set_variables(self, k, v):
        self.variables[k] = v
    def get_variables(self,k):
        return self.variables.get(k,None)
        
def main():
    #donald = Duck(color = 'blue')
    donald = Duck(feet = 2)
    #print(donald.get_color())
    donald.set_variables('color', 'blue')
    print(donald.get_variables('feet'))
    print(donald.get_variables('color'))
    
    kevin = Duck()
    kevin.set_variables('color', 'red')
    print(kevin.get_variables('color'))
    
   
    
if __name__ == '__main__':main()
   