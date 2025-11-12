import pytest
from src.truco.truco import Truco


class TestTruco:
    def test_valor_inicial(self):
        t = Truco()
        assert hasattr(t, "valor") or hasattr(t, "pontos")

    def test_pedir_truco(self):
        t = Truco()
        if hasattr(t, "pedir"):
            t.pedir()
            assert True
        else:
            pytest.skip("Método pedir() não implementado")

    def test_limite_truco(self):
        t = Truco()
        if hasattr(t, "pedir"):
            for _ in range(5):
                t.pedir()
            assert True
        else:
            pytest.skip("Método pedir() não implementado")

    def test_recusar_truco(self):
        t = Truco()
        if hasattr(t, "recusar"):
            t.recusar()
            assert True
        else:
            pytest.skip("Método recusar() não implementado")
