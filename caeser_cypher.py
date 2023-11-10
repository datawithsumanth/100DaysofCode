import string
from art import cc_logo

repeat = 'yes'
alphabet_list = list(string.ascii_lowercase)
print(cc_logo)
def caeser_cypher( msg, shift_no, selection):
    cypher_text=''
    if selection == 'decode':
        shift_no *= -1 * shift_no

    for i in msg:
        if i in alphabet_list:
            encrypt_no = (alphabet_list.index(i) + shift_no) % 26
            cypher_text += (alphabet_list[encrypt_no])
        else:
            cypher_text += i
    return cypher_text

while repeat == 'yes':
    selection = input("type encode to encrypt and decode to decrypt\n").lower()
    msg = input("Type your message:\n").lower()
    shift_no = int(input("Type the shift number\n"))
    print(caeser_cypher(msg, shift_no, selection))
    repeat = input("Would you like to go again?\n")
else:
    print("Goodbye!")
