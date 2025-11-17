from src.truco.jogo import Jogo
from src.truco.jogador import Jogador
from src.truco.bot import Bot

class TestJogo:
    def test_iniciar_mao(self):
        jogador = Jogador("jogador1")
        assert jogador.criar_mao is not None

    def test_avaliar_rodada_empate(self):
        jogador = Jogador("jogador1")
        bot = Bot("bot1")
        assert jogador.pontos == bot.pontos 

    def test_encerrar_partida(self):
        jogo = Jogo()
        jogador = Jogador("jogador1")
        bot = Bot("bot1")


        if jogo.jogador_fugiu:
            assert True
        if jogador.pontos > bot.pontos:
            assert jogador.nome == "jogador1"
        if bot.pontos > jogador.pontos:
            assert bot.nome == "bot1"

