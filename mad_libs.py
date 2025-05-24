# Mad Libs Project
# Developed by Shumaila Usmani

# Introduction
print("🎉 Welcome to the Mad Libs Story Generator!")
print("Let's create a funny story. Answer the following prompts.\n")

# Getting inputs from the user
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
emotion = input("Enter an emotion: ")

# Creating the story using f-string
story = f"""
One day, {name} was walking through the {place} feeling very {adjective}.
Suddenly, they saw a mysterious {noun} lying on the ground.
Without thinking, {name} decided to {verb} it.
This made them feel extremely {emotion}, and they couldn't stop laughing!
It was definitely a day to remember!
"""

# Displaying the story
print("\n📖 Here’s your Mad Libs story:")
print(story)
