from telethon import TelegramClient

api_id = 35177324   # tu api_id
api_hash = "7975692bd48734fc89c8905a1addb23a"

client = TelegramClient("session_name", api_id, api_hash)

async def main():
    await client.start()
    async for dialog in client.iter_dialogs():
        print(dialog.name, dialog.id)

with client:
    client.loop.run_until_complete(main())