class Point:
    
    def __init__(self,x,y):
        self.x_cord = x
        self.y_cord = y
        
    def __str__(self):
        return "<{},{}>".format(self.x_cord,self.y_cord)
    
    
    
    def euclidian_distance(self,other):
        return ((self.x_cord - other.x_cord)**2 + (self.y_cord - other.y_cord)**2)**0.5

    def distance_origin(self):
        return self.euclidian_distance(Point(0,0))
        
        
p1 = Point(0,0)
p2 = Point(10,10)


d = p1.euclidian_distance(p2)
print(d)

p1.distance_origin()