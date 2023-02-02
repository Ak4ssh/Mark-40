from pyrogram import filters
from pyrogram.types import Message

from .. import (Mark, Session, Session2, Session3, Session4,
               Session5, Session6, Session7, Session8, Session9, Session10, Session11,
               Session12, Session13, Session14, Session15, Session16, Session17, Session18,
               Session19, Session20, ASSEM_HNDLR)


@Mark.on_message(filters.command(["ssemble"], prefixes=ASSEM_HNDLR))
async def join(_, e: Message):
    chid = e.chat.id
    inp = await _.export_chat_invite_link(chid)
    count = 0
    try:
        if Session:
            await Session.join_chat(inp)
            await Session.send_message(e.chat.id,"Mark-1 Arrived in the chat.")
            count += 1
        if Session2:
            await Session2.join_chat(inp)
            await Session2.send_message(e.chat.id,"Mark-2 Arrived in the chat.")
            count += 1
        if Session3:
            await Session3.join_chat(inp)
            await Session3.send_message(e.chat.id,"Mark-3 Arrived in the chat.")
            count += 1
        if Session4:
            await Session4.join_chat(inp)
            await Session4.send_message(e.chat.id,"Mark-4 Arrived in the chat.")
            count += 1
        if Session5:
            await Session5.join_chat(inp)
            await Session5.send_message(e.chat.id,"Mark-5 Arrived in the chat.")
            count += 1
        if Session6:
            await Session6.join_chat(inp)
            await Session6.send_message(e.chat.id,"Mark-6 Arrived in the chat.")
            count += 1
        if Session7:
            await Session7.join_chat(inp)
            await Session7.send_message(e.chat.id,"Mark-7 Arrived in the chat.")
            count += 1
        if Session8:
            await Session8.join_chat(inp)
            await Session8.send_message(e.chat.id,"Mark-8 Arrived in the chat.")
            count += 1
        if Session9:
            await Session9.join_chat(inp)
            await Session9.send_message(e.chat.id,"Mark-9 Arrived in the chat.")
            count += 1
        if Session10:
            await Session10.join_chat(inp)
            await Session10.send_message(e.chat.id,"Mark-10 Arrived in the chat.")
            count += 1
        if Session11:
            await Session11.join_chat(inp)
            await Session11.send_message(e.chat.id,"Mark-11 Arrived in the chat.")
            count += 1
        if Session12:
            await Session12.join_chat(inp)
            await Session12.send_message(e.chat.id,"Mark-12 Arrived in the chat.")
            count += 1
        if Session13:
            await Session13.join_chat(inp)
            await Session13.send_message(e.chat.id,"Mark-13 Arrived in the chat.")
            count += 1
        if Session14:
            await Session14.join_chat(inp)
            await Session14.send_message(e.chat.id,"Mark-14 Arrived in the chat.")
            count += 1
        if Session15:
            await Session15.join_chat(inp)
            await Session15.send_message(e.chat.id,"Mark-15 Arrived in the chat.")
            count += 1
        if Session16:
            await Session16.join_chat(inp)
            await Session16.send_message(e.chat.id,"Mark-16 Arrived in the chat.")
            count += 1
        if Session17:
            await Session17.join_chat(inp)
            await Session17.send_message(e.chat.id,"Mark-17 Arrived in the chat.")
            count += 1
        if Session18:
            await Session18.join_chat(inp)
            await Session18.send_message(e.chat.id,"Mark-18 Arrived in the chat.")
            count += 1
        if Session19:
            await Session19.join_chat(inp)
            await Session19.send_message(e.chat.id,"Mark-19 Arrived in the chat.")
            count += 1
        if Session20:
            await Session20.join_chat(inp)
            await Session20.send_message(e.chat.id,"Mark-20 Arrived in the chat.")
            count += 1
    except Exception as ex:
        await e.reply_text(f"ERROR")
