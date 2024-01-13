# I Sujan Rokad, 000882948, certify that this work is my own effort and that I have not allowed anyone to copy from it.

"""
Author:                 Sujan Rokad
Authorship statement:   I, Sujan Rokad, 000882948, certify that this material is my original work. No other person's work has been used without due acknowledgement.
Purpose:                Create a custom animal song based on user input and print the lyrics using the song_printer function.
"""

from animal_song import song_printer

song = []

# Collect user input for animals and their sounds
while True:
    animal_name = input("Please enter an animal name (or type 'done' to quit): ")
    if animal_name.lower() == "done":
        break
    
    animal_sound = input("Please enter an animal sound (or type 'done' to quit): ")
    if animal_sound.lower() == "done":
        break
    
    song.append([animal_name, animal_sound])

# Print the custom animal song using the song_printer function
song_printer(song)
