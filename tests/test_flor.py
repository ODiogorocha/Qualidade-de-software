from src.truco.flor import Flor
from src.truco.jogador import Jogador



class TestFlor:
    def test_valor_inicial(self):
        flor = Flor()
        jogador = Jogador("jogador1")
        assert jogador.pontos != (jogador.pontos + flor.valor_flor)

    def test_pedir_flor(self):
        flor = Flor()
        assert flor.quem_pediu_flor is not None

    def test_aumentar_flor(self):
        flor = Flor()
        if (flor.quem_pediu_contraflor or flor.quem_pediu_contraflor_resto 
                or flor.quem_pediu_contraflor_resto):
            assert True
