---
id: CASO-001
titulo: Preparação do Estudo Demonstrativo sobre Drenagem Urbana e Alerta Preventivo na Sub-bacia de Itapeba
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
  - GOV-008
  - FICHA-GOV-008
  - CICLO-PC-001
  - PPC-001
  - ARQ-003
  - PPC-META-001
  - ARQ-001
produz_entrada_para: []
relaciona_se_com:
  - CASOS-INDEX
  - CASO-001-PRONTIDAO
  - CASO-001-FONTES
  - CASO-001-GEOMETRIA
  - CASO-001-DADOS-CHUVA
  - GOV-006
  - GOV-007
  - MODELO-INDICADORES-001
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
estado_do_caso: preparacao
territorio: Sub-bacia de Itapeba, Maricá/RJ; polígono oficial pendente
periodo_preliminar: 2022-01-01 a 2026-06-30
tipo_de_caso: demonstrativo
issue_acompanhamento: 2
---

# CASO-001 — Drenagem Urbana e Alerta Preventivo na Sub-bacia de Itapeba

## Estado

**Preparação.** Este documento não contém diagnóstico oficial, recomendação de obra, contratação, avaliação de política ou conclusão sobre o sistema de drenagem de Maricá.

A pesquisa inicial reduziu o escopo para a sub-bacia de Itapeba e definiu o período preliminar de 2022-01-01 a 2026-06-30. A matriz consolidou 15 fontes públicas; os protocolos de chuva e geometria possuem validadores testados com fixtures sintéticos. O polígono oficial, as séries reais, os documentos técnicos, a participação local e a revisão independente continuam pendentes.

O PPC-001 somente poderá começar após nova decisão do portão de prontidão do GOV-008. Consulte o [registro de prontidão](CASO-001_REGISTRO_DE_PRONTIDAO.md), a [matriz de fontes](CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md), o [protocolo geoespacial](CASO-001_PROTOCOLO_DE_GEOMETRIA_E_DELIMITACAO.md) e a issue #2.

## 1. Pergunta decisória preliminar

Como estruturar uma decisão pública auditável para reduzir riscos e impactos de alagamentos na sub-bacia de Itapeba, articulando macrodrenagem, microdrenagem, manutenção, monitoramento e comunicação de risco, sem presumir previamente a combinação adequada de medidas?

A pergunta poderá ser refinada após obtenção do polígono, dos projetos e das séries de dados.

## 2. Justificativa da seleção

O tema foi selecionado para preparação porque:

- integra engenharia civil, gestão pública, sustentabilidade e tecnologia;
- permite comparar manutenção, obras, soluções baseadas na natureza, monitoramento, comunicação e não intervenção;
- possui efeitos potencialmente mensuráveis e distribuídos territorialmente;
- exige articulação entre evidência técnica, capacidade institucional e conhecimento local;
- testa diferentes etapas do ciclo sem depender de uma única solução;
- pode gerar aprendizado reutilizável sobre decisões urbanas sob incerteza.

A sub-bacia de Itapeba foi escolhida como recorte preliminar porque fontes municipais identificam intervenção de macrodrenagem anunciada em 2026, existe estação pluviométrica pública com o nome Itapeba e há registro municipal de acumulado elevado e ocorrências no evento de abril de 2022.

Essas razões justificam preparar o estudo, mas não demonstram que uma intervenção específica seja necessária, suficiente ou eficaz.

## 3. Delimitação atual

| Elemento | Estado atual |
|---|---|
| Município | Maricá/RJ |
| Unidade | sub-bacia de Itapeba |
| Polígono | pendente; camada estadual candidata localizada, feição ainda não obtida |
| Sistema de referência candidato | EPSG:4674 — SIRGAS 2000, conforme serviços do GeoINEA |
| Período | 2022-01-01 a 2026-06-30, sujeito à completude das séries |
| Evento de referência | chuvas de abril de 2022, ainda sem validação completa dos dados brutos |
| População e grupos afetados | pendente do polígono e de dados oficiais |
| Unidades potenciais | Defesa Civil, SOMAR, Urbanismo, Meio Ambiente e SANEMAR nas interfaces pertinentes |
| Responsável pela documentação | Projeto Pragmatismo Cívico |
| Revisores | cadastro ainda sem pessoas elegíveis |

O nome da sub-bacia não será tratado como limite cartográfico suficiente. A camada `GPL_SUBBACIAS_ERJ_50` é fonte candidata, mas sua existência não comprova que haja feição denominada Itapeba ou equivalência com o recorte municipal. O estudo não avançará sem geometria verificável.

## 4. Limites desta versão

Esta versão:

- não afirma que todas as fontes necessárias estejam disponíveis;
- não afirma que uma feição oficial de Itapeba tenha sido obtida;
- não atribui causa a eventos;
- não avalia desempenho de órgão, contrato, sistema ou serviço;
- não estima custos ou benefícios;
- não seleciona tecnologia, fornecedor ou obra;
- não define prioridade territorial fora do recorte preparatório;
- não coleta dados pessoais;
- não substitui planos oficiais de emergência, drenagem, defesa civil, saneamento ou ordenamento territorial;
- não trata comunicação institucional como prova de eficácia;
- não trata fixture sintético como dado ou mapa real.

## 5. Fontes verificadas e fontes pendentes

A [Matriz de Fontes e Lacunas](CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md) registra 15 fontes com identificador, classe, órgão, URL, cobertura, estado de obtenção, formato, licença conhecida, hash, uso, risco e relação com o portão.

Ela inclui:

- Plano de Contingência Municipal 2026;
- contratos anunciados em 2026 para Itapeba;
- registro municipal das chuvas de abril de 2022;
- Programa Municipal de Drenagem;
- Plano Diretor, Lei Complementar nº 400/2025 e anexo de mapas;
- estação pluviométrica Itapeba e interfaces do Cemaden;
- monitoramento hidrometeorológico do INEA e Hidroweb da ANA;
- iniciativa municipal de monitoramento inteligente da drenagem;
- camada estadual poligonal de sub-bacias do GeoINEA;
- base de hidrografia RJ25, na escala 1:25.000.

A matriz diferencia fonte `localizada`, `consultada`, `obtida` e `tratada`. Nenhuma fonte desta versão foi classificada como obtida ou tratada para fins empíricos.

Ainda precisam ser obtidos ou verificados:

- feição oficial da sub-bacia ou evidência documentada de ausência de correspondência nominal;
- produtos técnicos completos do programa de drenagem;
- contrato, projeto, cronograma, geometrias e indicadores das intervenções;
- séries brutas e metadados de estações;
- registros administrativos agregados de ocorrências, manutenção e danos;
- regras e dados de alertas aplicáveis ao recorte;
- fontes de participação e conhecimento local.

Nenhuma lacuna será preenchida por número inventado, digitalização apresentada como oficial ou inferência apresentada como fato.

## 6. Infraestrutura geoespacial

O [protocolo de geometria e delimitação](CASO-001_PROTOCOLO_DE_GEOMETRIA_E_DELIMITACAO.md) registra:

- camada poligonal `GPL_SUBBACIAS_ERJ_50`, ID `4`, do GeoINEA;
- hidrografia do Projeto RJ25, em escala 1:25.000;
- referência espacial EPSG:4674 publicada pelos serviços;
- procedimento de consulta, preservação, hash e revisão;
- hierarquia de evidência cartográfica;
- critérios que impedem converter nome de bairro ou linha de drenagem em polígono oficial;
- validador `scripts/validar_geojson_subbacia.py`;
- fixture sintético e teste de rejeição de geometria inválida.

O status `geodata/pipeline` confirma apenas o funcionamento do validador sobre dados sintéticos.

## 7. Alternativas que o diagnóstico deverá permitir examinar

Sem antecipar recomendação, o caso deverá manter abertas alternativas como:

- não intervenção e manutenção do arranjo atual;
- manutenção preventiva e corretiva;
- revisão de rotinas operacionais;
- intervenções localizadas de microdrenagem;
- intervenções estruturais de maior porte;
- soluções baseadas na natureza e infraestrutura verde;
- monitoramento hidrometeorológico e da rede de drenagem;
- melhoria de alertas e comunicação;
- medidas de ordenamento e controle de ocupação;
- combinação gradual de medidas;
- piloto reversível antes de expansão.

Alternativas inviáveis ou inadequadas só poderão ser eliminadas com justificativa verificável.

## 8. Pessoas e unidades a considerar

A preparação deverá mapear, sem presumir representação:

- moradores, trabalhadores e usuários da sub-bacia;
- pessoas com mobilidade reduzida ou barreiras de comunicação;
- escolas, saúde, assistência e equipamentos públicos;
- transporte e vias críticas;
- trabalhadores de manutenção e operação;
- defesa civil e resposta a emergências;
- planejamento urbano, obras, saneamento e meio ambiente;
- comerciantes, prestadores e organizações locais;
- pesquisadores e profissionais com conhecimento pertinente;
- territórios conectados a montante ou a jusante.

Participação não será usada apenas para confirmar uma proposta previamente escolhida.

## 9. Riscos iniciais

| Risco | Salvaguarda inicial |
|---|---|
| limite da sub-bacia ainda indefinido | obter feição oficial, preservar consulta e documentar método de recorte |
| camada estadual incompatível com o recorte municipal | comparar atributos, conceitos, projetos e fontes municipais |
| dados incompletos ou incompatíveis | registrar cobertura, qualidade, UTC, lacunas e transformações |
| retenção excessiva ou publicação acidental | aplicar política de retenção, quarentena, descarte e revisão periódica |
| foco excessivo em tecnologia | comparar alternativas operacionais, ambientais, estruturais e não intervenção |
| exposição de pessoas afetadas | usar agregação e minimização de dados |
| confusão com plano ou avaliação oficial | declarar natureza demonstrativa e não vinculante |
| captura por fornecedor ou interesse político | conflitos públicos e ausência de marca ou solução pré-selecionada |
| revisão insuficiente | manter caso em preparação até capacidade compatível |
| comunicação institucional tomada como avaliação | exigir documentos, dados e verificação independente |
| urgência usada para pular diagnóstico | separar resposta emergencial de decisão estrutural |

## 10. Portão de prontidão

Situação atual:

- [x] pergunta decisória preliminar revisada;
- [x] responsável pela documentação identificado;
- [x] riscos e conflitos iniciais registrados;
- [x] versões iniciais registradas;
- [x] critérios de suspensão e encerramento definidos;
- [x] matriz de fontes e lacunas consolidada;
- [x] processamento, retenção e descarte de chuva documentados e testados sinteticamente;
- [x] protocolo e validador geoespacial testados sinteticamente;
- [ ] polígono territorial oficial obtido;
- [ ] período confirmado após teste de completude das séries;
- [ ] fontes mínimas obtidas e avaliadas integralmente;
- [ ] plano de dados executado com dados reais e revisão manual;
- [ ] grupos afetados e canais preliminares confirmados;
- [ ] interlocutores institucionais confirmados;
- [ ] estratégia de revisão viável.

**Resultado atual:** permanece em preparação.

## 11. Sequência metodológica prevista

1. GOV-008 — seleção e prontidão;
2. PPC-001 — diagnóstico do problema delimitado;
3. PPC-002 — formulação de alternativas;
4. PPC-003 — avaliação técnica;
5. PPC-004 — decisão demonstrativa e justificativa;
6. Teoria da Mudança;
7. PPC-005 e PPC-006 — plano de implementação e monitoramento, se aplicável;
8. PPC-007 — plano ou avaliação de resultados;
9. PPC-008 — lições sobre o caso e sobre o framework.

O caso pode ser encerrado antes de etapas posteriores quando dados, capacidade, ética ou proporcionalidade não permitirem continuidade.

## 12. Produtos esperados da preparação

- [x] registro de prontidão atualizado;
- [x] matriz de fontes e lacunas;
- [x] processador e protocolo de qualidade das séries de chuva;
- [x] protocolo e validador de geometria;
- [ ] polígono oficial e memória de delimitação aplicada ao arquivo real;
- [ ] teste e revisão da série real;
- [ ] mapa preliminar de partes afetadas;
- [ ] registro de conflitos e interlocutores confirmados;
- [ ] decisão de prontidão, suspensão ou encerramento;
- [ ] plano de trabalho do PPC-001.

## 13. Critério de sucesso desta etapa

A preparação será bem-sucedida quando permitir decidir, com honestidade, se existe capacidade mínima para iniciar o diagnóstico. Avançar de etapa não é, por si só, medida de sucesso.

## 14. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Seleção do primeiro tema demonstrativo e registro dos limites, fontes e portão de prontidão | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Recorte preliminar da sub-bacia de Itapeba, período inicial, fontes verificadas e decisão de manter preparação | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Integração da matriz de fontes, retenção de dados e atualização dos produtos e bloqueios do portão | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-18 | compatível | Inclusão das fontes geoespaciais, protocolo de delimitação, validador e status `geodata/pipeline` | Projeto Pragmatismo Cívico |
