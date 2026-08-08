---
name: jornada-invisivel-mapper
description: >
  Use when the user needs to map a customer journey, reveal invisible touchpoints,
  identify moments of truth and friction, or connect journey insights to a North Star
  metric. Ative quando o usuário precisar: entender experiência do cliente, mapear
  jornada de compra, identificar gargalos não-óbvios no funil, diferenciar jornada vs
  processo vs canal, ou encontrar oportunidades de inovação escondidas nos atritos da
  experiência. Keywords: jornada do cliente, touchpoint, momento de verdade, atrito,
  experiência, funil, jornada invisível, percepção, decisão, canal, processo, experimento,
  teste A/B, pós-venda, recuperação, multi-touch.
version: 4.0.0
author: Fabrizzio Topper / Growth Intelligence — USP ESALQ MBX
license: MIT
metadata:
  hermes:
    tags: [customer-journey, growth, funnel, moment-of-truth, friction, experimentation, north-star]
    related_skills: [north-star-architect]
    requires_toolsets: [terminal]
---

# Jornada Invisível Mapper

> **Formato universal:** esta skill roda em Kimi CLI, Claude Code e Hermes Agent.
> O pacote contém este `SKILL.md` e o script determinístico `scripts/validar_relatorio.py`.
> Antes de entregar qualquer relatório, execute o validador (seção 14.1).

## 0. Princípio Zero (leia antes de tudo)

> **A jornada que você desenha no quadro branco é a jornada que VOCÊ quer ver. 
> A jornada que o cliente vive é a que importa. A diferença entre as duas é onde o dinheiro some.**

> **Growth não mapeia por 3 meses para depois agir. Growth testa em 48h e mede em 7 dias.**

Esta skill não é consultoria de €500/hora. É ferramenta para quem precisa de resultado 
na segunda-feira com o que tem na mão hoje.

Baseada no framework de **Fabrizzio Topper**, Growth Intelligence — USP ESALQ MBX.

---

## 1. Contexto de Domínio (o que o agente precisa saber)

- **Jornada do cliente** = soma de todas as experiências que formam percepção e decisão, 
  do primeiro contato ao abandono ou recompra. NÃO é o fluxograma do seu CRM.
- **Jornada invisível** = camadas de influência que você não controla diretamente, 
  mas que definem a escolha: sentimento de confiança, comparação com concorrente, 
  opinião de terceiro, memória de experiência anterior, expectativa criada por marketing.
- **Momento de verdade** = ponto na jornada onde a percepção do cliente é formada 
  ou destruída de forma irreversível. São poucos. Cada um vale mais que 100 touchpoints comuns.
- **Momento de recuperação** = quando um erro é corrigido de forma surpreendente. 
  Em Customer Service, resolve BEM = lealdade maior do que se nunca tivesse problema 
  (service recovery paradox). O momento de recuperação é mais poderoso que o momento de magia.
- **Touchpoint visível** = interação mensurável: clique, ligação, visita, proposta. 
  Você tem dados. Você acha que isso é a jornada. Não é.
- **Touchpoint invisível** = influência não-mensurável: o cliente que pesquisa seu 
  concorrente no Google às 3h da manhã, o amigo que diz "não compra lá", a lembrança 
  de um atraso de entrega de 2 anos atrás. Você não tem dados. Mas isso decide a venda.
- **Atrito** = qualquer ponto da jornada onde o cliente gasta mais energia do que deveria 
  para avançar. Atrito invisível é pior que atrito visível — porque você não sabe que existe.
- **Atrito de handoff** = transferência mal documentada entre departamentos 
  (vendas → CS, CS → técnico). Cada handoff não mapeado é um cliente perdido.
- **Processo** = como SUA empresa faz as coisas (interno). Não é jornada.
- **Canal** = onde a interação acontece (Meta, WhatsApp, loja física). Não é jornada.
- **Jornada ≠ Processo ≠ Canal.** Eles se conectam, mas são coisas diferentes. 
  Confundir os três é o erro mais comum de mapeamento.
- **Jornada fragmentada** = cliente vê anúncio no Instagram no celular, pesquisa no Google 
  no trabalho, recebe email no desktop, compra na loja física. Sem atribuição multi-touch, 
  você acha que a venda veio da loja. Veio do Instagram.
- **North Star da jornada** = cada momento de verdade deve ter KPI associado. 
  Sem número, é mapa de parede, não estratégia de growth.

---

## 2. Fase 0: Mínimo Viável para Começar (não espere o ideal)

### 2.1 O que você PRECISA ter (mínimo absoluto)

| Item | Mínimo viável | Ideal | Se faltar o mínimo |
|------|--------------|-------|-------------------|
| Dados de comportamento | Google Analytics, 100+ sessões | Mixpanel/Amplitude com eventos | Use entrevistas como proxy |
| Entrevistas com clientes | 3 profundas | 20 estruturadas | Use dados quantitativos + 1 entrevista |
| Definição de persona | 1 persona viva (nome, idade, rotina) | 5 personas com jobs-to-be-done | Use seu cliente mais recente |
| LGPD/GDPR | Aviso de privacidade no site | Consentimento explícito por etapa | Não rastreie individualmente sem consentimento |

**Regra de ouro:** Se não tem o ideal, use o mínimo. Growth é iterativo, não waterfall. 
Mapeamento ruim hoje é melhor que mapeamento perfeito em 3 meses.

### 2.2 Dicionário de Jornada (exigir antes de interpretar)

Antes de citar qualquer etapa da jornada, exija do usuário:
- **Qual é o gatilho de início?** (o que faz o cliente começar a jornada?)
- **Qual é o gatilho de fim?** (quando ele considera a jornada concluída?)
- **Quem mais participa da decisão?** (cônjuge, amigo, contador, patrão)
- **O que ele faz quando NÃO está interagindo com você?** (pesquisa concorrente, adia, desiste)

**Regra de ouro:** Se o usuário não souber responder "o que o cliente faz quando não está comigo", 
você está mapeando metade da jornada. Sinalize como **GAP CRÍTICO**, não como aborto.

---

## 3. Fase 1: Diagnóstico da Jornada Atual (o que existe hoje)

### 3.1 Mapear o que VOCÊ acha que é a jornada (5 minutos)

Desenhe a jornada atual da empresa — NÃO a ideal, a REAL:

1. Liste todos os canais ativos (Meta, Google, site, loja, telefone, WhatsApp, indicação).
2. Para cada canal, liste os touchpoints que VOCÊ controla (anúncio, landing page, formulário, 
   ligação do vendedor, proposta, contrato, entrega, pós-venda).
3. Marque em VERMELHO os touchpoints onde você NÃO TEM DADOS de comportamento do cliente 
   (ex: "cliente compara com concorrente" — você não sabe quando isso acontece).
4. Se mais de 30% dos touchpoints estão em vermelho, **a jornada que você desenhou é ficção.** 
   Recomece com pesquisa qualitativa.

### 3.2 Mapear o que o CLIENTE vive (mínimo viável)

**Opção A — Se você tem dados quantitativos (100+ usuários):**
- Análise de funil: onde está o maior abandono?
- Análise de tempo: onde o cliente fica mais tempo parado?
- Análise de repetição: onde o cliente volta mais de uma vez?
- Heatmap (se tiver): onde clica, onde para, onde desiste.

**Opção B — Se você tem 3 entrevistas profundas:**

| Pergunta | O que revela | Tempo |
|----------|-------------|-------|
| "Conte-me o dia em que você decidiu procurar [produto]." | Gatilho real de início | 5 min |
| "O que você fez ANTES de nos encontrar?" | Touchpoints invisíveis | 3 min |
| "Teve algum momento em que quase desistiu?" | Atritos críticos | 5 min |
| "O que mais te fez confiar em nós?" | Momento de verdade positivo | 3 min |
| "O que mais te deixou com dúvida?" | Momento de verdade negativo | 3 min |
| "Se você contasse para um amigo como foi comprar conosco, o que diria?" | Percepção consolidada | 3 min |
| "O que aconteceu DEPOIS que você comprou?" | Jornada pós-venda | 5 min |
| "Teve algum problema que resolvemos bem?" | Momento de recuperação | 5 min |

**Regra de ouro:** Se 2 de 3 entrevistados mencionam o mesmo touchpoint invisível, 
ele entra no mapa como **crítico**. Não ignore porque você não tem dados quantitativos.

### 3.3 Integridade do Funil (validação obrigatória antes de prosseguir)

Antes de publicar qualquer tabela de etapas, valide a aritmética do funil:

1. **Fechamento sequencial:** para cada etapa, `chegaram(n+1) = chegaram(n) − abandonaram(n)`. 
   Se divergir, corrija os números ANTES de prosseguir. Funil que não fecha invalida 
   toda taxa calculada sobre ele.
2. **Conversão acumulada:** usar a última etapa EFETIVA (quem completou), nunca a nominal 
   (quem chegou na etapa). "100 descobertas → 43 chegaram na compra, 21 abandonaram" 
   significa **22 conversões (22%)**, não 43.
   **Aritmética explícita obrigatória:** a frase de conversão acumulada deve MOSTRAR A CONTA —
   "X descobertas → Y completaram = Z%", onde Y = chegaram − abandonaram da última etapa
   obrigatória, com a fonte nomeada (calculado ou oficial). Headline sem conta visível = reprovado.
3. **Viés de sobrevivência:** se o abandono for 0% em TODAS as etapas, o dataset provavelmente 
   só contém clientes que completaram a jornada. Sinalize **VIÉS DE SOBREVIVÊNCIA** e trate 
   as taxas como limite superior otimista, não como realidade.
4. **Discrepância com métrica oficial:** se os dados calculados divergirem de uma métrica oficial 
   em QUALQUER etapa obrigatória (não só na etapa de advocacy), resolva a divergência ou sinalize 
   como GAP DE DADOS com hipótese de causa E veredito de qual fonte priorizar. Nunca deixar 
   contradição pendurada sem veredito — divergência silenciosa em etapa obrigatória é bloqueante.

**Regra de ouro:** número que não fecha é pior que número ausente. O ausente você declara, 
o errado você defende sem saber.

---

## 4. Fase 2: Identificação dos Touchpoints Invisíveis

### 4.1 Os 5 Tipos de Touchpoint Invisível (priorizados por influenciabilidade)

| Tipo | Exemplo | Como detectar | Prioridade para ação |
|------|---------|-------------|---------------------|
| **1. Influência social** | Amigo diz "não compra lá" | Perguntar "quem mais influenciou sua decisão?" | **ALTA** — você pode criar programa de indicação |
| **2. Memória de experiência** | Cliente teve problema com entrega 2 anos atrás | Perguntar "já ouviu falar de nós antes?" | MÉDIA — você pode reconquistar com oferta |
| **3. Comparação silenciosa** | Cliente abre 3 abas de concorrente ao mesmo tempo | Análise de tempo entre cliques, heatmaps | BAIXA — você não controla, só reage |
| **4. Expectativa não-atendida** | Marketing prometeu "entrega em 24h", operação entrega em 72h | Cruzar promessa de marketing com SLA real | **ALTA** — você controla a promessa |
| **5. Emoção não-registrada** | Cliente fica frustrado com formulário longo, mas não reclama | Análise de abandono em etapas específicas | **ALTA** — você controla o formulário |

**Regra de ouro:** Priorize touchpoints invisíveis que você pode INFLUENCIAR com budget e decisão interna. 
Influência social (programa de indicação) > comparação silenciosa (que você não controla).

### 4.2 Cruzamento: Visível vs Invisível

Para cada etapa da jornada, crie uma matriz:

```
ETAPA: "Consideração de proposta"
┌────────────────────┬────────────────────┬────────────────────┐
│   TOUCHPOINT VISÍVEL │  TOUCHPOINT INVISÍVEL │   IMPACTO NA DECISÃO │
├────────────────────┼────────────────────┼────────────────────┤
│ Proposta enviada    │ Cliente compara com  │ Se proposta for 10%  │
│ por email           │ 2 concorrentes        │ mais cara, perde      │
│                     │ simultaneamente       │ mesmo com melhor    │
│                     │                       │ atendimento         │
├────────────────────┼────────────────────┼────────────────────┤
│ Follow-up do        │ Cliente espera que    │ Se demora > 24h,    │
│ vendedor            │ vendedor lembre dele  │ cliente acha que    │
│                     │ sem ser lembrado      │ não é prioridade    │
└────────────────────┴────────────────────┴────────────────────┘
```

**Regra de ouro:** Se o touchpoint invisível tem impacto maior que o visível, 
a etapa está **quebrada do lado de fora**. Você precisa consertar o invisível, não o visível.

---

## 5. Fase 3: Identificação dos Momentos de Verdade

### 5.1 Definição rigorosa

Momento de verdade = ponto na jornada onde a percepção do cliente muda de forma 
**irreversível** (positiva ou negativa) e essa mudança influencia a decisão final.

NÃO é qualquer interação. É o momento que o cliente lembra quando conta para um amigo.

### 5.2 Filtro de identificação (3 perguntas)

Para cada touchpoint (visível ou invisível), pergunte:
1. **Se removermos este touchpoint, a decisão do cliente mudaria?** 
   → Se SIM, é candidato a momento de verdade.
2. **Este touchpoint cria uma memória emocional (positiva ou negativa)?**
   → Se SIM, é candidato a momento de verdade.
3. **Este touchpoint é mencionado espontaneamente em entrevistas?**
   → Se SIM, é momento de verdade.

**Regra de ouro:** Uma jornada de 20 touchpoints tem no máximo 3-5 momentos de verdade. 
Se você encontrou 15, está confundindo momento de verdade com touchpoint comum.

### 5.3 Classificação dos Momentos de Verdade

| Tipo | Característica | Exemplo | Ação recomendada | KPI associado |
|------|---------------|---------|-----------------|-------------|
| **Momento de Magia** | Supera expectativa. Cliente conta para outros. | Entrega 2 dias antes do prometido | Replicar e amplificar | Taxa de indicação pós-momento |
| **Momento de Frustração** | Destrói confiança. Cliente desiste ou churna. | Proposta com erro de preço | Eliminar imediatamente | Taxa de abandono na etapa |
| **Momento de Dúvida** | Cria incerteza. Cliente para ou compara. | Falta de informação sobre garantia | Clarear e simplificar | Tempo de decisão na etapa |
| **Momento de Confirmação** | Valida decisão. Cliente se sente inteligente. | Test drive que supera expectativa | Documentar e reforçar | Taxa de conversão pós-momento |
| **Momento de Recuperação** | Erro corrigido de forma surpreendente. Lealdade aumenta. | Problema de entrega resolvido com upgrade grátis | Criar protocolo de recovery | NPS pós-recuperação vs NPS normal |

**Regra de ouro:** Momento de Recuperação é o mais poderoso de todos. 
Um cliente que teve problema BEM resolvido fica mais leal do que cliente que nunca teve problema.

### 5.4 Fallback de Taxonomia (obrigatório)

A taxonomia existe porque cada tipo tem **ação recomendada e KPI padrão vinculados**. 
Tipo inventado quebra o vínculo tipo → ação → KPI.

- Se a emoção observada não cabe em nenhum dos 5 tipos, mapeie para o tipo **mais próximo** 
  e registre a emoção real na coluna **Emoção** (ex: tipo Frustração, emoção "remorso"; 
  tipo Frustração, emoção "indiferença/esquecimento").
- **NUNCA** criar tipo novo sem declarar explicitamente: 
  *"Extensão de taxonomia: [tipo novo], porque nenhum dos 5 existentes cobre [razão], 
  com ação recomendada [X] e KPI padrão [Y]."*

---

## 6. Fase 4: Análise de Atritos e Oportunidades

### 6.1 Mapeamento de Atritos

Atrito = energia que o cliente gasta para avançar na jornada. 
Quanto mais atrito, mais chance de abandono.

**Tipos de atrito:**
- **Atrito visível:** formulário longo, fila na loja, demora no atendimento. 
  Você mede. Você corrige.
- **Atrito invisível:** dúvida não sanada, medo de fazer besteira, comparação 
  com concorrente que parece mais confiável. Você não mede. Você não corrige. 
  O cliente some.
- **Atrito de handoff:** transferência mal documentada entre departamentos 
  (vendas → CS, CS → técnico). Cliente repete a mesma informação 3 vezes para 3 pessoas. 
  Isso não é atrito de processo. É atrito de jornada — e mata lealdade.

### 6.2 Matriz de Atrito (priorização com dono e esforço)

Para cada atrito identificado, classifique:

```
                    IMPACTO NA DECISÃO
                 Baixo          Alto
           ┌─────────────┬─────────────┐
    Fácil  │   Atrito 2  │  ATRITO 1   │  ← Resolver primeiro
    de     │  (ignorar)  │  (resolver  │
    resolver│             │   imediatamente)│
           ├─────────────┼─────────────┤
    Difícil│   Atrito 3  │  Atrito 4   │  ← Planejar para Q2
    de     │  (monitorar)│  (projetar  │
    resolver│             │   mudança)  │
           └─────────────┴─────────────┘
```

**Cada atrito na matriz deve ter:**
- **Dono:** quem é responsável por resolver?
- **Esforço:** quantas horas de trabalho? (dev: 4h, design: 2h, legal: 2 semanas)
- **Dependências:** o que precisa estar pronto antes? (ex: aprovação de budget, integração de API)
- **Data de teste:** quando vai rodar o teste A/B? (máx 7 dias para Atrito 1)

**Regra de ouro:** Matriz sem dono e sem data de teste é decoração de parede.

### 6.3 Oportunidades — com estimativa de impacto

**Pergunta-chave:** "O que o cliente queria fazer, mas não conseguiu por causa do atrito?"

Para cada oportunidade, estime:

| Oportunidade | Clientes afetados/mês | Valor por cliente | Receita potencial | Custo de implementar | ROI estimado | Tempo para deploy |
|-------------|----------------------|-------------------|-------------------|---------------------|--------------|-------------------|
| Gateway com reembolso 7 dias | 50 | €25.000 | €1.250.000 | €5.000 | 250:1 | 2 semanas |
| Avaliação instantânea no site | 30 | €30.000 | €900.000 | €8.000 | 112:1 | 3 semanas |
| Botão de indicação no WhatsApp | 20 | €400 (recompensa) | €8.000 | €1.000 | 8:1 | 1 semana |

**Regra de ouro:** Oportunidade sem estimativa de impacto é wishlist. 
Growth prioriza por ROI e velocidade, não por "seria legal".

---

## 7. Fase 5: Diferenciação — Jornada vs Processo vs Canal

### 7.1 O Erro Clássico

Empresas confundem:
- **Canal** (onde) com **Jornada** (por que o cliente está lá)
- **Processo** (como a empresa faz) com **Jornada** (o que o cliente sente)

**Exemplo de erro:**
> "Nossa jornada é: cliente vê anúncio no Meta → clica → preenche formulário → 
> recebe ligação → visita loja → compra."

Isso é **processo de aquisição**, não jornada do cliente. O cliente não "preenche formulário". 
Ele "tenta entender se vale a pena dar dados pessoais para uma empresa que não conhece".

### 7.2 Teste de Diferenciação

Para cada etapa que você desenhou, pergunte:

| Pergunta | Se a resposta for "sim" | O que isso significa |
|----------|------------------------|---------------------|
| Esta etapa descreve uma ação DA EMPRESA? | Sim | É processo, não jornada. |
| Esta etapa descreve um canal específico? | Sim | É canal, não jornada. |
| Esta etapa descreve uma EMOÇÃO ou DECISÃO do cliente? | Sim | É jornada. |

**Regra de ouro:** Se mais de 50% das etapas do seu mapa descrevem ações da empresa, 
você mapeou o processo interno. Jogue fora e recomece do lado do cliente.

---

## 8. Fase 6: Jornada Fragmentada e Atribuição Multi-Touch

### 8.1 O Problema

Cliente vê anúncio no Instagram no celular → pesquisa no Google no trabalho → 
recebe email no desktop → compra na loja física.

Sem atribuição multi-touch, você acha que a venda veio da loja. Veio do Instagram.

### 8.2 Mapeamento de Jornada Fragmentada

Para cada venda, pergunte (na entrevista ou no pós-venda):
- "Onde você NOS VIU pela primeira vez?" (awareness)
- "Onde você nos PESQUISOU?" (consideração)
- "Onde você DECIDIU comprar?" (decisão)
- "Onde você EFETIVAMENTE comprou?" (conversão)

**Regra de ouro:** Se a resposta para as 4 perguntas for diferente, sua jornada é fragmentada. 
Você precisa de atribuição multi-touch, não last-click.

### 8.3 Janela de Conversão

Defina a janela de atribuição para sua jornada:
- **B2C impulsivo** (varejo, restaurante): 7 dias
- **B2C considerado** (carro, imóvel): 30-60 dias
- **B2B** (SaaS, serviços): 90-180 dias

**Regra de ouro:** Se sua janela de atribuição for menor que o ciclo real de decisão do cliente, 
você está sub-atribuindo canais de topo de funil (awareness) e super-atribuindo canais de fundo (conversão).

**Regra obrigatória:** TODO relatório deve declarar a janela de conversão recomendada e a justificativa 
em 1 linha. Relatório sem janela declarada está incompleto — item bloqueante na autovalidação (seção 14).

---

## 9. Fase 7: Conectando Jornada com North Star

### 9.1 Cada Momento de Verdade vira Driver

A jornada invisível não é mapa de parede. É **input para a North Star**.

| Momento de Verdade | Driver na North Star | KPI | Meta |
|-------------------|---------------------|-----|------|
| Cliente compara com concorrente (invisível) | Aquisição Qualificada | Taxa de conversão vs concorrente | ≥70% |
| Primeiro atendimento pós-venda | Retenção | Tempo até primeiro contato | ≤24h |
| Problema resolvido surpreendentemente | Retenção | NPS pós-recuperação | ≥80 |
| Indicação espontânea no WhatsApp | Expansão | Taxa de indicação/100 vendas | ≥15 |

**Regra de ouro:** Se um momento de verdade não conecta com nenhum driver da North Star, 
ele é interessante, mas não prioritário. Growth investe no que move métrica, não no que é curioso.

### 9.2 Exporte para North Star Architect

Use a skill `north-star-architect` para transformar momentos de verdade em:
- Drivers de retenção (momentos pós-venda)
- Drivers de aquisição (momentos de descoberta e consideração)
- Drivers de expansão (momentos de indicação e upsell)

**Regra de ouro:** Jornada sem North Star é mapa sem destino. North Star sem jornada é destino sem estrada.

---

## 10. Fase 8: Experimentação Rápida (Growth em velocidade)

### 10.1 Não mapeie por 3 meses. Teste em 48h.

| Hipótese | Teste | Métrica de sucesso | Tempo | Custo |
|----------|-------|---------------------|-------|-------|
| "Formulário longo gera abandono" | Reduzir de 12 para 4 campos | Taxa de conversão do formulário | 7 dias | €0 |
| "Demora no follow-up perde cliente" | Ligação em 2h vs 24h | Taxa de conversão lead → proposta | 7 dias | €0 |
| "Garantia não clara gera dúvida" | Adicionar badge de garantia na landing | Taxa de scroll até CTA | 7 dias | €0 |
| "Indicação no WhatsApp funciona" | Botão de "indicar amigo" no pós-venda | Número de indicações/mês | 14 dias | €500 |

**Regra de ouro:** Teste A/B de jornada é mais barato e mais rápido que mapeamento completo. 
Growth aprende testando, não desenhando.

### 10.2 Protocolo de Experimento

1. **Hipótese:** formato obrigatório "Se [mudança], então [resultado], porque [raciocínio]". 
   Hipótese sem o "porque" não entra no plano — é palpite, não hipótese.
2. **Amostra:** mínimo 100 usuários por variação (ou 30% do tráfego, o que for maior). 
   **Gate de amostra:** se a amostra planejada for < 100 por variação, o teste DEVE ser marcado 
   como **DIRECTIONAL** (evidência direcional, não conclusão), com uma das 3 saídas: 
   estender prazo até atingir amostra, fundir variações, ou declarar limitação no relatório. 
   Nunca apresentar teste subdimensionado como teste padrão. **Sem exceção:** o gate vale para 
   TODO teste da tabela, inclusive o primeiro — ordem de prioridade não isenta marcação.
3. **Métrica principal:** 1 número que decide sucesso ou falha.
4. **Métrica secundária:** 2 números que explicam o porquê.
5. **Prazo:** máx 14 dias. Se não tem resultado em 14 dias, a mudança é muito pequena ou a métrica é errada. 
   Prazo maior que 14 dias exige justificativa explícita (ex: ciclo de entrega física).
6. **Decisão:** se melhoria > 10% e significância estatística > 95%, implementar. Se não, próxima hipótese. 
   **Este critério de decisão deve aparecer em todo plano de teste** — plano sem critério 
   de decisão declarado é experimento sem dono.

---

## 11. Fase 9: Síntese e Plano de Ação

### 11.1 Mapa Final da Jornada Invisível

O entregável final deve conter:

1. **Jornada Visível** (o que você já sabia) — em cinza, para referência.
2. **Jornada Invisível** (o que você descobriu) — em destaque, com ícones de alerta.
3. **Momentos de Verdade** (3-5 no máximo) — em destaque máximo, com emoção e KPI associado.
4. **Momentos de Recuperação** (protocolo de CS) — com script e autorização de frontline.
5. **Atritos Priorizados** (Atrito 1 e 4) — com dono, esforço, dependências e data de teste.
6. **Oportunidades** — com estimativa de impacto (clientes × valor × custo × ROI).
7. **Experimentos em andamento** — hipótese, teste, métrica, prazo.

### 11.2 Formato de Entrega

**NÃO entregue:** fluxograma bonito com 20 etapas e setas coloridas.
**ENTREGUE:** tabela com emoção, decisão, KPI e ação para cada momento crítico.

| Etapa | Touchpoint Visível | Touchpoint Invisível | Emoção | Decisão | KPI | Ação Prioritária | Dono | Teste A/B | Prazo |
|-------|-------------------|---------------------|--------|---------|-----|-----------------|------|-----------|-------|
| Consideração | Recebe proposta | Compara com 2 concorrentes | Ansiedade | Avança se preço for competitivo | Taxa conversão: ≥28% | Criar comparativo transparente no site | Marketing | Landing com/sem comparativo | 7 dias |
| Pós-venda | Recebe carro | Lembra de atraso anterior | Desconfiança | Não indica amigos | Indicações/100: ≥15 | Ligar em 7 dias para verificar satisfação | CS | Script de recovery | 7 dias |
| Recuperação | Problema resolvido | Recebe upgrade grátis | Surpresa + gratidão | Vira promotor | NPS pós-recovery: ≥80 | Criar protocolo de upgrade para erros | CS | Oferta recovery | 14 dias |

### 11.3 Próxima Ação

Sempre termine com:
> **"Próxima ação: [ação concreta] até [data] por [dono]. Teste A/B: [hipótese] em [prazo]."**

Se não consegue definir isso, o mapeamento está incompleto.

**Regra de validação temporal (obrigatória):** declare a data da análise no cabeçalho do relatório 
e derive TODAS as datas dela: `data do prazo = data da análise + prazo do teste/ação`. 
**NUNCA** entregar data de prazo anterior à data da análise. Prazo no passado é erro bloqueante —
item da autovalidação (seção 14).

**Regra de prazo do mapa final:** prazo maior que 14 dias no mapa final exige a mesma justificativa 
explicita que prazo de teste (seção 10.2). Sem justificativa, o item é bloqueante.

---

## 12. Restrições e Anti-Padrões (o que NUNCA fazer)

- **PREFIRA** dados quantitativos + entrevistas. Não um ou outro. Os dois são necessários.
- **PREFIRA** testar em 48h a mapear por 3 meses. Growth aprende iterando.
- **PREFIRA** 3 entrevistas profundas a 20 entrevistas rasas. Qualidade > quantidade.
- **NUNCA** confunda canal com jornada. "Meta Ads" é canal. "Cliente descobre que precisa de carro" é jornada.
- **NUNCA** confunda processo com jornada. "Vendedor liga em 24h" é processo. "Cliente espera ser lembrado" é jornada.
- **NUNCA** ignore touchpoints invisíveis só porque você não tem dados. Dados ausentes ≠ inexistência.
- **NUNCA** crie mapa com mais de 5 momentos de verdade. Se tem 15, você está confundindo touchpoint com momento crítico.
- **NUNCA** priorize atrito de baixo impacto só porque é fácil de resolver. Isso é procrastinação com cara de produtividade.
- **NUNCA** entregue mapa sem ação prioritária e teste A/B. Mapa sem ação é arte, não estratégia.
- **NUNCA** assuma que a jornada do cliente B2B é igual à do B2C. B2B tem múltiplos decisores, ciclos longos, e risco de carreira.
- **NUNCA** ignore a jornada pós-venda. É onde a lealdade é construída — e onde o churn começa (dia 3, não mês 6).
- **NUNCA** faça mapeamento sem consentimento LGPD/GDPR. Dados de comportamento são dados pessoais.
- **NUNCA** deixe momento de verdade sem KPI associado. Sem número, é curiosidade, não growth.
- **NUNCA** ignore o momento de recuperação. É mais poderoso que o momento de magia.

---

## 13. Exemplos de Ativação (quando usar esta skill)

- "Meu funil tem 45% de abandono no formulário. O que está acontecendo?"
- "Clientes elogiam o atendimento, mas não indicam amigos. Por quê?"
- "Quero mapear a jornada real do meu cliente de stand de veículos."
- "Nosso processo de venda parece perfeito, mas a conversão caiu 20%."
- "Como diferencio jornada, processo e canal no meu negócio?"
- "Onde estão os momentos de verdade que definem se o cliente fica ou vai?"
- "Meu concorrente tem pior atendimento, mas vende mais. O que eu não estou vendo?"
- "Como uso dados e IA para amplificar insights da jornada do cliente?"
- "Como conecto a jornada do cliente com minha North Star?"
- "Como testo mudanças na jornada sem esperar 3 meses de mapeamento?"

---

## 14. Autovalidação Final (obrigatória, em 2 passes)

### 14.1 Passo 1 — Validação determinística (script)

Antes de entregar, execute o validador a partir da raiz da skill:

```bash
# Linux / macOS / Hermes
python3 scripts/validar_relatorio.py <relatorio.md>

# Windows / Kimi CLI / Claude Code
python scripts/validar_relatorio.py <relatorio.md>
```

O script verifica de forma determinística: datas vs data da análise, aritmética da conversão
acumulada (nominal vs efetiva), fechamento do funil, divergências calc vs oficial em etapas
obrigatórias, marcação DIRECTIONAL por amostra, prazos > 14 dias e taxonomia dos 5 tipos.

**Qualquer FAIL do script = relatório bloqueado.** Corrija e rode de novo até PASS.
WARN exige justificativa escrita no relatório. Não edite o script para passar — edite o relatório.

### 14.2 Passo 2 — Checklist com evidência

Cada item exige **evidência citável** (tabela, linha ou valor do relatório) ao lado do [x].
**[x] sem evidência = item reprovado.** Checklist não é formulário para preencher — é auditoria
para provar. Um item sem prova = voltar e corrigir antes de entregar. Sem exceção.

- [ ] **Datas:** evidência = data da análise + menor e maior prazo do relatório
- [ ] **Funil:** evidência = a conta da conversão acumulada, etapa por etapa (ex: "43−21=22, tabela 1.2 calc")
- [ ] **Sobrevivência:** evidência = % de abandono por etapa, ou declaração de não-aplicável com motivo
- [ ] **Discrepâncias:** evidência = lista de TODAS as divergências calc vs oficial e o veredito de cada uma
- [ ] **Amostra:** evidência = a amostra de CADA teste listada individualmente, com marcação DIRECTIONAL onde n < 100
- [ ] **Taxonomia:** evidência = os 5 tipos usados, ou a declaração de extensão
- [ ] **Matriz de atritos:** evidência = 1 atrito exemplo com os 4 campos preenchidos
- [ ] **Janela de conversão:** evidência = valor + justificativa de 1 linha
- [ ] **Hipóteses:** evidência = 1 hipótese colada verbatim mostrando Se/então/porque
- [ ] **Critério de decisão:** evidência = o critério de 1 teste padrão (não-DIRECTIONAL)
- [ ] **Momentos de verdade:** evidência = contagem (máx 5) + KPI de cada um
- [ ] **Próxima ação:** evidência = a frase final colada verbatim

**Regra de ouro:** a skill não confia na própria memória. Todo relatório passa por auditoria
antes de sair — porque número errado com cara de certo destrói mais valor do que relatório nenhum.
E checklist sem evidência é teatro de compliance.
