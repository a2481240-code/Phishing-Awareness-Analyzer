# ==========================================
# PHISHING AWARENESS ANALYZER
# DecodLabs Internship Project
# Author: Abdullah
# Language: Python
# ==========================================

print("==========================================")
print("       PHISHING AWARENESS ANALYZER")
print("==========================================")

# Get message from user
message = input("Message: ")
message = message.lower()

# Starting values
risk_score = 0
red_flags = []

# Suspicious keywords
suspicious_keywords = [
    "urgent",
    "password",
    "click here",
    "verify",
    "account",
    "login",
    "bank",
    "security",
    "update",
    "confirm"
]

# Check suspicious keywords
for keyword in suspicious_keywords:
    if keyword in message:
        red_flags.append(f"Suspicious keyword: {keyword}")
        risk_score += 1

# Sensitive information
sensitive_keywords = [
    "otp",
    "pin",
    "passcode",
    "verification code"
]

# Check sensitive information requests
for keyword in sensitive_keywords:
    if keyword in message:
        red_flags.append(
            f"Sensitive information request: {keyword}"
        )
        risk_score += 1

# Check for suspicious links
if "http://" in message or "https://" in message:
    red_flags.append("Suspicious link")
    risk_score += 1

# Common phishing phrases
phishing_phrases = [
    "your account has been compromised",
    "you have won a prize",
    "your account will be suspended",
    "verify your identity",
    "update your payment information"
]

# Check phishing phrases
for phrase in phishing_phrases:
    if phrase in message:
        red_flags.append(f"Phishing phrase: {phrase}")
        risk_score += 1

# Determine risk level
if risk_score <= 1:
    risk_level = "LOW"
elif risk_score <= 3:
    risk_level = "MEDIUM"
else:
    risk_level = "HIGH"


# ==========================================
# ANALYSIS RESULTS
# ==========================================

print("\nMessage:")
print(message)

print("\n---")
print("ANALYSIS RESULTS")
print("---")

print(f"\nRisk Score : {risk_score}")
print(f"Risk Level : {risk_level}")

print("\nRed Flags Detected:")

if len(red_flags) == 0:
    print("No suspicious indicators detected.")
else:
    for number, flag in enumerate(red_flags, 1):
        print(f"[{number}] {flag}")

# Security recommendation
print("\n---")
print("Security Recommendation:")

if risk_level == "HIGH":
    print("Do not click links or share personal information.")
    print("Verify the sender through an official source.")

elif risk_level == "MEDIUM":
    print("Be careful and verify the sender before taking action.")

else:
    print("No major suspicious indicators were detected.")

print("\n---")
print("Analysis Complete")
print("==========================================")