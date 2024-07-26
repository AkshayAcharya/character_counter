def f(s):
    r = {}

    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1  # Correctly initialize to 1 instead of 0
    return r

s="Akshay Acharya"
print(f(s))