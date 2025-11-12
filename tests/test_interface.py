import pytest
from truco.interface import Interface

class TestInterface:
    """Classe de testes para o módulo Interface"""

    def setup_method(self):
        self.interface = Interface()

    def test_menu_principal(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "1")
        escolha = self.interface.menu_principal()
        assert escolha == "1"

    def test_exibir_mensagem(self, capsys):
        self.interface.exibir_mensagem("Olá, jogador!")
        captured = capsys.readouterr()
        assert "Olá, jogador!" in captured.out
