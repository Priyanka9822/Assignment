#to replace all occurance of "a"with "$" in STRING

S="PRIYANKa a"
s=""
for i in S:
        if i=="a":
            s=s+"$"
        else:
            s=s+i
print(s)