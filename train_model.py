url = input("Enter URL: ")

# Rules
if "https" not in url:
    print("⚠️ Not Secure (HTTPS is missing)")

elif len(url) > 30:
    print("⚠️ Suspicious (URL is too long)")

elif "@" in url or "-" in url:
    print("⚠️ Suspicious (Strange characters detected)")

elif "login" in url or "verify" in url or "bank" in url:
    print("⚠️ Possible Phishing Website")

else:
    print("✅ Safe URL")
    