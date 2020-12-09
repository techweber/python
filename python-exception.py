# simple try exception block code
# try:
# 	print(x)
# except:
# 	print("An exception has occurred")

# Many exceptions example
# try:
# 	print(x)
# except NameError:
# 	print("Variable x is not defined")
# except:
# 	print("Something else went wrong")

# example of using else block with try except block
# try:
# 	print("Hello")
# except:
# 	print("Something went wrong")
# else:
# 	print("Nothing went wrong")

# finally block example
# try:
# 	print(x)
# except:
# 	print("something went wrong")
# finally:
# 	print("Finally we are here")

# example to raise and exception

# x = -1

# if x < 0:
# 	raise Exception("Sorry, no numbers below zero")


#example raise an exception if variable is not an integer

x = "Hello"

if not type(x) is int:
	raise TypeError("Only integers are allowed")



