from random import shuffle 
unshuffled_list = ['','O','']
def shuffle_list(a):
    shuffle(a)
    return a 

def user_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('choose a number 0,1,2')
    return int(guess)

def guess_check(a,guess):
    if a[guess] == 'O':
        print('you won!')
    else:
        print('try again!')
        print(a)
        
#first we shuffle the list 
x = shuffle_list(unshuffled_list)

#we take in the user guess 
y = user_guess()

#we compare the user guess to the guess we've recieved from the user. 
guess_check(x,y)

