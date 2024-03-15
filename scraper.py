from telethon.sync import TelegramClient
import json
from telethon.tl.types import MessageMediaDocument, InputMessagesFilterDocument
from os import getenv

# Replace these with your own values
api_id = int(getenv('api_id'))
api_hash = getenv('api_hash')
channel_username = getenv('channel_username')


list_of_messages = []
client = TelegramClient('anon', api_id, api_hash)

mime_types = {'application/vnd.rar', 'application/x-fictionbook+xml', 'text/plain', 'application/zip',
              'application/x-7z-compressed', 'application/msword', 'application/rtf', 'image/vnd.djvu',
              'application/epub+zip', 'application/pdf', 'application/x-rar', 'image/vnd.djvu+multipage',
              'application/vnd.ms-htmlhelp', 'application/x-mobipocket-ebook',
              'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}


async def main():
    async for message in client.iter_messages(channel_username, filter=InputMessagesFilterDocument):

        if bool(message.media) and message.text != '':
            if isinstance(message.media, MessageMediaDocument):
                if message.media.document.mime_type not in mime_types:
                    continue
                try:
                    media_name = message.media.document.attributes[0].file_name
                except AttributeError:
                    media_name = None
                list_of_messages.append(
                    {"id": message.id, "text": message.text, "media_name": media_name}
                )
        elif bool(message.media):
            try:
                media_name = message.media.document.attributes[0].file_name
            except AttributeError:
                continue
            list_of_messages.append(
                {"id": message.id, "text": None, "media_name": media_name}
            )


with client:
    client.loop.run_until_complete(main())
    with open("messages.json", "w") as outfile:
        outfile.write(json.dumps(list_of_messages))
