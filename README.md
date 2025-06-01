# Analisador de Sentimentos em Comentários

## 🧠 Sobre o projeto

Este projeto em equipe tem como objetivo desenvolver um **sistema de análise de sentimentos** capaz de identificar, classificar e pesar emoções em comentários escritos em **português**.

A aplicação lê comentários individuais ou em lote (formato JSON) e classifica cada um como **positivo**, **negativo** ou **neutro**, com base em palavras-chave pré-definidas e seus respectivos pesos.  
Além disso, implementamos o **tratamento de negações** (ex: “não gostei”, “não é ruim”) para melhorar a precisão da análise.

---

## 🔍 Funcionalidades

- Identificação de palavras positivas e negativas  
- Atribuição de pesos conforme intensidade das palavras  
- Tratamento de negações para evitar classificações erradas  
- Interface simples via terminal  
- Suporte a múltiplos comentários em JSON

---

## 🛠️ Tecnologias

- Python 3.13
- Bibliotecas padrão: `json`, `string`  
- Códigos ANSI para colorir saída no terminal

---

## 🚀 Como usar

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/sentiment-analyzer-br.git
