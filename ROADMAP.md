---
id: GOV-002
titulo: Roadmap do Pragmatismo Cívico
versao: 0.13.0
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
- [ ] processo formal de propostas de mudança;
- [ ] política de revisão e aprovação;
- [ ] regras sobre conflitos de interesse;
- [ ] fóruns de discussão pública;
- [ ] programa de colaboradores e revisores;
- [ ] conselho consultivo plural.

### Critério de conclusão

O projeto deve receber, avaliar e incorporar contribuições sem perder coerência metodológica ou ser capturado por interesses particulares.

## Fase 5 — Plataforma pública

**Objetivo:** tornar o conhecimento acessível, verificável e reutilizável.

### Entregas

- [x] infraestrutura reproduzível do portal;
- [x] biblioteca navegável com 40 documentos;
- [x] catálogo e mapa de relações;
- [x] validação de metadados, grafo, links e catálogo;
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

## Decisão arquitetural vigente

O ARQ-003 adotou uma estrutura híbrida:

- caminhos existentes permanecem estáveis;
- novas aplicações serão publicadas em `casos/`;
- relatórios oficiais serão publicados em `relatorios/`;
- a decisão será reavaliada após três casos, 60 documentos ou evidência de custo material da estrutura atual.

## Prioridades imediatas

1. formalizar o processo de propostas de mudança;
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
| 0.1.0 | 2026-07-17 | inicial | Migração documental e registro da Fase 1 | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-17 | compatível | Conclusão da Fase 2A | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-17 | compatível | Conclusão da Fase 2B | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-17 | compatível | Conclusão da Fase 2C | Projeto Pragmatismo Cívico |
| 0.5.0 | 2026-07-17 | compatível | Conclusão da Fase 3A | Projeto Pragmatismo Cívico |
| 0.6.0 | 2026-07-18 | compatível | Conclusão da Fase 3B | Projeto Pragmatismo Cívico |
| 0.7.0 | 2026-07-18 | compatível | Conclusão da Fase 3C | Projeto Pragmatismo Cívico |
| 0.8.0 | 2026-07-18 | compatível | Conclusão da Fase 4A | Projeto Pragmatismo Cívico |
| 0.9.0 | 2026-07-18 | compatível | Conclusão da Fase 4B | Projeto Pragmatismo Cívico |
| 0.10.0 | 2026-07-18 | compatível | Conclusão da Fase 4C e cobertura dos 38 documentos | Projeto Pragmatismo Cívico |
| 0.11.0 | 2026-07-18 | compatível | Conclusão da Fase 5 e promoção da validação automática | Projeto Pragmatismo Cívico |
| 0.12.0 | 2026-07-18 | compatível | Conclusão da Fase 6 | Projeto Pragmatismo Cívico |
| 0.13.0 | 2026-07-18 | compatível | Conclusão da Fase 7, adoção da estrutura híbrida e promoção da governança de mudanças | Projeto Pragmatismo Cívico |
