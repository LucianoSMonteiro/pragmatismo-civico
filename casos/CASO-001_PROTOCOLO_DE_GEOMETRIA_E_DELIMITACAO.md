---
id: CASO-001-GEOMETRIA
titulo: Protocolo de Aquisição, Validação e Delimitação Geoespacial do CASO-001
versao: 0.2.0
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
  - ARQ-003
  - PPC-META-001
  - ARQ-001
produz_entrada_para: []
relaciona_se_com:
  - CASOS-INDEX
  - CASO-001-DADOS-CHUVA
  - PPC-001
  - MODELO-INDICADORES-001
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
issue_acompanhamento: 6
scripts_associados:
  - scripts/coletar_geoinea_subbacia.py
  - scripts/coletar_geoinea_subbacia_ipv4.py
  - scripts/geoinea_ipv4_transport.py
  - scripts/validar_geojson_subbacia.py
estado_da_geometria: fonte_localizada_consulta_hospedada_bloqueada_geometria_oficial_pendente
---

# CASO-001 — Protocolo de geometria e delimitação

## 1. Estado

Foram localizados serviços geoespaciais oficiais do Instituto Estadual do Ambiente — INEA que podem apoiar a delimitação:

- camada estadual de sub-bacias hidrográficas em geometria poligonal;
- base de trechos de drenagem do Projeto RJ25, em escala 1:25.000.

**Nenhuma feição correspondente à sub-bacia de Itapeba foi obtida, arquivada ou validada como limite oficial do caso.** O portão permanece fechado.

O validador, o coletor e o transporte IPv4 foram aprovados com respostas sintéticas controladas. Aprovação do código não comprova existência, oficialidade, disponibilidade ou adequação da geometria real.

## 2. Fontes geoespaciais candidatas

### 2.1 Camada de sub-bacias do GeoINEA

| Campo | Registro |
|---|---|
| órgão | Instituto Estadual do Ambiente — INEA |
| serviço | `Recursos_Hidricos_Gestao_Costeira/MapServer` |
| camada | `GPL_SUBBACIAS_ERJ_50`, ID `4` |
| tipo | Feature Layer poligonal |
| campo de exibição | `sub_bacias` |
| outros campos observados | `objectid`, `rh`, área e comprimento calculados |
| referência espacial publicada | EPSG:4674 — SIRGAS 2000 |
| formatos de consulta | JSON, GeoJSON e PBF |
| item do serviço | `e20f5ed7320d45e7a2d0fa2f0e84cf54` |
| URL | <https://geoportal.inea.rj.gov.br/server/rest/services/Recursos_Hidricos_Gestao_Costeira/MapServer/4> |

A camada é candidata prioritária porque contém polígonos e atributo de nome de sub-bacia. Sua existência não demonstra que haja feição denominada Itapeba nem que a classificação estadual coincida com a sub-bacia usada pelo programa municipal de drenagem.

### 2.2 Hidrografia do Projeto RJ25

| Campo | Registro |
|---|---|
| órgãos | IBGE e Governo do Estado do Rio de Janeiro / SEA-RJ |
| serviço | `GLN_HIDROGRAFIA_SEM_CANAL_25K/MapServer` |
| camada | trechos de drenagem, ID `0` |
| escala declarada | 1:25.000 |
| referência espacial publicada | EPSG:4674 — SIRGAS 2000 |
| formatos de consulta | JSON, GeoJSON e PBF |
| item do serviço | `3cfe5a77b64c480ea3de9a062f766599` |
| URL | <https://geoportal.inea.rj.gov.br/server/rest/services/GLN_HIDROGRAFIA_SEM_CANAL_25K/MapServer/0> |

Trechos de drenagem servem para conferência topológica e contexto hidrográfico. Linhas de rios e canais **não definem por si mesmas o divisor ou o polígono de uma sub-bacia**.

## 3. Tentativas reais de consulta

Em 18 de julho de 2026 foram executadas duas séries independentes de consulta a partir de runners hospedados do GitHub Actions.

| Série | Transporte | Tentativas | Resultado | Execução | Artefato de validação |
|---|---|---:|---|---:|---|
| A | biblioteca HTTP padrão do Python | 3 | tempo esgotado ao solicitar os metadados da camada | `29658467155` | SHA-256 `4d2d2b2c450f1967cbf4ec8113de39d146bad01e408d3bdb4b4f8e4741e87bbe` |
| B | `curl --ipv4` | 3 | conexão com `geoportal.inea.rj.gov.br:443` não estabelecida em 30 segundos | `29658776194` | SHA-256 `7be511784a29ec17b4ef26b02778e2fd8f97d82e89cdef1a4304cd5147718914` |

As duas séries falharam **antes do recebimento dos metadados da camada**. Consequentemente:

- nenhum byte da fonte oficial foi recebido;
- nenhum hash de resposta do GeoINEA pôde ser calculado;
- nenhum identificador ou atributo foi consultado;
- não houve resultado nominal vazio;
- não é possível afirmar presença ou ausência de uma feição denominada Itapeba;
- a limitação observada é de conectividade entre os runners hospedados e o servidor, não uma conclusão cartográfica.

Os relatórios preservados registram as falhas e os parâmetros das tentativas. A coleta deve ser repetida em rede que alcance o serviço.

## 4. Hierarquia de evidência cartográfica

A delimitação deve preferir, nesta ordem:

1. feição vetorial oficial com metadados, atributos, sistema de referência e data;
2. exportação vetorial preservada diretamente de geosserviço oficial;
3. mapa oficial georreferenciado com escala e legenda suficientes;
4. derivação analítica reproduzível, claramente identificada como não oficial;
5. croqui ou digitalização manual apenas para exploração, nunca como limite oficial.

Nome de bairro, título de contrato, imagem ilustrativa ou ponto de estação não atende ao requisito territorial.

## 5. Procedimento de aquisição

Para cada tentativa:

1. registrar URL do serviço, camada, item, data e metadados observados;
2. consultar o atributo `sub_bacias` por Itapeba e variações justificadas;
3. preservar a resposta integral, inclusive quando não houver resultado;
4. distinguir falha de conexão, erro do serviço e consulta concluída sem feição;
5. não ampliar a busca espacial sem referência territorial documentada;
6. exportar em GeoJSON ou formato vetorial equivalente sem editar os bytes originais;
7. registrar parâmetros da consulta, filtro, `outFields`, `returnGeometry` e sistema de referência;
8. calcular SHA-256 do arquivo recebido;
9. manter original em `work/caso-001/geometria/raw/`;
10. executar o validador e preservar manifesto e relatório;
11. revisar manualmente atributos, escala, data, licença, geometria e adequação temática;
12. comparar com o Plano Diretor, programa de drenagem, projetos e rede hidrográfica;
13. emitir memória de delimitação antes de alterar o estado do portão.

Consulta concluída sem resultado deve ser documentada. Falha de conexão não deve ser registrada como consulta sem resultado. Nenhuma das duas situações autoriza inventar limite ou converter automaticamente o bairro de Itapeba em bacia hidrográfica.

## 6. Coletor auditável

O coletor consulta, em ordem:

1. metadados da camada;
2. conjunto de `objectIds`;
3. atributos `objectid`, `sub_bacias` e `rh` em lotes;
4. correspondências nominais normalizadas localmente;
5. GeoJSON somente quando houver correspondência.

Ele preserva respostas brutas, URLs efetivas, códigos HTTP, tipos de conteúdo, tamanhos, hashes, atributos combinados, correspondências, manifesto e relatório.

### Execução local padrão

```bash
python scripts/coletar_geoinea_subbacia.py \
  --output-dir work/caso-001/geometria/raw/consulta-geoinea \
  --search-term Itapeba \
  --timeout 60
```

### Execução local forçando IPv4

```bash
python scripts/coletar_geoinea_subbacia_ipv4.py \
  --output-dir work/caso-001/geometria/raw/consulta-geoinea-ipv4 \
  --search-term Itapeba \
  --timeout 60
```

O workflow `.github/workflows/coletar-geoinea.yml` oferece execução manual e preservação de artefato quando o ambiente conectado consegue alcançar o serviço.

## 7. Estrutura local

```text
work/caso-001/geometria/
├── raw/          # respostas e arquivos recebidos sem alteração
├── processed/    # conversões ou recortes reproduzíveis
├── manifest/     # hashes, parâmetros e proveniência
└── reports/      # validação automática e revisão manual
```

O diretório `work/` permanece ignorado pelo Git. Aplicam-se as regras de retenção, quarentena, descarte e backups do `CASO-001-DADOS-CHUVA` enquanto não existir política geoespacial mais específica.

## 8. Validador

Exemplo após obter uma geometria:

```bash
python scripts/validar_geojson_subbacia.py \
  --input work/caso-001/geometria/raw/itapeba.geojson \
  --manifest work/caso-001/geometria/manifest/manifest.json \
  --report work/caso-001/geometria/reports/validacao.md \
  --source-url "URL_EXATA_DA_CONSULTA" \
  --accessed-at 2026-07-18 \
  --source-srid EPSG:4674 \
  --expected-name Itapeba
```

O envelope esperado somente deve ser informado quando houver limite municipal ou regional obtido de fonte confiável. Não deve ser criado apenas para fazer o teste passar.

## 9. Verificações automáticas

A suíte `geodata/pipeline` verifica:

- normalização e seleção nominal de atributos;
- coleta em lotes e preservação de respostas;
- resultado válido sem correspondência nominal;
- transporte IPv4 e separação entre corpo e metadados HTTP;
- rejeição de falha de conexão e status não exitoso;
- JSON e estrutura GeoJSON;
- presença de Feature, Polygon ou MultiPolygon;
- coordenadas numéricas e finitas;
- longitude e latitude em intervalos plausíveis;
- fechamento, vértices distintos e auto-interseções simples;
- extensão espacial, nome esperado e área aproximada;
- SHA-256, tamanho e proveniência declarada.

Falha estrutural produz código de saída diferente de zero. A área calculada é aproximada e não substitui cálculo geodésico em software SIG.

## 10. Revisão manual obrigatória

Antes de usar uma geometria no portão:

- confirmar órgão produtor e cadeia de custódia;
- verificar metadados, data, escala, precisão e sistema de referência;
- confirmar licença, restrições e possibilidade de publicação;
- identificar o significado institucional de “sub-bacia” na fonte;
- verificar se a feição realmente corresponde a Itapeba;
- comparar com drenagem, relevo, lagoas, canais e projetos municipais;
- verificar a posição da estação Cemaden sem presumir representatividade;
- registrar sobreposições com população, serviços, ocorrências e intervenções;
- revisar transformações, recortes e reprojeções;
- obter revisão técnica independente proporcional.

## 11. Fixtures sintéticos

Os testes utilizam respostas ArcGIS e um polígono inventado para verificar coleta, correspondência, GeoJSON, hash, relatório e rejeição de anel aberto.

Os fixtures não representam Itapeba, Maricá, uma bacia ou qualquer limite real. Não podem ser publicados como mapa nem citados como evidência.

## 12. Critério de conclusão da issue #6

A issue somente poderá ser encerrada quando:

- [ ] a feição oficial tiver sido obtida e preservada;
- [ ] a consulta e a origem forem reproduzíveis;
- [ ] o arquivo possuir hash;
- [ ] sistema de referência, data, escala e atributos forem registrados;
- [ ] o validador automático for aprovado com o arquivo real;
- [ ] a revisão manual confirmar adequação temática;
- [ ] divergências com fontes municipais forem explicadas;
- [ ] a memória de delimitação for publicada;
- [ ] o registro de prontidão e a issue #2 forem atualizados.

**Estado atual:** coletor e validação prontos; conectividade dos runners hospedados bloqueada; geometria oficial pendente.

## 13. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Registro dos geosserviços candidatos, procedimento de aquisição, validação e critérios de conclusão | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Coletor auditável, transporte IPv4, tentativas reais de consulta, evidência de falha de conectividade e ampliação da suíte geoespacial | Projeto Pragmatismo Cívico |
