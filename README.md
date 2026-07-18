<!--
---
id: PORTAL-INICIO
titulo: Pragmatismo Cívico — Página inicial
versao: 0.13.0
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

**Estado atual:** desenvolvimento aberto. Os **55 documentos** da navegação canônica estão identificados, versionados e submetidos à validação automática. O CASO-001 permanece em preparação na sub-bacia de Itapeba. A matriz consolida 15 fontes e os protocolos pluviométrico e geoespacial possuem validadores aprovados apenas com fixtures sintéticos. Nenhuma feição oficial de Itapeba, arquivo mensal real ou produto técnico integral foi incorporado. Não existe diagnóstico, recomendação ou resultado empírico. O cadastro de revisores permanece vazio e o deploy público depende da ativação inicial do GitHub Pages na issue #1.

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

Veja fontes, geosserviços candidatos, protocolos de dados e bloqueios que impedem iniciar o diagnóstico.

[Consultar o protocolo geoespacial](casos/CASO-001_PROTOCOLO_DE_GEOMETRIA_E_DELIMITACAO.md)

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
| [Ficha GOV-005](FICHA_GOV-005_PROPOSTA_DE_MUDANCA.md) | registro da proposta |
| [GOV-006](GOV-006_POLITICA_DE_REVISAO_E_APROVACAO.md) | competência, independência, quórum e decisão |
| [Ficha GOV-006](FICHA_GOV-006_REGISTRO_DE_REVISAO_E_APROVACAO.md) | registro da revisão e aprovação |
| [GOV-007](GOV-007_PROGRAMA_E_CADASTRO_PUBLICO_DE_REVISORES.md) | candidatura, elegibilidade, disponibilidade e painéis |
| [Cadastro de Revisores](CADASTRO_PUBLICO_DE_REVISORES.md) | registro público canônico, atualmente vazio |
| [GOV-008](GOV-008_PROTOCOLO_DE_SELECAO_E_CONDUCAO_DE_CASOS.md) | seleção, prontidão, condução e encerramento de casos |
| [Ficha GOV-008](FICHA_GOV-008_REGISTRO_DE_SELECAO_E_CONDUCAO_DE_CASO.md) | modelo de seleção e portão de prontidão |
| [Guia de Contribuição](CONTRIBUTING.md) | orientação para propostas, revisão, candidatura e casos |

### Fluxo de casos

```text
Seleção GOV-008 → registro de prontidão → decisão do portão
→ PPC-001 somente se aprovado → ciclo metodológico
→ revisão → publicação de evidências e limitações → encerramento
```

## Primeiro caso demonstrativo

O [CASO-001](casos/CASO-001_DRENAGEM_URBANA_E_ALERTA_PREVENTIVO_EM_MARICA.md) prepara um estudo sobre drenagem urbana e alerta preventivo na sub-bacia de Itapeba, em Maricá/RJ.

O [registro de prontidão](casos/CASO-001_REGISTRO_DE_PRONTIDAO.md) refinou a pergunta, definiu o período preliminar, avaliou os requisitos do portão e manteve o caso em preparação.

A [matriz de fontes](casos/CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md):

- consolida 15 fontes públicas com identificadores `F-001` a `F-015`;
- diferencia norma, plano, cartografia, comunicação e portal de dados;
- inclui uma camada poligonal estadual de sub-bacias e a hidrografia RJ25;
- declara que nenhuma fonte foi obtida ou tratada para uso empírico;
- relaciona as lacunas aos requisitos do portão.

O [protocolo geoespacial](casos/CASO-001_PROTOCOLO_DE_GEOMETRIA_E_DELIMITACAO.md):

- registra fontes candidatas do GeoINEA;
- exige preservar consulta, arquivo, parâmetros, licença e hash;
- impede tratar linha de drenagem, bairro ou croqui como polígono oficial;
- valida estrutura GeoJSON, anéis, coordenadas, extensão e nome esperado;
- é testado apenas com polígono sintético.

O [protocolo pluviométrico](casos/CASO-001_PROTOCOLO_DE_DADOS_PLUVIOMETRICOS.md):

- separa aquisição humana de processamento automatizado;
- calcula SHA-256 das fontes;
- normaliza UTC e horário de Brasília;
- sinaliza datas inválidas, valores ausentes ou negativos, duplicidades e lacunas;
- produz CSV, manifesto e relatório;
- é testado apenas com fixture sintético;
- define retenção, quarentena e descarte.

Continuam pendentes:

- feição oficial e memória de delimitação — issue #6;
- produtos técnicos e geometrias — issue #7;
- downloads mensais reais e revisão das flags — issue #4;
- participação local — issue #8;
- revisão independente — issue #9.

Preparação não é diagnóstico. A issue #2 acompanha a próxima decisão do portão.

## Privacidade na candidatura e nos casos

Issues são públicas. Candidaturas não devem conter endereço, telefone, documento oficial, data de nascimento, informação médica, renda, contato privado ou dado sensível de terceiros.

Casos não devem publicar dados pessoais, sigilosos ou de segurança apenas para aumentar aparência de transparência. Enquanto não houver canal privado formal, informação confidencial não deve ser enviada ao repositório.

## Validação automática

A CI verifica:

- metadados, versões, estados e históricos;
- dependências, relações, substituições e ciclos;
- links e âncoras;
- formulários de proposta e candidatura;
- salvaguardas públicas de privacidade;
- template de pull request;
- pipeline pluviométrico com dados sintéticos;
- pipeline GeoJSON com geometrias sintéticas;
- catálogo nas seis camadas e estrutura física;
- `mkdocs build --strict --clean`.

Status registrados:

- `documentation/validation`;
- `data/pipeline`;
- `geodata/pipeline`;
- `documentation/catalog`;
- `portal/build`.

## Próximas entregas

- realizar os downloads mensais autorizados — issue #4;
- obter e verificar a feição oficial — issue #6;
- obter produtos técnicos integrais — issue #7;
- confirmar interlocutores e participação — issue #8;
- realizar a primeira chamada pública de revisores — issue #3;
- obter revisão técnica — issue #9;
- emitir nova decisão do portão — issue #2;
- habilitar o GitHub Pages — issue #1;
- criar a ficha padrão de indicadores;
- desenvolver o checklist de transparência;
- revisar a licença.

Consulte o [Roadmap](ROADMAP.md).

## Licença

O repositório utiliza atualmente a licença MIT. Sua adequação para documentação, ferramentas e eventual software será revisada antes da primeira versão estável.

<details markdown="1">
<summary>Metadados documentais</summary>

```yaml
id: PORTAL-INICIO
titulo: Pragmatismo Cívico — Página inicial
versao: 0.13.0
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
| 0.5.0 | 2026-07-18 | compatível | Inclusão do ARQ-003 | Projeto Pragmatismo Cívico |
| 0.6.0 | 2026-07-18 | compatível | Inclusão do GOV-005 | Projeto Pragmatismo Cívico |
| 0.7.0 | 2026-07-18 | compatível | Inclusão do GOV-006 | Projeto Pragmatismo Cívico |
| 0.8.0 | 2026-07-18 | compatível | Inclusão do GOV-007 e cadastro | Projeto Pragmatismo Cívico |
| 0.9.0 | 2026-07-18 | compatível | Inclusão do GOV-008 e CASO-001 | Projeto Pragmatismo Cívico |
| 0.10.0 | 2026-07-18 | compatível | Recorte de Itapeba, registro de prontidão e linha de base de 52 documentos | Projeto Pragmatismo Cívico |
| 0.11.0 | 2026-07-18 | compatível | Protocolo pluviométrico, pipeline sintético, quarto status de CI e linha de base de 53 documentos | Projeto Pragmatismo Cívico |
| 0.12.0 | 2026-07-18 | compatível | Matriz de fontes, política de retenção e linha de base de 54 documentos | Projeto Pragmatismo Cívico |
| 0.13.0 | 2026-07-18 | compatível | Protocolo geoespacial, validador GeoJSON, quinto status de CI e linha de base de 55 documentos | Projeto Pragmatismo Cívico |
