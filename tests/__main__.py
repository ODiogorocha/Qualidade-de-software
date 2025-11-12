"""
Main para rodar todos os testes do sistema Truco
Autor: Diogo Rocha Marques, Gabriel de Quadro
"""

import pytest

class TestRunner:
    """Executa toda a suíte de testes do sistema de Truco"""

    def run_all_tests(self):
        print("\n Iniciando suíte de testes completa do Sistema Truco...\n")

        arquivos_teste = [
            "tests/test_baralho.py",
            "tests/test_jogador.py",
            "tests/test_jogo.py",
            "tests/test_cbr.py",
            "tests/test_dados.py",
            "tests/test_bot.py",
            "tests/test_truco.py",
            "tests/test_pontos.py",
            "tests/test_envido.py",
            "tests/test_flor.py",
            "tests/test_interface.py",
            "tests/test_uc01_partida.py",
            "tests/test_uc02_truco.py",
            "tests/test_uc03_envido.py",
            "tests/test_uc04_flor.py",
        ]

        resultado = pytest.main(["-v"] + arquivos_teste)

        if resultado == 0:
            print("\n Todos os testes passaram com sucesso!\n")
        else:
            print("\n Alguns testes falharam!\n")

if __name__ == "__main__":
    runner = TestRunner()
    runner.run_all_tests()
