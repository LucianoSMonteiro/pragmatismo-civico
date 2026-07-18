---
id: CASOS-INDEX
titulo: Casos e Evidências do Pragmatismo Cívico
versao: 0.4.0
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

| Caso | Tema | Território | Estado | Resultado disponível |
|---|---|---|---|---|
| [CASO-001](CASO-001_DRENAGEM_URBANA_E_ALERTA_PREVENTIVO_EM_MARICA.md) | drenagem urbana e alerta preventivo | sub-bacia de Itapeba; polígono oficial pendente | preparação | [registro de prontidão](CASO-001_REGISTRO_DE_PRONTIDAO.md), [matriz de fontes](CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md) e [protocolo de dados](CASO-001_PROTOCOLO_DE_DADOS_PLUVIOMETRICOS.md) |

O período preliminar do CASO-001 é 2022-01-01 a 2026-06-30. A pergunta foi refinada, 13 fontes públicas foram consolidadas e o processamento, retenção e descarte dos dados foram documentados. O portão permanece fechado por falta de geometria oficial, documentos técnicos integrais, coleta real de dados, participação local e revisão independente.

O processador pluviométrico está testado apenas com fixture sintético. Nenhum arquivo mensal real do Cemaden foi incluído ou tratado como evidência do caso.

Ainda não há estudo concluído, diagnóstico oficial, recomendação, implementação avaliada ou estimativa de impacto publicada.

## Regras de publicação

Casos devem:

- seguir o GOV-008;
- utilizar caminho estável em `casos/`;
- declarar estado, território, período e versões;
- separar dados, hipóteses, interpretações e decisões;
- registrar revisão, conflitos e limitações;
- preservar resultados negativos ou inconclusivos;
- não publicar dados pessoais ou sigilosos desnecessários;
- ligar relatórios e dados sem duplicar fontes canônicas.

## Como interpretar os estados

- **preparação:** não existe diagnóstico validado;
- **pronto para diagnóstico:** fontes e governança mínimas foram verificadas;
- **diagnóstico a aprendizagem:** indica a etapa vigente do ciclo;
- **suspenso:** existe impedimento temporário registrado;
- **encerrado:** o caso terminou, inclusive de forma inconclusiva.

## Pendências do CASO-001

1. obter polígono oficial da sub-bacia de Itapeba — issue #6;
2. obter produtos técnicos e geometrias de drenagem — issue #7;
3. realizar downloads mensais autorizados e revisar a série — issue #4;
4. confirmar interlocutores e participação local — issue #8;
5. obter capacidade de revisão — issue #9;
6. emitir nova decisão do portão na issue #2.

A matriz de fontes foi concluída na issue #10. O processador e a política local de armazenamento, retenção e descarte foram concluídos nas issues #5 e #11. Essas conclusões documentais não equivalem à obtenção dos dados e arquivos pendentes.

## Casos futuros

Novos casos somente serão adicionados quando houver responsável, escopo preliminar e registro de seleção. Diretórios ou documentos vazios não devem ser criados para simular capacidade inexistente.

## Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Criação do índice público da camada de aplicações e evidências | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Inclusão do registro de prontidão, recorte de Itapeba e decisão de manter o CASO-001 em preparação | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Inclusão do protocolo pluviométrico, pipeline sintético e rastreamento das frentes do portão | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-18 | compatível | Inclusão da matriz de fontes, política de retenção e linha de base de cinco documentos de aplicação | Projeto Pragmatismo Cívico |
