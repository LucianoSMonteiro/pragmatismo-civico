---
id: CASO-001-DADOS-CHUVA
titulo: Protocolo de Aquisição e Qualidade de Dados Pluviométricos do CASO-001
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
  - GOV-008
  - PPC-META-001
  - ARQ-001
produz_entrada_para: []
relaciona_se_com:
  - CASOS-INDEX
  - CASO-001-FONTES
  - PPC-001
  - MODELO-INDICADORES-001
substitui: []
substituido_por: null
compatibilidade: compativel
proxima_revisao: null
issue_acompanhamento: 4
script_associado: scripts/processar_chuva_cemaden.py
---

# CASO-001 — Protocolo de dados pluviométricos

## 1. Estado

O processador está implementado e aprovado em teste sintético. **Nenhum arquivo mensal real do Cemaden foi incluído no repositório.**

A coleta real permanece pendente porque o portal exige confirmação humana para cada download mensal. Este protocolo não autoriza contornar CAPTCHA, confirmação de segurança ou restrição de acesso.

## 2. Escopo inicial

| Campo | Definição |
|---|---|
| fonte | Mapa Interativo do Cemaden |
| estação | Itapeba |
| código observado no portal | `3717` |
| município | Maricá/RJ |
| período preliminar | janeiro de 2022 a junho de 2026 |
| frequência de aquisição | um arquivo por mês |
| horário de origem | UTC |
| horário derivado | `America/Sao_Paulo` |

O período e a estação ainda precisam ser confirmados pela completude e pelos metadados dos arquivos obtidos.

## 3. Estrutura local

Os arquivos devem permanecer inicialmente em diretório local ignorado pelo Git:

```text
work/caso-001/cemaden/
├── raw/          # arquivos recebidos sem alteração
├── processed/    # CSV normalizado
├── manifest/     # hashes, filtros, cobertura e contagens
└── reports/      # relatório de qualidade e revisão manual
```

O `.gitignore` exclui `work/`. Isso reduz risco de publicação acidental, mas não substitui controles de acesso, licença, privacidade ou segurança no computador utilizado.

## 4. Aquisição mensal

Para cada mês:

1. acessar o download oficial de dados pluviométricos;
2. selecionar `RJ`, município `Maricá`, mês e ano;
3. preencher a confirmação de segurança manualmente;
4. baixar o arquivo sem alterar seu conteúdo;
5. nomear a cópia local de forma estável, por exemplo `cemaden-rj-marica-2022-04.csv`;
6. registrar data de acesso, página de origem e observações;
7. nunca substituir silenciosamente arquivo já adquirido;
8. preservar versões distintas quando o provedor republicar um mês.

A interface oficial informa que o download histórico é mensal, os registros usam UTC e os dados são brutos, podendo conter inconsistências.

## 5. Execução do processador

```bash
python scripts/processar_chuva_cemaden.py \
  --input-dir work/caso-001/cemaden/raw \
  --output work/caso-001/cemaden/processed/itapeba.csv \
  --manifest work/caso-001/cemaden/manifest/manifest.json \
  --report work/caso-001/cemaden/reports/quality.md \
  --station-name Itapeba \
  --station-id 3717 \
  --municipality Maricá \
  --state RJ
```

O processador aceita CSV ou TXT, tenta reconhecer delimitador e codificação e mapeia aliases comuns de data, precipitação, estação, município e UF.

## 6. Produtos

### CSV normalizado

Campos:

- `timestamp_utc`;
- `timestamp_america_sao_paulo`;
- `rainfall_mm`;
- identificação da estação;
- município e UF;
- arquivo e linha de origem;
- flags de qualidade.

### Manifesto JSON

Registra:

- versão do processador;
- filtros aplicados;
- SHA-256, tamanho, codificação e delimitador de cada fonte;
- linhas lidas, correspondentes e normalizadas;
- cobertura temporal;
- contagens de achados automáticos;
- limitações conhecidas.

### Relatório Markdown

Resume cobertura, hashes e flags para inspeção humana.

## 7. Controles automáticos

| Flag ou contagem | Interpretação |
|---|---|
| `invalid_timestamp` | data não reconhecida e linha não normalizada |
| `invalid_rainfall` | precipitação ausente ou não numérica |
| `negative_value` | valor negativo preservado e sinalizado |
| `duplicate_timestamp` | mais de uma linha no mesmo instante |
| `gap_after_previous` | intervalo superior a três vezes o intervalo modal observado |
| `filtered_out` | linha de outra estação, município ou UF |

Flags não provam erro instrumental e não autorizam exclusão automática. Toda correção ou remoção deve ser documentada.

## 8. Teste sintético

O arquivo `tests/fixtures/cemaden_itapeba_sintetico.csv` contém somente dados inventados para testar:

- vírgula decimal;
- conversão UTC;
- filtro de estação;
- data inválida;
- valor ausente;
- valor negativo;
- duplicidade;
- lacuna temporal.

Nenhuma linha do fixture pode ser citada como observação real. A CI executa o teste e publica o status `data/pipeline`.

## 9. Revisão manual obrigatória

Antes de usar a série no portão ou no PPC-001:

- conferir metadados e localização da estação;
- verificar início, fim e frequência esperada;
- revisar todas as flags;
- comparar acumulados com fontes independentes quando possível;
- verificar mudanças de equipamento ou código;
- distinguir ausência de chuva de ausência de registro;
- documentar qualquer transformação;
- avaliar licença e possibilidade de publicação;
- obter revisão técnica proporcional.

## 10. Limites analíticos

A série de uma estação:

- não define sozinha o limite da sub-bacia;
- não representa automaticamente toda a distribuição espacial da chuva;
- não demonstra causa de alagamento;
- não mede danos, manutenção ou capacidade da drenagem;
- não comprova eficácia de obra, alerta ou sistema inteligente;
- não substitui dados de nível, radar, ocorrências e conhecimento local.

## 11. Critério para publicação

Arquivos brutos ou derivados somente devem entrar na árvore pública após decisão registrada sobre:

- licença e atribuição;
- ausência ou tratamento de dados sensíveis;
- integridade e qualidade;
- tamanho e formato;
- utilidade para auditoria;
- risco de interpretação indevida;
- versão e hash canônicos.

Até essa decisão, somente o protocolo, o processador e o fixture sintético permanecem públicos.

## 12. Retenção e descarte local

### 12.1 Princípios

- retenção deve ser necessária, proporcional e vinculada à finalidade do caso;
- arquivo bruto não é alterado, mas pode ser eliminado quando sua retenção deixar de ser necessária ou permitida;
- manifesto, relatório e decisão de descarte preservam a memória sem exigir conservação indefinida dos dados;
- obrigação legal, contratual, de auditoria ou preservação de evidência prevalece sobre os prazos ordinários;
- material suspeito, não autorizado ou contendo dado pessoal desnecessário deve ser isolado imediatamente.

### 12.2 Prazos ordinários

| Categoria | Retenção mínima | Destino previsto |
|---|---|---|
| `raw/` — originais autorizados | durante o caso e por 12 meses após seu encerramento | preservar se necessário para auditoria; caso contrário, descartar com registro |
| `processed/` — derivados não publicados | durante o caso e por 12 meses após o encerramento | publicar versão aprovada ou descartar |
| `manifest/` — hashes e proveniência | durante o caso e por 24 meses após o encerramento | preservar no relatório final quando não houver restrição |
| `reports/` — qualidade e revisão | durante o caso e por 24 meses após o encerramento | incorporar ao acervo público quando aprovado |
| temporários, cópias intermediárias e duplicatas verificadas | até 30 dias após processamento e conferência de hash | eliminar |
| fixture sintético e testes | enquanto o processador for mantido | preservar no repositório |
| arquivo não autorizado, excessivo ou com dado sensível desnecessário | somente pelo tempo necessário para confirmar a ocorrência, no máximo 7 dias salvo obrigação de preservação | colocar em quarentena e eliminar com registro |

Os prazos são máximos ordinários, não autorização automática para conservar. A revisão pode determinar descarte antecipado quando a finalidade terminar ou a retenção aumentar risco sem benefício.

### 12.3 Revisão periódica

Enquanto o caso estiver ativo, o responsável deve revisar o inventário local pelo menos a cada 90 dias e registrar:

- categorias e quantidade de arquivos;
- espaço ocupado;
- existência de cópias e backups;
- licença e restrições conhecidas;
- necessidade de continuidade;
- incidentes, acessos excepcionais e decisões de descarte.

No encerramento, deve ser produzido inventário final com a destinação de cada conjunto.

### 12.4 Procedimento de descarte

1. identificar arquivo, categoria, caminho e hash quando disponível;
2. confirmar que não existe obrigação de retenção ou litígio conhecido;
3. registrar motivo, responsável e autorização;
4. mover para quarentena local restrita por até sete dias, quando o risco não exigir eliminação imediata;
5. eliminar a cópia principal e as cópias controladas;
6. registrar data, método e limitações do descarte;
7. verificar backups e registrar quando a expiração ocorrer apenas pelo ciclo normal do provedor.

Não se deve prometer apagamento irrecuperável em SSD, armazenamento em nuvem ou sistema com snapshots quando essa propriedade não puder ser tecnicamente verificada. Nesses casos, o registro deve declarar a limitação e impedir novo acesso ou restauração deliberada.

### 12.5 Backups, acesso e incidentes

- backups seguem o mesmo prazo da fonte, com criptografia e acesso mínimo quando disponíveis;
- credenciais e caminhos locais não são publicados;
- incidente de exposição suspende o processamento e exige avaliação antes da continuidade;
- arquivos potencialmente maliciosos não devem ser abertos fora de ambiente isolado;
- descarte não substitui comunicação de incidente quando houver obrigação aplicável.

## 13. Rastreamento

- [Matriz de fontes e lacunas](CASO-001_MATRIZ_DE_FONTES_E_LACUNAS.md) — proveniência e pendências;
- issue #4 — coleta mensal real;
- issue #5 — processador, teste e CI, concluída;
- issue #11 — armazenamento, retenção e descarte;
- issue #2 — decisão consolidada do portão.

## 14. Histórico de alterações

| Versão | Data | Tipo | Alteração | Responsável |
|---|---|---|---|---|
| 0.1.0 | 2026-07-18 | inicial | Criação do protocolo, estrutura local, processador, produtos e controles de qualidade | Projeto Pragmatismo Cívico |
| 0.2.0 | 2026-07-18 | compatível | Definição de retenção, revisão periódica, quarentena, descarte, backups e limites técnicos | Projeto Pragmatismo Cívico |
