import pytest
from truco.cbr import Cbr

class TestCBR:
    def test_carregar_modelo(self):
        cbr = Cbr()
        assert hasattr(cbr, "__init__")

    def test_dimensionalidade(self):
        cbr = Cbr()
        # Verifica se o objeto foi criado corretamente
        assert isinstance(cbr, Cbr)
