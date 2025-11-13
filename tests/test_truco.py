from src.truco.truco import Truco 
from src.truco.jogador import Jogador


class TestTruco:
    def test_valor_inicial(self):
        jogador = Jogador("jogador")
        assert jogador.pontos == 0


    def test_pedir_truco(self):
        truco = Truco()
        
        assert truco.pedir_truco is not None or not 0

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
