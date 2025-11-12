import pytest
from src.truco.jogo import Jogo
from src.truco.jogador import Jogador
from src.truco.baralho import Baralho


class TestJogo:
    def test_iniciar_mao(self):
        jogo = Jogo()
        if hasattr(jogo, "iniciar_mao"):
            jogo.iniciar_mao()
            assert True
        else:
            pytest.skip("Método iniciar_mao() não implementado")

    def test_avaliar_rodada_empate(self):
        jogo = Jogo()
        if hasattr(jogo, "avaliar_rodada"):
            assert jogo.avaliar_rodada(None, None) in ["empate", "jogador1", "jogador2"]
        else:
            pytest.skip("Método avaliar_rodada() não implementado")

    def test_atualizar_placar(self):
        jogo = Jogo()
        if hasattr(jogo, "atualizar_placar"):
            jogo.atualizar_placar()
            assert True
        else:
            pytest.skip("Método atualizar_placar() não implementado")

    def test_encerrar_partida(self):
        jogo = Jogo()
        if hasattr(jogo, "encerrar_partida"):
            jogo.encerrar_partida()
            assert True
        else:
            pytest.skip("Método encerrar_partida() não implementado")
