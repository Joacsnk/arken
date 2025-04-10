# Projeto: Arken - Gerenciador de Senhas

## Visão Geral
Um gerenciador de senhas simples com geração de senhas seguras, armazenamento criptografado em arquivo `.json`, e sistema de backup via email e Google Drive. O foco é aprendizado prático em Python, segurança, manipulação de arquivos e integração com APIs.

---

## Etapas do Projeto

### 1. Planejamento
- Objetivo: Criar um gerenciador funcional de senhas com foco em segurança e backups automáticos.
- Estrutura base: Interface via terminal (CLI).
- Componentes principais:
  - Gerador de senhas com diferentes níveis de segurança.
  - Armazenamento local criptografado.
  - Backup automático via email.
  - Backup automático via Google Drive.

---

## Tecnologias Utilizadas

### Linguagem
- Python 3.10+

### Bibliotecas
- `random` e `secrets` – geração de senhas.
- `json` – manipulação de dados.
- `cryptography` – criptografia simétrica (Fernet).
- `smtplib`, `email` – envio de email com anexo.
- `pydrive` ou `google-api-python-client` – integração com Google Drive.

---

## Estrutura de Pastas
```
/arken
├── arken/                      # Pacote principal
│   ├── __init__.py
│   ├── main.py                 # Ponto de entrada
│   ├── core/                   # Lógica principal
│   │   ├── senha_generator.py
│   │   ├── senha_manager.py
│   │   ├── crypto_utils.py
│   ├── backup/                 # Lógica de backup
│   │   ├── email.py
│   │   ├── drive.py
│   └── data/                   # Dados do usuário
│       └── senhas.json
│
├── .env                        # Variáveis de ambiente
├── requirements.txt
└── README.md
```

---

## Etapas Detalhadas

### Etapa 1: Geração de Senhas
- Criar função `gerar_senha(nivel)` com três níveis:
  - Fraca: letras minúsculas.
  - Média: letras + números.
  - Forte: letras + números + símbolos.
- Usar `secrets.choice` para maior segurança.

### Etapa 2: Gerenciamento de Senhas
- Funções:
  - `adicionar_senha(site, usuario, senha)`
  - `listar_senhas()`
  - `remover_senha(site)`
- Usar arquivo `senhas.json` como banco de dados local.

### Etapa 3: Criptografia
- Usar `cryptography.fernet` para:
  - Criptografar conteúdo do JSON antes de salvar.
  - Descriptografar ao ler para mostrar ao usuário.
- Armazenar chave em `.env` ou gerar a partir de senha mestre (hash).

### Etapa 4: Backup via Email
- Usar `smtplib` e `email.message`:
  - Criar função que envia o `senhas.json` criptografado para um email.
  - Configurar remetente e destinatário no `.env`.

### Etapa 5: Backup via Google Drive
- Usar `pydrive` ou `google-api-python-client`:
  - Autenticação via OAuth2.
  - Upload automático do arquivo `senhas.json` para pasta segura no Drive.

---

## Extras (Futuros)
- Interface gráfica (Tkinter ou PyQt).
- Pesquisa e filtros por nome/site.
- Login com autenticação de dois fatores.

---

## Segurança
- Nunca salvar senhas em texto puro.
- Não subir arquivos `.env` ou `senhas.json` para repositórios públicos.
- Usar autenticação segura nas APIs (email e Google).

---

## Documentação e Deploy
- Criar `README.md` com instruções:
  - Instalação.
  - Geração de chave.
  - Uso dos comandos.
  - Configuração de variáveis de ambiente.
- Scripts `requirements.txt` e setup de ambiente virtual.

---

## Status
**Em planejamento.**

Próximos passos:
- Iniciar pelo módulo `senha_generator.py`
- Esboçar a estrutura do JSON e a criptografia com `crypto_utils.py`
- Implementar os backups por último

---

> Projeto pessoal com foco em prática real de segurança, automação e integração em Python.
