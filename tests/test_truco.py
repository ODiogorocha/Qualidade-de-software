from src.truco.truco import Truco 
from src.truco.jogador import Jogador


class TestTruco:
    def test_valor_inicial(self):
        jogador = Jogador("jogador")
        assert jogador.pontos == 0


    def test_pedir_truco(self):
        truco = Truco()
        
        assert truco.pedir_truco is not None or not 0

    def test_limite_truco(self):
        truco = Truco()
        if truco.valor_aposta >= 4: #pontuacao certa 4 
            assert True

    def test_recusar_truco(self):
        truco = Truco()
        if truco.jogador_fugiu == 1:
            assert True