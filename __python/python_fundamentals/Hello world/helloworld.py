# 1. TASK: print "Hello World"
print("hello World")
#answers: 
#Hello World
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("hello",name)	# with a comma
#print("hello" + name )	# with a +
#answers:
#hello Noelle
#helloNoelle
# 3. print "Hello 42!" with the number in a variable
name = 42
print("hello",name)	# with a comma
#print("hello"+ name)	# with a +	-- this one should give us an error!
#answers:
#hello 42
#TypeError: can only concatenate str (not "int") to str
#correct answer:
#print("hello"+ str(name))
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat sushi {} and {}".format(fave_food1,fave_food2)) # with .format()
print(f"I love to eat sushi {fave_food1} and {fave_food2}") # with an f string
#answers:
#I love to eat sushi sushi and pizza
#I love to eat sushi sushi and pizza