# 🚀 Sprint 1 — CLI de Gerenciamento de Tarefas

Este projeto consiste em uma ferramenta **CLI (Command Line Interface)** desenvolvida em Python, com o objetivo de simular a manipulação de um banco de dados de tarefas em memória.

---

## 📌 Descrição

A aplicação permite realizar operações básicas de um sistema de gerenciamento de tarefas, simulando um banco de dados sem persistência em disco.

As tarefas são armazenadas em uma estrutura de dados em memória durante a execução do programa.

---

## 🔧 Funcionalidades:
- Criação de registros
- Leitura de dados
- Atualização de informações
- Remoção de registros

---
## 🧠 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

- Praticar conceitos de CRUD
- Trabalhar com estruturas de dados em memória

## 🧱 Estrutura da Tarefa

Cada tarefa segue o seguinte formato:

```json
{
  "id": {
    "title": "",
    "description": "",
    "status": ""
  }
}
```
## como executar 

```bash
git clone https://github.com/pedrohebert/curso_backend.git
cd curso_backend/sprint1
python main.py
```

> [!NOTE]  
> verifique se a versão instalada do python é 3.12+ com:
> ``` bash
> python --version
> ```

