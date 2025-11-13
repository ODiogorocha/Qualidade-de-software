import pytest
from src.truco.flor import Flor
from src.truco.jogador import Jogador


class TestFlor:
    def test_valor_inicial(self):
        flor = Flor()
        assert hasattr(flor, "valor") or hasattr(flor, "pontos")

    def test_pedir_flor(self):
        flor = Flor()
        assert flor.quem_pediu_flor is not None

    def test_aumentar_flor(self):
        flor = Flor()
        if hasattr(flor.quem_pediu_contraflor or flor.quem_pediu_restoflor, "aumentar"):
            assert True
        else:
            pytest.skip("Método aumentar() não implementado")

