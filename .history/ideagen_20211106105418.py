######TODO#####
#Figure out how to pull string values from a list and print it out
#how to pull multiple lists and concat them
#make it run N number of times
#how to randomize results (permutations?)
#

path_to_file = "C:/Users/Jon/Desktop/Shiz/_Code/IdeaGen/lists"

#reads specific list and prints it
with open(path_to_file + "/list1.txt", 'r') as f:
    lines = f.read()
    print(lines)

