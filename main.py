from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

# Replace with your credentials
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

async def main():
    await client.start()
    print("Bot is running and listening for new messages...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
