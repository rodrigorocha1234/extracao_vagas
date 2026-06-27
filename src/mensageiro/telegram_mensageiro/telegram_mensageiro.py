from datetime import datetime

import telebot

from src.config.config import Config


class TelegramMensageiro:
    def __init__(self):
        self.__bot = telebot.TeleBot(Config.TOKEN_TELEGRAM)
        self.__chat_id = Config.CHAT_ID_TELEGRAM

    def formatar_texto(self, mensagem: tuple[str, str, str]) -> str:
        return f"""
        🚀 <b>Vaga encontrada</b>

        📅 <b>Data:</b> {datetime.now().strftime("%d/%m/%Y")}
        🏢 <b>Empresa:</b> {mensagem[2]}

        💼 <b>{mensagem[0]}</b>

        🔗 <b>{mensagem[1]}</b>
        """.strip()

    def enviar_mensagem(self, mensagem: str) -> None:
        self.__bot.send_message(chat_id=self.__chat_id, text=mensagem, parse_mode="HTML", )
