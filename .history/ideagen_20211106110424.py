######TODO#####
#Figure out how to pull string values from a list and print it out
#how to pull multiple lists and concat them
#make it run N number of times
#how to randomize results (permutations?)
#

path_to_file = "C:/Users/Jon/Desktop/Shiz/_Code/IdeaGen/lists"
list1 = []

#reads specific list and prints it
with open(path_to_file + "/list1.txt", 'r') as f:
    for line in f:
        list1 += line

#strip all \n from list        
list1 = list1[0::2]
print(list1)     


for value in list1:
    print(value)


#loop through all lists and return file name
#save list values to lists
