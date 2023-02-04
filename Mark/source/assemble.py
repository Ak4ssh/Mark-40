from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.types import Update

from .. import (MARK, Session, Session2, Session3, Session4,
               Session5, Session6, Session7, Session8, Session9, Session10, Session11,
               Session12, Session13, Session14, Session15, Session16, Session17, Session18,
               Session19, Session20, ASSEM_HNDLR, BYE_HNDLR)

sessions = [Session, Session2, Session3, Session4, Session5, Session6, Session7, Session8, Session9, Session10,
           Session11, Session12, Session13, Session14, Session15, Session16, Session17, Session18, Session19, Session20]

@MARK.on_message(filters.command(["ssemble"], prefixes=ASSEM_HNDLR))
async def join_group(client, message, chat_id):
    # Iterate through each session in the list
   chat = await MARK.get_chat(chat_id)
   for i, session in enumerate(sessions):
        if session:
          if chat.username:
            # Join the session to the group
            session.join_chat(chat.username)   
        
@MARK.on_message(filters.command(["k"], prefixes=BYE_HNDLR))
async def join(_, chat_id: int, e: Message):
    chid = e.chat.id
    chat = await MARK.get_chat(chat_id)
    e.chat.id = await _.export_chat_invite_link(chid)
    count = 0
    try:
        if Session:
            await Session.leave_chat(e.chat.id)
            count += 1
        if Session2:
            await Session2.leave_chat(e.chat.id)
            count += 1
        if Session3:
            await Session3.leave_chat(e.chat.id)
            count += 1
        if Session4:
            await Session4.leave_chat(e.chat.id)
            count += 1
        if Session5:
            await Session5.leave_chat(e.chat.id)
            count += 1
        if Session6:
            await Session6.leave_chat(e.chat.id)
            count += 1
        if Session7:
            await Session7.leave_chat(e.chat.id)
            count += 1
        if Session8:
            await Session8.leave_chat(e.chat.id)
            count += 1
        if Session9:
            await Session9.leave_chat(e.chat.id)
            count += 1
        if Session10:
            await Session10.leave_chat(e.chat.id)
            count += 1
        if Session11:
            await Session11.leave_chat(e.chat.id)
            count += 1
        if Session12:
            await Session12.leave_chat(e.chat.id)
            count += 1
        if Session13:
            await Session13.leave_chat(e.chat.id)
            count += 1
        if Session14:
            await Session14.leave_chat(e.chat.id)
            count += 1
        if Session15:
            await Session15.leave_chat(e.chat.id)
            count += 1
        if Session16:
            await Session16.leave_chat(e.chat.id)
            count += 1
        if Session17:
            await Session17.leave_chat(e.chat.id)
            count += 1
        if Session18:
            await Session18.leave_chat(e.chat.id)
            count += 1
        if Session19:
            await Session19.leave_chat(e.chat.id)
            count += 1
        if Session20:
            await Session20.leave_chat(e.chat.id)
            count += 1
    except Exception as ex:
        await e.reply_text(f"ERROR")
