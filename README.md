<!--
---
id: PORTAL-INICIO
titulo: Pragmatismo Cívico — Página inicial
versao: 0.2.0
status: rascunho
tipo: publicacao
idioma: pt-BR
data_criacao: null
data_versao: 2026-07-18
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - FRAMEWORK-DE-REFERENCIA
  - ARQ-001
  - ARQ-002
  - GOV-002
produz_entrada_para: []
relaciona_se_com:
  - GUIA-COMECAR
  - CICLO-PC-001
  - GOV-003
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---
-->

<div class="pc-hero" markdown>

# Pragmatismo Cívico

<p class="pc-tagline">Decidir com evidências. Agir com responsabilidade. Aprender continuamente.</p>

O **Pragmatismo Cívico** é um framework aberto para governança e decisões de interesse público. Ele organiza princípios, governança, métodos, ferramentas e evidências de aplicação para melhorar a qualidade das decisões por meio de transparência, responsabilidade, sustentabilidade, cooperação e aprendizado contínuo.

[Começar agora](docs/COMECAR.md){ .md-button .md-button--primary }
[Explorar o método](CICLO_DO_PRAGMATISMO_CIVICO.md){ .md-button }

</div>

<div class="pc-status" markdown>

**Estado atual:** desenvolvimento aberto. O ciclo metodológico completo — PPC-001 a PPC-008 —, a Teoria da Mudança, suas fichas práticas e os padrões de governança documental estão publicados para revisão, teste e aplicação experimental. Os 38 documentos da navegação canônica possuem identificação e versionamento documental. A migração mínima de metadados foi concluída, mas ainda não há estudo de caso oficial publicado nem validação empírica suficiente para declarar o framework estável.

</div>

## Escolha seu caminho

<div class="pc-grid" markdown>

<div class="pc-card" markdown>

### Entender o projeto

Conheça a identidade, os princípios, a teoria, a arquitetura e os limites do framework.

[Conhecer o framework](FRAMEWORK_DE_REFERENCIA.md)

</div>

<div class="pc-card" markdown>

### Resolver um problema público

Comece pelo diagnóstico estruturado e avance pelo ciclo de alternativas, decisão, implementação, avaliação e aprendizado.

[Aplicar o PPC-001](PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md)

</div>

<div class="pc-card" markdown>

### Usar ferramentas

Acesse fichas, matrizes e instrumentos práticos para documentar, comparar, implementar e avaliar decisões.

[Explorar as ferramentas](FICHA_PPC-001_DIAGNOSTICO_DE_PROBLEMA_PUBLICO.md)

</div>

<div class="pc-card" markdown>

### Contribuir

Participe da evolução do framework com propostas rastreáveis, revisáveis e coerentes com seus princípios fundadores.

[Como contribuir](CONTRIBUTING.md)

</div>

</div>

## O ciclo do Pragmatismo Cívico

<div class="pc-cycle" markdown>
<span class="pc-step">Diagnosticar</span><span class="pc-arrow">→</span>
<span class="pc-step">Formular alternativas</span><span class="pc-arrow">→</span>
<span class="pc-step">Avaliar</span><span class="pc-arrow">→</span>
<span class="pc-step">Decidir</span><span class="pc-arrow">→</span>
<span class="pc-step">Explicitar a mudança</span><span class="pc-arrow">→</span>
<span class="pc-step">Implementar</span><span class="pc-arrow">→</span>
<span class="pc-step">Monitorar</span><span class="pc-arrow">→</span>
<span class="pc-step">Avaliar resultados</span><span class="pc-arrow">→</span>
<span class="pc-step">Aprender e melhorar</span>
</div>

O ciclo não termina na decisão. Resultados geram evidências; evidências geram aprendizado; aprendizado melhora a próxima decisão. Veja a descrição integrada no [Ciclo do Pragmatismo Cívico](CICLO_DO_PRAGMATISMO_CIVICO.md).

```text
PPC-001 — Diagnóstico
    ↓
PPC-002 — Formulação e comparação de alternativas
    ↓
PPC-003 — Avaliação técnica
    ↓
PPC-004 — Decisão e justificativa pública
    ↓
Teoria da Mudança
    ↓
PPC-005 — Implementação e gestão adaptativa
    ↓
PPC-006 — Monitoramento e avaliação contínua
    ↓
PPC-007 — Avaliação de resultados e impactos
    ↓
PPC-008 — Aprendizagem institucional e melhoria contínua
    ↺
Novo ciclo pelo PPC-001
```

## Ideia central

> Toda decisão pública é uma hipótese que deve ser justificada, testada, medida, revisada e aperfeiçoada em benefício das pessoas.

O framework não pergunta apenas de onde veio uma proposta. Pergunta:

- qual problema real ela procura resolver;
- quais evidências a sustentam;
- quais alternativas foram consideradas;
- quais direitos, riscos e custos estão envolvidos;
- como a decisão será implementada, monitorada e revista;
- o que a instituição aprenderá com os resultados.

## O que o Pragmatismo Cívico não é

O Pragmatismo Cívico **não é uma ideologia, filosofia política, doutrina, partido ou movimento político**. Não pertence à esquerda, à direita, ao centro, a governos, organizações ou indivíduos.

É uma infraestrutura metodológica aberta para decisões de interesse público. Nenhuma pessoa ou instituição pode reivindicar exclusividade sobre o framework.

## Princípios fundamentais

1. O cidadão está no centro de toda decisão pública.
2. Políticas devem ser avaliadas por seus efeitos, evidências e respeito a direitos, não por identidade ideológica.
3. Ciência, engenharia, dados, experiência prática e conhecimento local devem orientar decisões.
4. Transparência, rastreabilidade, prestação de contas e auditabilidade são requisitos essenciais.
5. Toda decisão deve permanecer aberta à revisão diante de novas evidências.
6. Sustentabilidade deve considerar dimensões ambientais, sociais, econômicas e institucionais.
7. Cooperação e pluralidade são superiores à polarização como métodos de resolução de problemas.
8. Dignidade, liberdade, direitos e qualidade de vida são finalidades centrais da governança.
9. Inovação deve ser acompanhada de avaliação, responsabilidade e aprendizado.
10. A complexidade metodológica deve ser proporcional à importância, ao risco e à reversibilidade da decisão.

## Arquitetura documental

O acervo é organizado em seis camadas lógicas conectadas:

1. **Princípios e fundamentos** — identidade, teoria, princípios e especificações fundadoras.
2. **Governança e arquitetura** — manutenção, metadados, ciclo de vida, contribuição e organização documental.
3. **Método** — ciclo operacional e padrões PPC aplicáveis às decisões públicas.
4. **Ferramentas** — fichas, matrizes, indicadores, checklists e modelos.
5. **Aplicações e evidências** — estudos de caso, pilotos, avaliações e lições aprendidas.
6. **Publicação e acesso** — repositório, portal, busca, navegação e versões de distribuição.

A definição completa está no [ARQ-001 — Arquitetura Documental do Framework](ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md). O estado do acervo e a migração progressiva são acompanhados pelo [ARQ-002 — Inventário e Plano de Migração Documental](ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md).

## Padrões metodológicos disponíveis

| Recurso | Função |
|---|---|
| [PPC-001](PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md) | Define e diagnostica o problema público, sua linha de base, causas, efeitos e grupos afetados. |
| [PPC-002](PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md) | Orienta a geração e comparação de alternativas, incluindo inação, riscos e reversibilidade. |
| [PPC-003](PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md) | Estrutura a avaliação técnica, a qualidade das evidências e a recomendação. |
| [PPC-004](PPC-004_DECISAO_E_JUSTIFICATIVA.md) | Registra a decisão pública, a competência, a justificativa e as alternativas descartadas. |
| [Teoria da Mudança](MODELO_DE_TEORIA_DA_MUDANCA.md) | Explicita a lógica causal, as hipóteses, os resultados e os impactos pretendidos. |
| [PPC-005](PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md) | Transforma a decisão em intervenção executável, responsável e adaptável. |
| [PPC-006](PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md) | Acompanha execução, produtos, resultados, riscos e hipóteses. |
| [PPC-007](PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md) | Avalia resultados, impactos, atribuição, custos e efeitos adversos. |
| [PPC-008](PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md) | Converte evidências e experiência em memória institucional e melhoria contínua. |

## Governança dos padrões

| Recurso | Função |
|---|---|
| [PPC-000](PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md) | Define como os padrões PPC são estruturados, validados, mantidos e relacionados. |
| [PPC-META-001](PPC-META-001_METADADOS_E_VERSIONAMENTO.md) | Padroniza identificadores, metadados, versões, compatibilidade e histórico. |
| [PPC-000A](PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md) | Define estados, transições, revisão, substituição, obsolescência e arquivamento. |
| [Modelo de Governança](MODELO_DE_GOVERNANCA.md) | Organiza o ciclo decisório, os papéis e as salvaguardas de governança. |
| [ARQ-001](ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md) | Define camadas, categorias, dependências e organização do acervo. |
| [ARQ-002](ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md) | Inventaria o acervo, registra dívida documental e organiza a migração. |

## Ferramentas disponíveis

Cada etapa possui instrumento prático correspondente:

- [Ficha PPC-001](FICHA_PPC-001_DIAGNOSTICO_DE_PROBLEMA_PUBLICO.md);
- [Ficha PPC-002](FICHA_PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md);
- [Ficha PPC-003](FICHA_PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md);
- [Ficha PPC-004](FICHA_PPC-004_DECISAO_E_JUSTIFICATIVA.md);
- [Ficha de Teoria da Mudança](FICHA_TEORIA_DA_MUDANCA.md);
- [Ficha PPC-005](FICHA_PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md);
- [Ficha PPC-006](FICHA_PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md);
- [Ficha PPC-007](FICHA_PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md);
- [Ficha PPC-008](FICHA_PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md);
- [Matriz de Avaliação de Políticas Públicas](MATRIZ_DE_AVALIACAO_DE_POLITICAS_PUBLICAS.md);
- [Indicadores do Pragmatismo Cívico](INDICADORES.md).

## Regra de preservação da essência

Toda expansão do projeto deve concretizar os princípios fundadores, e não redefini-los. Novos documentos e ferramentas precisam demonstrar:

- qual problema real procuram resolver;
- quais princípios colocam em prática;
- como seus resultados poderão ser avaliados;
- como direitos, transparência e responsabilidade serão protegidos;
- por que acrescentam capacidade prática sem produzir complexidade desnecessária.

O documento central para essa verificação é o [Framework de Referência](FRAMEWORK_DE_REFERENCIA.md).

## Próximas entregas

As prioridades atuais são:

- formalizar o processo de propostas de mudança;
- criar o catálogo documental público e o mapa de dependências;
- implementar validação automática de metadados, identificadores e links;
- criar a ficha padrão de indicadores;
- desenvolver o checklist de transparência e rastreabilidade;
- estruturar o protocolo de avaliação do próprio framework;
- selecionar e documentar o primeiro estudo de caso demonstrativo;
- revisar a licença aplicável à documentação, às ferramentas e a eventual software;
- preparar versões para impressão dos padrões e fichas.

A evolução planejada está registrada no [Roadmap](ROADMAP.md).

## Licença e colaboração

O repositório utiliza atualmente a licença MIT. A adequação entre a licença, os documentos conceituais, as ferramentas e eventual software será revisada antes da primeira versão estável.

Contribuições são organizadas por regras públicas de governança, integridade, rastreabilidade e preservação dos princípios fundadores.

## Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Migração documental para o PPC-META-001 por representação estruturada equivalente, preservando a apresentação do README no GitHub e no portal | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Registro da conclusão da migração mínima dos 38 documentos e atualização das prioridades de catálogo e validação | Projeto Pragmatismo Cívico |
