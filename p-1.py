import datetime
#----step 1 : welcome and instruction----
print('welcome to the interractive personal data collecter!')
print('='*55)
print('this program collects basic setails about you,dempnstrates')
print('python dsts types ,type casting ,and inspects memory addresses.\n')

#---steps 2: collects information with type casting ----
name=input('Enter youe name:')

#type casting input string to int and float 
age=int(input('Enter your age:'))
height=float(input('Enter your hight in meters:'))
favorite_numbers=int(input('Enter your favorite number:'))

#----step 3: data processing & arithmetic operations-----
#calculate approximate birth year 
current_year=datetime.datetime.now().year
birth_year=current_year-age
#convert float height to an integer (demonstrating explicit type casting)
rounded_height=int(height)

#===== step 4:display result and summary -----
print('\n'+'-'*50)
print('USER SUMMARY')
print('-'*50)
print(f'hello {name}!')
print(f'Based on your age({age}),you were born on around({birth_year}).')

print('\n'+'='*50)
print('TYPE CASTING DEMONSTRATION')
print('-'*50)
print(f'orignal float height:{height} ({type(height)})')
print('Explanation:converting float to int truncates the decimal portion.')

#---- step 5: variable inspection using type() and id ()----
print('\n'+'')