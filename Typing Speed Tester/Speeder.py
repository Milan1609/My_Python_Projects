from time import *
import random as r

#  to check the errors in user input and count it .
def unsound_words(par_test,user_test):
    error = 0
    for i in range(len(par_test)):
        try:
            if par_test[i] != user_test[i]:
                error = error + 1
        except :
            error = error + 1
    return error

#To check time of typing speed of user.
def  speed_time(start_t,end_t,user_input):
    delay_time = end_t - start_t
    time_r = round(delay_time, 2)
    speed = len(user_input) / time_r
    return round(speed)

if __name__ == '_main_' :

    while True:
        hi = input(' Start Your Test : yes / no :- ')
        if hi == 'yes':

            test = ["The quick brown fox jumps over the lazy dog.",
                    "Now is the time for all good men to come to the aid of their country.",
                    "Don't make a mountain out of a molehill.",
                    "Friends are flowers in the garden of life.",
                    "What a beautiful day it is on the beach, here in beautiful and sunny Hawaii.",
                    "A bird in the hand is worth two in the bush."]  # for random sentances , we  are using list .

            test1 = r.choice(test)   # it gives us a chosie of one of the string  from the list .

            print("*****-------->>>>>>> Typing Speed <<<<<<-------*****")

            print(test1)
            print()
            print()

            time_01 = time()
            testing = input("  Enter the sentence here  :- ")
            time_02 = time()

            print('Typing Speed :- ' , speed_time(time_01,time_02,testing) , 'w/sec')  # this will show your speed in woed per secand .
            print(' Error :- ' , unsound_words(test1,testing))   # This will show your number of errors in our input . 

        elif hi == 'no':
            print(' Thank you for visiting my side.')
            break

        else:
            print(' Wrong Input . Plase check your input value .')
