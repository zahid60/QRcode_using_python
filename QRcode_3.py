import segno

qrcode = segno.make('https://www.linkedin.com/in/zahid-hasan60/')
qrcode.save('linkedin.png', dark="yellow", light="#323524", scale=10)

qrcode = segno.make_qr("https://github.com/zahid60")
qrcode.save(
    "GitHub.png",
    scale=10,
    light="lightblue",
    dark="darkblue",
    data_dark="green",
)

qrcode = segno.make_qr("https://www.facebook.com/zahidhasan.shanto.733/")
qrcode.save(
    "Facebook.png",
    scale=10,
    light="lightblue",
    dark="darkblue",
    data_dark="green",
    data_light="lightgreen",
)
