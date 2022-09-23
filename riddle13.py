'''Challenge
Online status
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.

Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
'''

def online_count(dict1):
    count = 0
    for i in dict1.values():
        if i == "online":
            count = count + 1
    
    return count
        
        
m = online_count({
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
})

print(m)