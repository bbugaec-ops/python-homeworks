numbers = [(1,2),(3,1),(4,4),(5,3)]
starts = list(filter(lambda a: a[0] > a[1],numbers))
print(starts)