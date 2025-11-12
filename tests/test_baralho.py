import pytest
from truco.baralho import Baralho
from truco.carta import Carta

class TestBaralho:
    def test_cria_baralho(self):
        baralho = Baralho()
        # Deve ter 40 cartas (sem 8, 9 e 10)
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
        # Verifica se uma carta válida foi retirada
        assert isinstance(carta, Carta)
        # E o baralho tem uma carta a menos
        assert len(baralho.cartas) == 39
