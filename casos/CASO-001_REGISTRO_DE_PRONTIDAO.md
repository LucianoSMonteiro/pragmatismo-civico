---
id: CASO-001-PRONTIDAO
titulo: Registro de Prontidão do CASO-001 — Sub-bacia de Itapeba
versao: 0.4.0
status: rascunho
tipo: aplicacao
idioma: pt-BR
data_criacao: 2026-07-18
data_versao: 2026-07-18
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - CASO-001
  - GOV-008
  - FICHA-GOV-008
  - GOV-006
  - GOV-007
  - PPC-META-001
  - ARQ-001
produz_entrada_para: []
relaciona_se_com:
  - CASOS-INDEX
  - CASO-001-FONTES
  - CASO-001-DOCUMENTOS-TECNICOS
  - CASO-001-GEOMETRIA
  - CASO-001-DADOS-CHUVA
  - PPC-001
  - MODELO-INDICADORES-001
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
estado_do_portao: preparacao
territorio_preliminar: Sub-bacia de Itapeba, Maricá/RJ; polígono oficial pendente
periodo_preliminar: 2022-01-01 a 2026-06-30
issue_acompanhamento: 2
---

# CASO-001 — Registro de prontidão

## 1. Decisão atual

**Permanece em preparação.**

A pesquisa consolidou 15 fontes gerais e um registro técnico com 8 fontes oficiais ou institucionais, 20 alegações, 3 inconsistências e 7 grupos documentais requeridos. Foram distinguidos comunicação institucional, registro financeiro, orientação procedimental, índice de contratação e registro histórico.

Essa estrutura melhora a rastreabilidade, mas não substitui documentos integrais. Ainda faltam a feição oficial de Itapeba, o programa final, contratos, projetos, geometrias, cronogramas, medições, séries reais, interlocutores, participação local e revisão independente.

Este registro não inicia o PPC-001 e não constitui diagnóstico, avaliação de obra, recomendação ou decisão oficial.

## 2. Pergunta decisória revisada

Como estruturar uma decisão pública auditável para reduzir riscos e impactos de alagamentos na sub-bacia de Itapeba, articulando macrodrenagem, microdrenagem, manutenção, monitoramento e comunicação de risco, sem presumir previamente a combinação adequada de medidas?

## 3. Delimitação preliminar

| Elemento | Definição atual | Limitação |
|---|---|---|
| unidade territorial | sub-bacia de Itapeba, Maricá/RJ | polígono e limites oficiais ainda não obtidos |
| fonte poligonal candidata | GeoINEA `GPL_SUBBACIAS_ERJ_50`, camada 4 | resposta oficial não recebida pelos runners hospedados |
| fonte hidrográfica complementar | Projeto RJ25, escala 1:25.000 | linhas de drenagem não definem o polígono |
| referência espacial candidata | EPSG:4674 — SIRGAS 2000 | deve ser confirmada no arquivo preservado |
| período | 2022-01-01 a 2026-06-30 | poderá mudar após avaliação de completude |
| evento de referência | chuvas de abril de 2022 | deve ser confrontado com séries brutas |
| população | moradores, usuários, trabalhadores e serviços na área | depende do polígono e de dados oficiais |

Falha de conectividade não significa ausência da feição.

## 4. Responsabilidade documental e atores potenciais

| Função ou unidade | Situação |
|---|---|
| Projeto Pragmatismo Cívico | responsável pela documentação |
| Defesa Civil | fonte potencial para riscos, alertas e ocorrências |
| SOMAR | fonte potencial para drenagem, manutenção e obras |
| Urbanismo e Planejamento Territorial | fonte potencial para uso do solo e cartografia |
| Meio Ambiente e Sustentabilidade | fonte potencial para soluções ambientais e monitoramento |
| SANEMAR | interface com esgotamento e recursos hídricos |
| INEA | produtor de geosserviços e sistemas hidrometeorológicos |
| CAIXA | agente financeiro das operações divulgadas |
| revisão independente | indisponível; cadastro permanece vazio |

A listagem não representa parceria, anuência ou participação confirmada.

## 5. Fontes e documentos técnicos

A [Matriz de Fontes](CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md) contém `F-001` a `F-015`. O [Registro Técnico](CASO-001_DOCUMENTOS_TECNICOS_E_CONTRATACOES.md) e seu JSON estruturado registram:

- 8 fontes técnicas ou financeiras;
- 20 alegações identificadas;
- 3 inconsistências abertas;
- 7 grupos documentais necessários;
- regras que impedem promover notícia a contrato;
- exigência de arquivo local e SHA-256 para fonte obtida ou tratada.

Nenhuma fonte está classificada como obtida ou tratada para uso empírico.

## 6. Estrutura financeira preliminar

As fontes consultadas atribuem às três intervenções de drenagem:

- investimento total agregado de aproximadamente R$ 123,1 milhões;
- R$ 117 milhões em recursos do FGTS;
- territórios descritos com variações entre Itaipuaçu, Itapeba, Jardim Atlântico, Jardim Atlântico Oeste e Barroco.

Ainda faltam valores individualizados, números de proposta e operação, contratos, contrapartidas, cronogramas, metas e condições de desembolso.

O Pregão Eletrônico 14/2026 — Smart Drainage permanece separado das operações do Novo PAC. Valor estimado e registro de preços não equivalem a contrato ou implantação.

## 7. Inconsistências que bloqueiam uso decisório

| ID | Tema | Estado |
|---|---|---|
| `INC-001` | aproximadamente 19.500 beneficiários na fonte da CAIXA versus mais de 300 mil na comunicação municipal | aberta |
| `INC-002` | nomes territoriais não individualizados | aberta |
| `INC-003` | investimento total versus recurso financiado | explicação provisória; contratos pendentes |

Os números permanecem atribuídos às respectivas fontes até reconciliação documental.

## 8. Documentos requeridos

| ID | Documento | Estado |
|---|---|---|
| `REQ-001` | programa final e produtos intermediários | pendente |
| `REQ-002` | contratação da consultoria e ordens de serviço | pendente |
| `REQ-003` | cartas-consulta e anexos das operações | pendente |
| `REQ-004` | termos e contratos de financiamento individualizados | pendente |
| `REQ-005` | projetos, QCI, riscos, geometrias e fotografias | pendente |
| `REQ-006` | edital, termo de referência e anexos do Pregão 14/2026 | pendente |
| `REQ-007` | cronogramas, medições, indicadores e relatórios | pendente |

## 9. Plano de dados e evidências

Regras:

- preservar dados e documentos brutos separadamente de extrações;
- calcular hash somente após preservar os bytes exatos;
- distinguir falha de conexão, resposta vazia e documento ausente;
- distinguir notícia, financiamento, contratação, projeto, medição e resultado;
- não combinar chuva, ocorrência, dano e obra como grandezas equivalentes;
- não inferir causalidade a partir de correlação temporal;
- não transformar linha de drenagem, bairro ou croqui em polígono oficial;
- registrar licença, restrição, transformação e revisão;
- publicar somente dados agregados quando necessário.

Estado de execução:

- processador pluviométrico testado com fixture sintético;
- coletor e validador geoespacial testados com respostas controladas;
- registro técnico validado automaticamente;
- nenhuma série real, resposta GeoINEA ou documento técnico integral foi incorporado.

## 10. Avaliação do portão

| Requisito | Estado | Evidência ou pendência |
|---|---|---|
| pergunta preliminar | atendido | pergunta revisada para Itapeba |
| território e período | parcial | unidade e período definidos; feição oficial pendente |
| responsável | atendido | responsável documental identificado |
| fontes mínimas | parcial | inventários estruturados; arquivos integrais pendentes |
| plano de dados | parcial | códigos e regras definidos; execução real pendente |
| documentos técnicos | parcial | 8 fontes e 7 grupos requeridos; nenhum integral obtido |
| grupos afetados | parcial | categorias mapeadas; canais e território pendentes |
| riscos e conflitos | atendido nesta etapa | salvaguardas e inconsistências registradas |
| estratégia de revisão | não atendido | cadastro sem revisor elegível ou ativo |
| critérios de suspensão | atendido | definidos abaixo |

## 11. Critérios de suspensão ou encerramento

O caso permanecerá em preparação, será suspenso ou encerrado diante de impossibilidade de obter delimitação confiável, fontes mínimas, qualidade compatível, proteção de dados, capacidade de revisão, salvaguardas para conflitos ou proporcionalidade de custo e aprendizado.

## 12. Pendências prioritárias

1. obter REQ-001 e REQ-002;
2. obter REQ-003 a REQ-005;
3. obter REQ-006 e REQ-007;
4. reconciliar beneficiários e nomes territoriais;
5. executar o coletor GeoINEA em rede acessível;
6. baixar e revisar a série Cemaden;
7. confirmar interlocutores e participação;
8. obter revisão técnica;
9. emitir nova decisão do portão.

## 13. Resultado

- [ ] pronto para iniciar PPC-001;
- [x] permanece em preparação;
- [ ] suspenso;
- [ ] encerrado antes do diagnóstico.

## 14. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Fontes, recorte preliminar e decisão de preparação | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Matriz de fontes e retenção | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Fontes e protocolo geoespacial | Projeto Pragmatismo Cívico |
| 0.3.1 | 2026-07-18 | correção | Tentativas GeoINEA e distinção de falha de conexão | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-18 | compatível | Registro técnico, estrutura financeira, inconsistências e documentos requeridos | Projeto Pragmatismo Cívico |
