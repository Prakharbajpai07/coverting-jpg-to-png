from PIL import Image, ImageFilter

img =Image.open('pokemon.jpg')
print(img)
print(img.format, img.size, img.mode)
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert("L")
filtered_img.save("blur.png",'png')
# filtered_img = filtered_img.rotate(90)
# filtered_img = filtered_img.resize((9000,9000))
box = (100, 100, 800, 400)
filtered_img = filtered_img.crop(box)
filtered_img.show()
Image._show(img)