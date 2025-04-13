import unittest
from unittest.mock import patch, MagicMock
from core.gerador_senha import GeradorSenha

class TestGeradorSenha(unittest.TestCase):
    def setUp(self):
        self.gerador = GeradorSenha()

    @patch('builtins.input', side_effect=["1"])
    @patch('core.gerador_senha.GeradorSenha.gerador_senha')
    def test_opcao_interface_nivel_1(self, mock_gerador_senha, mock_input):
        mock_gerador_senha.return_value = "12345678"
        self.gerador.inicio()
        mock_gerador_senha.assert_called_with(8, True, False, False, False)
        self.assertEqual(self.gerador.senha, "12345678")

    @patch('builtins.input', side_effect=["2"])
    @patch('core.gerador_senha.GeradorSenha.gerador_senha')
    def test_opcao_interface_nivel_2(self, mock_gerador_senha, mock_input):
        mock_gerador_senha.return_value = "abcdefghij"
        self.gerador.inicio()
        mock_gerador_senha.assert_called_with(10, False, False, True, False)
        self.assertEqual(self.gerador.senha, "abcdefghij")

    @patch('builtins.input', side_effect=["3"])
    @patch('core.gerador_senha.GeradorSenha.gerador_senha')
    def test_opcao_interface_nivel_3(self, mock_gerador_senha, mock_input):
        mock_gerador_senha.return_value = "AbcDefGhiJkl"
        self.gerador.inicio()
        mock_gerador_senha.assert_called_with(12, False, True, True, False)
        self.assertEqual(self.gerador.senha, "AbcDefGhiJkl")

    @patch('builtins.input', side_effect=["4"])
    @patch('core.gerador_senha.GeradorSenha.gerador_senha')
    def test_opcao_interface_nivel_4(self, mock_gerador_senha, mock_input):
        mock_gerador_senha.return_value = "Abc123Def456Ghi"
        self.gerador.inicio()
        mock_gerador_senha.assert_called_with(16, True, True, True, False)
        self.assertEqual(self.gerador.senha, "Abc123Def456Ghi")

    @patch('builtins.input', side_effect=["5"])
    @patch('core.gerador_senha.GeradorSenha.gerador_senha')
    def test_opcao_interface_nivel_5(self, mock_gerador_senha, mock_input):
        mock_gerador_senha.return_value = "Abc123!@#Def456"
        self.gerador.inicio()
        mock_gerador_senha.assert_called_with(18, True, True, True, True)
        self.assertEqual(self.gerador.senha, "Abc123!@#Def456")

    @patch('builtins.input', side_effect=["6", "1", "8", "2", "3", "4", "5", "6"])
    @patch('core.gerador_senha.GeradorSenha.gerador_senha')
    def test_senha_personalizada(self, mock_gerador_senha, mock_input):
        mock_gerador_senha.return_value = "Custom123!"
        self.gerador.inicio()
        mock_gerador_senha.assert_called_with(8, True, True, True, True)
        self.assertEqual(self.gerador.senha, "Custom123!")

    @patch('builtins.input', side_effect=["7"])
    @patch('core.gerador_senha.MenuPrincipal')
    def test_opcao_interface_sair(self, mock_menu_principal, mock_input):
        mock_menu_principal_instance = MagicMock()
        mock_menu_principal.return_value = mock_menu_principal_instance
        self.gerador.inicio()
        mock_menu_principal_instance.inicio.assert_called_once()

    @patch('builtins.input', side_effect=["1", "3"])
    @patch('core.gerador_senha.GeradorSenha.gerador_senha')
    @patch('core.gerador_senha.GeradorSenha.copiar_conteudo')
    def test_interface_mostrando_senha_copiar(self, mock_copiar_conteudo, mock_gerador_senha, mock_input):
        mock_gerador_senha.return_value = "12345678"
        self.gerador.inicio()
        mock_copiar_conteudo.assert_called_with("12345678")

if __name__ == "__main__":
    unittest.main()