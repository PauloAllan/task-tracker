
# Task Tracker

```markdown
Um CLI simples em Python para gerenciar suas tarefas do dia a dia.
```
## 🗂 Estrutura do Projeto

```bash
task-tracker/
├─ tasks/               # Código Python
│  ├─ **init**.py
│  ├─ cli.py
│  ├─ models.py
│  └─ storage.py
├─ data/                # Arquivo de dados (não versionado)
│  └─ tasks.json
├─ .gitignore           # Arquivos que o Git deve ignorar
└─ README.md            # Este arquivo
```
## Importante:

````

>  ".venv/" e "data/tasks.json" não estão no GitHub.  
> O ".venv/" deve ser criado localmente.

````
---

## ⚡ Funcionalidades
````
- Adicionar tarefas
- Listar tarefas
- Marcar tarefa como concluída
- Editar título de tarefa
- Remover tarefas
````
---

## 💻 Como usar

1. Clone o projeto:

```bash
git clone https://github.com/PauloAllan/task-tracker.git
cd task-tracker
```


2. Crie e ative o ambiente virtual:

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Rode os comandos do CLI:

### Listar tarefas

```bash
python -m tasks.cli list
```

### Adicionar tarefa

```bash
python -m tasks.cli add "Minha tarefa"
```

### Marcar tarefa como concluída

```bash
python -m tasks.cli done 1
```

### Editar título de tarefa

```bash
python -m tasks.cli edit 1 "Novo título"
```

### Remover tarefa

```bash
python -m tasks.cli remove 1
```

## 📌 Observações

* O arquivo `data/tasks.json` será criado automaticamente na primeira execução.
* Você pode criar seu próprio `.venv` em qualquer máquina e o CLI funcionará normalmente.
* É um projeto ótimo para estudar **Python, manipulação de arquivos JSON e construção de CLI**.

---

