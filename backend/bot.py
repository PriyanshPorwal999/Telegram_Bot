# Final Telegram ChatBot Code 

import os

from boltiotai import openai

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import load_dotenv

from example import example

# Load .env file
load_dotenv()

bot = Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])

dp = Dispatcher()

openai.api_key = os.environ['OPENAI_API_KEY']

example()


@dp.message(CommandStart(['start', 'help']))
async def welcome(message: types.Message):
  await message.reply('Hello! I am GPT Chat BOT. You can ask me anything :)')


@dp.message()
async def gpt(message: types.Message):
  messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role":"user", "content":message.text}]

  response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

  await message.reply(response['choices'][0]['message']['content'])

async def main():
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())