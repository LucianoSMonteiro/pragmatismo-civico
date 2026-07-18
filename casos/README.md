---
id: CASOS-INDEX
titulo: Casos e Evidências do Pragmatismo Cívico
versao: 0.6.0
status: rascunho
tipo: publicacao
idioma: pt-BR
data_criacao: 2026-07-18
data_versao: 2026-07-18
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - GOV-008
  - ARQ-003
  - ARQ-002
  - PPC-META-001
  - ARQ-001
produz_entrada_para: []
relaciona_se_com:
  - CATALOGO-DOCUMENTAL
  - CASO-001
  - CASO-001-PRONTIDAO
  - CASO-001-FONTES
  - CASO-001-DOCUMENTOS-TECNICOS
  - CASO-001-GEOMETRIA
  - CASO-001-DADOS-CHUVA
  - FICHA-GOV-008
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# Casos e Evidências do Pragmatismo Cívico

Esta área reúne aplicações, pilotos, avaliações e lições aprendidas. A presença de um documento aqui não significa que o caso esteja concluído, que seus resultados sejam positivos ou que o framework tenha sido validado.

## Estado atual

| Caso | Tema | Território | Estado | Produtos disponíveis |
|---|---|---|---|---|
| [CASO-001](CASO-001_DRENAGEM_URBANA_E_ALERTA_PREVENTIVO_EM_MARICA.md) | drenagem urbana e alerta preventivo | sub-bacia de Itapeba; polígono oficial pendente | preparação | [prontidão](CASO-001_REGISTRO_DE_PRONTIDAO.md), [fontes](CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md), [documentos técnicos](CASO-001_DOCUMENTOS_TECNICOS_E_CONTRATACOES.md), [geometria](CASO-001_PROTOCOLO_DE_GEOMETRIA_E_DELIMITACAO.md) e [chuva](CASO-001_PROTOCOLO_DE_DADOS_PLUVIOMETRICOS.md) |

O período preliminar é 2022-01-01 a 2026-06-30. A pergunta foi refinada, 15 fontes gerais e oito fontes técnicas ou financeiras foram estruturadas. Foram localizados geosserviços oficiais candidatos do INEA, operações de financiamento do Novo PAC e o Pregão Eletrônico 14/2026 — Smart Drainage.

O portão permanece fechado porque nenhuma feição oficial de Itapeba, arquivo mensal real, programa final, contrato integral, projeto, medição, participação local ou revisão independente foi incorporado.

Ainda não há estudo concluído, diagnóstico oficial, recomendação, implementação avaliada ou estimativa de impacto publicada.

## Infraestrutura disponível

| Recurso | Estado | Limite |
|---|---|---|
| matriz de fontes | 15 fontes classificadas | inventário não substitui obtenção dos arquivos |
| registro técnico estruturado | 8 fontes, 20 alegações, 3 inconsistências e 7 grupos documentais pendentes | notícias e índices não substituem contratos, projetos e medições |
| processador pluviométrico | teste sintético aprovado | nenhuma série mensal real processada |
| coletor e validador GeoJSON | testes controlados aprovados | nenhuma geometria oficial processada |
| retenção e descarte | regras documentadas | execução depende do ambiente local |
| revisão independente | indisponível | cadastro público permanece vazio |

A validação documental verifica o registro técnico. Os estados `data/pipeline` e `geodata/pipeline` comprovam o funcionamento dos códigos de teste, não a qualidade de fontes reais nem a execução de obras.

## Regras de publicação

Casos devem:

- seguir o GOV-008;
- utilizar caminho estável em `casos/`;
- declarar estado, território, período e versões;
- separar dados, hipóteses, interpretações e decisões;
- separar comunicação, financiamento, contratação, projeto, medição e resultado;
- registrar revisão, conflitos e limitações;
- preservar resultados negativos ou inconclusivos;
- não publicar dados pessoais ou sigilosos desnecessários;
- ligar relatórios e dados sem duplicar fontes canônicas;
- distinguir fixture sintético de fonte empírica;
- exigir caminho local e SHA-256 antes de classificar uma fonte como obtida;
- não apresentar serviço cartográfico como polígono obtido sem consulta, arquivo, hash e revisão.

## Como interpretar os estados

- **preparação:** não existe diagnóstico validado;
- **pronto para diagnóstico:** fontes e governança mínimas foram verificadas;
- **diagnóstico a aprendizagem:** indica a etapa vigente do ciclo;
- **suspenso:** existe impedimento temporário registrado;
- **encerrado:** o caso terminou, inclusive de forma inconclusiva.

## Pendências do CASO-001

1. consultar, preservar e revisar a feição oficial da sub-bacia — issue #6;
2. obter programa final, contratos, projetos, geometrias, cronogramas e medições — issue #7;
3. realizar downloads mensais autorizados e revisar a série — issue #4;
4. confirmar interlocutores e participação local — issue #8;
5. obter capacidade de revisão — issue #9;
6. emitir nova decisão do portão — issue #2.

A matriz de fontes foi concluída na issue #10. O processador e a política local de armazenamento, retenção e descarte foram concluídos nas issues #5 e #11. O inventário técnico da issue #7 foi estruturado, mas a issue permanece aberta porque os documentos integrais não foram obtidos.

## Casos futuros

Novos casos somente serão adicionados quando houver responsável, escopo preliminar e registro de seleção. Diretórios ou documentos vazios não devem ser criados para simular capacidade inexistente.

## Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Criação do índice público da camada de aplicações e evidências | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Inclusão do registro de prontidão, recorte de Itapeba e decisão de manter o CASO-001 em preparação | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Inclusão do protocolo pluviométrico, pipeline sintético e rastreamento das frentes do portão | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-18 | compatível | Inclusão da matriz de fontes, política de retenção e linha de base de cinco documentos de aplicação | Projeto Pragmatismo Cívico |
| 0.5.0 | 2026-07-18 | compatível | Inclusão do protocolo geoespacial, fontes do GeoINEA e status `geodata/pipeline` | Projeto Pragmatismo Cívico |
| 0.6.0 | 2026-07-18 | compatível | Inclusão do registro técnico e financeiro, inconsistências e controles de evidência | Projeto Pragmatismo Cívico |
