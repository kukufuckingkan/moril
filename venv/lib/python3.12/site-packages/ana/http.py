import urllib
import io

from urllib import request as req

def request (url: str) -> bytes:
    try:
        with req.urlopen(url) as response :
            # Read the response data
            data = response.read()
            binary = io.BytesIO(data)
            return binary

    except urllib.error.URLError as e:
        print(f"Failed to fetch data: {e.reason}")  