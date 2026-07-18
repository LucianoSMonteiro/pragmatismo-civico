---
id: MATRIZ-PPC-001
titulo: Matriz de Avaliação de Políticas Públicas
versao: 0.1.0
status: rascunho
tipo: ferramenta
idioma: pt-BR
data_criacao: null
data_versao: 2026-07-18
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - PPC-001
  - PPC-002
  - PPC-003
  - PPC-META-001
  - ARQ-001
produz_entrada_para: []
relaciona_se_com:
  - CICLO-PC-001
  - FICHA-PPC-002
  - FICHA-PPC-003
  - FICHA-PPC-004
  - MODELO-INDICADORES-001
substitui: []
substituido_por: null
compatibilidade: inicial
proxima_revisao: null
documentos_associados:
  - id: PPC-002
    versao: 0.1.0
  - id: PPC-003
    versao: 0.1.0
---

# Matriz de Avaliação de Políticas Públicas

## Status

Rascunho inicial preparado para aplicação experimental e revisão pública. Não há registro de transição formal para os estados `piloto` ou `revisao-publica`.

O campo `documentos_associados` registra os padrões e versões que esta ferramenta operacionaliza.

## Finalidade

Oferecer um método transparente para comparar alternativas de política pública por critérios explícitos, evidências, riscos, custos e resultados esperados.

A matriz não substitui a decisão democrática. Ela torna a decisão mais clara, comparável, justificável e auditável.

## Pré-condições

A matriz somente deve ser aplicada quando houver:

- problema público definido;
- linha de base;
- objetivos verificáveis;
- ao menos duas alternativas relevantes, incluindo a opção de não agir quando aplicável;
- evidências e incertezas registradas.

O diagnóstico deve seguir o `PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md`.

## Regras gerais

1. Os critérios devem ser definidos antes da pontuação.
2. Os pesos devem somar 100%.
3. Toda nota deve possuir justificativa e fonte.
4. Incerteza não pode ser escondida por uma nota precisa.
5. Direitos fundamentais não podem ser compensados por ganhos em outros critérios.
6. Alternativas inviáveis juridicamente ou incompatíveis com os princípios fundadores devem ser rejeitadas antes da classificação final.
7. A matriz deve ser acompanhada de análise narrativa.

## Escala de notas

| Nota | Interpretação |
|---:|---|
| 0 | desempenho inexistente, incompatível ou evidência contrária forte |
| 1 | desempenho muito baixo |
| 2 | desempenho baixo |
| 3 | desempenho intermediário ou incerto |
| 4 | desempenho alto |
| 5 | desempenho muito alto, sustentado por evidência robusta |

Quando a evidência for insuficiente, usar a marcação `I` — insuficiente — em vez de inventar uma nota.

## Critérios mínimos

| Critério | Pergunta central |
|---|---|
| Efetividade | A alternativa tem probabilidade de produzir o resultado pretendido? |
| Impacto na qualidade de vida | Qual melhoria concreta pode gerar para as pessoas? |
| Equidade | Como benefícios, custos e riscos serão distribuídos? |
| Direitos e dignidade | A alternativa respeita direitos, liberdades e salvaguardas? |
| Eficiência | Os resultados justificam recursos, tempo e capacidade utilizados? |
| Sustentabilidade | É sustentável ambiental, social, econômica e institucionalmente? |
| Viabilidade jurídica e institucional | Pode ser executada dentro das regras e capacidades existentes ou adaptáveis? |
| Viabilidade operacional e tecnológica | Há pessoas, processos, infraestrutura e tecnologia adequados? |
| Transparência e auditabilidade | A execução e os resultados podem ser acompanhados e verificados? |
| Riscos e efeitos adversos | Quais danos, falhas ou consequências não intencionais podem ocorrer? |
| Escalabilidade e adaptabilidade | Pode crescer ou ser ajustada sem perder qualidade? |
| Qualidade da evidência | Quão confiável é a base empírica da alternativa? |

Critérios adicionais podem ser incluídos quando necessários, desde que sua utilidade seja justificada.

## Pesos

Os pesos não são fixos. Devem refletir o problema, o contexto e as prioridades legitimamente definidas.

Para cada peso, registrar:

- justificativa;
- participantes da definição;
- conflitos de interesse;
- sensibilidade do resultado a mudanças no peso.

Direitos e salvaguardas funcionam como limites, não apenas como itens compensáveis.

## Cálculo

Para cada critério:

`pontuação ponderada = nota × peso`

Quando os pesos forem expressos em porcentagem e as notas variarem de 0 a 5, a pontuação total poderá ser normalizada para 0 a 100.

A pontuação numérica é um apoio. Não é uma decisão automática.

## Modelo de matriz

| Critério | Peso | Alternativa A | Alternativa B | Alternativa C | Não agir |
|---|---:|---:|---:|---:|---:|
| Efetividade |  |  |  |  |  |
| Qualidade de vida |  |  |  |  |  |
| Equidade |  |  |  |  |  |
| Direitos e dignidade |  |  |  |  |  |
| Eficiência |  |  |  |  |  |
| Sustentabilidade |  |  |  |  |  |
| Viabilidade jurídica e institucional |  |  |  |  |  |
| Viabilidade operacional e tecnológica |  |  |  |  |  |
| Transparência e auditabilidade |  |  |  |  |  |
| Riscos e efeitos adversos |  |  |  |  |  |
| Escalabilidade e adaptabilidade |  |  |  |  |  |
| Qualidade da evidência |  |  |  |  |  |
| **Total** | **100%** |  |  |  |  |

Cada célula deve remeter a uma justificativa detalhada.

## Análise de incerteza

Para cada alternativa, registrar:

- grau de confiança das evidências;
- hipóteses críticas;
- variáveis externas;
- intervalos ou cenários possíveis;
- informações que poderiam alterar a classificação.

Recomenda-se testar cenários otimista, central e adverso.

## Análise de sensibilidade

Recalcular a matriz com variações plausíveis nos pesos e notas.

Uma alternativa cuja liderança desapareça após pequenas alterações deve ser tratada como decisão sensível, exigindo deliberação adicional, piloto ou produção de novas evidências.

## Avaliação de riscos

Os riscos devem ser avaliados por:

- probabilidade;
- impacto;
- reversibilidade;
- população exposta;
- capacidade de prevenção e resposta.

Riscos graves a direitos, integridade física, privacidade ou estabilidade institucional exigem salvaguardas específicas e podem tornar uma alternativa inadmissível.

## Valor público

A análise deve considerar o valor público esperado: melhoria efetiva da qualidade de vida em relação aos recursos, riscos, tempo e impactos necessários.

Isso impede que resultados isolados sejam avaliados sem considerar custos, distribuição, sustentabilidade e confiança institucional.

## Registro da decisão

O relatório final deve indicar:

1. alternativa escolhida;
2. alternativas rejeitadas;
3. critérios e pesos utilizados;
4. justificativas das notas;
5. evidências e limitações;
6. riscos aceitos e mitigados;
7. opiniões divergentes relevantes;
8. condições de implementação;
9. indicadores de acompanhamento;
10. data ou condição de revisão.

## Presunção de revisabilidade

Toda decisão pública é tratada como uma hipótese sujeita a teste, mensuração e revisão.

A escolha deve prever uma das seguintes decisões futuras:

- manter;
- ajustar;
- ampliar;
- simplificar;
- substituir;
- encerrar.

## Salvaguardas contra mau uso

A matriz não deve ser usada para:

- fabricar aparência de objetividade;
- esconder decisões políticas atrás de fórmulas;
- escolher pesos depois de conhecer o resultado;
- compensar violações de direitos com benefícios econômicos;
- excluir participação relevante;
- apresentar evidência fraca como certeza.

## Critério de qualidade

A avaliação é considerada auditável quando um terceiro consegue reconstruir:

- o problema;
- as alternativas;
- os critérios;
- os pesos;
- as evidências;
- as notas;
- as incertezas;
- a justificativa da decisão.

## Evolução

A matriz deve ser testada em casos reais e revisada com base em resultados, dificuldades de uso e avaliações independentes, sempre preservando os princípios fundadores do Pragmatismo Cívico.

## Histórico de alterações da ferramenta

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Migração documental para o PPC-META-001, identificação formal e vínculo às versões 0.1.0 dos PPC-002 e PPC-003 | Projeto Pragmatismo Cívico |
