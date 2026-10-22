# Refatoração de Código Python com Apoio de IA

Exercício de comparação entre uma versão inicial de um programa de notas e uma versão **refatorada**, com melhor organização e validação das entradas.

## Objetivo

Entender como melhorar a legibilidade, a manutenção e a robustez de um código sem alterar seu objetivo central: calcular a média das notas e informar se o aluno foi aprovado.

## Arquivos

| Arquivo | Descrição |
|---|---|
| `programa_notas.py` | Versão original, com lógica sequencial e sem validações de entrada. |
| `programa_notas.py_novo` | Versão refatorada, organizada em funções e com tratamento de entradas inválidas. |

## Melhorias na refatoração

- Funções separadas para leitura, cálculo da média e verificação da aprovação.
- Verificação de quantidade de notas maior que zero.
- Validação de notas entre 0 e 10.
- Tratamento de `ValueError` ao converter entradas.
- Ponto de entrada `if __name__ == "__main__":`.
- Exibição formatada da média.

**Regra usada nas duas versões:** média a partir de **6** significa aprovação.

## Como executar

Requisitos: Python 3. Nenhuma biblioteca externa é necessária.

```powershell
git clone https://github.com/Coutin061017/Refatorando-c-digo-com-apoio-de-IA.git
cd Refatorando-c-digo-com-apoio-de-IA
```

Versão original:

```powershell
python programa_notas.py
```

Versão refatorada:

```powershell
python programa_notas.py_novo
```

> Nota: o arquivo refatorado está salvo com o nome `.py_novo`, preservado aqui como no exercício original. Ele pode ser executado explicitamente pelo interpretador Python.

## Aprendizados

Comparação de versões, decomposição em funções, boas práticas de validação e uso crítico de ferramentas de IA para apoiar refatoração.

**Autor:** [André Coutinho](https://github.com/Coutin061017)
