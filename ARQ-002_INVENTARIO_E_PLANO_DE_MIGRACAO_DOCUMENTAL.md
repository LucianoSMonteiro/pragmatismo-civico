---
id: ARQ-002
titulo: Inventário e Plano de Migração Documental
versao: 0.15.1
status: rascunho
tipo: arquitetura
idioma: pt-BR
data_criacao: 2026-07-17
data_versao: 2026-07-18
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - ARQ-001
  - PPC-000
  - PPC-000A
  - PPC-META-001
produz_entrada_para:
  - CATALOGO-DOCUMENTAL
  - VALIDACAO-AUTOMATICA-DE-METADADOS
relaciona_se_com:
  - GOV-002
  - MKDOCS
  - PORTAL-INICIO
  - GUIA-COMECAR
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# ARQ-002 — Inventário e Plano de Migração Documental

## Status

Rascunho ativo. As Fases 0 a 5 estão concluídas: os documentos públicos possuem metadados, o catálogo documental está publicado e a navegação canônica contém 39 documentos. A Fase 6 de validação automática foi iniciada e já verifica também a correspondência entre o catálogo gerado e o publicado.

## 1. Objetivo

Transformar a arquitetura do ARQ-001 em um processo verificável de inventário, catálogo, validação e evolução documental, sem mover arquivos sem benefício demonstrado, quebrar URLs ou inventar informações históricas.

## 2. Fonte e método

O inventário utiliza:

- `mkdocs.yml` como fonte da navegação pública;
- metadados estruturados de cada documento como fonte de identificador, versão, estado e relações;
- `CATALOGO_DOCUMENTAL.md` como visão pública consolidada;
- a branch padrão como fonte canônica;
- commits e execuções de CI como evidência operacional.

Arquivos de infraestrutura são inventariados separadamente e não entram na contagem dos documentos públicos, salvo quando também aparecem na navegação.

## 3. Resumo do acervo público

A navegação contém **39 documentos Markdown**.

| Camada | Quantidade | Situação geral |
|---|---:|---|
| Publicação e acesso | 3 | página inicial, guia e catálogo identificados e versionados |
| Princípios e fundamentos | 6 | todos conformes |
| Governança e arquitetura | 9 | todos conformes |
| Método | 10 | todos conformes; reciprocidade obrigatória verificada |
| Ferramentas | 11 | todas conformes e vinculadas aos padrões associados |
| Aplicações e evidências | 0 | ainda não há estudo de caso oficial publicado |
| **Total** | **39** | **39 documentos identificados, versionados e catalogados** |

Trinta e oito documentos utilizam cabeçalho YAML no início do arquivo. O `README.md` utiliza representação estruturada equivalente em comentário HTML e seção colapsável, preservando sua função de página inicial no GitHub e no portal.

## 4. Inventário por camada

### 4.1 Publicação e acesso

| Documento | Identificador | Caminho | Versão | Representação |
|---|---|---|---:|---|
| Página inicial | `PORTAL-INICIO` | `README.md` | 0.3.0 | bloco equivalente e seção colapsável |
| Guia de início | `GUIA-COMECAR` | `docs/COMECAR.md` | 0.3.0 | cabeçalho YAML |
| Catálogo documental | `CATALOGO-DOCUMENTAL` | `CATALOGO_DOCUMENTAL.md` | 0.1.0 | cabeçalho YAML e geração reproduzível |

### 4.2 Princípios e fundamentos

| Documento | Identificador | Versão |
|---|---|---:|
| Carta de Princípios | `CARTA-DE-PRINCIPIOS` | 0.1.2 |
| Especificação | `SPECIFICATION` | 0.2.0 |
| Framework de Referência | `FRAMEWORK-DE-REFERENCIA` | 0.2.0 |
| Teoria do Pragmatismo Cívico | `TEORIA-DO-PRAGMATISMO-CIVICO` | 0.1.0 |
| Manifesto | `MANIFESTO` | 0.1.0 |
| Glossário | `GLOSSARIO` | 0.1.0 |

A hierarquia declarada permanece: direitos e garantias democráticas → Carta → Especificação → Framework → método → ferramentas e aplicações.

### 4.3 Governança e arquitetura

| Documento | Identificador |
|---|---|
| PPC-000 | `PPC-000` |
| Modelo de Governança | `GOV-001` |
| Roadmap | `GOV-002` |
| Guia de Contribuição | `GOV-003` |
| Código de Conduta | `GOV-004` |
| Metadados e Versionamento | `PPC-META-001` |
| Ciclo de Vida dos Padrões | `PPC-000A` |
| Arquitetura Documental | `ARQ-001` |
| Inventário e Plano de Migração | `ARQ-002` |

### 4.4 Método

| Documento | Identificador | Versão | Relação principal |
|---|---|---:|---|
| Ciclo do Pragmatismo Cívico | `CICLO-PC-001` | 0.1.0 | visão integrada |
| PPC-001 | `PPC-001` | 0.1.1 | diagnóstico |
| PPC-002 | `PPC-002` | 0.1.0 | alternativas |
| PPC-003 | `PPC-003` | 0.1.0 | avaliação técnica |
| PPC-004 | `PPC-004` | 0.1.0 | decisão |
| Teoria da Mudança | `MODELO-TDM-001` | 0.1.0 | ponte causal |
| PPC-005 | `PPC-005` | 0.1.0 | implementação |
| PPC-006 | `PPC-006` | 0.1.0 | monitoramento |
| PPC-007 | `PPC-007` | 0.1.0 | avaliação |
| PPC-008 | `PPC-008` | 0.1.1 | aprendizagem e retroalimentação entre ciclos |

### 4.5 Ferramentas

| Documento | Identificador | Versão | Documento associado |
|---|---|---:|---|
| Ficha PPC-001 | `FICHA-PPC-001` | 0.1.0 | PPC-001 0.1.1 |
| Ficha PPC-002 | `FICHA-PPC-002` | 0.1.0, piloto | PPC-002 0.1.0 |
| Ficha PPC-003 | `FICHA-PPC-003` | 0.1.4, piloto | PPC-003 0.1.0 |
| Ficha PPC-004 | `FICHA-PPC-004` | 0.1.0 | PPC-004 0.1.0 |
| Ficha de Teoria da Mudança | `FICHA-TDM-001` | 0.1.0 | MODELO-TDM-001 0.1.0 |
| Ficha PPC-005 | `FICHA-PPC-005` | 0.1.0 | PPC-005 0.1.0 |
| Ficha PPC-006 | `FICHA-PPC-006` | 0.1.1 | PPC-006 0.1.0 |
| Ficha PPC-007 | `FICHA-PPC-007` | 0.1.1 | PPC-007 0.1.0 |
| Ficha PPC-008 | `FICHA-PPC-008` | 0.1.0 | PPC-008 0.1.0 |
| Matriz de avaliação | `MATRIZ-PPC-001` | 0.1.0 | PPC-002 e PPC-003 0.1.0 |
| Indicadores | `MODELO-INDICADORES-001` | 0.1.0 | PPC-001, TDM, PPC-006 e PPC-007 |

### 4.6 Aplicações e evidências

Nenhum estudo de caso, piloto institucional ou relatório de aplicação está publicado na navegação canônica.

## 5. Infraestrutura fora da navegação

| Recurso | Função | Tratamento |
|---|---|---|
| `mkdocs.yml` | configuração, caminhos e navegação pública | fonte operacional do catálogo |
| `requirements.txt` | dependências fixadas do portal | infraestrutura |
| `.github/workflows/pages.yml` | validação, empacotamento e eventual deploy | automação |
| `scripts/prepare_mkdocs.py` | cria árvore temporária compatível com MkDocs | automação reproduzível |
| `scripts/generate_catalog.py` | gera o catálogo a partir dos metadados | automação reproduzível |
| `scripts/validate_metadata_graph.py` | valida estados, IDs, dependências e reciprocidade | validação parcial da Fase 6 |
| `docs/assets/` | estilos e ativos públicos | infraestrutura do portal |
| `LICENSE` | licença atual do repositório | revisão de adequação pendente |
| `.gitignore` | exclui artefatos locais de build | infraestrutura |

## 6. Cobertura e limites

Todos os 39 documentos públicos possuem:

- identificador estável;
- versão semântica;
- estado canônico;
- idioma e responsáveis;
- relações documentais aplicáveis;
- compatibilidade e histórico.

A conclusão da cobertura e do catálogo não significa estabilidade do framework. Permanecem ausentes casos oficiais, validação empírica suficiente, política de propostas de mudança e parte da validação automática.

## 7. Dívida documental

| ID | Problema | Risco | Estado | Tratamento |
|---|---|---|---|---|
| DD-001 | documentos navegáveis sem metadados | versões ambíguas | resolvida | Fases 1 a 4 |
| DD-002 | reciprocidade do ciclo metodológico | grafo incoerente | resolvida | auditoria 2C e validação automática |
| DD-003 | matriz e indicadores sem versões associadas | aplicações irreplicáveis | resolvida | Fase 3C |
| DD-004 | vínculos genéricos nas ferramentas | grafo heterogêneo | resolvida | Fase 3C |
| DD-005 | acervo predominantemente na raiz | manutenção futura difícil | aberta, baixa | decidir somente após validação |
| DD-006 | ausência de catálogo público | localização manual | resolvida | `CATALOGO-DOCUMENTAL` 0.1.0 |
| DD-007 | validação automática incompleta | regressões podem chegar ao portal | aberta | concluir Fase 6; deriva do catálogo já bloqueada |
| DD-008 | ausência de estudos de caso | método sem validação empírica | aberta, alta | preparar primeiro caso |
| DD-009 | datas históricas incompletas | história retrospectiva fictícia | controlada | preservar `null` e commits |
| DD-010 | confirmação de CI limitada | falhas poderiam passar despercebidas | parcialmente resolvida | status explícito `portal/build` e artefatos de diagnóstico |
| DD-011 | arquitetura histórica do Framework desatualizada | descrição incompatível | resolvida | Framework 0.2.0 |
| DD-012 | Especificação tratava documentos vigentes como futuros | ambiguidade | resolvida | Especificação 0.2.0 |
| DD-013 | ciclo conceitual confundido com ciclo PPC | aplicação inconsistente | resolvida | Especificação 0.2.0 |
| DD-014 | sustentabilidade institucional ausente da Especificação | incoerência normativa | resolvida | Especificação 0.2.0 |
| DD-015 | README incompatível com front matter comum | apresentação degradada | controlada | representação equivalente reconhecida pelos scripts |
| DD-016 | guia inicial cobria apenas parte do método | aplicação parcial | resolvida | GUIA-COMECAR 0.2.0 |
| DD-017 | guia atribuía versionamento ao PPC-000 | orientação imprecisa | resolvida | separação PPC-000/PPC-000A/PPC-META-001 |
| DD-018 | GitHub Pages ainda não habilitado | portal não é implantado | aberta | issue #1; ativação única pelo proprietário |
| DD-019 | `docs_dir` inválido e saída dentro do acervo | build estrito falhava | resolvida | árvore temporária `.mkdocs-src` e `site/` externo ao acervo |
| DD-020 | PPC-008 e Ficha PPC-003 declaravam saídas não recíprocas | dependências circulares ou indevidas | resolvida | relações reclassificadas e validador incorporado |
| DD-021 | catálogo publicado podia divergir das fontes canônicas | versões e relações desatualizadas | resolvida | CI compara geração reproduzível com arquivo publicado |

## 8. Avanços acumulados

As revisões produziram:

- cobertura de metadados e catálogo dos 39 documentos;
- alinhamento às seis camadas do ARQ-001;
- normalização do ciclo e das onze ferramentas;
- migração dos seis documentos fundadores;
- reparos de coerência no Framework, Especificação e guia de início;
- catálogo gerado por processo repetível;
- detecção automática de IDs duplicados, estados não canônicos, dependências inexistentes e saídas obrigatórias sem reciprocidade;
- bloqueio automático de divergência entre catálogo gerado e publicado;
- preparação reproduzível da árvore MkDocs;
- build estrito confirmado e registrado por status de commit;
- artefatos de diagnóstico preservados em caso de falha.

## 9. Plano progressivo

### Fases 0 a 4 — Migração e cobertura

**Estado:** concluídas.

### Fase 5 — Catálogo e navegação

**Estado:** concluída.

Entregas realizadas:

- catálogo público dos 39 documentos;
- identificador, versão, estado, tipo e caminho;
- agrupamento por camada;
- mapa de dependências obrigatórias e relações complementares;
- rotas de leitura;
- inventário inicial da infraestrutura fora da navegação;
- inclusão do catálogo no portal sem mover documentos existentes.

### Fase 6 — Validação automática

**Estado:** iniciada.

Concluído:

- leitura de YAML e da representação equivalente do README;
- campos mínimos;
- identificadores duplicados;
- estados canônicos;
- existência das dependências;
- reciprocidade de saídas obrigatórias;
- correspondência entre catálogo gerado e publicado;
- preparação e build estrito;
- status explícito de CI.

Pendente:

- formato completo de versões e compatibilidade;
- verificação de links internos e âncoras;
- validação das relações de substituição;
- relatório consolidado de dívida;
- deploy do portal após habilitação do Pages.

### Fase 7 — Estrutura física

Somente após a Fase 6 será decidido se arquivos devem sair da raiz. Manter a estrutura atual continua sendo uma opção legítima.

## 10. Critérios e decisões desta versão

Esta versão decide que:

- a Fase 5 está concluída;
- a linha de base pública contém 39 documentos;
- o catálogo é gerado a partir das fontes canônicas e publicado no repositório;
- a CI deve falhar quando o catálogo publicado divergir da geração atual;
- as relações PPC-008 → PPC-001 e Ficha PPC-003 → PPC-004 são complementares, não dependências obrigatórias;
- o build do portal está operacional;
- a implantação depende da ativação inicial do GitHub Pages registrada na issue #1;
- a próxima execução deve completar a Fase 6.

## 11. Próxima ação

Concluir a **Fase 6 — Validação automática**, acrescentando verificação de versões, compatibilidade, links, substituições e relatório consolidado de dívida.

## 12. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Inventário inicial, dívida documental e plano progressivo | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-17 | compatível | Migração do PPC-000 e do Modelo de Governança | Projeto Pragmatismo Cívico |
| 0.3.0 | 2026-07-17 | compatível | Correção das camadas e revisão da navegação | Projeto Pragmatismo Cívico |
| 0.4.0 | 2026-07-17 | compatível | Conclusão da Fase 1 | Projeto Pragmatismo Cívico |
| 0.5.0 | 2026-07-17 | compatível | Correções de identificadores e da Ficha PPC-003 | Projeto Pragmatismo Cívico |
| 0.6.0 | 2026-07-17 | compatível | Conclusão da Fase 2A | Projeto Pragmatismo Cívico |
| 0.7.0 | 2026-07-17 | compatível | Conclusão da Fase 2B | Projeto Pragmatismo Cívico |
| 0.8.0 | 2026-07-17 | compatível | Conclusão da Fase 2C | Projeto Pragmatismo Cívico |
| 0.9.0 | 2026-07-17 | compatível | Conclusão da Fase 3A | Projeto Pragmatismo Cívico |
| 0.10.0 | 2026-07-18 | compatível | Conclusão da Fase 3B e consolidação editorial | Projeto Pragmatismo Cívico |
| 0.11.0 | 2026-07-18 | compatível | Conclusão da Fase 3C | Projeto Pragmatismo Cívico |
| 0.12.0 | 2026-07-18 | compatível | Conclusão da Fase 4A | Projeto Pragmatismo Cívico |
| 0.13.0 | 2026-07-18 | compatível | Conclusão da Fase 4B e reparos normativos | Projeto Pragmatismo Cívico |
| 0.14.0 | 2026-07-18 | compatível | Conclusão da Fase 4C e cobertura dos 38 documentos | Projeto Pragmatismo Cívico |
| 0.14.1 | 2026-07-18 | correção | Sincronização do README 0.2.2 | Projeto Pragmatismo Cívico |
| 0.15.0 | 2026-07-18 | compatível | Conclusão da Fase 5, publicação do catálogo, reparos do grafo documental e estabilização do build estrito | Projeto Pragmatismo Cívico |
| 0.15.1 | 2026-07-18 | correção | Sincronização das versões de entrada e registro da verificação automática de deriva do catálogo | Projeto Pragmatismo Cívico |
