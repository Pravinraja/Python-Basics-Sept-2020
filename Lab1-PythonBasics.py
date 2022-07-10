#Problem 1)

    #Ask the User for their Name and their favorite number
    #Print to screen "Hi <name>, your favorite number is <number>" replace <> with their input
    #If there favorite number is greater than 10 tell them "they think big"
    #If their favorite number is less than 10 tell them "Think bigger next time!"


name = input("Enter your name: ") 
#print(name) 
number= input("Enter your favorite number ")
print(f"Hi {name}, your favorite number is {number}")
if int(number)>10:
    print("you think big")
else:
    print("think bigger next time")


#Problem 2)

#Create a List of 10 Natural language names (English, Icelandic ...)
#Print to the screen the first 3 languages
#Print to screen the last language
#Ask the User to add one language to the previous list
#Loop through the List and print each to screen

List = ["English", "Spanish", "Tamil", "French", "Latin", "German", "Japanese", "Mandarin", "Hindi", "Urdu"]
print(f"the first 3 languages are {List[:3]}")
print(f"the last language is {List[-1]}")
number= input("Hello, please add another language to the list ")
List.append(number)
print(List)
for i in List: 
    print(i) 

#Problem 3)

    #Create a Dictionary of names and ages i.e names={'nathan':37} make sure there are at least 10 entries
    #Ask the user for a name
    #Print of "that user is <age> years old
    #If the user does not exist, tell the user "I do not know that user
    
UserAge =	{
  "Kumar": 23,
  "David": 20,
  "Ford": 41,
  "Jackson": 30,
  "Martha": 40,
  "Bruce": 24,
  "Arthur": 20,
  "Thomas": 10,
  "Penny": 29,
  "Sophie": 88,
}
List = input('Please enter your name to search ')
#for i in thisdict.values(): 
for user, age in UserAge.items(): 
    #print(i)
    if user == List:
        print(f"The user {user} age is {age} ")
        break
else:
    print("the user does not exist")

#Problem 4)

    #Write a function (make_a_name) that creates a celebrity nickname
   # The function should take two names as parameters
  #  The function should combine the first 3 letters of the first parameter with the last 3 letters of the second parameter
 #   Print out the new name
#    For example make_a_name(Mary  Jones,John Smith) should print Marith
def make_a_name(firstname, lastname):  
    firstname_3 = firstname[:3]
    lastname_3 = lastname[-3:]
    print(f"the first 3 letters of the first parameter with the last 3 letters of the second parameter {firstname_3}{lastname_3}")

make_a_name("Mary Jones", "John Smith")
