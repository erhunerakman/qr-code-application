import qrcode

# QR kodunda yer alacak veri (isim veya bağlantı gibi)
data = "name or link"

# QR kodunu oluştur
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# QR kodunu resim olarak oluştur
img = qr.make_image(fill_color="black", back_color="white")

# Oluşturulan QR kodunu kaydet
img.save("new.png")