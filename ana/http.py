import urllib
import io

from urllib import request

def request (url: str) -> bytes:
    try:
        with request.urlopen(url) as response :
            # Read the response data
            data = response.read()
            return io.BytesIO(data)

    except urllib.error.URLError as e:
        print(f"Failed to fetch data: {e.reason}")  