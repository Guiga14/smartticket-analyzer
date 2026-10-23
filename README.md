
# SmartTicket Analyzer

Classificador de chamados de suporte técnico desenvolvido em Python, utilizando Machine Learning para sugerir categorias e regras para determinar prioridades.

## Funcionalidades

- Classificação de chamados em Hardware, Software, Rede e Acesso.
- Sugestão de prioridade: Alta, Média ou Baixa.
- Armazenamento do histórico de chamados em JSON.
- Identificação sequencial e data de registro.
- Testes automatizados das regras de prioridade.

## Tecnologias

- Python 3.13
- scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- JSON
- unittest

## Como executar

1. Clone o repositório.
2. Crie e ative um ambiente virtual Python.
3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:

   ```bash
   python classificador.py
   ```

5. Digite a descrição de um chamado.

## Exemplo de utilização

Entrada:

    O servidor está fora do ar

Saída:

    Categoria sugerida: Rede
    Prioridade sugerida: Alta
    Chamado #1 salvo com sucesso!

## Testes

Execute:

```bash
python -m unittest -v
```

O projeto possui quatro testes automatizados das regras de prioridade.

## Como funciona

O modelo utiliza TF-IDF para transformar textos em características numéricas e Multinomial Naive Bayes para sugerir a categoria de cada chamado.

A prioridade é definida separadamente, por regras baseadas em expressões encontradas na descrição.

Os resultados são registrados localmente no arquivo `chamados.json`.

## Limitações

Este é um projeto demonstrativo, treinado com 16 descrições fictícias. As categorias sugeridas podem ser imprecisas e não substituem a análise humana.

As regras de prioridade também são simplificadas e não representam uma avaliação completa de impacto e urgência.