from Server import server
from Client import client
import requests
import asyncio
import json

async def main():

    url = "127.0.0.1"
    port = 8000

    my_server = server.Api_Service(url, port)
    my_client = client.Api_Client(url, port)

    server_task = asyncio.create_task(my_server.StartServer())

    await asyncio.sleep(7)

    await asyncio.to_thread(my_client.print_get, "/questions/0")
    await asyncio.to_thread(my_client.print_get, "/questions/1")
    await asyncio.to_thread(my_client.print_get, "/questions/-1")

    test_data = {
        "Тип Отдыха": 5,
        "Климат": 1,
        "Бюджет": 3, 
        "Компания": 1,
        "Сезон": 3, 
        "Локация": 1
    }

    await asyncio.to_thread(my_client.print_post, "/answers/", test_data)

    my_server.StopServer()
    await server_task
    
if __name__ == "__main__":
    asyncio.run(main())