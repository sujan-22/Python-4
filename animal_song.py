#I Sujan Rokad, 000882948, certify that this work is my own effort and that I have not allowed anyone to copy from it.

"""
Author:                 Sujan Rokad
Authorship statement:   I, Sujan Rokad, 000882948, certify that this material is my original work. No other person's work has been used without due acknowledgement.
Purpose:                Print the lyrics of "Old MacDonald Had a Farm" with customizable animals and sounds.
"""

def song_printer(song):
    """
    Prints the lyrics of "Old MacDonald Had a Farm" with customizable animals and sounds.

    Args:
        song (list): A list of tuples, where each tuple contains an animal and its corresponding sound.
    """
    print("Old MacDonald had a farm, E-I E-I O!")
    for word in song:
        print("And on that farm there was a", word[0], ", E-I E-I O!")
        print(" With a ", word[1], ",", word[1], " here, and a ", word[1], ",", word[1], " there, ")
        print(" Here a ", word[1], "," , " there a ", word[1], ",", " everywhere a ", word[1], ",", word[1])
    print("Old MacDonald had a farm, E-I E-I O!")
