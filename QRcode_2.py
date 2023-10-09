import qrcode

links = ["https://www.linkedin.com/in/zahid-hasan60/",
         "https://www.facebook.com/zahidhasan.shanto.733/",
         "https://github.com/zahid60"]

for index, link in enumerate(links):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=5,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="maroon", back_color="cyan")

    files = f"QRcode{index + 1}.png"
    img.save(files)

# Program to customize Qrcode as you wish
