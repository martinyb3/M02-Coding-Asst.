# m02-Asst - Encrypt/Decrypt Demo 
# author: myb
# created: 2026-03-30  
# IDE: visual studio code
# program of encrypting and decrypting using symmetric and asymmetric method
# CODING ASSISTANCE was used in this program

# Encrypt/Decrypt - Symmetric Method 
# CodeAssist-AI: Used to explain how to write encrypting and decrypting code using symmetric method

#Step 1: Install cryptography library and import Fernet
from cryptography.fernet import Fernet

#Step 2: 
key = Fernet.generate_key() #Generate encrypted code to use as my key
cipher_text = Fernet(key)   #prepare a cryptographic algorithm with the generated code so that it can begin producing secure outputs.
                            #cipher_text becomes a Live Object. It is now an active "engine" that sits in your computer's memory, ready to perform tasks.

#Step 3: Create the secret message; .encode() method converts the message to computer lang. (bytes and bits)
message = "This is a secret message".encode()

#Step 4: Encrypt message
encrypted_message = cipher_text.encrypt(message) #turns my message into a string of unreadable ciphertext 

#Step 5: Revert message back to original bytes
plain_text = cipher_text.decrypt(encrypted_message)

print()
print()

#Step 6: Decode original message
print("Symmetric Method")
print(f"Decryptic Message: {plain_text.decode()}")

print()
print()

# Encrypt/Decrypt - Asymmetric Method 
# CodeAssist-AI: Used to explain how to write encrypting and decrypting code using asymmetric method

import rsa  

# 1: Generate the Public and Private keys
# (pubkey is for locking, privkey is for unlocking)
pubkey, privkey = rsa.newkeys(512)

# 2: The secret message (must be converted to bytes)
message = "For your eyes only!".encode('utf8')

# 3: Encrypt the message using the Public Key
ciphertext = rsa.encrypt(message, pubkey)
print("Asymmetric Method")
print(f"Encrypted: {ciphertext.hex()[:50]}...")

# 4: Decrypt the message using the Private Key
decrypted_message = rsa.decrypt(ciphertext, privkey)
print(f"Decrypted Message: {decrypted_message.decode('utf8')}")

print()
print()