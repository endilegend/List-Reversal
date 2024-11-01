#recursive function
def reverse(lst):
    #base case
    if len(lst) == 0:
        return []

    #recursive step
    #grabs the last number and adds it to the list, while the list is noow the list up to the last number.
    return [lst[-1]] + reverse(lst[:-1])

#creates list with 1-35        
lst = list(range(1,36))
print(lst)

#uses the recursive function to reverse the list
print(reverse(lst))