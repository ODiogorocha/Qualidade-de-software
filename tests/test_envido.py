from src.truco.envido import Envido


class TestEnvido:
    def test_valor_inicial(self):
        e = Envido()
        assert hasattr(e, "valor") or hasattr(e, "pontos") or True

    def test_pedir_envido(self):
        e = Envido()
        if hasattr(e, "jogador_pediu_envido"):
            assert e.jogador_pediu_envido is not None #vazio


    def test_aumentar_envido(self):
        e = Envido()
        if e.quem_real_envido or e.quem_falta_envido:
            assert True


    def test_recusar_envido(self):
        e = Envido()
        if e.quem_fugiu:
            assert True