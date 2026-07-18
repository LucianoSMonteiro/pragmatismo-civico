---
id: ARQ-003
titulo: Decisão sobre a Estrutura Física do Repositório
versao: 0.1.0
status: rascunho
tipo: arquitetura
idioma: pt-BR
data_criacao: 2026-07-18
data_versao: 2026-07-18
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - ARQ-001
  - ARQ-002
  - PPC-META-001
produz_entrada_para: []
relaciona_se_com:
  - CATALOGO-DOCUMENTAL
  - MKDOCS
  - PORTAL-INICIO
  - GOV-002
substitui: []
substituido_por: null
compatibilidade: inicial
proxima_revisao: null
---

# ARQ-003 — Decisão sobre a Estrutura Física do Repositório

## Status da decisão

Decisão arquitetural inicial. Os caminhos dos documentos existentes serão preservados. O crescimento futuro adotará uma estrutura híbrida, com diretórios específicos para coleções expansíveis.

## 1. Problema

As camadas definidas pelo ARQ-001 são lógicas, enquanto a maior parte dos documentos permanece na raiz do repositório. A Fase 7 precisava decidir se o benefício de reorganizar fisicamente o acervo superava os riscos de alterar caminhos canônicos, links e referências externas.

## 2. Opções avaliadas

### Opção A — manter todos os documentos na raiz

Vantagens:

- preserva todos os caminhos e URLs existentes;
- reduz risco de links quebrados;
- mantém edição e histórico simples;
- não exige redirecionamentos.

Limitações:

- a raiz tende a ficar visualmente extensa;
- coleções futuras podem dificultar localização e manutenção;
- a estrutura física não expressa diretamente as camadas lógicas.

### Opção B — mover todo o acervo para diretórios por camada

Vantagens:

- aproxima a estrutura física das camadas do ARQ-001;
- separa categorias na visualização do repositório;
- pode facilitar automações específicas por diretório.

Limitações:

- altera quase todos os caminhos canônicos;
- exige revisão ampla de links, navegação e catálogo;
- afeta URLs de edição e possíveis referências externas;
- cria obrigação duradoura de redirecionamento;
- produz pouco ganho para o leitor do portal, cuja navegação já é lógica.

### Opção C — estrutura híbrida

Preserva os documentos existentes em seus caminhos atuais e utiliza diretórios para novas coleções cujo crescimento ou natureza justificam separação física.

## 3. Evidência reproduzível

A execução `29633432120`, baseada em 39 documentos navegáveis, produziu o artefato `structure-analysis` com os seguintes resultados:

| Medida | Resultado |
|---|---:|
| Documentos Markdown na raiz | 38 |
| Documentos que mudariam de caminho em uma migração por camada | 37 |
| Links Markdown entre documentos públicos | 125 |
| Referências internas potencialmente afetadas | 124 |
| Entradas de navegação a revisar | 37 |
| Diretórios de destino | 5 |

Os documentos mais afetados seriam o catálogo, o README e o guia de início, justamente as principais portas públicas do acervo.

## 4. Critérios de decisão

| Critério | Estrutura atual | Migração por camada | Estrutura híbrida |
|---|---|---|---|
| Preservação de URLs | alta | baixa | alta |
| Risco de regressão | baixo | alto | baixo |
| Navegação no portal | adequada | equivalente | adequada |
| Clareza visual no GitHub | moderada | alta | alta para coleções futuras |
| Custo imediato | baixo | alto | baixo |
| Escalabilidade para casos e relatórios | moderada | alta | alta |
| Reversibilidade | alta | moderada | alta |

## 5. Decisão

Adotar a **estrutura híbrida**:

1. preservar os caminhos dos documentos públicos existentes;
2. manter `README.md`, `mkdocs.yml` e arquivos de governança geral em seus caminhos atuais;
3. criar novas coleções de aplicações em `casos/`;
4. criar relatórios oficiais em `relatorios/`;
5. manter automações em `scripts/`, ativos em `docs/assets/` e workflows em `.github/workflows/`;
6. não criar diretórios vazios; cada diretório deve nascer com uma entrega real;
7. continuar usando `mkdocs.yml`, metadados e catálogo para representar as camadas lógicas.

A decisão não impede uma migração futura. Ela exige que qualquer migração demonstre benefício líquido e seja tratada como alteração arquitetural versionada.

## 6. Consequências

### Consequências positivas

- nenhum documento existente é movido;
- nenhuma URL ou referência precisa ser alterada;
- a navegação pública continua estável;
- casos e relatórios futuros não ampliarão indefinidamente a raiz;
- o custo de manutenção permanece proporcional ao tamanho atual do projeto.

### Limitações aceitas

- a raiz continuará contendo a maior parte do núcleo documental;
- as camadas não serão representadas integralmente por diretórios;
- leitores do repositório dependerão do catálogo e da navegação para a visão arquitetural.

## 7. Condições para reavaliação

A decisão deve ser reavaliada quando ocorrer uma das condições:

- publicação de três estudos de caso oficiais;
- crescimento do acervo navegável para 60 documentos;
- criação recorrente de relatórios, anexos ou conjuntos de dados;
- necessidade comprovada de permissões ou automações por diretório;
- disponibilidade de mecanismo confiável de redirecionamento;
- evidência documentada de que a estrutura atual causa erros ou custo material de manutenção.

## 8. Requisitos para uma migração futura

Uma proposta de migração deverá incluir:

- mapa completo de origem e destino;
- inventário de links e referências externas afetadas;
- estratégia de redirecionamento ou páginas de aviso;
- atualização atômica da navegação e do catálogo;
- validação automática antes e depois da mudança;
- plano de reversão;
- justificativa de benefício líquido;
- registro de decisão e versão compatível ou incompatível.

## 9. Verificação contínua

O script `scripts/analyze_repository_structure.py` gera uma análise atualizada em cada execução do workflow. O relatório é preservado como artefato `structure-analysis` por 14 dias.

## 10. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Decisão pela estrutura híbrida, preservação dos caminhos existentes e definição de gatilhos para reavaliação | Projeto Pragmatismo Cívico |
