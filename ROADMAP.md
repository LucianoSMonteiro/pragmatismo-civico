---
id: GOV-002
titulo: Roadmap do Pragmatismo Cívico
versao: 0.21.0
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

### Entregas

- [x] especificação, manifesto e carta de princípios;
- [x] framework de referência e teoria;
- [x] glossário e modelo de governança;
- [x] arquitetura, inventário e decisão sobre estrutura física;
- [x] código de conduta e guia de contribuição;
- [ ] revisão da adequação da licença.

## Fase 2 — Metodologia aplicada

**Objetivo:** transformar princípios em padrões e instrumentos práticos.

### Entregas

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

### Entregas

- [x] protocolo de seleção e condução de casos — GOV-008;
- [x] ficha de seleção, prontidão e condução — FICHA-GOV-008;
- [x] índice público da camada de aplicações e evidências;
- [x] seleção do primeiro caso — CASO-001;
- [x] recorte preliminar para a sub-bacia de Itapeba;
- [x] período preliminar de 2022-01-01 a 2026-06-30;
- [x] decisão motivada de manter o caso em preparação;
- [x] matriz canônica de 15 fontes, estados de obtenção e lacunas;
- [x] processador reproduzível de chuva, manifesto, relatório e teste sintético;
- [x] protocolo de aquisição, qualidade, retenção e descarte pluviométrico;
- [x] identificação de camada poligonal de sub-bacias e hidrografia RJ25 no GeoINEA;
- [x] protocolo de aquisição, validação e delimitação geoespacial;
- [x] validador GeoJSON, manifesto, relatório e testes sintéticos;
- [x] estados separados `data/pipeline` e `geodata/pipeline`;
- [ ] consultar e preservar a feição oficial de Itapeba — issue #6;
- [ ] obter produtos técnicos, projetos, geometrias e cronogramas — issue #7;
- [ ] baixar mensalmente e revisar a série pluviométrica real — issue #4;
- [ ] confirmar interlocutores e plano participativo local — issue #8;
- [ ] obter capacidade de revisão compatível — issue #9;
- [ ] aprovar, suspender ou encerrar o portão de prontidão — issue #2;
- [ ] aplicar o PPC-001 somente após aprovação do portão;
- [ ] aplicar o ciclo completo quando proporcional e viável;
- [ ] publicar dados, hipóteses e limitações;
- [ ] avaliar utilidade e custo metodológico;
- [ ] publicar relatório de lições aprendidas;
- [ ] atualizar o framework com base nos testes.

O CASO-001 continua em preparação. A localização de um geosserviço oficial e a aprovação do validador sintético não equivalem à obtenção do polígono. Nenhuma série real, feição oficial ou documento técnico integral foi incorporado como evidência.

### Critério de conclusão

Ao menos três casos, em domínios distintos, devem produzir documentação auditável e evidências sobre utilidade e limites do método.

## Fase 4 — Comunidade e governança aberta

**Objetivo:** permitir evolução plural, organizada e íntegra.

### Entregas

- [x] ciclo de vida, metadados e versionamento;
- [x] migração e cobertura documental;
- [x] catálogo, validação automática e decisão estrutural;
- [x] processo formal de propostas — GOV-005;
- [x] política de revisão e aprovação — GOV-006;
- [x] regras de conflitos, impedimentos, recusas e quórum;
- [x] registro de revisão e template de pull request;
- [x] programa e cadastro público de revisores — GOV-007;
- [x] ficha e formulário de candidatura;
- [x] protocolo de casos demonstrativos — GOV-008;
- [ ] primeira chamada pública e primeiras admissões — issue #3;
- [ ] fóruns de discussão pública;
- [ ] instância plural permanente.

### Critério de conclusão

O projeto deve receber, revisar e incorporar contribuições sem perder coerência, ocultar insuficiência de capacidade ou ser capturado por interesses particulares.

## Fase 5 — Plataforma pública

**Objetivo:** tornar o conhecimento acessível, verificável e reutilizável.

### Entregas

- [x] infraestrutura reproduzível do portal;
- [x] biblioteca navegável com 55 documentos;
- [x] catálogo e mapa de relações nas seis camadas;
- [x] índice público de casos e evidências;
- [x] validação de metadados, grafo, links e catálogo;
- [x] validação dos formulários e template de pull request;
- [x] salvaguardas de privacidade na candidatura pública;
- [x] análise automática da estrutura física;
- [x] artefatos e estados separados de CI;
- [x] teste sintético e artefato do pipeline pluviométrico;
- [x] teste sintético e artefato do pipeline geoespacial;
- [ ] ativação inicial do GitHub Pages e primeiro deploy — issue #1;
- [ ] painel de indicadores demonstrativo;
- [ ] versões para impressão;
- [ ] Livro Base;
- [ ] materiais educativos;
- [ ] traduções.

## Fase 6 — Rede de aplicação

**Objetivo:** apoiar experimentação em instituições e territórios.

### Entregas

- [ ] parcerias com universidades e centros de pesquisa;
- [ ] colaboração com organizações da sociedade civil;
- [ ] projetos com administrações públicas;
- [ ] formação de facilitadores;
- [ ] avaliações independentes;
- [ ] comunidade internacional de práticas.

## Governança vigente

O GOV-005 governa proposta, triagem, consulta, implementação e reconsideração.

O GOV-006 governa funções, competência, independência, conflitos, quórum, decisão e verificação.

O GOV-007 governa candidatura, elegibilidade, disponibilidade, proteção de dados, formação de painéis e manutenção do cadastro.

O GOV-008 governa seleção, prontidão, condução, publicação, suspensão e encerramento de casos.

O cadastro público de revisores permanece vazio. Isso impede que o CASO-001 alegue revisão independente e mantém o portão em preparação.

## Decisão arquitetural vigente

O ARQ-003 preserva caminhos existentes, direciona aplicações para `casos/`, relatórios para `relatorios/` e arquivos locais ainda não publicáveis para `work/`, ignorado pelo Git. A decisão será revista após três casos, 60 documentos ou evidência de custo material.

## Prioridades imediatas

1. consultar a camada `GPL_SUBBACIAS_ERJ_50`, preservar a resposta e confirmar ou refutar a correspondência com Itapeba — issue #6;
2. obter recorte da hidrografia RJ25 para conferência topológica — issue #6;
3. executar os downloads mensais autorizados da estação Itapeba — issue #4;
4. obter produtos técnicos do Programa Municipal de Drenagem e das intervenções — issue #7;
5. confirmar interlocutores e participação local — issue #8;
6. realizar a primeira chamada pública de revisores — issue #3;
7. obter revisão técnica compatível — issue #9;
8. emitir nova decisão do portão — issue #2;
9. habilitar o GitHub Pages — issue #1;
10. criar a ficha padrão de indicadores;
11. desenvolver o checklist de transparência e rastreabilidade;
12. estruturar o protocolo de avaliação do framework;
13. revisar a licença.

## Controle de coerência

Antes de iniciar uma entrega, verificar:

1. princípio fundador concretizado;
2. problema prático resolvido;
3. possível duplicação;
4. efeito sobre simplicidade e aplicação;
5. documentos relacionados;
6. direitos, transparência e neutralidade;
7. forma de teste;
8. custo metodológico;
9. capacidade real de revisão e manutenção.

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
| 0.11.0 | 2026-07-18 | compatível | Conclusão da Fase 5 | Projeto Pragmatismo Cívico |
| 0.12.0 | 2026-07-18 | compatível | Conclusão da Fase 6 | Projeto Pragmatismo Cívico |
| 0.13.0 | 2026-07-18 | compatível | Conclusão da Fase 7 | Projeto Pragmatismo Cívico |
| 0.14.0 | 2026-07-18 | compatível | Publicação do GOV-005 e instrumentos | Projeto Pragmatismo Cívico |
| 0.15.0 | 2026-07-18 | compatível | Publicação do GOV-006 e instrumentos | Projeto Pragmatismo Cívico |
| 0.16.0 | 2026-07-18 | compatível | Publicação do GOV-007 e instrumentos | Projeto Pragmatismo Cívico |
| 0.17.0 | 2026-07-18 | compatível | Publicação do GOV-008 e seleção preparatória do CASO-001 | Projeto Pragmatismo Cívico |
| 0.18.0 | 2026-07-18 | compatível | Recorte de Itapeba, inventário de fontes e decisão de manter o portão fechado | Projeto Pragmatismo Cívico |
| 0.19.0 | 2026-07-18 | compatível | Pipeline pluviométrico reproduzível, protocolo público e linha de base de 53 documentos | Projeto Pragmatismo Cívico |
| 0.20.0 | 2026-07-18 | compatível | Matriz canônica de fontes, política de retenção e linha de base de 54 documentos | Projeto Pragmatismo Cívico |
| 0.21.0 | 2026-07-18 | compatível | Geosserviços candidatos, protocolo geoespacial, validador GeoJSON e linha de base de 55 documentos | Projeto Pragmatismo Cívico |
