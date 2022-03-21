 #!/usr/bin/python
"""
Python  Functions
"""

# Write a function unique_list() that takes a list and returns a new list with unique elements of the first list.
# unique_list: (1,2,3,3,3,3,4,4,5)
        
def unique_list(a):
    newList = []
    for x in a:
        if x not in newList:
            newList.append(x)
    return newList

#Write a function multiply() to multiply all giving numbers in a list.
#Sample List : (9, 2, 3, -6, 7)
#Expected Output : -2268

def multiply(a):
    listSum = 1
    for x in a:
        listSum = listSum * x 
    return listSum


# Write a function get_average() that takes an arbitrary number of arguments and returns the average of them
# Number of arguments : (5,6,8,10,31)
# Expected Output : 12

def get_average(*a):
    listAverage = 0
    listAverage = sum(a)/len(a)
    return listAverage
