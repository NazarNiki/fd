import vegatable_class
class Assistant():
    def _init(self,name,position):
        self.Name=name
        self.Position=position
    def print_info(self):
        print('Name:',self.Name)
        print('Postition:',self.Position)
    def water(self,vegatable):
        vegatable.water_saturation+=1
        print('fvg',vegatable.kind,'/n')
    def fertilize(self,vegatable):
        vegatable.fertilize_saturation+=1
        print('fvg',vegatable.kind,'/n')
    def turn_light(self,vegatable):
        vegatable.light_saturation+=1
        print('fvg',vegatable.kind,'/n')
    def checkresullt(self,result1,result2,result3):
        if result1 ==True and result2 ==True and result3==True:
            self.print_info()
            print('passed xthe certification')
        else:
            self.print_info()
            print('Didn t pass certification')
