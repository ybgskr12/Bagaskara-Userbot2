""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, cilik_cmd


@cilik_cmd(pattern="ihelp$")
async def usit(event):
    await edit_or_reply(
        event,
        f"**Hai {owner} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"★ **GroupSupport :** [Grup Support](t.me/allfucek )\n"
        f"★ **Channel :** [Channel](t.me/loveisfuckedup )\n"
        f"★ **OwnerRepo :** [ʙᴧɢᴧsҡᴧʀᴧ](t.me/ybgskr)\n"
        f"★ **Repo :** [Bagaskara-Userbot](https://github.com/ybgskr12/Bagaskara-Userbot2)\n",
    )


@cilik_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Bagaskara-Userbot:** [KLIK DISINI](https://telegra.ph/List-Variabel-Heroku-untuk-Man-Userbot-09-22)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk Cilik-Userbot.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository Bagaskara-Userbot.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String Bagaskara-Userbot.\
    "
    }
)
