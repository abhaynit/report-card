f2 = open('aman.mp4','ab')
with open("ak.mp4", "rb") as f:
    while True:
        byte = f.read(1024)
        if not byte:
            break
        else:
            f2.write(byte)
f2.close()