from requests import get
from requests.exceptions import MissingSchema, InvalidURL
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError, YoutubeDLError
from fast_dash import FastDash
import os
import subprocess
from threading import Thread, Lock
from typing import Dict, Any

DOWNLOAD_LOCK = Lock()
SHUTDOWN_INITIATED = False


DOWNLOAD_FOLDER = os.path.expandvars("%userprofile%\\Music")
YDL_OPTIONS = {
    "outtmpl": f"{DOWNLOAD_FOLDER}\\%(title)s.%(ext)s",
}


class VideoNotFoundError(YoutubeDLError):
    pass


def download_video(name_or_url: str) -> Dict[Any, Any]:
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            get(name_or_url)
            video = ydl.extract_info(name_or_url, download=True)
        except (ConnectionError, MissingSchema, InvalidURL):
            search_results = ydl.extract_info(f"ytsearch:{name_or_url}", download=True)
            try:
                video = search_results["entries"][0]
            except IndexError:
                raise VideoNotFoundError(f'"{name_or_url}" not found!')
        return video


def handle_video_download_request(video_name: str) -> str:
    global SHUTDOWN_INITIATED, DOWNLOAD_LOCK

    with DOWNLOAD_LOCK:
        if SHUTDOWN_INITIATED:
            return
        try:
            video = download_video(video_name)
        except VideoNotFoundError:
            return "Video not found!"
        except DownloadError:
            return "Something went wrong while downloading video!"
        except Exception as e:
            error_msg = "ERROR: Unexpected error occurred while searching and downloading video!"
            error_msg += f"\r\n {repr(e)}"
            return error_msg
        output_file = video["requested_downloads"][0]["filepath"]
        subprocess.Popen(
            f'explorer.exe /select,"{output_file}"',
            shell=True,
        )
        delayed_shutdown()
        return f"{video['title']} downloaded successfully to \"{DOWNLOAD_FOLDER}\"!"


def delayed_shutdown(delay: float = 1) -> None:
    global SHUTDOWN_INITIATED
    SHUTDOWN_INITIATED = True

    def shutdown() -> None:
        import time

        time.sleep(delay)
        os._exit(0)

    t = Thread(target=shutdown)
    t.start()


app = FastDash(
    callback_fn=handle_video_download_request,
    title="Youtube Downloader",
)
subprocess.Popen("start http://127.0.0.1:8080", shell=True)
app.run()
