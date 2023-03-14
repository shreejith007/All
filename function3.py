#function with Multiple input
def greet_with(name,location):
    print(f"my name is{name}"+f"From {location}")
    
greet_with("Shreejith","Mandleshwar")

greet_with("mandleshwar","Shreejith") # o/p will be reversed in this situation (positional argument error)
    
    #with key aurgument
def greet_with(name="Shreejith",location="Mandleshwar"):
    
    

 greet_with("Shreejith","Mandleshwar")


