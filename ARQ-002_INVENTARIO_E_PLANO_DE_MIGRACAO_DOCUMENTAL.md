---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.25.0
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
  - CASO-001-PRONTIDAO
  - CASO-001-FONTES
  - CASO-001-GEOMETRIA
  - CASO-001-DADOS-CHUVA
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# ARQ-002 — Inventário e Plano de Migração Documental

## Status

Rascunho ativo. As Fases 0 a 7 estão concluídas e a Fase 8 está em execução. Os **55 documentos públicos** estão identificados, versionados e submetidos a validação automática.

A estrutura física é governada pelo ARQ-003; propostas pelo GOV-005; revisão pelo GOV-006; revisores pelo GOV-007; e seleção, prontidão e condução de casos pelo GOV-008.

O GitHub Pages ainda depende de ativação inicial pelo proprietário, registrada na issue #1. O cadastro de revisores permanece vazio. O CASO-001 está em preparação e não possui diagnóstico ou resultado empírico. Os pipelines de chuva e geometria passaram apenas com fixtures sintéticos; nenhuma série real ou feição oficial foi incorporada.

## 1. Objetivo

Manter inventário verificável do acervo, de sua arquitetura, automação, dívida e evolução, preservando URLs e histórico e evitando mudanças sem benefício demonstrado.

## 2. Fontes canônicas

- `mkdocs.yml` para a navegação;
- metadados estruturados dos documentos;
- `CATALOGO_DOCUMENTAL.md` para a visão consolidada;
- GOV-005 a GOV-008 para mudança, revisão, revisores e casos;
- `casos/README.md` para o índice público;
- `CASO-001-PRONTIDAO` para a decisão vigente do portão;
- `CASO-001-FONTES` para fontes, estado de obtenção e lacunas;
- `CASO-001-GEOMETRIA` para aquisição e validação geoespacial;
- `CASO-001-DADOS-CHUVA` para aquisição, qualidade, retenção e descarte pluviométrico;
- ARQ-003 para caminhos e diretórios;
- branch padrão, commits, estados e artefatos da CI como evidência operacional.

## 3. Resumo do acervo público

| Camada | Quantidade | Situação geral |
|---|---:|---|
| Publicação e acesso | 3 | página inicial, guia e catálogo conformes |
| Princípios e fundamentos | 6 | todos conformes |
| Governança e arquitetura | 15 | inclui GOV-005 a GOV-008, cadastro e ARQ-003 |
| Método | 10 | todos conformes |
| Ferramentas | 15 | inclui FICHAS GOV-005 a GOV-008 |
| Aplicações e evidências | 6 | índice, CASO-001, prontidão, fontes, geometria e chuva |
| **Total** | **55** | **55 documentos submetidos à validação** |

Cinquenta e quatro documentos usam cabeçalho YAML. O `README.md` utiliza representação estruturada equivalente.

## 4. Inventário resumido

### 4.1 Publicação e acesso

| Documento | Identificador | Versão |
|---|---|---:|
| Página inicial | `PORTAL-INICIO` | 0.13.0 |
| Guia de início | `GUIA-COMECAR` | 0.13.0 |
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
| Roadmap | `GOV-002` | 0.21.0 |
| Guia de Contribuição | `GOV-003` | 0.5.0 |
| Código de Conduta | `GOV-004` | 0.1.0 |
| Processo de Propostas de Mudança | `GOV-005` | 0.1.1 |
| Política de Revisão e Aprovação | `GOV-006` | 0.1.0 |
| Programa e Cadastro de Revisores | `GOV-007` | 0.1.1 |
| Cadastro Público de Revisores | `CADASTRO-REVISORES` | 0.1.1 |
| Protocolo de Casos Demonstrativos | `GOV-008` | 0.1.0 |
| Metadados e Versionamento | `PPC-META-001` | 0.2.0 |
| Ciclo de Vida dos Padrões | `PPC-000A` | 0.1.1 |
| Arquitetura Documental | `ARQ-001` | 0.2.0 |
| Inventário e Plano de Migração | `ARQ-002` | 0.25.0 |
| Decisão sobre a Estrutura Física | `ARQ-003` | 0.1.0 |

### 4.4 Método e ferramentas

O método permanece composto por `CICLO-PC-001`, PPC-001 a PPC-008 e `MODELO-TDM-001`. As ferramentas incluem fichas PPC-001 a PPC-008, Teoria da Mudança, matriz, indicadores e FICHAS GOV-005 a GOV-008, nas versões registradas no catálogo.

### 4.5 Aplicações e evidências

| Documento | Identificador | Versão | Estado material |
|---|---|---:|---|
| Índice de Casos e Evidências | `CASOS-INDEX` | 0.5.0 | índice público |
| Drenagem e alerta preventivo em Itapeba | `CASO-001` | 0.4.0 | preparação |
| Registro de Prontidão | `CASO-001-PRONTIDAO` | 0.3.0 | portão não aprovado |
| Matriz de Fontes e Lacunas | `CASO-001-FONTES` | 0.2.0 | 15 fontes; obtenção empírica pendente |
| Protocolo de Geometria e Delimitação | `CASO-001-GEOMETRIA` | 0.1.0 | validador sintético; feição oficial pendente |
| Protocolo de Dados Pluviométricos | `CASO-001-DADOS-CHUVA` | 0.2.0 | processador sintético; série real pendente |

Nenhuma fonte foi classificada como obtida ou tratada para uso empírico. Os geosserviços candidatos do INEA foram localizados, mas nenhuma feição de Itapeba foi preservada ou validada.

## 5. Infraestrutura de validação e dados

| Recurso | Função |
|---|---|
| `scripts/generate_catalog.py` | gera catálogo nas seis camadas |
| `scripts/validate_metadata_graph.py` | valida campos, formatos, histórico, relações, substituições e ciclos |
| `scripts/validate_links.py` | valida destinos internos e âncoras |
| `scripts/validate_issue_forms.py` | valida formulários e template de pull request |
| `scripts/generate_validation_report.py` | produz relatório consolidado e dívida manual conhecida |
| `scripts/analyze_repository_structure.py` | calcula impacto de migração física |
| `scripts/prepare_mkdocs.py` | prepara a árvore temporária do portal |
| `scripts/processar_chuva_cemaden.py` | normaliza chuva, calcula hashes e produz manifesto e relatório |
| `tests/test_processar_chuva_cemaden.py` | testa o processador com dados sintéticos |
| `scripts/validar_geojson_subbacia.py` | valida GeoJSON, anéis, coordenadas, extensão, nome e proveniência |
| `tests/test_validar_geojson_subbacia.py` | testa geometria válida e rejeição de anel aberto |
| `tests/fixtures/itapeba_subbacia_sintetica.geojson` | polígono exclusivamente sintético |
| `.github/workflows/pages.yml` | valida documentação, chuva, geometria, catálogo e portal |

## 6. Governança vigente

GOV-005 governa propostas; GOV-006, revisão e aprovação; GOV-007, revisores; GOV-008, seleção e condução dos casos.

O cadastro começa vazio. O CASO-001 publica essa limitação e não pode simular revisão independente.

## 7. Validação automática

A CI verifica:

- campos, versões, estados, datas, compatibilidade e históricos;
- identificadores, dependências, reciprocidade, substituições e ciclos;
- links internos e âncoras;
- formulários, privacidade e template de pull request;
- pipeline pluviométrico com fixture sintético;
- pipeline GeoJSON com fixture sintético;
- correspondência do catálogo nas seis camadas;
- preparação e `mkdocs build --strict --clean`.

Estados registrados:

- `documentation/validation`;
- `data/pipeline`;
- `geodata/pipeline`;
- `documentation/catalog`;
- `portal/build`.

## 8. Estrutura física

O ARQ-003 preserva caminhos existentes e determina aplicações em `casos/`, relatórios em `relatorios/`, automações em `scripts/` e ativos em `docs/assets/`.

Arquivos locais não publicáveis permanecem em `work/`, ignorado pelo Git. A política do CASO-001 define revisão periódica, retenção, quarentena, descarte e limites técnicos.

## 9. Dívida documental e operacional

| ID | Problema | Estado | Tratamento |
|---|---|---|---|
| DD-005 | acervo predominantemente na raiz | controlada | estrutura híbrida do ARQ-003 |
| DD-008 | ausência de estudos de caso | parcialmente resolvida | CASO-001 ainda sem diagnóstico ou resultado |
| DD-018 | GitHub Pages não habilitado | aberta | issue #1 |
| DD-032 | ausência de instância plural | aberta, controlada | regime provisório limita decisões críticas |
| DD-035 | cadastro sem revisor elegível ou ativo | aberta, alta | issues #3 e #9 |
| DD-036 | ausência de canal privado | aberta | não coletar conteúdo confidencial por issue |
| DD-041 | CASO-001 sem prontidão mínima | aberta, alta | issue #2 e registro de prontidão |
| DD-044 | feição oficial da sub-bacia indisponível | aberta, alta | issue #6; geosserviço candidato localizado |
| DD-045 | série pluviométrica real não coletada | aberta, alta | issue #4; processador pronto |
| DD-046 | documentos técnicos integrais indisponíveis | aberta, alta | issue #7 |
| DD-047 | participação e interlocutores não confirmados | aberta, alta | issue #8 |
| DD-048 | matriz de fontes dispersa | resolvida | `CASO-001-FONTES` |
| DD-049 | publicação acidental e retenção indefinida | controlada | `work/`, prazos, quarentena e descarte |
| DD-050 | pipeline de chuva sem teste | resolvida | `data/pipeline` |
| DD-051 | ausência de protocolo e validação geoespacial | resolvida | `CASO-001-GEOMETRIA` e `geodata/pipeline` |
| DD-052 | risco de confundir geosserviço com polígono obtido | controlada | estados de fonte, critérios de aquisição e revisão explícitos |

## 10. Plano progressivo

| Fase | Tema | Estado |
|---|---|---|
| 0 a 4 | migração e cobertura | concluídas |
| 5 | catálogo e navegação | concluída |
| 6 | validação automática | concluída |
| 7 | estrutura física | concluída |
| 8 | primeiros casos e evidências | em execução |

A evolução é governada pelos GOV-005 a GOV-008, com rigor proporcional e limites explícitos de capacidade.

## 11. Próxima ação

Consultar e preservar a resposta da camada estadual de sub-bacias, confirmar ou refutar a correspondência com Itapeba, executar a coleta pluviométrica autorizada, obter documentos técnicos integrais e formar capacidade de revisão antes de nova decisão do portão.

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
| 0.21.0 | 2026-07-18 | compatível | Publicação do GOV-008 e seleção preparatória do CASO-001 | Projeto Pragmatismo Cívico |
| 0.21.1 | 2026-07-18 | correção | Sincronização da versão do Guia de Contribuição | Projeto Pragmatismo Cívico |
| 0.22.0 | 2026-07-18 | compatível | Registro de prontidão, recorte de Itapeba e linha de base de 52 documentos | Projeto Pragmatismo Cívico |
| 0.23.0 | 2026-07-18 | compatível | Protocolo pluviométrico e linha de base de 53 documentos | Projeto Pragmatismo Cívico |
| 0.24.0 | 2026-07-18 | compatível | Matriz de fontes, retenção e linha de base de 54 documentos | Projeto Pragmatismo Cívico |
| 0.25.0 | 2026-07-18 | compatível | Protocolo geoespacial, validador GeoJSON e linha de base de 55 documentos | Projeto Pragmatismo Cívico |
