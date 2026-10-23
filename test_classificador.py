import unittest
from classificador import definir_prioridade


class TestPrioridade(unittest.TestCase):

    # Verifica a prioridade de um sistema indisponível
    def test_prioridade_alta(self):
        descricao = "O sistema está fora do ar"
        self.assertEqual(definir_prioridade(descricao), "Alta")

    # Verifica a prioridade de um erro comum
    def test_prioridade_media(self):
        descricao = "Não consigo abrir o programa"
        self.assertEqual(definir_prioridade(descricao), "Média")

    # Verifica uma solicitação sem urgência identificada
    def test_prioridade_baixa(self):
        descricao = "Solicito instalação de um aplicativo"
        self.assertEqual(definir_prioridade(descricao), "Baixa")

    # Verifica se letras maiúsculas alteram o resultado
    def test_maiusculas(self):
        descricao = "SISTEMA FORA DO AR"
        self.assertEqual(definir_prioridade(descricao), "Alta")


if __name__ == "__main__":
    unittest.main()
