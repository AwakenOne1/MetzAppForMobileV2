import base64


with open('Pictures/cat.jpg', 'rb') as image_file:
    image_data = image_file.read()


image_64 = base64.b64encode(image_data).decode('utf-8')

print(image_64)

lis1 = list()

