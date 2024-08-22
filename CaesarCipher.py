logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# Define the alphabet including a shift for wrapping around
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to perform the Caesar cipher encryption or decryption
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  # Adjust shift_amount based on whether it's encryption or decryption
  if cipher_direction == "decode":
    shift_amount *= -1
  # Loop through each character in the start_text
  for char in start_text:
    if char in alphabet:
      # Find the current position of the character in the alphabet
      position = alphabet.index(char)
      # Calculate the new position after shifting
      new_position = position + shift_amount
      # Append the shifted character to the end_text
      end_text += alphabet[new_position]
    else:
      # If the character is not in the alphabet (like punctuation), append it unchanged
      end_text += char
      # Print the result of encryption or decryption
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Main program execution starts here
print(logo)

# Loop until the user decides to exit
should_end = False
# Loop to handle multiple encryption/decryption requests
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26 # Ensure the shift number is within the range of the alphabet

  # Call the caesar function to perform encryption or decryption
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  # Ask user if they want to encrypt/decrypt another message
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")