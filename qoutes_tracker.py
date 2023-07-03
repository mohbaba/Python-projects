import requests
import telebot
from telebot import types

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}

headers = {
	"X-RapidAPI-Key": "4fc5c694d7msha02ff297e54b089p15b409jsnd00a548ee6fe",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

API_TOKEN = '5994318053:AAFBXZ-aWb99W6ILKzgXq-EmufCM0c2NF3I'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def welcome_message(message):
    
    markup = types.InlineKeyboardMarkup()
    trackcoin = types.InlineKeyboardButton('Track Coin', callback_data= 'trackcoin')
    portfolio = types.InlineKeyboardButton('Portfolio', callback_data= ' portfolio')
    markup.row(trackcoin, portfolio)
    bot.send_message(message.chat.id, 'Crypto tracker bot is online', reply_markup = markup)


@bot.callback_query_handler(func = lambda call: True)
def handle_callback_query(call):
    if call.data == 'trackcoin':
        bot.send_message(call.message.chat.id, 'Type coin Example: BTC')
        
    elif call.data == 'portfolio':
        bot.send_message(call.message.chat.id,'Portfolio functionality is not implemented yet.')

bot.polling() 