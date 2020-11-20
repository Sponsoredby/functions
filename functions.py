def my_function():
    print ("This is my first function: ")
    print ("This is a very basic & boring use of a custom function: ")
my_function()

print ("\nIn the next section I create a custom function with an arguement, the argument is 'country' \n")

def food_function(country):
    if country == "england":
        print ("Fish and Chips")
    elif country == "jamaica":
        print ("Ackee & Saltfish")
    else:
        print ("Sandwiches")

food_function("england")
food_function("")
food_function("jamaica")

print ("\nSo an example could be for a restaraunt and the question is whats on the menu for lunch?\n")
print ("Todays lunch menu is: \n")
food_function("")

print ("\nWhats on the menu for dinner? ")
print ("Todays dinner menu is: \n ")
food_function("england")
food_function ("jamaica")

print ("\nNext functions with return values using hello from various countries:")


name = input ("Please enter your name: ")
def my_lang(lang):
    if lang == "es":
        return "hola"
    elif lang == "fr":
        return "bonjour"
    elif lang =="de":
        return "guten tag"
    else:
        return "hello"

print (my_lang("es"),name)
print (my_lang("fr"),name)
print (my_lang("de"),name)
print (my_lang(""),name)
