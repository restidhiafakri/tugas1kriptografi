print ("Tugas 01 Kriptografi")
print ("Nama : Resti")
print ("Nim  : E1E1 19 012")

def encript(plaintext, key):
    encoded = []

    for i in range(len(plaintext)):
        xor = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encoded.append(chr(xor))

    return ''.join(encoded)

def decript(chipertext, key):
    return encript(chipertext, key)

def main():
    print('Pilih Menu: \n1. Enkripsi\n2. Dekripsi')
    pilihan = int(input('Input Pilihan: '))

    if pilihan == 1:
        plaintext = str(input('Input plaintext: '))
        key = str(input('Input key: '))

        print('Plaintext: ', plaintext)
        print('Enkripsi: ', encript(plaintext, key))
    elif pilihan == 2:
        chipertext = str(input('Input chipertext: '))
        key = str(input('Input key: '))

        print('Chipertext: ', chipertext)
        print('Dekripsi: ', decript(chipertext, key))
    else:
        exit()

main()
