from PIL import Image

image = Image.open('01.jpg')


image.show()

# The file format of the source file.
print(image.format) # Output: 

# The pixel format used by the image. Typical values are “1”, “L”, “RGB”, or “CMYK.”
print(image.mode) # Output:

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(image.size) # Output: 

# Colour palette table, if any.
print(image.palette) # Output: None

# Format
image = Image.open('01.jpg')
image.save('new_image.png')

# Resize
new_image = image.resize((400, 400))
new_image.save('image_400.jpg')
print(image.size) # Output
print(new_image.size) # Output

# Crop
box = (150, 200, 600, 600)
cropped_image = image.crop(box)
cropped_image.save('cropped_image.jpg')

# Paste
logo = Image.open('logo.png')
image_copy = image.copy()
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
image_copy.paste(logo, position)
image_copy.save('pasted_image.jpg')

# Paste (transparent)
logo = Image.open('logo.png')
image_copy = image.copy()
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
image_copy.paste(logo, position, logo)
image_copy.save('pasted_image1.jpg')


# Rotate
image_rot_90 = image.rotate(90)
image_rot_90.save('image_rot_90.jpg')

image_rot_180 = image.rotate(180)
image_rot_180.save('image_rot_180.jpg')

image.rotate(45).save('image_rot_45.jpg')

# Flip
image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
image_flip.save('image_flip.jpg')

# Color transform
greyscale_image = image.convert('L')
greyscale_image.save('greyscale_image.jpg')
