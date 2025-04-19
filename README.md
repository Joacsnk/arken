# 🔐 Arken – Gerenciador de Senhas Seguro

Arken é um gerenciador de senhas pessoal desenvolvido em Python com foco em **segurança, criptografia e privacidade de dados**, utilizando os padrões modernos da biblioteca `cryptography`.

## 📌 Funcionalidades

- Geração de senhas seguras e personalizadas
- Armazenamento local de senhas com **criptografia simétrica (Fernet)**
- Proteção com **senha mestre derivada com salt** (PBKDF2 + SHA256)
- Criação automática da estrutura de dados na primeira execução
- Interface simples via terminal
- Cópia automática de senhas para a área de transferência

## 🔒 Segurança

- Todas as senhas são criptografadas localmente com **Fernet (AES + HMAC)**
- A chave de criptografia real é protegida por uma **senha mestre**
- A senha mestre nunca é armazenada — uma **chave derivada segura** é usada (PBKDF2HMAC + salt)
- Arquivos sensíveis não são versionados graças a um `.gitignore` bem definido

## 🧪 Tecnologias Utilizadas

| Recurso               | Finalidade                              |
|-----------------------|------------------------------------------|
| `os`, `base64`        | Manipulação de arquivos e codificação    |
| `cryptography`        | Criptografia simétrica e derivação de chave |
| `PBKDF2HMAC` + `salt` | Geração de chave segura a partir da senha mestre |
| `Fernet`              | Criptografia e descriptografia dos dados |
| `json`                | Armazenamento local estruturado          |

## 📁 Estrutura do Projeto

```
arken/
├── core/
│   ├── gerenciador_senha.py     # Lógica de gerenciamento de senhas
│   ├── ferramentas_crypto.py    # Criptografia e segurança
│   └── senha_generator.py       # Geração de senhas personalizadas
├── data/
│   ├── senhas.json              # Arquivo com senhas criptografadas (ignorado)
│   ├── chave.key                # Chave do sistema (criptografada)
│   └── salt.salt                # Salt único usado para derivar chave
├── .env                         # Variáveis de ambiente (ignorado)
├── .gitignore
├── requirements.txt
└── main.py                      # Arquivo principal
```

## 🛠️ Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/arken.git
cd arken
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate       # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o sistema

```bash
python main.py
```

## ✅ Requisitos

- Python 3.10 ou superior
- Biblioteca `cryptography`

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).  
Você pode usá-lo, modificá-lo e distribuí-lo, desde que mantenha os créditos originais.

## 🧠 Aviso de Segurança

> Arken é um projeto local e educativo.  
> Não foi auditado profissionalmente para uso em produção sensível.  
> Use com responsabilidade e adapte conforme seu nível de segurança exigido.