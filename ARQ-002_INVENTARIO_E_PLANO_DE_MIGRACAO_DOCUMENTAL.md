---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.20.0
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

Rascunho ativo. As Fases 0 a 7 estão concluídas. Os **47 documentos públicos** estão identificados, versionados, catalogados e submetidos a validação automática.

A estrutura física é governada pelo ARQ-003; propostas pelo GOV-005; revisão e aprovação pelo GOV-006; e candidatura, elegibilidade e cadastro de revisores pelo GOV-007.

O GitHub Pages ainda depende de ativação inicial pelo proprietário, registrada na issue #1. O cadastro público existe, mas não possui pessoa elegível ou ativa.

## 1. Objetivo

Manter inventário verificável do acervo, de sua arquitetura, automação, dívida e evolução, preservando URLs e histórico e evitando mudanças sem benefício demonstrado.

## 2. Fontes canônicas

- `mkdocs.yml` para a navegação;
- metadados estruturados dos documentos;
- `CATALOGO_DOCUMENTAL.md` para a visão consolidada;
- GOV-005 para propostas;
- GOV-006 para revisão, aprovação e verificação;
- GOV-007 para o programa de revisores;
- `CADASTRO_PUBLICO_DE_REVISORES.md` para elegibilidade e disponibilidade;
- ARQ-003 para caminhos e diretórios;
- branch padrão, commits, status e artefatos da CI como evidência operacional.

## 3. Resumo do acervo público

| Camada | Quantidade | Situação geral |
|---|---:|---|
| Publicação e acesso | 3 | página inicial, guia e catálogo conformes |
| Princípios e fundamentos | 6 | todos conformes |
| Governança e arquitetura | 14 | inclui GOV-005 a GOV-007, cadastro e ARQ-003 |
| Método | 10 | todos conformes |
| Ferramentas | 14 | inclui FICHAS GOV-005 a GOV-007 |
| Aplicações e evidências | 0 | nenhum estudo de caso oficial publicado |
| **Total** | **47** | **47 documentos catalogados e validados** |

Quarenta e seis documentos usam cabeçalho YAML. O `README.md` utiliza representação estruturada equivalente.

## 4. Inventário resumido

### 4.1 Publicação e acesso

| Documento | Identificador | Versão |
|---|---|---:|
| Página inicial | `PORTAL-INICIO` | 0.8.0 |
| Guia de início | `GUIA-COMECAR` | 0.8.0 |
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
| Roadmap | `GOV-002` | 0.16.0 |
| Guia de Contribuição | `GOV-003` | 0.4.0 |
| Código de Conduta | `GOV-004` | 0.1.0 |
| Processo de Propostas de Mudança | `GOV-005` | 0.1.1 |
| Política de Revisão e Aprovação | `GOV-006` | 0.1.0 |
| Programa e Cadastro de Revisores | `GOV-007` | 0.1.0 |
| Cadastro Público de Revisores | `CADASTRO-REVISORES` | 0.1.1 |
| Metadados e Versionamento | `PPC-META-001` | 0.2.0 |
| Ciclo de Vida dos Padrões | `PPC-000A` | 0.1.1 |
| Arquitetura Documental | `ARQ-001` | 0.2.0 |
| Inventário e Plano de Migração | `ARQ-002` | 0.20.0 |
| Decisão sobre a Estrutura Física | `ARQ-003` | 0.1.0 |

### 4.4 Método

O método permanece composto por `CICLO-PC-001`, PPC-001 a PPC-008 e `MODELO-TDM-001`, nas versões registradas no catálogo.

### 4.5 Ferramentas

O acervo contém as fichas PPC-001 a PPC-008, Ficha de Teoria da Mudança, matriz, indicadores e:

- `FICHA-GOV-005` — proposta de mudança;
- `FICHA-GOV-006` — revisão e aprovação;
- `FICHA-GOV-007` — candidatura e avaliação de revisor.

## 5. Infraestrutura de validação

| Recurso | Função |
|---|---|
| `scripts/generate_catalog.py` | gera o catálogo a partir da navegação e dos metadados |
| `scripts/validate_metadata_graph.py` | valida campos, formatos, histórico, relações, substituições e ciclos |
| `scripts/validate_links.py` | valida destinos internos e âncoras |
| `scripts/validate_issue_forms.py` | valida os formulários canônicos e o template de pull request |
| `scripts/generate_validation_report.py` | produz relatório consolidado e dívida manual conhecida |
| `scripts/analyze_repository_structure.py` | calcula o impacto de migração física |
| `scripts/prepare_mkdocs.py` | prepara a árvore temporária do portal |
| `.github/workflows/pages.yml` | valida, analisa, compara catálogo, compila e empacota |

A validação dos formulários exige campos canônicos da proposta e da candidatura, declarações obrigatórias e salvaguardas contra publicação de dados pessoais sensíveis.

## 6. Governança de mudanças e revisões

O GOV-005 governa proposta, triagem, consulta, implementação, reversão e reconsideração.

O GOV-006 governa funções, competência, independência, conflitos, quórum, decisão e verificação.

O GOV-007 governa candidatura, elegibilidade, disponibilidade, proteção de dados, formação de painéis, revisão periódica e saída do cadastro.

O cadastro começa vazio. Mantenedores e autores não são incluídos automaticamente.

## 7. Validação automática

A CI verifica:

- campos, versões, estados, datas, compatibilidade e históricos;
- identificadores, dependências, reciprocidade, substituições e ciclos;
- links internos e âncoras;
- formulários de proposta e candidatura;
- salvaguardas públicas de privacidade;
- template de pull request;
- correspondência do catálogo;
- preparação e `mkdocs build --strict --clean`.

Status registrados:

- `documentation/validation`;
- `documentation/catalog`;
- `portal/build`.

## 8. Estrutura física

O ARQ-003 preserva caminhos existentes e determina aplicações em `casos/`, relatórios em `relatorios/`, automações em `scripts/` e ativos em `docs/assets/`.

## 9. Dívida documental e operacional

| ID | Problema | Estado | Tratamento |
|---|---|---|---|
| DD-005 | acervo predominantemente na raiz | controlada | estrutura híbrida do ARQ-003 |
| DD-008 | ausência de estudos de caso | aberta, alta | preparar primeiro caso demonstrativo |
| DD-009 | datas históricas incompletas | controlada | preservar `null` e commits |
| DD-015 | README sem front matter convencional | controlada | representação equivalente reconhecida |
| DD-018 | GitHub Pages não habilitado | aberta | issue #1 |
| DD-028 | ausência de processo de mudança | resolvida | GOV-005 |
| DD-031 | ausência de política de revisão | resolvida | GOV-006 |
| DD-032 | ausência de instância plural | aberta, controlada | regime provisório limita decisões críticas |
| DD-033 | ausência de programa e cadastro de revisores | resolvida | GOV-007, ficha, formulário e cadastro publicados |
| DD-034 | pull requests sem estrutura comum | resolvida | template publicado e validado |
| DD-035 | cadastro sem revisor elegível ou ativo | aberta, alta | realizar primeira chamada e avaliações públicas |
| DD-036 | ausência de canal privado para informação confidencial | aberta | não coletar dados confidenciais por issue; definir canal antes de necessidade real |
| DD-037 | formulário de candidatura teve YAML inválido | resolvida | indentação e placeholder corrigidos; contrato incorporado à CI |
| DD-038 | saída da FICHA-GOV-007 não era recíproca | resolvida | cadastro passou a depender da ficha |

## 10. Plano progressivo

| Fase | Tema | Estado |
|---|---|---|
| 0 a 4 | migração e cobertura | concluídas |
| 5 | catálogo e navegação | concluída |
| 6 | validação automática | concluída |
| 7 | estrutura física | concluída |

A evolução é governada pelos GOV-005 a GOV-007, com rigor proporcional e limites explícitos de capacidade.

## 11. Próxima ação

Selecionar e documentar o primeiro estudo de caso demonstrativo e realizar a primeira chamada pública de revisores, sem admitir pessoas automaticamente ou coletar dados confidenciais em issues.

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
| 0.20.0 | 2026-07-18 | compatível | Publicação do GOV-007, ficha, formulário, cadastro e salvaguardas de privacidade | Projeto Pragmatismo Cívico |
