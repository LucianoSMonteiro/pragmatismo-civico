---
id: PPC-000A
titulo: Ciclo de Vida dos Padrões
versao: 0.1.1
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
  - PPC-META-001
produz_entrada_para: []
relaciona_se_com:
  - GOV-001
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# PPC-000A — Ciclo de Vida dos Padrões

## Status

Rascunho inicial para discussão pública e adoção progressiva.

## 1. Objetivo

Definir como os Padrões do Pragmatismo Cívico — PPCs — são propostos, elaborados, revisados, testados, aprovados, mantidos, substituídos, declarados obsoletos e arquivados.

O PPC-000A busca impedir que um padrão:

- seja considerado oficial sem critérios verificáveis;
- mude de estado sem justificativa pública;
- permaneça indefinidamente sem revisão;
- seja substituído ou abandonado sem preservar o histórico;
- adquira estabilidade apenas por tempo de existência ou autoridade dos autores;
- seja aplicado fora de seu grau real de maturidade.

## 2. Escopo

Aplica-se a:

- PPCs metodológicos;
- padrões transversais PPC-META;
- revisões estruturais de padrões existentes;
- decisões de estabilização, substituição, obsolescência e arquivamento;
- ferramentas cuja validade dependa diretamente do estado de um PPC.

Pode ser utilizado, com adaptações proporcionais, para documentos de governança, arquitetura e ferramentas oficiais.

Não define o mérito substantivo de cada padrão nem substitui revisão técnica, consulta pública, teste de usabilidade ou avaliação de impacto.

## 3. Relação com outros documentos

O `PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md` estabelece a governança geral do ecossistema.

O `PPC-META-001_METADADOS_E_VERSIONAMENTO.md` estabelece como o estado, a versão, as dependências, a compatibilidade e o histórico devem ser registrados.

O PPC-000A detalha:

- os estados oficiais do ciclo de vida;
- as transições permitidas;
- os critérios de entrada e saída;
- as evidências necessárias;
- as responsabilidades;
- as decisões de manutenção e encerramento.

## 4. Princípios do ciclo de vida

A gestão dos padrões deve observar:

1. **Não presunção de estabilidade** — nenhum padrão nasce estável.
2. **Evidência proporcional** — o rigor da validação cresce com impacto, risco, custo e irreversibilidade.
3. **Transparência de estado** — o grau de maturidade deve ser visível a quem utiliza o padrão.
4. **Rastreabilidade** — toda transição deve possuir registro verificável.
5. **Reversibilidade responsável** — um estado pode ser revisto quando novas evidências justificarem.
6. **Preservação histórica** — substituição ou arquivamento não apagam versões anteriores.
7. **Participação adequada** — pessoas afetadas e especialistas devem participar quando pertinente.
8. **Divergência preservada** — objeções relevantes não devem desaparecer do registro.
9. **Simplicidade** — o processo não deve criar cerimônia sem utilidade.
10. **Responsabilidade explícita** — cada transição deve indicar quem propôs, revisou e decidiu.

## 5. Visão geral

O fluxo ordinário é:

```text
Ideia
  ↓
Proposta
  ↓
Rascunho
  ↓
Revisão pública
  ↓
Piloto
  ↓
Estável
  ↓
Em revisão
  ├──→ Estável
  ├──→ Substituído
  ├──→ Obsoleto
  └──→ Arquivado
```

Nem todo documento precisa percorrer todas as etapas com a mesma intensidade. A dispensa de uma etapa deve ser justificada, registrada e proporcional ao risco.

## 6. Estados oficiais

Os valores canônicos do campo `status` são:

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

### 6.1 Ideia

Representa uma necessidade, hipótese ou oportunidade ainda não formalizada como proposta.

Uma ideia deve registrar, no mínimo:

- problema percebido;
- contexto em que surgiu;
- pessoa ou grupo que a apresentou;
- relação possível com padrões existentes.

A ideia não é um padrão e não deve ser apresentada como orientação oficial.

**Saída ordinária:** proposta ou encerramento sem continuidade.

### 6.2 Proposta

Representa uma iniciativa formal para criar, revisar substancialmente, substituir ou retirar um padrão.

Uma proposta deve demonstrar:

- problema real a resolver;
- público ou processo afetado;
- evidências iniciais;
- alternativas já consideradas;
- ausência de duplicação desnecessária;
- aderência aos princípios fundadores;
- custo metodológico esperado;
- responsável por conduzir o trabalho.

**Saída ordinária:** rascunho, devolução para complementação ou rejeição fundamentada.

### 6.3 Rascunho

Representa um documento estruturado, mas ainda não validado suficientemente.

O rascunho deve conter:

- metadados mínimos;
- objetivo e escopo;
- processo ou regras propostas;
- dependências;
- critérios de aplicação;
- limitações conhecidas;
- histórico inicial;
- questões ainda abertas.

Rascunhos podem ser utilizados para aprendizagem, desde que seu estado seja comunicado e os riscos sejam controlados.

**Saída ordinária:** revisão pública, retorno à proposta ou encerramento.

### 6.4 Revisão pública

Representa um rascunho aberto a contribuições estruturadas de pessoas externas à equipe autora.

A abertura da revisão deve informar:

- versão submetida;
- período ou condição de encerramento;
- perguntas específicas;
- canais de participação;
- critérios de análise das contribuições;
- responsáveis pela consolidação;
- tratamento de conflitos de interesse;
- forma de publicação das respostas.

A mera disponibilidade pública do arquivo não equivale a revisão pública.

**Saída ordinária:** piloto, novo rascunho, suspensão ou rejeição.

### 6.5 Piloto

Representa um padrão em aplicação controlada, real ou simulada, para verificar utilidade, clareza, custo e efeitos indesejados.

O piloto deve possuir:

- contexto e responsáveis;
- versão testada;
- critérios de sucesso;
- indicadores de qualidade;
- riscos e salvaguardas;
- plano de coleta de evidências;
- mecanismo de interrupção;
- registro de adaptações;
- relatório de resultados e limitações.

O uso em piloto não autoriza afirmar validade geral.

**Saída ordinária:** estável, novo rascunho, novo piloto, suspensão ou obsolescência.

### 6.6 Estável

Representa um padrão validado e recomendado para uso geral dentro de seu escopo declarado.

A estabilidade exige, proporcionalmente:

- coerência com os princípios fundadores;
- revisão técnica;
- revisão de coerência documental;
- consulta ou revisão pública adequada;
- teste de usabilidade;
- evidência de aplicação;
- registro de limitações;
- avaliação do custo de uso;
- resposta às objeções relevantes;
- decisão formal de aprovação;
- versão e data de revisão futura.

Estável não significa perfeito, definitivo ou universal.

**Saída ordinária:** em revisão, substituído, obsoleto ou arquivado.

### 6.7 Em revisão

Representa um padrão estável submetido a reavaliação formal.

A revisão pode ser motivada por:

- revisão periódica;
- nova evidência;
- falha ou incidente;
- mudança legal, tecnológica ou institucional;
- incompatibilidade com outro documento;
- custo excessivo;
- dificuldade de aplicação;
- efeitos distributivos ou riscos não previstos;
- proposta de substituição.

Enquanto estiver em revisão, o padrão continua vigente, salvo declaração explícita de suspensão ou restrição.

**Saída ordinária:** estável em nova versão, substituído, obsoleto ou arquivado.

### 6.8 Substituído

Representa um padrão sucedido por outro documento identificado.

A declaração deve informar:

- documento substituto;
- razão da substituição;
- data de vigência;
- compatibilidade;
- orientação de migração;
- tratamento de aplicações em andamento;
- localização das versões anteriores.

Um padrão substituído não deve ser recomendado para novos usos, salvo exceção documentada.

### 6.9 Obsoleto

Representa um padrão não recomendado, sem necessariamente possuir sucessor direto.

Pode ocorrer quando:

- deixou de resolver o problema;
- produz riscos ou efeitos indesejados;
- possui custo desproporcional;
- tornou-se incompatível com o framework;
- perdeu sustentação empírica;
- deixou de ser aplicável ao contexto.

A obsolescência deve indicar alternativas disponíveis e riscos de continuidade do uso.

### 6.10 Arquivado

Representa um documento retirado do catálogo ativo, mas preservado para memória, auditoria ou pesquisa.

O arquivamento deve registrar:

- motivo;
- estado anterior;
- data;
- responsável pela decisão;
- localização canônica;
- política de acesso;
- documento substituto, quando houver.

Arquivar não significa apagar.

## 7. Transições permitidas

As transições ordinárias são:

| Origem | Destino | Condição mínima |
|---|---|---|
| ideia | proposta | problema e responsável identificados |
| proposta | rascunho | admissibilidade aprovada |
| proposta | arquivado | rejeição ou perda de objeto registrada |
| rascunho | revisao-publica | completude mínima e questões de consulta definidas |
| rascunho | proposta | necessidade de reformulação estrutural |
| rascunho | arquivado | encerramento fundamentado |
| revisao-publica | piloto | contribuições consolidadas e riscos controlados |
| revisao-publica | rascunho | mudanças relevantes necessárias |
| revisao-publica | arquivado | inviabilidade ou rejeição fundamentada |
| piloto | estavel | evidência suficiente e aprovação formal |
| piloto | rascunho | revisão metodológica necessária |
| piloto | piloto | novo teste justificado |
| piloto | obsoleto | risco ou inadequação demonstrados |
| estavel | em-revisao | gatilho de revisão registrado |
| estavel | substituido | sucessor aprovado e migração definida |
| estavel | obsoleto | inadequação demonstrada |
| estavel | arquivado | perda de objeto ou encerramento definitivo |
| em-revisao | estavel | revisão concluída e versão aprovada |
| em-revisao | substituido | sucessor aprovado |
| em-revisao | obsoleto | retirada recomendada |
| em-revisao | arquivado | encerramento definitivo |
| substituido | arquivado | migração consolidada e preservação assegurada |
| obsoleto | arquivado | preservação e comunicação asseguradas |

Transições fora dessa tabela exigem justificativa excepcional, análise de risco e registro explícito.

## 8. Portões de decisão

### 8.1 Admissibilidade da proposta

Verifica se:

- existe problema definido;
- o tema pertence ao escopo do projeto;
- não há duplicação evidente;
- há responsável e capacidade mínima;
- o custo esperado é proporcional;
- a proposta não viola princípios fundadores.

### 8.2 Prontidão para revisão pública

Verifica se o rascunho:

- possui estrutura mínima;
- declara limitações e incertezas;
- contém metadados válidos;
- identifica questões abertas;
- não apresenta referências quebradas;
- permite contribuição informada.

### 8.3 Prontidão para piloto

Verifica se:

- contribuições foram respondidas;
- riscos possuem salvaguardas;
- existem critérios de interrupção;
- contexto e usuários estão definidos;
- dados e responsabilidades estão organizados;
- o teste pode gerar evidência útil.

### 8.4 Decisão de estabilidade

Verifica se:

- houve teste suficiente;
- limitações foram registradas;
- divergências relevantes foram tratadas;
- o padrão pode ser aplicado sem orientação informal indispensável;
- a versão é coerente com as ferramentas associadas;
- a manutenção futura possui responsável;
- há data ou condição de revisão.

### 8.5 Decisão de retirada

Verifica se:

- usuários e aplicações afetadas foram identificados;
- riscos de continuidade e retirada foram comparados;
- existe orientação de transição;
- o histórico será preservado;
- o portal e os documentos relacionados serão atualizados.

## 9. Papéis e responsabilidades

### 9.1 Proponente

Formula a ideia ou proposta e apresenta a justificativa inicial.

### 9.2 Responsável pelo documento

Coordena elaboração, consolidação, manutenção e resposta às contribuições.

### 9.3 Revisão técnica

Avalia coerência metodológica, evidências, riscos e aplicabilidade.

### 9.4 Revisão de coerência

Verifica compatibilidade com princípios, arquitetura, metadados, dependências e padrões existentes.

### 9.5 Participantes da revisão pública

Apresentam contribuições, objeções, experiências e perspectivas afetadas.

### 9.6 Instância aprovadora

Decide sobre transições que exigem aprovação formal, declarando fundamentos e conflitos de interesse.

### 9.7 Custódia do repositório

Garante registro técnico, preservação histórica, publicação e controle de acesso.

Na fase inicial do projeto, uma mesma pessoa pode exercer mais de um papel. A acumulação deve ser declarada, e decisões de estabilidade devem buscar revisão externa independente.

## 10. Registro obrigatório de transição

Toda transição deve registrar:

- identificador do documento;
- versão de origem e destino;
- estado anterior e novo estado;
- data;
- proponente;
- revisores;
- instância decisória;
- evidências consideradas;
- objeções relevantes;
- decisão e justificativa;
- compatibilidade;
- ações pendentes;
- próxima revisão, quando aplicável;
- commit, issue ou pull request correspondente.

Modelo mínimo:

| Data | Versão | De | Para | Decisão | Responsáveis | Referência |
|---|---|---|---|---|---|---|
| 2026-07-17 | 0.1.0 | proposta | rascunho | Primeira publicação para desenvolvimento | Projeto Pragmatismo Cívico | commit |

## 11. Aprovação e divergência

Uma decisão de transição deve:

- declarar o critério utilizado;
- separar evidência, interpretação e decisão;
- registrar votos ou posições quando houver colegiado;
- preservar pareceres divergentes relevantes;
- declarar conflitos de interesse;
- explicar por que objeções não acolhidas foram rejeitadas;
- evitar consenso aparente produzido por ausência de participação.

A existência de divergência não impede uma decisão, mas sua ocultação invalida a rastreabilidade.

## 12. Revisão periódica

Todo padrão estável deve possuir uma data ou condição de revisão.

Como referência inicial:

- padrões de alto risco: revisão ao menos anual;
- padrões metodológicos gerais: revisão ao menos a cada dois anos;
- padrões transversais: revisão ao menos a cada dois anos;
- revisão extraordinária: sempre que ocorrer gatilho relevante.

A periodicidade deve ser reduzida quando houver:

- rápida mudança tecnológica ou normativa;
- alto impacto sobre direitos;
- evidência limitada;
- elevado custo de erro;
- incidentes recorrentes;
- baixa maturidade do padrão.

O vencimento da revisão não torna automaticamente o padrão inválido, mas deve gerar alerta e decisão explícita sobre continuidade.

## 13. Mudanças emergenciais

Mudanças emergenciais podem ser adotadas quando a espera pelo processo ordinário produzir risco relevante.

Devem:

- possuir escopo mínimo necessário;
- registrar a urgência;
- indicar duração ou condição de expiração;
- declarar impactos e incertezas;
- preservar a versão anterior;
- passar por revisão posterior em prazo definido;
- não ser utilizadas para evitar participação ou escrutínio.

Uma mudança emergencial não transforma automaticamente o documento em estável.

## 14. Suspensão temporária

Um padrão pode ter uso temporariamente suspenso sem mudança imediata para obsoleto quando:

- houver risco grave ainda em investigação;
- ocorrer falha de segurança ou direitos;
- dados essenciais se tornarem indisponíveis;
- surgir incompatibilidade crítica.

A suspensão deve informar:

- alcance;
- início;
- motivo;
- usos afetados;
- alternativas temporárias;
- responsável pela investigação;
- condição de reavaliação.

O campo `status` permanece conforme o estado formal, e a suspensão deve ser registrada em campo ou aviso específico até decisão definitiva.

## 15. Reabertura e reversão

Documentos substituídos, obsoletos ou arquivados não devem retornar silenciosamente ao catálogo ativo.

A reativação exige:

- nova proposta;
- justificativa baseada em evidências;
- análise das razões da retirada anterior;
- nova versão;
- revisão de compatibilidade;
- transição formal para rascunho ou piloto.

## 16. Relação com versionamento

A mudança de estado e a mudança de versão são decisões relacionadas, mas distintas.

- uma correção editorial pode alterar a versão sem mudar o estado;
- uma transição para revisão pública normalmente exige versão identificada;
- a estabilidade deve corresponder a uma versão específica;
- a volta de `em-revisao` para `estavel` deve publicar nova versão quando houver alteração material;
- substituição e obsolescência devem atualizar metadados mesmo sem mudança de conteúdo metodológico;
- aplicações devem registrar a versão e o estado efetivamente utilizados.

As regras semânticas de versão são definidas pelo PPC-META-001.

## 17. Ferramentas associadas

Quando um PPC mudar de estado, suas ferramentas devem ser avaliadas.

A decisão deve indicar se cada ficha, matriz, checklist ou modelo:

- permanece compatível;
- precisa de atualização;
- será substituído;
- será declarado obsoleto;
- deve permanecer disponível apenas para uso histórico.

Nenhum padrão deve ser considerado plenamente estabilizado se suas ferramentas obrigatórias estiverem incompatíveis.

## 18. Comunicação pública

Mudanças de estado relevantes devem ser comunicadas no portal e, quando aplicável:

- no changelog;
- no roadmap;
- na página do padrão;
- nas ferramentas associadas;
- em notas de migração;
- nos canais comunitários.

O usuário não deve precisar examinar o histórico de commits para descobrir que um padrão deixou de ser recomendado.

## 19. Critérios de conformidade

Um processo atende ao PPC-000A quando:

- utiliza um estado canônico;
- respeita as transições permitidas ou justifica exceção;
- registra critérios de entrada e saída;
- identifica responsáveis e revisores;
- preserva evidências e divergências;
- atualiza versão e metadados;
- avalia ferramentas e dependências;
- comunica a mudança;
- preserva o histórico;
- define próxima revisão quando pertinente.

## 20. Limitações

Este padrão não garante, por si só:

- qualidade científica ou técnica;
- representatividade da participação;
- independência dos revisores;
- ausência de captura institucional;
- disponibilidade de recursos para pilotos;
- preservação digital de longo prazo;
- legitimidade política de uma aplicação concreta.

Essas limitações devem ser tratadas por governança, revisão independente, transparência e avaliação contínua.

## 21. Adoção inicial

A adoção será progressiva:

1. novos PPCs utilizam imediatamente os estados canônicos;
2. documentos existentes mantêm seu estado declarado até revisão;
3. o catálogo deve identificar documentos sem estado ou versão explícita;
4. a migração deve começar pelos documentos centrais;
5. nenhuma retroatividade deve apagar o estado real em que uma versão foi produzida;
6. o processo de migração deve ser acompanhado no roadmap.

## 22. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Primeira publicação do ciclo de vida dos padrões | Projeto Pragmatismo Cívico |
| 0.1.1 | 2026-07-17 | correção | Substituição do relacionamento legado pelo identificador canônico GOV-001 | Projeto Pragmatismo Cívico |
