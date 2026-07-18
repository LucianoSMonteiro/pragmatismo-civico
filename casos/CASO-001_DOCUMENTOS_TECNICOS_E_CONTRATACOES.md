---
id: CASO-001-DOCUMENTOS-TECNICOS
titulo: Registro de Documentos Técnicos, Financiamentos e Contratações do CASO-001
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
  - CASO-001-FONTES
  - GOV-008
  - PPC-META-001
  - ARQ-001
produz_entrada_para: []
relaciona_se_com:
  - CASOS-INDEX
  - CASO-001-GEOMETRIA
  - CASO-001-DADOS-CHUVA
  - PPC-001
  - MODELO-INDICADORES-001
substitui: []
substituido_por: null
compatibilidade: inicial
proxima_revisao: null
issue_acompanhamento: 7
registro_estruturado: casos/CASO-001_REGISTRO_DOCUMENTOS_TECNICOS.json
estado_dos_documentos: inventario_validado_documentos_integrais_pendentes
---

# CASO-001 — Documentos técnicos, financiamentos e contratações

## 1. Estado

Foram consolidadas oito fontes oficiais ou institucionais relacionadas ao Programa Municipal de Drenagem, às operações do Novo PAC, à contratação Smart Drainage e a uma intervenção histórica em Itapeba.

**Nenhum programa final, contrato de financiamento integral, carta-consulta, projeto, anteprojeto, geometria, cronograma físico-financeiro, medição ou as-built foi obtido e preservado com hash.** O portão permanece fechado.

O registro estruturado `CASO-001_REGISTRO_DOCUMENTOS_TECNICOS.json` contém 20 alegações identificadas, três inconsistências e sete grupos documentais pendentes. A validação automática impede promover comunicação institucional a evidência financeira ou contratual primária e exige arquivo local e SHA-256 para qualquer fonte marcada como `obtida` ou `tratada`.

## 2. Regra de separação das evidências

| Classe | O que pode demonstrar | O que não demonstra sozinha |
|---|---|---|
| comunicação institucional | existência de anúncio, audiência, intenção, assinatura divulgada ou narrativa do órgão | conteúdo integral do contrato, projeto, execução, medição, resultado ou eficácia |
| registro do agente financeiro | estrutura geral do financiamento, valores agregados e objetos divulgados | números e cláusulas de cada contrato, cronograma, contrapartida executada ou conformidade da obra |
| regra de seleção | documentos que normalmente devem acompanhar uma proposta | quais documentos Maricá efetivamente entregou e qual versão foi aprovada |
| índice de contratação | procedimento, processo, objeto, situação e valor estimado publicados | contrato celebrado, preço adjudicado, pagamento, implantação ou relação com outra operação |
| registro histórico | existência de intervenção anterior e contexto territorial | equivalência com os projetos de 2024–2026 ou estado atual da infraestrutura |

Notícia, fotografia de cerimônia, valor anunciado ou nome de bairro não será tratado como contrato, projeto, polígono, medição ou resultado.

## 3. Fontes consolidadas

| ID | Fonte | Classe | Estado | Uso principal |
|---|---|---|---|---|
| `DT-001` | audiência sobre o prognóstico, 25/10/2023 | comunicação institucional | consultada | confirmar que houve apresentação de prognóstico e propostas |
| `DT-002` | última audiência, 07/11/2023 | comunicação institucional | consultada | registrar promessa de documento compilado e metas temporais |
| `DT-003` | anúncio municipal do PAC Seleções, 26/07/2024 | comunicação institucional | consultada | identificar três projetos da SOMAR e recursos FGTS agregados |
| `DT-004` | anúncio da CAIXA, 06/01/2026 | registro financeiro institucional | consultada | distinguir investimento total, FGTS, intervenções e beneficiários divulgados |
| `DT-005` | anúncio municipal da assinatura, 06/01/2026 | comunicação institucional | consultada | registrar descrição municipal do escopo e valores aproximados |
| `DT-006` | requisitos federais para drenagem urbana | orientação de seleção | consultada | definir anexos técnicos que devem ser procurados |
| `DT-007` | Pregão Eletrônico 14/2026 — Smart Drainage | índice de contratação | consultada | separar contratação tecnológica das obras do Novo PAC |
| `DT-008` | obra do João Português, 2020 | registro histórico | consultada | impedir confusão entre intervenção anterior e projetos atuais |

Nenhuma dessas fontes está classificada como `obtida` ou `tratada` para fins empíricos.

## 4. Programa Municipal de Drenagem

A Prefeitura e a SOMAR informaram em outubro de 2023 que uma consultoria contratada apresentou prognóstico com propostas para o plano de ações. Entre as alternativas divulgadas estavam detenção e amortecimento a montante, recuperação de lagoas e orlas, valorização de canais naturais e diretrizes de ocupação.

Na audiência final de novembro de 2023, foi informado que seria compilado documento com as propostas e parecer técnico da SOMAR e da SANEMAR, contendo metas de curto, médio e longo prazo.

Ainda faltam:

- identificação da consultoria e do processo de contratação;
- contrato e ordens de serviço;
- plano de trabalho e produtos intermediários;
- diagnóstico e bases utilizadas;
- prognóstico integral;
- plano de ações e critérios de priorização;
- mapas, modelos, cenários e geometrias;
- documento compilado e parecer técnico;
- versão final aprovada e histórico de revisões.

A inexistência desses arquivos no inventário atual não significa que não existam. Significa apenas que não foram localizados, obtidos e preservados nesta etapa.

## 5. Operações do Novo PAC

### 5.1 Estrutura financeira divulgada

A CAIXA informou três termos de compromisso com cinco operações de financiamento para mobilidade, esgotamento e drenagem em Maricá.

Para as três intervenções de drenagem, a CAIXA divulgou:

- investimento total de **R$ 123,1 milhões**;
- **R$ 117 milhões** em recursos do FGTS;
- obras em Itaipuaçu, Itapeba e Jardim Atlântico;
- galerias, redes, pavimentação e intervenção em canal no Jardim Atlântico;
- aproximadamente **19.500 pessoas** beneficiadas.

A diferença entre R$ 123,1 milhões de investimento e R$ 117 milhões de FGTS é compatível, em princípio, com contrapartida ou recursos não financiados. Essa explicação é provisória até a leitura dos instrumentos integrais.

O anúncio municipal de 2024 também registra R$ 117 milhões para três projetos da SOMAR, identificados como Barroco, Jardim Atlântico Oeste e Itapeba.

### 5.2 O que ainda não foi individualizado

As fontes públicas consultadas não permitem determinar:

- número de cada proposta, operação, termo e contrato;
- valor de investimento e financiamento específico de Itapeba;
- contrapartida municipal por operação;
- agente executor e responsáveis técnicos de cada intervenção;
- perímetro, ruas, canais e população diretamente atendida em cada território;
- cronograma de projeto, licitação, obra e desembolso;
- metas físicas e indicadores;
- condicionantes ambientais, fundiárias ou de reassentamento;
- situação da análise técnica e liberação de recursos;
- relação entre as operações financeiras e futuros procedimentos licitatórios.

## 6. Inconsistências abertas

### 6.1 Beneficiários

A CAIXA informa aproximadamente **19.500 pessoas** beneficiadas pelas três intervenções de drenagem. A Prefeitura informa **mais de 300 mil beneficiários diretos**.

A diferença é material e não será resolvida por escolha arbitrária. Devem ser obtidos:

- memória de cálculo;
- definição de beneficiário direto e indireto;
- população de referência;
- território considerado;
- data e fonte demográfica;
- eventual distinção entre população municipal, população das bacias e população protegida.

Até a reconciliação, os dois números permanecem como alegações atribuídas às respectivas fontes.

### 6.2 Nomes territoriais

As fontes usam combinações diferentes:

- Barroco;
- Jardim Atlântico Oeste;
- Jardim Atlântico;
- Itaipuaçu;
- Itapeba.

É necessário confirmar se Barroco e Jardim Atlântico Oeste são intervenções distintas, subáreas de Itaipuaçu ou nomenclaturas resumidas do mesmo objeto. A mesma cautela vale para “Itapeba” como bairro, sub-bacia, sistema de drenagem ou área de projeto.

### 6.3 Total de investimento e recurso financiado

O total municipal divulgado para mobilidade, saneamento e drenagem é aproximadamente R$ 267 milhões. A CAIXA informa R$ 254,4 milhões em recursos do FGTS. Os valores são reconciliáveis quando se distingue investimento total de financiamento, mas os contratos devem confirmar:

- valor de investimento;
- valor financiado;
- contrapartida;
- encargos e condições;
- valores por operação.

## 7. Smart Drainage não é automaticamente a obra do PAC

O Portal da Transparência registra o Pregão Eletrônico `14/2026`, processo `25402/2025`, para registro de preços de solução integrada de inteligência e gestão de microdrenagem urbana.

Na data da consulta, o portal informava:

- situação: `Em andamento`;
- valor estimado: **R$ 92.038.805,89**;
- objeto com hardware IoT como serviço, licenciamento de software e serviços de engenharia sanitária.

Esse registro não demonstra:

- contrato celebrado;
- valor adjudicado ou executado;
- implantação concluída;
- cobertura em Itapeba;
- vinculação aos R$ 117 milhões do Novo PAC;
- substituição de obras de macro ou microdrenagem;
- eficácia do sistema.

A contratação tecnológica deve permanecer separada das três operações de obras até que documentos oficiais estabeleçam relação entre elas.

## 8. Documentos que devem existir ou ser solicitados

Os requisitos federais atuais para propostas de drenagem indicam a necessidade de projeto ou anteprojeto, composição do investimento, comprovação e delimitação de áreas de risco, pontos de intervenção e relatório fotográfico. Isso orienta a busca, mas não prova o conteúdo da proposta de Maricá de 2024.

| ID | Documento requerido | Estado |
|---|---|---|
| `REQ-001` | Programa Municipal de Drenagem — versão final e produtos intermediários | pendente |
| `REQ-002` | contrato da consultoria e ordens de serviço | pendente |
| `REQ-003` | cartas-consulta e anexos das três operações do Novo PAC | pendente |
| `REQ-004` | termos de compromisso e contratos de financiamento individualizados | pendente |
| `REQ-005` | projetos ou anteprojetos, QCI, mapas de risco, geometrias e fotografias | pendente |
| `REQ-006` | edital, termo de referência e anexos do Pregão 14/2026 | pendente |
| `REQ-007` | cronogramas, medições, indicadores e relatórios de execução | pendente |

## 9. Protocolo de obtenção

Para cada documento:

1. registrar órgão, sistema, URL, processo, procedimento, operação e data;
2. preservar os bytes originais sem edição;
3. calcular SHA-256;
4. registrar nome, tamanho, tipo MIME e data de acesso;
5. verificar assinatura, versão, anexos e integridade;
6. distinguir minuta, edital, contrato, aditivo, projeto, medição e relatório;
7. registrar restrições de licença, sigilo e dados pessoais;
8. extrair fatos em registro separado sem alterar o original;
9. reconciliar valores, territórios, unidades e períodos;
10. submeter projeto e geometria a revisão técnica proporcional;
11. atualizar o portão somente após avaliar suficiência e qualidade.

Fontes locais ainda não publicáveis devem permanecer em `work/caso-001/documentos-tecnicos/`, ignorado pelo Git.

## 10. Validação automática

Execute:

```bash
python scripts/validar_registro_documentos_tecnicos.py \
  --registry casos/CASO-001_REGISTRO_DOCUMENTOS_TECNICOS.json \
  --report work/caso-001/documentos-tecnicos/validacao-registro.md
```

O validador verifica:

- versão do esquema e identificadores únicos;
- tipos de fonte, níveis de evidência e estados;
- datas e URLs HTTPS;
- alegações com escopo, valor e unidade;
- referências das inconsistências;
- documentos requeridos;
- proibição de classificar notícia como evidência financeira primária;
- exigência de caminho e SHA-256 para fonte obtida ou tratada.

A validação estrutural não comprova autenticidade, completude, mérito técnico ou execução contratual.

## 11. Critério de conclusão da issue #7

A issue somente poderá ser encerrada quando:

- [ ] o programa final e seus produtos forem obtidos e preservados;
- [ ] a consultoria e sua contratação forem identificadas;
- [ ] as três operações de drenagem forem individualizadas;
- [ ] termos e contratos de financiamento forem preservados;
- [ ] projetos, geometrias, riscos e QCI forem obtidos;
- [ ] valores e beneficiários forem reconciliados;
- [ ] o Pregão 14/2026 for documentado sem confusão com as obras;
- [ ] cronogramas, medições e indicadores estiverem disponíveis ou sua ausência formalmente registrada;
- [ ] a revisão técnica avaliar adequação e suficiência;
- [ ] o registro de prontidão e a issue #2 forem atualizados.

**Estado atual:** inventário e controles prontos; documentos integrais e evidência de execução pendentes.

## 12. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Consolidação de fontes técnicas e financeiras, inconsistências, registro estruturado, protocolo de obtenção e critérios de conclusão | Projeto Pragmatismo Cívico |
