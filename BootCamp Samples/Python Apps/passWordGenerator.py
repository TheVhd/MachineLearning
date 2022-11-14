import random
import string

def keyGen():
    letters1 = string.ascii_lowercase
    letter2 = string.ascii_uppercase
    letter3 = string.ascii_letters
    dgts1 = string.digits
    dgts2 = string.punctuation
    lowerLttr = [''.join(random.choice(letters1))for i in range(3)]
    dgts_3 = [''.join(random.choice(dgts2)) for i in range(2)]
    upperLttr = [''.join(random.choice(letter2))for i in range(3)]
    dgts_2 = [''.join(random.choice(dgts2)) for i in range(2)]
    lttrs = [''.join(random.choice(letter3))for i in range(3)]
    dgts_1 = [''.join(random.choice(dgts1))for i in range(3)]
    passKey = lowerLttr + dgts_3 + upperLttr + dgts_2 + lttrs + dgts_1
    psswrd = ''.join(passKey)
    print(psswrd)
    return psswrd

keyGen()
