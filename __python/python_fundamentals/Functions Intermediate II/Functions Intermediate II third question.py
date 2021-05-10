
def printInfo(some_dict):
    for x in some_dict:
        print(len(dojo[x]), x)
        for y in some_dict:
            print(some_dict[x])
        


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
