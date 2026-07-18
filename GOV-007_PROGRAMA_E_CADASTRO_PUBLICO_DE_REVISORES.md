---
id: GOV-007
titulo: Programa e Cadastro Público de Revisores
versao: 0.1.0
status: rascunho
tipo: governanca
idioma: pt-BR
data_criacao: 2026-07-18
data_versao: 2026-07-18
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - FRAMEWORK-DE-REFERENCIA
  - GOV-003
  - GOV-004
  - GOV-005
  - GOV-006
  - PPC-META-001
  - ARQ-001
produz_entrada_para:
  - FICHA-GOV-007
  - CADASTRO-REVISORES
relaciona_se_com:
  - GOV-001
  - GOV-002
  - ARQ-002
substitui: []
substituido_por: null
compatibilidade: inicial
proxima_revisao: null
ferramentas_associadas:
  - FICHA_GOV-007_CANDIDATURA_E_AVALIACAO_DE_REVISOR.md
  - CADASTRO_PUBLICO_DE_REVISORES.md
---

# GOV-007 — Programa e Cadastro Público de Revisores

## 1. Objetivo

Criar uma base pública, plural e verificável de pessoas aptas a revisar propostas conforme o GOV-006, sem transformar cadastro em título honorífico, vínculo empregatício ou garantia de participação em painéis.

## 2. Princípios

- candidatura aberta e critérios públicos;
- competência demonstrada por diferentes formas de conhecimento;
- independência e conflitos declarados;
- diversidade de trajetórias e vínculos, sem coleta obrigatória de dados sensíveis;
- participação voluntária e revogável;
- exposição mínima de dados pessoais;
- seleção de painéis por pertinência e independência, não por prestígio;
- registro de decisões de admissão, suspensão e encerramento;
- acessibilidade e ausência de retaliação por recusa ou indisponibilidade.

## 3. Escopo do programa

O programa mantém:

1. formulário público de candidatura;
2. avaliação de elegibilidade;
3. cadastro público de pessoas elegíveis;
4. disponibilidade declarada;
5. áreas de competência e experiência;
6. vínculos e conflitos gerais;
7. histórico de participação em painéis;
8. revisão periódica do cadastro;
9. regras de suspensão, saída e reconsideração.

## 4. Elegibilidade

A pessoa candidata deve:

- aceitar o Código de Conduta e as regras de revisão;
- compreender que a função é voluntária, salvo acordo específico publicado;
- demonstrar competência técnica, metodológica, institucional, comunitária ou vivencial pertinente;
- declarar vínculos capazes de afetar independência;
- informar disponibilidade realista;
- concordar com a publicação dos campos mínimos do cadastro;
- comprometer-se a recusar painéis para os quais não tenha competência, tempo ou independência.

Titulação, vínculo acadêmico ou cargo público não são requisitos universais. Experiência prática e conhecimento vivido podem ser materialmente relevantes.

## 5. Candidatura

A candidatura usa a `FICHA-GOV-007` ou o formulário público de issue. Deve informar apenas:

- identificação pública escolhida;
- perfil público no GitHub;
- áreas de competência;
- síntese de experiência verificável;
- setores, territórios ou contextos conhecidos;
- vínculos institucionais relevantes;
- conflitos gerais conhecidos;
- idiomas de trabalho;
- faixa de disponibilidade;
- links públicos opcionais;
- consentimento para publicação dos campos mínimos.

Não devem ser solicitados em issue pública endereço, telefone, documento oficial, data de nascimento, dados médicos, renda, identidade protegida ou contato privado.

## 6. Avaliação da candidatura

A avaliação verifica:

- completude e coerência das informações;
- aderência ao Código de Conduta;
- competência demonstrada nas áreas declaradas;
- capacidade de produzir revisão fundamentada;
- conflitos e limitações conhecidos;
- concordância com publicidade mínima;
- existência de fraude, falsificação ou omissão material.

Resultados possíveis:

- elegível;
- elegível com escopo limitado;
- solicitar complementação;
- não elegível neste momento;
- suspender análise por risco ou conflito não resolvido.

A decisão deve ser motivada e permitir reconsideração.

## 7. Estados do cadastro

| Estado | Significado |
|---|---|
| candidato | candidatura ainda em análise |
| elegível | pode ser convidado para painéis compatíveis |
| ativo | elegível e disponível no período atual |
| indisponível | permanece elegível, mas não recebe convites |
| suspenso | participação interrompida enquanto condição é analisada |
| encerrado | cadastro removido por solicitação, expiração ou decisão motivada |

Somente pessoas em estado `elegível` ou `ativo` podem compor painéis.

## 8. Cadastro público

O `CADASTRO-REVISORES` publica:

- identificador `REV-NNN`;
- identificação pública e perfil GitHub;
- áreas de competência;
- síntese de trajetórias ou setores;
- vínculos institucionais declarados;
- idiomas;
- disponibilidade agregada;
- estado;
- data de admissão e próxima revisão;
- participações concluídas, quando existirem.

Conflitos específicos de uma proposta pertencem ao registro do painel, não ao cadastro geral.

## 9. Proteção de dados

O programa adota minimização de dados. Informações não necessárias à seleção e à transparência não devem ser coletadas ou publicadas.

A pessoa pode solicitar correção, indisponibilidade ou encerramento do cadastro. A remoção de dados públicos não apaga registros decisórios históricos que precisem preservar autoria, voto, conflito ou responsabilidade, mas esses registros devem manter apenas o necessário.

Enquanto não houver canal privado formal, nenhuma informação confidencial deve ser enviada por issue pública.

## 10. Disponibilidade

A disponibilidade é declarada por faixa:

- até 2 horas por mês;
- de 2 a 5 horas por mês;
- de 5 a 10 horas por mês;
- acima de 10 horas por mês;
- indisponível temporariamente.

Ela deve ser confirmada antes de cada painel. Recusar convite não reduz elegibilidade nem gera prioridade negativa.

## 11. Formação de painéis

A secretaria seleciona candidatos conforme:

1. competência pertinente ao objeto;
2. independência em relação à autoria e ao resultado;
3. disponibilidade confirmada;
4. diversidade de trajetórias, setores e perspectivas;
5. participação de pessoas afetadas quando material;
6. equilíbrio de carga e prevenção de concentração;
7. requisitos de quórum do GOV-006.

Não se deve selecionar painel apenas por ordem de inscrição, notoriedade ou proximidade com mantenedores.

## 12. Conflitos e impedimentos

Vínculos gerais são declarados no cadastro. Antes de cada painel, a pessoa atualiza conflitos específicos e pode:

- participar plenamente;
- participar apenas como fonte de informação;
- abster-se de tema específico;
- recusar a designação;
- ser substituída por impedimento.

Omissão material pode gerar suspensão e revisão de decisões anteriores.

## 13. Revisão periódica

A elegibilidade deve ser revista ao menos anualmente ou quando houver:

- mudança relevante de vínculo;
- indisponibilidade prolongada;
- violação de conduta;
- omissão de conflito;
- desempenho reiteradamente insuficiente;
- solicitação da própria pessoa;
- nova evidência sobre a candidatura.

## 14. Suspensão e encerramento

Suspensão exige motivo registrado e oportunidade de resposta, salvo risco imediato. Encerramento pode ocorrer por solicitação, expiração sem confirmação, perda de elegibilidade ou violação grave.

Crítica fundamentada, voto divergente, recusa por conflito ou indisponibilidade não constituem motivo de sanção.

## 15. Regime inicial

O cadastro começa sem revisores presumidos. Mantenedores, autores e colaboradores somente entram após candidatura e avaliação registradas.

A existência do programa não significa que os mínimos permanentes do GOV-006 foram atingidos. Até isso ocorrer, permanecem os limites do regime provisório.

## 16. Indicadores

- candidaturas recebidas e concluídas;
- tempo de análise;
- pessoas elegíveis, ativas e indisponíveis;
- diversidade de trajetórias e vínculos;
- áreas sem cobertura;
- convites aceitos e recusados;
- conflitos declarados;
- concentração de participações;
- revisões periódicas vencidas;
- suspensões, encerramentos e reconsiderações.

## 17. Critérios de qualidade

O programa atende ao GOV-007 quando:

- não publica dados pessoais desnecessários;
- decisões de elegibilidade são motivadas;
- cadastro e disponibilidade estão atualizados;
- painéis atendem competência, independência e diversidade;
- conflitos são tratados antes da deliberação;
- recusas não geram retaliação;
- registros permitem auditoria;
- a ausência de capacidade é declarada honestamente.

## 18. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Criação do programa, critérios de candidatura, proteção de dados e formação de painéis | Projeto Pragmatismo Cívico |
