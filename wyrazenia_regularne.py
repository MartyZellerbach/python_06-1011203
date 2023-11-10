import re

# re biblioteka do działań z wyrażeniami regularnymi

text = "Przykładowy tekst z adresam email: przykladowy@example.com"
text1 = "Twoj adres email to moj_email@example.com"

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
match = re.search(email_pattern, text1)
if match:
    print("Znaleziono email: ", match.group())  # Znaleziono email:  moj_email@example.com

numbers_pattern = r'\d+'
numbers = re.findall(numbers_pattern, "W tekscie sa liczby 123 i 888")
print(f"Numbers {numbers}")  # Numbers ['123', '888']
