age = input(str('Are you over 75 years old and a smoker?: YES or NO: '))
disease = input(str('Do you have a severe chronic disease?: YES or NO: '))
weakness = input(str('Is your immune system too weak?: YES or NO: '))
if age == 'yes':
    age = False
elif age == 'no' :
    age = True
if disease == 'yes' :
    disease = False
elif disease == 'no' :
    disease = True
if weakness == 'yes' :
    weakness = False
elif weakness == 'no' :
    weakness = True
result = (weakness and age and disease)

if result == False :
    print('You are in the risk group!')
elif result == True :
    print('Well done! You are not in the risk group.')
