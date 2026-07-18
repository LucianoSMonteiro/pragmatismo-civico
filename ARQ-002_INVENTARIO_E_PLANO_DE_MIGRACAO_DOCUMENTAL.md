---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.16.1
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

Rascunho ativo. As Fases 0 a 6 estão concluídas: os 39 documentos públicos estão identificados, versionados, catalogados e submetidos a validação automática de metadados, relações, links, âncoras, catálogo e build estrito.

O GitHub Pages ainda depende de ativação inicial pelo proprietário, registrada na issue #1. Esse bloqueio é operacional e não invalida a aprovação do acervo nem da compilação.

## 1. Objetivo

Transformar a arquitetura do ARQ-001 em um processo verificável de inventário, catálogo, validação e evolução documental, sem mover arquivos sem benefício demonstrado, quebrar URLs ou inventar informações históricas.

## 2. Fontes canônicas

O processo utiliza:

- `mkdocs.yml` como fonte da navegação pública;
- metadados estruturados de cada documento;
- `CATALOGO_DOCUMENTAL.md` como visão consolidada;
- a branch padrão como fonte canônica;
- commits, status e artefatos da CI como evidência operacional.

## 3. Resumo do acervo público

| Camada | Quantidade | Situação geral |
|---|---:|---|
| Publicação e acesso | 3 | página inicial, guia e catálogo conformes |
| Princípios e fundamentos | 6 | todos conformes |
| Governança e arquitetura | 9 | todos conformes |
| Método | 10 | todos conformes |
| Ferramentas | 11 | todas conformes e vinculadas aos padrões |
| Aplicações e evidências | 0 | nenhum estudo de caso oficial publicado |
| **Total** | **39** | **39 documentos validados** |

Trinta e oito documentos usam cabeçalho YAML. O `README.md` utiliza representação estruturada equivalente em comentário HTML e seção colapsável.

## 4. Inventário resumido

### 4.1 Publicação e acesso

| Documento | Identificador | Versão |
|---|---|---:|
| Página inicial | `PORTAL-INICIO` | 0.4.0 |
| Guia de início | `GUIA-COMECAR` | 0.4.0 |
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

| Documento | Identificador |
|---|---|
| Especificação do Ecossistema PPC | `PPC-000` |
| Modelo de Governança | `GOV-001` |
| Roadmap | `GOV-002` |
| Guia de Contribuição | `GOV-003` |
| Código de Conduta | `GOV-004` |
| Metadados e Versionamento | `PPC-META-001` |
| Ciclo de Vida dos Padrões | `PPC-000A` |
| Arquitetura Documental | `ARQ-001` |
| Inventário e Plano de Migração | `ARQ-002` |

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
| `scripts/prepare_mkdocs.py` | prepara árvore temporária compatível com MkDocs |
| `.github/workflows/pages.yml` | executa validação, compara catálogo, compila e empacota o portal |

## 6. Resultado da Fase 6

A execução final `29633147790`, no commit `d49f6ad9865823928f9b5d7071e724f572f70df7`, foi aprovada com:

| Medida | Resultado |
|---|---:|
| Documentos avaliados | 39 |
| Dependências obrigatórias | 174 |
| Saídas declaradas | 46 |
| Relações complementares | 113 |
| Substituições vigentes | 0 |
| Destinos internos verificados | 126 |
| Âncoras verificadas | 0 |
| Erros | 0 |
| Avisos | 0 |

A automação verifica:

- presença dos campos obrigatórios;
- versões no formato `X.Y.Z`;
- estados, idioma, datas e compatibilidade;
- responsáveis e listas sem duplicidade;
- presença da versão corrente no histórico;
- existência de referências;
- reciprocidade de saídas e substituições;
- ciclos de dependências obrigatórias;
- links internos e âncoras;
- correspondência entre catálogo gerado e publicado;
- preparação e `mkdocs build --strict --clean`.

Três status de commit são registrados:

- `documentation/validation`;
- `documentation/catalog`;
- `portal/build`.

Os artefatos `validation-report`, `catalog-preview` e `github-pages` são preservados nas execuções aplicáveis. O relatório de validação permanece disponível por 14 dias, inclusive quando a execução é reprovada.

## 7. Limites da automação

A automação não substitui:

- revisão humana do mérito;
- aprovação metodológica;
- avaliação da qualidade das evidências;
- comprovação da adequação de uma mudança de versão;
- registro formal de transições de estado;
- validação empírica por aplicações reais.

## 8. Dívida documental e operacional

| ID | Problema | Estado | Tratamento |
|---|---|---|---|
| DD-005 | acervo predominantemente na raiz | aberta, baixa | avaliar na Fase 7 |
| DD-007 | validação automática incompleta | resolvida | Fase 6 concluída |
| DD-008 | ausência de estudos de caso | aberta, alta | preparar primeiro caso demonstrativo |
| DD-009 | datas históricas incompletas | controlada | preservar `null` e commits |
| DD-015 | README incompatível com front matter comum | controlada | representação equivalente reconhecida |
| DD-018 | GitHub Pages não habilitado | aberta | issue #1 |
| DD-019 | configuração original do MkDocs inválida | resolvida | árvore temporária e saída isolada |
| DD-020 | relações obrigatórias indevidas | resolvida | reclassificação e validação automática |
| DD-021 | possível deriva do catálogo | resolvida | comparação obrigatória na CI |
| DD-022 | validação não produzia diagnóstico persistente | resolvida | relatório e log preservados como artefato |
| DD-023 | parser de histórico não reconhecia títulos numerados ou qualificados | resolvida | parser ampliado sem dispensar a versão corrente |
| DD-024 | prévia do catálogo era preservada somente após comparação | resolvida | artefato enviado antes da verificação |
| DD-025 | divergência do catálogo era registrada como falha de build | resolvida | status `documentation/catalog` separado |

## 9. Plano progressivo

### Fases 0 a 4 — Migração e cobertura

**Estado:** concluídas.

### Fase 5 — Catálogo e navegação

**Estado:** concluída.

### Fase 6 — Validação automática

**Estado:** concluída.

### Fase 7 — Estrutura física

**Estado:** próxima decisão arquitetural.

A Fase 7 deve comparar os custos e benefícios de manter os documentos na raiz ou migrá-los para diretórios por camada. Nenhum arquivo será movido sem plano de redirecionamento, verificação de links e benefício demonstrado.

## 10. Decisões desta versão

Esta versão decide que:

- a Fase 6 está concluída;
- a CI deve preservar relatório e prévia antes de qualquer interrupção;
- validação, catálogo e build possuem status distintos;
- o bloqueio do Pages permanece separado da validação do acervo;
- a estrutura física não será alterada automaticamente;
- a próxima prioridade geral do projeto é formalizar propostas de mudança;
- a próxima prioridade arquitetural é avaliar a Fase 7.

## 11. Próxima ação

Formalizar o processo de propostas de mudança no eixo de governança e, em paralelo, preparar uma decisão fundamentada sobre a Fase 7 da arquitetura documental.

## 12. Histórico de alterações

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
| 0.15.0 | 2026-07-18 | compatível | Conclusão da Fase 5, publicação do catálogo e estabilização do build | Projeto Pragmatismo Cívico |
| 0.15.1 | 2026-07-18 | correção | Registro da verificação de deriva do catálogo | Projeto Pragmatismo Cívico |
| 0.16.0 | 2026-07-18 | compatível | Conclusão da Fase 6, validação integral e relatório persistente | Projeto Pragmatismo Cívico |
| 0.16.1 | 2026-07-18 | correção | Sincronização das versões de entrada, execução final, artefatos e terceiro status da CI | Projeto Pragmatismo Cívico |
