import aioredis
import json
import asyncio

class Chat:
    def __init__(self, room_name):
        self.room_name = room_name


    async def start_db(self):
        self.redis = await aioredis.create_redis_pool("redis://localhost:7379")
        await self.redis.set("room_name", self.room_name)

    async def save_message(self, message_dict):
        room_name = await self.get("room_name")
        message_json = json.dumps(message_dict)
        await self.redis.rpush(room_name, message_json)

    async def clear_db(self):
        await self.redis.flushall()

    async def get_all_messages(self):
        room_name = await self.redis.get("room_name")
        messages_list = await self.redis.lrange(room_name, 0 , -1, encoding="utf-8")
        messages = []
        for  message in messages_list:
            message_dict = json.load(message)
            message.append(message_dict)

    async def get_name(self):
        room_name = await self.get("room_name", encoding="utf-8")
        return room_name


async def main():
    chat_db  = Chat("messages")
    await chat_db.start_db()  
    await chat_db.save_message({"handle": "first_user", "message": "hey"})
    await chat_db.save_message({"handle": "first_user", "message": "hey"})
    await chat_db.save_message({"handle": "second_user", "message": "What's up?"})
    await chat_db.save_message({"handle": "first_user", "message": "all good!"})

    chat_messages = await chat_db.get_all_messages()
    chat_db_name = await chat_db.get_name()

    print("db name {}".format(chat_db_name))

    for message in chat_messages:
        print("message by {} with message {}".format(message["handle"], message["message"]))
    
    await chat_db.clear_db()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
