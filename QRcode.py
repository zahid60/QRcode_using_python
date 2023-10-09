import qrcode as qr

img1 = qr.make("https://www.linkedin.com/in/zahid-hasan60/")
img2 = qr.make("https://www.facebook.com/zahidhasan.shanto.733/")
img3 = qr.make("https://github.com/zahid60")

img1.save("Linkedin.com.png")
img2.save("Facebook.com.png")
img3.save("GitHub.com.png")

# Normal QRcode program
