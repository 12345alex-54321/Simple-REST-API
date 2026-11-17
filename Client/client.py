import requests

class Api_Client:

    def __init__(self, addr: str, p: int):

        self.server_address = "http://" + addr + ":" + str(p)
        self.port = p

    def print_get(self, endpoint: str):

        response = requests.get(self.server_address + endpoint)
        print("Код ответа сервера: ")
        print(response.status_code)
        print("Ответ сервера: ")
        print(response.text)

    def print_post(self, endpoint: str, post_data: dict):

        response = requests.post(self.server_address + endpoint, json=post_data)
        print("Код ответа сервера: ")
        print(response.status_code)
        print("Ответ сервера: ")
        print(response.text)


