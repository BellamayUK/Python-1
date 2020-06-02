grade = int(input("What score did you get on your Physics paper:")) 
if grade >=90:
    print("A")
elif (grade <=89) and (grade >=80):
    print("B")
elif (grade <=79) and (grade>=70):
    print("C")
elif (grade >=65) and (grade <=69):
    print("E")
else:
    print("F")