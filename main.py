from aiogram import executor
import logging
from config import dp
from handlers import commands, callback, extra, admin, fsm_anketa

commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_hanlers_fsm_anketa(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)