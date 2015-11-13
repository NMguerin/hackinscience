import string
alpha = string.ascii_lowercase
for i in range(len(alpha)):
    for j in range(len(alpha)):
        if j > i:
            print("%s%s" % (alpha[i], alpha[j]))
