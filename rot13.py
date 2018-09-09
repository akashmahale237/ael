#ROT13 CIPHER
plain_text="AKASH"
cipher_text = ""

for i in range(len(plain_text)):
    if (ord(plain_text[i]) + 13) < 91:
        cipher_text = cipher_text + chr(ord(plain_text[i]) + 13)
    else:
        cipher_text = cipher_text + chr(ord(plain_text[i]) + 13 - 26)
print(cipher_text)

