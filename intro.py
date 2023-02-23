print("Hello, World!")

print(55*4)

majina= 'OJ'

print(majina)


points=1,2,3

print(points)

teamkubwa='Arsenal'

print(teamkubwa)

#Multi way

BMI = 23
if BMI<10:
    print('malnurished')
elif BMI <17:
    print('medium')
else:
    print('normal')
print('Done')


#Functions

def course():
    print('Economics')
    print('Statistics')

course()


#Parameters

def book(genre):
    if genre=='fic':
        print('Fiction')
    elif genre=='ac':
        print('action')
    else:
        print('comedy')

book('fic')


#Return functions

def book(genre):
    if genre=='fic':
        return 'Fiction'
    elif genre=='ac':
        return 'action'
    else:
        return 'comedy'
    
print(book('ac'),'scenes')


#Loops
 #FOR Loop

for h in [5,4,3,2,1]:
    print(h) 
print('Blastoff!')  

friends=['John','Mesis','Sawe']
for friend in friends:
    print('How are you:',friend)

#To break after a specific friend

    friends=['John','Mesis','Sawe']
for friend in friends:
    if friend=='Mesis':
        break
    print('How are you:',friend)

#While loop

n=-4
while n < 0:
    print(n)
    n=n+1
print('Blastoff!')
print(n)




largest_so_far=1
print('Before',largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far= the_num
    print(largest_so_far,the_num)

print('After',largest_so_far)   