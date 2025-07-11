import os
import csv
import json
from datetime import datetime
import re
import zipfile

BASE_DIR = 'src'
DADOS_DIR = os.path.join(BASE_DIR, 'dados')
BACKUP_DIR = os.path.join(BASE_DIR, 'backup')
TEMP_DIR = os.path.join(BASE_DIR, 'temp')

for d in [DADOS_DIR, BACKUP_DIR, TEMP_DIR]:
    os.makedirs(d, exist_ok=True)

# ----------- BLOCO 1: TXT -----------

def exercicio_1_2():
    tarefas = ["Comprar pão", "Estudar Python", "Lavar roupa"]
    arq = os.path.join(DADOS_DIR, 'tarefas.txt')
    with open(arq, 'w', encoding='utf-8') as f:
        for t in tarefas:
            f.write(t + '\n')

def exercicio_1_3():
    metas = ["Fazer exercício 3 vezes por semana", "Ler 12 livros por ano"]
    arq = os.path.join(DADOS_DIR, 'metas.txt')
    with open(arq, 'w', encoding='utf-8') as f:
        for m in metas:
            f.write(m + '\n')

def exercicio_1_5():
    arq = os.path.join(DADOS_DIR, 'tarefas.txt')
    with open(arq, 'r', encoding='utf-8') as f:
        tarefas = f.readlines()
    for i, t in enumerate(tarefas, 1):
        print(f"{i}. {t.strip()}")

def exercicio_1_6():
    arq = os.path.join(DADOS_DIR, 'metas.txt')
    with open(arq, 'r', encoding='utf-8') as f:
        metas = f.readlines()
    for m in metas:
        print(f"- {m.strip()}")

def exercicio_1_8():
    nova = "Pagar contas"
    arq = os.path.join(DADOS_DIR, 'tarefas.txt')
    with open(arq, 'a', encoding='utf-8') as f:
        f.write(nova + '\n')

def exercicio_1_9():
    progresso = "Correr 5 km em menos de 30 minutos"
    arq = os.path.join(DADOS_DIR, 'metas.txt')
    with open(arq, 'a', encoding='utf-8') as f:
        f.write(progresso + '\n')

def exercicio_1_11():
    arq = os.path.join(DADOS_DIR, 'tarefas.txt')
    with open(arq, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    print(f"Tarefas registradas: {len(linhas)}")

def exercicio_1_12():
    arq = os.path.join(DADOS_DIR, 'tarefas.txt')
    with open(arq, 'r', encoding='utf-8') as f:
        tarefas = f.readlines()
    urgentes = [t.strip() for t in tarefas if 'urgente' in t.lower()]
    if urgentes:
        print("Tarefas com 'urgente':")
        for t in urgentes:
            print(f"- {t}")
    else:
        print("Nenhuma tarefa com 'urgente'.")

def exercicio_1_14():
    data_str = datetime.now().strftime('%Y%m%d')
    origem = os.path.join(DADOS_DIR, 'tarefas.txt')
    destino = os.path.join(BACKUP_DIR, f'tarefas_backup_{data_str}.txt')
    with open(origem, 'r', encoding='utf-8') as f_origem, open(destino, 'w', encoding='utf-8') as f_destino:
        f_destino.write(f_origem.read())
    print(f"Backup criado em: {destino}")

def exercicio_1_15():
    origem = os.path.join(DADOS_DIR, 'metas.txt')
    destino = os.path.join(DADOS_DIR, 'metas_prioridade.txt')
    with open(origem, 'r', encoding='utf-8') as f:
        metas = f.readlines()
    with open(destino, 'w', encoding='utf-8') as f:
        for m in metas:
            f.write(m.strip().upper() + '\n')

# ----------- BLOCO 2: CSV -----------

def exercicio_2_2():
    arq = os.path.join(DADOS_DIR, 'produtos.csv')
    cabecalho = ['id', 'nome', 'preço', 'estoque']
    produtos = [
        ['1', 'Camiseta', '49.90', '20'],
        ['2', 'Calça Jeans', '120.00', '15'],
        ['3', 'Tênis', '250.00', '10'],
    ]
    with open(arq, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(cabecalho)
        writer.writerows(produtos)

def exercicio_2_3():
    arq = os.path.join(DADOS_DIR, 'eventos.csv')
    cabecalho = ['artista', 'local', 'data', 'ingressos']
    eventos = [
        ['Coldplay', 'Maracanã', '2025-09-10', '5000'],
        ['Beyoncé', 'Allianz Parque', '2025-10-05', '3000'],
        ['Ed Sheeran', 'Morumbi', '2025-11-20', '0'],
    ]
    with open(arq, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(cabecalho)
        writer.writerows(eventos)

def exercicio_2_5():
    arq = os.path.join(DADOS_DIR, 'produtos.csv')
    total = 0
    with open(arq, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            preco = float(row['preço'])
            estoque = int(row['estoque'])
            total += preco * estoque
    print(f"Valor total do estoque: R$ {total:.2f}")

def exercicio_2_6():
    arq = os.path.join(DADOS_DIR, 'eventos.csv')
    with open(arq, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        eventos_disponiveis = [row for row in reader if int(row['ingressos']) > 0]
    if eventos_disponiveis:
        print("Eventos com ingressos disponíveis:")
        for ev in eventos_disponiveis:
            print(f"- {ev['artista']} em {ev['local']} na data {ev['data']}")
    else:
        print("Nenhum evento com ingressos disponíveis.")

def exercicio_2_8():
    novos_produtos = [
        ['4', 'Jaqueta', '180.00', '8'],
        ['5', 'Boné', '35.00', '25'],
        ['6', 'Meias', '15.00', '50'],
    ]
    arq = os.path.join(DADOS_DIR, 'produtos.csv')
    with open(arq, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(novos_produtos)

def exercicio_2_9():
    novo_show = ['Adele', 'Espaço das Américas', '2025-12-15', '2000']
    arq = os.path.join(DADOS_DIR, 'eventos.csv')
    with open(arq, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(novo_show)

def exercicio_2_11():
    arq = os.path.join(DADOS_DIR, 'produtos.csv')
    precos = []
    with open(arq, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            precos.append(float(row['preço']))
    media = sum(precos) / len(precos) if precos else 0
    print(f"Média dos preços dos produtos: R$ {media:.2f}")

def exercicio_2_12():
    arq = os.path.join(DADOS_DIR, 'eventos.csv')
    evento_alvo = 'Coldplay'
    novo_ingressos = '4800'
    eventos = []
    with open(arq, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['artista'] == evento_alvo:
                row['ingressos'] = novo_ingressos
            eventos.append(row)
    with open(arq, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['artista', 'local', 'data', 'ingressos'])
        writer.writeheader()
        writer.writerows(eventos)
    print(f"Ingressos do evento {evento_alvo} atualizados para {novo_ingressos}.")

def exercicio_2_14():
    arq = os.path.join(DADOS_DIR, 'produtos.csv')
    ids = set()
    repetidos = set()
    with open(arq, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['id'] in ids:
                repetidos.add(row['id'])
            else:
                ids.add(row['id'])
    if repetidos:
        print(f"IDs repetidos encontrados: {', '.join(repetidos)}")
    else:
        print("Todos os IDs de produtos são únicos.")

def exercicio_2_15():
    # Sistema de busca por artista no eventos.csv
    artista_busca = input("Digite o nome do artista para busca: ").strip()
    arq = os.path.join(DADOS_DIR, 'eventos.csv')
    encontrados = []
    with open(arq, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if artista_busca.lower() in row['artista'].lower():
                encontrados.append(row)
    if encontrados:
        print(f"Eventos encontrados para '{artista_busca}':")
        for e in encontrados:
            print(f"- {e['artista']} em {e['local']} na data {e['data']} com {e['ingressos']} ingressos")
    else:
        print(f"Nenhum evento encontrado para o artista '{artista_busca}'.")

# ----------- BLOCO 3: JSON -----------

def exercicio_3_2():
    perfil = {
        "username": "influenciador_123",
        "seguidores": 15000,
        "seguindo": 200,
        "posts": 120,
        "biografia": "Amo viajar e compartilhar dicas de lifestyle."
    }
    arq = os.path.join(DADOS_DIR, 'perfil_instagram.json')
    with open(arq, 'w', encoding='utf-8') as f:
        json.dump(perfil, f, indent=4, ensure_ascii=False)

def exercicio_3_3():
    monstro = {
        "nome": "Goblin",
        "tipo": "Inimigo",
        "nivel": 5,
        "pontos_ataque": 25,
        "recompensas": {
            "ouro": 50,
            "itens": ["Espada pequena", "Escudo leve"]
        }
    }
    arq = os.path.join(DADOS_DIR, 'monstro.json')
    with open(arq, 'w', encoding='utf-8') as f:
        json.dump(monstro, f, indent=4, ensure_ascii=False)

def exercicio_3_5():
    arq = os.path.join(DADOS_DIR, 'perfil_instagram.json')
    with open(arq, encoding='utf-8') as f:
        perfil = json.load(f)
    taxa = perfil['seguidores'] / perfil['posts'] if perfil['posts'] > 0 else 0
    print(f"Taxa de engajamento média: {taxa:.2f} seguidores por post")

def exercicio_3_6():
    arq = os.path.join(DADOS_DIR, 'monstro.json')
    with open(arq, encoding='utf-8') as f:
        monstro = json.load(f)
    ouro = monstro['recompensas'].get('ouro', 0)
    print(f"Recompensa mais valiosa: {ouro} moedas de ouro")

def exercicio_3_8():
    arq = os.path.join(DADOS_DIR, 'perfil_instagram.json')
    with open(arq, encoding='utf-8') as f:
        perfil = json.load(f)
    novo_post = {"data": "2025-07-11", "likes": 500}
    if 'posts_lista' not in perfil:
        perfil['posts_lista'] = []
    perfil['posts_lista'].append(novo_post)
    with open(arq, 'w', encoding='utf-8') as f:
        json.dump(perfil, f, indent=4, ensure_ascii=False)
    print("Novo post adicionado ao perfil Instagram.")

def exercicio_3_9():
    arq = os.path.join(DADOS_DIR, 'monstro.json')
    with open(arq, encoding='utf-8') as f:
        monstro = json.load(f)
    monstro['pontos_ataque'] += 10
    with open(arq, 'w', encoding='utf-8') as f:
        json.dump(monstro, f, indent=4, ensure_ascii=False)
    print(f"Pontos de ataque do monstro atualizados para {monstro['pontos_ataque']}.")

def exercicio_3_11():
    arq = os.path.join(DADOS_DIR, 'perfil_instagram.json')
    with open(arq, encoding='utf-8') as f:
        perfil = json.load(f)
    if perfil.get('seguidores', 0) > 10000:
        print("Perfil tem mais de 10.000 seguidores.")
    else:
        print("Perfil tem menos de 10.000 seguidores.")

def exercicio_3_12():
    arq = os.path.join(DADOS_DIR, 'monstro.json')
    with open(arq, encoding='utf-8') as f:
        monstro = json.load(f)
    ouro = monstro['recompensas'].get('ouro', 0)
    itens = monstro['recompensas'].get('itens', [])
    print(f"Total recompensas: {ouro} moedas de ouro e {len(itens)} itens.")

def exercicio_3_14():
    data_str = datetime.now().strftime('%Y%m%d')
    origem = os.path.join(DADOS_DIR, 'perfil_instagram.json')
    destino = os.path.join(BACKUP_DIR, f'perfil_instagram_backup_{data_str}.json')
    with open(origem, 'r', encoding='utf-8') as f_origem, open(destino, 'w', encoding='utf-8') as f_destino:
        f_destino.write(f_origem.read())
    print(f"Backup do perfil Instagram criado: {destino}")

def exercicio_3_15():
    p1 = {
        "nome": "Arya Stark",
        "nivel": 16,
        "hp": 320,
        "habilidades": ["Agilidade", "Furtividade", "Disfarces"]
    }
    p2 = {
        "nome": "Jon Snow",
        "nivel": 20,
        "hp": 400,
        "habilidades": ["Espada", "Liderança", "Resistência"]
    }
    grupo = [p1, p2]
    arq = os.path.join(DADOS_DIR, 'grupo.json')
    with open(arq, 'w', encoding='utf-8') as f:
        json.dump(grupo, f, indent=4, ensure_ascii=False)
    print(f"Arquivo grupo.json criado com {len(grupo)} personagens.")

# ----------- BLOCO 4: EXERCÍCIOS MISTOS -----------

def exercicio_4_2():
    itens = ['Espada', 'Escudo', 'Poção']
    arq_txt = os.path.join(DADOS_DIR, 'inventario.txt')
    with open(arq_txt, 'w', encoding='utf-8') as f:
        for item in itens:
            f.write(item + '\n')
    arq_csv = os.path.join(DADOS_DIR, 'inventario.csv')
    with open(arq_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['item'])
        for item in itens:
            writer.writerow([item])
    arq_json = os.path.join(DADOS_DIR, 'inventario.json')
    with open(arq_json, 'w', encoding='utf-8') as f:
        json.dump(itens, f, indent=4, ensure_ascii=False)
    print("Inventário salvo em TXT, CSV e JSON.")

def exercicio_4_3():
    feed = [
        {"titulo": "Nova atualização lançada", "data": "2025-07-10"},
        {"titulo": "Evento especial começa amanhã", "data": "2025-07-11"}
    ]
    arq_json = os.path.join(DADOS_DIR, 'feed.json')
    with open(arq_json, 'w', encoding='utf-8') as f:
        json.dump(feed, f, indent=4, ensure_ascii=False)
    arq_txt = os.path.join(DADOS_DIR, 'feed.txt')
    with open(arq_txt, 'w', encoding='utf-8') as f:
        for noticia in feed:
            f.write(f"{noticia['data']} - {noticia['titulo']}\n")
    print("Feed salvo em JSON e TXT.")

def exercicio_4_4():
    arq_json = os.path.join(DADOS_DIR, 'perfil_instagram.json')
    arq_csv = os.path.join(DADOS_DIR, 'perfil_relatorio.csv')
    with open(arq_json, encoding='utf-8') as f:
        perfil = json.load(f)
    with open(arq_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Campo', 'Valor'])
        for k, v in perfil.items():
            writer.writerow([k, v])
    print("Relatório CSV do perfil criado.")

def exercicio_4_5():
    zip_path = os.path.join(BACKUP_DIR, 'savegame.zip')
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for filename in os.listdir(DADOS_DIR):
            if filename.endswith(('.json', '.txt', '.csv')):
                zipf.write(os.path.join(DADOS_DIR, filename), arcname=filename)
    print(f"Save game compactado em {zip_path}")

# ----------- Chamadas para teste ------------

if __name__ == '__main__':
    print("Executando todos os exercícios (TXT, CSV, JSON, MISTOS)...\n")

    # BLOCO 1 - TXT
    exercicio_1_2()
    exercicio_1_3()
    exercicio_1_5()
    exercicio_1_6()
    exercicio_1_8()
    exercicio_1_9()
    exercicio_1_11()
    exercicio_1_12()
    exercicio_1_14()
    exercicio_1_15()
    print("\n--- BLOCO 1 TXT executado ---\n")

    # BLOCO 2 - CSV
    exercicio_2_2()
    exercicio_2_3()
    exercicio_2_5()
    exercicio_2_6()
    exercicio_2_8()
    exercicio_2_9()
    exercicio_2_11()
    exercicio_2_12()
    exercicio_2_14()
    # Para exercicio_2_15, por ser interativo, descomente para usar
    # exercicio_2_15()
    print("\n--- BLOCO 2 CSV executado ---\n")

    # BLOCO 3 - JSON
    exercicio_3_2()
    exercicio_3_3()
    exercicio_3_5()
    exercicio_3_6()
    exercicio_3_8()
    exercicio_3_9()
    exercicio_3_11()
    exercicio_3_12()
    exercicio_3_14()
    exercicio_3_15()
    print("\n--- BLOCO 3 JSON executado ---\n")

    # BLOCO 4 - MISTOS
    exercicio_4_2()
    exercicio_4_3()
    exercicio_4_4()
    exercicio_4_5()
    print("\n--- BLOCO 4 MISTOS executado ---\n")
