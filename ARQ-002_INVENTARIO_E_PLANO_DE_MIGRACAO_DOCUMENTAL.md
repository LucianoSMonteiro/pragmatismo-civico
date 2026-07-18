---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.13.0
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
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# ARQ-002 — Inventário e Plano de Migração Documental

## Status

Rascunho para execução progressiva. Este documento registra o estado conhecido do acervo, a dívida documental, os reparos realizados e a sequência controlada de migração.

## 1. Objetivo

Transformar a arquitetura definida pelo `ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md` em um plano executável, sem mover arquivos precipitadamente, quebrar URLs ou atribuir metadados históricos sem evidência.

O documento possui duas funções:

1. inventariar e classificar o acervo público atual;
2. organizar a migração gradual para o PPC-META-001, o PPC-000A e a arquitetura documental.

## 2. Escopo e método do inventário

O inventário cobre os documentos expostos na navegação canônica do portal em `mkdocs.yml`, além dos principais arquivos conhecidos de configuração e publicação.

A navegação é utilizada como fonte da lista de documentos públicos. A classificação por camada segue o ARQ-001 e pode diferir da posição escolhida no menu quando a lógica de uso do portal justificar outra apresentação.

O recorte:

- representa o acervo público apresentado ao usuário;
- permite rastrear cada item por caminho conhecido;
- reduz o risco de declarar como completo um levantamento ainda não automatizado;
- cria uma linha de base verificável para expansões posteriores.

Arquivos fora da navegação, anexos, ativos, automações e registros históricos deverão ser incorporados em revisão posterior do inventário.

## 3. Resumo do acervo público

A navegação atual contém **38 documentos Markdown**.

| Camada | Quantidade | Situação geral |
|---|---:|---|
| Publicação e acesso | 2 | conteúdo sincronizado; metadados ainda pendentes |
| Princípios e fundamentos | 6 | todos os seis documentos migrados; Fase 4B concluída |
| Governança e arquitetura | 9 | todos os nove documentos conformes |
| Método | 10 | todos os dez documentos conformes e reciprocidade obrigatória verificada |
| Ferramentas | 11 | todas as onze ferramentas conformes |
| Aplicações e evidências | 0 | camada ainda sem estudo de caso publicado |
| **Total** | **38** | 36 documentos conformes e 2 ainda não migrados |

Arquivos conhecidos de suporte incluem `mkdocs.yml`, `requirements.txt`, `LICENSE`, ativos de estilo e automações em `.github/`. Eles são tratados como infraestrutura, não como documentos metodológicos.

## 4. Inventário por camada

### 4.1 Publicação e acesso

| Documento | Caminho | Função | Metadados | Prioridade |
|---|---|---|---|---|
| Página inicial | `README.md` | entrada pública e apresentação | conteúdo sincronizado; metadados a migrar | alta |
| Guia de início | `docs/COMECAR.md` | orientação de leitura e uso | a migrar | alta |

### 4.2 Princípios e fundamentos

| Documento | Identificador | Caminho | Versão | Metadados |
|---|---|---|---:|---|
| Carta de Princípios | `CARTA-DE-PRINCIPIOS` | `CARTA_DE_PRINCIPIOS.md` | 0.1.2 | presente |
| Especificação | `SPECIFICATION` | `SPECIFICATION.md` | 0.2.0 | presente |
| Framework de Referência | `FRAMEWORK-DE-REFERENCIA` | `FRAMEWORK_DE_REFERENCIA.md` | 0.2.0 | presente |
| Teoria do Pragmatismo Cívico | `TEORIA-DO-PRAGMATISMO-CIVICO` | `TEORIA_DO_PRAGMATISMO_CIVICO.md` | 0.1.0 | presente |
| Manifesto | `MANIFESTO` | `MANIFESTO.md` | 0.1.0 | presente |
| Glossário | `GLOSSARIO` | `GLOSSARIO.md` | 0.1.0 | presente |

A hierarquia declarada permanece: direitos e garantias democráticas → Carta → Especificação → Framework → método → ferramentas e aplicações.

### 4.3 Governança e arquitetura

| Documento | Identificador | Metadados |
|---|---|---|
| PPC-000 | `PPC-000` | presente |
| Modelo de governança | `GOV-001` | presente |
| PPC-META-001 | `PPC-META-001` | presente |
| PPC-000A | `PPC-000A` | presente |
| Arquitetura documental | `ARQ-001` | presente |
| Inventário e plano de migração | `ARQ-002` | presente |
| Guia de contribuição | `GOV-003` | presente |
| Código de conduta | `GOV-004` | presente |
| Roadmap | `GOV-002` | presente |

### 4.4 Método

| Documento | Identificador | Relação principal | Metadados |
|---|---|---|---|
| Ciclo do Pragmatismo Cívico | `CICLO-PC-001` | visão integrada | presente |
| PPC-001 | `PPC-001` | diagnóstico | presente |
| PPC-002 | `PPC-002` | alternativas | presente |
| PPC-003 | `PPC-003` | avaliação técnica | presente |
| PPC-004 | `PPC-004` | decisão | presente |
| Teoria da mudança | `MODELO-TDM-001` | ponte entre decisão e implementação | presente |
| PPC-005 | `PPC-005` | implementação | presente |
| PPC-006 | `PPC-006` | monitoramento | presente |
| PPC-007 | `PPC-007` | avaliação | presente |
| PPC-008 | `PPC-008` | aprendizagem | presente |

### 4.5 Ferramentas

| Documento | Identificador | Documento associado | Metadados |
|---|---|---|---|
| Ficha PPC-001 | `FICHA-PPC-001` | PPC-001 versão 0.1.1 | presente |
| Ficha PPC-002 | `FICHA-PPC-002` | PPC-002 versão 0.1.0 | presente; piloto preservado |
| Ficha PPC-003 | `FICHA-PPC-003` | PPC-003 versão 0.1.0 | presente; piloto preservado |
| Ficha PPC-004 | `FICHA-PPC-004` | PPC-004 versão 0.1.0 | presente |
| Ficha de teoria da mudança | `FICHA-TDM-001` | MODELO-TDM-001 versão 0.1.0 | presente |
| Ficha PPC-005 | `FICHA-PPC-005` | PPC-005 versão 0.1.0 | presente |
| Ficha PPC-006 | `FICHA-PPC-006` | PPC-006 versão 0.1.0 | presente |
| Ficha PPC-007 | `FICHA-PPC-007` | PPC-007 versão 0.1.0 | presente |
| Ficha PPC-008 | `FICHA-PPC-008` | PPC-008 versão 0.1.0 | presente |
| Matriz de avaliação | `MATRIZ-PPC-001` | PPC-002 e PPC-003, versões 0.1.0 | presente |
| Indicadores | `MODELO-INDICADORES-001` | PPC-001 0.1.1, MODELO-TDM-001, PPC-006 e PPC-007 0.1.0 | presente |

### 4.6 Aplicações e evidências

Nenhum estudo de caso, piloto ou relatório de aplicação está publicado na navegação canônica nesta versão.

## 5. Situação de metadados

### 5.1 Documentos conformes verificados

Possuem cabeçalho estruturado alinhado ao PPC-META-001:

- os seis documentos de princípios e fundamentos;
- os nove documentos de governança e arquitetura;
- os dez documentos da camada de método;
- as onze ferramentas da navegação canônica.

### 5.2 Documentos ainda não migrados

Restam apenas:

- `README.md`;
- `docs/COMECAR.md`.

A migração não deve presumir data histórica de criação, autoria individual, aprovação formal inexistente, versão anterior não registrada ou estabilidade não demonstrada. Quando uma informação não puder ser comprovada, deve ser registrada como `null`, lista vazia ou pendência documental.

## 6. Dívida documental

| ID | Problema | Risco | Estado | Tratamento |
|---|---|---|---|---|
| DD-001 | 2 dos 38 documentos navegáveis ainda não possuem cabeçalho PPC-META-001 | versões e responsabilidades ambíguas | aberta | executar Fase 4C |
| DD-002 | reciprocidade das dependências obrigatórias do ciclo metodológico | incoerência entre padrões | resolvida | auditoria concluída no lote 2C; futura automação deve impedir regressões |
| DD-003 | matriz e indicadores não registravam versões associadas | aplicações irreplicáveis | resolvida | corrigida no lote 3C |
| DD-004 | vínculos genéricos e heterogêneos nas ferramentas | grafo documental inconsistente | resolvida | revisão conjunta concluída no lote 3C |
| DD-005 | acervo predominantemente na raiz | manutenção futura pode ficar difícil | aberta, baixa | não mover arquivos antes de medir benefício |
| DD-006 | ausência de catálogo documental gerado | localização depende do `mkdocs.yml` | aberta | criar catálogo após migração mínima |
| DD-007 | ausência de validação automática de metadados e links | erros podem chegar ao portal | aberta | criar automação após estabilizar esquema |
| DD-008 | camada de aplicações sem estudos de caso publicados | método sem validação empírica documentada | aberta, alta | preparar primeiro caso após ferramentas mínimas |
| DD-009 | datas e históricos anteriores não estão uniformemente registrados | história retrospectiva fictícia | controlada | preservar incerteza e usar commits como evidência |
| DD-010 | execuções de push do workflow não são expostas pelo conector utilizado | publicação não confirmada pela auditoria automatizada | aberta | verificar diretamente no GitHub Actions |
| DD-011 | arquitetura histórica do Framework tratava documentos publicados como futuros | descrição incompatível com o acervo vigente | resolvida | Framework 0.2.0 alinhado às seis camadas do ARQ-001 |
| DD-012 | Especificação tratava documentos existentes como futuras derivações e citava classes não formalizadas | ambiguidade sobre o acervo oficial | resolvida | Especificação 0.2.0 distingue documentos vigentes de propostas futuras |
| DD-013 | ciclo conceitual da Especificação podia ser confundido com o ciclo operacional PPC | aplicação inconsistente | resolvida | Especificação 0.2.0 esclarece a relação entre os dois níveis |
| DD-014 | sustentabilidade institucional aparecia na Carta e no Framework, mas não integralmente na Especificação | incoerência normativa | resolvida | Especificação 0.2.0 alinhada à sustentabilidade integral |

## 7. Correções e avanços resultantes das revisões

As revisões do repositório produziram:

- sincronização do README com o ciclo completo e a governança documental;
- alinhamento da arquitetura pública às seis camadas do ARQ-001;
- conclusão das Fases 1, 2 e 3;
- normalização das onze ferramentas e de seus vínculos;
- migração dos seis documentos de princípios e fundamentos;
- identificação canônica da Teoria, Especificação, Manifesto e Glossário;
- normalização das saídas documentais da Carta, da Especificação e do Framework;
- atualização do Framework para a arquitetura vigente;
- esclarecimento, na Especificação, da distinção entre movimentos conceituais e ciclo operacional PPC;
- alinhamento da sustentabilidade institucional;
- preservação dos princípios, hipóteses teóricas, definições e compromissos do Manifesto.

A configuração do workflow está presente e coerente com GitHub Pages, mas sua execução mais recente deve ser confirmada diretamente no histórico do GitHub Actions, pois o conector utilizado não retorna eventos de push desse workflow.

## 8. Princípios da migração

A migração deve:

1. não mover arquivos prematuramente;
2. não alterar conteúdo metodológico ou normativo apenas para adicionar metadados;
3. separar migração documental de reparos substantivos e versionar ambos;
4. não inventar datas, autores ou aprovações;
5. preservar nomes e URLs consolidados;
6. avançar em lotes pequenos e revisáveis;
7. atualizar versões de acordo com a mudança real;
8. declarar dependências com base no conteúdo;
9. verificar links, navegação e publicação após cada lote;
10. registrar dívida não resolvida.

## 9. Plano de migração progressiva

### Fase 0 — Linha de base

**Estado:** concluída e corrigida.

### Fase 1 — Núcleo de governança

**Estado:** concluída — 5 de 5 documentos migrados.

### Fase 2 — Núcleo metodológico

**Estado:** concluída — lotes 2A, 2B e 2C finalizados; 10 de 10 documentos migrados.

### Fase 3 — Ferramentas

**Estado:** concluída — lotes 3A, 3B e 3C finalizados; 11 de 11 ferramentas conformes.

### Fase 4 — Fundamentos e entrada

**Estado:** em andamento — lotes 4A e 4B concluídos; 6 de 8 documentos migrados.

Lotes:

- **4A — concluído:** Framework de Referência e Carta de Princípios;
- **4B — concluído:** Teoria do Pragmatismo Cívico, Especificação, Manifesto e Glossário;
- **4C — próximo:** README e guia de início.

O lote 4B foi seguido por uma revisão separada e versionada que reparou a arquitetura histórica do Framework, a distinção entre ciclo conceitual e operacional e a reciprocidade dos vínculos de autoridade.

### Fase 5 — Catálogo e navegação

Entregas: catálogo público, indicação de versão e estado, agrupamento por camada, mapa de dependências, revisão da ordem de leitura e identificação de documentos técnicos fora da navegação principal.

### Fase 6 — Validação automática

Entregas: esquema YAML, identificadores duplicados, formato de versão e estado, referências quebradas, build estrito e relatório de dívida remanescente.

### Fase 7 — Estrutura física

Somente após as fases anteriores será decidido se arquivos devem sair da raiz. A opção legítima de manter a estrutura atual permanece aberta.

## 10. Checklist de cada lote

Antes do commit:

- [ ] escopo definido;
- [ ] arquivos lidos integralmente;
- [ ] metadados baseados em evidência;
- [ ] versão e estado coerentes;
- [ ] dependências verificadas;
- [ ] histórico atualizado;
- [ ] links preservados;
- [ ] conteúdo substantivo preservado ou alteração separadamente justificada.

Após o commit:

- [ ] arquivos relidos na branch padrão;
- [ ] navegação verificada;
- [ ] roadmap atualizado;
- [ ] build ou status consultado;
- [ ] SHA registrado;
- [ ] dívida residual anotada.

## 11. Critérios para concluir a migração mínima

A migração mínima estará concluída quando:

- todos os 38 documentos navegáveis possuírem identificação, versão, estado e responsáveis;
- PPCs e ferramentas declararem relações verificáveis;
- documentos fundadores possuírem fonte canônica e histórico preservado;
- o portal permitir localizar versão e estado;
- nenhuma movimentação tiver produzido links quebrados conhecidos;
- o inventário puder ser atualizado por processo repetível;
- novos documentos nascerem conformes;
- a dívida restante estiver registrada e priorizada.

## 12. Decisões desta versão

Esta versão decide que:

- o inventário utiliza a navegação canônica como fonte da lista de documentos;
- a classificação por camada segue o ARQ-001;
- nenhum arquivo será movido durante os primeiros lotes;
- documentos sem evidência histórica não receberão datas ou aprovações retroativas;
- as Fases 1, 2 e 3 estão concluídas;
- os lotes 4A e 4B estão concluídos;
- reparos normativos relevantes devem possuir versão e histórico próprios;
- a próxima execução será a Fase 4C;
- a estrutura física será decidida somente depois de metadados, catálogo e validação.

## 13. Próxima ação

Executar a **Fase 4C — Publicação e acesso**, migrando `README.md` e `docs/COMECAR.md`, revisando a coerência da orientação inicial e concluindo a cobertura de metadados dos 38 documentos navegáveis.

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
