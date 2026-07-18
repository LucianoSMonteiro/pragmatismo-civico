---
id: CASO-001-FONTES
titulo: Matriz de Fontes e Lacunas do CASO-001
versao: 0.2.1
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
  - CASO-001-PRONTIDAO
  - CASO-001-DADOS-CHUVA
  - GOV-008
  - PPC-META-001
  - ARQ-001
produz_entrada_para: []
relaciona_se_com:
  - CASOS-INDEX
  - CASO-001-GEOMETRIA
  - PPC-001
  - MODELO-INDICADORES-001
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
issue_acompanhamento: 10
estado_da_matriz: preparacao
---

# CASO-001 — Matriz de fontes e lacunas

## 1. Estado

Esta matriz consolida **15 fontes públicas** localizadas para preparar o CASO-001. Ela distingue comunicação institucional, norma, plano, cartografia, documentação técnica e portal de dados; registra o que foi apenas localizado, o que pôde ser consultado e o que ainda precisa ser obtido integralmente.

A matriz **não valida diagnóstico, causalidade, desempenho de órgão, eficácia de obra ou suficiência da evidência**. O portão permanece fechado.

Data desta verificação: **18 de julho de 2026**.

A camada estadual de sub-bacias foi confirmada como fonte candidata por seus metadados públicos. Duas séries de aquisição a partir de runners hospedados falharam antes do recebimento de qualquer byte. Isso é uma limitação de conectividade, não consulta vazia e não evidência de ausência da feição.

## 2. Escala de estado

| Estado | Significado |
|---|---|
| localizada | a existência e a URL foram verificadas |
| consultada | o conteúdo público disponível foi lido, sem arquivamento canônico local |
| obtida | o arquivo integral foi preservado com proveniência e hash |
| tratada | a fonte foi transformada por procedimento documentado e revisada |
| pendente | o conteúdo integral, o arquivo ou a cobertura necessária ainda não foi obtido |
| bloqueada no ambiente | a fonte existe, mas o ambiente de coleta não conseguiu estabelecer conexão ou receber resposta |

Nenhuma fonte desta versão está classificada como `obtida` ou `tratada` para fins empíricos do caso.

## 3. Registro canônico

| ID | Órgão e fonte | Classe | Estado | Cobertura ou data principal |
|---|---|---|---|---|
| F-001 | Prefeitura / Plano de Contingência Municipal 2026 | plano referido por comunicação institucional | localizada | município; prevenção e resposta em 2026 |
| F-002 | Prefeitura / contratos anunciados em janeiro de 2026 | comunicação institucional | consultada | Itapeba e Itaipuaçu; publicação de 2026-01-06 |
| F-003 | Prefeitura e Defesa Civil / chuvas de abril de 2022 | registro operacional publicado | consultada | evento de 1º e 2 de abril de 2022 |
| F-004 | Prefeitura e SOMAR / Programa Municipal de Drenagem | plano referido por comunicação institucional | consultada | município; prognóstico e audiência de 2023-10-25 |
| F-005 | Prefeitura / portal do Plano Diretor | repositório oficial | consultada | território municipal e processo de revisão |
| F-006 | Município / Lei Complementar nº 400/2025 | norma | consultada | Plano Diretor vigente; publicação oficial de 2025 |
| F-007 | Prefeitura / Anexo II — Mapas do Plano Diretor | cartografia | localizada, pendente | território municipal; revisão cartográfica de 2024 |
| F-008 | Cemaden / Pluviômetros Automáticos | documentação de dados | consultada | rede nacional; dados brutos em UTC |
| F-009 | Cemaden / página da estação Itapeba `idpcd=3717` | portal de dados | consultada | estação denominada Itapeba; metadados pendentes |
| F-010 | Cemaden / download mensal do Mapa Interativo | portal de dados | consultada, coleta pendente | arquivos mensais por UF e município |
| F-011 | INEA / Monitoramento Hidrometeorológico | portal de dados e documentação | consultada | Estado do Rio de Janeiro |
| F-012 | ANA / Hidroweb e Rede Hidrometeorológica Nacional | portal de dados | consultada | rede nacional de chuva, nível e vazão |
| F-013 | Prefeitura / sistema inteligente de prevenção de enchentes | comunicação institucional | consultada | iniciativa municipal divulgada em 2026-06-18 |
| F-014 | INEA / `GPL_SUBBACIAS_ERJ_50`, camada 4 | geosserviço vetorial poligonal | consultada em metadados; aquisição hospedada bloqueada; feição pendente | sub-bacias do Estado do Rio de Janeiro |
| F-015 | INEA, IBGE e SEA-RJ / hidrografia RJ25 | geosserviço vetorial linear | consultada, dados pendentes | hidrografia estadual na escala 1:25.000 |

## 4. Proveniência, formato e integridade

| ID | URL canônica | Formato consultado | Licença ou restrição conhecida | Hash |
|---|---|---|---|---|
| F-001 | <https://www.marica.rj.gov.br/noticia/prefeitura-de-marica-apresenta-plano-de-contingencia-municipal-2026-em-audiencia-publica/> | HTML | não identificada; plano integral pendente | não aplicável à página dinâmica |
| F-002 | <https://www.marica.rj.gov.br/noticia/prefeitura-de-marica-assina-contratos-de-r-267-milhoes-com-o-governo-federal-para-investimentos-em-transporte-saneamento-e-drenagem/> | HTML | não identificada; contratos integrais pendentes | não aplicável à página dinâmica |
| F-003 | <https://www.marica.rj.gov.br/noticia/prefeitura-de-marica-cria-cinturao-de-apoio-as-vitimas-das-enchentes/> | HTML | não identificada | não aplicável à página dinâmica |
| F-004 | <https://www.marica.rj.gov.br/noticia/moradores-de-marica-debatem-programa-municipal-de-drenagem-2/> | HTML | não identificada; produtos técnicos pendentes | não aplicável à página dinâmica |
| F-005 | <https://www.marica.rj.gov.br/plano-diretor/> | HTML com ligações para documentos | não identificada | não aplicável à página dinâmica |
| F-006 | <https://www.marica.rj.gov.br/wp-content/uploads/2025/02/Lei_400_17-01-2025-PDM_JOM_1691.pdf> | PDF oficial, 22 páginas | ato normativo público; redistribuição do arquivo não verificada | pendente; bytes não preservados |
| F-007 | <https://www.marica.rj.gov.br/wp-content/uploads/2024/11/ANEXOS_Mapas-PDM22-rev24_compressed.pdf> | PDF cartográfico | não verificada | pendente |
| F-008 | <https://www2.cemaden.gov.br/pluviometros-automatico/> | HTML | redistribuição dos arquivos mensais não verificada | não aplicável à página dinâmica |
| F-009 | <https://resources.cemaden.gov.br/graficos/interativo/grafico_CEMADEN.php?idpcd=3717&uf=RJ> | página dinâmica | não verificada | não aplicável |
| F-010 | <https://mapainterativo.cemaden.gov.br/> | interface e arquivos mensais | confirmação humana; licença dos arquivos pendente | pendente para cada arquivo |
| F-011 | <https://www.inea.rj.gov.br/ar-agua-e-solo/monitoramento-hidrometeorologico/> | HTML e sistemas ligados | licença dos dados históricos não verificada | não aplicável à página dinâmica |
| F-012 | <https://www.gov.br/ana/pt-br/assuntos/aplicativos-sistemas> e <https://www.snirh.gov.br/hidroweb> | portais e serviços | licença dos conjuntos deve ser confirmada separadamente | pendente para arquivos obtidos |
| F-013 | <https://www.marica.rj.gov.br/noticia/marica-investe-em-sistema-inteligente-para-prevencao-de-enchentes/> | HTML | não identificada | não aplicável à página dinâmica |
| F-014 | <https://geoportal.inea.rj.gov.br/server/rest/services/Recursos_Hidricos_Gestao_Costeira/MapServer/4> | ArcGIS Feature Layer; JSON, GeoJSON e PBF | metadados e condições de redistribuição ainda devem ser preservados | nenhum hash da fonte: nenhuma resposta recebida nas tentativas hospedadas |
| F-015 | <https://geoportal.inea.rj.gov.br/server/rest/services/GLN_HIDROGRAFIA_SEM_CANAL_25K/MapServer/0> | ArcGIS Feature Layer; JSON, GeoJSON e PBF | copyright publicado do IBGE; condições do arquivo exportado devem ser verificadas | pendente |

Os hashes `4d2d2b2c450f1967cbf4ec8113de39d146bad01e408d3bdb4b4f8e4741e87bbe` e `7be511784a29ec17b4ef26b02778e2fd8f97d82e89cdef1a4304cd5147718914` identificam os **artefatos de diagnóstico da CI**, não respostas do GeoINEA.

## 5. Uso, limitações e lacunas

| ID | Uso permitido nesta etapa | Limitação ou lacuna principal |
|---|---|---|
| F-001 | identificar protocolos, riscos, atribuições e pontos de apoio a confirmar | notícia não substitui PLACON integral nem comprova capacidade |
| F-002 | confirmar que contratos relacionados a drenagem e saneamento foram anunciados | faltam contratos, financiamentos, projetos, geometrias, cronogramas, medições e indicadores |
| F-003 | selecionar evento de referência e orientar pedidos de registros agregados | acumulado, ocorrência, dano e causa não são equivalentes; série bruta pendente |
| F-004 | identificar processo, alternativas e participação já divulgados | faltam plano de trabalho, diagnóstico, prognóstico, ações, bases, mapas e atas |
| F-005 | localizar produtos territoriais e memória participativa | minutas e produtos podem ter sido superados pela lei aprovada |
| F-006 | confirmar marco urbanístico, anexos e diretrizes vigentes | a lei não define sozinha o polígono da sub-bacia |
| F-007 | fornecer contexto municipal de macrozoneamento e sistemas territoriais | não foi demonstrado que contenha limite hidrográfico de Itapeba; escala e SRID pendentes |
| F-008 | documentar natureza bruta, inconsistências possíveis e horário UTC | disponibilidade não equivale a qualidade ou representatividade espacial |
| F-009 | orientar identificação preliminar e filtro da estação | nome e parâmetro não comprovam localização dentro do futuro polígono |
| F-010 | permitir aquisição da série conforme protocolo pluviométrico | coleta real, hashes, processamento e revisão ainda pendentes |
| F-011 | buscar chuva, nível, radar e fonte independente de comparação | cobertura estadual não garante estação representativa de Itapeba |
| F-012 | localizar estações e séries complementares | presença ou ausência de estação não define comparabilidade espacial ou temporal |
| F-013 | identificar possível fonte futura e alternativa de monitoramento | anúncio não comprova implantação, precisão, cobertura ou eficácia |
| F-014 | fornecer camada candidata de polígonos estaduais de sub-bacias | runners hospedados não alcançaram o serviço; presença nominal e equivalência temática continuam desconhecidas |
| F-015 | conferir drenagem e coerência topológica na escala 1:25.000 | linhas de drenagem não definem divisor ou polígono de sub-bacia |

## 6. Fontes geoespaciais candidatas

### F-014 — Camada estadual de sub-bacias

- **órgão:** Instituto Estadual do Ambiente — INEA;
- **serviço:** `Recursos_Hidricos_Gestao_Costeira/MapServer`;
- **camada:** `GPL_SUBBACIAS_ERJ_50`, ID `4`;
- **tipo:** Feature Layer, geometria poligonal;
- **campo de exibição:** `sub_bacias`;
- **campo regional:** `rh`;
- **referência espacial publicada:** EPSG:4674 — SIRGAS 2000;
- **formatos:** JSON, GeoJSON e PBF;
- **item do serviço:** `e20f5ed7320d45e7a2d0fa2f0e84cf54`;
- **estado:** metadados públicos consultados; nenhuma resposta de API recebida pelos runners hospedados;
- **tratamento:** `CASO-001-GEOMETRIA`, coletor auditável, transporte IPv4 e validador GeoJSON.

Tentativas executadas:

| Execução | Transporte | Tentativas | Resultado |
|---:|---|---:|---|
| `29658467155` | Python HTTP padrão | 3 | timeout antes dos metadados |
| `29658776194` | `curl --ipv4` | 3 | conexão TCP/TLS não estabelecida antes do timeout |

A camada permanece candidata prioritária. A falha do ambiente hospedado não confirma nem refuta a presença de Itapeba.

### F-015 — Hidrografia do Projeto RJ25

- **órgãos:** IBGE e Governo do Estado do Rio de Janeiro / SEA-RJ;
- **serviço:** `GLN_HIDROGRAFIA_SEM_CANAL_25K/MapServer`;
- **camada:** trechos de drenagem, ID `0`;
- **escala declarada:** 1:25.000;
- **referência espacial publicada:** EPSG:4674 — SIRGAS 2000;
- **formatos:** JSON, GeoJSON e PBF;
- **item do serviço:** `3cfe5a77b64c480ea3de9a062f766599`;
- **estado:** metadados consultados; recorte de Itapeba não obtido;
- **uso:** comparação topológica e contextual, nunca geração automática do limite oficial.

## 7. Relação com o portão de prontidão

| Requisito | Fontes relacionadas | Estado atual |
|---|---|---|
| pergunta preliminar | F-002, F-003, F-004, F-013 | suficiente apenas para formular a pergunta, não para respondê-la |
| território e período | F-003, F-005, F-006, F-007, F-009, F-014 e F-015 | parcial; serviço candidato localizado, coleta hospedada bloqueada e polígono pendente |
| autoridades e interlocutores | F-001, F-002, F-004 e F-013 | potenciais, sem participação confirmada |
| fontes mínimas | F-001 a F-015 | inventário consolidado; arquivos técnicos, feição oficial e dados reais pendentes |
| plano de dados | F-008 a F-012, F-014, F-015, `CASO-001-DADOS-CHUVA` e `CASO-001-GEOMETRIA` | códigos testados sinteticamente; execução real depende de ambiente com acesso às fontes |
| grupos afetados e participação | F-001, F-003, F-004 e F-005 | categorias e processos localizados; recorte e canais do caso pendentes |
| riscos e conflitos | F-002, F-004 e F-013 | comunicações e fornecedores não serão tratados como avaliação independente |
| estratégia de revisão | todas | não atendida; cadastro de revisores permanece vazio |

## 8. Lacunas prioritárias

1. **geometria:** repetir a consulta em rede que alcance o GeoINEA, preservar a resposta e então confirmar ou refutar correspondência nominal; registrar sistema de referência, escala, data, licença e hash;
2. **programa de drenagem:** obter produtos técnicos integrais e bases do diagnóstico, prognóstico e plano de ações;
3. **intervenções de 2026:** obter contratos, projetos, geometrias, cronogramas, medições e indicadores;
4. **chuva real:** realizar downloads mensais autorizados, gerar hashes, processar e revisar flags;
5. **estações complementares:** verificar inventários do INEA e ANA e comparabilidade espacial e temporal;
6. **ocorrências e danos:** obter registros administrativos agregados e seus critérios;
7. **participação:** confirmar interlocutores e canais acessíveis para pessoas situadas no polígono;
8. **revisão:** formar capacidade técnica independente e registrar conflitos.

## 9. Regras de manutenção

- uma fonte nova recebe identificador estável `F-nnn`;
- página ou serviço localizado não é marcado como arquivo obtido;
- falha de rede não é registrada como consulta concluída sem resultado;
- hash somente é registrado após preservação dos bytes exatos;
- consulta concluída sem feição também deve ser preservada;
- republicação gera nova versão ou novo registro de origem;
- notícia institucional permanece comunicação, mesmo quando descreve contrato ou resultado;
- fonte superada não é apagada: seu estado e substituição são registrados;
- transformação aponta para origem, script, parâmetros e saída;
- linha de drenagem não pode ser convertida silenciosamente em polígono;
- a matriz deve ser revisada antes de nova decisão do portão.

## 10. Resultado

- [x] 15 fontes localizadas consolidadas;
- [x] classes e estados diferenciados;
- [x] limitações, licenças conhecidas e riscos registrados;
- [x] fontes relacionadas aos requisitos do portão;
- [x] geosserviço poligonal candidato identificado;
- [x] coletor, transporte IPv4 e validador testados com fixtures;
- [x] tentativas reais hospedadas e falhas de conectividade documentadas;
- [ ] resposta oficial da API recebida e preservada;
- [ ] feição oficial de Itapeba obtida e preservada;
- [ ] arquivos técnicos integrais obtidos e preservados;
- [ ] hashes das fontes reais calculados;
- [ ] séries reais coletadas e tratadas;
- [ ] suficiência revisada independentemente.

A conclusão documental desta matriz resolve a dispersão do inventário, mas **não resolve as lacunas empíricas**.

## 11. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Consolidação de 13 fontes oficiais, estados de obtenção, usos, limitações e lacunas do portão | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Inclusão das camadas de sub-bacias e hidrografia do GeoINEA e do protocolo de validação geoespacial | Projeto Pragmatismo Cívico |
| 0.2.1 | 2026-07-18 | correção | Distinção entre falha de conectividade, consulta vazia e ausência nominal; registro das tentativas hospedadas | Projeto Pragmatismo Cívico |
