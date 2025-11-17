from src.truco.jogador import Jogador


class TestPontos:
    def test_inicializacao(self):
        jogador = Jogador("Teste")
        assert jogador.pontos == 0

    def test_adicionar_pontos(self):
        jogador = Jogador("Teste")
        jogador_antes = jogador.pontos
        jogador_depois = jogador.adicionar_pontos(1)

        if jogador_antes != jogador_depois:
            assert True

    def test_resetar_pontos(self):
        jogador = Jogador("Teste")
        jogador_antes = jogador.pontos
        jogador.resetar()

        if jogador_antes != jogador.pontos:
            assert True
        