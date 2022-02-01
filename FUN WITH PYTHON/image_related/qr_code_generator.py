import qrcode

img = qrcode.make("https://www.youtube.com/")
img.save("abhay.jpg")