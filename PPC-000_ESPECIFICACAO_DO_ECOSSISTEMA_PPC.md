---
id: PPC-000
titulo: Especificação do Ecossistema PPC
versao: 0.1.0
status: rascunho
tipo: padrao-transversal
idioma: pt-BR
data_criacao: null
data_versao: 2026-07-17
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - FRAMEWORK-DE-REFERENCIA
produz_entrada_para:
  - PPC-001
  - PPC-002
  - PPC-003
  - PPC-004
  - PPC-005
  - PPC-006
  - PPC-007
  - PPC-008
relaciona_se_com:
  - PPC-000A
  - PPC-META-001
  - ARQ-001
  - GOV-001
substitui: []
substituido_por: null
compatibilidade: inicial
proxima_revisao: null
---

# PPC-000 — Especificação do Ecossistema PPC

## Status

Rascunho inicial para discussão pública.

## 1. Objetivo

Estabelecer regras comuns para criação, organização, revisão, validação, versionamento e descontinuação dos Padrões do Pragmatismo Cívico — PPCs.

O PPC-000 é a metanorma do ecossistema metodológico. Ele não define uma etapa específica de política pública; define como os demais padrões devem ser construídos e mantidos.

## 2. Escopo

Aplica-se a todos os documentos identificados como PPC.

Não substitui:

- os princípios fundadores;
- o `FRAMEWORK_DE_REFERENCIA.md`;
- a `SPECIFICATION.md`;
- os instrumentos práticos associados a cada padrão.

## 3. Identificação obrigatória

Todo PPC deve conter:

- código único;
- título;
- versão;
- status;
- data da versão;
- autores ou responsáveis;
- histórico de alterações;
- dependências;
- ferramentas associadas.

A estrutura, a sintaxe e as regras detalhadas desses elementos são definidas pelo `PPC-META-001_METADADOS_E_VERSIONAMENTO.md`.

## 4. Estados do ciclo de vida

Os estados canônicos do ecossistema são:

1. **Ideia** — necessidade ou hipótese ainda não formalizada.
2. **Proposta** — iniciativa formal submetida à análise de admissibilidade.
3. **Rascunho** — documento estruturado ainda não suficientemente validado.
4. **Revisão pública** — versão aberta a contribuições estruturadas.
5. **Piloto** — padrão em aplicação controlada para geração de evidências.
6. **Estável** — versão validada e recomendada dentro do escopo declarado.
7. **Em revisão** — padrão estável submetido a reavaliação formal.
8. **Substituído** — padrão sucedido por outro documento identificado.
9. **Obsoleto** — padrão não recomendado, sem sucessor obrigatório.
10. **Arquivado** — documento retirado do catálogo ativo e preservado para memória.

Os valores de metadados, critérios de entrada e saída, transições permitidas, responsabilidades e registros obrigatórios são definidos pelo `PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md`.

Nenhum PPC deve nascer diretamente como estável. Mudanças de estado devem ser justificadas, registradas e comunicadas.

## 5. Estrutura mínima obrigatória

Todo PPC deve conter, no mínimo:

### 5.1 Objetivo

Qual problema metodológico o padrão resolve.

### 5.2 Escopo

Quando deve e quando não deve ser utilizado.

### 5.3 Princípios relacionados

Quais princípios fundadores concretiza.

### 5.4 Entradas

Informações, documentos, dados ou decisões anteriores necessários.

### 5.5 Processo

Etapas de aplicação, responsabilidades e pontos de controle.

### 5.6 Saídas

Produtos documentais ou decisórios gerados.

### 5.7 Critérios mínimos

Condições necessárias para considerar o padrão adequadamente aplicado.

### 5.8 Indicadores de qualidade

Como avaliar utilidade, completude, clareza, rastreabilidade e custo de aplicação.

### 5.9 Limitações

Condições em que o padrão pode não ser suficiente.

### 5.10 Referências

Fontes teóricas, normativas e empíricas relevantes.

## 6. Dependências e interoperabilidade

Todo PPC deve declarar:

- **depende de** — padrões ou documentos necessários antes da aplicação;
- **produz entrada para** — padrões que utilizam seus resultados;
- **relaciona-se com** — documentos complementares sem dependência obrigatória;
- **ferramentas associadas** — fichas, matrizes, checklists e modelos.

A numeração não implica independência. O ecossistema deve funcionar como um fluxo coerente.

Exemplo:

```text
PPC-001 — Diagnóstico
    ↓
PPC-002 — Formulação e comparação de alternativas
    ↓
PPC-003 — Avaliação e recomendação
    ↓
PPC-004 — Registro e justificação da decisão
```

## 7. Versionamento

O versionamento deve seguir três níveis:

- **X.Y.Z**
- **Z — alteração editorial:** correções sem mudança metodológica;
- **Y — evolução compatível:** melhorias que preservam compatibilidade;
- **X — mudança incompatível:** alteração estrutural ou metodológica relevante.

Mudanças incompatíveis devem:

- justificar necessidade;
- indicar impactos;
- oferecer orientação de transição;
- preservar versões anteriores para auditoria.

O detalhamento operacional do versionamento, da compatibilidade e da migração é definido pelo `PPC-META-001_METADADOS_E_VERSIONAMENTO.md`.

## 8. Critérios para criação de um novo PPC

Uma proposta deve demonstrar:

1. problema real não resolvido adequadamente por padrões existentes;
2. coerência com os princípios fundadores;
3. ausência de duplicação desnecessária;
4. aplicabilidade prática;
5. possibilidade de avaliação;
6. custo metodológico proporcional ao benefício esperado;
7. compatibilidade com o restante do ecossistema.

## 9. Proporcionalidade metodológica

> O rigor metodológico deve ser proporcional ao impacto, ao custo, ao risco, à incerteza e à irreversibilidade da decisão.

Cada PPC deve indicar formas simplificadas e completas de aplicação quando isso for tecnicamente possível.

## 10. Validação

Antes de alcançar o estado estável, um PPC deve passar, quando aplicável, por:

- revisão de coerência;
- revisão técnica;
- revisão pública;
- teste de usabilidade;
- aplicação-piloto;
- registro de limitações;
- avaliação do custo de aplicação;
- incorporação documentada das lições aprendidas.

A decisão de estabilidade deve observar os portões e os registros definidos pelo PPC-000A.

## 11. Qualidade do padrão

A qualidade de um PPC deve ser avaliada em pelo menos cinco dimensões:

1. **Utilidade** — resolve o problema declarado?
2. **Clareza** — pode ser aplicado sem orientação informal dos autores?
3. **Reprodutibilidade** — equipes distintas produzem resultados comparáveis?
4. **Rastreabilidade** — decisões e alterações podem ser reconstruídas?
5. **Proporcionalidade** — o valor gerado justifica a complexidade introduzida?

## 12. Obsolescência e substituição

Um PPC pode ser declarado obsoleto quando:

- deixar de resolver o problema;
- apresentar custo excessivo;
- houver evidência de efeitos indesejados;
- for substituído por método superior;
- tornar-se incompatível com o núcleo do framework.

A obsolescência não apaga o documento. O histórico deve permanecer acessível.

As diferenças entre substituição, obsolescência e arquivamento, bem como suas exigências de migração e comunicação, são definidas pelo PPC-000A.

## 13. Governança de mudanças

Toda mudança deve registrar:

- problema identificado;
- evidência utilizada;
- alternativas consideradas;
- decisão tomada;
- responsáveis;
- impactos esperados;
- data de revisão futura.

Os metadados, o histórico e a compatibilidade da mudança devem seguir o PPC-META-001. As transições de estado devem seguir o PPC-000A.

## 14. Regra de simplicidade

> Nenhum PPC deve existir apenas para aumentar formalidade documental.

Padrões devem melhorar decisões, proteger direitos, aumentar transparência ou preservar aprendizado. Caso contrário, devem ser simplificados ou removidos.

## 15. Padrões complementares

O PPC-000 estabelece a governança geral do ecossistema e pode ser detalhado por padrões transversais, sem transferir ou alterar seus princípios fundamentais.

Atualmente, complementam este documento:

- `PPC-META-001_METADADOS_E_VERSIONAMENTO.md` — identificação, metadados, histórico, versionamento, compatibilidade e migração documental;
- `PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md` — estados, transições, validação, manutenção, substituição, obsolescência e arquivamento.

## 16. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Migração documental para o PPC-META-001, sem mudança substantiva das regras | Projeto Pragmatismo Cívico |
