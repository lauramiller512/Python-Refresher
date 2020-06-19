friends = {"Olivia", "Jyoti", "Amelia"}
abroad = {"Olivia", "Amelia"}

local_friends = friends.difference(abroad) # looks within friends to find the duplicates from abroad
print(local_friends) # prints {"Jyoti"}

z = x.difference(y) # returns set of items that only exist in set x, and not in set y