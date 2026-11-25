import string

password = input("Enter your password: ")

score = 0
feedback = []

if len(password) >= 8:
    score += 1
else:
    feedback.append("Use at least 8 characters")

if any(c.isupper() for c in password):
    score += 1
else:
    feedback.append("Add an uppercase letter (A-Z)")

if any(c.islower() for c in password):
    score += 1
else:
    feedback.append("Add a lowercase letter (a-z)")

if any(c.isdigit() for c in password):
    score += 1
else:
    feedback.append("Add a number (0-9)")

if any(c in string.punctuation for c in password):
    score += 1
else:
    feedback.append("Add a special character (@, #, $, !)")

if score <= 2:
    print("Strength: WEAK")
elif score <= 4:
    print("Strength: MEDIUM")
else:
    print("Strength: STRONG")

if feedback:
    print("Suggestions to improve your password:")
    for tip in feedback:
        print("-", tip)