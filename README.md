<!--
---
id: PORTAL-INICIO
titulo: Pragmatismo Cívico — Página inicial
versao: 0.8.0
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
  - GOV-007
  - CADASTRO-REVISORES
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

O **Pragmatismo Cívico** é um framework aberto para governança e decisões de interesse público. Ele organiza princípios, métodos, ferramentas, revisão e aprendizagem para melhorar decisões por meio de transparência, responsabilidade, sustentabilidade, cooperação e evidências.

[Começar agora](docs/COMECAR.md){ .md-button .md-button--primary }
[Explorar o método](CICLO_DO_PRAGMATISMO_CIVICO.md){ .md-button }
[Consultar o catálogo](CATALOGO_DOCUMENTAL.md){ .md-button }

</div>

<div class="pc-status" markdown>

**Estado atual:** desenvolvimento aberto. Os **47 documentos** da navegação canônica estão identificados, versionados, catalogados e validados automaticamente. O processo de mudanças, a política de revisão e o programa público de revisores estão publicados como rascunhos. O cadastro de revisores existe, mas não possui pessoa elegível ou ativa e não constitui instância plural. Ainda não há estudo de caso oficial nem validação empírica suficiente para declarar estabilidade. O deploy público depende da ativação inicial do GitHub Pages registrada na issue #1.

</div>

## Escolha seu caminho

<div class="pc-grid" markdown>

<div class="pc-card" markdown>

### Entender o projeto

Conheça identidade, princípios, teoria, arquitetura e limites.

[Conhecer o framework](FRAMEWORK_DE_REFERENCIA.md)

</div>

<div class="pc-card" markdown>

### Aplicar o método

Avance por diagnóstico, alternativas, decisão, implementação, avaliação e aprendizado.

[Explorar o ciclo](CICLO_DO_PRAGMATISMO_CIVICO.md)

</div>

<div class="pc-card" markdown>

### Propor uma mudança

Registre problema, alternativas, riscos, compatibilidade, decisão e verificação.

[Conhecer o processo](GOV-005_PROCESSO_DE_PROPOSTAS_DE_MUDANCA.md)

</div>

<div class="pc-card" markdown>

### Candidatar-se a revisor

Declare competências, vínculos, disponibilidade e limites sem publicar dados sensíveis.

[Conhecer o programa](GOV-007_PROGRAMA_E_CADASTRO_PUBLICO_DE_REVISORES.md)

</div>

</div>

## O ciclo metodológico

```text
PPC-001 — Diagnóstico
    ↓
PPC-002 — Alternativas
    ↓
PPC-003 — Avaliação técnica
    ↓
PPC-004 — Decisão e justificativa
    ↓
Teoria da Mudança
    ↓
PPC-005 — Implementação adaptativa
    ↓
PPC-006 — Monitoramento
    ↓
PPC-007 — Avaliação de resultados e impactos
    ↓
PPC-008 — Aprendizagem institucional
    ↺
Novo ciclo pelo PPC-001
```

Toda decisão pública é tratada como hipótese que deve ser justificada, testada, medida, revisada e aperfeiçoada.

## O que o Pragmatismo Cívico não é

O Pragmatismo Cívico **não é ideologia, partido, doutrina ou movimento político**. É infraestrutura metodológica aberta. Nenhuma pessoa ou instituição pode reivindicar exclusividade sobre o framework.

## Princípios essenciais

1. cidadão no centro;
2. avaliação por efeitos, evidências e direitos;
3. ciência, dados, experiência prática e conhecimento local;
4. transparência, rastreabilidade e prestação de contas;
5. revisão diante de novas evidências;
6. sustentabilidade ambiental, social, econômica e institucional;
7. cooperação e pluralidade;
8. dignidade, liberdade e qualidade de vida;
9. inovação com responsabilidade;
10. complexidade proporcional ao risco e à reversibilidade.

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
- [ARQ-002 — Inventário](ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md);
- [ARQ-003 — Estrutura Física](ARQ-003_DECISAO_SOBRE_A_ESTRUTURA_FISICA_DO_REPOSITORIO.md);
- [Catálogo Documental](CATALOGO_DOCUMENTAL.md).

Os caminhos existentes permanecem estáveis. Novas aplicações serão publicadas em `casos/` e relatórios oficiais em `relatorios/`.

## Padrões metodológicos

| Recurso | Função |
|---|---|
| [PPC-001](PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md) | diagnosticar o problema |
| [PPC-002](PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md) | formular e comparar alternativas |
| [PPC-003](PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md) | avaliar tecnicamente |
| [PPC-004](PPC-004_DECISAO_E_JUSTIFICATIVA.md) | decidir e justificar |
| [Teoria da Mudança](MODELO_DE_TEORIA_DA_MUDANCA.md) | explicitar lógica causal |
| [PPC-005](PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md) | implementar e adaptar |
| [PPC-006](PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md) | monitorar |
| [PPC-007](PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md) | avaliar resultados e impactos |
| [PPC-008](PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md) | aprender e melhorar |

## Governança de mudanças e revisores

| Recurso | Função |
|---|---|
| [GOV-005](GOV-005_PROCESSO_DE_PROPOSTAS_DE_MUDANCA.md) | proposta, triagem, consulta e implementação |
| [Ficha GOV-005](FICHA_GOV-005_PROPOSTA_DE_MUDANCA.md) | registro da proposta |
| [GOV-006](GOV-006_POLITICA_DE_REVISAO_E_APROVACAO.md) | competência, independência, quórum e decisão |
| [Ficha GOV-006](FICHA_GOV-006_REGISTRO_DE_REVISAO_E_APROVACAO.md) | registro da revisão e aprovação |
| [GOV-007](GOV-007_PROGRAMA_E_CADASTRO_PUBLICO_DE_REVISORES.md) | candidatura, elegibilidade, disponibilidade e painéis |
| [Ficha GOV-007](FICHA_GOV-007_CANDIDATURA_E_AVALIACAO_DE_REVISOR.md) | candidatura e avaliação |
| [Cadastro de Revisores](CADASTRO_PUBLICO_DE_REVISORES.md) | registro público canônico, atualmente vazio |
| [Guia de Contribuição](CONTRIBUTING.md) | orientação para propostas, revisão e candidatura |

### Fluxo de governança

```text
Problema → Proposta PM-AAAA-NNN → Triagem → Revisão GOV-006
→ Decisão → Implementação → Verificação → Encerramento
```

Revisores podem ser convidados apenas após candidatura e avaliação pelo GOV-007. Elegibilidade não garante convite, remuneração ou posição institucional.

## Privacidade na candidatura

Issues são públicas. A candidatura não deve conter endereço, telefone, documento oficial, data de nascimento, informação médica, renda, contato privado ou dado sensível de terceiros.

Enquanto não houver canal privado formal, informação confidencial não deve ser enviada ao repositório.

## Validação automática

A CI verifica:

- metadados, versões, estados e históricos;
- dependências, relações, substituições e ciclos;
- links e âncoras;
- formulários de proposta e candidatura;
- salvaguardas públicas de privacidade;
- template de pull request;
- catálogo e estrutura física;
- `mkdocs build --strict --clean`.

Status registrados:

- `documentation/validation`;
- `documentation/catalog`;
- `portal/build`.

## Próximas entregas

- selecionar e documentar o primeiro estudo de caso;
- realizar a primeira chamada pública de revisores;
- habilitar o GitHub Pages — issue #1;
- criar a ficha padrão de indicadores;
- desenvolver o checklist de transparência;
- estruturar o protocolo de avaliação do framework;
- revisar a licença;
- preparar versões para impressão.

Consulte o [Roadmap](ROADMAP.md).

## Licença

O repositório utiliza atualmente a licença MIT. Sua adequação para documentação, ferramentas e eventual software será revisada antes da primeira versão estável.

<details markdown="1">
<summary>Metadados documentais</summary>

```yaml
id: PORTAL-INICIO
titulo: Pragmatismo Cívico — Página inicial
versao: 0.8.0
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
  - GOV-007
  - CADASTRO-REVISORES
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
| 0.1.0 a 0.4.0 | 2026-07-18 | compatível | Migração, catálogo e validação automática | Projeto Pragmatismo Cívico |
| 0.5.0 | 2026-07-18 | compatível | Inclusão do ARQ-003 | Projeto Pragmatismo Cívico |
| 0.6.0 | 2026-07-18 | compatível | Inclusão do GOV-005 | Projeto Pragmatismo Cívico |
| 0.7.0 | 2026-07-18 | compatível | Inclusão do GOV-006 | Projeto Pragmatismo Cívico |
| 0.8.0 | 2026-07-18 | compatível | Inclusão do GOV-007, cadastro, candidatura e salvaguardas de privacidade | Projeto Pragmatismo Cívico |
