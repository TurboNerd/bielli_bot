#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import (MessageHandler, Filters)

import config

# enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

#############################
#         functions         #
#############################
def get_full_name(update):
    return update.message.from_user.first_name + " " + update.message.from_user.last_name

#############################
#         commands          #
#############################
def start(bot, update):
    chat_id = update.message.chat_id
    logger.debug('start command received from chat "%s"' % (chat_id))
    bot.send_message(chat_id=chat_id, text="biellibot is under aggressive development")

def read(bot, update):
    chat_id = update.message.chat_id
    logger.debug('read a message from chat "%s"' % (chat_id))
    bot.send_message(chat_id=chat_id, text="maledetto bielli")

def error(bot, update, error):
    logger.error('Update "%s" caused error "%s"' % (update, error))

#############################
#           main            #
#############################
def main():
    config.read_config('settings.json')

    updater = Updater(token=config.get_telegram_key())

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands
    dispatcher.add_handler(CommandHandler('start', start))

    # on noncommand i.e message - do something
    dispatcher.add_handler(MessageHandler(Filters.text, read))

    # log all errors
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT.
    updater.idle()

if __name__ == '__main__':
    main()
