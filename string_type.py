s = "You are awesome"
print(s)

s1 = """You are
the creator
of your destiny"""
print(s1)

print(s[2]) # 2 index of string s
print(s*2) # doubles the string
print(s*3) # triples the string

print(len(s1))

# Slicing a string
print(s[0:5])
print(s[0:])
print(s[:8])
print(s[-3:-1])   # -1 is always the last element

print(s[0:9:2])   # ([start,end,step increment]).
print(s[15::-1])  # step increment can be negative
print(s[::-1])    # this easily REVERSES a string!
