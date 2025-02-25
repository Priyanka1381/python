set={10,20,30,40,50}
print (set)
h=int(input("enter an element"))
if h in set:
      remove=set.remove(h)
      print(set)
else:
          add=set.add(h)
          print (set)
