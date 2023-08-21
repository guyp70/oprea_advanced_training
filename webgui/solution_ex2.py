from fast_dash import fastdash, Image
import os
import base64

PUPPIES_PHOTOS = os.listdir("./puppies")


def encode_image(image_path: str) -> str:
    encoded = base64.b64encode(open(image_path, "rb").read())
    image_extension = image_path.split(".")[-1]
    return f"data:image/{image_extension};base64,{encoded.decode()}"


@fastdash(update_live=True)
def puppies(puppy_photo: str = PUPPIES_PHOTOS) -> Image:
    return encode_image(f"./puppies/{puppy_photo}")


# * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
