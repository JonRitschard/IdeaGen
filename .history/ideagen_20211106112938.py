######TODO#####
#Figure out how to pull string values from a list and print it out
#how to pull multiple lists and concat them
#make it run N number of times
#how to randomize results (permutations?)
#

path_to_file = "C:/Users/Jon/Desktop/Shiz/_Code/IdeaGen/lists"
file1 = "list1.txt"
list1 = []
list2 = []
list3 = []


#reads specific list and adds values to list1
with open(path_to_file + "/{}", 'r') as f:
    for line in f:
        list1 += line
#strip all \n from list        
list1 = list1[0::2]
#print(list1)     

#reads specific list and adds values to list2
with open(path_to_file + "/list2.txt", 'r') as f:
    for line in f:
        list2 += line
#strip all \n from list        
list2 = list2[0::2]
#print(list2)  

#reads specific list and adds values to list3
with open(path_to_file + "/list3.txt", 'r') as f:
    for line in f:
        list3 += line
#strip all \n from list        
list3 = list3[0::2]
#print(list3)  

#print the values of lists in order
for value in list1:
    print(value)
for value in list2:
    print(value)
for value in list3:
    print(value)

#I think map() would concat list values...
#loop through all lists and return file name

