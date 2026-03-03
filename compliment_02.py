# FILE NAME - compliment_02.py

# NAME: Evan Beer
# DATE: 3/3/26
# BRIEF DESCRIPTION: Does the same thing as compliment_01 but with an extra message if you don't want a compliment.  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YOUR CODE BELOW THIS LINE ##########

def main():
    compliment_giver()

def compliment_giver():
    Choice = input('Would you like a compliment? ')
    
    if Choice == 'yes':
        print("You have wonderful eyes.")

    else: print('No compliment for you!')
    print('Thank you for playing.')

main()








########### END YOUR CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Would you like a compliment? yes
You have wonderful eyes.
Thank you for playing.
'''


'''
Would you like a compliment? Yes
No compliment for you!
Thank you for playing.
'''


'''
Would you like a compliment? y
No compliment for you!
Thank you for playing.
'''


'''
Would you like a compliment? no
No compliment for you!
Thank you for playing.
'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you struggle with this lab (YES/NO)?

No it was easy because I just took the compliment_01 code and added the new message line of code to it and it worked.






'''
