data = input("Enter the String : ")

seperate_string = {}

for char in data:
    print(char)
    if(char in seperate_string):
        seperate_string[char] += 1;
    else:
        seperate_string[char] = 1;

for key,value in seperate_string.items():
    print(f"character {key} is {value} present")