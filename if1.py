char=0
dig=0
message='hello world! 123'
for a in message:
    if a.isalpha():
        char=char+1
    elif a.isdigit():
        dig=dig+1

print(char)
print(dig)


