import json
from datetime import datetime
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


def definir_prioridade(descricao):
    # Converte o texto para letras minúsculas
    texto = descricao.lower()

    # Expressões que indicam problemas críticos
    palavras_criticas = [
        "fora do ar",
        "empresa parada",
        "todos sem acesso",
        "servidor caiu",
        "ninguém consegue trabalhar"
    ]

    # Verifica se existe uma situação crítica
    if any(palavra in texto for palavra in palavras_criticas):
        return "Alta"

    # Expressões que indicam problemas comuns
    palavras_medias = [
        "não funciona",
        "não consigo",
        "erro",
        "travando",
        "sem conexão"
    ]

    # Verifica se existe uma situação de prioridade média
    if any(palavra in texto for palavra in palavras_medias):
        return "Média"

    # Demais solicitações recebem prioridade baixa
    return "Baixa"


def salvar_chamado(descricao, categoria, prioridade):
    # Define o arquivo onde os chamados serão armazenados
    arquivo = Path(__file__).resolve().parent / "chamados.json"

    # Carrega os chamados existentes
    if arquivo.exists():
        with arquivo.open("r", encoding="utf-8") as f:
            chamados = json.load(f)
    else:
        chamados = []

    # Cria um novo registro
    novo_chamado = {
        "id": max((item["id"] for item in chamados), default=0) + 1,
        "descricao": descricao,
        "categoria": categoria,
        "prioridade": prioridade,
        "data": datetime.now().isoformat(timespec="seconds")
    }

    # Adiciona o chamado ao histórico
    chamados.append(novo_chamado)

    # Salva o histórico atualizado
    with arquivo.open("w", encoding="utf-8") as f:
        json.dump(chamados, f, ensure_ascii=False, indent=4)

    return novo_chamado


# Exemplos fictícios usados para treinar o classificador
descricoes = [
    "O computador não liga",
    "O teclado parou de funcionar",
    "O monitor está sem imagem",
    "O mouse apresenta defeito",
    "O sistema está travando",
    "O programa fecha sozinho",
    "O aplicativo apresenta erro",
    "Não consigo abrir o software",
    "A internet está lenta",
    "O Wi-Fi não conecta",
    "A rede está sem conexão",
    "Não consigo acessar a internet",
    "Esqueci minha senha",
    "Minha conta está bloqueada",
    "Não consigo fazer login",
    "Preciso recuperar meu acesso"
]

# Categoria correspondente a cada descrição
categorias = [
    "Hardware", "Hardware", "Hardware", "Hardware",
    "Software", "Software", "Software", "Software",
    "Rede", "Rede", "Rede", "Rede",
    "Acesso", "Acesso", "Acesso", "Acesso"
]

# Cria o modelo de classificação de textos
modelo = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

# Treina o modelo com os exemplos fictícios
modelo.fit(descricoes, categorias)


if __name__ == "__main__":
    # Recebe a descrição digitada pelo usuário
    chamado = input("Descreva o problema: ").strip()

    if not chamado:
        print("A descrição não pode estar vazia.")
    else:
        # Classifica o chamado utilizando IA
        categoria = modelo.predict([chamado])[0]

        # Sugere a prioridade utilizando regras
        prioridade = definir_prioridade(chamado)

        # Exibe o resultado da análise
        print(f"Categoria sugerida: {categoria}")
        print(f"Prioridade sugerida: {prioridade}")

        # Salva o chamado em JSON
        registro = salvar_chamado(chamado, categoria, prioridade)

        print(f"Chamado #{registro['id']} salvo com sucesso!")
