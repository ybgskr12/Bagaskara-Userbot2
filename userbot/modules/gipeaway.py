# @greyyvbss
#cilik-userbot

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, cilik_cmd


@cilik_cmd(pattern="a(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Assalamualaikum kak ,apakah ada Giveaway???**")


@cilik_cmd(pattern="b(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BABI SOALNYA GA DANTA BET**")


@cilik_cmd(pattern="c(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**ANJING LAMA BET, TURUNIN SOALNYA**")


@cilik_cmd(pattern="d(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**MANA SOALNYA BUJED, GUA NUNGGUIN DARI TADI**")


@cilik_cmd(pattern="e(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**MINIMAL KALO HADIAHNYA DIKIT, SOALNYA DANTA DIKIT YA ANJENG 😁!!**")


@cilik_cmd(pattern="f(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**HETT GIPEAWAY NYA DIKIT BET, DASAR GC MISKIN CUIHHH!!**")


@cilik_cmd(pattern="g(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**KALO GIPEAWAY SOALNYA YANG BENER YA NGENTOTTT**")


@cilik_cmd(pattern="h(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**MINGGIR-MINGGIR DONATUR MAU LEWAT**")


@cilik_cmd(pattern="i(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**MISKIN MISKIN AJA TOD, GAUSAH SOK SOK AN JADI DONATUR!!**")


@cilik_cmd(pattern="j(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**GCAST DULU AHHHHH, KALI AJA MENANG GIPEAWAY!!**")


@cilik_cmd(pattern="k(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**JAWABAN YANG BENER YANG MANA ANJENG**")


@cilik_cmd(pattern="m(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**PAANSI SOALNYA PRIK BANGET!!**")


@cilik_cmd(pattern="n(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**NAJISSS GIPEAWAY NYA CUMAN CEBAN YANG BANYAKAN NAPAH!!**")


@cilik_cmd(pattern="o(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**OMEGAT GUA MENANG GIPEAWAY, MAYAN BUAT PICIES!!** 🥵🥵")


@cilik_cmd(pattern="r(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**RAME JUGA DISINI, IKUTAN AHHH!!**")


@cilik_cmd(pattern="s(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**GC ANJING SOALNYA GA DANTA SEMUA DAHLAH!!**")


@cilik_cmd(pattern="t(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**HETTT SOALNYA GAMPANG BET, BARI MEREM GE BISA INI MAH** 🥱")


@cilik_cmd(pattern="u(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**UDAH UDAH GIPEAWAY NYA UDAHAN, YAH KASIAN BET KETINGGALAN**")


@cilik_cmd(pattern="v(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**CAPE CAPE GIKES SOALNYA GA DANTA KONTOLL**")


@cilik_cmd(pattern="w(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**CLUE NYA APA ANJENG, SOALNYA GAJELAS**")

    
@cilik_cmd(pattern="x(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**DIMANA ADA GIPEAWAY DISITU ADA GUA WHAHAHAHAHA**")
    
   
@cilik_cmd(pattern="z(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**GUA MAU NURUNIN SOAL NIH , BENTAR MIKIR DULU**")  
    

CMD_HELP.update(
    {
        "gipeaway": f"**➢ Plugin : **`gipeaway`\
        \n\n ┌✪ **Syntax :** {cmd}a-z\
        \n └✪ **Function :** Kata-Kata buat giveaway\
    "
    })

