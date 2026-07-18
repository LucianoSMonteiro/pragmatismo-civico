---
id: GOV-006
titulo: Política de Revisão e Aprovação
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
  - GOV-001
  - GOV-004
  - GOV-005
  - PPC-000A
  - PPC-META-001
  - ARQ-001
produz_entrada_para: []
relaciona_se_com:
  - GOV-002
  - GOV-003
  - ARQ-002
  - FICHA-GOV-006
substitui: []
substituido_por: null
compatibilidade: inicial
proxima_revisao: null
ferramentas_associadas:
  - FICHA_GOV-006_REGISTRO_DE_REVISAO_E_APROVACAO.md
---

# GOV-006 — Política de Revisão e Aprovação

## 1. Objetivo

Definir regras permanentes para revisar e decidir propostas de mudança do Pragmatismo Cívico com competência explícita, independência proporcional, tratamento de conflitos, justificativa pública e preservação do dissenso.

A política impede que autoria, controle técnico do repositório ou votação sem fundamentos sejam tratados como aprovação substantiva.

## 2. Escopo

Aplica-se às propostas formais do GOV-005 e às decisões de criação, alteração, substituição, obsolescência ou arquivamento de documentos, ferramentas, automações, estudos de caso e componentes de publicação.

Correções editoriais de baixo impacto podem usar rito simplificado quando não alterarem obrigação, interpretação, método ou compatibilidade.

## 3. Princípios

1. **Separação de funções** — propor, revisar, decidir, implementar e verificar são funções distintas.
2. **Independência proporcional** — o rigor cresce com impacto, risco e irreversibilidade.
3. **Competência demonstrada** — participação exige conhecimento ou experiência pertinente.
4. **Publicidade por padrão** — composição, conflitos, fundamentos e decisão devem ser públicos.
5. **Impedimento efetivo** — conflito material pode exigir abstenção ou substituição.
6. **Dissenso preservado** — objeções e votos divergentes permanecem no registro.
7. **Direitos como limite** — maioria ou eficiência não legitimam violação de direitos ou integridade.
8. **Decisão motivada** — resultado sem fundamento não constitui aprovação válida.
9. **Compatibilidade explícita** — efeitos sobre versões e aplicações anteriores devem ser informados.
10. **Revisabilidade** — nova evidência ou vício processual pode justificar reconsideração.

## 4. Funções

### 4.1 Secretaria

Registra proposta, cronograma, composição, conflitos, documentos, pareceres, votos e decisão. Não decide mérito quando atuar apenas como secretaria.

### 4.2 Relatoria

Sintetiza problema, alternativas, evidências, riscos, objeções e questões decisórias. A pessoa proponente não deve relatar proposta moderada, alta ou crítica.

### 4.3 Revisores

Analisam mérito, método, direitos, riscos, compatibilidade e implementabilidade. Podem recomendar aprovação, condições, piloto, complementação, suspensão, rejeição ou insuficiência de evidência.

### 4.4 Instância decisória

Confirma competência e quórum, considera pareceres e contribuições e publica decisão motivada. Votação não substitui fundamentação.

### 4.5 Implementação e verificação

A implementação traduz a decisão em alterações rastreáveis. A verificação confirma correspondência com a decisão, atualização de versões e relações, cumprimento de condições e aprovação da CI. Quando possível, o verificador deve ser diferente do implementador.

## 5. Elegibilidade

Revisor ou decisor deve:

- compreender o escopo;
- aceitar o Código de Conduta;
- declarar vínculos e conflitos;
- possuir tempo e acesso suficientes;
- demonstrar competência técnica, metodológica, institucional ou vivencial pertinente;
- registrar fundamentos e divergências;
- não estar impedido.

Titulação formal não é obrigatória quando experiência prática ou vivida for materialmente relevante.

## 6. Independência e conflitos

Independência considera autoria, interesse financeiro, relação hierárquica, vínculo institucional, benefício pessoal e participação no fato analisado.

Devem ser declarados interesses acadêmicos, profissionais ou institucionais relacionados, mesmo quando não gerem impedimento.

Há impedimento para relatar, votar ou decidir quando a pessoa:

- é autora principal da proposta;
- obterá benefício direto e específico;
- está subordinada a quem controla o resultado;
- representa formalmente parte material da decisão;
- participou de incidente cuja apuração integra a proposta;
- omitiu conflito material;
- possui interesse pessoal capaz de comprometer razoavelmente a confiança no processo.

A pessoa impedida pode fornecer informação factual, com sua condição registrada. Recusa voluntária por falta de independência ou disponibilidade não deve gerar retaliação.

## 7. Rigor por impacto

| Impacto | Revisão mínima | Decisão mínima | Salvaguardas |
|---|---|---|---|
| baixo | uma revisão distinta da autoria, quando houver | um decisor competente | CI e ausência de efeito normativo |
| moderado | dois revisores, um independente da autoria | maioria simples, mínimo de dois decisores | riscos e compatibilidade explícitos |
| alto | três revisores, dois independentes | dois terços, mínimo de três decisores | participação afetada quando pertinente e plano de migração |
| crítico ou fundacional | cinco revisores, maioria independente | três quartos, mínimo de cinco decisores | consulta pública, análise de direitos, respostas a objeções e reversão |

Os números representam o modelo permanente. O regime provisório da seção 12 limita decisões quando esse mínimo não puder ser alcançado.

Objeção fundamentada sobre direitos, fraude, segurança, integridade ou ilegalidade suspende a decisão até análise específica.

## 8. Quórum e deliberação

O quórum inclui somente pessoas elegíveis e não impedidas. Ausências e abstenções por conflito não contam como votos válidos.

Antes da deliberação devem existir:

- síntese da proposta;
- versão efetivamente analisada;
- pareceres disponíveis;
- conflitos registrados;
- respostas às objeções materiais;
- texto ou decisão submetida.

Votos possíveis: aprovar, aprovar com condições, aprovar para piloto, devolver, rejeitar, declarar insuficiência ou abster-se por conflito.

Empate significa ausência de aprovação e exige complementação, novo painel ou manutenção do estado atual.

## 9. Critérios de revisão

A revisão considera, conforme aplicável:

- coerência com Carta, Especificação e Framework;
- problema demonstrado e ausência de duplicação;
- qualidade e limites das evidências;
- alternativas, inclusive não alterar;
- direitos, equidade, sustentabilidade e integridade;
- clareza, usabilidade e custo metodológico;
- compatibilidade e migração;
- dependências, links, catálogo e automações;
- capacidade de implementação e manutenção;
- riscos, reversibilidade e monitoramento;
- contribuições públicas e objeções;
- resultado das validações automáticas;
- maturidade permitida pelo PPC-000A.

## 10. Registro da decisão

Toda decisão publica:

- identificador e versão analisada;
- tipo, impacto e rito;
- composição e funções;
- conflitos, impedimentos e recusas;
- quórum e votos;
- pareceres e contribuições considerados;
- resultado, fundamentos e divergências;
- condições, prazos e responsáveis;
- compatibilidade e migração;
- implementação, verificação e reconsideração.

A `FICHA-GOV-006` fornece o registro operacional mínimo.

## 11. Decisões emergenciais

Medida emergencial pode conter risco imediato de segurança, ilegalidade, violação de direitos, corrupção de dados ou indisponibilidade grave.

Ela deve ser limitada, motivada, reversível e possuir prazo ou condição de expiração. Não pode alterar permanentemente o núcleo fundador. O prazo ordinário máximo é de 90 dias, salvo impossibilidade justificada e publicada.

## 12. Regime provisório atual

Enquanto não existir instância plural permanente:

- mantenedores exercem secretaria e decisões de baixo impacto;
- propostas moderadas exigem ao menos duas manifestações fundamentadas, uma externa à autoria;
- propostas altas podem avançar para rascunho, consulta ou piloto, mas não para estabilidade quando faltar o painel mínimo;
- propostas críticas ou fundacionais não podem estabilizar, substituir definitivamente o núcleo ou criar incompatibilidade geral sem o quórum permanente;
- insuficiência de revisores deve ser publicada;
- acumulação de funções deve constar no registro;
- a futura instância permanente poderá reexaminar decisões provisórias.

Esse regime permite manutenção responsável sem atribuir representatividade inexistente aos mantenedores.

## 13. Instância plural permanente

A instância permanente deve possuir:

- número ímpar entre cinco e nove integrantes;
- mandato de dois anos, com no máximo duas reconduções consecutivas;
- processo público de candidatura ou indicação;
- critérios publicados de competência, diversidade e independência;
- declaração pública de vínculos;
- substituição em impedimentos;
- regras de vacância, suspensão e destituição;
- atas, decisões e votos preservados;
- avaliação periódica do processo.

Nenhuma organização deve controlar mais de um terço dos assentos.

## 14. Constituição da instância permanente

A transição exige cumulativamente:

- ao menos sete pessoas elegíveis cadastradas como revisoras;
- pelo menos quatro trajetórias ou vínculos institucionais independentes;
- nenhuma organização controlando mais de um terço das vagas;
- processo público de candidatura ou indicação;
- regras operacionais de conflitos, proteção de dados e conduta;
- capacidade de secretaria e preservação de registros;
- três propostas formais concluídas com registros públicos;
- decisão de constituição submetida ao GOV-005 e a consulta pública.

O primeiro colegiado terá mandatos escalonados para evitar substituição simultânea de todos os integrantes.

## 15. Reconsideração

Pode haver reconsideração por:

- nova evidência material;
- erro factual relevante;
- conflito ou impedimento não declarado;
- violação de quórum ou rito;
- implementação divergente;
- consequência adversa não considerada;
- incompatibilidade descoberta posteriormente.

Vício grave deve ser revisto com participação de pessoas não responsáveis pela decisão original.

## 16. Transparência e restrições

Registros são públicos por padrão. Podem ser restringidos apenas dados cuja divulgação produza risco legítimo de privacidade, segurança, ilegalidade ou dano a pessoa vulnerável.

Mesmo quando anexos forem restritos, devem ser públicos o fundamento, a existência do material e uma síntese não sensível sempre que possível.

## 17. Indicadores

A política deve acompanhar:

- tempo de triagem, revisão, decisão e verificação;
- independência e diversidade dos painéis;
- conflitos declarados;
- dissensos registrados;
- propostas devolvidas por insuficiência;
- decisões reconsideradas;
- condições cumpridas;
- falhas após implementação;
- participação de pessoas afetadas;
- custo de revisão em relação ao impacto.

## 18. Revisão desta política

O GOV-006 deve ser revisto após a constituição da instância permanente, após as primeiras cinco decisões moderadas ou superiores, após incidente relevante ou quando houver evidência de custo ou exclusão desproporcional.

## 19. Critérios de qualidade

Uma decisão atende ao GOV-006 quando:

- funções, competência e conflitos estão registrados;
- o rigor corresponde ao impacto;
- quórum e votos são verificáveis;
- evidências, alternativas e objeções foram consideradas;
- fundamentos, condições e divergências foram publicados;
- implementação e verificação são rastreáveis;
- incompatibilidades possuem migração;
- a CI aplicável foi aprovada;
- limites do regime provisório foram explicitados;
- reconsideração permanece possível.

## 20. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Criação da política permanente, do regime provisório e dos critérios de constituição da instância plural | Projeto Pragmatismo Cívico |
