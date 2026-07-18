---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.21.0
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
  - ARQ-003
relaciona_se_com:
  - GOV-002
  - GOV-005
  - GOV-006
  - GOV-007
  - GOV-008
  - MKDOCS
  - PORTAL-INICIO
  - GUIA-COMECAR
  - CASOS-INDEX
  - CASO-001
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# ARQ-002 — Inventário e Plano de Migração Documental

## Status

Rascunho ativo. As Fases 0 a 7 estão concluídas. Os **51 documentos públicos** estão identificados, versionados e submetidos a validação automática.

A estrutura física é governada pelo ARQ-003; propostas pelo GOV-005; revisão pelo GOV-006; revisores pelo GOV-007; e seleção, prontidão e condução de casos pelo GOV-008.

O GitHub Pages ainda depende de ativação inicial pelo proprietário, registrada na issue #1. O cadastro de revisores permanece vazio. O CASO-001 está em preparação e não possui diagnóstico ou resultado empírico.

## 1. Objetivo

Manter inventário verificável do acervo, de sua arquitetura, automação, dívida e evolução, preservando URLs e histórico e evitando mudanças sem benefício demonstrado.

## 2. Fontes canônicas

- `mkdocs.yml` para a navegação;
- metadados estruturados dos documentos;
- `CATALOGO_DOCUMENTAL.md` para a visão consolidada;
- GOV-005 para propostas;
- GOV-006 para revisão, aprovação e verificação;
- GOV-007 e `CADASTRO_PUBLICO_DE_REVISORES.md` para revisores;
- GOV-008 e `FICHA_GOV-008_REGISTRO_DE_SELECAO_E_CONDUCAO_DE_CASO.md` para casos;
- `casos/README.md` para o índice público de aplicações;
- ARQ-003 para caminhos e diretórios;
- branch padrão, commits, status e artefatos da CI como evidência operacional.

## 3. Resumo do acervo público

| Camada | Quantidade | Situação geral |
|---|---:|---|
| Publicação e acesso | 3 | página inicial, guia e catálogo conformes |
| Princípios e fundamentos | 6 | todos conformes |
| Governança e arquitetura | 15 | inclui GOV-005 a GOV-008, cadastro e ARQ-003 |
| Método | 10 | todos conformes |
| Ferramentas | 15 | inclui FICHAS GOV-005 a GOV-008 |
| Aplicações e evidências | 2 | índice público e CASO-001 em preparação |
| **Total** | **51** | **51 documentos submetidos à validação** |

Cinquenta documentos usam cabeçalho YAML. O `README.md` utiliza representação estruturada equivalente.

## 4. Inventário resumido

### 4.1 Publicação e acesso

| Documento | Identificador | Versão |
|---|---|---:|
| Página inicial | `PORTAL-INICIO` | 0.9.0 |
| Guia de início | `GUIA-COMECAR` | 0.9.0 |
| Catálogo documental | `CATALOGO-DOCUMENTAL` | 0.1.0 |

### 4.2 Princípios e fundamentos

| Documento | Identificador | Versão |
|---|---|---:|
| Carta de Princípios | `CARTA-DE-PRINCIPIOS` | 0.1.2 |
| Especificação | `SPECIFICATION` | 0.2.0 |
| Framework de Referência | `FRAMEWORK-DE-REFERENCIA` | 0.2.0 |
| Teoria do Pragmatismo Cívico | `TEORIA-DO-PRAGMATISMO-CIVICO` | 0.1.0 |
| Manifesto | `MANIFESTO` | 0.1.0 |
| Glossário | `GLOSSARIO` | 0.1.0 |

### 4.3 Governança e arquitetura

| Documento | Identificador | Versão |
|---|---|---:|
| Especificação do Ecossistema PPC | `PPC-000` | 0.1.0 |
| Modelo de Governança | `GOV-001` | 0.1.0 |
| Roadmap | `GOV-002` | 0.17.0 |
| Guia de Contribuição | `GOV-003` | 0.4.0 |
| Código de Conduta | `GOV-004` | 0.1.0 |
| Processo de Propostas de Mudança | `GOV-005` | 0.1.1 |
| Política de Revisão e Aprovação | `GOV-006` | 0.1.0 |
| Programa e Cadastro de Revisores | `GOV-007` | 0.1.1 |
| Cadastro Público de Revisores | `CADASTRO-REVISORES` | 0.1.1 |
| Protocolo de Casos Demonstrativos | `GOV-008` | 0.1.0 |
| Metadados e Versionamento | `PPC-META-001` | 0.2.0 |
| Ciclo de Vida dos Padrões | `PPC-000A` | 0.1.1 |
| Arquitetura Documental | `ARQ-001` | 0.2.0 |
| Inventário e Plano de Migração | `ARQ-002` | 0.21.0 |
| Decisão sobre a Estrutura Física | `ARQ-003` | 0.1.0 |

### 4.4 Método

O método permanece composto por `CICLO-PC-001`, PPC-001 a PPC-008 e `MODELO-TDM-001`, nas versões registradas no catálogo.

### 4.5 Ferramentas

O acervo contém fichas PPC-001 a PPC-008, Ficha de Teoria da Mudança, matriz, indicadores e:

- `FICHA-GOV-005` — proposta de mudança;
- `FICHA-GOV-006` — revisão e aprovação;
- `FICHA-GOV-007` — candidatura e avaliação de revisor;
- `FICHA-GOV-008` — seleção, prontidão e condução de caso.

### 4.6 Aplicações e evidências

| Documento | Identificador | Versão | Estado material |
|---|---|---:|---|
| Índice de Casos e Evidências | `CASOS-INDEX` | 0.1.0 | índice público inicial |
| Drenagem urbana e alerta preventivo em Maricá/RJ | `CASO-001` | 0.1.0 | preparação; portão de prontidão não aprovado |

A existência do CASO-001 não equivale a estudo concluído, diagnóstico oficial ou validação empírica.

## 5. Infraestrutura de validação

| Recurso | Função |
|---|---|
| `scripts/generate_catalog.py` | gera catálogo nas seis camadas |
| `scripts/validate_metadata_graph.py` | valida campos, formatos, histórico, relações, substituições e ciclos |
| `scripts/validate_links.py` | valida destinos internos e âncoras |
| `scripts/validate_issue_forms.py` | valida formulários e template de pull request |
| `scripts/generate_validation_report.py` | produz relatório consolidado e dívida manual conhecida |
| `scripts/analyze_repository_structure.py` | calcula impacto de migração física |
| `scripts/prepare_mkdocs.py` | prepara a árvore temporária do portal |
| `.github/workflows/pages.yml` | valida, analisa, compara catálogo, compila e empacota |

## 6. Governança vigente

O GOV-005 governa proposta, triagem, consulta, implementação, reversão e reconsideração.

O GOV-006 governa funções, competência, independência, conflitos, quórum, decisão e verificação.

O GOV-007 governa candidatura, elegibilidade, disponibilidade, proteção de dados, formação de painéis, revisão periódica e saída do cadastro.

O GOV-008 governa seleção, portão de prontidão, dados, participação, revisão, publicação, suspensão e encerramento de casos.

O cadastro começa vazio. O CASO-001 deve publicar essa limitação e não pode simular revisão independente.

## 7. Validação automática

A CI verifica:

- campos, versões, estados, datas, compatibilidade e históricos;
- identificadores, dependências, reciprocidade, substituições e ciclos;
- links internos e âncoras;
- formulários de proposta e candidatura;
- salvaguardas públicas de privacidade;
- template de pull request;
- correspondência do catálogo nas seis camadas;
- preparação e `mkdocs build --strict --clean`.

Status registrados:

- `documentation/validation`;
- `documentation/catalog`;
- `portal/build`.

## 8. Estrutura física

O ARQ-003 preserva caminhos existentes e determina aplicações em `casos/`, relatórios em `relatorios/`, automações em `scripts/` e ativos em `docs/assets/`.

A criação efetiva de `casos/` confirmou a estratégia híbrida sem mover documentos anteriores.

## 9. Dívida documental e operacional

| ID | Problema | Estado | Tratamento |
|---|---|---|---|
| DD-005 | acervo predominantemente na raiz | controlada | estrutura híbrida do ARQ-003 |
| DD-008 | ausência de estudos de caso | parcialmente resolvida | CASO-001 selecionado, ainda sem diagnóstico ou resultado |
| DD-009 | datas históricas incompletas | controlada | preservar `null` e commits |
| DD-015 | README sem front matter convencional | controlada | representação equivalente reconhecida |
| DD-018 | GitHub Pages não habilitado | aberta | issue #1 |
| DD-028 | ausência de processo de mudança | resolvida | GOV-005 |
| DD-031 | ausência de política de revisão | resolvida | GOV-006 |
| DD-032 | ausência de instância plural | aberta, controlada | regime provisório limita decisões críticas |
| DD-033 | ausência de programa de revisores | resolvida | GOV-007 e instrumentos |
| DD-035 | cadastro sem revisor elegível ou ativo | aberta, alta | realizar primeira chamada e avaliações públicas |
| DD-036 | ausência de canal privado | aberta | não coletar conteúdo confidencial por issue |
| DD-039 | ciclo entre GOV-003 e GOV-007 | resolvida | vínculo reclassificado como complementar |
| DD-040 | ausência de protocolo para casos | resolvida | GOV-008 e FICHA-GOV-008 |
| DD-041 | CASO-001 sem prontidão mínima | aberta, alta | delimitar território, fontes, responsáveis, dados e revisão |
| DD-042 | catálogo não representava a sexta camada | resolvida | camada Aplicações e evidências incorporada ao gerador |

## 10. Plano progressivo

| Fase | Tema | Estado |
|---|---|---|
| 0 a 4 | migração e cobertura | concluídas |
| 5 | catálogo e navegação | concluída |
| 6 | validação automática | concluída |
| 7 | estrutura física | concluída |
| 8 | primeiros casos e evidências | iniciada |

A evolução é governada pelos GOV-005 a GOV-008, com rigor proporcional e limites explícitos de capacidade.

## 11. Próxima ação

Completar o portão de prontidão do CASO-001 e realizar a primeira chamada pública de revisores, sem inventar dados, presumir solução ou coletar conteúdo confidencial em issues.

## 12. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Inventário inicial, dívida e plano progressivo | Projeto Pragmatismo Cívico |
| 0.2.0 a 0.14.1 | 2026-07-17 a 2026-07-18 | compatível | Migração, cobertura e sincronizações progressivas | Projeto Pragmatismo Cívico |
| 0.15.0 | 2026-07-18 | compatível | Conclusão da Fase 5 e estabilização do build | Projeto Pragmatismo Cívico |
| 0.16.0 | 2026-07-18 | compatível | Conclusão da Fase 6 | Projeto Pragmatismo Cívico |
| 0.17.0 | 2026-07-18 | compatível | Conclusão da Fase 7 | Projeto Pragmatismo Cívico |
| 0.18.0 | 2026-07-18 | compatível | Publicação do GOV-005 e instrumentos | Projeto Pragmatismo Cívico |
| 0.19.0 | 2026-07-18 | compatível | Publicação do GOV-006 e instrumentos | Projeto Pragmatismo Cívico |
| 0.20.0 | 2026-07-18 | compatível | Publicação do GOV-007 e instrumentos | Projeto Pragmatismo Cívico |
| 0.20.1 | 2026-07-18 | correção | Eliminação do ciclo GOV-003/GOV-007 | Projeto Pragmatismo Cívico |
| 0.21.0 | 2026-07-18 | compatível | Publicação do GOV-008, ativação da sexta camada e seleção preparatória do CASO-001 | Projeto Pragmatismo Cívico |
