from fast_dash import fastdash, Upload
import hashlib
import base64


@fastdash(update_live=True)
def md5sum_calc(upload_data: Upload) -> str:
    if upload_data.startswith("data:application/octet-stream;base64,"):
        file_data = upload_data[len("data:application/octet-stream;base64,") :]
        file_data = base64.b64decode(file_data)
        return f"md5: {hashlib.md5(file_data).hexdigest()}"
    return f"An error occurred while uploading the file! (upload_data[:100]= {upload_data[:100]})"


# * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
