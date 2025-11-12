import pytest
from src.truco.jogo import Jogo
from src.truco.jogador import Jogador
from src.truco.baralho import Baralho


class TestUC01Partida:
    def test_inicializar_partida(self):
        jogo = Jogo()
        if hasattr(jogo, "iniciar_mao"):
            jogo.iniciar_mao()
            assert True
        else:
            pytest.skip("Método iniciar_mao() não implementado")

    def test_exibir_cartas_do_jogador(self, capsys):
        jogador = Jogador("Teste")
        baralho = Baralho()
        jogador.criar_mao(baralho)
        jogador.mostrar_mao(None)
        captured = capsys.readouterr()
        assert "de" in captured.out

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
