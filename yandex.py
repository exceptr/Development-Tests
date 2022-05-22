import requests


class YaUploader:
    token_ya = ''

    def __init__(self, token_ya=token_ya):
        super().__init__()
        self.token_ya = token_ya

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token_ya)
        }

    def get_folders_list(self):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        params = {"path": "disk:/"}
        response = requests.get(folder_url, headers=headers, params=params).json()['_embedded']
        items = response['items']
        names_folder = []
        for dict in items:
            names_folder.append(dict['name'])
        return names_folder

    def get_a_folder(self):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": f"/backup/"}
        response = requests.put(folder_url, headers=headers, params=params)
        return response.status_code


if __name__ == '__main__':
    yandex_user = YaUploader()
    # print(yandex_user.get_a_folder())