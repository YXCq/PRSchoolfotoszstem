import base64

with open("templates/img.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')


def photo_changes(user):
    user.photo1 = base64.b64encode(user.photo1).decode('utf-8') if user.photo1 else encoded_string
    user.photo2 = base64.b64encode(user.photo2).decode('utf-8') if user.photo2 else encoded_string
