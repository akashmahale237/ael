import numpy as np
plain_text="AKASHNITINMAHALE"
cipher_text = ""

ak = np.reshape(list(pt), (3,4))
print(ak)

ans = np.flipud(np.fliplr(mat1))
print(ans)


for i in range(4):
    for j in range(3):
        if result[j,i] != ' ':
            cipher_text = cipher_text + result[j,i]
            print(result[j,i])

print(cipher_text)

