import pytest
from src.truco.bot import Bot
from src.truco.jogador import Jogador
from src.truco.baralho import Baralho


class TestBot:
    def test_decisao_truco(self):
        bot = Bot("Bot")
        jogador = Jogador("Jogador")
        baralho = Baralho()
        bot.criar_mao(baralho)
        decisao = bot.decidir_truco()
        assert decisao in [True, False]

    def test_jogar_carta(self):
        bot = Bot("Bot")
        baralho = Baralho()
        bot.criar_mao(baralho)
        carta_jogada = bot.jogar_carta(0)
        assert carta_jogada is not None
