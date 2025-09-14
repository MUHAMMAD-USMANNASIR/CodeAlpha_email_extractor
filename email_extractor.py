import re
with open("data.txt", "r") as file:
    content = file.read()
print(" Raw content from data.txt:")
print(repr(content))
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", content)
if emails:
    with open("emails.txt", "w") as f:
        f.write("\n".join(emails))
    print(f" Extracted {len(emails)} emails and saved to emails.txt")
else:
    print(" No valid emails found in data.txt")
