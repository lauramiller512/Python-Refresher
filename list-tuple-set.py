l = ["Bob", "Laura", "Pearce"]
t = ("Bob", "Laura", "Pearce") # tuples cannot be modified after they are created
s = {"Bob", "Laura", "Pearce"} # items in a set are not in order

l[0] = "Louie"
print(l)

l.append("Ozzy")
print(l)