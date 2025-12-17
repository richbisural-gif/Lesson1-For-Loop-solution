bad_chars = [';', ':', '!', '*']
string = "py;th* o:n ! ;py * t*h:o !n"
result = ""

for char in string:
    if char not in bad_chars and char != " ":
        result += char

print(result)
