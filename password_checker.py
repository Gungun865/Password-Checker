import re
import math
import getpass


common_passwords = ['123456', 'password', '123456789', 'qwerty', 'abc123', '111111', '123123', 'iloveyou']

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[^A-Za-z0-9]', password): charset += 32  
    entropy = len(password) * math.log2(charset) if charset else 0
    return round(entropy, 2)

def estimated_crack_time(entropy):
    guesses = 2 ** entropy
    guesses_per_second = 1e9  
    seconds = guesses / guesses_per_second
    return convert_seconds(seconds)

def convert_seconds(seconds):
    if seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds / 60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds / 3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds / 86400)} days"
    else:
        return f"{int(seconds / 31536000)} years"

def password_strength(password):
    strength = 0
    feedback = []

    if password.lower() in common_passwords:
        feedback.append("Your password is too common. Choose a more unique one.")
        return "Very Weak", feedback, 0, 0

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")
  
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Add at least one digit.")

    if re.search(r'[^A-Za-z0-9]', password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    if strength == 5:
        rating = "Very Strong"
    elif strength >= 4:
        rating = "Strong"
    elif strength >= 3:
        rating = "Moderate"
    elif strength >= 2:
        rating = "Weak"
    else:
        rating = "Very Weak"

    entropy = calculate_entropy(password)
    return rating, feedback, strength * 2, entropy

if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐")
    password = getpass.getpass("Enter your password (input hidden): ")

    result, feedback, score, entropy = password_strength(password)
    crack_time = estimated_crack_time(entropy)

    print(f"\nStrength: {result}")
    print(f"Score: {score}/10")
    print(f"Entropy: {entropy} bits")
    print(f"Estimated Time to Crack: {crack_time}")

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print("- " + f)
