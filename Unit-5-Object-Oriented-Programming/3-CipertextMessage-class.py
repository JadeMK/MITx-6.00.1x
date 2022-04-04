"""
Problem 3 - CipertextMessage

Given an encrypted message, if you know the shift used to encode the message,
decoding it is trivial. If message is the encrypted message, and s is the shift
used to encrypt the message, then apply_shift(message, 26-s) gives you the
original plaintext message. Do you see why?

The problem, of course, is that you don’t know the shift. But our encryption
method only has 26 distinct possible values for the shift! We know English is
the main language of these emails, so if we can write a program that tries each
shift and maximizes the number of English words in the decoded message, we can
decrypt their cipher! A simple indication of whether or not the correct shift
has been found is if most of the words obtained after a shift are valid words.
Note that this only means that most of the words obtained are actual words.
It is possible to have a message that can be decoded by two separate shifts
into different sets of words. While there are various strategies for deciding
between ambiguous decryptions, for this problem we are only looking for a
simple solution.
"""


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text
        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.
        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return
        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        shifted = 0
        decrypted_best = 0
        decrypted_result = ""
        for i in range(26):
            decrypted_text = self.apply_shift(i)
            words = decrypted_text.split(' ')
            decrypted = sum([is_word(self.get_valid_words(), j) for j in words])
            if decrypted > decrypted_best:
                shifted = i
                decrypted_best = decrypted
                decrypted_result = decrypted_text
        return (shifted, decrypted_result)
