alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1"]

c = "ABCDZ abcdz XUOie1"
d = "DEFGC defgc axrlhC"

# Encrypts string using Ceasar Cipher
def encrypt(a):
    str2 = ""
    # Loop through string character by character
    # If character is a space then add space to encrypted string
    # else finds the encrypted character and adds to the encrypted string
    for s in a:
        if s == ' ':
            str2 = str2 + ' '
        else:
            str2 = str2 + str(alphabet[(alphabet.index(s.upper()) + len(alphabet) + 3) % len(alphabet)])
    print(str2)

# Decrypts string using Ceasar Cipher
def decrypt(a):
    str2 = ""
    # Loop through string character by character
    # If character is a space then add space to decrypted string
    # else finds the decrypted character and adds to the decrypted string
    for s in a:
        if s == ' ':
            str2 = str2 + ' '
        else:
            str2 = str2 + str(alphabet[(alphabet.index(s.upper()) + len(alphabet) - 3) % len(alphabet)])
    print(str2)


