def iterateDictionary(some_list):
    for x in (some_list):
        print(x)
def iterateDictionary2(key_name,some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)