import pytest
from src.truco.pontos import Pontos


class TestPontos:
    def test_inicializacao(self):
        p = Pontos()
        assert hasattr(p, "pontos")

    def test_adicionar_pontos(self):
        p = Pontos()
        if hasattr(p, "adicionar"):
            p.adicionar(2)
            assert p.pontos >= 2
        else:
            pytest.skip("Método adicionar() não implementado")

    def test_resetar_pontos(self):
        p = Pontos()
        if hasattr(p, "resetar"):
            p.adicionar(3)
            p.resetar()
            assert p.pontos == 0
        else:
            pytest.skip("Método resetar() não implementado")
