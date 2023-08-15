#create empty set
s = set()

#add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
# this ^^ value will not appear because its not a unique value
s.remove(2)
print(s)
print(f"The set has {len(s)} elements.")
