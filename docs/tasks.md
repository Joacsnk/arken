# Tarefas do Projeto Arken - Gerenciador de Senhas

Este documento detalha a divisão de tarefas para o desenvolvimento do projeto, seguindo o estilo do projeto dailyflow. Cada tarefa é descrita com nome, explicação, tempo estimado e as tecnologias envolvidas. As tarefas são divididas em commits, funcionalidades, limpeza, e outras atividades, mesmo as mais simples.

---

## 1. Preparação do Ambiente e Configurações Iniciais

### Tarefa: Iniciar Repositório Git
- **Nome:** Iniciar Repositório Git  
- **Explicação:** Criar um repositório Git local, definir as configurações iniciais e fazer o primeiro commit com o README.md e a estrutura base do projeto.  
- **Tempo Estimado:** 30 minutos  
- **Tecnologias:** Git, Terminal/Shell  
- *Commit sugerido:* “Setup do repositório e inclusão do README.md inicial”

---

### Tarefa: Configuração do Ambiente Virtual
- **Nome:** Configurar Ambiente Virtual  
- **Explicação:** Criar um ambiente virtual para isolar as dependências do projeto e configurar o arquivo `requirements.txt` com as bibliotecas iniciais.  
- **Tempo Estimado:** 15 minutos  
- **Tecnologias:** Python (venv ou virtualenv), Pip  
- *Commit sugerido:* “Criação do ambiente virtual e arquivo requirements.txt”

---

### Tarefa: Definir Estrutura de Pastas
- **Nome:** Estrutura de Pastas Inicial  
- **Explicação:** Criar a estrutura de pastas conforme o planejamento (ex.: pacote `arken`, subpastas `core`, `backup` e `data`) e adicionar arquivos iniciais como `__init__.py`.  
- **Tempo Estimado:** 20 minutos  
- **Tecnologias:** Terminal, Editor de Texto, Markdown  
- *Commit sugerido:* “Estrutura de pastas e arquivos base configurados”

---

### Tarefa: Configurar o Arquivo .env
- **Nome:** Configurar .env  
- **Explicação:** Criar o arquivo `.env` para armazenar configurações sensíveis, como chaves de API, credenciais de email, entre outros.  
- **Tempo Estimado:** 10 minutos  
- **Tecnologias:** Editor de Texto  
- *Commit sugerido:* “Adiciona arquivo .env e configura variáveis iniciais (exemplo)”

---

## 2. Funcionalidades Básicas do Projeto

### Tarefa: Implementar Gerador de Senhas
- **Nome:** Gerador de Senhas  
- **Explicação:** Desenvolver a função `gerar_senha(nivel)` com três níveis de segurança (fraca, média, forte) e incluir testes unitários para garantir seu funcionamento.  
- **Tempo Estimado:** 1 hora  
- **Tecnologias:** Python, Módulos `random` e `secrets`  
- *Commit sugerido:* “Implementa função de geração de senhas e testes unitários”

---

### Tarefa: Implementar Gerenciador de Senhas
- **Nome:** Gerenciamento de Senhas  
- **Explicação:** Criar funções para adicionar, listar e remover senhas, utilizando um arquivo JSON (`senhas.json`) para armazenamento local.  
- **Tempo Estimado:** 1 hora e 30 minutos  
- **Tecnologias:** Python, Manipulação de JSON, Operações de Arquivo  
- *Commit sugerido:* “Cria funções para gerenciamento de senhas (adicionar, listar, remover)”

---

### Tarefa: Implementar Módulo de Criptografia
- **Nome:** Criptografia de Dados  
- **Explicação:** Desenvolver funções de criptografia e descriptografia usando a biblioteca `cryptography` (Fernet) para assegurar que o JSON seja salvo e lido com segurança.  
- **Tempo Estimado:** 2 horas  
- **Tecnologias:** Python, Biblioteca `cryptography`  
- *Commit sugerido:* “Adiciona módulo de criptografia para dados sensíveis”

---

## 3. Funcionalidades de Backup

### Tarefa: Implementar Backup via Email
- **Nome:** Backup por Email  
- **Explicação:** Criar um módulo que utilize `smtplib` e `email.message` para enviar o arquivo `senhas.json` criptografado por email, utilizando variáveis do `.env` para configuração.  
- **Tempo Estimado:** 2 horas  
- **Tecnologias:** Python, `smtplib`, Módulo `email`  
- *Commit sugerido:* “Implementa backup via email com envio do JSON criptografado”

---

### Tarefa: Implementar Backup via Google Drive
- **Nome:** Backup via Google Drive  
- **Explicação:** Desenvolver a funcionalidade que autentica via OAuth2 e realiza o upload automático do arquivo de senhas para uma pasta segura no Google Drive.  
- **Tempo Estimado:** 3 horas  
- **Tecnologias:** Python, `pydrive` ou `google-api-python-client`  
- *Commit sugerido:* “Adiciona módulo para backup no Google Drive”

---

## 4. Melhorias e Manutenção do Código

### Tarefa: Configuração de Linting e Formatação
- **Nome:** Linting e Formatação  
- **Explicação:** Configurar ferramentas como `pylint` ou `flake8` e formatação automática (ex.: Black) para manter a consistência do código.  
- **Tempo Estimado:** 30 minutos  
- **Tecnologias:** Python, Pylint, Black  
- *Commit sugerido:* “Configura linting e formatação automática do código”

---

### Tarefa: Criação de Logs e Mensagens de Erro
- **Nome:** Implementação de Logs  
- **Explicação:** Adicionar um módulo de logging para monitorar a execução, capturando mensagens de erro e informações que facilitem a depuração.  
- **Tempo Estimado:** 45 minutos  
- **Tecnologias:** Python (módulo logging)  
- *Commit sugerido:* “Adiciona sistema de logging para monitoramento e debug”

---

### Tarefa: Documentação Inline e Comentários
- **Nome:** Documentação do Código  
- **Explicação:** Inserir comentários e docstrings em todas as funções e módulos para facilitar a manutenção e a compreensão por outros desenvolvedores.  
- **Tempo Estimado:** 45 minutos  
- **Tecnologias:** Python, Boas práticas de documentação  
- *Commit sugerido:* “Insere documentação e comentários para funções principais”

---

### Tarefa: Testes Integrados e Validação Final
- **Nome:** Testes Integrados  
- **Explicação:** Executar testes integrados para garantir que todos os módulos interajam corretamente, identificando e corrigindo eventuais bugs.  
- **Tempo Estimado:** 1 hora  
- **Tecnologias:** Python (unittest ou pytest)  
- *Commit sugerido:* “Executa testes integrados e corrige bugs identificados”

---

## 5. Tarefas Administrativas e Outras Melhorias

### Tarefa: Padronização dos Commits
- **Nome:** Definir Padrão de Commits  
- **Explicação:** Estabelecer mensagens de commit padronizadas para documentar cada alteração, facilitando o acompanhamento do histórico de mudanças do projeto.  
- **Tempo Estimado:** 15 minutos  
- **Tecnologias:** Git  
- *Commit sugerido:* “Define padrão para mensagens de commit no CONTRIBUTING.md”

---

### Tarefa: Revisão Geral do Projeto
- **Nome:** Revisão e Limpeza Final  
- **Explicação:** Realizar uma revisão completa do código, removendo redundâncias e refatorando partes que possam ser otimizadas, garantindo a manutenção da qualidade do projeto.  
- **Tempo Estimado:** 1 hora  
- **Tecnologias:** Python, Revisão de Código Manual  
- *Commit sugerido:* “Revisão e refatoração final do código”

---
