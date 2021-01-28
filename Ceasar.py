alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
#The alphabet is written two times for the case if the user wants to encrypt the letter Z 
encrypt = input("Enter your message: ")
key = int(input("Enter desired key(number from 1 to 25): "))
encrypt = encrypt.lower()
encrypted = ""

for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else: 
        encrypted = encrypted + letter

print("Your cipher is: ", encrypted)
