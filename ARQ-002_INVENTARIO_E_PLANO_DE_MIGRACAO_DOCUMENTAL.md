---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.27.0
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
  - CASO-001-DOCUMENTOS-TECNICOS
  - CASO-001-GEOMETRIA
  - CASO-001-DADOS-CHUVA
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# ARQ-002 — Inventário e Plano de Migração Documental

## Status

Rascunho ativo. As Fases 0 a 7 estão concluídas e a Fase 8 está em execução. Os **56 documentos públicos** estão identificados, versionados e submetidos a validação automática.

A estrutura física é governada pelo ARQ-003; propostas pelo GOV-005; revisão pelo GOV-006; revisores pelo GOV-007; e seleção, prontidão e condução de casos pelo GOV-008.

O GitHub Pages ainda depende de ativação inicial pelo proprietário, registrada na issue #1. O cadastro de revisores permanece vazio. O CASO-001 está em preparação e não possui diagnóstico ou resultado empírico.

A camada de aplicações agora contém registros distintos para fontes gerais, documentos técnicos e contratações, geometria e chuva. O inventário técnico está estruturado e validado, mas nenhum programa final, contrato integral, projeto, medição ou as-built foi obtido com hash.

## 1. Objetivo

Manter inventário verificável do acervo, de sua arquitetura, automação, dívida e evolução, preservando URLs e histórico e evitando mudanças sem benefício demonstrado.

## 2. Fontes canônicas

- `mkdocs.yml` para a navegação;
- metadados estruturados dos documentos;
- `CATALOGO_DOCUMENTAL.md` para a visão consolidada;
- GOV-005 a GOV-008 para mudança, revisão, revisores e casos;
- `casos/README.md` para o índice público;
- `CASO-001-PRONTIDAO` para a decisão vigente do portão;
- `CASO-001-FONTES` para fontes gerais, obtenção e lacunas;
- `CASO-001-DOCUMENTOS-TECNICOS` e seu registro JSON para comunicações, financiamentos, contratações, alegações e documentos requeridos;
- `CASO-001-GEOMETRIA` para coleta, validação e delimitação geoespacial;
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
| Aplicações e evidências | 7 | índice, caso, prontidão, fontes, documentos técnicos, geometria e chuva |
| **Total** | **56** | **56 documentos submetidos à validação** |

Cinquenta e cinco documentos usam cabeçalho YAML. O `README.md` utiliza representação estruturada equivalente.

## 4. Inventário resumido

### 4.1 Publicação e acesso

| Documento | Identificador | Versão |
|---|---|---:|
| Página inicial | `PORTAL-INICIO` | 0.13.0 |
| Guia de início | `GUIA-COMECAR` | 0.13.0 |
| Catálogo documental | `CATALOGO-DOCUMENTAL` | 0.1.0 |

### 4.2 Princípios, governança, método e ferramentas

As camadas permanecem nas versões registradas no catálogo. O inventário corrente é `ARQ-002` 0.27.0; o roadmap será sincronizado com a linha de base de 56 documentos.

### 4.3 Aplicações e evidências

| Documento | Identificador | Versão | Estado material |
|---|---|---:|---|
| Índice de Casos e Evidências | `CASOS-INDEX` | 0.6.0 | índice público |
| Drenagem e alerta preventivo em Itapeba | `CASO-001` | 0.4.0 | preparação |
| Registro de Prontidão | `CASO-001-PRONTIDAO` | 0.3.1 | portão não aprovado |
| Matriz de Fontes e Lacunas | `CASO-001-FONTES` | 0.2.1 | 15 fontes; obtenção empírica pendente |
| Documentos Técnicos e Contratações | `CASO-001-DOCUMENTOS-TECNICOS` | 0.1.0 | 8 fontes, 20 alegações e 7 grupos documentais pendentes |
| Protocolo de Geometria e Delimitação | `CASO-001-GEOMETRIA` | 0.2.0 | coleta hospedada bloqueada; feição pendente |
| Protocolo de Dados Pluviométricos | `CASO-001-DADOS-CHUVA` | 0.2.0 | processador sintético; série real pendente |

Nenhuma fonte foi classificada como obtida ou tratada para uso empírico. O novo registro técnico diferencia comunicação institucional, registro financeiro, orientação procedimental, índice de contratação e registro histórico.

## 5. Infraestrutura de validação e dados

| Recurso | Função |
|---|---|
| `scripts/generate_catalog.py` | gera catálogo nas seis camadas |
| `scripts/validate_metadata_graph.py` | valida campos, formatos, histórico, relações, substituições e ciclos |
| `scripts/validate_links.py` | valida destinos internos e âncoras |
| `scripts/validate_issue_forms.py` | valida formulários e template de pull request |
| `scripts/generate_validation_report.py` | produz relatório consolidado e inclui o registro de evidências técnicas |
| `scripts/validar_registro_documentos_tecnicos.py` | valida fontes, alegações, inconsistências, estados e exigência de hash |
| `casos/CASO-001_REGISTRO_DOCUMENTOS_TECNICOS.json` | registro estruturado de 8 fontes, 20 alegações, 3 inconsistências e 7 documentos requeridos |
| `tests/test_validar_registro_documentos_tecnicos.py` | testa classificação, hash e referências entre alegações |
| `scripts/processar_chuva_cemaden.py` | normaliza chuva, calcula hashes e produz manifesto e relatório |
| `scripts/coletar_geoinea_subbacia.py` | consulta metadados, IDs, atributos e GeoJSON |
| `scripts/coletar_geoinea_subbacia_ipv4.py` | executa a coleta local forçando IPv4 |
| `scripts/validar_geojson_subbacia.py` | valida GeoJSON, anéis, coordenadas, extensão, nome e proveniência |
| `.github/workflows/pages.yml` | valida documentação, evidências, chuva, geometria, catálogo e portal |

## 6. Regras de evidência incorporadas

A automação agora impede:

- comunicação institucional classificada como evidência financeira primária;
- fonte `obtida` ou `tratada` sem caminho local e SHA-256;
- identificadores duplicados de fonte, alegação, inconsistência ou documento requerido;
- inconsistência que referencie alegação inexistente;
- valor numérico sem unidade;
- URL de fonte sem HTTPS.

Essas verificações controlam estrutura e rastreabilidade. Não comprovam autenticidade, completude, mérito técnico, execução, entrega ou eficácia.

## 7. Validação automática

A CI verifica:

- campos, versões, estados, datas, compatibilidade e históricos;
- identificadores, dependências, reciprocidade, substituições e ciclos;
- links internos e âncoras;
- formulários, privacidade e template de pull request;
- registro de evidências técnicas e financeiras;
- pipeline pluviométrico com fixture sintético;
- coleta ArcGIS e transporte IPv4 com respostas controladas;
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

Arquivos integrais ainda não publicáveis devem permanecer em `work/caso-001/documentos-tecnicos/`, ignorado pelo Git, até revisão de licença, privacidade, integridade e necessidade de publicação.

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
| DD-046 | documentos técnicos integrais indisponíveis | aberta, alta | issue #7; inventário e lista REQ-001 a REQ-007 estruturados |
| DD-047 | participação e interlocutores não confirmados | aberta, alta | issue #8 |
| DD-048 | matriz de fontes dispersa | resolvida | `CASO-001-FONTES` |
| DD-049 | publicação acidental e retenção indefinida | controlada | `work/`, prazos, quarentena e descarte |
| DD-050 | pipeline de chuva sem teste | resolvida | `data/pipeline` |
| DD-051 | ausência de protocolo e validação geoespacial | resolvida | `CASO-001-GEOMETRIA` e `geodata/pipeline` |
| DD-052 | risco de confundir geosserviço com polígono obtido | controlada | estados e critérios explícitos |
| DD-053 | GeoINEA inacessível aos runners hospedados nas tentativas documentadas | aberta, controlada | coletor local, transporte IPv4 e workflow manual |
| DD-054 | risco de confundir anúncio, financiamento, contratação, projeto e execução | controlada | registro estruturado, classes de evidência e validação automática |

DD-046 permanece aberta: estruturar o inventário não equivale a obter os documentos integrais. DD-054 está controlada, mas só poderá ser considerada resolvida após uso consistente em casos posteriores.

## 10. Plano progressivo

| Fase | Tema | Estado |
|---|---|---|
| 0 a 4 | migração e cobertura | concluídas |
| 5 | catálogo e navegação | concluída |
| 6 | validação automática | concluída |
| 7 | estrutura física | concluída |
| 8 | primeiros casos e evidências | em execução |

## 11. Próxima ação

Obter e preservar os sete grupos documentais REQ-001 a REQ-007, começando pelo programa final, contratação da consultoria, termos e contratos de financiamento e anexos técnicos das três operações. Em paralelo, executar o coletor em rede que alcance o GeoINEA, coletar a série pluviométrica autorizada e formar capacidade de revisão antes de nova decisão do portão.

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
| 0.26.0 | 2026-07-18 | compatível | Coletor auditável, transporte IPv4, tentativas reais e dívida DD-053 | Projeto Pragmatismo Cívico |
| 0.27.0 | 2026-07-18 | compatível | Registro técnico estruturado, validação de evidências, dívida DD-054 e linha de base de 56 documentos | Projeto Pragmatismo Cívico |
