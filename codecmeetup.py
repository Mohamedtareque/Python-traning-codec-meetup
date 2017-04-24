#python quotations 
#'character' , "Word" , 
#""" Multiply lines  paragraph"""
##############################
#formate strings %s %d %f 
#example 
list =["Codec","First"]
letter = """ Dear %s team \n this is our %s meetup 

"""
print letter%(list[0],list[1])
###############################
#Python supports the if, else, and elif statements for conditional execution of code. 
#The syntax is >> if expression: block 
#If the expression evaluates to true execute the block of code
x= False
y = False
if x == True : 
	print "X is true"
elif y == True :
	print"y is true" 
else : 
	print "Both false"
######################################
#Python supports the while statement for conditional looping
#the syntax is while expression: block.
#While the expression evaluates to true, execute the block in looping fashion
x= 1 
while x< 10:
	print x 
	x +=1 
#####################################
#Python also supports the for statement for sequential looping. 
#The syntax is for item in sequence:block. 
#Each loop item is set to the next item in the sequence, and the block of code is executed. 
#The for loop continues until there are no more items left in the sequence. 
for x in range(1,10):
	print "for loop " , x
######### example 2 ############
word = "Codec Team" 
list =[] 
for ch in word : 
	list.append(ch)
print list
############# example 3 #######
dic ={} 
for i , char in enumerate(word):
	dic[i]=char
print dic 
####################Example 4 ###############
for key in dic:
	print key ,'=', dic[key]
#########################
