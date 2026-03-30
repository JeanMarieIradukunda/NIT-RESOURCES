# Prompt user to enter names
names = input("Enter your names: ")

#variable for storing subjects
subjects = []
#Loop subject one by one in recording from user keyboard
for x in range(3):
    subject = input("Enter subject: ")
    subjects.append(subject)
#print the usernames with message
print('\n Subjects recorded by', names + "are:")

#Print out the recorded subjects from subjects variable
for s in subjects:
    print("-"+s)

