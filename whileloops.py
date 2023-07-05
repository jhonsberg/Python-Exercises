"""
Title: While Loops
Name: Jonah Honsberger
Date: 09/24/2022 [MM-DD-YYYY]
"""

# keep count of attempts
attempt=0

# while the attempt counter is under 3 and pin is correct, print 'Access Granted'
while attempt < 3:
    pin = input('Enter PIN Code: ')
    if pin == '2357':
        print('Access Granted')
        break
    # if attempt is incorrect +1 to attempt counter
    else:
        attempt += 1
        # when user runs out of attempts, print 'Access Denied'
        if attempt == 3:
            print('Access Denied')
        # while the attempt counter is under 3, print 'Invalid PIN Number.'
        elif attempt <3:
            print('Invalid PIN Number.')