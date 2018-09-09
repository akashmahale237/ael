

#Substitution cipher
pt  = 'PRATHAMESH'
#pt = 'ABYZ'
key = [5,8,3]
num = 2
ct = ""
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']        #ASCII values A:65 and Z:90

for i in range(len(pt)):
    num = (num+1)%3
    if (ord(pt[i]) + key[num]) < 91:
        ct = ct + chr(ord(pt[i]) + key[num])
    else:
        ct = ct + chr(ord(pt[i]) + key[num] - 26)
    #print(i,num)
print(ct)


#ROT-13

ct = ""

for i in range(len(pt)):
    if (ord(pt[i]) + 13) < 91:
        ct = ct + chr(ord(pt[i]) + 13)
    else:
        ct = ct + chr(ord(pt[i]) + 13 - 26)
    #print(i,num)
print(ct)

#Transposition

import math
ct = ""

for i in range(4):
    for j in range(math.ceil(len(pt)/4)):
        if i+4*j <= len(pt)-1:
            ct = ct + pt[i+4*j]
            print(i,j,i+4*j)
print(ct)

#Double Transposition

import numpy as np
ct = ""
pt = 'PRATHAMESH  '
#for i in range(len(pt)):
mat1 = np.reshape(list(pt), (3,4))
print(mat1)

result = np.flipud(np.fliplr(mat1))
print(result)


for i in range(4):
    for j in range(3):
        if result[j,i] != ' ':
            ct = ct + result[j,i]
            print(result[j,i])

print(ct)

#Vernam Cipher
pt = 'PRATHAMESH'
ct = ""

random = 'ABCDEFGHIJ'

for i in range(len(pt)):
    if (ord(pt[i]) + ord(random[i])-65) < 91:
        ct = ct + chr(ord(pt[i]) + ord(random[i])-65)
    else:
        ct = ct + chr(ord(pt[i]) + ord(random[i]) - 65 - 26)

print(ct)

#Diffie Hellman

ga = 7
pa = 13

gb = 23
pb = 11

xa = 6
xb = 9

ya = pow(ga,xa)%pa
yb = pow(gb,xb)%pb

print('Ya and Yb to be exchanged are:',ya,yb)

ska = pow(yb,xa)%pa
skb = pow(ya,xb)%pb

print('Secret Key at Alice is',ska)
print('Secret Key at Bob is',skb)

UPDATED CODE with PPP’s Output:


#Substitution cipher
pt  = 'PRATHAMESH'
#pt = 'ABYZ'
key = [5,8,3]
num = 2
ct = ""

for i in range(len(pt)):
    num = (num+1)%3
    if (ord(pt[i]) + key[num]) < 91:
        ct = ct + chr(ord(pt[i]) + key[num])
    else:
        ct = ct + chr(ord(pt[i]) + key[num] - 26)
    #print(i,num)
    
print('Plaintext:',pt)
print('Ciphertext:',ct)

#ROT-13

ct = ""

for i in range(len(pt)):
    if (ord(pt[i]) + 13) < 91:
        ct = ct + chr(ord(pt[i]) + 13)
    else:
        ct = ct + chr(ord(pt[i]) + 13 - 26)
    #print(i,num)

print('Plaintext:',pt)
print('Ciphertext:',ct)


#Transposition

import math
ct = ""

for i in range(4):
    for j in range(math.ceil(len(pt)/4)):
        if i+4*j <= len(pt)-1:
            ct = ct + pt[i+4*j]


print('Plaintext:',pt)
print('Ciphertext:',ct)



#Double Transposition

import numpy as np
ct = ""
pt = 'PRATHAMESH  '
#for i in range(len(pt)):
mat1 = np.reshape(list(pt), (3,4))
#print(mat1)

result = np.flipud(np.fliplr(mat1))
#print(result)


for i in range(4):
    for j in range(3):
        if result[j,i] != ' ':
            ct = ct + result[j,i]
            #print(result[j,i])

print('Plaintext:',pt)
print('Ciphertext:',ct)



#Vernam Cipher
pt = 'PRATHAMESH'
ct = ""

random = 'ABCDEFGHIJ'

for i in range(len(pt)):
    if (ord(pt[i]) + ord(random[i])-65) < 91:
        ct = ct + chr(ord(pt[i]) + ord(random[i])-65)
    else:
        ct = ct + chr(ord(pt[i]) + ord(random[i]) - 65 - 26)

print('Plaintext:',pt)
print('Ciphertext:',ct)



#Diffie Hellman

ga = 7
pa = 13

gb = 23
pb = 11

xa = 6
xb = 9

ya = pow(ga,xa)%pa
yb = pow(gb,xb)%pb

print('Ya and Yb to be exchanged are:',ya,yb)

ska = pow(yb,xa)%pa
skb = pow(ya,xb)%pb

print('Secret Key at Alice is',ska)
print('Secret Key at Bob is',skb)



