<!--
---
id: PORTAL-INICIO
titulo: Pragmatismo Cívico — Página inicial
versao: 0.7.0
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
  - ARQ-003
  - GOV-005
  - GOV-006
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

O **Pragmatismo Cívico** é um framework aberto para governança e decisões de interesse público. Ele organiza princípios, governança, métodos, ferramentas e evidências de aplicação para melhorar decisões por meio de transparência, responsabilidade, sustentabilidade, cooperação e aprendizado contínuo.

[Começar agora](docs/COMECAR.md){ .md-button .md-button--primary }
[Explorar o método](CICLO_DO_PRAGMATISMO_CIVICO.md){ .md-button }
[Consultar o catálogo](CATALOGO_DOCUMENTAL.md){ .md-button }

</div>

<div class="pc-status" markdown>

**Estado atual:** desenvolvimento aberto. Os 44 documentos da navegação canônica estão identificados, versionados, catalogados e validados automaticamente. O ciclo PPC-001 a PPC-008, a Teoria da Mudança, treze ferramentas e os padrões de governança estão disponíveis para revisão e aplicação experimental. O GOV-005 governa propostas e o GOV-006 governa revisão, aprovação e verificação. A instância plural permanente ainda não foi constituída, portanto decisões críticas e fundacionais permanecem limitadas pelo regime provisório. Ainda não há estudo de caso oficial nem validação empírica suficiente para declarar estabilidade. O deploy público depende da ativação inicial do GitHub Pages registrada na issue #1.

</div>

## Escolha seu caminho

<div class="pc-grid" markdown>

<div class="pc-card" markdown>

### Entender o projeto

Conheça a identidade, os princípios, a teoria, a arquitetura e os limites do framework.

[Conhecer o framework](FRAMEWORK_DE_REFERENCIA.md)

</div>

<div class="pc-card" markdown>

### Aplicar o método

Comece pelo diagnóstico e avance por alternativas, decisão, implementação, avaliação e aprendizado.

[Explorar o ciclo](CICLO_DO_PRAGMATISMO_CIVICO.md)

</div>

<div class="pc-card" markdown>

### Usar ferramentas

Acesse fichas, matriz e indicadores para documentar, implementar e revisar decisões.

[Explorar as ferramentas](FICHA_PPC-001_DIAGNOSTICO_DE_PROBLEMA_PUBLICO.md)

</div>

<div class="pc-card" markdown>

### Propor e revisar uma mudança

Registre problema, alternativas, riscos, compatibilidade, composição, quórum, decisão e verificação.

[Conhecer a governança de mudanças](GOV-005_PROCESSO_DE_PROPOSTAS_DE_MUDANCA.md)

</div>

</div>

## O ciclo

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

Toda decisão pública é tratada como hipótese que deve ser justificada, testada, medida, revisada e aperfeiçoada.

## O que o Pragmatismo Cívico não é

O Pragmatismo Cívico **não é ideologia, partido, doutrina ou movimento político**. É uma infraestrutura metodológica aberta. Nenhuma pessoa ou instituição pode reivindicar exclusividade sobre o framework.

## Princípios essenciais

1. O cidadão está no centro da decisão pública.
2. Propostas são avaliadas por efeitos, evidências e respeito a direitos.
3. Ciência, engenharia, dados, experiência prática e conhecimento local orientam decisões.
4. Transparência, rastreabilidade e prestação de contas são requisitos.
5. Toda decisão permanece aberta à revisão diante de novas evidências.
6. Sustentabilidade inclui dimensões ambientais, sociais, econômicas e institucionais.
7. Cooperação e pluralidade são superiores à polarização como método.
8. Dignidade, liberdade, direitos e qualidade de vida são finalidades centrais.
9. Inovação exige avaliação, responsabilidade e aprendizado.
10. A complexidade deve ser proporcional à importância, ao risco e à reversibilidade.

## Arquitetura documental

O acervo possui seis camadas lógicas:

1. princípios e fundamentos;
2. governança e arquitetura;
3. método;
4. ferramentas;
5. aplicações e evidências;
6. publicação e acesso.

Consulte:

- [ARQ-001 — Arquitetura Documental](ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md);
- [ARQ-002 — Inventário e Plano de Migração](ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md);
- [ARQ-003 — Estrutura Física do Repositório](ARQ-003_DECISAO_SOBRE_A_ESTRUTURA_FISICA_DO_REPOSITORIO.md);
- [Catálogo Documental](CATALOGO_DOCUMENTAL.md).

### Estrutura física vigente

Os caminhos existentes permanecem estáveis. O crescimento adotará uma estrutura híbrida:

- novas aplicações em `casos/`;
- relatórios oficiais em `relatorios/`;
- automações em `scripts/`;
- ativos públicos em `docs/assets/`.

A decisão será reavaliada após três casos oficiais, 60 documentos ou evidência de custo material da estrutura atual.

## Padrões metodológicos

| Recurso | Função |
|---|---|
| [PPC-001](PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md) | Define e diagnostica o problema público. |
| [PPC-002](PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md) | Formula e compara alternativas. |
| [PPC-003](PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md) | Estrutura a avaliação técnica. |
| [PPC-004](PPC-004_DECISAO_E_JUSTIFICATIVA.md) | Registra decisão e justificativa. |
| [Teoria da Mudança](MODELO_DE_TEORIA_DA_MUDANCA.md) | Explicita a lógica causal. |
| [PPC-005](PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md) | Organiza implementação adaptativa. |
| [PPC-006](PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md) | Monitora execução e resultados. |
| [PPC-007](PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md) | Avalia resultados e impactos. |
| [PPC-008](PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md) | Converte evidências em aprendizagem. |

## Governança documental e de mudanças

| Recurso | Função |
|---|---|
| [PPC-000](PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md) | Estrutura o ecossistema de padrões. |
| [PPC-000A](PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md) | Define estados e transições. |
| [PPC-META-001](PPC-META-001_METADADOS_E_VERSIONAMENTO.md) | Define metadados e versionamento. |
| [GOV-005](GOV-005_PROCESSO_DE_PROPOSTAS_DE_MUDANCA.md) | Governa identificação, triagem e ciclo da proposta. |
| [Ficha GOV-005](FICHA_GOV-005_PROPOSTA_DE_MUDANCA.md) | Registra o conteúdo e a evolução da proposta. |
| [GOV-006](GOV-006_POLITICA_DE_REVISAO_E_APROVACAO.md) | Governa competência, independência, quórum, aprovação e reconsideração. |
| [Registro GOV-006](FICHA_GOV-006_REGISTRO_DE_REVISAO_E_APROVACAO.md) | Registra composição, conflitos, votos, decisão e verificação. |
| [Guia de Contribuição](CONTRIBUTING.md) | Orienta contribuições editoriais e formais. |
| [ARQ-001](ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md) | Define camadas e relações. |
| [ARQ-002](ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md) | Acompanha cobertura, validação e dívida. |
| [ARQ-003](ARQ-003_DECISAO_SOBRE_A_ESTRUTURA_FISICA_DO_REPOSITORIO.md) | Governa caminhos e gatilhos de reorganização. |

### Como uma mudança formal avança

```text
Problema → Proposta PM-AAAA-NNN → Triagem → Análise
→ Revisão e consulta proporcional → Decisão motivada
→ Implementação → Verificação → Encerramento ou reconsideração
```

Mudanças fundacionais não podem adquirir estado estável por decisão unilateral enquanto não houver instância plural formalmente constituída.

## Validação automática

A CI verifica:

- metadados, versões, estados e históricos;
- dependências, relações, substituições e ciclos;
- links e âncoras;
- formulário YAML de proposta de mudança;
- template de pull request;
- catálogo publicado;
- estrutura física;
- `mkdocs build --strict --clean`.

Status registrados:

- `documentation/validation`;
- `documentation/catalog`;
- `portal/build`.

## Próximas entregas

As prioridades atuais são:

- criar o cadastro público e o programa de revisores;
- selecionar e documentar o primeiro estudo de caso;
- habilitar o GitHub Pages e confirmar o primeiro deploy — issue #1;
- criar a ficha padrão de indicadores;
- desenvolver o checklist de transparência e rastreabilidade;
- estruturar o protocolo de avaliação do próprio framework;
- revisar a licença;
- preparar versões para impressão.

Consulte o [Roadmap](ROADMAP.md).

## Licença e colaboração

O repositório utiliza atualmente a licença MIT. A adequação entre essa licença, a documentação, as ferramentas e eventual software será revisada antes da primeira versão estável.

<details markdown="1">
<summary>Metadados documentais</summary>

```yaml
id: PORTAL-INICIO
titulo: Pragmatismo Cívico — Página inicial
versao: 0.7.0
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
  - ARQ-003
  - GOV-005
  - GOV-006
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
| 0.2.0 | 2026-07-18 | compatível | Registro da cobertura dos 38 documentos | Projeto Pragmatismo Cívico |
| 0.2.1 | 2026-07-18 | correção | Inclusão de metadados colapsáveis | Projeto Pragmatismo Cívico |
| 0.2.2 | 2026-07-18 | correção | Processamento Markdown do bloco colapsável | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Inclusão do catálogo e atualização para 39 documentos | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-18 | compatível | Registro da conclusão da validação automática | Projeto Pragmatismo Cívico |
| 0.5.0 | 2026-07-18 | compatível | Inclusão do ARQ-003 e atualização para 40 documentos | Projeto Pragmatismo Cívico |
| 0.6.0 | 2026-07-18 | compatível | Inclusão do GOV-005, da ficha, do formulário e atualização para 42 documentos | Projeto Pragmatismo Cívico |
| 0.7.0 | 2026-07-18 | compatível | Inclusão do GOV-006, do registro de revisão, do template de pull request e atualização para 44 documentos | Projeto Pragmatismo Cívico |
