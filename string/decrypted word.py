'''
 Input is an encrypted  string where there will be chars followed by number. The way to decrypt is 
to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special 
chars, all the chars between the number and special char are ignored.
eg - ac2bd3 means acacbdbdbd. 
ac2acc#cd3 acaccdcdcd

'''
import re

encrypted_str = input("Enter the encrypted string: ")
decrypted = ""

# Define a regular expression pattern to match the encoded parts
pattern = r'([A-Za-z]+)(\d+)'

# Find all matches in the encrypted string
matches = re.findall(pattern, encrypted_str)

for match in matches:
    chars_to_repeat, num = match
    num = int(num)

    # Repeat the characters and append to the decrypted string
    decrypted += chars_to_repeat * num

print(f"Decrypted String: {decrypted}, Length: {len(decrypted)}")
