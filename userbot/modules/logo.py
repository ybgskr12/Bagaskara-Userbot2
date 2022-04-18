#@greyyvbss
#@tofik_dn

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_delete, edit_or_reply, cilik_cmd


@cilik_cmd(pattern=r"logo(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await edit_delete(event, "**Silahkan Masukan Text Untuk Logo**")
    else:
        await edit_or_reply(event, "`Processing...`")
    chat = "@oneupdirty_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"/logo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            msg = await conv.send_message(f"/logo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            logo,
            caption=f"Logo by [{owner}](tg://user?id={aing.id})",
        )
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id, logo.id])
        await event.delete()


@cilik_cmd(pattern=r"wlogo(?: |$)(.*)")   
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await edit_delete(event, "**Silahkan Masukan Text Untuk Logo**")
    else:
        await edit_or_reply(event, "`Processing...`")
    chat = "@oneupdirty_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"/wlogo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            msg = await conv.send_message(f"/wlogo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            logo,
            caption=f"Logo by [{owner}](tg://user?id={aing.id})",
        )
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id, logo.id])
        await event.delete()        
      
   
CMD_HELP.update(
    {
        "logo": f"**Plugin : **`logo`\
        \n\n  •  **Syntax :** `{cmd}logo` <text>\
        \n  •  **Function : **Membuat logo dari text yang anda berikan\
        \n\n  •  **Syntax :** `{cmd}wlogo` <text>\
        \n  •  **Function : **Membuat logo dari text yang anda berikan\
    "
    }
)
