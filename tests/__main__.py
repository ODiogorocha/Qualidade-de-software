"""
Main para rodar todos os testes do sistema Truco
Autor: Diogo Rocha Marques, Gabriel de Quadro
"""

import pytest

class TestRunner:
    """Executa toda a suíte de testes do sistema de Truco"""

    def rodar_testes(self):
        print("\n Iniciando suíte de testes completa do Sistema Truco...\n")

        arquivos_teste = [
            "tests/test_baralho.py",
            "tests/test_jogador.py",
            "tests/test_jogo.py",
            "tests/test_cbr.py",
            "tests/test_dados.py",
            "tests/test_truco.py",
            "tests/test_pontos.py",
            "tests/test_envido.py",
            "tests/test_flor.py",
            "tests/test_interface.py"
        ]

        resultado = pytest.main(["-v"] + arquivos_teste)

        if resultado == 0:
            print("\n Todos os testes passaram com sucesso!\n")
        else:
            print("\n Alguns testes falharam!\n")

if __name__ == "__main__":
    runner = TestRunner()
    runner.rodar_testes()
