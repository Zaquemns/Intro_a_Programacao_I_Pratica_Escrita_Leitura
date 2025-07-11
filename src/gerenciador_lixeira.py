import os
import csv
import json

# Diretórios base
BASE_DIR = 'src'
DADOS_DIR = os.path.join(BASE_DIR, 'dados')
BACKUP_DIR = os.path.join(BASE_DIR, 'backup')
TEMP_DIR = os.path.join(BASE_DIR, 'temp')

# Criar pastas se não existirem
for d in [DADOS_DIR, BACKUP_DIR, TEMP_DIR]:
    os.makedirs(d, exist_ok=True)

# --- TXT: tarefas.txt e lixeira_tarefas.txt ---
ARQ_TAREFAS = os.path.join(DADOS_DIR, 'tarefas.txt')
ARQ_LIXEIRA_TXT = os.path.join(BACKUP_DIR, 'lixeira_tarefas.txt')

def listar_tarefas():
    try:
        with open(ARQ_TAREFAS, 'r') as f:
            tarefas = [l.strip() for l in f.readlines()]
    except FileNotFoundError:
        tarefas = []
    return tarefas

def salvar_tarefas(tarefas):
    with open(ARQ_TAREFAS, 'w') as f:
        for t in tarefas:
            f.write(t + '\n')

def listar_lixeira_txt():
    try:
        with open(ARQ_LIXEIRA_TXT, 'r') as f:
            excluidas = [l.strip() for l in f.readlines()]
    except FileNotFoundError:
        excluidas = []
    return excluidas

def salvar_lixeira_txt(tarefas):
    with open(ARQ_LIXEIRA_TXT, 'w') as f:
        for t in tarefas:
            f.write(t + '\n')

def excluir_tarefa_txt(indice):
    tarefas = listar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        salvar_tarefas(tarefas)
        lixeira = listar_lixeira_txt()
        lixeira.append(tarefa_removida)
        salvar_lixeira_txt(lixeira)
        print(f"Tarefa '{tarefa_removida}' movida para a lixeira.")
    else:
        print("Índice inválido.")

def restaurar_tarefa_txt(indice):
    lixeira = listar_lixeira_txt()
    if 0 <= indice < len(lixeira):
        tarefa_restaurada = lixeira.pop(indice)
        salvar_lixeira_txt(lixeira)
        tarefas = listar_tarefas()
        tarefas.append(tarefa_restaurada)
        salvar_tarefas(tarefas)
        print(f"Tarefa '{tarefa_restaurada}' restaurada da lixeira.")
    else:
        print("Índice inválido.")

# --- CSV: contatos.csv e lixeira_contatos.csv ---
ARQ_CONTATOS = os.path.join(DADOS_DIR, 'contatos.csv')
ARQ_LIXEIRA_CSV = os.path.join(BACKUP_DIR, 'lixeira_contatos.csv')

def listar_contatos():
    try:
        with open(ARQ_CONTATOS, newline='') as f:
            reader = csv.reader(f)
            contatos = list(reader)
    except FileNotFoundError:
        contatos = []
    return contatos

def salvar_contatos(contatos):
    with open(ARQ_CONTATOS, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(contatos)

def listar_lixeira_csv():
    try:
        with open(ARQ_LIXEIRA_CSV, newline='') as f:
            reader = csv.reader(f)
            excluidos = list(reader)
    except FileNotFoundError:
        excluidos = []
    return excluidos

def salvar_lixeira_csv(contatos):
    with open(ARQ_LIXEIRA_CSV, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(contatos)

def excluir_contato_csv(indice):
    contatos = listar_contatos()
    if len(contatos) == 0:
        print("Arquivo vazio.")
        return
    if 0 <= indice < len(contatos):
        contato_removido = contatos.pop(indice)
        salvar_contatos(contatos)
        lixeira = listar_lixeira_csv()
        lixeira.append(contato_removido)
        salvar_lixeira_csv(lixeira)
        print(f"Contato '{contato_removido}' movido para a lixeira.")
    else:
        print("Índice inválido.")

def restaurar_contato_csv(indice):
    lixeira = listar_lixeira_csv()
    if 0 <= indice < len(lixeira):
        contato_restaurado = lixeira.pop(indice)
        salvar_lixeira_csv(lixeira)
        contatos = listar_contatos()
        contatos.append(contato_restaurado)
        salvar_contatos(contatos)
        print(f"Contato '{contato_restaurado}' restaurado da lixeira.")
    else:
        print("Índice inválido.")

# --- JSON: personagem.json e lixeira_personagem.json ---
ARQ_PERSONAGEM = os.path.join(DADOS_DIR, 'personagem.json')
ARQ_LIXEIRA_JSON = os.path.join(BACKUP_DIR, 'lixeira_personagem.json')

def listar_personagens():
    try:
        with open(ARQ_PERSONAGEM, 'r') as f:
            personagens = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        personagens = []
    return personagens

def salvar_personagens(personagens):
    with open(ARQ_PERSONAGEM, 'w') as f:
        json.dump(personagens, f, indent=4)

def listar_lixeira_json():
    try:
        with open(ARQ_LIXEIRA_JSON, 'r') as f:
            excluidos = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        excluidos = []
    return excluidos

def salvar_lixeira_json(personagens):
    with open(ARQ_LIXEIRA_JSON, 'w') as f:
        json.dump(personagens, f, indent=4)

def excluir_personagem(indice):
    personagens = listar_personagens()
    if 0 <= indice < len(personagens):
        personagem_removido = personagens.pop(indice)
        salvar_personagens(personagens)
        lixeira = listar_lixeira_json()
        lixeira.append(personagem_removido)
        salvar_lixeira_json(lixeira)
        print(f"Personagem '{personagem_removido.get('nome', 'desconhecido')}' movido para a lixeira.")
    else:
        print("Índice inválido.")

def restaurar_personagem(indice):
    lixeira = listar_lixeira_json()
    if 0 <= indice < len(lixeira):
        personagem_restaurado = lixeira.pop(indice)
        salvar_lixeira_json(lixeira)
        personagens = listar_personagens()
        personagens.append(personagem_restaurado)
        salvar_personagens(personagens)
        print(f"Personagem '{personagem_restaurado.get('nome', 'desconhecido')}' restaurado da lixeira.")
    else:
        print("Índice inválido.")
