

from . import start_text, start_buttons
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, CallbackQuery
from . import functions

@Client.on_message(filters.command(["start"], ["!", "/"]))
async def start(_, ok: Message):
    user = ok.from_user.id
    chat = ok.chat.id
    if user == chat:
       msg = start_text.format(ok.from_user.mention)
       try:
         await ok.reply_photo(PIC, caption=msg, reply_markup=InlineKeyboardMarkup(start_buttons))
       except:
         await ok.reply_text(msg, reply_markup=InlineKeyboardMarkup(start_buttons))
    else:
        await ok.reply_text("Contact me in PM to start :) ")


@Client.on_callback_query()
async def _callbacks(red: Client, callback_query: CallbackQuery):
   query = callback_query.data.lower()
   chat_id = callback_query.from_user.id
   message_id = callback_query.message.id
   if query == 'start_':
       await functions.one_word_query(chat_id, message_id)
