---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.17.0
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

Rascunho ativo. As Fases 0 a 7 estão concluídas. Os 40 documentos públicos estão identificados, versionados, catalogados e submetidos a validação automática. A estrutura física vigente foi avaliada e a decisão registrada no ARQ-003.

O GitHub Pages ainda depende de ativação inicial pelo proprietário, registrada na issue #1. Esse bloqueio operacional não invalida o acervo nem a compilação.

## 1. Objetivo

Transformar a arquitetura do ARQ-001 em um processo verificável de inventário, catálogo, validação e evolução documental, preservando URLs e histórico e evitando mudanças físicas sem benefício demonstrado.

## 2. Fontes canônicas

O processo utiliza:

- `mkdocs.yml` para a navegação pública;
- metadados estruturados de cada documento;
- `CATALOGO_DOCUMENTAL.md` para a visão consolidada;
- ARQ-003 para a decisão sobre caminhos e diretórios;
- a branch padrão como fonte canônica;
- commits, status e artefatos da CI como evidência operacional.

## 3. Resumo do acervo público

| Camada | Quantidade | Situação geral |
|---|---:|---|
| Publicação e acesso | 3 | página inicial, guia e catálogo conformes |
| Princípios e fundamentos | 6 | todos conformes |
| Governança e arquitetura | 10 | todos conformes, incluindo ARQ-003 |
| Método | 10 | todos conformes |
| Ferramentas | 11 | todas conformes e vinculadas aos padrões |
| Aplicações e evidências | 0 | nenhum estudo de caso oficial publicado |
| **Total** | **40** | **40 documentos catalogados e validados** |

Trinta e nove documentos usam cabeçalho YAML. O `README.md` utiliza representação estruturada equivalente em comentário HTML e seção colapsável.

## 4. Inventário resumido

### 4.1 Publicação e acesso

| Documento | Identificador | Versão |
|---|---|---:|
| Página inicial | `PORTAL-INICIO` | 0.5.0 |
| Guia de início | `GUIA-COMECAR` | 0.5.0 |
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
| Roadmap | `GOV-002` | 0.13.0 |
| Guia de Contribuição | `GOV-003` | 0.1.0 |
| Código de Conduta | `GOV-004` | 0.1.0 |
| Metadados e Versionamento | `PPC-META-001` | 0.2.0 |
| Ciclo de Vida dos Padrões | `PPC-000A` | 0.1.1 |
| Arquitetura Documental | `ARQ-001` | 0.2.0 |
| Inventário e Plano de Migração | `ARQ-002` | 0.17.0 |
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
| Ficha PPC-001 | `FICHA-PPC-001` | 0.1.0 |
| Ficha PPC-002 | `FICHA-PPC-002` | 0.1.0, piloto |
| Ficha PPC-003 | `FICHA-PPC-003` | 0.1.4, piloto |
| Ficha PPC-004 | `FICHA-PPC-004` | 0.1.0 |
| Ficha de Teoria da Mudança | `FICHA-TDM-001` | 0.1.0 |
| Ficha PPC-005 | `FICHA-PPC-005` | 0.1.0 |
| Ficha PPC-006 | `FICHA-PPC-006` | 0.1.1 |
| Ficha PPC-007 | `FICHA-PPC-007` | 0.1.1 |
| Ficha PPC-008 | `FICHA-PPC-008` | 0.1.0 |
| Matriz de avaliação | `MATRIZ-PPC-001` | 0.1.0 |
| Indicadores | `MODELO-INDICADORES-001` | 0.1.0 |

## 5. Infraestrutura de validação

| Recurso | Função |
|---|---|
| `scripts/generate_catalog.py` | gera o catálogo a partir da navegação e dos metadados |
| `scripts/validate_metadata_graph.py` | valida campos, formatos, histórico, relações, substituições e ciclos |
| `scripts/validate_links.py` | valida destinos internos e âncoras |
| `scripts/generate_validation_report.py` | produz relatório consolidado e dívida manual conhecida |
| `scripts/analyze_repository_structure.py` | calcula o impacto de uma migração física por camada |
| `scripts/prepare_mkdocs.py` | prepara a árvore temporária compatível com MkDocs |
| `.github/workflows/pages.yml` | valida, analisa, compara catálogo, compila e empacota o portal |

## 6. Validação automática

A CI verifica:

- campos obrigatórios, versões, estados, datas e compatibilidade;
- responsáveis, histórico e unicidade de identificadores;
- existência e reciprocidade das relações obrigatórias;
- substituições e ciclos de dependência;
- links internos e âncoras;
- correspondência entre catálogo gerado e publicado;
- preparação e `mkdocs build --strict --clean`.

São registrados os status:

- `documentation/validation`;
- `documentation/catalog`;
- `portal/build`.

Os artefatos incluem `validation-report`, `catalog-preview`, `structure-analysis` e `github-pages` nas execuções aplicáveis.

## 7. Resultado da Fase 7

A análise executada no run `29633432120`, com 39 documentos na linha de base, mostrou:

| Medida | Resultado |
|---|---:|
| Documentos na raiz | 38 |
| Documentos que seriam movidos | 37 |
| Links entre documentos públicos | 125 |
| Referências potencialmente afetadas | 124 |
| Entradas de navegação a revisar | 37 |

A migração atingiria quase todo o acervo sem melhorar a navegação do portal, que já é lógica e independente da estrutura física.

O ARQ-003 decidiu pela estrutura híbrida:

- preservar os caminhos existentes;
- usar `casos/` para novas aplicações;
- usar `relatorios/` para relatórios oficiais;
- manter automações, workflows e ativos nos diretórios atuais;
- reavaliar após três casos oficiais, 60 documentos ou evidência de custo material da estrutura vigente.

## 8. Dívida documental e operacional

| ID | Problema | Estado | Tratamento |
|---|---|---|---|
| DD-005 | acervo predominantemente na raiz | controlada | estrutura híbrida adotada no ARQ-003 |
| DD-008 | ausência de estudos de caso | aberta, alta | preparar primeiro caso demonstrativo |
| DD-009 | datas históricas incompletas | controlada | preservar `null` e commits |
| DD-015 | README incompatível com front matter comum | controlada | representação equivalente reconhecida |
| DD-018 | GitHub Pages não habilitado | aberta | issue #1 |
| DD-026 | migração física ameaçaria quase todos os links | resolvida | caminhos existentes preservados |
| DD-027 | crescimento futuro poderia ampliar a raiz indefinidamente | controlada | casos e relatórios terão diretórios próprios |

## 9. Plano progressivo

| Fase | Tema | Estado |
|---|---|---|
| 0 a 4 | migração e cobertura | concluídas |
| 5 | catálogo e navegação | concluída |
| 6 | validação automática | concluída |
| 7 | estrutura física | concluída |

A evolução arquitetural deixa de ser uma migração em aberto. Alterações futuras dependerão dos gatilhos e requisitos do ARQ-003.

## 10. Próxima ação

A prioridade geral passa a ser a governança de mudanças: criar um processo formal de propostas, análise, decisão, implementação e registro público. Em paralelo, deve ser preparado o primeiro estudo de caso demonstrativo.

## 11. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Inventário inicial, dívida documental e plano progressivo | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-17 | compatível | Migração do PPC-000 e do Modelo de Governança | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-17 | compatível | Correção das camadas e revisão da navegação | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-17 | compatível | Conclusão da Fase 1 | Projeto Pragmatismo Cívico |
| 0.5.0 | 2026-07-17 | compatível | Correções de identificadores e da Ficha PPC-003 | Projeto Pragmatismo Cívico |
| 0.6.0 | 2026-07-17 | compatível | Conclusão da Fase 2A | Projeto Pragmatismo Cívico |
| 0.7.0 | 2026-07-17 | compatível | Conclusão da Fase 2B | Projeto Pragmatismo Cívico |
| 0.8.0 | 2026-07-17 | compatível | Conclusão da Fase 2C | Projeto Pragmatismo Cívico |
| 0.9.0 | 2026-07-17 | compatível | Conclusão da Fase 3A | Projeto Pragmatismo Cívico |
| 0.10.0 | 2026-07-18 | compatível | Conclusão da Fase 3B e consolidação editorial | Projeto Pragmatismo Cívico |
| 0.11.0 | 2026-07-18 | compatível | Conclusão da Fase 3C | Projeto Pragmatismo Cívico |
| 0.12.0 | 2026-07-18 | compatível | Conclusão da Fase 4A | Projeto Pragmatismo Cívico |
| 0.13.0 | 2026-07-18 | compatível | Conclusão da Fase 4B e reparos normativos | Projeto Pragmatismo Cívico |
| 0.14.0 | 2026-07-18 | compatível | Conclusão da Fase 4C e cobertura dos 38 documentos | Projeto Pragmatismo Cívico |
| 0.14.1 | 2026-07-18 | correção | Sincronização do README 0.2.2 | Projeto Pragmatismo Cívico |
| 0.15.0 | 2026-07-18 | compatível | Conclusão da Fase 5 e publicação do catálogo | Projeto Pragmatismo Cívico |
| 0.15.1 | 2026-07-18 | correção | Registro da verificação de deriva do catálogo | Projeto Pragmatismo Cívico |
| 0.16.0 | 2026-07-18 | compatível | Conclusão da Fase 6 e validação automática completa | Projeto Pragmatismo Cívico |
| 0.16.1 | 2026-07-18 | correção | Sincronização das versões e dos três status de CI | Projeto Pragmatismo Cívico |
| 0.17.0 | 2026-07-18 | compatível | Conclusão da Fase 7, adoção da estrutura híbrida e incorporação do ARQ-003 | Projeto Pragmatismo Cívico |
