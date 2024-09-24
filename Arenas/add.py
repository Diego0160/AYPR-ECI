a = int(input())
b = int(input())

r = a + b

if a < 0:
    a_str = "(" + str(a) + ")"
else:
    a_str = str(a)

if b < 0:
    b_str = "(" + str(b) + ")"
else:
    b_str = str(b)

print(a_str + "+" + b_str + "=" + str(r))
