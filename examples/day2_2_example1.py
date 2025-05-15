
def hello():                # Definition of a function
    print("hello, world!!")

hello()                     # Calling the function

def hello(word):            # Definiton of a function with argument
    print("hello,", word)

hello("python!!")           # Calling the function with an argument

def hello(word):            # Definiton of a function with argument and return value
    sentence = "hello, %s!!" % word
    return sentence

x = hello("bio334")         # Calling the function with arugment and the return value is assined to a variable
print(x)
