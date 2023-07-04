"""
Title: Short Story Generator
Name: Jonah Honsberger
Date: 10/28/2022 [MM-DD-YYYY]
"""


print('Enter your name: ')
name = input()

print('Enter a noun: ')
noun = input()

print('Enter a verb: ')
verb = input()

print('Enter an adjective: ')
adj = input()

print('Enter an adverb: ')
adv = input()

# generate story from variables given
print(
   name + ' was walking one day when he suddenly saw ' + noun + ' that was ' + adv + ' ' + verb + " but in a " + adj +
   ' way. But it suddenly disappeared so he assumed it must have been a hallucination.'
)
