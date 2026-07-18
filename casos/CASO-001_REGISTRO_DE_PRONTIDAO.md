---
id: CASO-001-PRONTIDAO
titulo: Registro de Prontidão do CASO-001 — Sub-bacia de Itapeba
versao: 0.3.0
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

A pesquisa de fontes públicas permitiu reduzir o escopo municipal para a **sub-bacia de Itapeba** e definir um período preliminar de **1º de janeiro de 2022 a 30 de junho de 2026**. A matriz canônica consolidou 15 fontes. Foram localizados serviços oficiais do GeoINEA com polígonos estaduais de sub-bacias e hidrografia na escala 1:25.000. Os validadores de chuva e geometria passaram em testes exclusivamente sintéticos.

O portão não está aprovado porque ainda faltam a feição oficial de Itapeba, arquivos técnicos integrais, coleta e revisão das séries reais, confirmação de interlocutores institucionais, plano participativo local e revisão independente.

Este registro não inicia o PPC-001 e não constitui diagnóstico, avaliação de obra, recomendação ou decisão oficial.

## 2. Pergunta decisória revisada

Como estruturar uma decisão pública auditável para reduzir riscos e impactos de alagamentos na sub-bacia de Itapeba, articulando macrodrenagem, microdrenagem, manutenção, monitoramento e comunicação de risco, sem presumir previamente a combinação adequada de medidas?

## 3. Delimitação preliminar

| Elemento | Definição atual | Limitação |
|---|---|---|
| unidade territorial | sub-bacia de Itapeba, Maricá/RJ | polígono e limites oficiais ainda não obtidos |
| fonte poligonal candidata | GeoINEA `GPL_SUBBACIAS_ERJ_50`, camada 4 | não foi confirmada feição denominada Itapeba nem equivalência com o recorte municipal |
| fonte hidrográfica complementar | Projeto RJ25, escala 1:25.000 | linhas de drenagem não definem o polígono da bacia |
| referência espacial candidata | EPSG:4674 — SIRGAS 2000 | deve ser confirmada no arquivo e nos metadados preservados |
| foco operacional | drenagem pluvial, ocorrências de alagamento, monitoramento e alerta | não inclui avaliação integral de saneamento ou risco geológico |
| período | 2022-01-01 a 2026-06-30 | poderá mudar após avaliação de completude das séries |
| evento de referência | chuvas de abril de 2022 | registro público operacional ainda precisa ser confrontado com séries brutas |
| contexto de intervenção | contratos e iniciativas divulgados em 2026 | comunicações institucionais não substituem projetos, medições ou contratos completos |
| população | moradores, usuários, trabalhadores e serviços situados na área delimitada | quantidade e perfil dependem do polígono e de dados oficiais |

O período começa em 2022 para incluir um evento público com acumulado elevado registrado em Itapeba e termina em junho de 2026 para preservar uma janela fechada anterior a este registro.

## 4. Responsabilidade documental e atores a consultar

| Função | Situação |
|---|---|
| responsável pela documentação | Projeto Pragmatismo Cívico |
| Secretaria de Proteção e Defesa Civil | fonte e interlocutora potencial para riscos, monitoramento, alertas e ocorrências |
| Serviços de Obras de Maricá — SOMAR | fonte e interlocutora potencial para drenagem, manutenção e obras |
| Secretaria de Urbanismo e Planejamento Territorial | fonte e interlocutora potencial para Plano Diretor, uso do solo e cartografia |
| Secretaria de Meio Ambiente e Sustentabilidade | fonte e interlocutora potencial para soluções ambientais e monitoramento inteligente |
| Companhia de Saneamento de Maricá — SANEMAR | interlocutora potencial apenas nas interfaces entre drenagem, esgotamento e recursos hídricos |
| Instituto Estadual do Ambiente — INEA | órgão produtor de geosserviços candidatos e sistemas hidrometeorológicos |
| revisão independente | não disponível; cadastro público permanece vazio |

A listagem não representa parceria, anuência, responsabilidade atribuída nem participação confirmada dessas instituições.

## 5. Matriz canônica de fontes

A [Matriz de Fontes e Lacunas](CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md) é o registro canônico desta etapa. Ela contém identificadores `F-001` a `F-015`, órgão, título, data, URL, classe, cobertura, formato, licença conhecida, estado de obtenção, hash, uso, risco e relação com o portão.

Resultados relevantes:

- 15 fontes públicas foram consolidadas;
- a Lei Complementar nº 400/2025 foi consultada em PDF oficial;
- o Anexo II de mapas do Plano Diretor foi localizado, mas ainda não foi obtido e inspecionado com hash;
- a página pública do Cemaden confirma estação denominada Itapeba, mas código, coordenadas e histórico ainda devem ser confirmados;
- a camada poligonal `GPL_SUBBACIAS_ERJ_50` publica geometria de sub-bacias em EPSG:4674 e aceita GeoJSON, mas a feição de Itapeba não foi obtida;
- a hidrografia RJ25 foi registrada como fonte de conferência topológica, não como limite automático;
- nenhuma fonte desta versão foi classificada como `obtida` ou `tratada` para fins empíricos.

Comunicação institucional permanece identificada como tal e não substitui contrato, projeto, medição ou avaliação de eficácia.

## 6. Plano de dados e geometria

A etapa de preparação utilizará apenas fontes públicas ou formalmente autorizadas.

Regras gerais:

- arquivar URL, título, órgão, data de acesso, período coberto e versão;
- preservar dados brutos separadamente de dados tratados;
- calcular hash somente após preservar os bytes exatos;
- registrar parâmetros de consulta e respostas vazias;
- converter horários UTC de forma explícita;
- verificar lacunas, duplicidades, valores impossíveis e mudanças de estação;
- não combinar registros de chuva, ocorrência e dano como se fossem equivalentes;
- não inferir causalidade a partir de correlação temporal;
- não transformar linha de drenagem, nome de bairro ou croqui em polígono oficial;
- publicar somente dados agregados quando houver risco de identificação;
- registrar licença, restrição e método de transformação;
- não utilizar comunicação institucional como prova suficiente de desempenho;
- revisar retenção, descarte, backups e acesso conforme `CASO-001-DADOS-CHUVA`.

Estado de execução:

- processador de chuva, manifesto, relatório e flags foram testados com fixture sintético;
- validador GeoJSON, hash, relatório e rejeição de anel aberto foram testados com fixture sintético;
- estrutura local e política de retenção e descarte estão definidas;
- nenhum arquivo mensal real foi adquirido, processado ou revisado;
- nenhuma geometria oficial foi adquirida, processada ou revisada;
- a suficiência da estação, do período e do recorte ainda não foi demonstrada.

## 7. Grupos e serviços a mapear

A delimitação deverá identificar, sem presumir representação:

- moradores e trabalhadores da sub-bacia;
- pessoas com mobilidade reduzida ou barreiras de comunicação;
- escolas, unidades de saúde e assistência;
- transporte e vias críticas;
- comércio e serviços locais;
- equipes de manutenção, obras e resposta;
- organizações comunitárias e ambientais;
- usuários de áreas a jusante ou conectadas hidraulicamente.

O plano participativo ainda não está definido.

## 8. Conflitos e salvaguardas

- não existe fornecedor ou tecnologia selecionada;
- não existe vínculo declarado com órgão municipal, contratada ou financiador;
- comunicações oficiais serão tratadas como fontes institucionais, não como avaliação independente;
- geosserviço oficial não será tratado como feição adequada sem consulta e revisão;
- a iniciativa de drenagem inteligente será examinada como alternativa ou fonte de dados, sem endosso;
- qualquer contato institucional, apoio ou conflito posterior deverá ser registrado;
- urgência operacional não autoriza pular diagnóstico ou proteção de dados.

## 9. Documentos e versões previstos

| Documento | Versão |
|---|---:|
| GOV-008 | 0.1.0 |
| FICHA-GOV-008 | 0.1.0 |
| CASO-001-FONTES | 0.2.0 |
| CASO-001-GEOMETRIA | 0.1.0 |
| CASO-001-DADOS-CHUVA | 0.2.0 |
| PPC-001 | 0.1.1 |
| CICLO-PC-001 | 0.1.0 |
| MODELO-INDICADORES-001 | 0.1.0 |
| GOV-006 | 0.1.0 |
| GOV-007 | 0.1.1 |

As versões serão congeladas novamente quando o portão for decidido.

## 10. Avaliação do portão

| Requisito | Estado | Evidência ou pendência |
|---|---|---|
| pergunta preliminar | atendido | pergunta revisada para a sub-bacia de Itapeba |
| território e período | parcial | unidade, período e geosserviço candidato definidos; feição oficial pendente |
| responsável | atendido | Projeto Pragmatismo Cívico responsável pela documentação |
| fontes mínimas | parcial | 15 fontes consolidadas; arquivos técnicos, geometria e séries reais ainda não obtidos |
| plano de dados | parcial | processadores, retenção e descarte definidos; execução real e revisão manual pendentes |
| grupos afetados | parcial | categorias mapeadas; território e canais de participação pendentes |
| riscos e conflitos | atendido nesta etapa | salvaguardas e ausência de solução pré-selecionada registradas |
| versões | atendido | conjunto inicial registrado |
| estratégia de revisão | não atendido | cadastro sem revisor elegível ou ativo |
| critérios de suspensão | atendido | definidos na seção seguinte |

## 11. Critérios de suspensão ou encerramento

O caso permanecerá em preparação, será suspenso ou encerrado quando ocorrer:

- impossibilidade de obter delimitação territorial confiável;
- ausência de séries ou registros mínimos para o período;
- qualidade de dados incompatível com a pergunta;
- impossibilidade de tratar riscos de privacidade ou segurança;
- ausência prolongada de capacidade de revisão;
- conflito material sem salvaguarda;
- exigência de promover solução, fornecedor ou narrativa prévia;
- custo de continuidade desproporcional ao aprendizado possível.

## 12. Pendências prioritárias

1. consultar a camada `GPL_SUBBACIAS_ERJ_50`, preservar a resposta e confirmar ou refutar correspondência com Itapeba;
2. obter recorte da hidrografia RJ25 para conferência topológica;
3. obter e inspecionar o anexo cartográfico do Plano Diretor;
4. obter produtos técnicos do Programa Municipal de Drenagem;
5. obter documentação técnica e geometrias das intervenções anunciadas para 2026;
6. baixar e testar as séries da estação Cemaden Itapeba;
7. verificar estações e dados históricos do INEA e da ANA;
8. solicitar ou localizar registros administrativos agregados de ocorrências;
9. confirmar interlocutores institucionais e estruturar participação local;
10. obter ao menos revisão técnica elegível ou registrar impossibilidade;
11. emitir nova decisão do portão.

## 13. Resultado

- [ ] pronto para iniciar PPC-001;
- [x] permanece em preparação;
- [ ] suspenso;
- [ ] encerrado antes do diagnóstico.

## 14. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Verificação de fontes públicas, recorte preliminar da sub-bacia de Itapeba e decisão de manter o caso em preparação | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Consolidação da matriz de fontes, protocolo de retenção e atualização da avaliação do portão | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Inclusão de fontes geoespaciais, protocolo de delimitação, validador GeoJSON e novo status de CI | Projeto Pragmatismo Cívico |
