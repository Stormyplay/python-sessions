print ("Welcome to the test score calculator!")

testsub = str(input("what was it a test on?"))

your_score = int(input("What score did your get on the test?")) 

test_fulmks = int(input("How much was the test out of?"))

Result = your_score/test_fulmks * 100 
print("You got", Result, "% on your", testsub,"test")

if Result >= 90:
    print("Grade A")

if Result >= 80 and Result < 90:
    print("Grade B")

if Result >= 70 and Result < 80:
    print("Grade C")

if Result >= 60 and Result < 70:
    print("Grade D")

if Result >= 50 and Result < 60:
    print ("Grade F!")

if Result <= 50:
    print("Big F")