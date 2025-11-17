import pytest
from unittest.mock import patch
from src.truco.interface import Interface  

class CartaFalsa:
    def __init__(self, nome):
        self.nome = nome

    def retornar_carta(self):
        return self.nome


class JogadorFalso:
    def __init__(self, nome):
        self.nome = nome


@pytest.fixture
def interface():
    return Interface()



def test_borda_simples(interface, capsys):
    interface.border_msg("Olá Mundo")
    saida = capsys.readouterr().out
    assert "Olá Mundo" in saida
    assert "╔" in saida and "╚" in saida  

def test_borda_titulo(interface, capsys):
    interface.border_msg("Mensagem teste", title="Título")
    saida = capsys.readouterr().out
    assert "Título" in saida
    assert "Mensagem teste" in saida


def test_mostrar_carta_jogada(interface, capsys):
    carta = CartaFalsa("4 de Copas")
    interface.mostrar_carta_jogada("Jogador 1", carta)
    saida = capsys.readouterr().out
    assert "Jogador 1 jogou a carta: 4 de Copas" in saida


def test_mostrar_carta_ganhadora(interface, capsys):
    carta = CartaFalsa("7 de Espadas")
    interface.mostrar_carta_ganhadora(carta)
    saida = capsys.readouterr().out
    assert "Carta ganhadora: 7 de Espadas" in saida


def test_mostrar_ganhador_rodada(interface, capsys):
    interface.mostrar_ganhador_rodada("Jogador 2")
    saida = capsys.readouterr().out
    assert "Jogador 2 ganhou a rodada" in saida


def test_mostrar_placar_total(interface, capsys):
    interface.mostrar_placar_total("Ana", 5, "Beto", 3)
    saida = capsys.readouterr().out
    assert "Pontuação Total" in saida
    assert "Ana" in saida and "Beto" in saida


def test_mostrar_placar_rodadas(interface, capsys):
    interface.mostrar_placar_rodadas("Ana", 2, "Beto", 1)
    saida = capsys.readouterr().out
    assert "Rodadas da Partida Atual" in saida
    assert "Ana" in saida and "Beto" in saida


def test_mostrar_vencedor_flor(interface, capsys):
    interface.mostrar_vencedor_flor(1, "Ana", "Beto", 3)
    saida = capsys.readouterr().out
    assert "Vencedor Flor" in saida
    assert "Ana" in saida


def test_mostrar_vencedor_envido_jogador1(interface, capsys):
    interface.mostrar_vencedor_envido(1, "Ana", 31, "Beto", 28)
    saida = capsys.readouterr().out
    assert "Jogador 1 Vencedor Envido" in saida
    assert "Ana" in saida and "Beto" in saida


def test_mostrar_vencedor_envido_jogador2(interface, capsys):
    interface.mostrar_vencedor_envido(2, "Ana", 31, "Beto", 33)
    saida = capsys.readouterr().out
    assert "Jogador 2 Vencedor Envido" in saida
    assert "Beto" in saida


def test_mostrar_ganhador_jogo(interface, capsys):
    interface.mostrar_ganhador_jogo("Jogador 1")
    saida = capsys.readouterr().out
    assert "Jogador 1 ganhou o jogo" in saida


def test_mostrar_pediu_truco(interface, capsys):
    interface.mostrar_pediu_truco("Jogador 2")
    saida = capsys.readouterr().out
    assert "Jogador 2 pediu truco" in saida


def test_mostrar_jogador_opcoes(interface, capsys):
    interface.mostrar_jogador_opcoes("Jogador 1")
    saida = capsys.readouterr().out
    assert "Jogador 1 é mão" in saida


def test_mostrar_placar_total_jogador_fugiu(interface, capsys):
    jogador_fugiu = JogadorFalso("Carlos")
    interface.mostrar_placar_total_jogador_fugiu(jogador_fugiu, "Ana", 3, "Beto", 2)
    saida = capsys.readouterr().out
    assert "Carlos fugiu" in saida



def test_desenhar_cartas_ouros(interface):
    resultado = interface.desenhar_cartas("7 OUROS")
    assert any("♦" in linha for linha in resultado)


def test_desenhar_cartas_copas(interface):
    resultado = interface.desenhar_cartas("1 COPAS")
    assert any("♥" in linha for linha in resultado)


def test_desenhar_cartas_espadas(interface):
    resultado = interface.desenhar_cartas("1 ESPADAS")
    assert any("♠" in linha for linha in resultado)


def test_desenhar_cartas_bastos(interface):
    resultado = interface.desenhar_cartas("1 BASTOS")
    assert any("♣" in linha for linha in resultado)


def test_exibir_cartas(interface, capsys):
    interface.exibir_cartas(["1 COPAS", "7 OUROS"])
    saida = capsys.readouterr().out
    assert "┌─────────┐" in saida
    assert "♥" in saida or "♦" in saida


def test_exibir_unica_carta(interface, capsys):
    interface.exibir_unica_carta("7 OUROS")
    saida = capsys.readouterr().out
    assert "♦" in saida

@patch("os.system")
def test_limpar_tela(mock_system, interface):
    interface.limpar_tela()
    mock_system.assert_called_with("clear")
