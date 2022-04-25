import os

with open('shuffled_ciphers') as f:
    ciphers = [s.split() for s in f.readlines()]

for i in range(1, len(ciphers) + 1):

    for cipher in ciphers:
        command = "openssl enc -d {0} -k {1} -md md5 -in ciphertext{2} -out ciphertext{3} ".format(cipher[0], cipher[1], i, i + 1)
        error = os.system(command)

        if error == 0:
            print(i)
            ciphers.remove(cipher)
            break
with open('ciphertext' + str(i + 1)) as f:
    print(f.read())















