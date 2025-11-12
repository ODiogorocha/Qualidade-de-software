import pytest
from src.truco.jogador import Jogador
from src.truco.baralho import Baralho


class TestJogador:
    def test_receber_cartas(self):
        jogador = Jogador("Teste")
        baralho = Baralho()
        jogador.criar_mao(baralho)
        assert len(jogador.mao) == 3

    def test_jogar_cartas_validas(self):
        jogador = Jogador("Teste")
        baralho = Baralho()
        jogador.criar_mao(baralho)
        carta = jogador.jogar_carta(0)
        assert carta is not None

    def test_exibir_mao(self, capsys):
        jogador = Jogador("Teste")
        baralho = Baralho()
        jogador.criar_mao(baralho)
        jogador.mostrar_mao(None)
        captured = capsys.readouterr()
        assert "de" in captured.out
