import traceback
from datetime import datetime

import requests
from common_utils.logger import logger
from config.config import Config


class MonitorBot:
    BOT_ID = Config.MONITOR_BOT_ID
    CHAT_ID = Config.MONITOR_CHAT_ID
    MODULE_NAME = Config.APP_NAME

    @classmethod
    def send_message(cls, message: str):
        """Send messages to Telegram bot"""

        if Config.IS_MONITOR_BY_TELEGRAM:
            time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            msg = rf"\[{Config.APP_NAME}]\[{time}] {message}"

            try:
                requests.get(
                    f"https://api.telegram.org/bot{cls.BOT_ID}/sendMessage?"
                    f"chat_id={cls.CHAT_ID}&parse_mode=Markdown&text={msg}",
                    timeout=5,
                )
            except Exception as e:
                logger.error(e)
                traceback.print_exc()


if __name__ == "__main__":
    MonitorBot.send_message("test")
