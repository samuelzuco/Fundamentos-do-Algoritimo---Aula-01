votos = [0 for i in range(7)]
SO = ["", "Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outros"]
while True:
    v = int(input())
    if v == 0:
        break
else:
    if 0 < v <= 6:
        votos[v] += 1

print("")
