import random

#change these variables for your machine
path_to_files = "C:/Users/Jon/Desktop/Shiz/_Code/IdeaGen/lists"
path_to_save = "C:/Users/Jon/Desktop/Shiz/_Code/IdeaGen/results"

#change these if you change the file names in lists directory
file1, file2, file3 = "list1.txt", "list2.txt", "list3.txt"

#indicate how many results you would like
results = 5

list1, list2, list3 = [], [], []
outputList = ""

while results > 0:

    #reads file1 and adds values to list1
    with open(path_to_files + f"/{file1}",'r') as f:
        list1 += f.read().splitlines() 
        
    #reads file2 and adds values to list2
    with open(path_to_files + f"/{file2}",'r') as f:
        list2 += f.read().splitlines()

    #reads file3 and adds values to list3
    with open(path_to_files + f"/{file3}",'r') as f:
        list3 += f.read().splitlines()
    
    #concatenate values in lists
    randomizedResults = f"{random.choice(list1)} {random.choice(list2)} {random.choice(list3)} \n"

    #add results to outputList
    outputList += randomizedResults

    #reset the lists
    list1, list2, list3 = [], [], []

    #-1 iteration
    results-=1

print(outputList)

#write to txt file at save path
with open(path_to_save + f"/results.txt", 'w') as f:
    f.write(outputList)
    f.close()
