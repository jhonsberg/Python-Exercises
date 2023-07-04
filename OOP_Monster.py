"""
Title: OOP Monster
Name: Jonah Honsberger
Date: 11/03/2022 [MM-DD-YYYY]
"""

class Monster():
    def __init__(self, name, health):
        # Constructor
        self.name = name
        self.health = health

def main():
    # This creates the dog
    new_monster = Monster("Fluffy", 100)
    print("Monster's Name:", new_monster.name, "\n" " Health:", new_monster.health)

main()