row1 =["x","x","x"]
row2 =["x","x","x"]
row3 =["x","x","x"]
map =[row1,row2,row3]
postion=input("Where do your want to put Treasure")
horizontal=int(postion[0])
vertical=int(postion[1])
map[vertical-1][horizontal-1]="O"
print("{row1}\n{row2}\n{row3}")
