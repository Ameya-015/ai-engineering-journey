# Dict is HashMap in python without explicit type definition

dict = {"Mango" : 1, "Apple" : 2, "Watermelon" : 3}
m = dict["Mango"]
print(m);

print(dict.get("Grape"))
# Above print statement prints None. None is Java's null

#temp = dict["Grape"]
#print(temp);
# Above print returns error as key is not present in dict

#####################################################################################


# set is HashSet in Python without explicit type definition

# set is also declared using {} but without key:value pair

set = {1,2,3,4}
print(set);

print(2 in set)