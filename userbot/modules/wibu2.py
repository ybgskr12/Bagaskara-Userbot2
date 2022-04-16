# Copyright © Xa - Userbot
# Created by Rexa
# Masa iya lu tega mau hapus credit?!


from time import sleep
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import cilik_cmd


@cilik_cmd(pattern="awibu(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`W : Warga`")
    sleep(3)
    await typew.edit("`I : Indonesia`")
    sleep(3)
    await typew.edit("`B : Berpendidikan`")
    sleep(3)
    await typew.edit("`U : Unggul`")
    sleep(3)
    await typew.wdit("`(•‿•)`")


@cilik_cmd(pattern="wisad(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Menunggumu Menyukaimu..`")
    sleep(2)
    await typew.edit("`Bagaikan Menunggu...`")
    sleep(3)
    await typew.edit("`Anime No Game No Life Session 2...`")
    sleep(3)
    await typew.edit("`Karena itu Sangat Tidak Mungkin Terjadi...`")


@cilik_cmd(pattern="jalnin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Aku..`")
    sleep(2)
    await typew.edit("`Tidak akan`")
    sleep(2)
    await typew.edit("`Menarik`")
    sleep(2)
    await typew.edit("`Kembali`")
    sleep(2)
    await typew.edit("`Kata-Kata ku`")
    sleep(3)
    await typew.edit("`Karena itulah`")
    sleep(3)
    await typew.edit("`Jalan Ninjaku!`")


@cilik_cmd(pattern="kaku(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Ehhhhh`")
    sleep(2)
    await typew.edit("`Cuma mau nanya`")
    sleep(3)
    await typew.edit("`Anime Kok Kaku?`")
    sleep(3)
    await typew.edit("`AWOKAWOAKWOAK`")
    sleep(2)
    await typew.edit("`Padahal Genrenya Action`")
    sleep(3)
    await typew.edit("`Kalah sama Anime Dragon maid`")
    sleep(3)
    await typew.edit("`AWOKAWOAKWOAKWOAK`")
    sleep(3)


@cilik_cmd(pattern="kiyomasa(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**OIIIII**")
    sleep(2)
    await typew.edit("**Kiyomasa!!**")
    sleep(3)
    await typew.edit("**Nande-Nande**")
    sleep(3)
    await typew.edit("**Gambare-Gambare**")
    sleep(3)
    await typew.edit("**BAKAAAAA!!**")


@cilik_cmd(pattern="baka1(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`BAKAAAA!!`")
    sleep(2)
    await typew.edit("`BAKAA YAROU!!`")
    sleep(3)
    await typew.edit("`KUSSO!!`")
    sleep(2)
    await typew.edit("`BUKKOROSHITE YARUUU!!`")


@cilik_cmd(pattern="wgbt(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Konnichiwa!!`")
    sleep(2)
    await typew.edit("`Jadi gini`")
    sleep(2)
    await typew.edit("`Watashi Wa lagi gabut`")
    sleep(3)
    await typew.edit("`chotto matte!`")
    sleep(3)
    await typew.edit("`Watashi Bingung`")
    sleep(3)
    await typew.edit("`Dou sureba ii?`")
    sleep(2)
    await typew.edit("`mau nonton anime`")
    sleep(3)
    await typew.edit("`Tapi Watashi lagi ga mood`")
    sleep(3)
    await typew.edit("`Kocchi Kocchi`")
    sleep(2)
    await typew.edit("`temenin kegabutan watashi`")
    sleep(3)
    await typew.edit("`kalau ga mau watashi ga maksa`")
    sleep(3)
    await typew.edit("`Sou Ne :) Watashi pergi dulu`")
    sleep(3)
    await typew.edit("`Mata yooo!!!⊂(◉‿◉)つ`")
    sleep(3)


CMD_HELP.update(
    {
    "wibu2": f"➢ **Plugin : **`wibu2`\
    \n\n ┌✪ **Command :** `{cmd}awibu`\
    \n └✪ **Function : **Singkatan wibu.\
    \n\n ┌✪ **Command :** `{cmd}wisad`\
    \n └✪ **Function : **Wibu Sad.\
    \n\n ┌✪ **Command :** `{cmd}Jalnin`\
    \n └✪ **Function : **Kata Kata Naruto uzumaki.\
    \n\n ┌✪ **Command :** `{cmd}kaku`\
    \n └✪ **Function : **Cek sendiri aja.\
    \n\n ┌✪ **Command :** `{cmd}wgbt`\
    \n └✪ **Function : **Cek Sendiri aja.\
    \n\n ┌✪ **Command :** `{cmd}baka1`\
    \n └✪ **Function : **Cek Sendiri aja.\
    \n\n ┌✪ **Command :** `{cmd}kiyomasa`\
    \n └✪ **Function : **Nande nande."   
})

