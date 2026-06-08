# 🐄 Fazenda Sertão — Sistema de Gestão Rural

> Projeto desenvolvido para a disciplina de **Algoritmos e Lógica de Programação** — versão refatorada com arquitetura modular.

---

## 📋 Sobre o Projeto

O **Fazenda Sertão** é um sistema de gestão rural desenvolvido em Python como projeto avaliativo da cadeira de **Algoritmos e Lógica de Programação**. O sistema simula o gerenciamento de uma fazenda, permitindo o controle de animais, produção de leite, estoque de produtos e atendimento a clientes.

Esta versão é uma **refatoração completa** da versão original. O código foi reorganizado em uma arquitetura modular, com separação de responsabilidades em pacotes dedicados, adoção de dicionários no lugar de listas aninhadas e integração com bibliotecas externas para enriquecer a experiência no terminal e gerar documentos reais.

---

## 🗂️ Estrutura do Projeto

```
fazenda-sertao/
│
├── main.py                  # Ponto de entrada da aplicação
├── menu.py                  # Lógica e renderização dos menus
│
├── auth/
│   └── auth.py              # Autenticação e controle de login
│
├── config/
│   └── constantes.py        # Constantes globais (tipos, status, prefixos)
│
├── database/
│   └── dados.py             # Estruturas de dados em memória (estado global)
│
├── fazenda/
│   ├── animais.py           # CRUD de animais
│   ├── producao.py          # Registro e visualização de produção de leite
│   ├── estoque.py           # Gestão de produtos e estoque
│   ├── relatorio.py         # Relatório geral e histórico de movimentações
│   ├── usuarios.py          # Cadastro de usuários
│   └── cliente.py           # Funcionalidades do perfil cliente
│
├── utils/
│   ├── utils.py             # Componentes de UI: tabelas, menus, títulos
│   └── helpers.py           # Utilitários: limpar tela, gerar ID, CEP, nota fiscal
│
└── notas/
    └── nota_fiscal.pdf      # Nota fiscal gerada ao agendar retirada
```

> Na versão original, todo o código estava concentrado em um único arquivo `main.py`. A refatoração separou as responsabilidades em módulos e pacotes independentes.

---

## 🚀 Funcionalidades

O sistema possui dois perfis de acesso: **Administrador** e **Cliente**.

### 🔐 Autenticação

- Login com usuário e senha
- Verificação de credenciais via lista de usuários em memória
- Redirecionamento automático para o menu correspondente ao perfil

---

### 🛠️ Menu do Administrador

| Opção | Categoria | Funcionalidade |
|-------|-----------|----------------|
| 1 | Animais | Cadastrar Animal |
| 2 | Animais | Buscar Animal |
| 3 | Animais | Atualizar Animal |
| 4 | Animais | Remover Animal |
| 5 | Animais | Listar Animais |
| 6 | Produção | Registrar Produção de Leite |
| 7 | Produção | Gráfico de Produção de Leite |
| 8 | Estoque | Cadastrar Produto |
| 9 | Estoque | Adicionar Produto ao Estoque |
| 10 | Estoque | Ver Estoque Atual |
| 11 | Painel | Relatório Geral da Fazenda |
| 12 | Painel | Histórico de Movimentação |
| 13 | Sistema | Cadastrar Usuário |
| 14 | Sistema | Sair |

**Detalhes das funcionalidades:**

- **Cadastro de Animais:** suporta Bovino de Leite, Caprino, Ovino e Suíno. O ID é gerado automaticamente com prefixo por tipo (ex: `BOV-0001`, `CAP-0002`), eliminando duplicatas sem intervenção manual.
- **Busca e Atualização:** localiza animais por identificação e permite editar tipo, identificação ou status individualmente.
- **Remoção:** exibe os dados do animal e solicita confirmação antes de excluir.
- **Produção de Leite:** acumula litros produzidos por mês ao longo do ano, validando valores negativos.
- **Gráfico de Produção:** exibe um gráfico de barras horizontal no terminal com escala proporcional ao mês de maior produção.
- **Gestão de Produtos:** criação de produtos com nome, peso (kg) e preço, com validação de nome duplicado e estoque inicial zerado. Toda entrada de estoque é registrada no histórico.
- **Relatório Geral *(novo)*:** painel consolidado com rebanho por tipo (usando `Counter`), total acumulado de produção de leite com destaque do mês pico, e resumo do estoque de queijo com peso total.
- **Histórico de Movimentação *(novo)*:** tabela com data, ação (Cadastro, Entrada, Compra), item e quantidade de cada operação realizada no sistema.
- **Cadastro de Usuário:** cria novos usuários com validação de nome único, mínimo de 4 caracteres para usuário e senha, e definição de permissão de administrador.

---

### 🛒 Menu do Cliente

| Opção | Funcionalidade |
|-------|----------------|
| 1 | Ver Estoque Disponível |
| 2 | Comprar Produto |
| 3 | Comprar Animal |
| 4 | Agendar Retirada |
| 5 | Registrar Interesse em Produto |
| 6 | Ver Meus Interesses |
| 7 | Sair |

**Detalhes das funcionalidades:**

- **Estoque Disponível:** o cliente pode escolher entre visualizar o estoque de animais ou o de produtos.
- **Comprar Produto:** o cliente pode comprar a partir da lista geral ou diretamente da sua lista de interesses. Valida estoque disponível antes de confirmar, debita a quantidade e registra a movimentação.
- **Comprar Animal:** lista somente animais com status "Disponível p/ venda". Após a compra, o animal é removido do sistema e adicionado à lista de compras.
- **Agendar Retirada *(expandido)*:** permite agendar data e horário de entrega, informar o nome/razão social do cliente e buscar o endereço completo via **API ViaCEP** pelo CEP. Ao confirmar, uma **nota fiscal em PDF** é gerada automaticamente na pasta `notas/`.
- **Registrar Interesse:** o cliente marca produtos de interesse para acompanhamento futuro, sem duplicatas.
- **Ver Meus Interesses:** exibe todos os produtos que o cliente sinalizou interesse, com informações de peso, estoque e preço.

---

## 🆕 O Que Mudou na Refatoração

| Aspecto | Versão Original | Versão Refatorada |
|---------|-----------------|-------------------|
| Organização | Arquivo único (`main.py`) | Módulos em pacotes separados |
| Estrutura de dados | Listas aninhadas `[[...]]` | Dicionários `{...}` |
| Interface no terminal | `print()` simples | `rich` (tabelas, painéis, cores) |
| IDs dos animais | Inserção manual pelo usuário | Geração automática com prefixo |
| Endereço de entrega | Digitação livre | Consulta automática por CEP (ViaCEP) |
| Nota fiscal | Não existia | PDF gerado via `fpdf2` |
| Relatório | Não existia | Painel consolidado com `rich` |
| Histórico | Não existia | Log de todas as movimentações |
| Dependências | Nenhuma (stdlib puro) | `rich`, `requests`, `fpdf2` |
| Menu Admin | 12 opções | 14 opções |

---

## 🗃️ Estrutura de Dados

Os dados são armazenados em memória como **listas de dicionários**, evoluindo das listas aninhadas da versão original:

```python
# Usuários
usuarios = [
    {"usuario": "johndoe", "senha": "12345", "permissao": True},
    {"usuario": "janedoe", "senha": "12345", "permissao": False}
]

# Animais: ID gerado automaticamente (ex: BOV-0001)
animais = [
    {"tipo": "Bovino de Leite", "identificacao": "BOV-0001", "status": "Em lactação"}
]

# Métricas mensais de produção de leite
metricas = [
    {"mes": "Jan", "producao": 0.0},
    {"mes": "Fev", "producao": 0.0},
    # ... até Dezembro
]

# Produtos
produtos = [
    {"nome": "Queijo Minas", "peso": 0.5, "estoque": 10, "preco": 25.90}
]

# Histórico de movimentações
historico = [
    {"data": "08/06/2026", "acao": "Entrada", "item": "Queijo Minas", "quantidade": 10}
]

# Auxiliares
lista_compras = []   # Compras realizadas na sessão
agendamentos = []    # Retiradas agendadas
lista_interesses = []  # Interesses do cliente
```

---

## ▶️ Como Executar

**Pré-requisito:** Python 3.12 ou superior.

**1. Clone ou baixe o projeto:**

```bash
git clone https://github.com/seu-usuario/fazenda-sertao.git
cd fazenda-sertao
```

**2. Instale as dependências:**

```bash
pip install rich requests fpdf2
```

**3. Execute o programa:**

```bash
python main.py
```

---

## 🔑 Credenciais de Acesso (Padrão)

| Usuário | Senha | Perfil |
|---------|-------|--------|
| `johndoe` | `12345` | Administrador |
| `janedoe` | `12345` | Cliente |

> Novos usuários podem ser criados pelo administrador através da opção **13 — Cadastrar Usuário** no menu.

---

## 💡 Referência Rápida

### Tipos de Animais

| Prefixo | Tipo |
|---------|------|
| `BOV` | Bovino de Leite |
| `CAP` | Caprino |
| `OVI` | Ovino |
| `SUI` | Suíno |

### Status dos Animais

| Status | Descrição |
|--------|-----------|
| Em lactação | Animal em produção de leite |
| Para engorda | Animal destinado ao abate |
| Disponível p/ venda | Animal visível e comprável pelo cliente |

---

## 📦 Dependências

| Biblioteca | Uso |
|------------|-----|
| `rich` | Tabelas, painéis e formatação no terminal |
| `requests` | Consulta de CEP via API ViaCEP |
| `fpdf2` | Geração de nota fiscal em PDF |
| `collections.Counter` | Contagem de animais por tipo no relatório |
| `datetime` | Validação de datas/horas e registro no histórico |

---

## 📌 Observações

- Os dados **não são persistidos** entre execuções. Ao encerrar o programa, todas as informações são perdidas.
- A nota fiscal gerada é salva em `notas/nota_fiscal.pdf` e **sobrescrita** a cada novo agendamento. A pasta `notas/` está listada no `.gitignore`.
- A consulta de CEP requer conexão com a internet (API pública [ViaCEP](https://viacep.com.br)). Em caso de falha, o sistema informa o erro e solicita novo CEP.
- Validações de entrada (valores negativos, campos vazios, opções fora do intervalo, datas e horas malformadas) são tratadas com loops `while` em todas as funções.

---

*Projeto desenvolvido com fins exclusivamente acadêmicos.*