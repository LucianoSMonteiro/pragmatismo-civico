---
id: GOV-002
titulo: Roadmap do Pragmatismo Cívico
versao: 0.22.0
status: rascunho
tipo: governanca
idioma: pt-BR
data_criacao: null
data_versao: 2026-07-18
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - FRAMEWORK-DE-REFERENCIA
  - GOV-001
  - PPC-000
  - PPC-000A
  - PPC-META-001
  - ARQ-001
  - ARQ-002
produz_entrada_para: []
relaciona_se_com:
  - GOV-003
  - GOV-004
  - GOV-005
  - GOV-006
  - GOV-007
  - GOV-008
  - ARQ-003
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

# Roadmap do Pragmatismo Cívico

## Visão geral

Este roadmap organiza a evolução do Pragmatismo Cívico de uma base conceitual para um framework aberto, testável e aplicável em contextos reais.

Toda entrega deve preservar os princípios fundadores, resolver problema demonstrável e evitar complexidade sem capacidade de manutenção.

## Fase 1 — Fundação conceitual

**Objetivo:** consolidar identidade, princípios, teoria, arquitetura e governança básica.

- [x] especificação, manifesto e carta de princípios;
- [x] framework de referência e teoria;
- [x] glossário e modelo de governança;
- [x] arquitetura, inventário e decisão sobre estrutura física;
- [x] código de conduta e guia de contribuição;
- [ ] revisão da adequação da licença.

## Fase 2 — Metodologia aplicada

**Objetivo:** transformar princípios em padrões e instrumentos práticos.

- [x] ciclo operacional e PPC-000;
- [x] PPC-001 a PPC-008;
- [x] Teoria da Mudança e ficha;
- [x] fichas PPC-001 a PPC-008;
- [x] matriz e estrutura de indicadores;
- [ ] ficha padrão de indicadores;
- [ ] protocolo de revisão periódica;
- [ ] checklist de transparência e rastreabilidade;
- [ ] modelo de relatório de decisão;
- [ ] protocolo de avaliação do framework.

## Fase 3 — Casos-piloto e validação

**Objetivo:** testar o framework em problemas concretos.

### Entregas concluídas

- [x] protocolo e ficha de seleção e condução de casos — GOV-008 e FICHA-GOV-008;
- [x] índice público da camada de aplicações e evidências;
- [x] seleção do CASO-001 e recorte preliminar da sub-bacia de Itapeba;
- [x] período preliminar de 2022-01-01 a 2026-06-30;
- [x] decisão motivada de manter o caso em preparação;
- [x] matriz canônica de 15 fontes, estados de obtenção e lacunas;
- [x] processador e protocolo pluviométrico com testes sintéticos;
- [x] camada poligonal candidata, protocolo, coletor e validador geoespacial;
- [x] tentativas reais de conexão ao GeoINEA e registro da limitação dos runners;
- [x] inventário estruturado de 8 fontes técnicas e financeiras;
- [x] 20 alegações identificadas, 3 inconsistências e 7 grupos documentais requeridos;
- [x] validador que separa comunicação, financiamento, contratação, projeto e execução;
- [x] validação automática de caminho e SHA-256 para fontes obtidas ou tratadas;
- [x] estados separados `data/pipeline` e `geodata/pipeline`.

### Entregas pendentes

- [ ] consultar e preservar a feição oficial de Itapeba — issue #6;
- [ ] obter programa final, contrato da consultoria e produtos intermediários — issue #7;
- [ ] obter cartas-consulta, termos e contratos das três operações do Novo PAC — issue #7;
- [ ] obter projetos, anteprojetos, QCI, mapas de risco, geometrias e relatórios fotográficos — issue #7;
- [ ] obter edital, termo de referência e anexos do Pregão 14/2026 — issue #7;
- [ ] obter cronogramas, medições, indicadores e relatórios de execução — issue #7;
- [ ] reconciliar beneficiários e nomes territoriais — issue #7;
- [ ] baixar mensalmente e revisar a série pluviométrica real — issue #4;
- [ ] confirmar interlocutores e plano participativo local — issue #8;
- [ ] obter capacidade de revisão compatível — issue #9;
- [ ] aprovar, suspender ou encerrar o portão de prontidão — issue #2;
- [ ] aplicar o PPC-001 somente após aprovação do portão;
- [ ] publicar relatório de lições aprendidas e atualizar o framework.

O CASO-001 continua em preparação. Inventário estruturado, notícia oficial e índice de licitação não equivalem a programa final, contrato, projeto, medição ou resultado. Nenhuma série real, feição oficial ou documento técnico integral foi incorporado como evidência.

### Critério de conclusão

Ao menos três casos, em domínios distintos, devem produzir documentação auditável e evidências sobre utilidade e limites do método.

## Fase 4 — Comunidade e governança aberta

**Objetivo:** permitir evolução plural, organizada e íntegra.

- [x] ciclo de vida, metadados e versionamento;
- [x] migração, catálogo, validação automática e decisão estrutural;
- [x] processo formal de propostas — GOV-005;
- [x] política de revisão e aprovação — GOV-006;
- [x] programa e cadastro público de revisores — GOV-007;
- [x] protocolo de casos demonstrativos — GOV-008;
- [ ] primeira chamada pública e primeiras admissões — issue #3;
- [ ] fóruns de discussão pública;
- [ ] instância plural permanente.

## Fase 5 — Plataforma pública

**Objetivo:** tornar o conhecimento acessível, verificável e reutilizável.

- [x] infraestrutura reproduzível do portal;
- [x] biblioteca navegável com 56 documentos;
- [x] catálogo e mapa de relações nas seis camadas;
- [x] índice público de casos e evidências;
- [x] validação de metadados, grafo, links e catálogo;
- [x] validação de formulários, privacidade e template de pull request;
- [x] validação do registro estruturado de evidências técnicas;
- [x] análise automática da estrutura física;
- [x] artefatos e estados separados de CI;
- [x] testes dos pipelines pluviométrico e geoespacial;
- [ ] ativação inicial do GitHub Pages e primeiro deploy — issue #1;
- [ ] painel de indicadores demonstrativo;
- [ ] versões para impressão;
- [ ] Livro Base, materiais educativos e traduções.

## Fase 6 — Rede de aplicação

**Objetivo:** apoiar experimentação em instituições e territórios.

- [ ] parcerias com universidades e centros de pesquisa;
- [ ] colaboração com organizações da sociedade civil;
- [ ] projetos com administrações públicas;
- [ ] formação de facilitadores;
- [ ] avaliações independentes;
- [ ] comunidade internacional de práticas.

## Governança e arquitetura vigentes

GOV-005 governa propostas; GOV-006, revisão e aprovação; GOV-007, revisores; GOV-008, seleção e condução de casos.

O cadastro público de revisores permanece vazio. Isso impede alegação de revisão independente e mantém o portão em preparação.

O ARQ-003 preserva caminhos existentes, direciona aplicações para `casos/`, relatórios para `relatorios/` e arquivos locais ainda não publicáveis para `work/`. A decisão será revista após três casos, 60 documentos ou evidência de custo material.

## Prioridades imediatas

1. obter REQ-001 e REQ-002: programa final, produtos e contratação da consultoria — issue #7;
2. obter REQ-003 a REQ-005: propostas, contratos, projetos e geometrias do Novo PAC — issue #7;
3. obter REQ-006 e REQ-007: documentos do Smart Drainage, cronogramas, medições e indicadores — issue #7;
4. executar o coletor GeoINEA em rede que alcance o serviço — issue #6;
5. executar downloads mensais autorizados da estação Itapeba — issue #4;
6. confirmar interlocutores e participação local — issue #8;
7. realizar a primeira chamada pública de revisores — issue #3;
8. obter revisão técnica compatível — issue #9;
9. emitir nova decisão do portão — issue #2;
10. habilitar o GitHub Pages — issue #1;
11. criar a ficha padrão de indicadores;
12. desenvolver o checklist de transparência e revisar a licença.

## Controle de coerência

Antes de iniciar uma entrega, verificar princípio concretizado, problema resolvido, possível duplicação, simplicidade, relações documentais, direitos, transparência, forma de teste, custo metodológico e capacidade real de revisão.

## Princípios de execução

- avançar em etapas verificáveis;
- documentar decisões e limitações;
- testar antes de escalar;
- preservar memória institucional;
- evitar crescimento sem capacidade;
- rejeitar complexidade sem utilidade;
- preservar os princípios fundadores.

## Versionamento sugerido do framework

- `0.1` — fundação conceitual;
- `0.2` — padrões e ferramentas iniciais;
- `0.3` — primeiros casos-piloto;
- `0.4` — governança comunitária;
- `0.5` — portal e biblioteca pública;
- `1.0` — framework estável, testado e documentado.

## Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 a 0.10.0 | 2026-07-17 a 2026-07-18 | compatível | Migração e cobertura progressiva do acervo | Projeto Pragmatismo Cívico |
| 0.11.0 a 0.13.0 | 2026-07-18 | compatível | Conclusão das fases de catálogo, validação e estrutura física | Projeto Pragmatismo Cívico |
| 0.14.0 a 0.17.0 | 2026-07-18 | compatível | Publicação de GOV-005 a GOV-008 e seleção do CASO-001 | Projeto Pragmatismo Cívico |
| 0.18.0 | 2026-07-18 | compatível | Recorte de Itapeba e decisão de manter o portão fechado | Projeto Pragmatismo Cívico |
| 0.19.0 | 2026-07-18 | compatível | Pipeline pluviométrico e linha de base de 53 documentos | Projeto Pragmatismo Cívico |
| 0.20.0 | 2026-07-18 | compatível | Matriz de fontes e linha de base de 54 documentos | Projeto Pragmatismo Cívico |
| 0.21.0 | 2026-07-18 | compatível | Protocolo geoespacial, coletor e linha de base de 55 documentos | Projeto Pragmatismo Cívico |
| 0.22.0 | 2026-07-18 | compatível | Registro técnico, controles de evidência e linha de base de 56 documentos | Projeto Pragmatismo Cívico |
