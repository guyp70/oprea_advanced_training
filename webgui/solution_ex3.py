from fast_dash import fastdash, Upload
import hashlib
import base64


def decode_upload_data(upload_data: str) -> str:
    if upload_data.startswith("data:application/octet-stream;base64,"):
        b64_file_data = upload_data[len("data:application/octet-stream;base64,") :]
        return base64.b64decode(b64_file_data)
    raise ValueError(f"Unknown upload data format! (data: {upload_data[:50]} ...)")


@fastdash(update_live=True)
def md5sum_calc(upload_data: Upload) -> str:
    try:
        return f"md5: {hashlib.md5(decode_upload_data(upload_data)).hexdigest()}"
    except Exception as e:
        return f"An error occurred while uploading the file! (error: {e})"


# * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
