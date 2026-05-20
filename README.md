## Sumario 

- [Dados](#dados)  
    - [Task](#task)  
    - [Pulbic Task](#pulbic-task)
    - [Update Task](#update-task)   
+ [Endpoints](#endpoints)  
    - [GET all](#get-all)
    - [GET por id](#get-id)
    - [GET com filtros](#get-)
    - [POST/criar Task](#post-)
    - [PUT/atualizar Task](#put-id)
    - [DELETE/deletar Task](#delete-id)  
* [como executar o projeto](#como-executar-o-projeto)

## sobre

esse projeto é um conjunto de api em fastApi para armazenar em memória tasks.

### Dados
#### Task
```json
{
  "title": "string"
  "description": "string" | null
  "status": "TO DO" |"IN PROGRESS" | "COMPLETED" | null
}
```
>[!NOTE]
> "TO DO" é o valor padrão pra status

#### pulbic Task
retorno comum

```json
{
  "title": "string"
  "description": "string" | null
  "status": "TO DO" | "IN PROGRESS" | "COMPLETED"
  "id": int
}
```

#### update task
utilizados para atualizar tesks

campos null ou não presentes não serão atualizados
```json
{
  "title": "string" | null
  "description": "string" | null
  "status": "TO DO" | "IN PROGRESS" | "COMPLETED" | null
}
```

---
### Endpoints

#### GET "/all"
retorna todas as tasks armazenadas como uma lista de public_task
exemplo de resposta:
```json
[
  {
    "title": "string"
    "description": "string"
    "status": "TO DO" | "IN PROGRESS" | "COMPLETED"
    "id": int
  }
]
```

#### GET "/{id}"
retorna a task correspondete ao id no formato public_task ou um erro 404 caso id não exista

exemplo de resposta:
```json
{
  "title": "string"
  "description": "string" | null
  "status": "TO DO" | "IN PROGRESS" | "COMPLETED"
  "id": int
}
```

#### GET "/"
parametros:
- title: string
- description: string
- status: string  

uma busca filtrada nos dados salvos, retorna uma lista de publicTasks

```json
[
  {
    "title": "string"
    "description": "string"
    "status": "TO DO" | "IN PROGRESS" | "COMPLETED"
    "id": int
  }
]
```

#### POST "/"
cria uma nova task, recebe no body um Task e responde um public_task
exemplo de body:
```json
{
  "title": "string"
  "description": "string" | null
  "status": "TO DO" | "IN PROGRESS" | "COMPLETED" | null
}
```

>[!NOTE]
> caso o status não seja preenchido ou seja null será substitituido por "TO DO"

exemplo de resposta:

```json
{
  "title": "string"
  "description": "string" | null
  "status": "TO DO" | "IN PROGRESS" | "COMPLETED"
  "id": int
}
```

#### PATCH "/{id}"
atualiza uma task existente, recebe um update_taskno body e retorna um public_task atualizado

campos null ou não presentes no Body não serão atualizados

exemplo de body:
```json
{
  "title": "string" | null
  "description": "string" | null
  "status": "TO DO" | "IN PROGRESS" | "COMPLETED" | null
}
```
exemplo de resposta:

```json
{
  "title": "string"
  "description": "string" | null
  "status": "TO DO" | "IN PROGRESS" | "COMPLETED"
  "id": int
}
```

#### DELETE "/{id}"
deleta um task existente, retorna a public_task deletada

exemplo de resposta:
```json
{
  "title": "string"
  "description": "string" | null
  "status": "TO DO" | "IN PROGRESS" | "COMPLETED"
  "id": int
}
```

### extra

para mais informação, execute o projeto e acesse:
- Documentação interativa (Swagger): http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

---
## Como executar o projeto

### pre-requisitos
- python 3.12+
- git
---

1. clone o repositorio 
```bash
git clone https://github.com/pedrohebert/curso_backend.git
cd curso_backend
git swicth sprint4
```
---
### crie e ative o habiente virtual

#### uv (recomendado)

2. Criar ambiente virtual e instalar dependências
```bash
uv venv
uv sync
```
3. Ativar o ambiente

Linux / Mac

```bash
source ./.venv/bin/activate
#fish
source ./.venv/bin/activate.fish 
```

Windows

```bash
.venv\Scripts\activate
```

4. Executar o servidor

```bash
uv run uvicorn app.main:app --reload
```
---
#### Executando com pip + venv

método tradicional:

2. Criar ambiente virtual
```bash
python -m venv .venv
```
3. Ativar o ambiente

Linux / Mac

```bash
source ./.venv/bin/activate
#fish
source ./.venv/bin/activate.fish 
```

Windows

```bash
.venv\Scripts\activate
```

3. Instalar dependências

Se estiver usando requirements.txt:
```bash

pip install -r requirements.txt
```

Ou, caso use pyproject.toml:

```bash
pip install .
```

4. Executar o servidor  


```bash
uvicorn app.main:app --reload
```
