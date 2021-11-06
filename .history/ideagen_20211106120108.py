import random

path_to_file = "C:/Users/Jon/Desktop/Shiz/_Code/IdeaGen/lists"
file1, file2, file3 = "list1.txt", "list2.txt", "list3.txt"
list1, list2, list3 = [], [], []
results = 5

while results > 0:

    #reads specific list and adds values to list1
    with open(path_to_file + f"/{file1}", 'r') as f:
        for line in f:
            list1 += line
    #strip all \n from list        
    list1 = list1[0::2]
    #randomize list
    random.shuffle(list1)
    #print(list1)     

    #reads specific list and adds values to list2
    with open(path_to_file + f"/{file2}", 'r') as f:
        for line in f:
            list2 += line       
    list2 = list2[0::2]
    random.shuffle(list2)
    #print(list2)  

    #reads specific list and adds values to list3
    with open(path_to_file + f"/{file3}", 'r') as f:
        for line in f:
            list3 += line       
    list3 = list3[0::2]
    random.shuffle(list3)
    #print(list3)  
    """ 
    #print the values of lists in order
    for value in list1:
        print(value)
    for value in list2:
        print(value)
    for value in list3:
        print(value)
    """
    #concatenate values in lists
    print(f"list1[0]+list2[0]}+{list3[0]}")
    #reset the lists
    list1, list2, list3 = [], [], []
    #-1 iteration
    results-=1


