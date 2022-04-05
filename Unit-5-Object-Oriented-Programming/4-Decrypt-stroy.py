"""
Problem 4 - Decryption

Now that you have all the pieces to the puzzle, please use them to decode the
file story.txt. The file ps6.py contains a helper function get_story_string()
that returns the encrypted version of the story as a string. Create a
CiphertextMessage object using the story string and use decrypt_message to
return the appropriate shift value and unencrypted story string.
"""


def decrypt_story():
    """
    returns: a tuple of the appropriate shift value and unencrypted story string
    """
    story = CiphertextMessage(get_story_string())
    return story.decrypt_message()
