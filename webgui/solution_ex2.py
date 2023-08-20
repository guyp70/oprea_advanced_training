from fast_dash import fastdash, Image
import os


@fastdash
def puppies(puppy_id: int) -> Image:
    print(os.listdir('./puppies'))
    if f'{puppy_id}.jpg' in os.listdir('./puppies'):
        return Image(src=f'./puppies/{puppy_id}.jpg').to_html()


# * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)