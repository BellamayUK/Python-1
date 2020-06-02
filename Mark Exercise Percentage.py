maths_marks=int(input('Please enter your Maths Marks here: ')) 
chemistry_marks=int(input('Please enter your Chemistry Marks here: ')) 
physics_marks=int(input('Please enter your Physics Marks here: ')) 
 
total_marks= maths_marks + chemistry_marks + physics_marks
final_marks=float((total_marks/300) *100 )

print (final_marks)

if final_marks < 40:
    print('You failed')
elif (final_marks >= 40) and (final_marks <= 49):
    print('You got a D')
elif (final_marks >=50) and (final_marks <=59):
    print('You got a C')
elif (final_marks >=60) and (final_marks <=69):
    print ('You got a B')
else:
    print('You got an A')

 

