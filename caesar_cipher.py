from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char.isalpha():
            shifted_position = alphabet.index(char) + shift_amount
            shifted_position %= len(alphabet)
            output_text_char = alphabet[shifted_position]
            output_text += output_text_char
        else:
            output_text += char
    print(f"Here is the {encode_or_decode}d result: {output_text}")

while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if restart != "yes":
        print("Goodbye!")
        break
