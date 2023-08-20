from fast_dash import fastdash, Upload
import base64


@fastdash
def puppies(file: Upload) -> str:
    open('a.txt', 'wb').write(base64.b64decode(file))
    return f"File size: {len(base64.b64decode(file))}"


# * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)