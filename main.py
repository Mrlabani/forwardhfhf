from flask import Flask
from threading import Thread
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

# Flask app for Koyeb port binding
app = Flask(__name__)

@app.route('/')
def home():
    return 'Telethon forwarder is running.'

# Telethon setup
API_ID = 29382018
API_HASH = '4734a726c04620c61ec0a28a1ae0d57f'
STRING_SESSION = '1BVtsOHQBu2uVQahuk4tSa9LYRikEOLIBH1NOC_3gCV2vkfpi59uIETVBYcdiC8h6lflt_Ac8RrtL_y5JXfij_lG6JyzNLelf4Ed9WPmLaiDd_rpO1L2NRcJJTrmcm2Yykj-2N87t1DHPE1NmTLgdSujBLQBeUONxbFdFqUXNa_ZllAgzNypeBZdVCHWwMILys5G_V_H1My2OA8lq3sXXRDxVcG9WBOrrI4ynF9KXhnhVn8oaluRBGJoZBCI_JZo_7RbKqAeFneFKmgBe0m7fopDtX5jWtXZhaRCL-nYPsHXiSMnYfAmuVnU0wTU62uT_kiFLsDKZLk-0GpWd56N3uRvNjQ4h0e8='

SOURCE_CHANNEL = -1002466188262
TARGET_CHANNEL = -1002458733993

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def forward_message(event):
    try:
        await client.forward_messages(TARGET_CHANNEL, event.message)
        print("Message forwarded.")
    except Exception as e:
        print(f"Error: {e}")

async def telethon_main():
    await client.start()
    print("Telethon is running...")
    await client.run_until_disconnected()

def run_telethon():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(telethon_main())

# Start both Flask and Telethon
if __name__ == "__main__":
    Thread(target=run_telethon).start()
    app.run(host="0.0.0.0", port=8080)
    
