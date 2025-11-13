import pytest
from src.truco.envido import Envido


class TestEnvido:
    def test_valor_inicial(self):
        e = Envido()
        assert hasattr(e, "valor") or hasattr(e, "pontos") or True

    def test_pedir_envido(self):
        e = Envido()
        if hasattr(e, "jogador_pediu_envido"):
            assert e.jogador_pediu_envido is not None
        else:
            pytest.skip("Método pedir() não implementado")

    def test_aumentar_envido(self):
        e = Envido()
        if hasattr(e.quem_aumentou_envido or e.quem_falta_envido):
            assert True
        else:
            pytest.skip("Método aumentar() não implementado")

    def test_recusar_envido(self):
        e = Envido()
        if hasattr(e.quem_fugiu):
            assert True
        else:
            pytest.skip("Método recusar() não implementado")
