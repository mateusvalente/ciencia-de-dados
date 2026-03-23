# 🚀 Laboratório de ETL e Pipeline de Dados

Ambiente educacional completo para prática em **Engenharia e Ciência de Dados**, com foco em pipelines de dados modernos.

## ✨ Ferramentas Principais

| Ferramenta | Propósito |
|-----------|----------|
| 🎨 **Apache NiFi** | ETL visual e ingestão de dados |
| ⚙️ **Apache Airflow** | Orquestração de pipelines e DAGs |
| 🐘 **PostgreSQL** | Banco relacional (dados estruturados) |
| 🍃 **MongoDB** | Banco NoSQL (dados não estruturados) |
| 🔧 **pgAdmin** | Interface de administração PostgreSQL |
| 🔍 **Mongo Express** | Interface de administração MongoDB |
| 📊 **Jupyter Notebook** | Exploração e análise de dados |
| ☁️ **Apache Hadoop HDFS** | Sistema de arquivos distribuído |
| 🎯 **Apache Hue** | Interface visual para Hadoop e HDFS |
| 📈 **Power BI** | Visualização analítica (externo) |

## 🎯 Objetivo

Este projeto oferece um ambiente **realista e educacional** para aprender:

- Ingestão de dados com ferramentas visuais e programáticas
- Transformação e limpeza (ETL)
- Orquestração de fluxos de trabalho
- Armazenamento em bancos relacionais e não-relacionais
- Boas práticas em arquitetura de dados

---

## 🏗️ Arquitetura do Ambiente

```
┌───────────────────────────────────────────────────────────────────┐
│                      DOCKER COMPOSE                               │
├──────────────────┬──────────────────┬──────────────┬──────────────┤
│  INGESTÃO        │  ORQUESTRAÇÃO    │ARMAZENAMENTO │ DISTRIBUÍDO  │
├──────────────────┼──────────────────┼──────────────┼──────────────┤
│  • Apache NiFi   │ • Apache Airflow │ • PostgreSQL │ • HDFS       │
│  • Jupyter       │ • DAGs           │ • MongoDB    │ • Hue (UI)   │
│                  │                  │ • pgAdmin    │              │
│                  │                  │ • Mongo Exp. │              │
└──────────────────┴──────────────────┴──────────────┴──────────────┘
```

### Serviços Disponíveis

- **PostgreSQL**: Banco relacional principal
- **pgAdmin**: Gerenciador web do PostgreSQL
- **MongoDB**: Banco de dados NoSQL
- **Mongo Express**: Gerenciador web do MongoDB
- **Apache NiFi**: Fluxos visuais de dados
- **Apache Airflow**: Orquestração de DAGs
- **Jupyter Notebook**: Análise exploratória
- **Apache Hadoop HDFS**: Sistema de arquivos distribuído
- **Apache Hue**: Interface visual para gerenciamento de HDFS e análise

---

## 📋 Estrutura do Projeto

```
pratica-ciencia-dados-2/
├── docker-compose.yml      # Configuração dos containers
├── README.md               # Este arquivo
├── .env                    # Variáveis de ambiente
│
├── hadoop-config/                # sistema de arquivos distribuido
│   ├── core-site.xml
│   ├── hdfs-site.xml
├── airflow/                # Serviço de orquestração
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── dags/
│   │   ├── etl_alunos.py
│   │   └── estatisticas_mongodb.py
│   ├── logs/
│   └── plugins/
│
├── jupyter/                # Ambiente de análise
│   ├── Dockerfile
│   └── notebooks/
│       └── data/
│
├── nifi/                   # Ferramenta de ETL visual
│   └── Dockerfile
│
├── postgres/               # Banco relacional
│   └── init/
│       └── 01-init.sql
│
├── hadoop-config/          # Configurações Hadoop/HDFS
│   ├── core-site.xml
│   └── hdfs-site.xml
│
└── data/                   # Dados do projeto
    ├── in/                 # Dados de entrada
    └── out/                # Dados de saída
```

---

## 📦 Requisitos

Antes de começar, instale:

- ✅ [Docker Desktop](https://www.docker.com/products/docker-desktop)
- ✅ Docker Compose (incluído no Docker Desktop)
- ✅ [Git](https://git-scm.com/)
- ⭐ [Power BI Desktop](https://powerbi.microsoft.com/) *(opcional, executa fora do Docker)*

### ⚙️ Configuração Windows

Para melhor desempenho no Windows:
- Ativar **Virtualização** na BIOS
- Usar **WSL2** (Windows Subsystem for Linux 2)
- Manter Docker Desktop **atualizado**

---

## 🚀 Como Iniciar
### 1️⃣ Build e Inicialização

```bash
# Na raiz do projeto, execute:
docker compose build
docker compose up -d
```

### 2️⃣ Verificar Status

```bash
# Listar containers
docker compose ps

# Ver logs em tempo real
docker compose logs -f

# Ver logs de um serviço específico
docker compose logs -f airflow
```

### 3️⃣ Parar o Ambiente

```bash
# Parar containers (mantém volumes)
docker compose down

# Parar e remover volumes
docker compose down -v
```

---

## 🔗 Serviços e Acessos

| Serviço | URL | Porta |
|---------|-----|-------|
| **Apache Airflow** | http://localhost:8080 | 8080 |
| **pgAdmin** | http://localhost:8085 | 8085 |
| **Mongo Express** | http://localhost:8082 | 8082 |
| **Apache NiFi** | https://localhost:8443 | 8443 |
| **Jupyter Notebook** | http://localhost:8888 | 8888 |
| **Apache Hue** | http://localhost:8889 | 8889 |
| **PostgreSQL** | localhost | 5432 |
| **MongoDB** | localhost | 27017 |
| **HDFS NameNode** | http://localhost:50070 | 50070 |

🔐 **Nota**: O NiFi usa HTTPS em versões atuais da imagem oficial.

---

## 🔑 Credenciais Padrão

### PostgreSQL
```
Banco: etl_lab
Usuário: etl_user
Senha: etl_pass
```

### pgAdmin
```
E-mail: admin@local.com
Senha: admin123
```

### MongoDB
```
Usuário: admin
Senha: admin123
```

### Apache Airflow
```
Usuário: admin
Senha: admin123
```

### Apache NiFi
```
Usuário: admin
Senha: Admin123456789
```

### Jupyter Notebook
```
Token: (definido em .env)
```

### Apache Hue
```
Usuário: admin
Senha: admin
```

---

## 💾 Bancos de Dados

### PostgreSQL

**Esquema**: `aula`

**Tabelas principais**:
- `aula.alunos_raw` - Dados brutos de entrada
- `aula.alunos_tratados` - Dados após limpeza
- `aula.alunos_invalidos` - Registros inválidos
- `aula.alunos_analytics` - Dados preparados para BI

**Funcionalidade**:
- Armazena dados estruturados
- Suporta consultas analíticas complexas
- Integra com Power BI

### MongoDB

**Coleções principais**:
- `executions` - Histórico de execuções de DAGs
- `statistics` - Estatísticas agregadas
- `logs` - Logs de processamento

**Funcionalidade**:
- Armazena dados não estruturados
- Ideal para documentos de auditoria
- Flexível para evolução de schema

---

## 🔄 Fluxo de Dados Típico

```
Dados Brutos (in/)
    ↓
[NiFi] → ETL Visual
    ↓
[Airflow] → Orquestração de tarefas
    ↓
PostgreSQL (tratados) + MongoDB (logs)
    ↓
[Jupyter] / [Power BI] → Análise e Visualização
    ↓
Saída (out/)
```

---

## 💡 Conceitos-Chave

### DAGs (Directed Acyclic Graphs)
Fluxos de trabalho definidos no Airflow que orquestram tarefas em sequência ou paralelo.

**Exemplos no projeto**:
- `etl_alunos` - Pipeline completo de limpeza de dados de alunos
- `estatisticas_mongodb` - Agregação de estatísticas

### ETL (Extract Transform Load)
- **Extract**: NiFi ingere dados de fontes externas
- **Transform**: Airflow e scripts Python limpam/transformam
- **Load**: Dados carregados em PostgreSQL/MongoDB

### Containerização
Cada serviço roda em seu próprio container, garantindo isolamento e reprodutibilidade.

---

## ❓ Troubleshooting

### Problema: Containers não iniciam
```bash
# Verifique se a porta está em uso
netstat -ano | findstr :8080

# Limpe volumes e tente novamente
docker compose down -v
docker compose up -d
```

### Problema: Airflow retorna erro de conexão
```bash
# Reinicie o scheduler
docker compose restart airflow-scheduler
```

### Problema: PostgreSQL não conecta
```bash
# Verifique logs
docker compose logs postgres

# Recrie o container
docker compose down
docker compose up -d postgres
```

### Problema: Jupyter retorna erro de token
```bash
# Veja os logs para obter o token
docker compose logs jupyter
```

---

## 🎓 Como Usar

### 1. Exploração com Jupyter
```bash
# Acesse http://localhost:8888
# Use o token dos logs do container
docker compose logs jupyter | grep token
```

### 2. ETL Visual com NiFi
```bash
# Acesse https://localhost:8443
# Crie fluxos visuais de dados
# Monitore a ingestão em tempo real
```

### 3. Orquestração com Airflow
```bash
# Acesse http://localhost:8080
# Ative e monitore DAGs
# Visualize timeline de execuções
```

### 4. Gerenciamento de HDFS com Hue
```bash
# Acesse http://localhost:8889
# Login: admin / admin
# Navegue por arquivos, crie diretórios e gerencie dados distribuídos
```

### 5. Análise em Power BI
```
# Conecte ao PostgreSQL
Host: localhost
Port: 5432
Database: etl_lab
User: etl_user
Password: etl_pass
```

---

## 📚 Recursos Úteis

- [Documentação Apache Airflow](https://airflow.apache.org/)
- [Documentação Apache NiFi](https://nifi.apache.org/)
- [Documentação PostgreSQL](https://www.postgresql.org/docs/)
- [Documentação MongoDB](https://docs.mongodb.com/)
- [Jupyter Documentation](https://jupyter.org/documentation)
- [Documentação Apache Hadoop HDFS](https://hadoop.apache.org/docs/)
- [Documentação Apache Hue](https://gethue.com/)

---

## ⚖️ Licença

Este projeto é fornecido para fins educacionais.

---

## 👥 Suporte

Para dúvidas ou problemas:
1. Verifique os logs: `docker compose logs -f`
2. Consulte a seção de Troubleshooting
3. Reinicie o ambiente: `docker compose restart`