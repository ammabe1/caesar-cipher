abc = "abcdefghijklmnopqrstuvwxyz"

shft = int(input("Please enter the number of places to shift: "))
pln_txt = input ("Please enter a sentence: ")
pln_txt = pln_txt.lower()

cipher_txt = ""

for char in pln_txt:
    if char in abc:
        char_index = abc.find(char)
        char_index = (char_index + shft) % 26
        char = abc[char_index]
    cipher_txt += char
    
print(cipher_txt)
