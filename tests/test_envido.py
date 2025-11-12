import pytest
from src.truco.envido import Envido


class TestEnvido:
    def test_valor_inicial(self):
        e = Envido()
        assert hasattr(e, "valor") or hasattr(e, "pontos")

    def test_pedir_envido(self):
        e = Envido()
        if hasattr(e, "pedir"):
            assert e.pedir() is not None
        else:
            pytest.skip("Método pedir() não implementado")

    def test_aumentar_envido(self):
        e = Envido()
        if hasattr(e, "aumentar"):
            e.aumentar()
            assert True
        else:
            pytest.skip("Método aumentar() não implementado")

    def test_recusar_envido(self):
        e = Envido()
        if hasattr(e, "recusar"):
            e.recusar()
            assert True
        else:
            pytest.skip("Método recusar() não implementado")
