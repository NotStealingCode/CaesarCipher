from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  while shift_amount > 26:
      shift_amount -= 26
      
  if cipher_direction == "decode":
    shift_amount *= -1
      
  for char in start_text:
    if char not in alphabet:
        end_text += char
    else:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    
  print(f"\nHere's the {cipher_direction}d result: {end_text}")

print(logo)
restart_program = True
while restart_program == True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("\nType 'yes' if you wish to go again otherwise type 'no' to end the program.\n").lower()
    if result == "yes":
        restart_program = True
    else:
        restart_program = False