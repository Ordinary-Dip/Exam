s = "madam"
reverse = ""
for ch in s:
    reverse = ch + reverse
if s == reverse:
    print("panlindrom")
else:
    print("palindrom")