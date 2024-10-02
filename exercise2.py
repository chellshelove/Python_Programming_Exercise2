# Get input string from the user
input_string = input("Enter a string: ")

# Define the vowels
vowels = "aeiouAEIOU"

# Initialize a list to store the vowels found
found_vowels = [char for char in input_string if char in vowels]

# Initialize a counter for vowels
vowel_count = 0

# Loop through each character in the input string
for char in input_string:
    if char in vowels:
        vowel_count += 1

# Print the total number of vowels and the  vowels found
print("Number of vowels:", vowel_count)
print("Vowels in the string:", found_vowels)