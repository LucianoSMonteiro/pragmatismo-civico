---
id: GUIA-COMECAR
titulo: Começar no Pragmatismo Cívico
versao: 0.4.0
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

Comece pelo [Framework de Referência](../FRAMEWORK_DE_REFERENCIA.md).

Depois consulte:

1. [Carta de Princípios](../CARTA_DE_PRINCIPIOS.md);
2. [Especificação](../SPECIFICATION.md);
3. [Teoria do Pragmatismo Cívico](../TEORIA_DO_PRAGMATISMO_CIVICO.md);
4. [Manifesto](../MANIFESTO.md);
5. [Glossário](../GLOSSARIO.md).

## Quero aplicar o método

Leia primeiro o [Ciclo do Pragmatismo Cívico](../CICLO_DO_PRAGMATISMO_CIVICO.md).

| Etapa | Padrão ou modelo | Ferramenta principal |
|---|---|---|
| Diagnosticar | [PPC-001](../PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md) | [Ficha PPC-001](../FICHA_PPC-001_DIAGNOSTICO_DE_PROBLEMA_PUBLICO.md) |
| Formular alternativas | [PPC-002](../PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md) | [Ficha PPC-002](../FICHA_PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md) e [Matriz](../MATRIZ_DE_AVALIACAO_DE_POLITICAS_PUBLICAS.md) |
| Avaliar tecnicamente | [PPC-003](../PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md) | [Ficha PPC-003](../FICHA_PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md) |
| Decidir e justificar | [PPC-004](../PPC-004_DECISAO_E_JUSTIFICATIVA.md) | [Ficha PPC-004](../FICHA_PPC-004_DECISAO_E_JUSTIFICATIVA.md) |
| Explicitar a lógica causal | [Teoria da Mudança](../MODELO_DE_TEORIA_DA_MUDANCA.md) | [Ficha de Teoria da Mudança](../FICHA_TEORIA_DA_MUDANCA.md) |
| Implementar e adaptar | [PPC-005](../PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md) | [Ficha PPC-005](../FICHA_PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md) |
| Monitorar | [PPC-006](../PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md) | [Ficha PPC-006](../FICHA_PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md) e [Indicadores](../INDICADORES.md) |
| Avaliar resultados | [PPC-007](../PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md) | [Ficha PPC-007](../FICHA_PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md) |
| Aprender e melhorar | [PPC-008](../PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md) | [Ficha PPC-008](../FICHA_PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md) |

!!! note "Regra mínima"
    Nenhuma alternativa deve ser tratada como preferencial antes de ser comparada com opções viáveis e com a não intervenção. Toda decisão deve registrar evidências, riscos, hipóteses, limitações e critérios de revisão.

## Quero estudar a governança dos padrões

A leitura recomendada é:

1. [PPC-000](../PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md);
2. [PPC-000A](../PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md);
3. [PPC-META-001](../PPC-META-001_METADADOS_E_VERSIONAMENTO.md);
4. [ARQ-001](../ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md);
5. [ARQ-002](../ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md);
6. [Catálogo Documental](../CATALOGO_DOCUMENTAL.md).

## Como o acervo é validado

A automação executada na branch padrão:

- valida campos, versões, estados, datas e compatibilidade;
- verifica histórico, dependências, substituições e ciclos;
- verifica links internos e âncoras;
- compara o catálogo publicado com a geração atual;
- produz relatório preservado como artefato;
- executa o build estrito do portal.

Os status `documentation/validation` e `portal/build` permitem distinguir falhas documentais de falhas de compilação.

## Quero contribuir

Consulte o [Guia de Contribuição](../CONTRIBUTING.md), o [Código de Conduta](../CODE_OF_CONDUCT.md) e o [Roadmap](../ROADMAP.md).

Toda contribuição deve declarar:

- o problema concreto que pretende resolver;
- os princípios que coloca em prática;
- como sua utilidade poderá ser avaliada;
- os riscos de complexidade, captura ou descaracterização;
- as relações com documentos existentes.

## Estado atual

Os 39 documentos públicos estão identificados, versionados, catalogados e validados automaticamente. O deploy aguarda a ativação inicial do GitHub Pages na issue #1. Ainda não há estudo de caso oficial nem validação empírica suficiente para declarar o framework estável.

## Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Migração documental preservando rotas e orientações | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Cobertura do ciclo completo e correção da governança dos padrões | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Integração do catálogo e atualização para 39 documentos | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-18 | compatível | Registro da conclusão da Fase 6 e explicação da validação automática | Projeto Pragmatismo Cívico |
