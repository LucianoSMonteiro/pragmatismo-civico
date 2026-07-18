---
id: CASO-001-FONTES
titulo: Matriz de Fontes e Lacunas do CASO-001
versao: 0.1.0
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
  - PPC-001
  - MODELO-INDICADORES-001
substitui: []
substituido_por: null
compatibilidade: inicial
proxima_revisao: null
issue_acompanhamento: 10
estado_da_matriz: preparacao
---

# CASO-001 — Matriz de fontes e lacunas

## 1. Estado

Esta matriz consolida as fontes públicas localizadas para preparar o CASO-001. Ela distingue comunicação institucional, norma, plano, cartografia e portal de dados; registra o que foi apenas localizado, o que pôde ser consultado e o que ainda precisa ser obtido integralmente.

A matriz **não valida diagnóstico, causalidade, desempenho de órgão, eficácia de obra ou suficiência da evidência**. O portão permanece fechado.

Data desta verificação: **18 de julho de 2026**.

## 2. Escala de estado

| Estado | Significado |
|---|---|
| localizada | a existência e a URL foram verificadas |
| consultada | o conteúdo público disponível foi lido, sem arquivamento canônico local |
| obtida | o arquivo integral foi preservado com proveniência e hash |
| tratada | a fonte foi transformada por procedimento documentado e revisada |
| pendente | o conteúdo integral, o arquivo ou a cobertura necessária ainda não foi obtido |

Nenhuma fonte desta versão está classificada como `obtida` ou `tratada` para fins empíricos do caso.

## 3. Registro resumido

| ID | Fonte | Classe | Estado | Papel principal |
|---|---|---|---|---|
| F-001 | Plano de Contingência Municipal 2026 | plano / comunicação institucional | localizada | protocolos, riscos e resposta |
| F-002 | Contratos anunciados em janeiro de 2026 | comunicação institucional | consultada | contexto de intervenções em Itapeba |
| F-003 | Registro municipal das chuvas de abril de 2022 | registro operacional publicado | consultada | evento de referência e ocorrências |
| F-004 | Programa Municipal de Drenagem e Manejo de Águas Pluviais | plano / comunicação institucional | consultada | processo, prognóstico e alternativas |
| F-005 | Portal do Plano Diretor | repositório oficial | consultada | documentos territoriais e participação |
| F-006 | Lei Complementar nº 400/2025 | norma | consultada | marco urbanístico vigente |
| F-007 | Anexo II — Mapas do Plano Diretor | cartografia | localizada, pendente | contexto cartográfico municipal |
| F-008 | Pluviômetros automáticos do Cemaden | documentação de dados | consultada | natureza, horário e limites dos dados |
| F-009 | Página da estação Itapeba — parâmetro `idpcd=3717` | portal de dados | consultada | identificação preliminar da estação |
| F-010 | Download mensal do Mapa Interativo do Cemaden | portal de dados | consultada, coleta pendente | série pluviométrica bruta |
| F-011 | Monitoramento hidrometeorológico do INEA | portal de dados | consultada | chuva, nível, radar e inventário estadual |
| F-012 | Hidroweb / Rede Hidrometeorológica Nacional | portal de dados | consultada | estações e séries complementares |
| F-013 | Sistema inteligente de prevenção de enchentes de 2026 | comunicação institucional | consultada | iniciativa de monitoramento da drenagem |

## 4. Fontes detalhadas

### F-001 — Plano de Contingência Municipal 2026

- **órgão:** Prefeitura de Maricá / Secretaria de Proteção e Defesa Civil;
- **título público:** Prefeitura de Maricá apresenta Plano de Contingência Municipal 2026 em Audiência Pública;
- **data da publicação:** 2025-11-19;
- **URL:** <https://www.marica.rj.gov.br/noticia/prefeitura-de-marica-apresenta-plano-de-contingencia-municipal-2026-em-audiencia-publica/>;
- **classe:** plano referido por comunicação institucional;
- **cobertura:** município de Maricá; prevenção, preparação e resposta em 2026;
- **formato consultado:** página HTML;
- **licença e restrição:** não identificadas na página consultada;
- **hash:** não aplicável à página dinâmica; documento técnico integral não obtido;
- **uso possível:** identificar níveis de severidade, atribuições, rotas, pontos de apoio e protocolos a confirmar;
- **risco de interpretação:** a notícia resume o plano, mas não substitui o documento integral nem comprova capacidade ou desempenho;
- **requisito do portão:** atores, riscos, resposta e comunicação;
- **lacuna:** obter o PLACON integral, anexos, versão e data canônica.

### F-002 — Contratos anunciados em janeiro de 2026

- **órgão:** Prefeitura de Maricá;
- **título:** Prefeitura de Maricá assina contratos de R$ 267 milhões com o Governo Federal para investimentos em transporte, saneamento e drenagem;
- **data da publicação:** 2026-01-06;
- **URL:** <https://www.marica.rj.gov.br/noticia/prefeitura-de-marica-assina-contratos-de-r-267-milhoes-com-o-governo-federal-para-investimentos-em-transporte-saneamento-e-drenagem/>;
- **classe:** comunicação institucional sobre contratos;
- **cobertura:** intervenções anunciadas em Itapeba e Itaipuaçu; a página separa esgotamento sanitário de macrodrenagem;
- **formato consultado:** página HTML;
- **licença e restrição:** não identificadas;
- **hash:** não aplicável à página dinâmica;
- **uso possível:** confirmar que foram anunciados contratos de drenagem e saneamento relacionados a Itapeba;
- **risco de interpretação:** valores e benefícios anunciados não equivalem a escopo executivo, medição, entrega ou eficácia;
- **requisito do portão:** contexto de intervenção e autoridades relacionadas;
- **lacuna:** obter contratos, financiamentos, projetos, geometrias, cronogramas, medições e indicadores.

### F-003 — Chuvas e ocorrências de abril de 2022

- **órgão:** Prefeitura de Maricá / Defesa Civil;
- **título:** Prefeitura de Maricá cria cinturão de apoio às vítimas das enchentes;
- **data da publicação:** 2022-04-02;
- **URL:** <https://www.marica.rj.gov.br/noticia/prefeitura-de-marica-cria-cinturao-de-apoio-as-vitimas-das-enchentes/>;
- **classe:** registro operacional publicado em comunicação institucional;
- **cobertura:** evento de 1º e 2 de abril de 2022; município e bairros atingidos;
- **informações publicadas:** 261,39 mm em 24 horas no pluviômetro de Itapeba e 30 ocorrências no bairro;
- **formato consultado:** página HTML;
- **licença e restrição:** não identificadas;
- **hash:** não aplicável à página dinâmica;
- **uso possível:** selecionar evento de referência e formular pedidos de registros agregados;
- **risco de interpretação:** acumulado, ocorrência, dano e causa não são equivalentes; o texto é registro de resposta, não série validada;
- **requisito do portão:** evento, período, fontes mínimas e grupos afetados;
- **lacuna:** confrontar com dados brutos, horários, inventário de ocorrências e critérios administrativos.

### F-004 — Programa Municipal de Drenagem

- **órgão:** Prefeitura de Maricá / Serviços de Obras de Maricá — SOMAR;
- **título:** Moradores de Maricá debatem Programa Municipal de Drenagem;
- **data da publicação:** 2023-10-25;
- **URL:** <https://www.marica.rj.gov.br/noticia/moradores-de-marica-debatem-programa-municipal-de-drenagem-2/>;
- **classe:** plano referido por comunicação institucional;
- **cobertura:** município; quarta audiência pública e prognóstico;
- **formato consultado:** página HTML;
- **licença e restrição:** não identificadas;
- **hash:** não aplicável à página dinâmica;
- **uso possível:** identificar que houve diagnóstico/prognóstico e propostas incluindo amortecimento, canais naturais e soluções não exclusivamente estruturais;
- **risco de interpretação:** a notícia não contém produtos técnicos, critérios, bases ou priorização completa;
- **requisito do portão:** fontes técnicas, alternativas e participação;
- **lacuna:** obter plano de trabalho, diagnóstico, prognóstico, plano de ações, bases, mapas e atas.

### F-005 — Portal do Plano Diretor

- **órgão:** Prefeitura de Maricá / Urbanismo;
- **título:** Plano Diretor — processo de revisão;
- **URL:** <https://www.marica.rj.gov.br/plano-diretor/>;
- **classe:** repositório oficial de documentos e participação;
- **cobertura:** território municipal e processo de revisão;
- **formato consultado:** página HTML com ligações para projeto de lei, mapas e produtos;
- **licença e restrição:** não identificadas;
- **hash:** não aplicável à página dinâmica;
- **uso possível:** localizar documentos territoriais e memória participativa;
- **risco de interpretação:** produtos de elaboração podem ter sido superados pela lei aprovada;
- **requisito do portão:** território, uso do solo, participação e fontes mínimas;
- **lacuna:** arquivar versões canônicas e distinguir minuta, produto técnico e norma vigente.

### F-006 — Lei Complementar nº 400/2025

- **órgão:** Município de Maricá / Jornal Oficial de Maricá;
- **título:** Lei Complementar nº 400, de 17 de janeiro de 2025;
- **data oficial:** 2025-01-17; publicação no JOM em 2025-01-24;
- **URL:** <https://www.marica.rj.gov.br/wp-content/uploads/2025/02/Lei_400_17-01-2025-PDM_JOM_1691.pdf>;
- **classe:** norma;
- **cobertura:** território municipal; Plano Diretor de Desenvolvimento Urbano Sustentável;
- **formato consultado:** PDF oficial, 22 páginas;
- **estado:** texto integral consultado, arquivo não incorporado ao acervo do caso;
- **licença e restrição:** ato normativo público; condições de redistribuição do arquivo não verificadas;
- **hash:** pendente, pois os bytes não foram arquivados localmente;
- **uso possível:** confirmar marco vigente, anexos indissociáveis e diretrizes de saneamento, drenagem, recursos hídricos, clima e participação;
- **risco de interpretação:** a lei não define por si só o polígono da sub-bacia nem substitui planos setoriais;
- **requisito do portão:** território, marco normativo e participação;
- **lacuna:** preservar cópia canônica com hash e relacionar artigos e anexos ao recorte.

### F-007 — Anexo II: Mapas do Plano Diretor

- **órgão:** Prefeitura de Maricá / Urbanismo;
- **título observado:** Anexos — Mapas PDM22 revisão 2024;
- **URL:** <https://www.marica.rj.gov.br/wp-content/uploads/2024/11/ANEXOS_Mapas-PDM22-rev24_compressed.pdf>;
- **classe:** cartografia oficial associada ao processo do Plano Diretor;
- **cobertura esperada:** território municipal;
- **formato:** PDF cartográfico;
- **estado:** URL oficial localizada; obtenção e inspeção integral pendentes;
- **licença e restrição:** não verificadas;
- **hash:** pendente;
- **uso possível:** contexto de macrozoneamento, sistemas territoriais e referências espaciais;
- **risco de interpretação:** o título e a associação ao Plano Diretor não demonstram que contenha limite oficial da sub-bacia de Itapeba;
- **requisito do portão:** território;
- **lacuna:** obter o PDF, calcular hash, identificar sistema de referência, escala, data e verificar se existe geometria hidrográfica útil.

### F-008 — Documentação dos pluviômetros automáticos do Cemaden

- **órgão:** Centro Nacional de Monitoramento e Alertas de Desastres Naturais — Cemaden;
- **título:** Pluviômetros Automáticos;
- **URL:** <https://www2.cemaden.gov.br/pluviometros-automatico/>;
- **classe:** documentação de fonte de dados;
- **cobertura:** rede nacional do Cemaden;
- **formato consultado:** página HTML;
- **licença e restrição:** não verificadas para redistribuição dos arquivos mensais;
- **hash:** não aplicável à página dinâmica;
- **uso possível:** registrar que os dados são brutos, podem conter inconsistências e usam UTC;
- **risco de interpretação:** disponibilidade pública não equivale a controle de qualidade ou representatividade espacial;
- **requisito do portão:** plano de dados e qualidade;
- **lacuna:** verificar metadados, licença e histórico da estação.

### F-009 — Página da estação Itapeba

- **órgão:** Cemaden;
- **título:** Informações das PCDs Cemaden;
- **URL:** <https://resources.cemaden.gov.br/graficos/interativo/grafico_CEMADEN.php?idpcd=3717&uf=RJ>;
- **classe:** portal de dados;
- **cobertura observada:** estações de Maricá, incluindo Itapeba;
- **estado:** consultada com parâmetro `idpcd=3717`; identificação canônica ainda deve ser confirmada nos arquivos mensais e metadados;
- **formato:** página dinâmica;
- **licença e restrição:** não verificadas;
- **hash:** não aplicável;
- **uso possível:** confirmar existência pública de estação denominada Itapeba e orientar filtro inicial;
- **risco de interpretação:** nome e parâmetro de URL não comprovam localização dentro do futuro polígono da sub-bacia;
- **requisito do portão:** fontes mínimas e plano de dados;
- **lacuna:** obter coordenadas, histórico de equipamento, código canônico e cobertura temporal.

### F-010 — Download mensal do Mapa Interativo do Cemaden

- **órgão:** Cemaden;
- **título:** Mapa Interativo — Download de Dados Pluviométricos;
- **URL:** <https://mapainterativo.cemaden.gov.br/>;
- **classe:** portal de dados;
- **cobertura:** arquivos mensais por UF e, opcionalmente, município;
- **formato:** interface web e arquivos de dados;
- **estado:** interface consultada; downloads reais pendentes;
- **restrição operacional:** confirmação humana de segurança para cada download;
- **hash:** pendente para cada arquivo;
- **uso possível:** aquisição da série bruta conforme `CASO-001-DADOS-CHUVA`;
- **risco de interpretação:** o arquivo municipal pode conter múltiplas estações e dados inconsistentes;
- **requisito do portão:** fontes mínimas, período e plano de dados;
- **lacuna:** executar coleta autorizada, preservar originais, gerar manifesto e revisar flags.

### F-011 — Monitoramento hidrometeorológico do INEA

- **órgão:** Instituto Estadual do Ambiente — INEA;
- **título:** Monitoramento Hidrometeorológico;
- **URL:** <https://www.inea.rj.gov.br/ar-agua-e-solo/monitoramento-hidrometeorologico/>;
- **classe:** portal de dados e documentação;
- **cobertura:** Estado do Rio de Janeiro; estações automáticas, radares e boletins;
- **formato consultado:** página HTML;
- **licença e restrição:** não verificadas para dados históricos;
- **hash:** não aplicável à página dinâmica;
- **uso possível:** buscar chuva, nível, radar, inventário de estações e fonte independente de comparação;
- **risco de interpretação:** cobertura estadual não garante estação representativa da sub-bacia de Itapeba;
- **requisito do portão:** fontes mínimas, qualidade e comparação;
- **lacuna:** consultar inventário, coordenadas, períodos e disponibilidade histórica para Maricá.

### F-012 — Hidroweb e Rede Hidrometeorológica Nacional

- **órgão:** Agência Nacional de Águas e Saneamento Básico — ANA;
- **título:** Hidroweb / Rede Hidrometeorológica Nacional;
- **URLs:** <https://www.gov.br/ana/pt-br/assuntos/aplicativos-sistemas> e <https://www.snirh.gov.br/hidroweb>;
- **classe:** portal de dados hidrológicos;
- **cobertura:** rede nacional; chuva, níveis, vazões e metadados de estações;
- **formato consultado:** páginas de serviço;
- **licença indicada no portal gov.br:** Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada para o conteúdo do site; licença dos conjuntos deve ser confirmada separadamente;
- **hash:** não aplicável às páginas dinâmicas;
- **uso possível:** localizar estações complementares e séries convencionais ou telemétricas;
- **risco de interpretação:** ausência de estação na sub-bacia não invalida a rede; presença de estação municipal não garante comparabilidade;
- **requisito do portão:** fontes mínimas e qualidade;
- **lacuna:** pesquisar inventário por município, bacia, coordenadas, operador e período.

### F-013 — Sistema inteligente de prevenção de enchentes

- **órgão:** Prefeitura de Maricá / Meio Ambiente e Sustentabilidade;
- **título:** Maricá investe em sistema inteligente para prevenção de enchentes;
- **data da publicação:** 2026-06-18;
- **URL:** <https://www.marica.rj.gov.br/noticia/marica-investe-em-sistema-inteligente-para-prevencao-de-enchentes/>;
- **classe:** comunicação institucional sobre iniciativa tecnológica;
- **cobertura anunciada:** rede municipal de microdrenagem;
- **formato consultado:** página HTML;
- **licença e restrição:** não identificadas;
- **hash:** não aplicável à página dinâmica;
- **uso possível:** identificar possível fonte futura de dados operacionais e alternativa de monitoramento;
- **risco de interpretação:** anúncio de investimento e funcionalidades não comprova implantação, cobertura, interoperabilidade, precisão ou eficácia;
- **requisito do portão:** contexto, alternativas, dados e conflitos;
- **lacuna:** obter processo, contrato, arquitetura, pontos instalados, governança dos dados, métricas e resultados.

## 5. Relação com o portão de prontidão

| Requisito | Fontes relacionadas | Estado atual |
|---|---|---|
| pergunta preliminar | F-002, F-003, F-004, F-013 | suficiente apenas para formular a pergunta, não para respondê-la |
| território e período | F-003, F-005, F-006, F-007, F-009 | parcial; período preliminar definido, polígono pendente |
| autoridades e interlocutores | F-001, F-002, F-004, F-013 | potenciais, sem participação confirmada |
| fontes mínimas | F-001 a F-013 | matriz consolidada; arquivos técnicos e dados reais pendentes |
| plano de dados | F-008 a F-012 e `CASO-001-DADOS-CHUVA` | processador e regras testados com dados sintéticos; execução real pendente |
| grupos afetados e participação | F-001, F-003, F-004, F-005 | categorias e processos localizados; recorte e canais do caso pendentes |
| riscos e conflitos | F-002, F-004, F-013 | comunicações e fornecedores não serão tratados como avaliação independente |
| estratégia de revisão | todas | não atendida; cadastro de revisores permanece vazio |

## 6. Lacunas prioritárias

1. **geometria:** obter fonte cartográfica com limite reproduzível da sub-bacia, sistema de referência, escala, data, licença e hash;
2. **programa de drenagem:** obter produtos técnicos integrais e bases do diagnóstico, prognóstico e plano de ações;
3. **intervenções de 2026:** obter contratos, projetos, geometrias, cronogramas, medições e indicadores;
4. **chuva real:** realizar downloads mensais autorizados, gerar hashes, processar e revisar flags;
5. **estações complementares:** verificar inventários do INEA e ANA e comparabilidade espacial e temporal;
6. **ocorrências e danos:** obter registros administrativos agregados e seus critérios;
7. **participação:** confirmar interlocutores e canais acessíveis para pessoas situadas no polígono;
8. **revisão:** formar capacidade técnica independente e registrar conflitos.

## 7. Regras de manutenção

- uma fonte nova recebe identificador estável `F-nnn`;
- página localizada não é marcada como arquivo obtido;
- hash somente é registrado após preservação dos bytes exatos;
- republicação deve gerar nova versão ou novo registro de origem;
- notícia institucional permanece classificada como comunicação, mesmo quando descreve contrato ou resultado;
- fonte superada não é apagada: seu estado e substituição são registrados;
- toda transformação deve apontar para origem, script, parâmetros e saída;
- a matriz deve ser revisada antes de nova decisão do portão.

## 8. Resultado

- [x] fontes localizadas consolidadas;
- [x] classes e estados diferenciados;
- [x] limitações e riscos registrados;
- [x] fontes relacionadas aos requisitos do portão;
- [ ] arquivos técnicos integrais obtidos e preservados;
- [ ] hashes das fontes de arquivo calculados;
- [ ] séries reais coletadas e tratadas;
- [ ] suficiência revisada independentemente.

A conclusão documental desta matriz resolve a dispersão do inventário, mas **não resolve as lacunas empíricas**.

## 9. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Consolidação de fontes oficiais, estados de obtenção, usos, limitações e lacunas do portão | Projeto Pragmatismo Cívico |
