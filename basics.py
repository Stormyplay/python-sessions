print("===== CREATE YOUR AI DEVELOPER PROFILE =====")


name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_subject = input("Enter your favorite school subject: ")
dream_ai_project = input("What AI project would you like to build someday? ")

future_year = 2025 + (18 - int(age))


print("\n===== YOUR AI DEVELOPER PROFILE =====")
print("Name:", name)
print("Current Age:", age)
print("Favorite Subject:", favorite_subject)
print("Dream AI Project:", dream_ai_project)
print("By the year", future_year, "you'll be 18 and could be working on advanced AI!")
print("If you practice Python for just 30 minutes every day, by then you'll have practiced for over", (18 - int(age)) * 365 * 0.5, "hours!")
print("That's enough to become an expert!")

Ainame= input("what is my name? ")
print(" OK! From now on my name is", Ainame)

problem = input(" what would you like me to do first?")
print( "unfortunately the", problem, "feature is still under development")

shutdown = input ("you have reached maximum number of requests, shutdown? (yes/no) ")

if shutdown == "yes":
    print ("goodbye!")

if shutdown == "no":
    print ("to continue using", Ainame, "pay premium")

else: print ("please choose from yes/no")
