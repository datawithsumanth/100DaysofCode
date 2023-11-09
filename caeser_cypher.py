import string

repeat = 'yes'
alphabet_list = list(string.ascii_lowercase)
encrypt = ''
decrypt = ''
while repeat == 'yes':
    selection = input("type encode to encrypt and decode to decrypt\n").lower()
    msg = input("Type your message:\n").lower()
    shift_no = int(input("Type the shift number\n"))
    if selection == 'encode':
        for i in msg:
            encrypt_no = (alphabet_list.index(i) + shift_no) % 26
            encrypt += (alphabet_list[encrypt_no])
        print(encrypt)
    else:
        for i in encrypt:
            decrypt_no = (alphabet_list.index(i) - shift_no) % 26
            decrypt += (alphabet_list[decrypt_no])
        print(decrypt)

    repeat = input("Would you like to go again?\n")
