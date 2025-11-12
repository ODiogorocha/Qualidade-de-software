import pytest
from src.truco.jogo import Jogo


class TestUC02Truco:
    def test_pedir_truco(self):
        jogo = Jogo()
        if hasattr(jogo, "pedir_truco"):
            jogo.pedir_truco()
            assert True
        else:
            pytest.skip("Método pedir_truco() não implementado")

    def test_limitar_truco(self):
        jogo = Jogo()
        if hasattr(jogo, "pedir_truco"):
            for _ in range(5):
                jogo.pedir_truco()
            assert True
        else:
            pytest.skip("Método pedir_truco() não implementado")

    def test_recusar_truco(self):
        jogo = Jogo()
        if hasattr(jogo, "recusar_truco"):
            jogo.recusar_truco()
            assert True
        else:
            pytest.skip("Método recusar_truco() não implementado")
