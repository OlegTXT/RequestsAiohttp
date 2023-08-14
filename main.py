# import requests
#
#
# url = "https://jsonplaceholder.typicode.com/todos"
# a = requests.get(url)
#
# a.raise_for_status()
# print(a)
#
# with open('Task.txt', 'w') as file:
#     file.write(a.text)
#

import aiohttp
import asyncio


async def func():
    # открытие сесси в aiohttp
    async with aiohttp.ClientSession() as session:
        query = {
            "param" : "data",
            "param2" : "data",
        } # параметры
        # отправка запрос
        response = await session.get("http://google.com/")
        print(response.text) # текст данный
        print(response.status) # код статус
        print(response.url) # ссылка
        print(await response.json()) # json format


loop = asyncio.new_event_loop() # новый асинхронный цыкл
loop.create_task(func()) # добавляет в него новую функцию
loop.run_forever() # запускает цыкл




