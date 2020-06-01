grade = int(input("What score did you get on your Physics paper:")) 
if grade >= 85:
    print("Distinction")
elif (grade <= 85) and (grade >=65 ):
    print("Pass")
else:
    print("Fail")