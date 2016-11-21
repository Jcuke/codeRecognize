import os

import requests


def downloads_pic():
    for i in range(0, 100):
        url1 = 'http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS'
        res = requests.get(url1, stream=True)
        with open(os.path.abspath('.') + "/res3/" + str(i) +'.bmp', 'wb') as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
            f.close()

if __name__ == "__main__":
    downloads_pic()