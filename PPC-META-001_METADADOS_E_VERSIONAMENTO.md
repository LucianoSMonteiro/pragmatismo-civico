---
id: PPC-META-001
titulo: Metadados e Versionamento
versao: 0.2.0
status: rascunho
tipo: padrao-transversal
idioma: pt-BR
data_criacao: 2026-07-17
data_versao: 2026-07-17
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - PPC-000
produz_entrada_para: []
relaciona_se_com:
  - PPC-000A
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# PPC-META-001 — Metadados e Versionamento

## Status

Rascunho inicial para discussão pública e adoção progressiva.

## 1. Objetivo

Estabelecer um padrão comum de identificação, metadados, versionamento, histórico e relacionamento para os documentos do Pragmatismo Cívico.

O PPC-META-001 busca garantir que qualquer pessoa consiga responder, sem depender de conhecimento informal:

- qual documento está consultando;
- qual é sua versão e seu estado;
- quem responde por sua manutenção;
- quando e por que ele foi alterado;
- de quais documentos depende;
- quais documentos, ferramentas ou processos ele substitui ou complementa;
- se a mudança é compatível com usos anteriores.

## 2. Escopo

Aplica-se a:

- Padrões do Pragmatismo Cívico — PPCs;
- padrões transversais identificados como PPC-META;
- fichas, matrizes, checklists e modelos;
- documentos de governança;
- documentos de arquitetura;
- estudos de caso e relatórios oficiais;
- versões publicadas no portal.

Documentos históricos podem ser migrados progressivamente. Todo documento novo ou submetido a revisão estrutural deve adotar este padrão.

## 3. Relação com o PPC-000 e o PPC-000A

O `PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md` define as regras gerais do ecossistema de padrões.

O `PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md` define os estados canônicos, as transições, os portões de decisão e os registros necessários para mudança de estado.

O PPC-META-001 detalha especificamente:

- o conjunto mínimo de metadados;
- a sintaxe recomendada;
- as regras de versionamento;
- o registro de alterações;
- a declaração de dependências e compatibilidade;
- os critérios de validação documental.

Em caso de conflito, o PPC-000 orienta a governança geral, o PPC-000A orienta o ciclo de vida, e o PPC-META-001 orienta a representação documental e o versionamento.

## 4. Princípios

A aplicação deste padrão deve observar:

1. **Rastreabilidade** — mudanças devem poder ser reconstruídas.
2. **Clareza** — metadados devem ser compreensíveis por pessoas e processáveis por ferramentas.
3. **Proporcionalidade** — o registro não deve ser mais complexo que o valor que produz.
4. **Imutabilidade histórica** — versões anteriores não devem ser apagadas silenciosamente.
5. **Responsabilidade explícita** — manutenção e aprovação devem possuir responsáveis identificáveis.
6. **Compatibilidade declarada** — impactos sobre usos anteriores devem ser informados.
7. **Fonte única de verdade** — o repositório oficial é a referência para versões vigentes.

## 5. Identificador documental

Todo documento governado por este padrão deve possuir um identificador único e estável.

### 5.1 Formatos recomendados

- `PPC-000` a `PPC-999` — padrões metodológicos;
- `PPC-META-001` a `PPC-META-999` — padrões transversais;
- `FICHA-PPC-001` — ferramentas diretamente associadas a um PPC;
- `GOV-001` — documentos de governança;
- `ARQ-001` — documentos de arquitetura;
- `CASO-AAAA-NNN` — estudos de caso;
- `REL-AAAA-NNN` — relatórios oficiais.

O identificador não deve ser reutilizado, mesmo após obsolescência ou substituição.

### 5.2 Nome de arquivo

O nome do arquivo deve:

- começar pelo identificador quando houver código formal;
- utilizar letras maiúsculas, números, hífens e sublinhados;
- descrever o conteúdo de forma estável;
- evitar datas no nome, salvo em estudos de caso ou relatórios periódicos;
- preservar o caminho antigo por redirecionamento ou referência quando houver renomeação.

Exemplo:

```text
PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md
```

## 6. Bloco mínimo de metadados

Recomenda-se um cabeçalho YAML no início de cada documento. Enquanto o portal não automatizar a leitura desses dados, o mesmo conteúdo pode ser apresentado em uma seção textual equivalente.

```yaml
---
id: PPC-005
titulo: Implementação e Gestão Adaptativa
versao: 0.1.0
status: rascunho
tipo: padrao-metodologico
idioma: pt-BR
data_criacao: 2026-07-17
data_versao: 2026-07-17
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - PPC-004
  - MODELO-DE-TEORIA-DA-MUDANCA
produz_entrada_para:
  - PPC-006
relaciona_se_com:
  - FICHA-PPC-005
substitui: []
substituido_por: null
compatibilidade: inicial
proxima_revisao: null
---
```

## 7. Campos obrigatórios

### 7.1 `id`

Identificador único e permanente do documento.

### 7.2 `titulo`

Nome oficial, sem abreviações ambíguas.

### 7.3 `versao`

Versão semântica no formato `X.Y.Z`.

### 7.4 `status`

Estado vigente do documento, conforme o ciclo de vida oficial definido pelo PPC-000A.

Os valores aceitos são:

- `ideia`;
- `proposta`;
- `rascunho`;
- `revisao-publica`;
- `piloto`;
- `estavel`;
- `em-revisao`;
- `substituido`;
- `obsoleto`;
- `arquivado`.

A alteração desse campo deve corresponder a uma transição registrada segundo o PPC-000A.

### 7.5 `tipo`

Categoria funcional do documento, como:

- `principio`;
- `padrao-metodologico`;
- `padrao-transversal`;
- `ferramenta`;
- `governanca`;
- `arquitetura`;
- `estudo-de-caso`;
- `relatorio`.

### 7.6 `idioma`

Código de idioma, preferencialmente conforme BCP 47, como `pt-BR`.

### 7.7 `data_criacao`

Data da primeira versão registrada, em `AAAA-MM-DD`.

### 7.8 `data_versao`

Data da versão corrente, em `AAAA-MM-DD`.

### 7.9 `responsaveis`

Pessoas, equipes ou instâncias responsáveis pela manutenção.

### 7.10 Relacionamentos

Devem ser declarados, quando aplicáveis:

- `depende_de`;
- `produz_entrada_para`;
- `relaciona_se_com`;
- `substitui`;
- `substituido_por`.

### 7.11 `compatibilidade`

Deve assumir um dos valores:

- `inicial` — primeira versão;
- `compativel` — preserva aplicações anteriores;
- `parcial` — exige ajustes limitados;
- `incompativel` — exige migração explícita.

## 8. Campos condicionais

Devem ser preenchidos quando pertinentes:

- `aprovadores`;
- `proxima_revisao`;
- `licenca`;
- `jurisdicao`;
- `dados_sensiveis`;
- `ferramentas_associadas`;
- `repositorio_origem`;
- `commit_publicacao`;
- `url_canonica`;
- `palavras_chave`.

Campos adicionais podem ser criados, desde que documentados e sem duplicar significado existente.

## 9. Versionamento semântico

As versões seguem `X.Y.Z`.

### 9.1 Versão de correção — `Z`

Usada para alterações que não mudam o método ou a interpretação, como:

- correções ortográficas;
- melhoria de formatação;
- conserto de links;
- esclarecimentos sem efeito normativo;
- ajustes de acessibilidade.

Exemplo: `0.2.1` para `0.2.2`.

### 9.2 Versão menor — `Y`

Usada para evolução compatível, como:

- inclusão de orientações opcionais;
- melhoria de exemplos;
- novo campo não obrigatório;
- refinamento que preserva aplicações válidas;
- adição de ferramenta complementar.

Exemplo: `0.2.2` para `0.3.0`.

### 9.3 Versão maior — `X`

Usada para mudança incompatível, como:

- alteração de objetivo ou escopo;
- mudança de etapas obrigatórias;
- redefinição de critérios de conformidade;
- remoção de campos obrigatórios;
- alteração que invalida aplicações anteriores;
- substituição estrutural do documento.

Exemplo: `1.4.3` para `2.0.0`.

## 10. Versões anteriores a 1.0.0

Enquanto um documento estiver em desenvolvimento inicial:

- versões `0.Y.Z` indicam instabilidade possível;
- alterações incompatíveis podem ocorrer entre versões menores;
- toda incompatibilidade deve continuar explícita;
- o estado `estavel` deve ser reservado para documentos suficientemente testados, ainda que sua versão permaneça inferior a `1.0.0` durante a fase inicial do framework.

A adoção de `1.0.0` indica maturidade, documentação suficiente e confiança para uso geral, não perfeição ou imutabilidade.

## 11. Histórico de alterações

Todo documento deve possuir uma seção `Histórico de alterações` ou arquivo de changelog equivalente.

Formato mínimo:

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Primeira publicação | Projeto Pragmatismo Cívico |

O histórico deve registrar alterações documentais, não cada commit técnico irrelevante.

## 12. Registro de decisão da mudança

Alterações menores ou maiores devem informar:

1. problema identificado;
2. evidências ou manifestações consideradas;
3. alternativas avaliadas;
4. decisão adotada;
5. impacto esperado;
6. compatibilidade;
7. orientação de migração, quando necessária;
8. data ou condição de revisão.

Esse registro pode constar do próprio documento, de uma proposta de mudança, de uma issue ou de um pull request, desde que exista referência rastreável.

Mudanças do campo `status` devem também conter o registro de transição exigido pelo PPC-000A.

## 13. Dependências e relacionamentos

As dependências devem utilizar identificadores oficiais, evitando referências apenas por título.

### 13.1 Regras

- uma dependência obrigatória deve constar em `depende_de`;
- uma saída consumida por outro padrão deve constar em `produz_entrada_para`;
- relações complementares devem constar em `relaciona_se_com`;
- substituições devem ser recíprocas nos dois documentos;
- dependências circulares devem ser evitadas e justificadas quando inevitáveis;
- links internos devem ser verificados antes da publicação.

### 13.2 Coerência recíproca

Quando o documento A declara que produz entrada para B, o documento B deve declarar A como dependência, sempre que a relação for obrigatória.

## 14. Compatibilidade e migração

Uma mudança `parcial` ou `incompativel` deve apresentar:

- versão de origem;
- versão de destino;
- documentos e ferramentas afetados;
- campos ou etapas alterados;
- ações necessárias para migração;
- prazo recomendado;
- tratamento de registros históricos;
- riscos de não migrar.

Aplicações concluídas não devem ser reescritas para aparentar conformidade retroativa. Devem preservar a versão realmente utilizada.

## 15. Publicação e fonte canônica

A versão canônica é a registrada na branch padrão do repositório oficial, salvo declaração expressa em contrário.

Cada publicação deve, quando possível, permitir identificar:

- versão documental;
- commit correspondente;
- data de publicação;
- estado do documento;
- histórico anterior.

O portal GitHub Pages é uma interface de consulta. Em divergência técnica, prevalece o conteúdo versionado no repositório.

## 16. Validação mínima

Antes da publicação ou atualização, deve-se verificar:

- presença dos campos obrigatórios;
- unicidade do identificador;
- validade do formato da versão;
- coerência entre versão e tipo de mudança;
- validade do status;
- correspondência da mudança de estado com o PPC-000A;
- datas em formato padronizado;
- existência dos documentos referenciados;
- reciprocidade das dependências obrigatórias;
- ausência de links internos quebrados;
- atualização do histórico;
- declaração de compatibilidade;
- atualização do portal e do roadmap, quando aplicável.

## 17. Automação futura

O esquema foi concebido para permitir, posteriormente:

- validação automática em GitHub Actions;
- geração de catálogo de documentos;
- exibição de versão e status no portal;
- detecção de referências quebradas;
- mapas de dependência;
- geração de changelogs;
- alertas de revisão vencida;
- publicação de versões para impressão.

A automação deve apoiar a governança, não substituir revisão humana ou julgamento metodológico.

## 18. Migração do acervo existente

A adoção será progressiva:

1. novos documentos adotam o padrão desde a criação;
2. documentos alterados estruturalmente recebem metadados na mesma revisão;
3. documentos centrais são migrados antes de materiais auxiliares;
4. inconsistências encontradas são registradas e corrigidas sem reescrever o histórico;
5. a migração completa deve possuir checklist e acompanhamento no roadmap.

A ausência temporária de metadados em documento antigo não o invalida, mas deve ser tratada como dívida documental.

## 19. Critérios de conformidade

Um documento atende ao PPC-META-001 quando:

- possui identificador único;
- declara versão e status;
- identifica responsáveis;
- registra datas relevantes;
- declara relacionamentos e substituições;
- mantém histórico de alterações;
- informa compatibilidade;
- preserva versões anteriores;
- referencia uma fonte canônica;
- pode ser auditado sem depender da memória dos autores.

## 20. Limitações

Este padrão não resolve sozinho:

- a aprovação política ou técnica de conteúdos;
- a qualidade metodológica de um PPC;
- a governança de conflitos;
- a preservação externa de longo prazo;
- o ciclo completo de consulta e aprovação;
- a segurança de dados sensíveis.

Esses temas devem ser tratados pelos documentos próprios de governança, arquitetura e ciclo de vida.

## 21. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.2.0 | 2026-07-17 | evolução compatível | Integração com o PPC-000A e adoção de metadados no próprio documento | Projeto Pragmatismo Cívico |
| 0.1.0 | 2026-07-17 | inicial | Primeira publicação do padrão de metadados e versionamento | Projeto Pragmatismo Cívico |
