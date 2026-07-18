---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.6.0
status: rascunho
tipo: arquitetura
idioma: pt-BR
data_criacao: 2026-07-17
data_versao: 2026-07-17
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

O inventário inicial cobre os documentos expostos na navegação canônica do portal em `mkdocs.yml`, além dos principais arquivos conhecidos de configuração e publicação.

A navegação é utilizada como fonte da lista de documentos públicos. A classificação por camada segue o ARQ-001 e pode diferir da posição escolhida no menu quando a lógica de uso do portal justificar outra apresentação.

Esse recorte foi escolhido porque:

- representa o acervo público atualmente apresentado ao usuário;
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
| Método | 10 | lote 2A concluído; seis documentos migrados e quatro pendentes |
| Ferramentas | 11 | Ficha PPC-003 normalizada; demais vínculos ainda precisam ser estruturados |
| Aplicações e evidências | 0 | camada ainda sem estudo de caso publicado |
| **Total** | **38** | migração necessária, sem alteração imediata de caminhos |

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
| PPC-005 | `PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md` | implementação | a migrar | alta |
| PPC-006 | `PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md` | monitoramento | a migrar | alta |
| PPC-007 | `PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md` | avaliação | a migrar | alta |
| PPC-008 | `PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md` | aprendizagem | a migrar | alta |

### 4.5 Ferramentas

| Documento | Caminho | Documento associado | Metadados | Prioridade |
|---|---|---|---|---|
| Ficha PPC-001 | `FICHA_PPC-001_DIAGNOSTICO_DE_PROBLEMA_PUBLICO.md` | PPC-001 | a migrar | média |
| Ficha PPC-002 | `FICHA_PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md` | PPC-002 | a migrar | média |
| Ficha PPC-003 | `FICHA_PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md` | PPC-003 | presente | concluída nesta dimensão |
| Ficha PPC-004 | `FICHA_PPC-004_DECISAO_E_JUSTIFICATIVA.md` | PPC-004 | a migrar | média |
| Ficha de teoria da mudança | `FICHA_TEORIA_DA_MUDANCA.md` | modelo de teoria da mudança | a migrar | média |
| Ficha PPC-005 | `FICHA_PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md` | PPC-005 | a migrar | média |
| Ficha PPC-006 | `FICHA_PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md` | PPC-006 | a migrar | média |
| Ficha PPC-007 | `FICHA_PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md` | PPC-007 | a migrar | média |
| Ficha PPC-008 | `FICHA_PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md` | PPC-008 | a migrar | média |
| Matriz de avaliação | `MATRIZ_DE_AVALIACAO_DE_POLITICAS_PUBLICAS.md` | PPC-002 e PPC-003 | a migrar | média |
| Indicadores | `INDICADORES.md` | ciclo metodológico e avaliações | a migrar | média |

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
- `FICHA_PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md`;
- `CICLO_DO_PRAGMATISMO_CIVICO.md`;
- `PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md`;
- `PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md`;
- `PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md`;
- `PPC-004_DECISAO_E_JUSTIFICATIVA.md`;
- `MODELO_DE_TEORIA_DA_MUDANCA.md`.

### 5.2 Documentos ainda não migrados

Os demais itens do inventário devem ser tratados como não migrados até verificação direta e registro no próprio documento.

A migração não deve presumir:

- data histórica de criação;
- autoria individual;
- aprovação formal inexistente;
- versão anterior não registrada;
- estabilidade não demonstrada;
- dependência apenas inferida pelo número do PPC.

Quando uma informação não puder ser comprovada, deve ser registrada como `null`, lista vazia, estimativa explicitamente marcada ou pendência documental.

## 6. Dívida documental inicial

| ID | Problema | Risco | Prioridade | Tratamento proposto |
|---|---|---|---|---|
| DD-001 | 22 dos 38 documentos navegáveis ainda não possuem cabeçalho PPC-META-001 | versões e responsabilidades ambíguas | alta | migração em lotes controlados |
| DD-002 | dependências do ciclo metodológico ainda não estão uniformes em todos os padrões | incoerência entre padrões | alta | concluir lotes 2B e 2C |
| DD-003 | ferramentas não registram necessariamente a versão do padrão utilizada | aplicações podem ficar irreplicáveis | alta | adicionar campo de versão e vínculo |
| DD-004 | identificadores e metadados ainda heterogêneos nas ferramentas remanescentes | automação e catálogo dificultados | média | normalizar progressivamente sem descartar dados úteis |
| DD-005 | acervo predominantemente na raiz | manutenção futura pode ficar difícil | baixa no estágio atual | não mover arquivos antes de medir benefício |
| DD-006 | ausência de catálogo documental gerado | localização depende do `mkdocs.yml` | média | criar catálogo após migração mínima |
| DD-007 | ausência de validação automática de metadados e links | erros podem chegar ao portal | média | criar automação após estabilizar esquema |
| DD-008 | camada de aplicações sem estudos de caso publicados | método sem validação empírica documentada | alta | preparar primeiro caso após ferramentas mínimas |
| DD-009 | datas e históricos anteriores não estão uniformemente registrados | risco de história retrospectiva fictícia | alta | preservar incerteza e usar commits como evidência |
| DD-010 | execuções de push do workflow não são expostas pelo conector utilizado | publicação pode não ser confirmada pela auditoria automatizada | média | manter build estrito e verificar a execução diretamente no GitHub Actions |

## 7. Correções e avanços resultantes das revisões

As revisões do repositório produziram as seguintes correções e avanços:

- sincronização do README com PPC-001 a PPC-008, Teoria da Mudança, ferramentas e governança documental;
- alinhamento da arquitetura descrita no README às seis camadas do ARQ-001;
- reclassificação de ARQ-001, ARQ-002 e PPC-000 na camada de governança e arquitetura;
- adoção do nome canônico **Publicação e acesso** para a sexta camada;
- classificação de `INDICADORES.md` na camada de ferramentas;
- alinhamento da navegação, movendo Indicadores para a seção de ferramentas;
- verificação do workflow `.github/workflows/pages.yml` e de sua construção com `mkdocs build --strict`;
- migração de `ROADMAP.md`, `CONTRIBUTING.md` e `CODE_OF_CONDUCT.md` para o PPC-META-001;
- conclusão da Fase 1 do plano de migração documental;
- correção dos relacionamentos canônicos em ARQ-001 e PPC-000A;
- normalização do cabeçalho da Ficha PPC-003 sem alteração de seu conteúdo metodológico;
- conclusão do lote 2A com a migração do ciclo, PPC-001 a PPC-004 e Modelo de Teoria da Mudança.

A configuração do workflow está presente e coerente com GitHub Pages, mas a execução mais recente ainda deve ser confirmada no histórico do GitHub Actions, pois o conector utilizado não retorna os eventos de push desse workflow.

## 8. Princípios da migração

A migração deve seguir estas regras:

1. **não mover arquivos na primeira fase**;
2. **não alterar conteúdo metodológico apenas para adicionar metadados**;
3. **não inventar datas, autores ou aprovações**;
4. **preservar nomes e URLs consolidados**;
5. **migrar em lotes pequenos e revisáveis**;
6. **atualizar versão somente de acordo com a mudança real**;
7. **declarar dependências com base no conteúdo, não apenas na sequência numérica**;
8. **atualizar navegação e roadmap quando o lote afetar o portal**;
9. **verificar links e publicação após cada lote**;
10. **registrar dívida que não possa ser resolvida imediatamente**.

## 9. Plano de migração progressiva

### Fase 0 — Linha de base

**Estado:** concluída e corrigida.

Entregas:

- inventário inicial dos 38 documentos navegáveis;
- classificação por camada alinhada ao ARQ-001;
- registro da dívida documental inicial;
- reconhecimento de metadados legados;
- proibição explícita de movimentação prematura.

### Fase 1 — Núcleo de governança

**Estado:** concluída — 5 de 5 documentos migrados.

**Objetivo:** garantir que as regras que governam o restante do acervo sejam elas próprias rastreáveis.

Lote executado:

1. [x] `PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md`;
2. [x] `MODELO_DE_GOVERNANCA.md`;
3. [x] `ROADMAP.md`;
4. [x] `CONTRIBUTING.md`;
5. [x] `CODE_OF_CONDUCT.md`.

### Fase 2 — Núcleo metodológico

**Estado:** em andamento — lote 2A concluído; 6 de 10 documentos migrados.

**Objetivo:** tornar o ciclo PPC rastreável ponta a ponta.

Lotes:

- **2A — concluído:** ciclo, PPC-001 a PPC-004 e teoria da mudança;
- **2B — próximo:** PPC-005 a PPC-008;
- **2C:** revisão de reciprocidade das dependências.

Ações concluídas no lote 2A:

- adição de metadados e versões;
- declaração de entradas e saídas;
- identificação das ferramentas associadas;
- preservação do estado `rascunho` por ausência de validação formal suficiente;
- registro de compatibilidade como `inicial`;
- preservação do conteúdo metodológico.

### Fase 3 — Ferramentas

**Objetivo:** vincular cada instrumento à versão do padrão que operacionaliza.

Ações:

- atribuir identificadores estáveis;
- declarar documento associado;
- inserir campo para versão do padrão utilizado;
- distinguir campos obrigatórios e opcionais;
- verificar coerência entre ficha e PPC;
- preservar nomes de arquivo atuais nesta etapa.

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

O conteúdo do README já foi sincronizado com o estado atual, mas seu cabeçalho de metadados permanece reservado para esta fase.

Toda alteração nesses documentos deve ser estritamente documental, salvo processo substantivo específico.

### Fase 5 — Catálogo e navegação

Entregas:

- catálogo público de documentos;
- indicação de versão e status no portal;
- agrupamento por camada e categoria;
- mapa básico de dependências;
- revisão da ordem de leitura;
- identificação de documentos técnicos que podem ficar fora da navegação principal.

### Fase 6 — Validação automática

Entregas:

- esquema de validação dos cabeçalhos YAML;
- checagem de identificadores duplicados;
- validação do formato de versão e status;
- detecção de referências internas quebradas;
- build do MkDocs em pull requests e na branch padrão;
- relatório de dívida documental remanescente.

### Fase 7 — Estrutura física

Somente após as fases anteriores será decidido se arquivos devem sair da raiz.

A decisão deve comparar:

- melhoria real de localização e manutenção;
- custo de atualização de links;
- impacto sobre URLs externas;
- capacidade de redirecionamento;
- complexidade introduzida;
- reversibilidade.

A opção legítima de manter a estrutura atual deve permanecer aberta.

## 10. Checklist de cada lote

Antes do commit:

- [ ] escopo do lote definido;
- [ ] arquivos lidos integralmente;
- [ ] metadados baseados em evidência;
- [ ] versão coerente com a mudança;
- [ ] status conforme PPC-000A;
- [ ] dependências verificadas;
- [ ] histórico atualizado;
- [ ] links internos preservados;
- [ ] conteúdo substantivo não alterado acidentalmente.

Após o commit:

- [ ] arquivos novamente lidos da branch padrão;
- [ ] navegação verificada;
- [ ] roadmap atualizado, quando aplicável;
- [ ] build ou status de publicação consultado;
- [ ] SHA registrado;
- [ ] dívida residual anotada.

## 11. Critérios para concluir a migração mínima

A migração mínima estará concluída quando:

- todos os 38 documentos navegáveis possuírem identificação, versão, status e responsáveis;
- PPCs e ferramentas declararem relações recíprocas verificáveis;
- documentos fundadores possuírem fonte canônica e histórico preservado;
- o portal exibir ou permitir localizar versão e status;
- nenhuma movimentação tiver produzido links quebrados conhecidos;
- o inventário puder ser atualizado por processo repetível;
- novos documentos nascerem conformes aos padrões vigentes;
- a dívida restante estiver registrada e priorizada.

## 12. Decisões desta versão

Esta versão decide que:

- o inventário utiliza a navegação canônica como fonte da lista de documentos;
- a classificação por camada segue o ARQ-001, ainda que a posição no menu possa responder à lógica de uso;
- nenhum arquivo será movido durante os primeiros lotes;
- documentos sem evidência histórica não receberão datas ou aprovações retroativas;
- a Fase 2A está concluída e a próxima execução da migração será o lote 2B;
- a estrutura física do repositório será decidida somente depois de metadados, catálogo e validação.

## 13. Próxima ação

Executar a **Fase 2B — Núcleo metodológico**, migrando PPC-005 a PPC-008 e preparando a revisão de reciprocidade das dependências do ciclo completo.

## 14. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Inventário inicial, dívida documental e plano progressivo de migração | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-17 | compatível | Atualização do inventário e registro da migração do PPC-000 e do Modelo de Governança | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-17 | compatível | Correção das camadas, reconhecimento de metadados legados e registro da revisão de coerência do README e da navegação | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-17 | compatível | Conclusão da Fase 1 com a migração do roadmap, guia de contribuição e código de conduta | Projeto Pragmatismo Cívico |
| 0.5.0 | 2026-07-17 | compatível | Correção de identificadores canônicos, nomenclatura da sexta camada e normalização da Ficha PPC-003 | Projeto Pragmatismo Cívico |
| 0.6.0 | 2026-07-17 | compatível | Conclusão da Fase 2A com a migração do ciclo, PPC-001 a PPC-004 e Modelo de Teoria da Mudança | Projeto Pragmatismo Cívico |
