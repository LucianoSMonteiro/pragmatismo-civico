---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.18.0
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

Rascunho ativo. As Fases 0 a 7 estão concluídas. Os 42 documentos públicos estão identificados, versionados, catalogados e submetidos a validação automática. A estrutura física foi decidida no ARQ-003 e o processo de propostas de mudança foi publicado no GOV-005.

O GitHub Pages ainda depende de ativação inicial pelo proprietário, registrada na issue #1. Esse bloqueio operacional não invalida o acervo nem a compilação.

## 1. Objetivo

Manter um inventário verificável do acervo, de sua arquitetura, automação, dívida e evolução, preservando URLs e histórico e evitando mudanças sem benefício demonstrado.

## 2. Fontes canônicas

O processo utiliza:

- `mkdocs.yml` para a navegação pública;
- metadados estruturados de cada documento;
- `CATALOGO_DOCUMENTAL.md` para a visão consolidada;
- GOV-005 para propostas e decisões de mudança;
- ARQ-003 para caminhos e diretórios;
- a branch padrão como fonte canônica;
- commits, status e artefatos da CI como evidência operacional.

## 3. Resumo do acervo público

| Camada | Quantidade | Situação geral |
|---|---:|---|
| Publicação e acesso | 3 | página inicial, guia e catálogo conformes |
| Princípios e fundamentos | 6 | todos conformes |
| Governança e arquitetura | 11 | inclui GOV-005 e ARQ-003 |
| Método | 10 | todos conformes |
| Ferramentas | 12 | inclui a Ficha GOV-005 |
| Aplicações e evidências | 0 | nenhum estudo de caso oficial publicado |
| **Total** | **42** | **42 documentos catalogados e validados** |

Quarenta e um documentos usam cabeçalho YAML. O `README.md` utiliza representação estruturada equivalente em comentário HTML e seção colapsável.

## 4. Inventário resumido

### 4.1 Publicação e acesso

| Documento | Identificador | Versão |
|---|---|---:|
| Página inicial | `PORTAL-INICIO` | 0.6.0 |
| Guia de início | `GUIA-COMECAR` | 0.6.0 |
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
| Roadmap | `GOV-002` | 0.14.0 |
| Guia de Contribuição | `GOV-003` | 0.2.0 |
| Código de Conduta | `GOV-004` | 0.1.0 |
| Processo de Propostas de Mudança | `GOV-005` | 0.1.1 |
| Metadados e Versionamento | `PPC-META-001` | 0.2.0 |
| Ciclo de Vida dos Padrões | `PPC-000A` | 0.1.1 |
| Arquitetura Documental | `ARQ-001` | 0.2.0 |
| Inventário e Plano de Migração | `ARQ-002` | 0.18.0 |
| Decisão sobre a Estrutura Física | `ARQ-003` | 0.1.0 |

### 4.4 Método

| Documento | Identificador | Versão |
|---|---|---:|
| Ciclo do Pragmatismo Cívico | `CICLO-PC-001` | 0.1.0 |
| PPC-001 | `PPC-001` | 0.1.1 |
| PPC-002 | `PPC-002` | 0.1.0 |
| PPC-003 | `PPC-003` | 0.1.0 |
| PPC-004 | `PPC-004` | 0.1.0 |
| Teoria da Mudança | `MODELO-TDM-001` | 0.1.0 |
| PPC-005 | `PPC-005` | 0.1.0 |
| PPC-006 | `PPC-006` | 0.1.0 |
| PPC-007 | `PPC-007` | 0.1.0 |
| PPC-008 | `PPC-008` | 0.1.1 |

### 4.5 Ferramentas

| Documento | Identificador | Versão |
|---|---|---:|
| Fichas PPC-001 a PPC-008 | `FICHA-PPC-001` a `FICHA-PPC-008` | versões vigentes no catálogo |
| Ficha de Teoria da Mudança | `FICHA-TDM-001` | 0.1.0 |
| Ficha de Proposta de Mudança | `FICHA-GOV-005` | 0.1.0 |
| Matriz de avaliação | `MATRIZ-PPC-001` | 0.1.0 |
| Indicadores | `MODELO-INDICADORES-001` | 0.1.0 |

## 5. Infraestrutura de validação

| Recurso | Função |
|---|---|
| `scripts/generate_catalog.py` | gera o catálogo a partir da navegação e dos metadados |
| `scripts/validate_metadata_graph.py` | valida campos, formatos, histórico, relações, substituições e ciclos |
| `scripts/validate_links.py` | valida destinos internos e âncoras |
| `scripts/validate_issue_forms.py` | valida a estrutura dos formulários YAML de issue |
| `scripts/generate_validation_report.py` | produz relatório consolidado e dívida manual conhecida |
| `scripts/analyze_repository_structure.py` | calcula o impacto de migração física por camada |
| `scripts/prepare_mkdocs.py` | prepara a árvore temporária compatível com MkDocs |
| `.github/workflows/pages.yml` | valida, analisa, compara catálogo, compila e empacota o portal |

## 6. Governança de mudanças

O GOV-005 estabelece:

- identificadores `PM-AAAA-NNN`;
- tipos editorial, corretivo, metodológico, arquitetural, de governança, fundacional, de ciclo de vida e emergencial;
- níveis de impacto;
- triagem e admissibilidade;
- fluxos simplificado, ordinário e reforçado;
- consulta, revisão, decisão e conflitos de interesse;
- implementação, verificação, reversão e reconsideração;
- competência provisória e limite para mudanças fundacionais.

A `FICHA-GOV-005` e o formulário `.github/ISSUE_TEMPLATE/proposta-de-mudanca.yml` operacionalizam o processo.

## 7. Validação automática

A CI verifica:

- campos obrigatórios, versões, estados, datas e compatibilidade;
- responsáveis, histórico e unicidade de identificadores;
- existência e reciprocidade das relações obrigatórias;
- substituições e ciclos de dependência;
- links internos e âncoras;
- estrutura mínima dos formulários de issue;
- correspondência entre catálogo gerado e publicado;
- preparação e `mkdocs build --strict --clean`.

São registrados os status:

- `documentation/validation`;
- `documentation/catalog`;
- `portal/build`.

## 8. Estrutura física

O ARQ-003 preserva os caminhos existentes e determina:

- aplicações novas em `casos/`;
- relatórios oficiais em `relatorios/`;
- automações em `scripts/`;
- ativos em `docs/assets/`;
- reavaliação após três casos oficiais, 60 documentos ou evidência de custo material.

## 9. Dívida documental e operacional

| ID | Problema | Estado | Tratamento |
|---|---|---|---|
| DD-005 | acervo predominantemente na raiz | controlada | estrutura híbrida do ARQ-003 |
| DD-008 | ausência de estudos de caso | aberta, alta | preparar primeiro caso demonstrativo |
| DD-009 | datas históricas incompletas | controlada | preservar `null` e commits |
| DD-015 | README incompatível com front matter comum | controlada | representação equivalente reconhecida |
| DD-018 | GitHub Pages não habilitado | aberta | issue #1 |
| DD-028 | mudanças relevantes não possuíam processo operacional único | resolvida | GOV-005, ficha e formulário publicados |
| DD-029 | formulário poderia depender de rótulo inexistente | resolvida | dependência removida |
| DD-030 | GOV-003 e GOV-005 formariam ciclo obrigatório | resolvida | GOV-003 permanece dependente; GOV-005 apenas se relaciona ao guia |
| DD-031 | ausência de política permanente de revisão e aprovação | aberta | próxima prioridade de governança |
| DD-032 | ausência de instância plural constituída | aberta | decisões fundacionais permanecem limitadas |

## 10. Plano progressivo

| Fase | Tema | Estado |
|---|---|---|
| 0 a 4 | migração e cobertura | concluídas |
| 5 | catálogo e navegação | concluída |
| 6 | validação automática | concluída |
| 7 | estrutura física | concluída |

A evolução passa a ser governada pelo GOV-005. Alterações futuras devem possuir proposta formal quando ultrapassarem o fluxo editorial simplificado.

## 11. Próxima ação

Criar a política permanente de revisão e aprovação, detalhando competências, quóruns ou critérios decisórios, independência, impedimentos, prazos, consulta e transição entre a governança provisória e uma instância plural. Em paralelo, preparar o primeiro estudo de caso demonstrativo.

## 12. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Inventário inicial, dívida documental e plano progressivo | Projeto Pragmatismo Cívico |
| 0.2.0 a 0.14.1 | 2026-07-17 a 2026-07-18 | compatível | Migração, cobertura e sincronizações progressivas do acervo | Projeto Pragmatismo Cívico |
| 0.15.0 | 2026-07-18 | compatível | Conclusão da Fase 5 e estabilização do build | Projeto Pragmatismo Cívico |
| 0.15.1 | 2026-07-18 | correção | Verificação de deriva do catálogo | Projeto Pragmatismo Cívico |
| 0.16.0 | 2026-07-18 | compatível | Conclusão da Fase 6 | Projeto Pragmatismo Cívico |
| 0.16.1 | 2026-07-18 | correção | Sincronização final da validação | Projeto Pragmatismo Cívico |
| 0.17.0 | 2026-07-18 | compatível | Conclusão da Fase 7 e decisão pela estrutura híbrida | Projeto Pragmatismo Cívico |
| 0.18.0 | 2026-07-18 | compatível | Publicação do GOV-005, da ficha de proposta e da validação de formulários de issue | Projeto Pragmatismo Cívico |
