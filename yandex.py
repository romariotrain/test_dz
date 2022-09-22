import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type' : 'application/json',
            'Authorization' : 'OAuth {}'.format(self.token)
        }

    def create_file(self, file_name):
        URL = 'https://cloud-api.yandex.net:443/v1/disk/resources/files'
        headers = self.get_headers()
        params = {'path': file_name, 'overwrite': 'true'}
        response = requests.put(URL, headers=headers, params=params)
        pprint(response.status_code)
        return response.status_code


ya = YaUploader('Сюда вставить токен')


