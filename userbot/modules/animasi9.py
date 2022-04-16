# @greyyvbss 

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, cilik_cmd


@cilik_cmd(pattern="sponge(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏\n"
        "┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏ \n"
        "▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ \n"
        "▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ \n"
        "▕╭╮▏╮┈┈┈┈┏━━━╯▏\n"
        "▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ \n"
        "▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ \n"
        "▕┈╰▏╰╯╰━━━━╯┈┈▏ν2.ο\n"
        "           **BOBBB**      ")


@cilik_cmd(pattern="ngok(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┃┏┗┛┓┃╭┫NGOKKKK┃\n"
        "┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┗┻┛┗┻┛┈┈┈┈")


@cilik_cmd(pattern="musang(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        " ╱▏┈┈┈┈┈┈▕╲▕╲┈┈┈\n"
        "▏▏┈┈┈┈┈┈▕▏▔▔╲┈┈\n"
        "▏╲┈┈┈┈┈┈╱┈▔┈▔╲┈\n"
        "╲▏▔▔▔▔▔▔╯╯╰┳━━▀\n"
        "┈▏╯╯╯╯╯╯╯╯╱┃┈┈┈\n"
        "┈┃┏┳┳━━━┫┣┳┃┈┈┈\n"
        "┈┃┃┃┃┈┈┈┃┃┃┃┈┈┈\n"
        "┈┗┛┗┛┈┈┈┗┛┗┛┈┈┈")

    
@cilik_cmd(pattern="gajah(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
        "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
        "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
        "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
        "╭▏┈┈┈┈┈┈┈▏╲▂▂╱┈\n"
        "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
        "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
        "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈")

    
@cilik_cmd(pattern="liat(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,    
        "┈┈┈╭━━━━━╮┈┈┈┈┈\n"
        "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
        "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
        "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
        "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
        "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
        "┈┈┈┃┊┃╰━━┫┈Liatin Aja\n"
        "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")


CMD_HELP.update(
    {
    "animasi9": f"➢ **Plugin : **`animasi9`\
    \n\n ┌✪ **Syntax :** `{cmd}sponge`\
    \n └✪ **Function : **Mengirim Gambar SpongeBoob.\
    \n\n ┌✪ **Syntax :** `{cmd}ngok`\
    \n └✪ **Function : **Mengirim Gambar Babi.\
    \n\n ┌✪ **Syntax :** `{cmd}musang`\
    \n └✪ **Function : **Mengirim Gambar Musang.\
    \n\n ┌✪ **Syntax :** `{cmd}gajah`\
    \n └✪ **Function : **Mengirim Gambar Gajah.\
    \n\n ┌✪ **Syntax :** `{cmd}liat`\
    \n └✪ **Function : **Mengirim Gambar see."   
})
