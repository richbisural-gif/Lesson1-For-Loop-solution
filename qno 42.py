text = "Hello World"
result = ""

for char in text:
    if char.lower() not in "aeiou":
        result += char

print(result)
