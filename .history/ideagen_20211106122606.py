import random

path_to_files = "C:/Users/Jon/Desktop/Shiz/_Code/IdeaGen/lists"
path_to_save = "C:/Users/Jon/Desktop/Shiz/_Code/IdeaGen/results"
file1, file2, file3 = "list1.txt", "list2.txt", "list3.txt"
list1, list2, list3 = [], [], []
outputList = ""

results = 5

while results > 0:

    #reads specific list and adds values to list1
    with open(path_to_files + f"/{file1}", 'r') as f:
        for line in f:
            list1 += line
    #strip all \n from list        
    list1 = list1[0::2]  

    #reads specific list and adds values to list2
    with open(path_to_files + f"/{file2}", 'r') as f:
        for line in f:
            list2 += line       
    list2 = list2[0::2]

    #reads specific list and adds values to list3
    with open(path_to_files + f"/{file3}", 'r') as f:
        for line in f:
            list3 += line       
    list3 = list3[0::2]
    
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
f=open(path_to_save + f"/results.txt", 'w') as 