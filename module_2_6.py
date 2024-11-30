def gen_password(n):
    password = ""
    for i in range(1,n):
        for j in range(i + 1, n + 1):
            summ = i + j
            if n % summ ==0:
                password += f"{i}{j}"
    return password
for n in range(3, 21):
    result = gen_password(n)
    print(f"{n}-{result}")
