from tokenize import Name


class Student:
    # [assignment] Skeleton class. Add your code here
    
    
   
    def __init__(self,name,age,tracks,score ):
            self.name = name
            self.age=age
            self.tracks = tracks
            self.score=score
    pass
    
    
    def change_name( self, new_name):
        print("changed name" + self.name)
        
    r1 = Name("Neo")
    
    r1.change_name()


''' Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score() '''