---
id: CASO-001
titulo: Preparação do Estudo Demonstrativo sobre Drenagem Urbana e Alerta Preventivo na Sub-bacia de Itapeba
versao: 0.5.0
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
  - CASO-001-DOCUMENTOS-TECNICOS
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

A pesquisa reduziu o escopo para a sub-bacia de Itapeba e definiu o período preliminar de 2022-01-01 a 2026-06-30. A matriz consolidou 15 fontes públicas. O registro técnico estrutura 8 fontes oficiais ou institucionais, 20 alegações, 3 inconsistências e 7 grupos documentais pendentes.

Nenhum programa final, contrato integral, projeto, medição, feição oficial ou série real foi incorporado. O PPC-001 somente poderá começar após nova decisão do portão de prontidão do GOV-008.

Consulte o [registro de prontidão](CASO-001_REGISTRO_DE_PRONTIDAO.md), a [matriz de fontes](CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md), os [documentos técnicos e contratações](CASO-001_DOCUMENTOS_TECNICOS_E_CONTRATACOES.md), o [protocolo geoespacial](CASO-001_PROTOCOLO_DE_GEOMETRIA_E_DELIMITACAO.md) e a issue #2.

## 1. Pergunta decisória preliminar

Como estruturar uma decisão pública auditável para reduzir riscos e impactos de alagamentos na sub-bacia de Itapeba, articulando macrodrenagem, microdrenagem, manutenção, monitoramento e comunicação de risco, sem presumir previamente a combinação adequada de medidas?

A pergunta poderá ser refinada após obtenção do polígono, dos projetos e das séries de dados.

## 2. Justificativa da seleção

O tema foi selecionado porque integra engenharia civil, gestão pública, sustentabilidade e tecnologia; permite comparar medidas operacionais, estruturais, ambientais e informacionais; exige articulação entre evidência, capacidade institucional e conhecimento local; e pode produzir aprendizado reutilizável sobre decisões sob incerteza.

A sub-bacia de Itapeba foi escolhida como recorte preliminar porque fontes municipais identificam intervenção de drenagem anunciada, existe estação pluviométrica pública denominada Itapeba e há registro municipal de acumulado elevado e ocorrências em abril de 2022.

Essas razões justificam preparar o estudo, mas não demonstram que uma intervenção específica seja necessária, suficiente ou eficaz.

## 3. Delimitação atual

| Elemento | Estado atual |
|---|---|
| Município | Maricá/RJ |
| Unidade | sub-bacia de Itapeba |
| Polígono | pendente; fonte estadual candidata localizada, resposta oficial ainda não obtida |
| Sistema de referência candidato | EPSG:4674 — SIRGAS 2000 |
| Período | 2022-01-01 a 2026-06-30, sujeito à completude das séries |
| Evento de referência | chuvas de abril de 2022, sem validação completa dos dados brutos |
| População e grupos afetados | pendentes do polígono e de dados oficiais |
| Responsável pela documentação | Projeto Pragmatismo Cívico |
| Revisores | cadastro ainda sem pessoas elegíveis |

O nome da sub-bacia não será tratado como limite cartográfico suficiente. A camada `GPL_SUBBACIAS_ERJ_50` é fonte candidata, mas nenhuma resposta da API foi recebida nas tentativas hospedadas.

## 4. Fontes e documentos técnicos

A [Matriz de Fontes e Lacunas](CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md) registra 15 fontes gerais. O [Registro de Documentos Técnicos, Financiamentos e Contratações](CASO-001_DOCUMENTOS_TECNICOS_E_CONTRATACOES.md) separa:

- comunicação institucional;
- registro do agente financeiro;
- orientação procedimental de seleção;
- índice de contratação;
- registro histórico;
- documentos integrais ainda requeridos.

Nenhuma fonte está classificada como obtida ou tratada para fins empíricos.

## 5. Achados financeiros e contratuais preliminares

As fontes consultadas indicam três intervenções de drenagem relacionadas ao Novo PAC em territórios descritos como Itaipuaçu, Itapeba e Jardim Atlântico, com R$ 117 milhões de recursos do FGTS e investimento total agregado de aproximadamente R$ 123,1 milhões.

Esses valores são agregados. Ainda faltam números individuais de proposta, operação, termo e contrato, valores por território, contrapartidas, cronogramas, metas físicas e condições de desembolso.

O Pregão Eletrônico 14/2026 — Smart Drainage possui objeto tecnológico e valor estimado próprios. Não foi demonstrada vinculação financeira ou contratual com as três operações de drenagem do Novo PAC. Registro de preços, valor estimado e certame em andamento não equivalem a contrato, despesa executada ou implantação.

## 6. Inconsistências abertas

| Tema | Alegações em conflito | Tratamento atual |
|---|---|---|
| beneficiários | aproximadamente 19.500 pessoas na fonte da CAIXA versus mais de 300 mil na comunicação municipal | manter ambos atribuídos; obter memória de cálculo e definições |
| nomes territoriais | Barroco, Jardim Atlântico Oeste, Jardim Atlântico, Itaipuaçu e Itapeba | individualizar objetos nos contratos e projetos |
| investimento e financiamento | aproximadamente R$ 123,1 milhões de investimento versus R$ 117 milhões de FGTS | explicação provisória por contrapartida; confirmar nos instrumentos |

Nenhuma inconsistência será resolvida escolhendo arbitrariamente o número ou nome mais conveniente.

## 7. Documentos requeridos

| ID | Grupo documental | Estado |
|---|---|---|
| `REQ-001` | Programa Municipal de Drenagem — versão final e produtos intermediários | pendente |
| `REQ-002` | contratação da consultoria e ordens de serviço | pendente |
| `REQ-003` | cartas-consulta e anexos das três operações do Novo PAC | pendente |
| `REQ-004` | termos de compromisso e contratos de financiamento individualizados | pendente |
| `REQ-005` | projetos ou anteprojetos, QCI, mapas de risco, geometrias e fotografias | pendente |
| `REQ-006` | edital, termo de referência e anexos do Pregão 14/2026 | pendente |
| `REQ-007` | cronogramas, medições, indicadores e relatórios de execução | pendente |

## 8. Limites desta versão

Esta versão:

- não afirma que todas as fontes estejam disponíveis;
- não afirma que uma feição oficial de Itapeba tenha sido obtida;
- não trata notícia como contrato ou projeto;
- não trata financiamento como obra executada;
- não trata registro de preços como contratação concluída;
- não atribui causa a eventos;
- não avalia desempenho de órgão, contrato, sistema ou serviço;
- não estima custos ou benefícios além de reproduzir valores atribuídos às fontes;
- não seleciona tecnologia, fornecedor ou obra;
- não coleta dados pessoais;
- não substitui planos oficiais;
- não trata fixture sintético como dado real.

## 9. Alternativas que o diagnóstico deverá permitir examinar

Sem antecipar recomendação, o caso deverá manter abertas não intervenção, manutenção, revisão operacional, microdrenagem, intervenções estruturais, soluções baseadas na natureza, monitoramento, alertas, medidas de ordenamento, combinações graduais e pilotos reversíveis.

Alternativas só poderão ser eliminadas com justificativa verificável.

## 10. Pessoas e unidades a considerar

A preparação deverá mapear, sem presumir representação, moradores, trabalhadores, pessoas com barreiras de mobilidade ou comunicação, escolas, saúde, assistência, transporte, comércio, equipes operacionais, organizações locais, pesquisadores e territórios conectados a montante ou jusante.

Participação não será usada apenas para confirmar proposta previamente escolhida.

## 11. Riscos e salvaguardas

| Risco | Salvaguarda |
|---|---|
| limite territorial indefinido | obter feição oficial e memória de delimitação |
| comunicação tomada como contrato | classes de evidência e validação automática |
| financiamento confundido com execução | exigir contratos, projetos, cronogramas e medições |
| Smart Drainage confundido com obras do PAC | manter objetos separados até vínculo documental |
| números conflitantes | preservar atribuição e exigir memória de cálculo |
| dados incompletos | registrar cobertura, qualidade, lacunas e transformações |
| foco excessivo em tecnologia | comparar alternativas operacionais, ambientais e estruturais |
| captura por fornecedor ou interesse | conflitos públicos e ausência de solução pré-selecionada |
| revisão insuficiente | manter o caso em preparação |

## 12. Portão de prontidão

- [x] pergunta decisória preliminar revisada;
- [x] responsável pela documentação identificado;
- [x] riscos, conflitos e critérios de suspensão registrados;
- [x] matriz de fontes consolidada;
- [x] registro técnico estruturado e validado;
- [x] protocolos pluviométrico e geoespacial testados com fixtures;
- [ ] polígono territorial oficial obtido;
- [ ] programa final e contratos integrais obtidos;
- [ ] projetos, geometrias, cronogramas e medições obtidos;
- [ ] período confirmado após completude das séries;
- [ ] plano de dados executado com dados reais;
- [ ] grupos afetados e canais confirmados;
- [ ] interlocutores institucionais confirmados;
- [ ] estratégia de revisão viável.

**Resultado atual:** permanece em preparação.

## 13. Sequência metodológica prevista

1. GOV-008 — seleção e prontidão;
2. PPC-001 — diagnóstico, apenas se o portão for aprovado;
3. PPC-002 a PPC-004 — alternativas, avaliação e decisão;
4. Teoria da Mudança;
5. PPC-005 a PPC-008 — implementação, monitoramento, avaliação e aprendizagem, quando proporcionais.

O caso pode ser suspenso ou encerrado antes do diagnóstico quando dados, capacidade, ética ou proporcionalidade não permitirem continuidade.

## 14. Produtos esperados da preparação

- [x] registro de prontidão;
- [x] matriz de fontes;
- [x] registro estruturado de documentos técnicos;
- [x] processador e protocolo pluviométrico;
- [x] coletor e protocolo geoespacial;
- [ ] programa, contratos e projetos integrais;
- [ ] polígono oficial e memória de delimitação;
- [ ] série real revisada;
- [ ] mapa preliminar de partes afetadas;
- [ ] interlocutores e conflitos confirmados;
- [ ] decisão do portão;
- [ ] plano de trabalho do PPC-001.

## 15. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Seleção do primeiro tema demonstrativo e registro dos limites, fontes e portão | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Recorte de Itapeba, período e fontes verificadas | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-18 | compatível | Matriz de fontes e protocolo pluviométrico | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-18 | compatível | Fontes geoespaciais, protocolo e validador | Projeto Pragmatismo Cívico |
| 0.5.0 | 2026-07-18 | compatível | Registro técnico, financiamento, contratações, inconsistências e documentos requeridos | Projeto Pragmatismo Cívico |
