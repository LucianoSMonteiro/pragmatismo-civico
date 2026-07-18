---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.24.0
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
  - CASO-001-DADOS-CHUVA
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# ARQ-002 — Inventário e Plano de Migração Documental

## Status

Rascunho ativo. As Fases 0 a 7 estão concluídas e a Fase 8 está em execução. Os **54 documentos públicos** estão identificados, versionados e submetidos a validação automática.

A estrutura física é governada pelo ARQ-003; propostas pelo GOV-005; revisão pelo GOV-006; revisores pelo GOV-007; e seleção, prontidão e condução de casos pelo GOV-008.

O GitHub Pages ainda depende de ativação inicial pelo proprietário, registrada na issue #1. O cadastro de revisores permanece vazio. O CASO-001 está em preparação na sub-bacia de Itapeba e não possui diagnóstico ou resultado empírico. A matriz documental foi consolidada, mas nenhum polígono oficial, arquivo técnico integral ou série real foi incorporado.

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
- `casos/README.md` para o índice público;
- `casos/CASO-001_REGISTRO_DE_PRONTIDAO.md` para a decisão vigente do portão;
- `casos/CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md` para o inventário, estado de obtenção e lacunas das fontes;
- `casos/CASO-001_PROTOCOLO_DE_DADOS_PLUVIOMETRICOS.md` para aquisição, proveniência, qualidade, retenção e descarte da chuva;
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
| Aplicações e evidências | 5 | índice, CASO-001, prontidão, matriz de fontes e protocolo de dados |
| **Total** | **54** | **54 documentos submetidos à validação** |

Cinquenta e três documentos usam cabeçalho YAML. O `README.md` utiliza representação estruturada equivalente.

## 4. Inventário resumido

### 4.1 Publicação e acesso

| Documento | Identificador | Versão |
|---|---|---:|
| Página inicial | `PORTAL-INICIO` | 0.12.0 |
| Guia de início | `GUIA-COMECAR` | 0.12.0 |
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
| Roadmap | `GOV-002` | 0.20.0 |
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
| Inventário e Plano de Migração | `ARQ-002` | 0.24.0 |
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
| Índice de Casos e Evidências | `CASOS-INDEX` | 0.4.0 | índice público |
| Drenagem e alerta preventivo na sub-bacia de Itapeba | `CASO-001` | 0.3.0 | preparação |
| Registro de Prontidão do CASO-001 | `CASO-001-PRONTIDAO` | 0.2.0 | portão não aprovado |
| Matriz de Fontes e Lacunas | `CASO-001-FONTES` | 0.1.0 | 13 fontes consolidadas; obtenção integral pendente |
| Protocolo de Dados Pluviométricos | `CASO-001-DADOS-CHUVA` | 0.2.0 | processador e retenção definidos; coleta real pendente |

A matriz distingue fontes localizadas, consultadas, obtidas e tratadas. Nenhuma fonte foi classificada como obtida ou tratada para uso empírico. O protocolo define hashes, normalização UTC, flags, revisão manual, retenção e descarte. Nenhum arquivo mensal real foi incorporado.

## 5. Infraestrutura de validação e dados

| Recurso | Função |
|---|---|
| `scripts/generate_catalog.py` | gera catálogo nas seis camadas |
| `scripts/validate_metadata_graph.py` | valida campos, formatos, histórico, relações, substituições e ciclos |
| `scripts/validate_links.py` | valida destinos internos e âncoras |
| `scripts/validate_issue_forms.py` | valida formulários e template de pull request |
| `scripts/generate_validation_report.py` | produz relatório consolidado e dívida manual conhecida |
| `scripts/analyze_repository_structure.py` | calcula impacto de migração física e reconhece `casos/` |
| `scripts/prepare_mkdocs.py` | prepara a árvore temporária do portal |
| `scripts/processar_chuva_cemaden.py` | normaliza arquivos mensais, calcula hashes e produz manifesto e relatório |
| `tests/test_processar_chuva_cemaden.py` | testa filtros, datas, conversão de fuso e flags com fixture sintético |
| `tests/fixtures/cemaden_itapeba_sintetico.csv` | dados exclusivamente sintéticos para teste |
| `.github/workflows/pages.yml` | valida documentação, dados, catálogo e portal |

## 6. Governança vigente

O GOV-005 governa proposta, triagem, consulta, implementação, reversão e reconsideração.

O GOV-006 governa funções, competência, independência, conflitos, quórum, decisão e verificação.

O GOV-007 governa candidatura, elegibilidade, disponibilidade, proteção de dados, formação de painéis, revisão periódica e saída do cadastro.

O GOV-008 governa seleção, portão de prontidão, dados, participação, revisão, publicação, suspensão e encerramento de casos.

O cadastro começa vazio. O CASO-001 publica essa limitação e não pode simular revisão independente.

## 7. Validação automática

A CI verifica:

- campos, versões, estados, datas, compatibilidade e históricos;
- identificadores, dependências, reciprocidade, substituições e ciclos;
- links internos e âncoras;
- formulários de proposta e candidatura;
- salvaguardas públicas de privacidade;
- template de pull request;
- pipeline pluviométrico com fixture sintético;
- correspondência do catálogo nas seis camadas;
- preparação e `mkdocs build --strict --clean`.

Status registrados:

- `documentation/validation`;
- `data/pipeline`;
- `documentation/catalog`;
- `portal/build`.

## 8. Estrutura física

O ARQ-003 preserva caminhos existentes e determina aplicações em `casos/`, relatórios em `relatorios/`, automações em `scripts/` e ativos em `docs/assets/`.

Arquivos locais ainda não publicáveis são mantidos em `work/`, ignorado pelo Git. A política do CASO-001 define revisão a cada 90 dias, prazos ordinários por categoria, quarentena, registro de descarte, tratamento de backups e limites técnicos. Isso não substitui controles de acesso, licença ou privacidade.

## 9. Dívida documental e operacional

| ID | Problema | Estado | Tratamento |
|---|---|---|---|
| DD-005 | acervo predominantemente na raiz | controlada | estrutura híbrida do ARQ-003 |
| DD-008 | ausência de estudos de caso | parcialmente resolvida | CASO-001 ainda sem diagnóstico ou resultado |
| DD-009 | datas históricas incompletas | controlada | preservar `null` e commits |
| DD-015 | README sem front matter convencional | controlada | representação equivalente reconhecida |
| DD-018 | GitHub Pages não habilitado | aberta | issue #1 |
| DD-028 | ausência de processo de mudança | resolvida | GOV-005 |
| DD-031 | ausência de política de revisão | resolvida | GOV-006 |
| DD-032 | ausência de instância plural | aberta, controlada | regime provisório limita decisões críticas |
| DD-033 | ausência de programa de revisores | resolvida | GOV-007 e instrumentos |
| DD-035 | cadastro sem revisor elegível ou ativo | aberta, alta | issues #3 e #9 |
| DD-036 | ausência de canal privado | aberta | não coletar conteúdo confidencial por issue |
| DD-040 | ausência de protocolo para casos | resolvida | GOV-008 e FICHA-GOV-008 |
| DD-041 | CASO-001 sem prontidão mínima | aberta, alta | issue #2 e registro de prontidão |
| DD-042 | catálogo não representava a sexta camada | resolvida | camada incorporada ao gerador |
| DD-043 | analisador estrutural não reconhecia a sexta camada | resolvida | mapeamento para `casos/` |
| DD-044 | polígono oficial indisponível | aberta, alta | issue #6; anexo cartográfico apenas localizado |
| DD-045 | série pluviométrica real não coletada | aberta, alta | issue #4; processador pronto |
| DD-046 | documentos técnicos integrais indisponíveis | aberta, alta | issue #7 |
| DD-047 | participação e interlocutores não confirmados | aberta, alta | issue #8 |
| DD-048 | matriz de fontes incompleta | resolvida | `CASO-001-FONTES` e issue #10 |
| DD-049 | risco de publicação acidental e retenção indefinida | controlada | `work/` ignorado, prazos, quarentena e descarte; issue #11 |
| DD-050 | pipeline de dados sem teste automatizado | resolvida | teste sintético e status `data/pipeline` |

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

Executar a aquisição mensal autorizada da estação Itapeba, obter e verificar a geometria oficial, incorporar os documentos técnicos integrais e formar capacidade de revisão antes de nova decisão do portão.

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
| 0.23.0 | 2026-07-18 | compatível | Protocolo pluviométrico, teste sintético, quarto status de CI e linha de base de 53 documentos | Projeto Pragmatismo Cívico |
| 0.24.0 | 2026-07-18 | compatível | Matriz de fontes, política de retenção, atualização do portão e linha de base de 54 documentos | Projeto Pragmatismo Cívico |
