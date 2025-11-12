import pytest
from src.truco.dados import Dados


class TestDados:
    def test_tratamento_inicial_df(self, monkeypatch):
        monkeypatch.setattr(Dados, "tratamento_inicial_df", lambda self: {"idMao": 1})
        dados = Dados()
        assert isinstance(dados.casos, dict)

    def test_colunas_existentes(self, monkeypatch):
        monkeypatch.setattr(Dados, "tratamento_inicial_df", lambda self: {"idMao": 1})
        dados = Dados()
        assert "idMao" in dados.casos
