# Password-Checker
The Password Strength Checker is a simple yet effective Python script designed to evaluate the security of user-generated passwords. It provides feedback based on various characteristics like length, character diversity, and overall entropy, helping users understand how resistant their password might be to brute-force or dictionary attacks.
This tool is particularly useful for anyone concerned about password safety, offering real-time feedback and suggestions to create stronger credentials. By combining regular expressions and basic entropy calculation, the script gives a more analytical assessment than just labeling passwords as "weak" or "strong." It also compares the entered password against a list of commonly used passwords, warning the user if it matches any known insecure options.

✅ Key Features
Detects use of lowercase, uppercase, digits, and special characters

Calculates password entropy to measure complexity

Checks against a built-in common password list

Gives feedback or warnings about password strength

Provides security suggestions to improve weak passwords

Built With Python 3: Core programming language

re module: Used for pattern matching and character type detection

math module: Used to calculate entropy

💡 How It Works
Once the script is executed, it securely prompts the user to enter a password using getpass, which masks the input. The password is then analyzed to determine which types of characters it includes—such as lowercase letters, uppercase letters, numbers, and symbols. Based on the combination of these characters, the script calculates the potential size of the character set and estimates the password’s entropy.

Entropy, in this context, is a statistical measure used to estimate how many guesses an attacker would need to crack the password. If the password appears on the predefined list of common passwords, the script immediately flags it as insecure. Finally, a strength score and recommendation are displayed, helping users create more secure passwords.

This project is a great starting point for understanding basic cybersecurity practices and implementing password validation techniques.

