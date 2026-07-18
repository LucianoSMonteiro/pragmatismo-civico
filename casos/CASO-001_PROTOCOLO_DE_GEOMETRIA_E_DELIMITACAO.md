---
id: CASO-001-GEOMETRIA
titulo: Protocolo de Aquisição, Validação e Delimitação Geoespacial do CASO-001
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
compatibilidade: inicial
proxima_revisao: null
issue_acompanhamento: 6
script_associado: scripts/validar_geojson_subbacia.py
estado_da_geometria: fonte_candidata_localizada_geometria_oficial_pendente
---

# CASO-001 — Protocolo de geometria e delimitação

## 1. Estado

Foram localizados serviços geoespaciais oficiais do Instituto Estadual do Ambiente — INEA que podem apoiar a delimitação:

- camada estadual de sub-bacias hidrográficas em geometria poligonal;
- base de trechos de drenagem do Projeto RJ25, em escala 1:25.000.

**Nenhuma feição correspondente à sub-bacia de Itapeba foi ainda obtida, arquivada ou validada como limite oficial do caso.** O portão permanece fechado.

O validador geoespacial foi aprovado somente com fixture sintético. Aprovação do código não comprova existência, oficialidade ou adequação da geometria real.

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

A camada é uma candidata prioritária porque contém polígonos e atributo de nome de sub-bacia. Sua existência não demonstra que haja feição denominada Itapeba nem que a classificação estadual coincida com a sub-bacia usada pelo programa municipal de drenagem.

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

## 3. Hierarquia de evidência cartográfica

A delimitação deve preferir, nesta ordem:

1. feição vetorial oficial com metadados, atributos, sistema de referência e data;
2. exportação vetorial preservada diretamente de geosserviço oficial;
3. mapa oficial georreferenciado com escala e legenda suficientes;
4. derivação analítica reproduzível, claramente identificada como não oficial;
5. croqui ou digitalização manual apenas para exploração, nunca como limite oficial.

Nome de bairro, título de contrato, imagem ilustrativa ou ponto de estação não atende ao requisito territorial.

## 4. Procedimento de aquisição

Para cada tentativa:

1. registrar URL do serviço, camada, item, data e metadados observados;
2. consultar o atributo `sub_bacias` por Itapeba e variações justificadas;
3. preservar a resposta integral, inclusive quando não houver resultado;
4. não ampliar a busca espacial sem referência territorial documentada;
5. exportar em GeoJSON ou formato vetorial equivalente sem editar os bytes originais;
6. registrar parâmetros da consulta, filtro, `outFields`, `returnGeometry` e sistema de referência;
7. calcular SHA-256 do arquivo recebido;
8. manter original em `work/caso-001/geometria/raw/`;
9. executar o validador e preservar manifesto e relatório;
10. revisar manualmente atributos, escala, data, licença, geometria e adequação temática;
11. comparar com o Plano Diretor, programa de drenagem, projetos e rede hidrográfica;
12. emitir memória de delimitação antes de alterar o estado do portão.

Consulta sem resultado deve ser documentada; não autoriza inventar limite ou converter automaticamente o bairro de Itapeba em bacia hidrográfica.

## 5. Estrutura local

```text
work/caso-001/geometria/
├── raw/          # respostas e arquivos recebidos sem alteração
├── processed/    # conversões ou recortes reproduzíveis
├── manifest/     # hashes, parâmetros e proveniência
└── reports/      # validação automática e revisão manual
```

O diretório `work/` permanece ignorado pelo Git. Aplicam-se as regras de retenção, quarentena, descarte e backups do `CASO-001-DADOS-CHUVA` enquanto não existir política geoespacial mais específica.

## 6. Validador

Exemplo de execução após obter o arquivo:

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

## 7. Verificações automáticas

O script verifica:

- JSON e estrutura GeoJSON;
- presença de Feature, Polygon ou MultiPolygon;
- coordenadas numéricas e finitas;
- longitude e latitude em intervalos plausíveis;
- fechamento e número mínimo de vértices dos anéis;
- vértices distintos;
- auto-interseções simples;
- extensão espacial;
- correspondência do nome esperado nos atributos;
- área aproximada para controle de plausibilidade;
- SHA-256, tamanho e proveniência declarada.

Falha estrutural produz código de saída diferente de zero. A área calculada é aproximada e não substitui cálculo geodésico em software SIG.

## 8. Revisão manual obrigatória

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

## 9. Fixture sintético

`tests/fixtures/itapeba_subbacia_sintetica.geojson` contém um polígono inventado para testar:

- leitura de FeatureCollection;
- atributo com nome esperado;
- anel fechado;
- envelope espacial;
- hash e manifesto;
- geração de relatório;
- rejeição de anel aberto.

O fixture não representa Itapeba, Maricá, uma bacia ou qualquer limite real. Ele não pode ser publicado como mapa nem citado como evidência.

## 10. Critério de conclusão da issue #6

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

**Estado atual:** infraestrutura pronta; geometria oficial pendente.

## 11. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Registro dos geosserviços candidatos, procedimento de aquisição, validação e critérios de conclusão | Projeto Pragmatismo Cívico |
