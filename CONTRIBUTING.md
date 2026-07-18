---
id: GOV-003
titulo: Guia de Contribuição do Pragmatismo Cívico
versao: 0.3.0
status: rascunho
tipo: governanca
idioma: pt-BR
data_criacao: null
data_versao: 2026-07-18
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - FRAMEWORK-DE-REFERENCIA
  - PPC-000
  - PPC-000A
  - PPC-META-001
  - ARQ-001
  - GOV-005
  - GOV-006
produz_entrada_para: []
relaciona_se_com:
  - GOV-001
  - GOV-002
  - GOV-004
  - FICHA-GOV-005
  - FICHA-GOV-006
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# Contribuindo com o Pragmatismo Cívico

Obrigado pelo interesse em contribuir. O Pragmatismo Cívico é um framework aberto, mas sua abertura não significa ausência de critérios. Toda contribuição deve ampliar a utilidade do projeto sem descaracterizar seus princípios fundadores.

## 1. Antes de contribuir

Leia, nesta ordem:

1. `README.md`;
2. `CARTA_DE_PRINCIPIOS.md`;
3. `FRAMEWORK_DE_REFERENCIA.md`;
4. `SPECIFICATION.md`;
5. `GOV-005_PROCESSO_DE_PROPOSTAS_DE_MUDANCA.md`;
6. `GOV-006_POLITICA_DE_REVISAO_E_APROVACAO.md`;
7. este guia e o `CODE_OF_CONDUCT.md`.

Para mudanças formais, utilize a `FICHA_GOV-005_PROPOSTA_DE_MUDANCA.md` ou o formulário **Proposta de mudança** disponível nas issues. Revisões e decisões moderadas ou superiores devem possuir registro compatível com a `FICHA_GOV-006_REGISTRO_DE_REVISAO_E_APROVACAO.md`.

## 2. Regra central

> Novas propostas existem para concretizar os princípios fundadores, não para substituí-los silenciosamente.

Uma contribuição deve preservar, no mínimo:

- o cidadão no centro;
- a avaliação por resultados, não por rótulos ideológicos;
- o uso crítico de evidências;
- transparência, auditabilidade e responsabilidade;
- dignidade humana e direitos fundamentais;
- sustentabilidade integral;
- cooperação acima da polarização;
- revisão e melhoria contínua;
- neutralidade partidária do framework.

## 3. Formas de contribuição

São bem-vindas contribuições como:

- correções de clareza, ortografia ou consistência;
- referências técnicas e evidências relevantes;
- aprimoramento de definições e métodos;
- indicadores e instrumentos de avaliação;
- modelos e checklists práticos;
- estudos de caso documentados;
- identificação de riscos, limitações e efeitos adversos;
- traduções e melhorias de acessibilidade;
- propostas de organização que reduzam duplicidade e complexidade.

## 4. O que não será aceito

Não serão aceitas contribuições que:

- transformem o projeto em plataforma partidária ou eleitoral;
- defendam pessoas, governos ou campos ideológicos como autoridades incontestáveis;
- substituam evidências por slogans ou ataques pessoais;
- ocultem custos, riscos, incertezas ou conflitos de interesse;
- tratem eficiência como justificativa para violar direitos;
- criem complexidade sem utilidade prática demonstrável;
- dupliquem documentos ou conceitos sem necessidade;
- manipulem dados ou usem referências de forma seletiva e enganosa.

## 5. Teste de coerência

Antes de enviar uma proposta, responda:

1. Qual problema concreto esta contribuição resolve?
2. Qual princípio fundador ela concretiza?
3. Já existe conteúdo com a mesma função?
4. Que evidências ou experiências sustentam a proposta?
5. Quais são suas limitações e riscos?
6. Como seu valor poderá ser verificado?
7. Ela simplifica ou complica o uso do framework?
8. Exige atualização de outros documentos?
9. Pode gerar impacto desigual entre grupos ou territórios?
10. Preserva a neutralidade partidária e os direitos fundamentais?

## 6. Como propor mudanças

### 6.1 Correções editoriais de baixo impacto

Correções de ortografia, formatação, acessibilidade ou links podem ser apresentadas diretamente em pull request quando não alterarem interpretação, obrigação, método ou compatibilidade.

O pull request deve explicar o problema, o escopo e a ausência de efeito normativo. A CI deve ser aprovada antes da incorporação.

### 6.2 Mudanças formais

Mudanças corretivas relevantes, metodológicas, arquiteturais, de governança, fundacionais, de ciclo de vida ou emergenciais seguem o GOV-005.

A proposta deve ser aberta antes ou junto do trabalho de implementação e incluir:

- problema demonstrado;
- tipo e impacto;
- estado atual e alteração pretendida;
- princípios e documentos relacionados;
- evidências e limitações;
- alternativas consideradas, incluindo não alterar;
- benefícios, riscos e salvaguardas;
- compatibilidade e migração;
- plano de implementação, verificação e reversão;
- conflitos de interesse.

A issue é o registro canônico da proposta. O pull request implementa a decisão, mas não substitui triagem, revisão ou justificativa pública.

### 6.3 Revisão e aprovação

A revisão e a decisão seguem o GOV-006. O rigor depende do impacto:

- baixo impacto: revisão distinta da autoria quando houver capacidade;
- impacto moderado: ao menos duas manifestações fundamentadas;
- impacto alto: painel ampliado, independência proporcional e plano de migração;
- impacto crítico ou fundacional: fluxo reforçado, consulta pública e quórum permanente.

Enquanto a instância plural permanente não existir, propostas altas, críticas ou fundacionais permanecem sujeitas aos limites do regime provisório. A insuficiência de revisores deve ser declarada, não ocultada por reclassificação artificial.

## 7. Mudanças no núcleo e nas aplicações

### Núcleo normativo

Inclui a Carta de Princípios, a Especificação e o Framework de Referência. Mudanças nesses documentos são fundacionais, seguem fluxo reforçado e não podem adquirir estado estável por decisão unilateral enquanto não houver instância plural formalmente constituída.

### Metodologias e ferramentas

Podem evoluir com maior frequência, desde que permaneçam compatíveis com o núcleo, tenham utilidade verificável e sigam o rigor proporcional do GOV-005 e do GOV-006.

### Aplicações e estudos de caso

Devem declarar contexto, hipóteses, dados, limitações, versões utilizadas e resultados. Um caso específico não redefine automaticamente o framework inteiro.

## 8. Evidências e referências

Sempre que uma afirmação depender de dados ou pesquisa:

- identifique a fonte;
- prefira fontes primárias e verificáveis;
- informe data e contexto;
- não esconda evidências contrárias relevantes;
- diferencie fato, interpretação, hipótese e opinião;
- declare incertezas e limitações.

## 9. Linguagem e acessibilidade

Use linguagem clara, respeitosa e compreensível. Termos técnicos devem ser definidos ou ligados ao `GLOSSARIO.md`. Evite jargão desnecessário, retórica partidária e formulações que impeçam participação de pessoas não especialistas.

## 10. Estudos de caso

Um estudo de caso deve conter, no mínimo:

1. problema público;
2. população afetada;
3. linha de base;
4. alternativas consideradas;
5. decisão e justificativa;
6. custos, riscos e responsáveis;
7. indicadores;
8. resultados observados;
9. limitações;
10. lições aprendidas e revisão recomendada.

Novos casos devem seguir a estrutura híbrida do ARQ-003 e ser publicados em `casos/` quando houver uma entrega real.

## 11. Conflitos de interesse

Contribuidores, revisores e decisores devem declarar vínculos financeiros, partidários, profissionais, institucionais ou pessoais que possam influenciar materialmente uma proposta.

Conflitos relevantes são tratados pelo GOV-006. Declaração pode ser suficiente para vínculo de baixa intensidade; conflito material pode exigir restrição, abstenção, impedimento ou substituição.

## 12. Revisão

As contribuições serão avaliadas por:

- coerência com os princípios fundadores;
- clareza e precisão;
- qualidade das evidências;
- utilidade prática;
- proporcionalidade da complexidade;
- impactos sobre direitos, equidade e sustentabilidade;
- compatibilidade e reversibilidade;
- capacidade de auditoria e manutenção;
- conformidade da implementação com a decisão registrada;
- competência, independência e quórum do processo decisório.

Discordâncias fundamentadas são legítimas. O objetivo da revisão não é eliminar o dissenso, mas tornar decisões e justificativas públicas e verificáveis.

## 13. Pull requests

O template de pull request deve ser preenchido de forma proporcional. Mudanças formais devem referenciar a proposta canônica, o registro de revisão, a compatibilidade, os conflitos e as evidências de CI.

A aprovação de uma proposta não aprova automaticamente qualquer implementação. O diff deve corresponder à decisão e às condições registradas.

## 14. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Migração documental para o PPC-META-001, sem alteração substantiva das regras de contribuição | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Integração do GOV-005, da ficha canônica e do formulário de issue ao fluxo de contribuição | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Integração do GOV-006, do registro de revisão e do template de pull request | Projeto Pragmatismo Cívico |
