from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from datetime import datetime

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

welcome_image_url = "https://i.ibb.co/zVVZ845q/welcome-image.jpg"
channel_url = "https://t.me/gaurav_notes_pw"

@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def welcome_new_member(message: types.Message):
    group_name = message.chat.title

    for new_member in message.new_chat_members:
        user_name = f"@{new_member.username}" if new_member.username else "No username"
        user_id = new_member.id
        full_name = new_member.full_name

        # Get join date and time
        join_datetime = datetime.now()
        join_date = join_datetime.strftime("%d %B %Y")
        join_time = join_datetime.strftime("%I:%M %p")

        welcome_text = f"""🎉 New Member Joined! 🎉
Username: {user_name}
User ID: {user_id}
Full Name: {full_name}
Joined Group: {group_name} 📚
Join Date: {join_date} 🗓️
Join Time: {join_time} ⏰"""

        keyboard = InlineKeyboardMarkup()
        notes_button = InlineKeyboardButton(text="Notes Hub", url=channel_url)
        keyboard.add(notes_button)

        await bot.send_photo(chat_id=message.chat.id, photo=welcome_image_url, caption=welcome_text, reply_markup=keyboard)

async def is_admin(message: types.Message):
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    return member.is_chat_admin()

@dp.message_handler(commands=['ban'])
async def ban_user(message: types.Message):
    if not await is_admin(message):
        await message.reply("Aapke paas admin permissions nahi hain.")
        return
    if not message.reply_to_message:
        await message.reply("Ban karne ke liye kisi user ka reply karein.")
        return
    user_id = message.reply_to_message.from_user.id
    await bot.kick_chat_member(chat_id=message.chat.id, user_id=user_id)
    await message.reply(f"User {user_id} ko ban kar diya gaya hai.")

@dp.message_handler(commands=['unban'])
async def unban_user(message: types.Message):
    if not await is_admin(message):
        await message.reply("Aapke paas admin permissions nahi hain.")
        return
    if len(message.text.split()) < 2:
        await message.reply("Unban command ke sath user ID bhejein.")
        return
    user_id = int(message.text.split()[1])
    await bot.unban_chat_member(chat_id=message.chat.id, user_id=user_id)
    await message.reply(f"User {user_id} ka ban hata diya gaya hai.")

@dp.message_handler(commands=['mute'])
async def mute_user(message: types.Message):
    if not await is_admin(message):
        await message.reply("Aapke paas admin permissions nahi hain.")
        return
    if not message.reply_to_message:
        await message.reply("Mute karne ke liye kisi user ka reply karein.")
        return
    user_id = message.reply_to_message.from_user.id

    until_date = datetime.now().timestamp() + 3600
    permissions = ChatPermissions(can_send_messages=False)

    await bot.restrict_chat_member(chat_id=message.chat.id, user_id=user_id, permissions=permissions, until_date=until_date)
    await message.reply(f"User {user_id} ko 1 ghante ke liye mute kar diya gaya hai.")

@dp.message_handler(commands=['unmute'])
async def unmute_user(message: types.Message):
    if not await is_admin(message):
        await message.reply("Aapke paas admin permissions nahi hain.")
        return
    if not message.reply_to_message:
        await message.reply("Unmute karne ke liye kisi user ka reply karein.")
        return
    user_id = message.reply_to_message.from_user.id
    permissions = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True
    )
    await bot.restrict_chat_member(chat_id=message.chat.id, user_id=user_id, permissions=permissions)
    await message.reply(f"User {user_id} ka mute hata diya gaya hai.")

@dp.message_handler(commands=['kick'])
async def kick_user(message: types.Message):
    if not await is_admin(message):
        await message.reply("Aapke paas admin permissions nahi hain.")
        return
    if not message.reply_to_message:
        await message.reply("Kick karne ke liye kisi user ka reply karein.")
        return
    user_id = message.reply_to_message.from_user.id
    await bot.kick_chat_member(chat_id=message.chat.id, user_id=user_id)
    await bot.unban_chat_member(chat_id=message.chat.id, user_id=user_id)
    await message.reply(f"User {user_id} ko group se nikal diya gaya hai.")

if __name__ == '__main__':
    executor.start_polling(dp)
