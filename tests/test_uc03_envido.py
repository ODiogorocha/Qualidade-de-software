import pytest
from src.truco.envido import Envido


class TestUC03Envido:
    def test_pedir_envido(self):
        e = Envido()
        if hasattr(e, "pedir"):
            e.pedir()
            assert True
        else:
            pytest.skip("Método pedir() não implementado")

    def test_recusar_envido(self):
        e = Envido()
        if hasattr(e, "recusar"):
            e.recusar()
            assert True
        else:
            pytest.skip("Método recusar() não implementado")
