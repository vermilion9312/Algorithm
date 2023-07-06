import re
pattern = "a|e|i|o|u|A|E|I|O|U"
while True:
    str = input()
    if str == "#":
        break

    matches = re.findall(pattern, str)
    print(len(matches))
    