#!/usr/bin/python
# -*-coding:utf-8-*-
import requests


class DownloadValidateCode:

    def down_jyeoo_validate_code(self, url, path):

        response = requests.get(url, stream=True)
        with open(path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=2014):
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()


if __name__ == '__main__':
    obj = DownloadValidateCode()

    url = 'http://www.jyeoo.com/api/captcha/59a9122adc094b0fa5609aabc9b2dd3e?w=210&h=36&r=0.40980909410615807'
    for i in range(100):
        path = 'jyeoo/'+ str(i)+'.bmp'
        obj.down_jyeoo_validate_code(url, path)