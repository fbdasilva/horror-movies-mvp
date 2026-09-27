# Pipeline de Dados — Filmes de Terror

## 📌 Descrição

Este repositório apresenta a entrega de um **MVP (Minimum Viable Product ou Produto Mínimo Viável)** para a construção de um **pipeline de dados** utilizando uma base de dados de filmes de terror.

O projeto foi desenvolvido para a disciplina de **Engenharia de Dados da PUC-Rio**, com o objetivo de aplicar conceitos relacionados à ingestão, tratamento, transformação e análise de dados utilizando uma arquitetura estruturada em camadas.

## 🎯 Objetivo

O projeto tem como objetivo construir um pipeline capaz de processar dados de filmes de terror, passando pelas etapas de:

- ingestão dos dados;
- tratamento e limpeza;
- transformação dos dados;
- organização em diferentes camadas;
- geração de dados para análise;
- realização de análises sobre os filmes.

## 📂 Fonte dos dados

Os dados utilizados no projeto foram obtidos a partir do dataset **Horror Movies**, disponibilizado no Kaggle:

[Kaggle — Horror Movies](https://www.kaggle.com/datasets/evangower/horror-movies)

O arquivo utilizado no projeto é:

```text
horror_movies.csv
```

## 🏗️ Estrutura do Pipeline

O pipeline foi organizado utilizando uma arquitetura em camadas:

```text
Fonte de dados
     │
     ▼
┌─────────────┐
│   Bronze    │
│  Ingestão   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Silver    │
│ Tratamento  │
│ e limpeza   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Gold     │
│Transformação│
│ e agregações│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Análise   │
│ Resultados  │
└─────────────┘
```

## 📓 Notebooks

O repositório contém os notebooks utilizados durante o desenvolvimento do pipeline nos formatos:

- `.py` — arquivos Python;
- `.ipynb` — notebooks Jupyter.

## ▶️ Ordem de Execução

Para executar o pipeline corretamente, os notebooks devem ser executados na seguinte ordem:

```text
1. Bronze
   ↓
2. Silver
   ↓
3. Gold
   ↓
4. Análise
```

Cada etapa utiliza os dados gerados pela etapa anterior. Portanto, recomenda-se seguir a ordem apresentada para garantir o correto funcionamento do pipeline.

## 📄 Documentação do Projeto

Além dos notebooks, o repositório contém um **PDF com o detalhamento do projeto**, apresentando:

- descrição da solução;
- metodologia utilizada;
- processo de tratamento e transformação dos dados;
- resultados das análises;
- discussão dos resultados.
