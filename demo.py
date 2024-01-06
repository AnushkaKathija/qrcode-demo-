import qrcode

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=1)

qr.add_data("name=anushka/n usn: 1BI21IS014/n branch:ISE")  # Corrected line
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("advanced.png")
