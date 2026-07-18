---
id: ARQ-001
titulo: Arquitetura Documental do Framework
versao: 0.2.0
status: rascunho
tipo: arquitetura
idioma: pt-BR
data_criacao: 2026-07-17
data_versao: 2026-07-17
responsaveis:
  - Projeto Pragmatismo Cívico
aprovadores: []
depende_de:
  - FRAMEWORK-DE-REFERENCIA
  - PPC-000
  - PPC-000A
  - PPC-META-001
produz_entrada_para:
  - ARQ-002
relaciona_se_com:
  - GOV-001
  - GOV-002
  - MKDOCS
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
---

# ARQ-001 — Arquitetura Documental do Framework

## Status

Rascunho inicial para discussão pública e adoção progressiva.

## 1. Objetivo

Definir a arquitetura oficial dos documentos do Pragmatismo Cívico, incluindo:

- camadas e categorias documentais;
- responsabilidades de cada tipo de documento;
- relações de dependência;
- convenções de identificação e nomes;
- organização lógica do repositório;
- estrutura de navegação do portal;
- critérios para criação, alteração e localização de conteúdo;
- princípios para migração do acervo existente.

A arquitetura busca reduzir duplicação, ambiguidade e crescimento desordenado, sem transformar o repositório em uma burocracia documental.

## 2. Escopo

Aplica-se a todos os documentos oficiais do projeto, incluindo:

- princípios e fundamentos;
- documentos de governança;
- PPCs metodológicos e transversais;
- ferramentas práticas;
- estudos de caso;
- relatórios e avaliações;
- documentação do portal e do próprio repositório.

Não define o mérito metodológico dos PPCs, nem substitui o ciclo de vida, os metadados ou a governança de aprovação.

## 3. Relação com outros documentos

Esta arquitetura deve ser interpretada em conjunto com:

- `FRAMEWORK_DE_REFERENCIA.md` — preserva a essência e o núcleo conceitual;
- `PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md` — governa o ecossistema de padrões;
- `PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md` — governa estados e transições;
- `PPC-META-001_METADADOS_E_VERSIONAMENTO.md` — governa identificação, versão e relacionamentos;
- `MODELO_DE_GOVERNANCA.md` — define responsabilidades e decisões institucionais;
- `ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md` — inventaria o acervo e organiza a execução progressiva da migração;
- `mkdocs.yml` — materializa a navegação pública do acervo.

Em caso de conflito, documentos fundadores e normativos prevalecem sobre decisões de organização e navegação.

## 4. Princípios arquiteturais

A organização documental deve observar:

1. **Separação de responsabilidades** — cada documento deve possuir função clara.
2. **Dependência explícita** — relações obrigatórias devem ser declaradas.
3. **Fluxo compreensível** — o leitor deve saber por onde começar e como avançar.
4. **Fonte canônica única** — cada conteúdo oficial deve possuir uma versão de referência.
5. **Baixo acoplamento** — mudanças locais não devem exigir alterações desnecessárias em todo o acervo.
6. **Alta coesão** — conteúdos com a mesma finalidade devem permanecer próximos.
7. **Preservação histórica** — reorganização não deve apagar versões ou decisões anteriores.
8. **Proporcionalidade** — a estrutura deve crescer apenas quando facilitar uso, governança ou auditoria.
9. **Acessibilidade** — nomes, caminhos e navegação devem ser compreensíveis a públicos não especializados.
10. **Automação assistiva** — ferramentas podem validar e publicar, mas não substituir julgamento humano.

## 5. Camadas da arquitetura

O framework é organizado em seis camadas lógicas.

```text
1. Princípios e fundamentos
        ↓
2. Governança e arquitetura
        ↓
3. Método
        ↓
4. Ferramentas
        ↓
5. Aplicações e evidências
        ↓
6. Publicação e acesso
        ↺
Aprendizagem retroalimenta todas as camadas
```

As camadas são lógicas. Durante a migração, documentos podem permanecer na raiz do repositório, desde que sua categoria seja inequívoca.

## 6. Camada 1 — Princípios e fundamentos

### 6.1 Função

Define o núcleo conceitual, ético e identitário que orienta todo o framework.

### 6.2 Documentos típicos

- `FRAMEWORK_DE_REFERENCIA.md`;
- `TEORIA_DO_PRAGMATISMO_CIVICO.md`;
- `MANIFESTO.md`;
- `CARTA_DE_PRINCIPIOS.md`;
- `SPECIFICATION.md`;
- `GLOSSARIO.md`.

### 6.3 Regras

- mudanças devem ser raras e explicitamente justificadas;
- documentos inferiores não podem redefinir silenciosamente seus princípios;
- divergências interpretativas relevantes devem ser registradas;
- o conteúdo deve permanecer legível a públicos não especializados.

## 7. Camada 2 — Governança e arquitetura

### 7.1 Função

Define como o projeto é organizado, mantido, revisado e publicado.

### 7.2 Categorias

- governança institucional;
- governança dos padrões;
- metadados e versionamento;
- ciclo de vida;
- arquitetura documental;
- contribuição e conduta;
- roadmap e planejamento.

### 7.3 Documentos típicos

- `MODELO_DE_GOVERNANCA.md`;
- `PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md`;
- `PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md`;
- `PPC-META-001_METADADOS_E_VERSIONAMENTO.md`;
- `ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md`;
- `ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md`;
- `CONTRIBUTING.md`;
- `CODE_OF_CONDUCT.md`;
- `ROADMAP.md`.

### 7.4 Regra de precedência

A arquitetura organiza, mas não altera o conteúdo normativo dos documentos governados.

## 8. Camada 3 — Método

### 8.1 Função

Transforma princípios em um processo decisório aplicável.

### 8.2 Fluxo principal

```text
PPC-001 — Diagnóstico
↓
PPC-002 — Formulação de alternativas
↓
PPC-003 — Avaliação técnica
↓
PPC-004 — Decisão e justificativa
↓
Teoria da mudança
↓
PPC-005 — Implementação e gestão adaptativa
↓
PPC-006 — Monitoramento e avaliação contínua
↓
PPC-007 — Avaliação de resultados e impactos
↓
PPC-008 — Aprendizagem institucional e melhoria contínua
↺
Novo ciclo pelo PPC-001
```

### 8.3 Regras

- cada PPC deve possuir objetivo, entradas, processo, saídas, critérios e limitações;
- dependências obrigatórias devem ser recíprocas nos metadados;
- a numeração não substitui a declaração explícita de relações;
- ferramentas não devem introduzir obrigação metodológica ausente no padrão associado.

## 9. Camada 4 — Ferramentas

### 9.1 Função

Operacionaliza os padrões por meio de instrumentos reutilizáveis.

### 9.2 Tipos

- fichas;
- matrizes;
- checklists;
- modelos de relatório;
- roteiros;
- catálogos de indicadores;
- guias de facilitação.

### 9.3 Regras

- toda ferramenta deve declarar o padrão ou documento que operacionaliza;
- uma ferramenta pode possuir aplicação simplificada e completa;
- campos obrigatórios devem ser distinguíveis dos opcionais;
- ferramentas devem registrar a versão do padrão utilizada;
- exemplos preenchidos devem ser identificados como exemplos, não como modelos normativos.

## 10. Camada 5 — Aplicações e evidências

### 10.1 Função

Registra o uso real ou simulado do framework e produz evidências sobre sua utilidade.

### 10.2 Tipos

- estudos de caso;
- projetos-piloto;
- avaliações independentes;
- relatórios de implementação;
- relatórios de resultados e impactos;
- registros de lições aprendidas;
- conjuntos de dados e anexos metodológicos.

### 10.3 Regras

- cada aplicação deve informar quais versões dos padrões utilizou;
- fatos, interpretações e recomendações devem ser separados;
- dados sensíveis devem seguir restrições legítimas de privacidade e segurança;
- falhas, limitações e divergências não devem ser omitidas;
- aplicações concluídas não devem ser reescritas para aparentar conformidade retroativa.

## 11. Camada 6 — Publicação e acesso

### 11.1 Função

Torna o acervo localizável, compreensível e reutilizável.

### 11.2 Componentes

- repositório GitHub;
- GitHub Pages;
- configuração MkDocs;
- busca;
- navegação;
- versões para impressão;
- catálogo de documentos;
- changelogs e registros de versão.

### 11.3 Regra canônica

O repositório oficial é a fonte canônica. O portal é sua interface pública de leitura.

Em divergência causada por atraso de publicação, prevalece o conteúdo da branch padrão do repositório.

## 12. Categorias e identificadores

A identificação segue o PPC-META-001.

| Categoria | Prefixo recomendado | Exemplo |
|---|---|---|
| Padrão metodológico | `PPC-` | `PPC-005` |
| Padrão transversal | `PPC-META-` ou extensão governada | `PPC-META-001` |
| Arquitetura | `ARQ-` | `ARQ-001` |
| Governança | `GOV-` | `GOV-001` |
| Ferramenta | `FICHA-`, `MATRIZ-`, `CHECK-`, `MODELO-` | `FICHA-PPC-005` |
| Estudo de caso | `CASO-AAAA-NNN` | `CASO-2026-001` |
| Relatório | `REL-AAAA-NNN` | `REL-2026-001` |

Identificadores históricos já consolidados podem ser preservados. A migração não deve renomear documentos apenas por estética.

## 13. Convenções de nomes de arquivo

### 13.1 Regras gerais

- utilizar extensão `.md` para documentação textual;
- começar pelo identificador quando houver código formal;
- utilizar maiúsculas, números, hífens e sublinhados;
- evitar caracteres ambíguos e nomes genéricos;
- não incorporar a versão no nome do arquivo canônico;
- evitar datas, salvo em casos, relatórios e registros periódicos;
- preservar caminhos antigos quando uma renomeação for necessária.

### 13.2 Exemplos

```text
PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md
FICHA_PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md
ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md
CASO-2026-001_MOBILIDADE_URBANA.md
```

## 14. Organização lógica do repositório

### 14.1 Estado atual

O repositório utiliza predominantemente arquivos Markdown na raiz. Essa organização permanece válida durante a fase inicial porque reduz risco de links quebrados e facilita a transição.

### 14.2 Estrutura-alvo

Uma futura migração pode adotar:

```text
/
├── README.md
├── mkdocs.yml
├── fundamentos/
├── governanca/
├── metodo/
├── ferramentas/
├── casos/
├── relatorios/
├── assets/
└── .github/
```

### 14.3 Condições para mover arquivos

Um arquivo só deve mudar de caminho quando:

- houver benefício claro de navegação ou manutenção;
- todos os links internos forem atualizados;
- a navegação do portal for validada;
- referências externas relevantes forem consideradas;
- houver estratégia de redirecionamento ou aviso;
- a alteração for registrada como migração documental.

A criação desta arquitetura não autoriza, por si só, a movimentação imediata do acervo.

## 15. Regras de dependência

### 15.1 Direção preferencial

As dependências devem fluir das camadas inferiores para as superiores:

```text
Aplicações → Ferramentas → Método → Governança → Fundamentos
```

Um documento pode consultar resultados produzidos por camada posterior, mas não deve depender normativamente deles para definir seu próprio fundamento.

### 15.2 Regras

- fundamentos não dependem de ferramentas ou casos específicos;
- governança pode reger todas as camadas, mas não redefinir princípios;
- ferramentas dependem dos padrões que operacionalizam;
- casos dependem das versões efetivamente utilizadas;
- publicação depende de todas as camadas apenas para exposição, não para autoridade normativa;
- ciclos de aprendizado podem propor alterações, mas devem seguir a governança de mudanças.

## 16. Fonte única e duplicação

Um conceito normativo deve possuir uma fonte principal.

Documentos secundários podem:

- resumir;
- contextualizar;
- exemplificar;
- apontar para a fonte canônica.

Não devem copiar extensamente regras que possam divergir com o tempo. Quando repetição for necessária para usabilidade, deve haver referência explícita ao documento canônico.

## 17. Criação de novos documentos

Antes de criar um documento, deve-se responder:

1. qual problema documental ou metodológico ele resolve;
2. em qual camada se encontra;
3. qual categoria e identificador utiliza;
4. qual documento é sua fonte superior;
5. se já existe conteúdo equivalente;
6. quais dependências cria;
7. quem será responsável pela manutenção;
8. como será validado;
9. onde aparecerá no portal;
10. qual custo de manutenção adiciona.

Um novo arquivo não deve ser criado quando uma seção em documento existente resolver o problema com maior clareza.

## 18. Alteração de documentos

Uma alteração deve avaliar impactos sobre:

- documentos dependentes;
- ferramentas associadas;
- navegação;
- links internos;
- roadmap;
- metadados e versão;
- casos em andamento;
- versões para impressão;
- automações futuras.

Mudanças estruturais devem seguir PPC-META-001 e PPC-000A.

## 19. Navegação do portal

A navegação pública deve refletir a lógica de uso, não apenas a estrutura de arquivos.

Ordem recomendada:

1. Início e guia de entrada;
2. Fundamentos do projeto;
3. Método;
4. Ferramentas;
5. Aplicações e estudos de caso;
6. Governança e arquitetura;
7. Roadmap e contribuição.

Documentos técnicos de manutenção podem permanecer fora da navegação principal quando não forem úteis ao público geral, mas devem continuar localizáveis no repositório.

## 20. Critérios de qualidade arquitetural

A arquitetura é adequada quando:

- cada documento possui função reconhecível;
- o leitor consegue localizar o conteúdo sem conhecer o repositório previamente;
- dependências podem ser reconstruídas;
- há pouca duplicação normativa;
- mudanças possuem impacto previsível;
- o portal acompanha a fonte canônica;
- o acervo pode crescer sem perder coerência;
- a estrutura não exige manutenção desproporcional.

## 21. Validação de alterações arquiteturais

Antes de aprovar uma mudança de arquitetura, deve-se verificar:

- necessidade real;
- benefício para leitores e mantenedores;
- impacto sobre links e URLs;
- compatibilidade com MkDocs e GitHub Pages;
- impacto sobre automações;
- custo de migração;
- reversibilidade;
- preservação histórica;
- atualização do roadmap;
- conformidade com PPC-META-001 e PPC-000A.

## 22. Migração progressiva

A migração deve ocorrer em etapas controladas:

### Etapa 1 — Inventário

- listar documentos existentes;
- classificar por camada e categoria;
- identificar duplicações, lacunas e referências quebradas;
- registrar documentos sem metadados.

### Etapa 2 — Metadados

- adicionar identificadores e versões aos documentos centrais;
- declarar relações e responsáveis;
- preservar datas e histórico disponíveis;
- registrar incertezas sem inventar informações.

### Etapa 3 — Navegação

- alinhar o portal às camadas;
- criar catálogo de padrões e ferramentas;
- revisar nomes apresentados ao público;
- validar links.

### Etapa 4 — Estrutura física

- avaliar se mover arquivos produz benefício líquido;
- migrar em lotes pequenos;
- atualizar links, navegação e referências;
- verificar o build após cada lote.

### Etapa 5 — Automação

- validar metadados;
- detectar links quebrados;
- gerar catálogo e mapas de dependência;
- alertar sobre revisões vencidas.

## 23. Dívida documental

Inconsistências existentes devem ser tratadas como dívida documental, não apagadas ou disfarçadas.

Cada item deve registrar:

- problema;
- documentos afetados;
- risco;
- prioridade;
- ação proposta;
- responsável, quando definido;
- estado da correção.

## 24. Limitações

Esta arquitetura não resolve sozinha:

- conflitos substantivos entre documentos;
- falta de revisão técnica;
- ausência de participação pública;
- preservação digital de longo prazo;
- qualidade dos estudos de caso;
- segurança de dados;
- escolha da licença adequada.

## 25. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-17 | inicial | Primeira publicação da arquitetura documental | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-17 | compatível | Atualização das relações canônicas e incorporação do ARQ-002 à arquitetura publicada | Projeto Pragmatismo Cívico |
