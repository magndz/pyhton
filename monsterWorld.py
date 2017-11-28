# # # # # # # # # # # # # # # # # # # #
# Monsters' World
from random import randint
n = 4
object_number = 4  #1G, 3M
flag = True
while flag:
    obj_cell_list = []
    flag = False    
    #randomly select cells of objects that should not overlap with each other
    while True:
        cell = randint(0, n**2-1)
        if cell not in obj_cell_list:
            obj_cell_list.append(cell)    #first position for G, others for W 
        if len(obj_cell_list) == object_number:
            break     
    #determine whether objects are in proper cells 
    monsters = obj_cell_list[1:object_number]
    gold = obj_cell_list[0]
    if 0 in obj_cell_list: #G and Ms are not in cell 0
        flag = True
    elif (1 in monsters) and (n in monsters): #both cells adjacent to 0 does not include M.
        flag = True
    elif gold==(n-1): #if G is in the second corner
        if (n-2 in monsters) and (2*n-1 in monsters):
            flag = True
    elif gold==(n**2-n): #if G is in the third corner
        if (n**2-2*n in monsters) and (n**2-n+1 in monsters):
            flag = True
    elif gold==(n**2-1): #if G is in the last corner
        if (n**2-n-1 in monsters) and (n**2-2 in monsters):
            flag = True
    elif gold>0 and gold<(n-1): #the upper edge
        if (gold-1 in monsters) and (gold+n in monsters) and (gold+1 in monsters):
            flag = True
    elif gold>(n-1) and gold<(n**2-1): #the right edge
        if (gold-n in monsters) and (gold-1 in monsters) and (gold+n in monsters):
            flag = True
    elif gold>0 and gold<(n**2-n): #the left edge
        if (gold-n in monsters) and (gold+1 in monsters) and (gold+n in monsters):
            flag = True
    elif gold>(n**2-n) and gold<(n**2-1): #the lower edge
        if (gold-1 in monsters) and (gold-n in monsters) and (gold+1 in monsters):
            flag = True
#write the world to the file
f = open("monstersworld.txt", "w")
for i in range(n**2):
    if i==0:
        line = "P"
    elif i in obj_cell_list:
        if i==gold:
            line = "G"
        else:
            line = "M"
    else:
        line = "0" 
        
    if i != (n**2-1):
        f.write(line + "\n")
    else:
        f.write(line)
f.close()
# INSERT YOUR CODE HERE ...
moveList = ["w","d","s","a"] #move list we define directions in a list
roomList = ["S","H","P"] #room list we define room type in a list
f = open("monstersworld.txt", "r") #read file that monstersworld.txt read role
monstersWorld = f.readlines() #set monsterWorld with lines
f.close()#close file
monstersWorldList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #I have to define monsterWorldList like that because I did not have permission for use append function
col = 1     	#|
row = 0		#|
step = 0	#|variables
error = 0   	#|
monster = False #|
for x in range(len(monstersWorld)): monstersWorldList[x] = monstersWorld[x].replace("\n","") #this for loop to read charecters in list end replace them and set them another list that monstersWorldList
while True: #infinity loop 
	monster = False #initialize variable
	if(error == 0):# this if blog for error management, we set error variable with 0,1,2 and every number have a error massage with out 0, zero means no error
		#look around the current box if there exist a monster we give a massage and if not a  monster that room is safe
		if(((col+1) <= 4 and monstersWorldList[col+1+row-1] == "M") or ((col-1) > 0 and monstersWorldList[col-1+row-1] == "M") or ((row-4) > -1 and monstersWorldList[col+row-4-1] == "M") or ((row+4) <= 12 and monstersWorldList[col+row+4-1] == "M")):monster = True
		if(monster == False):print("You are in a safe room. Don’t worry!") #
		else:print("You just heard a howl. Be careful!")
		print("Number of steps taken so far is",step,".")
		for i in range(len(monstersWorld)):  #for loop for write room and hide Monsters and Gold than write like 4 x 4 matris
			if(i+1) % 4 != 0:
				if monstersWorldList[i] in roomList:
					print(monstersWorldList[i], end = " ")
				else:
					print("?", end = " ")
			else:
				if monstersWorldList[i] in roomList:
					print(monstersWorldList[i],"\n", end = "")
				else:
					print("?\n", end = "")
	elif(error == 1): #error 1 we check it if it is true give message
		print("There is no such direction! Choose right (d), left (a), up (w) or down (s).")
		print("Number of steps taken so far is",step,".")
		error = 0
	elif(error == 2): #error 2 we check it if it is true give message
		print("You hit the wall. Try another move!")
		print("Number of steps taken so far is",step,".")
		error = 0
	move = input("\nWhat is your move? ").lower()  #Requset input from user for insensitive input was used with .lower()
	if monster == True:monstersWorldList[col+row-1] = "H" #if monster is true we set previous step H else set it with S
	else:monstersWorldList[col+row-1] = "S"
	step += 1 #An increase value of step
	if not(move in moveList):error = 1 #if condition is true initialize error with 1 value
	else:
		#In order to direction we increase, decreasing column or row
		if(move == "w" and (row-4) > -1):row -= 4
		elif(move == "d" and (col+1) <= 4):col += 1
		elif(move == "s" and (row+4) <= 12):row += 4
		elif(move == "a" and (col-1) > 0):col -= 1
		else:error = 2
		#When current box is monster or gold break infinity loop
		if(monstersWorldList[col+row-1] == "M"):break
		elif(monstersWorldList[col+row-1] == "G"):break
		monstersWorldList[col+row-1] = "P"
if(monstersWorldList[col+row-1] == "M"): #if player catch monster we give the necessary explanations
	print("Oh no! You are eaten by a monster.")
	print("Number of steps taken so far is",step,".")
	print("Game Over! \nScore: 0")
else:#if player find gold we give the necessary information
	print("congratulation! You are found gold.")
	print("Number of steps taken so far is",step,".") 
	print("Game Over! \nScore:", 100//step)	#Calculate point	
