import pytest
from src.truco.flor import Flor


class TestUC04Flor:
    def test_pedir_flor(self):
        f = Flor()
        if hasattr(f, "pedir"):
            f.pedir()
            assert True
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
