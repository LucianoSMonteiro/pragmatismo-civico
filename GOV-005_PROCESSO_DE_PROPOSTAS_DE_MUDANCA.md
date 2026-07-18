---
id: GOV-005
titulo: Processo de Propostas de Mudança
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
  - GOV-003
  - GOV-004
  - PPC-000A
  - PPC-META-001
  - ARQ-001
produz_entrada_para: []
relaciona_se_com:
  - GOV-002
  - ARQ-002
  - FICHA-GOV-005
substitui: []
substituido_por: null
compatibilidade: inicial
proxima_revisao: null
ferramentas_associadas:
  - FICHA_GOV-005_PROPOSTA_DE_MUDANCA.md
---

# GOV-005 — Processo de Propostas de Mudança

## 1. Objetivo

Definir como mudanças no Pragmatismo Cívico são apresentadas, classificadas, analisadas, decididas, implementadas, verificadas e registradas.

O processo busca impedir que uma alteração relevante:

- seja incorporada sem problema e justificativa explícitos;
- modifique silenciosamente princípios, método ou responsabilidades;
- seja decidida por autoridade informal não registrada;
- omita riscos, alternativas, conflitos de interesse ou impactos distributivos;
- produza deriva entre documentos, ferramentas, catálogo e portal;
- apague objeções, versões anteriores ou razões de rejeição.

## 2. Escopo

Aplica-se a propostas que criem, alterem, substituam, tornem obsoleto, arquivem, renomeiem ou movam documentos, ferramentas, automações, regras de governança ou componentes de publicação.

Correções estritamente editoriais podem seguir fluxo simplificado, mas continuam sujeitas a revisão, versionamento e validação automática.

O processo não substitui:

- o mérito técnico de cada padrão;
- o ciclo de vida do PPC-000A;
- as regras de versionamento do PPC-META-001;
- o Código de Conduta;
- revisão jurídica, ética, científica ou de segurança quando necessária.

## 3. Princípios

Toda proposta deve observar:

1. **Problema antes da solução** — a necessidade deve ser demonstrada antes da alteração pretendida.
2. **Preservação do núcleo** — mudanças concretizam os princípios fundadores; não os redefinem silenciosamente.
3. **Proporcionalidade** — o rigor aumenta com impacto, risco, irreversibilidade e alcance.
4. **Alternativas reais** — manter o estado atual deve ser considerado quando plausível.
5. **Rastreabilidade** — proposta, revisão, decisão, implementação e verificação devem ser reconstruíveis.
6. **Divergência preservada** — objeções relevantes devem permanecer no registro.
7. **Conflitos declarados** — vínculos materiais devem ser informados e tratados.
8. **Compatibilidade explícita** — efeitos sobre aplicações e versões anteriores devem ser classificados.
9. **Reversibilidade** — mudanças arriscadas devem possuir mecanismo de interrupção ou reversão.
10. **Não presunção de aprovação** — abertura de issue ou pull request não confere legitimidade à proposta.

## 4. Identificação e registro

Propostas formais devem receber identificador no formato:

```text
PM-AAAA-NNN
```

Exemplo: `PM-2026-001`.

O identificador deve aparecer:

- no título da issue ou registro canônico;
- no documento preenchido da proposta;
- no pull request de implementação;
- na decisão final;
- no histórico dos documentos alterados, quando aplicável.

Enquanto não houver registro próprio automatizado, a issue do GitHub é a fonte canônica da proposta. Pull requests implementam decisões, mas não substituem o registro decisório.

## 5. Tipos de proposta

### 5.1 Editorial

Corrige ortografia, formatação, acessibilidade, links ou clareza sem alterar obrigação, interpretação ou método.

### 5.2 Corretiva

Repara inconsistência, erro factual, relação documental incorreta, falha de automação ou contradição não intencional.

### 5.3 Metodológica

Altera processo, critério, entrada, saída, obrigação, instrumento de análise ou forma de aplicação do framework.

### 5.4 Arquitetural

Altera camadas, identificadores, caminhos, navegação, dependências, catálogo, automações ou organização do repositório.

### 5.5 Governança

Altera papéis, competências, revisão, aprovação, participação, conflitos de interesse, transparência ou prestação de contas.

### 5.6 Fundacional

Altera Carta de Princípios, Especificação, Framework de Referência ou interpretação material do núcleo fundador.

### 5.7 Ciclo de vida

Propõe mudança de estado, estabilização, revisão, substituição, obsolescência ou arquivamento de documento governado.

### 5.8 Emergencial

Trata risco imediato de segurança, ilegalidade, violação de direitos, corrupção de dados, indisponibilidade grave ou erro capaz de causar dano relevante.

Uma proposta pode possuir mais de um tipo. Deve prevalecer o fluxo mais rigoroso aplicável.

## 6. Níveis de impacto

| Nível | Caracterização | Exemplos |
|---|---|---|
| baixo | alteração local, reversível e sem efeito normativo | ortografia, link, formatação |
| moderado | afeta uso ou interpretação limitada | melhoria de ferramenta, ajuste de navegação |
| alto | altera método, governança, compatibilidade ou vários documentos | novo critério obrigatório, mudança de processo |
| crítico | afeta princípios, direitos, segurança, estabilidade ou todo o ecossistema | mudança fundacional, retirada urgente, quebra ampla |

A classificação deve considerar alcance, pessoas afetadas, risco, irreversibilidade, custo de migração e capacidade de correção.

## 7. Estados da proposta

Os estados abaixo pertencem ao registro da proposta e não substituem o campo documental `status` do PPC-000A:

- `recebida`;
- `triagem`;
- `complementacao`;
- `admitida`;
- `em-analise`;
- `consulta-publica`;
- `decidida`;
- `em-implementacao`;
- `em-verificacao`;
- `encerrada`;
- `retirada`.

Toda mudança de estado deve registrar data, responsável e justificativa.

## 8. Conteúdo mínimo

A proposta deve informar:

- identificador e título;
- pessoa ou grupo proponente;
- problema demonstrado;
- contexto e pessoas ou processos afetados;
- tipo e nível de impacto;
- estado atual e alteração pretendida;
- princípios e documentos relacionados;
- evidências, experiências ou incidentes relevantes;
- alternativas consideradas, incluindo não alterar;
- benefícios esperados;
- riscos, efeitos adversos e salvaguardas;
- compatibilidade e migração;
- documentos, ferramentas, links e automações afetados;
- plano de implementação, verificação e reversão;
- conflitos de interesse;
- questões ainda abertas.

A ficha `FICHA-GOV-005` operacionaliza esse conteúdo.

## 9. Triagem e admissibilidade

A triagem verifica se a proposta:

- descreve problema compreensível e verificável;
- pertence ao escopo do projeto;
- não duplica proposta ou documento existente sem justificativa;
- identifica impactos e documentos relacionados;
- não viola manifestamente princípios, direitos ou Código de Conduta;
- apresenta informação suficiente para análise proporcional;
- indica responsável pelo acompanhamento.

Resultados possíveis:

- admitir;
- solicitar complementação;
- reunir com proposta relacionada;
- redirecionar para correção editorial simples;
- rejeitar como fora de escopo ou manifestamente incompatível;
- encerrar por perda de objeto;
- aceitar retirada pelo proponente.

Rejeição de admissibilidade deve ser fundamentada e não pode apagar o registro.

## 10. Plano de revisão

Após admissão, deve ser definido:

- perguntas que a revisão precisa responder;
- documentos e versões em análise;
- revisores necessários;
- participação de pessoas afetadas;
- necessidade de consulta pública, piloto ou parecer especializado;
- critérios de decisão;
- prazo ou condição de encerramento;
- tratamento de informações sensíveis.

### 10.1 Fluxo simplificado

Pode ser usado para propostas editoriais e corretivas de baixo impacto quando:

- não há mudança normativa ou metodológica;
- não há incompatibilidade;
- a CI cobre o risco principal;
- a justificativa e o diff são suficientes para revisão.

### 10.2 Fluxo ordinário

Usado para impacto moderado ou alto. Requer análise documentada, revisão dos documentos afetados, verificação de compatibilidade e decisão pública.

### 10.3 Fluxo reforçado

Obrigatório para mudanças fundacionais, críticas, incompatíveis ou com impacto relevante sobre direitos. Deve incluir, proporcionalmente:

- revisão técnica independente;
- consulta pública estruturada;
- resposta às objeções relevantes;
- avaliação de alternativas;
- plano de migração e reversão;
- decisão explicitamente motivada.

Enquanto não existir instância plural formalmente constituída, uma proposta fundacional não pode tornar o documento `estavel` por decisão unilateral. Ela pode avançar apenas como rascunho, revisão pública ou piloto, com a limitação registrada.

## 11. Revisores e conflitos de interesse

Revisores devem avaliar mérito e processo separadamente. Devem declarar vínculos financeiros, profissionais, institucionais, partidários ou pessoais capazes de influenciar materialmente a análise.

Quem possuir conflito relevante deve:

- declarar o conflito;
- abster-se da decisão quando sua independência estiver comprometida;
- limitar-se a fornecer informação factual quando apropriado;
- ter sua participação registrada.

A ausência de revisores independentes não deve ser disfarçada. A decisão pode permanecer provisória ou em estado de menor maturidade, com a limitação explicitada.

## 12. Consulta pública

A consulta deve indicar:

- versão e escopo submetidos;
- período ou condição de encerramento;
- perguntas específicas;
- canais acessíveis de participação;
- critérios para consolidar contribuições;
- responsáveis pela resposta;
- forma de publicação das contribuições e decisões;
- exceções legítimas de privacidade, segurança ou sigilo.

Disponibilizar um arquivo publicamente não equivale, por si só, a consulta pública.

## 13. Critérios de decisão

A decisão deve considerar:

- coerência com os princípios fundadores;
- evidência do problema;
- qualidade e suficiência das evidências;
- benefícios públicos esperados;
- riscos, direitos, equidade e sustentabilidade;
- clareza e aplicabilidade;
- custo metodológico e de manutenção;
- compatibilidade com aplicações anteriores;
- capacidade real de implementação;
- reversibilidade;
- objeções e alternativas relevantes;
- resultado das validações automáticas.

Pontuações ou maiorias simples não substituem justificativa substantiva.

## 14. Resultados da decisão

A proposta pode ser:

- aprovada;
- aprovada com condições;
- aprovada para piloto;
- devolvida para reformulação;
- suspensa por falta de evidência ou capacidade;
- rejeitada;
- retirada;
- substituída por proposta posterior;
- encerrada por perda de objeto.

A decisão deve registrar:

- resultado e data;
- responsáveis e participantes;
- fundamentos;
- evidências utilizadas;
- objeções relevantes e seu tratamento;
- condições e prazos;
- classificação de compatibilidade;
- documentos e versões afetados;
- plano de implementação e verificação.

## 15. Competência decisória provisória

Enquanto o projeto não possuir conselho ou instância plural formalmente constituída:

- mantenedores do repositório executam triagem e decisões ordinárias;
- decisões devem permanecer públicas e motivadas;
- proponente não deve ser o único revisor de mudança moderada, alta ou crítica;
- devem ser buscadas ao menos duas manifestações independentes para mudanças altas ou críticas;
- quando isso não for possível, a limitação deve ser registrada e o estado de maturidade não pode ser artificialmente elevado;
- mudanças fundacionais seguem a restrição do fluxo reforçado;
- a futura instância de governança poderá revisar decisões provisórias, preservando seu histórico.

Este arranjo não cria autoridade substantiva ilimitada nem presume legitimidade representativa dos mantenedores.

## 16. Implementação

Uma proposta aprovada deve ser implementada por mudança rastreável, preferencialmente pull request, contendo:

- referência ao identificador da proposta;
- arquivos alterados;
- versões e históricos atualizados;
- migração ou comunicação necessária;
- testes e validações aplicáveis;
- documentação de divergências entre decisão e implementação.

A aprovação da proposta não aprova automaticamente qualquer implementação. O diff deve corresponder à decisão.

## 17. Verificação e encerramento

Antes do encerramento, verificar:

- implementação integral das condições;
- consistência de metadados e versões;
- atualização de dependências e relações;
- links, catálogo, navegação e build;
- comunicação de incompatibilidades;
- preservação de versões anteriores;
- funcionamento dos critérios de sucesso;
- registro de falhas ou desvios.

A proposta somente passa a `encerrada` após verificação, ou após decisão explícita de encerrar sem implementação.

## 18. Mudanças emergenciais

Mudanças emergenciais devem ser:

- limitadas ao necessário para conter o risco;
- claramente identificadas como emergenciais;
- acompanhadas de justificativa e responsável;
- reversíveis quando possível;
- submetidas à CI e revisão posterior;
- reavaliadas em prazo ou condição definidos.

Uma medida emergencial não pode ser usada para introduzir mudança fundacional permanente sem o fluxo reforçado. Após contenção, deve ser criada ou complementada proposta ordinária.

## 19. Reconsideração

Uma decisão pode ser reconsiderada quando houver:

- erro factual ou processual relevante;
- nova evidência material;
- conflito de interesse não declarado;
- consequência adversa não prevista;
- incompatibilidade descoberta;
- descumprimento das condições aprovadas.

A reconsideração deve referenciar a proposta original e não apagar a decisão anterior.

## 20. Transparência e métricas

Devem ser acompanhados, quando houver volume suficiente:

- propostas recebidas por tipo e estado;
- tempo de triagem, decisão e implementação;
- proporção de propostas aprovadas, rejeitadas ou retiradas;
- solicitações de complementação;
- participação e diversidade de revisores;
- conflitos declarados;
- falhas detectadas após implementação;
- reversões e reconsiderações;
- custo de manutenção do processo.

As métricas servem para melhorar a governança, não para premiar velocidade ou quantidade de mudanças.

## 21. Limitações

Este processo ainda depende de mantenedores provisórios e não possui conselho plural constituído. Sua adoção como rascunho organiza a prática, mas não substitui a futura política de revisão e aprovação nem resolve, isoladamente, representatividade e capacidade de revisão independente.

## 22. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Criação do processo formal de propostas, revisão, decisão, implementação e registro público | Projeto Pragmatismo Cívico |
