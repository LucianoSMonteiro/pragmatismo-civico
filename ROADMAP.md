---
id: GOV-002
titulo: Roadmap do Pragmatismo Cívico
versao: 0.15.0
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
  - ARQ-003
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# Roadmap do Pragmatismo Cívico

## Visão geral

Este roadmap organiza a evolução do Pragmatismo Cívico de uma base conceitual para um framework aberto, testável e aplicável em contextos reais.

Toda nova entrega deve preservar os princípios fundadores, resolver um problema demonstrável e evitar complexidade sem capacidade de manutenção.

## Fase 1 — Fundação conceitual

**Objetivo:** consolidar identidade, princípios, teoria, arquitetura e governança básica.

### Entregas

- [x] especificação, manifesto e carta de princípios;
- [x] framework de referência e teoria do Pragmatismo Cívico;
- [x] glossário;
- [x] modelo de governança;
- [x] arquitetura, inventário e decisão sobre a estrutura física;
- [x] código de conduta e guia de contribuição;
- [ ] revisão da adequação da licença.

### Critério de conclusão

Os documentos centrais devem ser coerentes, compreensíveis e capazes de orientar contribuições sem permitir alteração silenciosa dos princípios fundadores.

## Fase 2 — Metodologia aplicada

**Objetivo:** transformar princípios em padrões e instrumentos de uso prático.

### Entregas

- [x] ciclo operacional;
- [x] PPC-000, PPC-000A e PPC-META-001;
- [x] PPC-001 a PPC-008;
- [x] modelo e ficha de Teoria da Mudança;
- [x] fichas PPC-001 a PPC-008;
- [x] matriz de avaliação e estrutura de indicadores;
- [ ] ficha padrão de indicadores;
- [ ] protocolo de revisão periódica;
- [ ] checklist de transparência e rastreabilidade;
- [ ] modelo de relatório de decisão;
- [ ] protocolo de avaliação do próprio framework.

### Critério de conclusão

Uma equipe externa deve conseguir utilizar padrões e ferramentas sem depender de orientação informal dos autores.

## Fase 3 — Casos-piloto e validação

**Objetivo:** testar o framework em problemas concretos.

### Entregas

- [ ] seleção transparente de casos;
- [ ] aplicação completa do ciclo;
- [ ] publicação de dados, hipóteses e limitações;
- [ ] revisão independente;
- [ ] avaliação da utilidade e do custo metodológico;
- [ ] relatório de lições aprendidas;
- [ ] atualização do framework com base nos testes.

### Critério de conclusão

Ao menos três casos, em domínios distintos, devem produzir documentação auditável e evidências sobre a utilidade do método.

## Fase 4 — Comunidade e governança aberta

**Objetivo:** permitir evolução plural, organizada e íntegra.

### Entregas

- [x] ciclo de vida, metadados e versionamento;
- [x] migração e cobertura documental — Fases 1 a 4C;
- [x] catálogo e mapa de dependências — Fase 5;
- [x] validação automática — Fase 6;
- [x] decisão sobre a estrutura física — Fase 7;
- [x] processo formal de propostas de mudança — GOV-005;
- [x] ficha e formulário de issue para propostas;
- [x] política permanente de revisão e aprovação — GOV-006;
- [x] regras institucionais sobre conflitos, impedimentos e recusas;
- [x] registro de revisão e template de pull request;
- [ ] cadastro público e programa de revisores;
- [ ] fóruns de discussão pública;
- [ ] conselho consultivo plural.

### Critério de conclusão

O projeto deve receber, avaliar e incorporar contribuições sem perder coerência metodológica ou ser capturado por interesses particulares.

## Fase 5 — Plataforma pública

**Objetivo:** tornar o conhecimento acessível, verificável e reutilizável.

### Entregas

- [x] infraestrutura reproduzível do portal;
- [x] biblioteca navegável com 44 documentos;
- [x] catálogo e mapa de relações;
- [x] validação de metadados, grafo, links e catálogo;
- [x] validação dos templates de contribuição;
- [x] análise automática da estrutura física;
- [x] artefatos e status separados de CI;
- [ ] ativação inicial do GitHub Pages e primeiro deploy — issue #1;
- [ ] painel de indicadores demonstrativo;
- [ ] catálogo de estudos de caso;
- [ ] versões para impressão;
- [ ] Livro Base do Pragmatismo Cívico;
- [ ] materiais educativos;
- [ ] tradução para outros idiomas.

### Critério de conclusão

Cidadãos, gestores, pesquisadores e organizações devem conseguir localizar, compreender, verificar, baixar e aplicar os materiais com facilidade.

## Fase 6 — Rede de aplicação

**Objetivo:** apoiar experimentação em instituições e territórios.

### Entregas

- [ ] parcerias com universidades e centros de pesquisa;
- [ ] colaboração com organizações da sociedade civil;
- [ ] projetos com administrações públicas interessadas;
- [ ] formação de facilitadores;
- [ ] publicação de avaliações independentes;
- [ ] comunidade internacional de práticas.

## Governança de mudanças vigente

O GOV-005 estabelece:

- identificadores `PM-AAAA-NNN`;
- tipos e níveis de impacto;
- triagem e admissibilidade;
- fluxos simplificado, ordinário e reforçado;
- consulta pública, implementação, reversão e reconsideração.

O GOV-006 estabelece:

- separação entre secretaria, relatoria, revisão, decisão, implementação e verificação;
- competência, independência, conflitos, impedimentos e recusas;
- quórum e maiorias proporcionais ao impacto;
- limites do regime provisório;
- critérios para constituir uma instância plural permanente;
- decisões emergenciais e reconsideração.

A próxima evolução é criar um cadastro público de revisores elegíveis e testar a política em propostas reais, sem presumir que a instância plural já existe.

## Decisão arquitetural vigente

O ARQ-003 adotou uma estrutura híbrida:

- caminhos existentes permanecem estáveis;
- novas aplicações serão publicadas em `casos/`;
- relatórios oficiais serão publicados em `relatorios/`;
- a decisão será reavaliada após três casos, 60 documentos ou evidência de custo material da estrutura atual.

## Prioridades imediatas

1. criar o cadastro público e o programa de revisores;
2. selecionar e documentar o primeiro estudo de caso demonstrativo;
3. habilitar o GitHub Pages para GitHub Actions e confirmar o primeiro deploy — issue #1;
4. criar a ficha padrão de indicadores;
5. desenvolver o checklist de transparência e rastreabilidade;
6. estruturar o protocolo de avaliação do próprio framework;
7. revisar a licença;
8. preparar versões para impressão.

## Controle de coerência

Antes de iniciar uma entrega, deve-se verificar:

1. qual princípio fundador ela concretiza;
2. qual problema prático resolve;
3. se já existe documento com a mesma função;
4. se simplifica ou complica a aplicação;
5. quais documentos relacionados devem mudar;
6. impactos sobre direitos, transparência, auditabilidade e neutralidade;
7. como sua utilidade poderá ser testada;
8. qual custo metodológico introduz.

## Princípios de execução

- avançar em etapas verificáveis;
- documentar decisões;
- testar antes de escalar;
- declarar limitações;
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
| 0.11.0 | 2026-07-18 | compatível | Conclusão da Fase 5 e promoção da validação automática | Projeto Pragmatismo Cívico |
| 0.12.0 | 2026-07-18 | compatível | Conclusão da Fase 6 e relatório persistente | Projeto Pragmatismo Cívico |
| 0.13.0 | 2026-07-18 | compatível | Conclusão da Fase 7 e decisão pela estrutura híbrida | Projeto Pragmatismo Cívico |
| 0.14.0 | 2026-07-18 | compatível | Publicação do GOV-005, da ficha, do formulário e da validação de issue forms | Projeto Pragmatismo Cívico |
| 0.15.0 | 2026-07-18 | compatível | Publicação do GOV-006, do registro de revisão e do template de pull request | Projeto Pragmatismo Cívico |
