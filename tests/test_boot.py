import pytest
from truco.baralho import Baralho
from truco.carta import Carta

class TestBaralho:
    def test_cria_baralho(self):
        baralho = Baralho()
        assert len(baralho.cartas) == 40

    def test_embaralha(self):
        baralho = Baralho()
        cartas_originais = baralho.cartas.copy()
        baralho.embaralhar()
        # O baralho deve estar embaralhado (ordem diferente)
        assert baralho.cartas != cartas_originais

    def test_retirar_carta(self):
        baralho = Baralho()
        carta = baralho.retirar_carta()
        assert isinstance(carta, Carta)
        assert len(baralho.cartas) == 39
