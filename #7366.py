f = open("input.txt", "r").read()
f = int(f)
w = open('output.txt', 'w')
w.write(str(f // 86400)+" "+str(f // 3600)+" "+str((f // 60)% 60)+" "+str(f % 60))
w.close()