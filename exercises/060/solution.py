import string
alpha = string.ascii_lowercase
for i in range(0, len(alpha)):
    for j in range(0, len(alpha)):
        print("%s%s" % (alpha[i], alpha[j]))
