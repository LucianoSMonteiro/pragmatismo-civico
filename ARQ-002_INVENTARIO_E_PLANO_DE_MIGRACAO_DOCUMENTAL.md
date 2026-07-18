---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.10.0
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

Rascunho para execução progressiva. Este documento registra o estado conhecido do acervo, a dívida documental e a sequência controlada de migração.

## 1. Objetivo

Transformar a arquitetura definida pelo `ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md` em um plano executável, sem mover arquivos precipitadamente, quebrar URLs ou atribuir metadados históricos sem evidência.

O documento possui duas funções:

1. inventariar e classificar o acervo público atual;
2. organizar a migração gradual para o PPC-META-001, o PPC-000A e a arquitetura documental.

## 2. Escopo e método do inventário

O inventário cobre os documentos expostos na navegação canônica do portal em `mkdocs.yml`, além dos principais arquivos conhecidos de configuração e publicação.

A navegação é utilizada como fonte da lista de documentos públicos. A classificação por camada segue o ARQ-001 e pode diferir da posição escolhida no menu quando a lógica de uso do portal justificar outra apresentação.

Esse recorte:

- representa o acervo público apresentado ao usuário;
- permite rastrear cada item por caminho conhecido;
- reduz o risco de declarar como completo um levantamento ainda não automatizado;
- cria uma linha de base verificável para expansões posteriores.

Arquivos fora da navegação, anexos, ativos, automações e registros históricos deverão ser incorporados em revisão posterior do inventário.

## 3. Resumo do acervo público

A navegação atual contém **38 documentos Markdown**.

| Camada | Quantidade | Situação geral |
|---|---:|---|
| Publicação e acesso | 2 | README sincronizado editorialmente; metadados ainda pendentes |
| Princípios e fundamentos | 6 | núcleo consolidado; migração deve ser cautelosa |
| Governança e arquitetura | 9 | todos os nove documentos possuem cabeçalho PPC-META-001 |
| Método | 10 | todos os dez documentos migrados e reciprocidade obrigatória verificada |
| Ferramentas | 11 | nove ferramentas conformes; lotes 3A e 3B concluídos; dois instrumentos pendentes |
| Aplicações e evidências | 0 | camada ainda sem estudo de caso publicado |
| **Total** | **38** | 28 documentos conformes e 10 ainda não migrados |

Arquivos conhecidos de suporte incluem `mkdocs.yml`, `requirements.txt`, `LICENSE`, ativos de estilo e automações em `.github/`. Eles são tratados como infraestrutura, não como documentos metodológicos.

## 4. Inventário por camada

### 4.1 Publicação e acesso

| Documento | Caminho | Função | Metadados | Prioridade |
|---|---|---|---|---|
| Página inicial | `README.md` | entrada pública e apresentação | conteúdo sincronizado; metadados a migrar | média |
| Guia de início | `docs/COMECAR.md` | orientação de leitura e uso | a migrar | alta |

### 4.2 Princípios e fundamentos

| Documento | Caminho | Função | Metadados | Prioridade |
|---|---|---|---|---|
| Framework de referência | `FRAMEWORK_DE_REFERENCIA.md` | fonte conceitual superior | a migrar | crítica |
| Teoria do Pragmatismo Cívico | `TEORIA_DO_PRAGMATISMO_CIVICO.md` | fundamento teórico | a migrar | alta |
| Manifesto | `MANIFESTO.md` | declaração identitária | a migrar | média |
| Carta de princípios | `CARTA_DE_PRINCIPIOS.md` | princípios normativos | a migrar | crítica |
| Especificação | `SPECIFICATION.md` | especificação fundadora | a migrar | alta |
| Glossário | `GLOSSARIO.md` | vocabulário oficial | a migrar | alta |

### 4.3 Governança e arquitetura

| Documento | Caminho | Função | Metadados | Prioridade |
|---|---|---|---|---|
| PPC-000 | `PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md` | metanorma do ecossistema PPC | presente | concluída nesta dimensão |
| Modelo de governança | `MODELO_DE_GOVERNANCA.md` | governança institucional | presente | concluída nesta dimensão |
| PPC-META-001 | `PPC-META-001_METADADOS_E_VERSIONAMENTO.md` | metadados e versões | presente | concluída nesta dimensão |
| PPC-000A | `PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md` | ciclo de vida | presente | concluída nesta dimensão |
| Arquitetura documental | `ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md` | arquitetura do acervo | presente | concluída nesta dimensão |
| Inventário e plano de migração | `ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md` | linha de base e execução da migração | presente | concluída nesta dimensão |
| Guia de contribuição | `CONTRIBUTING.md` | contribuições | presente | concluída nesta dimensão |
| Código de conduta | `CODE_OF_CONDUCT.md` | conduta comunitária | presente | concluída nesta dimensão |
| Roadmap | `ROADMAP.md` | planejamento | presente | concluída nesta dimensão |

### 4.4 Método

| Documento | Caminho | Relação principal | Metadados | Prioridade |
|---|---|---|---|---|
| Ciclo do Pragmatismo Cívico | `CICLO_DO_PRAGMATISMO_CIVICO.md` | visão integrada | presente | concluída nesta dimensão |
| PPC-001 | `PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md` | diagnóstico | presente | concluída nesta dimensão |
| PPC-002 | `PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md` | alternativas | presente | concluída nesta dimensão |
| PPC-003 | `PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md` | avaliação técnica | presente | concluída nesta dimensão |
| PPC-004 | `PPC-004_DECISAO_E_JUSTIFICATIVA.md` | decisão | presente | concluída nesta dimensão |
| Teoria da mudança | `MODELO_DE_TEORIA_DA_MUDANCA.md` | ponte entre decisão e implementação | presente | concluída nesta dimensão |
| PPC-005 | `PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md` | implementação | presente | concluída nesta dimensão |
| PPC-006 | `PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md` | monitoramento | presente | concluída nesta dimensão |
| PPC-007 | `PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md` | avaliação | presente | concluída nesta dimensão |
| PPC-008 | `PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md` | aprendizagem | presente | concluída nesta dimensão |

### 4.5 Ferramentas

| Documento | Caminho | Documento associado | Metadados | Prioridade |
|---|---|---|---|---|
| Ficha PPC-001 | `FICHA_PPC-001_DIAGNOSTICO_DE_PROBLEMA_PUBLICO.md` | PPC-001 versão 0.1.1 | presente | concluída nesta dimensão |
| Ficha PPC-002 | `FICHA_PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md` | PPC-002 versão 0.1.0 | presente; estado piloto preservado | concluída nesta dimensão |
| Ficha PPC-003 | `FICHA_PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md` | PPC-003 versão 0.1.0 | presente; estado piloto preservado | concluída nesta dimensão |
| Ficha PPC-004 | `FICHA_PPC-004_DECISAO_E_JUSTIFICATIVA.md` | PPC-004 versão 0.1.0 | presente | concluída nesta dimensão |
| Ficha de teoria da mudança | `FICHA_TEORIA_DA_MUDANCA.md` | MODELO-TDM-001 versão 0.1.0 | presente | concluída nesta dimensão |
| Ficha PPC-005 | `FICHA_PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md` | PPC-005 versão 0.1.0 | presente | concluída nesta dimensão |
| Ficha PPC-006 | `FICHA_PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md` | PPC-006 versão 0.1.0 | presente | concluída nesta dimensão |
| Ficha PPC-007 | `FICHA_PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md` | PPC-007 versão 0.1.0 | presente | concluída nesta dimensão |
| Ficha PPC-008 | `FICHA_PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md` | PPC-008 versão 0.1.0 | presente | concluída nesta dimensão |
| Matriz de avaliação | `MATRIZ_DE_AVALIACAO_DE_POLITICAS_PUBLICAS.md` | PPC-002 e PPC-003 | a migrar | alta |
| Indicadores | `INDICADORES.md` | ciclo metodológico, PPC-006 e PPC-007 | a migrar | alta |

### 4.6 Aplicações e evidências

Nenhum estudo de caso, piloto ou relatório de aplicação está publicado na navegação canônica nesta versão.

## 5. Situação de metadados

### 5.1 Documentos conformes verificados

Possuem cabeçalho estruturado alinhado ao PPC-META-001:

- `PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md`;
- `MODELO_DE_GOVERNANCA.md`;
- `PPC-META-001_METADADOS_E_VERSIONAMENTO.md`;
- `PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md`;
- `ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md`;
- `ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md`;
- `ROADMAP.md`;
- `CONTRIBUTING.md`;
- `CODE_OF_CONDUCT.md`;
- `CICLO_DO_PRAGMATISMO_CIVICO.md`;
- `PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md`;
- `PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md`;
- `PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md`;
- `PPC-004_DECISAO_E_JUSTIFICATIVA.md`;
- `MODELO_DE_TEORIA_DA_MUDANCA.md`;
- `PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md`;
- `PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md`;
- `PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md`;
- `PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md`;
- `FICHA_PPC-001_DIAGNOSTICO_DE_PROBLEMA_PUBLICO.md`;
- `FICHA_PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md`;
- `FICHA_PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md`;
- `FICHA_PPC-004_DECISAO_E_JUSTIFICATIVA.md`;
- `FICHA_TEORIA_DA_MUDANCA.md`;
- `FICHA_PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md`;
- `FICHA_PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md`;
- `FICHA_PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md`;
- `FICHA_PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md`.

### 5.2 Documentos ainda não migrados

Os dez documentos restantes são:

- `README.md`;
- `docs/COMECAR.md`;
- `FRAMEWORK_DE_REFERENCIA.md`;
- `TEORIA_DO_PRAGMATISMO_CIVICO.md`;
- `MANIFESTO.md`;
- `CARTA_DE_PRINCIPIOS.md`;
- `SPECIFICATION.md`;
- `GLOSSARIO.md`;
- `MATRIZ_DE_AVALIACAO_DE_POLITICAS_PUBLICAS.md`;
- `INDICADORES.md`.

A migração não deve presumir data histórica de criação, autoria individual, aprovação formal inexistente, versão anterior não registrada ou estabilidade não demonstrada. Quando uma informação não puder ser comprovada, deve ser registrada como `null`, lista vazia ou pendência documental.

## 6. Dívida documental

| ID | Problema | Risco | Prioridade | Tratamento proposto |
|---|---|---|---|---|
| DD-001 | 10 dos 38 documentos navegáveis ainda não possuem cabeçalho PPC-META-001 | versões e responsabilidades ambíguas | alta | concluir fases 3C e 4 |
| DD-002 | reciprocidade das dependências obrigatórias do ciclo metodológico precisava ser verificada | incoerência entre padrões | resolvida | auditoria concluída no lote 2C; futura automação deve impedir regressões |
| DD-003 | matriz e indicadores ainda não registram versões dos padrões associados | aplicações podem ficar irreplicáveis | alta | executar lote 3C |
| DD-004 | vínculos das ferramentas ainda precisam de revisão final conjunta | catálogo e automação podem refletir relações heterogêneas | média | revisar no lote 3C |
| DD-005 | acervo predominantemente na raiz | manutenção futura pode ficar difícil | baixa no estágio atual | não mover arquivos antes de medir benefício |
| DD-006 | ausência de catálogo documental gerado | localização depende do `mkdocs.yml` | média | criar catálogo após migração mínima |
| DD-007 | ausência de validação automática de metadados e links | erros podem chegar ao portal | média | criar automação após estabilizar esquema |
| DD-008 | camada de aplicações sem estudos de caso publicados | método sem validação empírica documentada | alta | preparar primeiro caso após ferramentas mínimas |
| DD-009 | datas e históricos anteriores não estão uniformemente registrados | risco de história retrospectiva fictícia | alta | preservar incerteza e usar commits como evidência |
| DD-010 | execuções de push do workflow não são expostas pelo conector utilizado | publicação pode não ser confirmada pela auditoria automatizada | média | manter build estrito e verificar a execução diretamente no GitHub Actions |

## 7. Correções e avanços resultantes das revisões

As revisões do repositório produziram:

- sincronização do README com o ciclo completo e a governança documental;
- alinhamento da arquitetura descrita no README às seis camadas do ARQ-001;
- correção das classificações do inventário e da navegação;
- verificação da configuração do workflow com `mkdocs build --strict`;
- conclusão da Fase 1 de governança;
- conclusão dos lotes 2A, 2B e 2C do núcleo metodológico;
- normalização das fichas PPC-001 a PPC-004 e da Ficha de Teoria da Mudança;
- preservação dos estados `piloto` das fichas PPC-002 e PPC-003;
- conclusão do lote 3B com a migração das fichas PPC-005 a PPC-008.

A configuração do workflow está presente e coerente com GitHub Pages, mas sua execução mais recente deve ser confirmada diretamente no histórico do GitHub Actions, pois o conector utilizado não retorna eventos de push desse workflow.

## 8. Princípios da migração

A migração deve:

1. não mover arquivos prematuramente;
2. não alterar conteúdo metodológico apenas para adicionar metadados;
3. não inventar datas, autores ou aprovações;
4. preservar nomes e URLs consolidados;
5. avançar em lotes pequenos e revisáveis;
6. atualizar versões de acordo com a mudança real;
7. declarar dependências com base no conteúdo;
8. atualizar navegação e roadmap quando necessário;
9. verificar links e publicação após cada lote;
10. registrar dívida não resolvida.

## 9. Plano de migração progressiva

### Fase 0 — Linha de base

**Estado:** concluída e corrigida.

### Fase 1 — Núcleo de governança

**Estado:** concluída — 5 de 5 documentos migrados.

Documentos: PPC-000, Modelo de Governança, Roadmap, Guia de Contribuição e Código de Conduta.

### Fase 2 — Núcleo metodológico

**Estado:** concluída — lotes 2A, 2B e 2C finalizados; 10 de 10 documentos migrados.

A revisão confirmou a reciprocidade das dependências obrigatórias. A retroalimentação PPC-008 → PPC-001 permanece uma relação complementar, sem criar dependência circular obrigatória.

### Fase 3 — Ferramentas

**Estado:** em andamento — lotes 3A e 3B concluídos; 9 de 11 ferramentas conformes.

Lotes:

- **3A — concluído:** fichas PPC-001, PPC-002, PPC-004 e Teoria da Mudança; a Ficha PPC-003 foi complementada;
- **3B — concluído:** fichas PPC-005 a PPC-008;
- **3C — próximo:** matriz de avaliação, indicadores e revisão final dos vínculos das ferramentas.

Ações realizadas:

- atribuição de identificadores estáveis;
- declaração do documento associado e de sua versão;
- preservação dos estados canônicos existentes;
- preservação integral de campos, instruções e checklists;
- separação entre histórico da ferramenta e registros preenchíveis de cada aplicação.

### Fase 4 — Fundamentos e entrada

**Objetivo:** migrar documentos de maior autoridade sem alterar silenciosamente sua essência.

Ordem recomendada:

1. `FRAMEWORK_DE_REFERENCIA.md`;
2. `CARTA_DE_PRINCIPIOS.md`;
3. `TEORIA_DO_PRAGMATISMO_CIVICO.md`;
4. `SPECIFICATION.md`;
5. `MANIFESTO.md`;
6. `GLOSSARIO.md`;
7. `README.md` e `docs/COMECAR.md`.

### Fase 5 — Catálogo e navegação

Entregas: catálogo público, indicação de versão e status, agrupamento por camada, mapa de dependências, revisão da ordem de leitura e identificação de documentos técnicos fora da navegação principal.

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
- [ ] conteúdo substantivo preservado.

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
- a Fase 2 está concluída;
- os lotes 3A e 3B estão concluídos;
- a próxima execução será o lote 3C;
- a estrutura física será decidida somente depois de metadados, catálogo e validação.

## 13. Próxima ação

Executar a **Fase 3C — Ferramentas**, migrando a Matriz de Avaliação de Políticas Públicas e os Indicadores, além de revisar a consistência conjunta dos vínculos das onze ferramentas.

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
| 0.10.0 | 2026-07-18 | compatível | Conclusão do lote 3B, atualização da dívida documental e consolidação editorial do inventário | Projeto Pragmatismo Cívico |
