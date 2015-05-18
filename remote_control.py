import lirc

sockid = lirc.init("myprog")

print("Ready")
while True:
    code = lirc.nextcode()
    if code:
        print(code[0])
