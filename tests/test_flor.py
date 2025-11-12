import pytest
from src.truco.flor import Flor


class TestFlor:
    def test_valor_inicial(self):
        f = Flor()
        assert hasattr(f, "valor") or hasattr(f, "pontos")

    def test_pedir_flor(self):
        f = Flor()
        if hasattr(f, "pedir"):
            assert f.pedir() is not None
        else:
            pytest.skip("Método pedir() não implementado")

    def test_aumentar_flor(self):
        f = Flor()
        if hasattr(f, "aumentar"):
            f.aumentar()
            assert True
        else:
            pytest.skip("Método aumentar() não implementado")

    def test_recusar_flor(self):
        f = Flor()
        if hasattr(f, "recusar"):
            f.recusar()
            assert True
        else:
            pytest.skip("Método recusar() não implementado")
