#dictionary = {key:value}
#in dictionary key are strings
dic ={
    "Bug":"An error in the program is known as bug"
    , "Fuction":"A piece of code whichh is called again and again"
    ,122:"ONE TWENTY TWO"}
print(dic)
print(dic["Fuction"])

dic["loop"]="just example"
print(dic)

# cretated empty dictionary
#empty_dictionary ={}

# empty the existing dictionary
#dic={}

#edit the item in dictionary
dic["Bug"]="AN moth in a computer"
print(dic)

# loop through dictionary
for key in dic:
     print(key)
     print(dic(key))