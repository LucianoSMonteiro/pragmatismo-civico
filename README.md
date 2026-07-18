<!--
---
id: PORTAL-INICIO
titulo: Pragmatismo Cívico — Página inicial
versao: 0.14.0
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
  - GOV-008
  - CADASTRO-REVISORES
  - CASOS-INDEX
  - CASO-001
  - CASO-001-PRONTIDAO
  - CASO-001-FONTES
  - CASO-001-DOCUMENTOS-TECNICOS
  - CASO-001-GEOMETRIA
  - CASO-001-DADOS-CHUVA
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

O **Pragmatismo Cívico** é um framework aberto para governança e decisões de interesse público. Ele organiza princípios, métodos, ferramentas, revisão, casos e aprendizagem para melhorar decisões por meio de transparência, responsabilidade, sustentabilidade, cooperação e evidências.

[Começar agora](docs/COMECAR.md){ .md-button .md-button--primary }
[Explorar o método](CICLO_DO_PRAGMATISMO_CIVICO.md){ .md-button }
[Consultar os casos](casos/README.md){ .md-button }
[Consultar o catálogo](CATALOGO_DOCUMENTAL.md){ .md-button }

</div>

<div class="pc-status" markdown>

**Estado atual:** desenvolvimento aberto. Os **56 documentos** da navegação canônica estão identificados, versionados e submetidos à validação automática. O CASO-001 permanece em preparação na sub-bacia de Itapeba. O registro técnico estrutura 8 fontes, 20 alegações, 3 inconsistências e 7 grupos documentais pendentes, mas nenhum programa final, contrato integral, projeto, medição, feição oficial ou série real foi incorporado. Não existe diagnóstico, recomendação ou resultado empírico. O cadastro de revisores permanece vazio e o deploy público depende da ativação inicial do GitHub Pages na issue #1.

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

### Acompanhar o primeiro caso

Veja fontes, financiamentos, contratações, documentos requeridos e bloqueios do portão.

[Consultar documentos técnicos](casos/CASO-001_DOCUMENTOS_TECNICOS_E_CONTRATACOES.md)

</div>

<div class="pc-card" markdown>

### Contribuir ou revisar

Proponha mudanças ou candidate-se ao programa público de revisores.

[Como contribuir](CONTRIBUTING.md)

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

O acervo possui seis camadas lógicas: princípios e fundamentos; governança e arquitetura; método; ferramentas; aplicações e evidências; publicação e acesso.

Consulte [ARQ-001](ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md), [ARQ-002](ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md), [ARQ-003](ARQ-003_DECISAO_SOBRE_A_ESTRUTURA_FISICA_DO_REPOSITORIO.md) e o [Catálogo](CATALOGO_DOCUMENTAL.md).

Os caminhos existentes permanecem estáveis. Novas aplicações são publicadas em `casos/`, relatórios oficiais em `relatorios/` e arquivos locais ainda não publicáveis em `work/`, ignorado pelo Git.

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

## Governança de mudanças, revisores e casos

| Recurso | Função |
|---|---|
| [GOV-005](GOV-005_PROCESSO_DE_PROPOSTAS_DE_MUDANCA.md) | proposta, triagem, consulta e implementação |
| [GOV-006](GOV-006_POLITICA_DE_REVISAO_E_APROVACAO.md) | competência, independência, quórum e decisão |
| [GOV-007](GOV-007_PROGRAMA_E_CADASTRO_PUBLICO_DE_REVISORES.md) | candidatura, elegibilidade, disponibilidade e painéis |
| [Cadastro de Revisores](CADASTRO_PUBLICO_DE_REVISORES.md) | registro público canônico, atualmente vazio |
| [GOV-008](GOV-008_PROTOCOLO_DE_SELECAO_E_CONDUCAO_DE_CASOS.md) | seleção, prontidão, condução e encerramento de casos |
| [Guia de Contribuição](CONTRIBUTING.md) | orientação para propostas, revisão, candidatura e casos |

## Primeiro caso demonstrativo

O [CASO-001](casos/CASO-001_DRENAGEM_URBANA_E_ALERTA_PREVENTIVO_EM_MARICA.md) prepara um estudo sobre drenagem urbana e alerta preventivo na sub-bacia de Itapeba, em Maricá/RJ.

O [registro de prontidão](casos/CASO-001_REGISTRO_DE_PRONTIDAO.md) mantém o caso em preparação. A [matriz de fontes](casos/CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md) consolida 15 fontes públicas sem promover material localizado a fonte obtida.

O [registro de documentos técnicos e contratações](casos/CASO-001_DOCUMENTOS_TECNICOS_E_CONTRATACOES.md):

- estrutura 8 fontes oficiais ou institucionais;
- identifica 20 alegações verificáveis;
- registra 3 inconsistências abertas;
- lista 7 grupos documentais necessários;
- distingue comunicação, financiamento, contratação, projeto, medição e execução;
- impede tratar valor estimado ou registro de preços como contrato e implantação;
- mantém separadas as operações de drenagem do Novo PAC e o Pregão 14/2026 — Smart Drainage.

Inconsistências abertas incluem aproximadamente 19.500 beneficiários informados pela CAIXA versus mais de 300 mil divulgados pelo município, além de variações territoriais entre Barroco, Jardim Atlântico Oeste, Jardim Atlântico, Itaipuaçu e Itapeba. Nenhum número foi escolhido arbitrariamente.

O [protocolo geoespacial](casos/CASO-001_PROTOCOLO_DE_GEOMETRIA_E_DELIMITACAO.md) registra fontes candidatas, coletor e validador, mas nenhuma feição oficial. O [protocolo pluviométrico](casos/CASO-001_PROTOCOLO_DE_DADOS_PLUVIOMETRICOS.md) registra aquisição e qualidade, mas nenhuma série real.

Continuam pendentes:

- programa final e contratação da consultoria;
- termos e contratos das operações do Novo PAC;
- projetos, anteprojetos, QCI, riscos e geometrias;
- edital e anexos do Smart Drainage;
- cronogramas, medições e indicadores;
- feição oficial da sub-bacia;
- série pluviométrica real;
- participação local e revisão independente.

Preparação não é diagnóstico. A issue #2 acompanha a próxima decisão do portão.

## Validação automática

A CI verifica:

- metadados, versões, estados, históricos e relações;
- links e âncoras;
- formulários, privacidade e template de pull request;
- registro técnico de fontes, alegações, inconsistências e documentos requeridos;
- classificação dos níveis de evidência;
- exigência de caminho local e SHA-256 para fontes obtidas ou tratadas;
- pipelines pluviométrico e geoespacial com fixtures controlados;
- catálogo nas seis camadas;
- `mkdocs build --strict --clean`.

Status registrados:

- `documentation/validation`;
- `data/pipeline`;
- `geodata/pipeline`;
- `documentation/catalog`;
- `portal/build`.

## Próximas entregas

- obter programa, contratos, projetos e medições — issue #7;
- obter e verificar a feição oficial — issue #6;
- realizar downloads mensais autorizados — issue #4;
- confirmar interlocutores e participação — issue #8;
- realizar chamada pública e obter revisão técnica — issues #3 e #9;
- emitir nova decisão do portão — issue #2;
- habilitar o GitHub Pages — issue #1;
- criar a ficha padrão de indicadores, checklist de transparência e revisar a licença.

Consulte o [Roadmap](ROADMAP.md).

## Licença

O repositório utiliza atualmente a licença MIT. Sua adequação para documentação, ferramentas e eventual software será revisada antes da primeira versão estável.

<details markdown="1">
<summary>Metadados documentais</summary>

```yaml
id: PORTAL-INICIO
titulo: Pragmatismo Cívico — Página inicial
versao: 0.14.0
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
  - GOV-008
  - CADASTRO-REVISORES
  - CASOS-INDEX
  - CASO-001
  - CASO-001-PRONTIDAO
  - CASO-001-FONTES
  - CASO-001-DOCUMENTOS-TECNICOS
  - CASO-001-GEOMETRIA
  - CASO-001-DADOS-CHUVA
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
| 0.5.0 a 0.9.0 | 2026-07-18 | compatível | Estrutura física e GOV-005 a GOV-008 | Projeto Pragmatismo Cívico |
| 0.10.0 | 2026-07-18 | compatível | Recorte de Itapeba e linha de base de 52 documentos | Projeto Pragmatismo Cívico |
| 0.11.0 | 2026-07-18 | compatível | Pipeline pluviométrico e linha de base de 53 documentos | Projeto Pragmatismo Cívico |
| 0.12.0 | 2026-07-18 | compatível | Matriz de fontes e linha de base de 54 documentos | Projeto Pragmatismo Cívico |
| 0.13.0 | 2026-07-18 | compatível | Protocolo geoespacial e linha de base de 55 documentos | Projeto Pragmatismo Cívico |
| 0.14.0 | 2026-07-18 | compatível | Registro técnico, controles de evidência e linha de base de 56 documentos | Projeto Pragmatismo Cívico |
