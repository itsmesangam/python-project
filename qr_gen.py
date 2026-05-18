import qrcode
img = qrcode.make('I Love U Smriti your heart sangam')
type(img)  # qrcode.image.pil.PilImage
img.save("loveU.png")