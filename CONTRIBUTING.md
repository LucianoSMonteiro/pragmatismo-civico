---
id: GOV-003
titulo: Guia de Contribuição do Pragmatismo Cívico
versao: 0.4.0
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
  - GOV-007
produz_entrada_para: []
relaciona_se_com:
  - GOV-001
  - GOV-002
  - GOV-004
  - FICHA-GOV-005
  - FICHA-GOV-006
  - FICHA-GOV-007
  - CADASTRO-REVISORES
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# Contribuindo com o Pragmatismo Cívico

Obrigado pelo interesse em contribuir. A abertura do projeto não significa ausência de critérios. Toda contribuição deve ampliar utilidade sem descaracterizar princípios fundadores.

## 1. Antes de contribuir

Leia, nesta ordem:

1. `README.md`;
2. `CARTA_DE_PRINCIPIOS.md`;
3. `FRAMEWORK_DE_REFERENCIA.md`;
4. `SPECIFICATION.md`;
5. `GOV-005_PROCESSO_DE_PROPOSTAS_DE_MUDANCA.md`;
6. `GOV-006_POLITICA_DE_REVISAO_E_APROVACAO.md`;
7. `GOV-007_PROGRAMA_E_CADASTRO_PUBLICO_DE_REVISORES.md`, se pretende revisar;
8. este guia e o `CODE_OF_CONDUCT.md`.

Para mudanças formais, use a `FICHA-GOV-005` ou o formulário **Proposta de mudança**. Revisões moderadas ou superiores usam a `FICHA-GOV-006`. Candidaturas a revisor usam a `FICHA-GOV-007` ou o formulário **Candidatura a revisor**.

## 2. Regra central

> Novas propostas existem para concretizar os princípios fundadores, não para substituí-los silenciosamente.

Toda contribuição deve preservar:

- cidadão no centro;
- avaliação por resultados e evidências;
- transparência, auditabilidade e responsabilidade;
- dignidade e direitos;
- sustentabilidade integral;
- cooperação e pluralidade;
- revisão e aprendizado;
- neutralidade partidária.

## 3. Formas de contribuição

São bem-vindas:

- correções de clareza, ortografia, acessibilidade ou links;
- evidências e referências verificáveis;
- aprimoramentos de métodos, indicadores e ferramentas;
- estudos de caso documentados;
- identificação de riscos e limitações;
- traduções;
- revisão fundamentada;
- candidatura ao programa público de revisores.

## 4. O que não será aceito

- propaganda partidária ou eleitoral;
- ataques pessoais ou intimidação;
- fabricação, manipulação ou ocultação de evidências;
- ocultação de conflitos materiais;
- violação de direitos em nome de eficiência;
- complexidade sem utilidade demonstrável;
- duplicação sem justificativa;
- publicação de dados pessoais sensíveis desnecessários.

## 5. Teste de coerência

Antes de enviar uma proposta, responda:

1. Qual problema concreto resolve?
2. Qual princípio concretiza?
3. Já existe conteúdo com a mesma função?
4. Que evidências ou experiências a sustentam?
5. Quais limitações e riscos existem?
6. Como seu valor será verificado?
7. Simplifica ou complica o uso?
8. Exige atualização de outros documentos?
9. Pode produzir impacto desigual?
10. Preserva neutralidade e direitos?

## 6. Como propor mudanças

### 6.1 Correções editoriais

Correções de baixo impacto podem ser apresentadas diretamente em pull request quando não alterarem interpretação, obrigação, método ou compatibilidade. A CI deve ser aprovada.

### 6.2 Mudanças formais

Mudanças corretivas relevantes, metodológicas, arquiteturais, de governança, fundacionais, de ciclo de vida ou emergenciais seguem o GOV-005.

A issue é o registro canônico da proposta. O pull request implementa a decisão, mas não substitui triagem, revisão ou justificativa.

### 6.3 Revisão e aprovação

A revisão segue o GOV-006. O rigor cresce com impacto, risco e irreversibilidade. Insuficiência de revisores deve ser declarada, não ocultada por reclassificação artificial.

### 6.4 Candidatura a revisor

A candidatura segue o GOV-007 e deve ser aberta pelo formulário **Candidatura a revisor** ou pela `FICHA-GOV-007`.

A issue é pública. Não inclua endereço, telefone, documento oficial, data de nascimento, informação médica, renda, contato privado ou dado de terceiro.

A candidatura deve informar:

- identificação pública;
- competências e limites;
- experiência pertinente;
- contextos conhecidos;
- vínculos e conflitos gerais;
- idiomas;
- disponibilidade;
- consentimento para publicação mínima.

Elegibilidade não garante convite, remuneração ou posição institucional. Mantenedores e autores não entram automaticamente no cadastro.

## 7. Mudanças no núcleo e nas aplicações

### Núcleo normativo

Carta, Especificação e Framework são fundacionais. Não podem adquirir estabilidade por decisão unilateral enquanto faltar instância plural.

### Métodos e ferramentas

Podem evoluir com maior frequência, desde que permaneçam compatíveis, úteis e rastreáveis.

### Aplicações

Devem declarar contexto, hipóteses, dados, limitações, versões e resultados. Novos casos serão publicados em `casos/`.

## 8. Evidências e referências

- identifique fonte, data e contexto;
- prefira fontes primárias;
- diferencie fato, hipótese, interpretação e opinião;
- declare incertezas e evidências contrárias relevantes;
- não atribua mais força à evidência do que ela suporta.

## 9. Linguagem e acessibilidade

Use linguagem clara, respeitosa e compreensível. Defina termos técnicos ou ligue-os ao Glossário. Evite jargão, retórica partidária e barreiras desnecessárias.

## 10. Estudos de caso

Um caso deve conter, no mínimo:

1. problema e população afetada;
2. linha de base;
3. alternativas;
4. decisão e justificativa;
5. custos, riscos e responsáveis;
6. indicadores;
7. resultados;
8. limitações;
9. lições e revisão recomendada.

## 11. Conflitos de interesse

Contribuidores, revisores e decisores devem declarar vínculos capazes de influenciar materialmente uma proposta. Conflito pode exigir declaração, restrição, abstenção, impedimento ou substituição.

## 12. Revisão

As contribuições são avaliadas por:

- coerência com princípios;
- clareza e precisão;
- qualidade das evidências;
- utilidade e custo metodológico;
- direitos, equidade e sustentabilidade;
- compatibilidade e reversibilidade;
- capacidade de auditoria e manutenção;
- competência, independência e quórum;
- correspondência da implementação com a decisão.

Dissenso fundamentado deve ser preservado.

## 13. Pull requests

O template deve ser preenchido proporcionalmente. Mudanças formais referenciam proposta, registro de revisão, compatibilidade, conflitos, reversão e CI.

Aprovar a proposta não aprova automaticamente qualquer implementação. O diff deve corresponder à decisão.

## 14. Privacidade e canais públicos

Issues e pull requests são públicos. Enquanto não houver canal privado formal, não envie informação confidencial. Dados sensíveis devem ser omitidos, agregados ou tratados por processo específico antes da coleta.

## 15. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Migração documental das regras de contribuição | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Integração do GOV-005 e do formulário de proposta | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Integração do GOV-006, registro de revisão e template de PR | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-18 | compatível | Integração do GOV-007, candidatura pública, cadastro e salvaguardas de privacidade | Projeto Pragmatismo Cívico |
