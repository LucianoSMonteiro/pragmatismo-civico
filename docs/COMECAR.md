---
id: GUIA-COMECAR
titulo: Começar no Pragmatismo Cívico
versao: 0.7.0
status: rascunho
tipo: guia
idioma: pt-BR
data_criacao: null
data_versao: 2026-07-18
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - FRAMEWORK-DE-REFERENCIA
  - CICLO-PC-001
  - ARQ-001
  - PPC-META-001
produz_entrada_para: []
relaciona_se_com:
  - PORTAL-INICIO
  - CATALOGO-DOCUMENTAL
  - ARQ-003
  - GOV-005
  - GOV-006
  - PPC-000
  - GOV-003
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# Começar

O Pragmatismo Cívico é um framework aberto para governança e decisões de interesse público baseadas em evidências, transparência, responsabilidade e aprendizado contínuo.

Esta página oferece rotas curtas para diferentes objetivos. A profundidade da aplicação deve ser proporcional ao impacto, ao risco, à incerteza e à reversibilidade da decisão.

Para localizar versões, estados, caminhos e relações, consulte o [Catálogo Documental](../CATALOGO_DOCUMENTAL.md).

## Quero entender o projeto

Leia, nesta ordem:

1. [Carta de Princípios](../CARTA_DE_PRINCIPIOS.md);
2. [Especificação](../SPECIFICATION.md);
3. [Framework de Referência](../FRAMEWORK_DE_REFERENCIA.md);
4. [Teoria do Pragmatismo Cívico](../TEORIA_DO_PRAGMATISMO_CIVICO.md);
5. [Manifesto](../MANIFESTO.md);
6. [Glossário](../GLOSSARIO.md).

## Quero aplicar o método

Leia primeiro o [Ciclo do Pragmatismo Cívico](../CICLO_DO_PRAGMATISMO_CIVICO.md).

| Etapa | Padrão ou modelo | Ferramenta principal |
|---|---|---|
| Diagnosticar | [PPC-001](../PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md) | [Ficha PPC-001](../FICHA_PPC-001_DIAGNOSTICO_DE_PROBLEMA_PUBLICO.md) |
| Formular alternativas | [PPC-002](../PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md) | [Ficha PPC-002](../FICHA_PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md) e [Matriz](../MATRIZ_DE_AVALIACAO_DE_POLITICAS_PUBLICAS.md) |
| Avaliar tecnicamente | [PPC-003](../PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md) | [Ficha PPC-003](../FICHA_PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md) |
| Decidir e justificar | [PPC-004](../PPC-004_DECISAO_E_JUSTIFICATIVA.md) | [Ficha PPC-004](../FICHA_PPC-004_DECISAO_E_JUSTIFICATIVA.md) |
| Explicitar a lógica causal | [Teoria da Mudança](../MODELO_DE_TEORIA_DA_MUDANCA.md) | [Ficha de Teoria da Mudança](../FICHA_TEORIA_DA_MUDANCA.md) |
| Implementar | [PPC-005](../PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md) | [Ficha PPC-005](../FICHA_PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md) |
| Monitorar | [PPC-006](../PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md) | [Ficha PPC-006](../FICHA_PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md) e [Indicadores](../INDICADORES.md) |
| Avaliar resultados | [PPC-007](../PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md) | [Ficha PPC-007](../FICHA_PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md) |
| Aprender e melhorar | [PPC-008](../PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md) | [Ficha PPC-008](../FICHA_PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md) |

!!! note "Regra mínima"
    Nenhuma alternativa deve ser tratada como solução preferencial antes de ser comparada com opções viáveis e com o cenário de não intervenção.

## Quero compreender a governança documental

A leitura recomendada é:

1. [PPC-000](../PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md) — estrutura do ecossistema;
2. [PPC-000A](../PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md) — estados e transições;
3. [PPC-META-001](../PPC-META-001_METADADOS_E_VERSIONAMENTO.md) — metadados e versões;
4. [GOV-005](../GOV-005_PROCESSO_DE_PROPOSTAS_DE_MUDANCA.md) — identificação, triagem e ciclo das propostas;
5. [GOV-006](../GOV-006_POLITICA_DE_REVISAO_E_APROVACAO.md) — competência, independência, quórum e decisão;
6. [ARQ-001](../ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md) — camadas e relações;
7. [ARQ-002](../ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md) — cobertura, validação e dívida;
8. [ARQ-003](../ARQ-003_DECISAO_SOBRE_A_ESTRUTURA_FISICA_DO_REPOSITORIO.md) — caminhos e estrutura híbrida;
9. [Catálogo Documental](../CATALOGO_DOCUMENTAL.md) — visão consolidada.

## Quero propor e revisar uma mudança

Use:

- [GOV-005 — Processo de Propostas de Mudança](../GOV-005_PROCESSO_DE_PROPOSTAS_DE_MUDANCA.md);
- [Ficha GOV-005](../FICHA_GOV-005_PROPOSTA_DE_MUDANCA.md);
- [GOV-006 — Política de Revisão e Aprovação](../GOV-006_POLITICA_DE_REVISAO_E_APROVACAO.md);
- [Registro GOV-006](../FICHA_GOV-006_REGISTRO_DE_REVISAO_E_APROVACAO.md);
- formulário **Proposta de mudança** nas issues;
- template de pull request;
- [Guia de Contribuição](../CONTRIBUTING.md).

Uma proposta formal deve registrar:

- problema demonstrado;
- tipo e impacto;
- evidências e alternativas;
- princípios e documentos afetados;
- riscos, direitos e salvaguardas;
- compatibilidade e migração;
- conflitos de interesse;
- implementação, verificação e reversão.

A revisão deve registrar composição, competência, independência, impedimentos, quórum, votos, fundamentos, condições e dissensos.

A issue registra a proposta. O pull request implementa a decisão e não substitui revisão, quórum ou justificativa pública.

## Regime provisório de aprovação

A política permanente está publicada, mas a instância plural ainda não foi constituída. Enquanto isso:

- mudanças de baixo impacto podem ser mantidas pelos responsáveis atuais com revisão proporcional;
- propostas moderadas exigem ao menos duas manifestações fundamentadas;
- propostas altas não avançam para estabilidade sem o painel mínimo;
- propostas críticas ou fundacionais não podem produzir alteração definitiva do núcleo sem o quórum permanente;
- limitações e acumulações de função devem ser publicadas.

## Estrutura física vigente

Os caminhos dos documentos existentes foram preservados porque uma migração por camada afetaria quase todo o grafo documental sem melhorar a navegação pública.

O crescimento futuro seguirá a estrutura híbrida:

- aplicações em `casos/`;
- relatórios em `relatorios/`;
- automações em `scripts/`;
- ativos em `docs/assets/`.

## Estado atual

O acervo navegável contém 44 documentos identificados, versionados, catalogados e validados automaticamente. O processo de propostas e a política de revisão estão publicados como rascunhos operacionais. A instância plural permanente e o cadastro público de revisores ainda são pendências. Também não há estudo de caso oficial nem validação empírica suficiente para declarar estabilidade. O deploy público aguarda a ativação inicial do GitHub Pages registrada na issue #1.

## Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Migração documental para o PPC-META-001 | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Cobertura do ciclo completo e correção da governança dos padrões | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Integração do catálogo e atualização para 39 documentos | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-18 | compatível | Registro da conclusão da validação automática | Projeto Pragmatismo Cívico |
| 0.5.0 | 2026-07-18 | compatível | Inclusão do ARQ-003 e atualização para 40 documentos | Projeto Pragmatismo Cívico |
| 0.6.0 | 2026-07-18 | compatível | Inclusão do GOV-005, da ficha, do formulário e atualização para 42 documentos | Projeto Pragmatismo Cívico |
| 0.7.0 | 2026-07-18 | compatível | Inclusão do GOV-006, do registro de revisão, do template de pull request e atualização para 44 documentos | Projeto Pragmatismo Cívico |
