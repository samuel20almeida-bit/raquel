# Site — Raquel Niejelski

Site institucional de página única, em HTML/CSS puro. Sem build, sem dependências,
sem framework: é só abrir `index.html` no navegador.

```
site-raquel/
├─ index.html                      ← todo o conteúdo e os textos
├─ css/style.css                   ← estilos e paleta (tokens no topo do arquivo)
└─ assets/
   ├─ padrao.svg                   ← padrão botânico (gerado, sem emendas)
   ├─ retrato-placeholder.svg      ← imagem temporária até a foto entrar
   └─ raquel.jpg                   ← ⚠ VOCÊ PRECISA ADICIONAR
```

---

## ⚠ Antes de publicar — o que trocar

Tudo que precisa de dado real está marcado com `<!-- TROCAR -->` no `index.html`.
Enquanto não forem preenchidos, o site mostra dados fictícios óbvios.

### ✅ Já preenchido

| O que | Valor |
|---|---|
| CRP | 08/45090 |
| WhatsApp | (41) 98821-8155 — nos 5 CTAs |
| E-mail | Raquel.aparecida.psi@gmail.com |
| Instagram | @raquel.niejelski.psique |
| Foto | `assets/raquel.jpg` |

### Auditoria de UX — situação

Dos 16 problemas mapeados, **13 estão fechados**. Os 3 restantes dependem de
informação que só a Raquel tem (ver tabela abaixo).

Fechados: links de WhatsApp mortos · CRP falso · e-mail e Instagram
fictícios · citação com 84 caracteres por linha · fontes carregadas em
cascata serial por `@import` · falta de `scroll-margin-top` · menu sem
seção ativa · `<br>` forçado em títulos · duas citações do mesmo autor ·
coluna dos passos com 32 caracteres · rótulos de CTA inconsistentes ·
rótulo que perguntava e título que não respondia · CTA secundário vago ·
nota do hero repetindo a FAQ.

### ✅ Nenhum placeholder restante

Formação (FAE), pós-graduação (PUC-PR), abordagem (Logoterapia) e público
atendido estão preenchidos.

Sobre o **valor da sessão**: a FAQ não publica o número. A resposta diz que
a Raquel combina no primeiro contato pelo WhatsApp, o que é uma escolha
legítima e comum na área. Se ela preferir publicar, é só trocar o texto
daquela pergunta (procure por `TROCAR` no `index.html`).

---

## Sobre a escrita

A copy foi revisada para não soar gerada por IA. Os padrões que foram
removidos, com a medição antes e depois:

| Marca | Antes | Depois |
|---|---|---|
| Travessões (`—`) | 13, um a cada 52 palavras | 2, só nas atribuições das citações |
| Tricolon com anáfora | "sem X, sem Y, sem Z" | nenhum |
| "não é X, é Y" | presente | nenhum |
| Vocabulário-clichê | "profundidade", "sem julgamento", "espaço reservado" | nenhum |
| Variação de frase | — | 3 a 41 palavras, desvio 6,6 |

Também foi corrigido o **feminino genérico** ("seguirmos juntas", "seja bem
cuidada"). A Raquel atende pessoas LGBTQIA+, e concordância no feminino
exclui parte desse público. O texto agora é neutro.

**Ao editar textos daqui pra frente**, os hábitos que mais entregam escrita
de IA: travessão no lugar de vírgula ou ponto, listas de três itens onde
dois bastariam, frases espelhadas do tipo "não é A, é B", e todas as frases
com o mesmo comprimento. Frase curta seguida de frase longa soa humano;
ritmo regular soa automático.

### A foto ✅ já está no lugar

`assets/raquel.jpg` — 1200×1543, 251 KB. O original de 3.3 MB ficou guardado
como `assets/raquel-original.jpg` (não precisa publicar esse).

> ⚠ **Se for trocar a foto um dia, cuidado com a extensão dobrada.** O Windows
> esconde extensões conhecidas por padrão: você vê "raquel", digita
> "raquel.jpg" ao salvar e o arquivo vira **`raquel.jpg.jpg`** — o site não
> acha e cai no placeholder. Para evitar: no Explorer, aba *Exibir* → marque
> *Extensões de nomes de arquivos*.

Para otimizar uma foto nova (redimensiona, comprime e faz backup do original):

```bash
python scripts/otimiza_foto.py assets/raquel.jpg
```

A foto atual tem proporção 0,778 contra 0,800 do arco, então só 2,7% é cortado
— ela aparece praticamente inteira. Se quiserem um enquadramento mais próximo
do rosto, há duas linhas comentadas em `css/style.css` (busque por
`transform: scale`) que fazem esse zoom.

Se o arquivo sumir, aparece um placeholder botânico em vez de imagem quebrada —
é o que o `onerror=` no HTML faz.

---

## Como publicar

Qualquer hospedagem de site estático serve, e todas têm plano grátis:

- **Netlify Drop** — https://app.netlify.com/drop · arraste a pasta inteira, sai no ar em segundos
- **Vercel** ou **Cloudflare Pages** — mesma ideia
- **GitHub Pages** — se quiser versionar

Para domínio próprio (ex. `raquelniejelski.com.br`), registre em registro.br e
aponte para a hospedagem escolhida.

---

## Decisões de design

Estrutura calcada em `brunobonato.com.br`, medida no site dele e reproduzida
aqui com a identidade da Raquel (paleta verde + padrão botânico).

### A estrutura das seções

| # | Seção | Fundo | Detalhe |
|---|---|---|---|
| 1 | **Hero** | `g700` + padrão full-bleed | 700px de altura, título 68px **centralizado** |
| 2 | Faixa de citação | `g900` | fina (~95px), **1 linha**, atribuição na mesma linha |
| 3 | É pra você? | `g700` | título 48px à esquerda, 6 cards em 3+3 |
| 4 | Faixa de citação | `g600` | ~185px, 2 linhas — **o verde da referência** |
| 5 | Sobre | `g800` | foto retangular (550×716) + texto |
| 6 | Como funciona | `g700` | 4 passos numerados |
| 7 | A abordagem | `g900` | 6 pilares **numerados "01."** em 24px |
| 8 | Dúvidas | `g800` | container estreito **600px**, centralizado |
| 9 | Chamada final | `g700` | container **720px**, título 58px |
| 10 | Rodapé | `g900` | |

O ritmo é o ponto: as **faixas finas de citação** cortando a página entre as
seções grandes são a assinatura do site de referência. São respiros de uma ou
duas linhas, não blocos altos — por isso a atribuição fica na mesma linha da
citação, e não embaixo.

A ordem também é intencional: **"É pra você?" vem antes de "Sobre"**. O leitor
se reconhece na dor primeiro, e só depois conhece a profissional.

Medidas conferidas contra a referência: container 1170px, título de seção 48px,
hero 68px, botão em pílula (raio 100px) de 18px em caixa normal, seções com
~100px acima e abaixo.

**Tipografia**
- `Sorts Mill Goudy` — títulos e corpo. Serifa old-style, peso 400 em tudo
  (nunca negrito), entrelinha justa nos títulos. É ela que dá o ar literário.
- `Jost` — apenas rótulos, menu e botões, em caixa alta com espaçamento largo.

### Escala modular — razão 1.2, ancorada no corpo

Havia 13 tamanhos escolhidos um a um, com razões entre degraus variando de
**1.06 a 1.39** — ou seja, escala nenhuma. Agora todo tamanho sai destes
tokens (`--fs-*` no topo do CSS):

| Token | px | Onde |
|---|---|---|
| `--fs-2xs` | 11,0 | rótulos do rodapé |
| `--fs-xs` | 13,2 | menu, eyebrow |
| `--fs-sm` | 15,8 | texto de card |
| `--fs-md` | **19,0** | **corpo — âncora da escala** |
| `--fs-lg` | 22,8 | lead, título de card, botão |
| `--fs-xl` | 27,4 | citação menor |
| `--fs-2xl` | 32,8 | citação maior |
| `--fs-3xl` | 47,3 | título de seção |
| `--fs-4xl` | 56,7 | título da chamada final |
| `--fs-5xl` | 68,0 | título do hero |

Medido na página: **10 tamanhos**, com razões entre degraus vizinhos de
**1,197 a 1,203** — mais um salto de 1,44 entre a citação maior e o título
de seção, que é exatamente 1,2² (dois degraus). Todo intervalo é uma
potência da mesma razão.

**Entrelinha por papel:** `--lh-display` 1.05 · `--lh-titulo` 1.28 ·
`--lh-corpo` 1.72. Antes doze títulos herdavam a entrelinha do corpo e um
`h3` de 21px ficava com 37px entre linhas, parecendo parágrafo.

### Espaçamento base 8

Todo valor de `padding`, `margin` e `gap` é múltiplo de 8px. Havia
30/56/100/128 e gaps de 20/24/40/64 sem base comum.

### Profundidade por luz

Em paleta escura a sombra preta quase não aparece. O volume vem de um
**fio claro de 1px na aresta superior** (`inset 0 1px 0`), simulando luz
vindo de cima, somado a uma sombra difusa que apoia a peça no fundo. O
retrato ganha também um halo dourado radial atrás.

> ⚠️ `.portrait-wrap` tem `z-index: 0` de propósito. Sem esse contexto de
> empilhamento, o `::after` de z-index negativo é pintado **antes** dos
> fundos das seções (ordem de pintura do CSS) e a moldura deslocada
> simplesmente não aparece.

> ⚠️ A revelação no scroll usa `animation`, não `transition`. A versão
> anterior declarava `transition` em `.reveal` e, por ter especificidade
> maior que `.card`, substituía o shorthand inteiro do componente — o hover
> do card perdia a animação de borda e ficava em 0,55s. Também **não** usa
> `forwards`: com fill-mode a última keyframe travaria o `transform` e o
> `translateY(-3px)` do hover pararia de funcionar.

**Paleta VERDE** — superfícies escuras com texto claro. A escala nasceu do verde
da faixa de citação (`--g600`), que virou a cor oficial do site.

### Por que existe uma superfície clara

A versão anterior era **99% escura** e as **727 palavras do site eram lidas
sobre fundo escuro**. Isso não é monotonia — é fadiga. Texto claro sobre
fundo escuro causa *halação* (a letra parece sangrar no fundo), tolerável
num hero ou numa faixa curta, mas não ao longo de 9.100px.

A solução foi introduzir **uma** superfície clara de areia para as duas
seções de leitura mais pesada, sem inverter o site. Resultado medido:
**28% da página em superfície clara**, com **269 das 727 palavras** lidas
em fundo claro, e as 9 transições entre seções todas perceptíveis.

Superfícies:

| Token | Hex | Matiz | Lum | Uso |
|---|---|---|---|---|
| `--ink` | `#141C10` | 100° | 9% | rodapé, abordagem, faixa de citação 1 |
| `--g800` | `#22301B` | 100° | 15% | reserva |
| `--g700` | `#38502C` | 100° | 24% | superfície principal |
| `--g600` | `#4F6B3D` | 97° | 33% | faixa de citação 2 — **o verde da referência** |
| `--warm` | `#2E2A18` | **49°** | 14% | seção Sobre — **quebra de matiz** |
| `--warm-2` | `#3A3420` | **46°** | 18% | chamada final — **quebra de matiz** |
| `--g500` | `#5F7F49` | 97° | 44% | ⚠ **só borda** — reprova com qualquer texto |

### Por que existem duas superfícies oliva

A primeira versão desta paleta usava só verdes, e ficou monótona: **97% da
página escura, todos os matizes entre 97° e 104°, luminosidade presa entre 15%
e 33%**. Quatro das nove transições entre seções eram imperceptíveis (contraste
abaixo de 1,5) — na prática, uma cor só do começo ao fim.

Clarear não resolvia: verde mais claro que `#5F7F49` reprova em contraste com
qualquer cor de texto. A saída foi **variar o matiz**: duas superfícies oliva
quentes (46–49°) cortam a sequência de verdes. O oliva ainda conversa com a luz
dourada da foto da Raquel.

Resultado medido: transições fracas caíram de **4/9 para 1/9**, e a única que
sobrou é a entrada da faixa verde — que se diferencia pela textura, já que ali o
padrão botânico vai a 22% de opacidade contra 12% do resto.

**Regra ao mexer nisso:** duas seções vizinhas precisam ter contraste ≥ 1,5
**ou** matizes separados por mais de 20°. Sem um dos dois, a troca não é
percebida e o site volta a parecer monocromático.

Texto e acentos, com o contraste medido:

| Token | Hex | Uso | Contraste |
|---|---|---|---|
| `--cream` | `#FBF6EA` | texto principal | 8.3:1 no g700 · 10.6:1 no g800 ✅ AAA |
| `--cream-2` | `#DCE3CD` | texto secundário | 6.8:1 no g700 · 8.6:1 no g800 ✅ |
| `--sage-pale` | `#C3D4A8` | terciário, títulos do rodapé | 5.7:1 no g700 ✅ AA |
| `--gold` | `#E0BC6B` | rótulos, números, ícones | 4.9:1 no g700 ✅ AA |
| `--coral` | `#E8845F` | fundo de botão (texto `--g900`) | 5.3:1 ✅ AA |

⚠ **Duas armadilhas desta paleta**, caso você mexa nas cores:

1. `--g500` (`#5F7F49`) é claro demais: **nenhuma** cor de texto passa em cima
   dele. Use só como borda.
2. Sobre `--g600` (o verde da faixa) só o `--cream` passa. O `--sage-pale` dá
   3.8:1 e reprova — por isso a assinatura "Carl Gustav Jung" é creme, e a
   hierarquia vem do tamanho e do espaçamento entre letras, não da cor.

Verificado na página renderizada: **0 falhas** de contraste, medindo cada
elemento de texto contra o fundo que ele realmente tem.

O padrão botânico (`assets/padrao.svg`) é **autoral**, gerado por script a partir
de curvas paramétricas — frondes, rosetas e íris nas cores das suas imagens.
Não é uma cópia do papel de parede original. Tileia sem emenda; 290 KB no disco,
~45 KB trafegados (SVG comprime muito bem).

**Acessibilidade** — verificado: sem rolagem horizontal em 375/768/1024/1440 px,
alvos de toque ≥ 44 px, foco visível no teclado, hierarquia de títulos correta
(1×h1, 6×h2, 16×h3), todas as imagens com `alt`, `prefers-reduced-motion`
respeitado. As animações de entrada só são aplicadas se o JS estiver rodando —
sem JS, a página aparece inteira normalmente.

---

## Ajustes rápidos

**Mudar cores** — edite os tokens no topo de `css/style.css`. Se mexer em cor de
texto, confira o contraste em https://webaim.org/resources/contrastchecker/

**Regerar o padrão** com outra densidade ou cores — o script está em
`scripts/gen_pattern.py`:

```bash
python scripts/gen_pattern.py assets/padrao.svg
```

**Mudar textos** — estão todos no `index.html`, em português, sem template engine.

---

## Nota sobre o conteúdo

Os textos são um ponto de partida que escrevi no tom do site de referência —
acolhedor, sem jargão e sem promessa de resultado. **Peça para a Raquel revisar
tudo antes de publicar**: a voz precisa ser dela, e há responsabilidade ética e
do CFP sobre como um psicólogo divulga o próprio trabalho (Resolução CFP nº
011/2018 trata da publicidade profissional).

Deixei no rodapé a referência ao CVV (188), que é boa prática em site de
psicologia.
