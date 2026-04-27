import tkinter as tk

def check_url():
    url = entry.get().lower()
    
    if "https" not in url:
        result.config(text="⚠️ Not Secure (HTTPS is missing)")
    elif len(url) > 30:
        result.config(text="⚠️ Suspicious (URL too long)")
    elif "@" in url or "-" in url:
        result.config(text="⚠️ Suspicious (Strange characters)")
    elif "login" in url or "verify" in url or "bank" in url:
        result.config(text="⚠️ Possible Phishing Website")
    else:
        result.config(text="✅ Safe URL")

root = tk.Tk()
root.title("Phishing Detector")
root.geometry("400x250")   # 👈 thoda bada size

# Label
label = tk.Label(root, text="Enter URL:")
label.pack(pady=5)

# Input box
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Button
btn = tk.Button(root, text="Check URL", command=check_url)
btn.pack(pady=10)

# Result
result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=10)

root.mainloop()
