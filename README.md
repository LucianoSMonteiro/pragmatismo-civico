<!--
---
id: PORTAL-INICIO
titulo: Pragmatismo Cívico — Página inicial
versao: 0.4.0
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
  - CATALOGO-DOCUMENTAL
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
[Consultar o catálogo](CATALOGO_DOCUMENTAL.md){ .md-button }

</div>

<div class="pc-status" markdown>

**Estado atual:** desenvolvimento aberto. Os 39 documentos da navegação canônica estão identificados, versionados, catalogados e submetidos a validação automática. A execução aprovada verifica metadados, versões, estados, datas, compatibilidade, histórico, dependências, substituições, links internos, âncoras, correspondência do catálogo e build estrito. O deploy público ainda depende da ativação inicial do GitHub Pages registrada na issue #1. Ainda não há estudo de caso oficial nem validação empírica suficiente para declarar o framework estável.

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

O framework pergunta:

- qual problema real procura resolver;
- quais evidências sustentam a análise;
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

O acervo é organizado em seis camadas lógicas:

1. **Princípios e fundamentos**;
2. **Governança e arquitetura**;
3. **Método**;
4. **Ferramentas**;
5. **Aplicações e evidências**;
6. **Publicação e acesso**.

A definição completa está no [ARQ-001](ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md). O estado do acervo e da validação está no [ARQ-002](ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md). O [Catálogo Documental](CATALOGO_DOCUMENTAL.md) reúne identificadores, versões, estados, caminhos e relações.

## Padrões metodológicos disponíveis

| Recurso | Função |
|---|---|
| [PPC-001](PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md) | Define e diagnostica o problema público. |
| [PPC-002](PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md) | Formula e compara alternativas. |
| [PPC-003](PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md) | Estrutura a avaliação técnica. |
| [PPC-004](PPC-004_DECISAO_E_JUSTIFICATIVA.md) | Registra a decisão e sua justificativa. |
| [Teoria da Mudança](MODELO_DE_TEORIA_DA_MUDANCA.md) | Explicita a lógica causal. |
| [PPC-005](PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md) | Organiza implementação e adaptação. |
| [PPC-006](PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md) | Acompanha execução e resultados. |
| [PPC-007](PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md) | Avalia resultados e impactos. |
| [PPC-008](PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md) | Converte evidências em aprendizado. |

## Governança dos padrões

| Recurso | Função |
|---|---|
| [PPC-000](PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md) | Estrutura o ecossistema PPC. |
| [PPC-META-001](PPC-META-001_METADADOS_E_VERSIONAMENTO.md) | Padroniza metadados e versões. |
| [PPC-000A](PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md) | Define estados e transições. |
| [Modelo de Governança](MODELO_DE_GOVERNANCA.md) | Organiza papéis e salvaguardas. |
| [ARQ-001](ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md) | Define a arquitetura documental. |
| [ARQ-002](ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md) | Inventaria, valida e orienta a evolução do acervo. |

## Ferramentas disponíveis

- [Ficha PPC-001](FICHA_PPC-001_DIAGNOSTICO_DE_PROBLEMA_PUBLICO.md);
- [Ficha PPC-002](FICHA_PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md);
- [Ficha PPC-003](FICHA_PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md);
- [Ficha PPC-004](FICHA_PPC-004_DECISAO_E_JUSTIFICATIVA.md);
- [Ficha de Teoria da Mudança](FICHA_TEORIA_DA_MUDANCA.md);
- [Ficha PPC-005](FICHA_PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md);
- [Ficha PPC-006](FICHA_PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md);
- [Ficha PPC-007](FICHA_PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md);
- [Ficha PPC-008](FICHA_PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md);
- [Matriz de Avaliação](MATRIZ_DE_AVALIACAO_DE_POLITICAS_PUBLICAS.md);
- [Indicadores](INDICADORES.md).

## Validação automática

Cada execução na branch padrão:

- valida os 39 documentos e o grafo de relações;
- verifica links internos e âncoras;
- gera um relatório consolidado preservado como artefato;
- compara o catálogo publicado com a geração atual;
- executa `mkdocs build --strict --clean`;
- registra os status `documentation/validation` e `portal/build`.

A automação apoia a governança, mas não substitui revisão humana, aprovação metodológica ou validação empírica.

## Próximas entregas

As prioridades atuais são:

- formalizar o processo de propostas de mudança;
- habilitar o GitHub Pages e confirmar o primeiro deploy — issue #1;
- avaliar a estrutura física do repositório na Fase 7;
- criar a ficha padrão de indicadores;
- desenvolver o checklist de transparência e rastreabilidade;
- estruturar o protocolo de avaliação do próprio framework;
- selecionar o primeiro estudo de caso demonstrativo;
- revisar a licença;
- preparar versões para impressão.

A evolução planejada está no [Roadmap](ROADMAP.md).

## Licença e colaboração

O repositório utiliza atualmente a licença MIT. A adequação entre a licença, os documentos conceituais, as ferramentas e eventual software será revisada antes da primeira versão estável.

<details markdown="1">
<summary>Metadados documentais</summary>

```yaml
id: PORTAL-INICIO
titulo: Pragmatismo Cívico — Página inicial
versao: 0.4.0
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
  - CATALOGO-DOCUMENTAL
  - CICLO-PC-001
  - GOV-003
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
```

</details>

## Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Migração documental por representação estruturada equivalente | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Registro da migração mínima dos 38 documentos | Projeto Pragmatismo Cívico |
| 0.2.1 | 2026-07-18 | correção | Inclusão da seção humana de metadados | Projeto Pragmatismo Cívico |
| 0.2.2 | 2026-07-18 | correção | Ativação do processamento Markdown na seção de metadados | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Inclusão do catálogo e atualização para 39 documentos | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-18 | compatível | Registro da conclusão da Fase 6 e da validação automática integral do acervo | Projeto Pragmatismo Cívico |
