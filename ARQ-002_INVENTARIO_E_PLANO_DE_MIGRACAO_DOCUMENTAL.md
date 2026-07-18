---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.14.0
status: rascunho
tipo: arquitetura
idioma: pt-BR
data_criacao: 2026-07-17
data_versao: 2026-07-18
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - ARQ-001
  - PPC-000
  - PPC-000A
  - PPC-META-001
produz_entrada_para:
  - CATALOGO-DOCUMENTAL
  - VALIDACAO-AUTOMATICA-DE-METADADOS
relaciona_se_com:
  - GOV-002
  - MKDOCS
  - PORTAL-INICIO
  - GUIA-COMECAR
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# ARQ-002 — Inventário e Plano de Migração Documental

## Status

Rascunho para execução progressiva. A cobertura mínima de identificação, versão, estado e responsabilidade foi concluída para os 38 documentos da navegação canônica. Este documento continua ativo para registrar dívida, catálogo, validação e decisões sobre a estrutura futura.

## 1. Objetivo

Transformar a arquitetura definida pelo `ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md` em um processo executável, sem mover arquivos precipitadamente, quebrar URLs ou atribuir metadados históricos sem evidência.

O documento possui duas funções:

1. inventariar e classificar o acervo público atual;
2. organizar a evolução de metadados, catálogo, validação e estrutura documental.

## 2. Escopo e método do inventário

O inventário utiliza a navegação canônica de `mkdocs.yml` como fonte dos documentos públicos e a classificação do ARQ-001 como referência das camadas.

Esse recorte:

- representa o acervo apresentado ao usuário;
- permite rastrear cada item por caminho conhecido;
- evita declarar como completo um levantamento mais amplo que ainda não foi automatizado;
- cria uma linha de base verificável para catálogo e validação.

Arquivos de infraestrutura, anexos, ativos, automações e registros históricos fora da navegação deverão ser incorporados em inventário técnico posterior.

## 3. Resumo do acervo público

A navegação contém **38 documentos Markdown**.

| Camada | Quantidade | Situação geral |
|---|---:|---|
| Publicação e acesso | 2 | ambos identificados e versionados; Fase 4C concluída |
| Princípios e fundamentos | 6 | todos conformes |
| Governança e arquitetura | 9 | todos conformes |
| Método | 10 | todos conformes; reciprocidade obrigatória verificada |
| Ferramentas | 11 | todas conformes e vinculadas aos padrões associados |
| Aplicações e evidências | 0 | ainda não há estudo de caso oficial publicado |
| **Total** | **38** | **38 documentos com identificação e versionamento** |

Trinta e sete documentos utilizam cabeçalho YAML no início do arquivo. O `README.md` utiliza representação estruturada equivalente em comentário HTML e seção humana colapsável, para preservar sua função de página inicial no GitHub e no portal.

Arquivos conhecidos de suporte incluem `mkdocs.yml`, `requirements.txt`, `LICENSE`, ativos de estilo e automações em `.github/`. Eles são tratados como infraestrutura, não como documentos metodológicos.

## 4. Inventário por camada

### 4.1 Publicação e acesso

| Documento | Identificador | Caminho | Versão | Representação |
|---|---|---|---:|---|
| Página inicial | `PORTAL-INICIO` | `README.md` | 0.2.1 | bloco estruturado equivalente e seção colapsável |
| Guia de início | `GUIA-COMECAR` | `docs/COMECAR.md` | 0.2.0 | cabeçalho YAML |

O guia de início cobre o ciclo completo, diferencia o PPC-000 do PPC-000A e do PPC-META-001 e declara que o framework ainda não possui validação empírica suficiente para estabilidade.

### 4.2 Princípios e fundamentos

| Documento | Identificador | Versão |
|---|---|---:|
| Carta de Princípios | `CARTA-DE-PRINCIPIOS` | 0.1.2 |
| Especificação | `SPECIFICATION` | 0.2.0 |
| Framework de Referência | `FRAMEWORK-DE-REFERENCIA` | 0.2.0 |
| Teoria do Pragmatismo Cívico | `TEORIA-DO-PRAGMATISMO-CIVICO` | 0.1.0 |
| Manifesto | `MANIFESTO` | 0.1.0 |
| Glossário | `GLOSSARIO` | 0.1.0 |

A hierarquia declarada permanece: direitos e garantias democráticas → Carta → Especificação → Framework → método → ferramentas e aplicações.

### 4.3 Governança e arquitetura

| Documento | Identificador |
|---|---|
| PPC-000 | `PPC-000` |
| Modelo de governança | `GOV-001` |
| Roadmap | `GOV-002` |
| Guia de contribuição | `GOV-003` |
| Código de conduta | `GOV-004` |
| PPC-META-001 | `PPC-META-001` |
| PPC-000A | `PPC-000A` |
| Arquitetura documental | `ARQ-001` |
| Inventário e plano de migração | `ARQ-002` |

### 4.4 Método

| Documento | Identificador | Relação principal |
|---|---|---|
| Ciclo do Pragmatismo Cívico | `CICLO-PC-001` | visão integrada |
| PPC-001 | `PPC-001` | diagnóstico |
| PPC-002 | `PPC-002` | alternativas |
| PPC-003 | `PPC-003` | avaliação técnica |
| PPC-004 | `PPC-004` | decisão |
| Teoria da Mudança | `MODELO-TDM-001` | ponte causal entre decisão e implementação |
| PPC-005 | `PPC-005` | implementação |
| PPC-006 | `PPC-006` | monitoramento |
| PPC-007 | `PPC-007` | avaliação |
| PPC-008 | `PPC-008` | aprendizagem |

### 4.5 Ferramentas

| Documento | Identificador | Documento associado |
|---|---|---|
| Ficha PPC-001 | `FICHA-PPC-001` | PPC-001 0.1.1 |
| Ficha PPC-002 | `FICHA-PPC-002` | PPC-002 0.1.0; estado piloto preservado |
| Ficha PPC-003 | `FICHA-PPC-003` | PPC-003 0.1.0; estado piloto preservado |
| Ficha PPC-004 | `FICHA-PPC-004` | PPC-004 0.1.0 |
| Ficha de Teoria da Mudança | `FICHA-TDM-001` | MODELO-TDM-001 0.1.0 |
| Ficha PPC-005 | `FICHA-PPC-005` | PPC-005 0.1.0 |
| Ficha PPC-006 | `FICHA-PPC-006` | PPC-006 0.1.0 |
| Ficha PPC-007 | `FICHA-PPC-007` | PPC-007 0.1.0 |
| Ficha PPC-008 | `FICHA-PPC-008` | PPC-008 0.1.0 |
| Matriz de avaliação | `MATRIZ-PPC-001` | PPC-002 e PPC-003 0.1.0 |
| Indicadores | `MODELO-INDICADORES-001` | PPC-001 0.1.1, MODELO-TDM-001, PPC-006 e PPC-007 0.1.0 |

### 4.6 Aplicações e evidências

Nenhum estudo de caso, piloto ou relatório de aplicação está publicado na navegação canônica nesta versão.

## 5. Situação de metadados

### 5.1 Cobertura concluída

Todos os 38 documentos navegáveis possuem:

- identificador estável;
- versão semântica;
- estado canônico;
- idioma;
- responsáveis;
- relações documentais aplicáveis;
- compatibilidade;
- histórico de alterações.

O README constitui uma exceção de representação, não de conteúdo: os mesmos campos estão disponíveis em formato estruturado, sem deslocar a apresentação pública da página.

### 5.2 Limite da conclusão

A conclusão da cobertura não significa que o programa documental inteiro esteja encerrado. Ainda faltam:

- catálogo gerado ou mantido por processo repetível;
- validação automática de identificadores, versões, estados, relações e links;
- confirmação sistemática do build e da publicação;
- inventário técnico de arquivos fora da navegação;
- decisão sobre eventual reorganização física do repositório.

## 6. Dívida documental

| ID | Problema | Risco | Estado | Tratamento |
|---|---|---|---|---|
| DD-001 | documentos navegáveis sem metadados | versões e responsabilidades ambíguas | resolvida | Fase 4C concluiu 38 de 38 documentos |
| DD-002 | reciprocidade das dependências obrigatórias do ciclo | incoerência entre padrões | resolvida | auditoria concluída no lote 2C |
| DD-003 | matriz e indicadores sem versões associadas | aplicações irreplicáveis | resolvida | corrigida no lote 3C |
| DD-004 | vínculos genéricos nas ferramentas | grafo inconsistente | resolvida | revisão conjunta concluída no lote 3C |
| DD-005 | acervo predominantemente na raiz | manutenção futura pode ficar difícil | aberta, baixa | não mover arquivos antes de medir benefício |
| DD-006 | ausência de catálogo documental gerado | localização depende de navegação manual | aberta | executar Fase 5 |
| DD-007 | ausência de validação automática de metadados e links | regressões podem chegar ao portal | aberta | executar Fase 6 |
| DD-008 | camada de aplicações sem estudos de caso | método sem validação empírica documentada | aberta, alta | preparar primeiro caso demonstrativo |
| DD-009 | datas e históricos anteriores incompletos | risco de história retrospectiva fictícia | controlada | preservar `null` e usar commits como evidência |
| DD-010 | execuções de push não aparecem no conector utilizado | publicação não confirmada pela auditoria atual | aberta | verificar diretamente no GitHub Actions |
| DD-011 | arquitetura histórica do Framework desatualizada | descrição incompatível com o acervo | resolvida | Framework 0.2.0 alinhado ao ARQ-001 |
| DD-012 | Especificação tratava documentos vigentes como futuros | ambiguidade sobre o acervo oficial | resolvida | Especificação 0.2.0 atualizada |
| DD-013 | ciclo conceitual confundido com ciclo PPC | aplicação inconsistente | resolvida | distinção registrada na Especificação 0.2.0 |
| DD-014 | sustentabilidade institucional ausente da Especificação | incoerência normativa | resolvida | alinhamento realizado na Especificação 0.2.0 |
| DD-015 | README não pode usar front matter comum sem risco para a página inicial | apresentação ou automação podem ser prejudicadas | controlada | representação estruturada equivalente e visível em seção colapsável; validador deverá reconhecer a exceção |
| DD-016 | guia de início cobria apenas o começo do método | aplicação parcial do ciclo | resolvida | GUIA-COMECAR 0.2.0 cobre PPC-001 a PPC-008 e Teoria da Mudança |
| DD-017 | guia atribuía ciclo de vida e versionamento ao PPC-000 | orientação de governança imprecisa | resolvida | funções separadas entre PPC-000, PPC-000A e PPC-META-001 |

## 7. Correções e avanços acumulados

As revisões produziram:

- cobertura de metadados dos 38 documentos navegáveis;
- alinhamento da arquitetura pública às seis camadas do ARQ-001;
- normalização do ciclo metodológico e das onze ferramentas;
- migração dos seis documentos fundadores;
- reparo da arquitetura histórica do Framework;
- distinção entre ciclo conceitual e ciclo operacional na Especificação;
- alinhamento da sustentabilidade institucional;
- guia de início completo e coerente com a governança vigente;
- preservação da apresentação pública do README com metadados verificáveis.

A configuração do workflow permanece coerente com GitHub Pages e `mkdocs build --strict`, mas a execução mais recente deve ser confirmada diretamente no histórico do GitHub Actions, pois o conector utilizado não retorna os eventos de push desse workflow.

## 8. Princípios da evolução documental

A evolução deve:

1. não mover arquivos sem benefício demonstrado;
2. separar migração documental de reparos substantivos;
3. não inventar datas, autores ou aprovações;
4. preservar nomes e URLs consolidados;
5. avançar em lotes pequenos e revisáveis;
6. atualizar versões de acordo com a mudança real;
7. declarar relações com base no conteúdo;
8. verificar links, navegação e publicação;
9. registrar exceções e dívida residual;
10. automatizar apenas regras suficientemente estabilizadas.

## 9. Plano progressivo

### Fase 0 — Linha de base

**Estado:** concluída e corrigida.

### Fase 1 — Núcleo de governança

**Estado:** concluída — 5 de 5 documentos migrados.

### Fase 2 — Núcleo metodológico

**Estado:** concluída — 10 de 10 documentos migrados e reciprocidade revisada.

### Fase 3 — Ferramentas

**Estado:** concluída — 11 de 11 ferramentas conformes.

### Fase 4 — Fundamentos e entrada

**Estado:** concluída — 8 de 8 documentos migrados.

Lotes:

- **4A:** Framework de Referência e Carta de Princípios;
- **4B:** Teoria do Pragmatismo Cívico, Especificação, Manifesto e Glossário;
- **4C:** README e guia de início, com reparo das rotas de aplicação e da governança dos padrões.

### Fase 5 — Catálogo e navegação

**Estado:** próxima.

Entregas:

- catálogo público dos 38 documentos;
- indicação de identificador, versão e estado;
- agrupamento por camada;
- mapa de dependências e relações;
- revisão da ordem de leitura;
- identificação dos documentos técnicos fora da navegação principal.

### Fase 6 — Validação automática

Entregas:

- esquema de metadados;
- detecção de identificadores duplicados;
- validação de versão, estado e compatibilidade;
- verificação de referências e links;
- suporte à representação equivalente do README;
- build estrito;
- relatório de dívida remanescente.

### Fase 7 — Estrutura física

Somente após catálogo e validação será decidido se arquivos devem sair da raiz. A opção de manter a estrutura atual permanece legítima.

## 10. Checklist de cada lote

Antes do commit:

- [ ] escopo definido;
- [ ] arquivos lidos integralmente;
- [ ] metadados baseados em evidência;
- [ ] versão e estado coerentes;
- [ ] dependências verificadas;
- [ ] histórico atualizado;
- [ ] links preservados;
- [ ] conteúdo substantivo preservado ou alteração justificada separadamente.

Após o commit:

- [ ] arquivos relidos na branch padrão;
- [ ] navegação verificada;
- [ ] roadmap atualizado;
- [ ] build ou status consultado;
- [ ] SHA registrado;
- [ ] dívida residual anotada.

## 11. Critérios da migração mínima

A migração mínima foi concluída porque:

- os 38 documentos possuem identificação, versão, estado e responsáveis;
- PPCs e ferramentas declaram relações verificáveis;
- documentos fundadores possuem fonte canônica e histórico;
- nenhum arquivo foi movido ou teve seu caminho público alterado;
- a dívida restante está registrada e priorizada.

Catálogo, automação, estudos de caso e estrutura física permanecem etapas posteriores e não devem ser confundidos com a cobertura mínima de metadados.

## 12. Decisões desta versão

Esta versão decide que:

- a Fase 4 está concluída;
- o README é conforme por representação estruturada equivalente;
- o guia de início passa a cobrir o ciclo completo;
- nenhum arquivo será movido durante a criação do catálogo;
- a próxima execução será a Fase 5;
- a validação automática deverá reconhecer a exceção documentada do README.

## 13. Próxima ação

Executar a **Fase 5 — Catálogo e navegação**, criando um catálogo documental público dos 38 documentos, com identificador, versão, estado, camada e relações principais, sem alterar os caminhos vigentes.

## 14. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Inventário inicial, dívida documental e plano progressivo de migração | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-17 | compatível | Atualização do inventário e registro da migração do PPC-000 e do Modelo de Governança | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-17 | compatível | Correção das camadas, reconhecimento de metadados legados e revisão do README e da navegação | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-17 | compatível | Conclusão da Fase 1 | Projeto Pragmatismo Cívico |
| 0.5.0 | 2026-07-17 | compatível | Correções de identificadores e normalização da Ficha PPC-003 | Projeto Pragmatismo Cívico |
| 0.6.0 | 2026-07-17 | compatível | Conclusão da Fase 2A | Projeto Pragmatismo Cívico |
| 0.7.0 | 2026-07-17 | compatível | Conclusão da Fase 2B | Projeto Pragmatismo Cívico |
| 0.8.0 | 2026-07-17 | compatível | Conclusão da Fase 2C | Projeto Pragmatismo Cívico |
| 0.9.0 | 2026-07-17 | compatível | Conclusão do lote 3A | Projeto Pragmatismo Cívico |
| 0.10.0 | 2026-07-18 | compatível | Conclusão do lote 3B e consolidação editorial do inventário | Projeto Pragmatismo Cívico |
| 0.11.0 | 2026-07-18 | compatível | Conclusão do lote 3C, identificação da matriz e dos indicadores e encerramento da Fase 3 | Projeto Pragmatismo Cívico |
| 0.12.0 | 2026-07-18 | compatível | Conclusão do lote 4A, migração do Framework e da Carta e registro da dívida editorial remanescente | Projeto Pragmatismo Cívico |
| 0.13.0 | 2026-07-18 | compatível | Conclusão do lote 4B, migração dos quatro documentos fundadores restantes e registro dos reparos normativos associados | Projeto Pragmatismo Cívico |
| 0.14.0 | 2026-07-18 | compatível | Conclusão do lote 4C, cobertura dos 38 documentos, reparo do guia de início e promoção do catálogo documental | Projeto Pragmatismo Cívico |
