# Next.js: primeiro mergulho no framework - 8h
**Disponível:** [ALURA]('https://cursos.alura.com.br/course/next-js-iniciando-framework')
**Professor:** Mario Souto
**Conteúdo:**
- Reconheça os benefícios do Next.js
- Entenda como o Next.js ajuda no SEO de seu site
- Implemente estilizar sua aplicação Next.js
- Investigue como o Next.js busca dados estáticos e dinâmicos
- Crie seu projeto na Vercel

## 1. Conhecendo Next.js Ver primeiro vídeo
### Apresentação

[00:00] Eu sou Mario Souto e seja bem-vindo a esse curso especial, em parceria com o canal DevSoutinho e a Alura, para trazer conteúdo de Next.js para vocês.

[00:09] A ideia aqui é abordarmos essa ferramenta que tem se tornado cada vez mais popular e que tem sido cada vez mais ousada.

[00:16] O Next.js é um framework que roda em cima do React, ou seja, ele vai nos ajudar a trabalhar melhor com o React, vai ajudar a resolver problemas de SEO, de performance, web virus, várias coisas, várias palavras que têm surgido bastante e que vamos abordar aqui no curso.

[00:31] E vamos falar também dessa questão de onde usar Next.js, quando usar. Cada vez mais ele se posiciona como o SDK da web, o kit de desenvolvimento da web.

[00:39] E para isso você vai, junto comigo, criar uma página promocional para essa feature aqui da Alura, o Alura Cases, que tem se tornado bastante popular e basicamente o site é esse aqui. Nós vamos criar esse site.

<img src="https://caelum-online-public.s3.amazonaws.com/2370-next-js-iniciando-framework/Transcri%C3%A7%C3%A3o/Aula+1/01.01_001_imagem1.png">

[00:51] Ele vai ter integração de scripts externos, teremos a parte de gerenciamento de CSS, carregar arquivos estáticos, vamos olhar algumas coisas de performance também. Tem bastante coisa para olharmos.

[01:02] E o projeto basicamente tem essas duas páginas aqui, mas tem muito conteúdo de Next.js para ajudar você a construir o seu próximo projeto com essa ferramenta. Bora codar junto?

### Preparando o ambiente: Windows

Para preparar o ambiente, precisaremos de algumas coisas instaladas no computador, são elas:

[Node.js/npm]('https://nodejs.org/pt-br/')

- Para instalar o Node, clique no link e baixe a versão LTS (versão recomendada).

<img src="https://caelum-online-public.s3.amazonaws.com/2370-next-js-iniciando-framework/01/aula1-imagem1.png">
_alt text: site do Nodejs, com o botão da versão recomendada em foco por um quadrado vermelho!_

- Para verificar se foi instalado corretamente, abra o terminal e escreva node -v ou node --version.

#### Git

- Caso não tenha um terminal de preferência, recomendo utilizar o git bash que é o utilizado neste curso. Para instalá-lo, haverá uma opção durante a instalação do git para permitir instalar o git bash.

<img src="https://caelum-online-public.s3.amazonaws.com/2370-next-js-iniciando-framework/01/aula1-imagem2.png">
alt text: Select Components. A caixa “Git Bash Here”  está em evidência por um quadrado vermelho

- Para verificar se o git foi instalado corretamente, abra o terminal e escreva git --version.

#### Visual Studio Code

- [Entre no link]('https://code.visualstudio.com/download') e baixe a versão de Windows.

### Preparando o ambiente: Linux

Para preparar o ambiente, precisamos de algumas coisas instaladas no computador, são elas:

#### Nodejs

- Para instalar o Node, abra o terminal e digite:
    
        sudo apt install nodejs

- Para conferir se o download ocorreu corretamente, digite:
    
        node -v ou node --version

#### Git

- Para instalar o git, abra o terminal e digite:

        sudo apt install git-all

- Para conferir se o download ocorreu corretamente, digite:

        git --version.

#### Visual Studio Code

[Entre no link]('https://code.visualstudio.com/download') e baixe a versão de Linux.

### Preparando o ambiente: Mac

#### Homebrew
Para preparar o ambiente, precisamos de alguns programas instalados no computador e, para isso, utilizaremos um controle de pacotes para mac super útil chamado Homebrew. Caso não tenha ele instalado, só [clicar no link]('https://brew.sh/index_pt-br') e seguir o comando que ele descreve para o download. Após isso, faremos download das nossas dependências para rodar o projeto, sendo elas:

#### [Nodejs/npm]('https://nodejs.org/en/download/')

- Para instalar o Node na sua máquina, clique no link e baixe a versão LTS (versão recomendada).
- Para verificar se foi instalado corretamente, abra o terminal e escreva:
        node -v ou node --version

#### Git

- Para instalar o git, abra o terminal e digite:

        brew install git

- Para verificar se o git foi instalado corretamente, abra o terminal e escreva:

        git --version

#### Visual Studio Code

[Entre no link]('https://code.visualstudio.com/download') e baixe a versão de Mac.

### O que é e por que usar Next.js?

[00:00] Eu tenho certeza que você está ansiosíssimo para começar a escrever o seu primeiro código com o Next.js. Mas calma, que esse vídeo aqui é super importante para você conseguir conversar com o pessoal do seu trabalho, para você conseguir se aprofundar um pouco mais e entender os problemas que fizeram o Next.js existir.

[00:16] E para começarmos a falar disso, eu deixei aberta a documentação aqui de novo. Repara que eu tenho aqui aquela página que fala do Next querer ser o SDK da web, o kit de desenvolvimento.

[00:27] E eu acho que é impossível falar do Next.js sem falar de um dos criadores dele, o Guillermo Rauch, que é uma pessoa super popular no mundo Node.js, JavaScript. Ele participou da criação de várias libs super famosas, como o Mongoose, o Socket.IO, que é mais popular para quem trabalha com Node, mas estou falando aqui só para caso você tenha curiosidade e queira dar uma procurada.

[00:49] E hoje ele é dono da Vercel, que é a empresa por trás do Next. A Vercel é uma empresa de hosting. Inclusive, até o final desse curso, nós vamos hospedar o nosso site lá, você vai conseguir mandar o link para as pessoas, falar: “Olha o projeto bacana que eu fiz aqui no curso da Alura”.

[01:09] Esse é o contexto inicial dele, mas o que eu quero falar de verdade é sobre esse artigo dele aqui, que ele fez a sete anos atrás, que ele fala dos sete princípios para você ter aplicações web mais ricas.

[01:21] E o legal é como ele fala da questão de ter coisas de pre rendered, coisas de você reagir, relacionadas à mudança de dados, então você altera o campo num filtro e a página muda sem ficar tendo refresh.

[01:34] Esse artigo está em inglês, mas eu super recomendo que você tente colocar no Google tradutor se você não souber inglês, tentar ler, porque ele tem muito conteúdo rico mesmo, ele até faz parte do material extra dessa aula.

[01:46] E o que eu queria trazer aqui é que para web sempre temos que focar no usuário, e é muito difícil, porque ao passo que temos usuários usando o iPhone 11, tem pessoas usando um celular de 2014, um celular às vezes de, se olharmos aqui, sete anos atrás.

[02:01] E você tem que considerar que o processamento desse celular é um pouco mais limitado, que essa pessoa às vezes pode estar com o plano de dados limitado, nós nos acostumamos muito a acessar site de casa, de wi-fi e tudo mais.

[02:13] E existem várias complexidades quando falamos de web, que por mais que você seja um excelente programador ou programadora, vai ser muito difícil de resolver. E eu trouxe até um pouco prático, que é esse mapa aqui, para você conseguir visualizar um pouco melhor.

<img src="https://caelum-online-public.s3.amazonaws.com/2370-next-js-iniciando-framework/Transcri%C3%A7%C3%A3o/Aula+1/01.05_002_imagem2.png">

[02:28] Pensa que todo site que você acessa é um monte de arquivo, que está em algum computador do mundo, e que basicamente você está pedindo esses arquivos e baixando para você.

[02:38] No cenário ideal de performance, por exemplo, a própria Vercel tem suporte a isso, você consegue ter um servidor próximo do seu usuário. Você poderia ter um servidor aqui no Brasil e o conteúdo ia chegar super rápido para o seu usuário. Mas lembra que a distância é importante.

[02:53] Então quanto mais longe o conteúdo está do seu usuário no mundo, muitos sites ficam hospedados nos Estados Unidos, na região da Virgínia, é como se cada clique que você dá no seu site está baixando uma imagem que está lá nos Estados Unidos e está vindo para cá.

[03:07] Isso tudo vai vir na velocidade da luz, então, sei lá, uma ida e volta, jogando a conta por cima aqui agora, seriam 50 milissegundos ali. E esses 50 milissegundos são considerando se você tivesse um cabo de fibra ótica ligado no seu celular, lá no data center que você vai baixar a informação.

[03:26] Eu sei que parece um negócio meio ciência de foguete que eu estou falando aqui agora, mas pensa que nós não temos cenário perfeito, pensa que o seu celular está acessando uma rede 3G, que bate numa antena, que essa antena bate num cabo, que passa por debaixo do oceano. Tem muita complexidade para essa informação chegar aos nossos usuários e como alguém que trabalha com web, é importante pensar nisso.

[03:48] Existem várias estratégias para lidar com isso, como a parte de cache, como tentar diminuir o tamanho dos arquivos para eles trafegarem mais rápido, enfim. Alguns desses pontos eu vou trazer aqui, alguns outros pontos você já pode aprender aqui na Alura, no curso de Performance Web.

[04:03] Eu até recomendo que você faça esse curso de performance depois desse curso aqui de Next, porque vai ter muita coisa que você vai aprender a mais.

[04:10] E indo para algo mais prático, eu queria mostrar para vocês que uma das empresas que mais tem servidores, que o pessoal usa, é a Amazon.

[04:17] Essa imagem aqui tem um pouco da distribuição dos servidores deles, os data centers onde ficam guardados os arquivos. E essa questão da disponibilidade, conseguir servir o arquivo rápido, servir o arquivo menor possível, para gastar menos o plano de dados do usuário, para conseguir atender, é um dos pré-requisitos importantes que você sempre tem que ter em mente e que eu vou reforçar bastante ao longo das aulas.

[04:40] Se você está com um pouco de dúvida, fica tranquilo, que nas próximas aulas eu vou falar bastante dessa questão de arquivos, otimização e tudo mais.

[04:47] E lembra também que o Next.js já vai automatizar muita coisa. A ideia aqui do curso é ir fazendo essa tour com vocês, explicando o passo a passo e tudo mais. E isso vai nos levar para a questão que, além do nosso usuário, como nós conseguimos metrificar isso? Como conseguimos saber que está bom ou que está ruim?

[05:07] Eu gosto de dizer, até parafraseando o Sérgio Lopes, do curso de performance, que performance é UX, é usabilidade, então você tem que sentir que o site está bom, o projeto está bom.

[05:19] Eu tenho até uma coisa para pegar aqui. Eu tenho, inclusive, aqui em casa, um celular mais antigo, eu tenho um celular da Motorola, esses de 2014 que eu dei o exemplo ali, onde eu tento testar boa parte dos projetos que eu estou trabalhando, para ver se a experiência está boa, se alguém com um celular mais antigo consegue usar, se pelo 3G ele está bom. Claro que o navegador nos dá essas ferramentas, mas é super bacana também.

[05:43] E além de fazer esse teste em dispositivo real, eu gosto de usar também essas métricas que o próprio Google usa para ajudar no ranqueamento das páginas, para dizer se o seu site é lento ou se ele é rápido, que são essas três aqui. É o Largest Contentful Paint, o First Input Delay e o Cumulative Layout Shift.

[06:02] Eu não vou me aprofundar tanto nelas aqui, mas esse Largest Contentful Paint é quanto tempo demoraria para carregar a sua página, até um pouco mais que aquela primeira parte inicial, essa primeira dobra que o pessoal chama.

[06:13] Pensa como se o site fosse um jornal, então ele está dobrado e nós abrimos as outras páginas desse jornal, quando você está fazendo scroll. E essa primeira parte aqui, e mais um pouco, significa esse LCP aqui.

[06:26] Tem o First Input Delay, que é quanto tempo demora para você conseguir clicar em alguma coisa. Sabe quando você abre um site e ele já carregou, mas o botão fica inativo por um tempo? É uma das coisas que vamos abordar, que o Next.js nos ajuda a conseguirmos gerenciar também.

[06:41] E esse último é o Cumulative Layoyt Shift, que normalmente acontece em sites que têm muita propaganda, que eles ficam "popando" coisas, e o site vai se recalculando e crescendo. E você acha que o texto está num lugar ou o botão, e quando você clica, ele está embaixo.

[06:56] Aqui foram exemplos mais falando mesmo, nós vamos tentar trazer alguma coisa mais na prática. O ideal seria ter um curso só de web virus, mas aqui dá para abordarmos também.

[07:05] E eu estou falando isso tudo porque o modelo padrão que o React funciona é baseado em Client Side Rendering. “Como assim, Mario?”. Basicamente nós pedimos para o servidor dos cabos submarinos, que bate lá no servidor da Amazon, ele nos traz os arquivos que vamos usar.

[07:27] E nesse momento começam a agir essas coisas aqui do Google, porque o site vai ter que carregar rápido coisas de arquivos que você baixou, ele vai ter que permitir que o usuário digite rápido e ele não vai poder ficar dando essas popada

[07:39] Quando usamos só o React ou só o Client Side Rendering, nós caímos no problema que é o problema geral das single-page applications, das SPAs.

[07:47] Que é o seguinte, basicamente você tem o seu projeto, ele carrega, só que quanto mais JavaScript você carrega, mais tempo demora para o usuário ver alguma coisa desenhada na tela. O seu site fica carregando, fica aquela barra de carregamento. Depois que carrega, fica até rápido, mas a primeira vez que você carrega fica muito lento.

[08:07] E isso impacta diretamente nessa questão do Largest Contentful Paint e do First Input Delay, porque demora para o usuário conseguir ver alguma coisa, que é um dos motivos que o Google às vezes tem dificuldade de indexar páginas que estão usando o React, por exemplo, porque ele não tem nenhum conteúdo que está vindo do servidor pronto, ele só tem basicamente um loading e depois de alguns segundos ele mostra a página por si só.

[08:32] E você fica: “Mario, mas como nós resolvemos isso?”. Tem uma forma de fazer isso, que é tipo usando PHP, não é exatamente mudando para PHP, você não precisa mudar de tecnologia para resolver esse problema, mas é mudando quem renderiza a nossa aplicação. Vou até dar um zoom out aqui.

[08:48] Tirando essa responsabilidade do nosso client e jogando-a para o servidor, fazendo o tal do Server Side Rendering. Que é o que o PHP faz, que o Java faz, que o Closure faz, que todas as linguagens de back-end fazem por padrão quando pré-renderizam o HTML no servidor e mandam para o usuário.

[09:06] O Next vai nos ajudar a fazer esse modelo de navegação, onde o HTML inicial já vem carregado, que faz com que esse carregamento do CSS, do HTML, apareça mais rápido, e nós vamos tentar otimizar a parte do JavaScript, coisa que ele faz muito para nós também, para ter esse First Input Delay rápido. Estou usando só para contextualizar com vocês aqui.

[09:28] E ele vai baixar o HTML, CSS, JavaScript, vai adicionar os eventos do React na página, eu vou explicar essa parte também para vocês, e depois a página se torna interativa. Então basicamente ele pré-renderiza o HTML no servidor e adiciona o React nesse código, como se ele estivesse fazendo só adicionar os eventos de clique, de abrir botão e tudo mais.

[09:51] Nesse ponto aqui o Next.js vai nos ajudar bastante. E o mais legal de tudo é que ele nos ajuda a trabalhar das duas formas, tanto via Server Side quanto via Client Side, por quê? Quem já trabalhou com back-end ou alguma linguagem tipo PHP, sabe que existe muito custo de servidor para você manter essas aplicações rodando.

[10:15] E para quem trabalha com front, existe um conceito que eu vou abordar ainda, mas em outros tópicos aqui do curso, que é a tal da Jamstack, que basicamente é você ter o seu site estático, que para o nosso caso, que é um site de duas páginas, que ele vai ter basicamente a home e a parte do FAQ, não precisa ter tanto custo assim de servidor, então a Jamstack super se aplicaria.

[10:38] Porém, se quisermos ter essa parte do Server Render para alguma coisa que pode ter uma atualização mais dinâmica e tal, como se fosse uma loja, e ainda assim ter o cache e várias outras vantagens, o Next.js vai nos ajudar.

[10:51] E por esse vídeo é só, eu vou parar um pouco, para no próximo nós começarmos a ver para valer, criar o nosso projeto e começar um pouco mais de mão na massa. Até já.

### Iniciando o projeto

[Getting Started]('https://nextjs.org/docs/getting-started')

1. Iniciando meu projeto Next.JS. No terminal:

    yarn init -y

2. Após criar o arquvio PACKAGE.JSON podemos editar o nome do nosso projeto:

    {
        name: "alura-cases-divulgacao",
        ...
    }

3. Instalação das dependências necessárias no projeto:

    yarn add next react react-dom

4. Criando um .gitignore:

    npx gitignore node

5. Adicionar no PACKAGE.JSON:

        "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start",
        "lint": "next lint"
        }

6. Adicionar uma nova pasta no ROOT do projeto e depois um arquivo INDEX.JS:

    projeto
    |--pages
        |--index.js

7. No arquivo INDEX.JS:

        function HomePage() {
            return <div>Welcome to Next.js!</div>
        }

        export default HomePage

8. No terminal para rodar meu projeto:

        yarn dev

---

[00:00] Chegou a hora de começarmos a colocar a mão na massa e ver o nosso projeto aqui virar realidade, de começarmos a trabalhar em cima dele.

[00:09] Antes de mais nada, vamos abrir a documentação do Next.js e a minha ideia nesse curso é te dar autonomia, então vou tentar o máximo possível sempre usar a documentação e fazer o passo a passo para você aprender a fazer as suas próprias consultas.

[00:21] Para criarmos um projeto, o Next.js tem até uma parte de learn, aqui em cima, à direita, que tem uns quizzes aqui, que eu acho que você pode até usar para praticar e tudo mais. Mas por hora vamos na parte de “Docs” aqui em cima, à esquerda.

[00:31] E você vai ver que é tudo super bem documentado, é realmente muito bom, é um projeto que dá gosto de usar pelo quão bem feita que é a documentação.

[00:39] Mas se descermos a página aqui, ele tem essa parte de “Setup”. Você pode usar tanto o npm quanto o yarn. Eu vou usar o yarn por uma escolha pessoal e porque alguns exemplos que eu quero trazer de coisas mais avançadas, de estrutura, de setup e tal, usam yarn. Se você manja muito de npm, você pode usar também, mas eu vou optar pelo yarn aqui.

[01:00] E lembrando que se você não tiver o yarn na sua máquina, porque ele não vem por padrão quando instalamos o Node, só quem vem quando instalamos o Node é o npm, você pode rodar esse comando aqui, npm install --global yarn ou ver as outras formas de instalação que tem na própria documentação.

[01:16] Lembrando que eu vou usar a versão 1, só para deixar claro para você também. Então antes de fazer o nosso projeto, vamos criar.

[01:24] O Next aqui, repara que ele tem esse create-next-app. Isso é como se fosse um gerador de projeto, ele vai pegar um template base do Next e vai trazer para você. Esse template base é muito bom, ele tem até suporte para typescript, não só esse template base, mas o Next inteiro. Se você basicamente mudar extensão de .js para .ts, o Next já está dando suporte para typescript por padrão para você.

[01:49] Mas aqui vamos trabalhar com a versão em JavaScript, porque é mais fácil de conseguirmos trazer os exemplos e tudo mais, e você fica aberto, se você quiser fazer em typestrip, segue seu coração.

[01:59] Mas por hora, faremos esse “Manual Setup” aqui. Ao invés de usar esse gerador, faremos o setup manual e você vai ver que ele vai virar meio que aquele gerador ali, eu vou até dar uns exemplos depois do porquê, mas só para você ter um pouco mais de controle e entender que não é um bicho de sete cabeças.

[02:16] O Next foi feito para ser simples e para facilitar a nossa vida sem ter que ficar configurando aqueles arquivos de webpack, o que faz o build otimizado, não. O Next vai trazer para você a melhor otimização possível que eles conseguirem enquanto você foca em fazer as features do produto que você trabalha.

[02:36] Por hora eu vou copiar o comando para adicionar algumas bibliotecas que precisamos, o Next, o React e o React-dom, yarn add next react react-dom. E antes delas eu vou até inicializar esse repositório, então vou fazer um yarn init -y, que no npm seria npm init -y também.

[02:56] O -y é só para ele dar sim para tudo e eu só venho aqui e ajusto o nome do projeto, que o nosso vai ser a página de divulgação do Alura Cases. Então “alura-cases-divulgacao”. Salvei aqui.

[03:12] Com o nosso “package.json” criado, eu vou agora voltar na documentação e copiar de novo as libs, porque eu acabei me perdendo. Copiei, yarn add next react react-dom, vou colar e aparentemente está carregando aqui, vamos deixar rolar.

[03:33] Esse aqui é um bom momento para você tomar um café. Aqui foi até rápido, mais rápido do que eu esperava, inclusive. E agora o nosso arquivo “package.json” tem as dependências declaradas aqui, tanto o React quanto o React-dom quanto o Next.

[03:51] Para clarear para você, pensa que o React é o core do React, a lib principal do código do React. O React-dom faz a cola desse core do React, da parte do Virtual DOM com o navegador, e você poderia ter o React e o React Native para rodar no celular, por exemplo, ao invés de React-dom.

[04:07] E o Next vai atuar fazendo a parte de build para nós, toda a parte de build, de gerenciamento de rotas e muitas coisas aqui, ele vai fazer para nós com o framework.

[04:20] Só para garantir aqui, eu vou também criar um arquivo “.gitignore”, vou rodar um comando especial aqui, npx gitignore node. Isso, aqui. Agora está pronto, está só considerando esses três arquivos que mexemos, ou “.gitignore” ou “package.json” e o yarn.lock, que é um arquivo gerado para mapear as dependências aqui e tudo mais.

[04:50] Se viermos aqui no “package.json”, não tem nada, só tem as libs. Voltando na documentação, ele fala que podemos abrir o “package.json” e adicionar esses scripts aqui. Então eu vou copiar isso aqui tudo e vou colar dentro da parte de dependencies aqui no código. Colei. Tanto esse script de “dev”, de “build”, “start”, “lint”.

[05:13] Em teoria nós já poderíamos rodá-los, mas eu vou pedir para você segurar só um pouco, para evitarmos uns erros meio catastróficos.

[05:20] Os comandos são auto descritivos, o dev você usa em modo de Dev, o build para gerar a versão de produção do projeto, tem até umas variantes que eu vou mostrar para vocês também.

[05:29] Tem a parte do start, que é para você rodar quando estiver em produção. E esse lint, que é para te ajudar a fazer melhor algumas configurações do Next, que eles têm como padrões de convenções de código. Aqui ele fala, o suporte de JavaScript, jsx, typescript e tal.

[05:49] E antes de qualquer coisa, de rodarmos o Dev lá, eu queria chegar nessa parte aqui, por quê? O Next, diferente de libs como, por exemplo, o React Router DOM, que é uma lib super popular para quem trabalha com React, vou até dar um zoom maior aqui.

[06:06] Não somos nós que vamos controlar o roteamento com o código. Para fazer qualquer página no Next.js, tudo que você precisa fazer é basicamente criar uma pasta “pages” na raiz do seu projeto e eu gosto de brincar com essa pasta é do Next, ela não é sua, ela é uma pasta do Next para fazer as configurações dele e tudo mais.

[06:26] E aqui à esquerda eu vou botar um arquivo “index.js”. E aqui dentro, se só fizermos export default function HomePage() {, se dermos um return e eu botar uma <div><\div> com... o GitHub Copilot está ligado, eu vou até desligá-lo agora, enquanto fazemos aqui um <h1></h1> e botamos um Alura Cases - Home, só para termos nosso título aqui. Salvamos aqui.

[07:06] Se viermos no terminal agora, dentro da pasta do curso, “01-NEXTJS-COURSE” que eu estou, e eu rodar yarn dev, olha só, compilou com sucesso, levou alguns milissegundos, x módulos, tem esse telemetry aqui, eu vou basicamente abrir essa URL “http://localhost:300” no navegador agora, e já está aberto, já temos rodando um projeto com Next.js.

[07:40] Foi basicamente isso, nós basicamente criamos o “package.json”, criamos a pasta “pages” e já está funcionando. Repara que eu nem precisei fazer o import do React aqui, ele já trouxe tudo por padrão, foi só criar as coisas e já está rodando.

[07:55] E se eu apagar aqui, por exemplo, ou escrever alguma coisa a mais, <h1>Alura Cases - Home Page</h1>, ele já tem o suporte do LiveReload, ele já atualiza as coisas, Hot Module Replacement, todos esses nomes bonitos para falar que ele tem automatizado o processo de recarregar pedaços da página ou a página inteira, já é por padrão, você não precisa configurar nada, está pronto para pegarmos e usarmos.

[08:19] Uma vez que já estejamos nessa parte aqui, você pode ver que faltam algumas coisas para conseguirmos deixar a nossa página mais bonita, tem a parte de CSS, tem a parte de fazer link para outra página.

[08:33] Mas repara que nós conseguimos fazer isso aqui, porque já é um código React. Então basicamente, se eu vier aqui no código e botar um link, `<a>`Ir para o FAQ</`a>, `a parte de perguntas, e botarmos um < a hre`f=“/f`aq”>, se clicarmos, ele cai` na página 404`. Lembrando que` voc`ê pode sobrescrever essa página, eu vou te mostra`r já já.

[0`9:03] Ele deu página não encontrada, por quê? Porque no nosso diretório pages não existe a página do FAQ. Se eu vier aqui à esquerda e criar um novo arquivo “faq.js”, export default function FAQPage() {, eu estou chamando de page aqui por uma convenção pessoal, mas você pode chamar do nome que você quiser, você pode chamar só de PaginaDePerguntas, não tem nenhuma restrição de idioma nem nada, está tudo tranquilo.

[09:33] Aqui agora eu vou fazer um return e vou copiar a mesma estrutura que temos aqui, essa `<div>` com `<h1>` e o `<a>`. Aqui temos o `<h1>`Alura Cases - Página de Perguntas FAQ`</h1>` e aqui na linha de baixo, `<a href=“/faq”>` Ir para a home`</a>`. E agora eu posso vir aqui e ajustar esse link, `<a href=“/”>`. Agora criamos duas páginas, o FAQ e a nossa home page.

[10:11] Quando eu carregar aqui, agora o FAQ deixou de ser uma página 404, mudou até rápido, não dá nem para vermos aqui, mas voltei para a home, “Home Page”, “Ir para o FAQ”, página do FAQ e já está funcionando, já temos navegação funcionando sem precisar configurar nada que o React Router teria. O próprio Next já abstrai para nós essa configuração.

[10:34] E fica tranquilo, se você precisar fazer rotas autenticadas e tudo mais, eu vou deixar vários materiais extras e vão ter outros cursos aqui na Alura focando especificamente nessa parte. Esse curso em específico é mais uma introdução geral, mas que é super importante você conseguir ter autonomia na hora de criar seus projetos.

[10:49] E uma coisa que eu já quero deixar claro para você que está aqui assistindo, é prestar atenção em alguns detalhes, porque o Next.js, a vantagem dele está nos detalhes. Por exemplo, quando eu estou aqui na página, “Ir para a home” e “Ir para o FAQ”, ele está sempre baixando todos os arquivos de novo.

[11:06] Se eu abrir aqui à direita a aba “Network” do navegador e carregar a página, eu vou limpar tudo aqui, aqui ele já baixou o FAQ, mas se eu for para a home, ele baixa tudo de novo, e se eu vou pagar o FAQ, baixa tudo de novo do FAQ, vários arquivos JavaScript ele está baixando de novo.

[11:24] Se eu abrir num projeto que já está pronto aqui, dar um “Inspect”, e olhar na parte de “Network”, então carreguei uma vez e limpei.

[11:35] Quando vamos para o FAQ, ele só baixa um arquivo, porque isso aqui, ele está usando o modelo de navegação SPA, e se eu navego de volta entre as páginas, ele não baixa mais nada, ele só está baixando no máximo o logo aqui e tal, porque eu dei um refresh. Mas ele não está tendo esse recarregamento da página e é isso que faremos no próximo vídeo.

### Para saber mais: Yarn

Se você está acostumado a utilizar o NPM como gerenciador de pacotes, deve estar se perguntando:

Preciso mesmo utilizar o Yarn?

Não! Apesar do Yarn ter nascido para solucionar os problemas do NPM, hoje em dia, o gerenciador de pacotes tradicional do Node já evoluiu bastante e a diferença de performance e segurança entre os dois está menor.

Durante o curso, o Yarn foi escolhido por preferência do instrutor. Para instalá-lo, basta executar o seguinte comando no terminal:

        npm install -g yarn

Depois, execute o comando para verificar se a instalação ocorreu corretamente:

        yarn -version

Também temos o artigo NPM vs Yarn caso você queira ver mais a fundo as particularidades de cada um.

### Componente Link do Next.js

[NextJS - Link]('https://nextjs.org/docs/api-reference/next/link')

1. Na INDEX.JS vamos importar os links:

    import Link from 'next/link'

2. Criamons no ROOT do projeto uma pasta SRC/COMPONENTS:
- Esta página serve para definirmos nossos componentes JS uma boa prática.
- E criamos uma função LINK para facilitar a utilização de links.

---

[00:00] Agora que já temos a nossa primeira página criada, na verdade, as duas primeiras, temos o FAQ e temos a nossa home, já conseguimos navegar entre elas, faltou fazermos esse lance da navegação no modelo SPA, sem termos que ficar recarregando tudo o tempo todo.

[00:17] Como prometido anteriormente, eu venho na documentação no Next.js e vou procurar aqui por “Link”. E repara que o Next vai nos trazer este “next/link”, aqui à esquerda.

[00:28] Ele tem alguns exemplos aqui, isso é importante falar, tudo que o Next traz na documentação ele sempre tenta trazer algum exemplo para conseguirmos trabalhar. Ele traz do próprio repositório do GitHub deles exemplos que as próprias pessoas da comunidade vão atualizando.

[00:47] E nós conseguimos ver que ele tem esse “Hello world example” aqui, que eu não vou olhar por hora, eu vou deixar para você curiar. Mas por hora, repara que temos um jeito do Next de fazer. Basicamente vamos importar esse componente ’next/link’ aqui e envolver uma tag `<a>` e não passar o href para ela.

[01:08] E você fica: “Meu Deus, o que está acontecendo aqui?”. Calma, que já vamos resolver. Eu vou fazer aqui o import do link, vou envolver, eu estou na nossa página do FAQ, é importante falar, voltei para o editor. No caso, eu estou na home, até eu me perdi aqui.

[01:25] Eu estou na home, importei o Link e vou colocar esse Link em volta do nosso `<a>`. Lembrando que esse link é o link do Next.js. O href vai sair da nossa tag `<a>` e vir para o link aqui. Então “Ctrl + X”, vem para cá, salvamos e vamos lá.

[01:53] Eu vou falar aqui agora, a dica para ver se está carregando tudo ou não, você pode abrir a aba network, nós já vamos abrir e olhar, mas é você olhar essa bolinha aqui à esquerda. Se essa bolinha rodar, fizer o X e depois ficar normal de novo, quer dizer que teve a navegação normal. Se ela não rodar, quer dizer que teve a navegação no modelo SPA.

[02:12] Se clicarmos aqui, “Ir para a home”, do FAQ para a home foi. E da home para o FAQ? Da home para o FAQ não teve. Voltamos aqui, carreguei, “Ir para o FAQ”, não teve. Ou seja, o componente link do Next já está fazendo o trabalho dele. Mas vamos fazer ficar melhor.

[02:34] Vamos aqui no código e vamos fazer dos dois, vamos fazer vir e voltar. Então do FAQ agora também vai ter o componente de link do Next. Nós vamos aqui no “faq.js”, envolver na página do FAQ agora, <Link></Link>, e o href=“/” está aqui, depois de <Link>. Ir para a home está com o link do Next e o ir para o FAQ também está com o link do Next.

[03:06] Carreguei a página, “Ir para a home”, “Ir para o FAQ”. Já parou de ter aquele carregamento extra que nós comentamos agora há pouco.

[03:14] Se dermos um “Inspect” aqui, aba “Network”, limpamos, ele parou de carregar mais arquivos, ou seja, exatamente o que queríamos no começo, está funcionando tal como esperado.

[03:29] Tem alguns detalhes para olharmos aqui agora, essa parte resolveu. Mas se dermos um “Inspect” aqui, ele está aqui com href e tal, certo. Se dermos um “Inspect” aqui também, dependendo da versão do Next que você estiver usando, pode ser que esse href aqui não tenha aparecido.

[03:50] Eu vou habilitar uma configuração do Next que é o passHref. Isso aqui é só para garantirmos, de novo, caso você esteja usando alguma versão antiga no projeto da sua empresa, se não estiver aparecendo href, você pode vir e usar esse passHref, que vai fazer ele mostrar o href na tag aqui.

[04:10] Outro detalhe importante agora, falando até um pouco mais de arquitetura, porque esse curso aqui, o React, eu espero que você já saiba, que você já tenha conhecimento geral de como usar, então a ideia é muito mais falar sobre como trabalhar com o Next.

[04:22] Vamos criar o nosso primeiro componente aqui agora e eu quero te dizer que nós teremos tendência a querer criá-lo dentro da pasta “pages”, mas isso não é o ideal. O ideal é todo o código da sua aplicação você criar numa pasta chamada de source, uma pasta sua, que você criou. Pode não ser a source, mas você vai criar a sua própria pasta de componentes que você quer usar.

[04:49] Eu tenho até outro nome que eu gosto de usar, que é, esse Link aqui está fazendo a ligação da nossa página com o framework, então o pessoal normalmente fala que essas dependências, esse componente é um componente de infraestrutura e tal.

[05:06] Eu posso até vir dentro da nossa pasta “components”, à esquerda, e só criar aqui, “Link” e eu vou criar um arquivo “index.js”. Eu estou criando uma pasta só porque depois pode ser que você adicione testes, pode ser que você adicione um CSS nesse arquivo, então vamos criar a pasta do componente com o index aqui.

[05:32] A lógica aqui vai ser: teremos agora o nosso componente link para não termos que ficar duplicando toda vez o link e o a. Só passamos o link e ele resolve para nós aqui.

[05:44] Então import Link from ‘next/link’; e export default function Link() {, return (. Aqui vamos copiar o nosso componente, vou dar um “Ctrl + X”. Estou tirando da home, da nossa pages home, e vou colar aqui.

[06:21] Dentro desse `<a>` vamos renderizar o children, que vai vir aqui do props, então o `export default function Link({ children, href, ...props})`. O href também vem, que vamos receber, então href aqui. E em teoria isso já deveria funcionar.

[06:50] O único ponto de atenção é que aqui estamos importando o Link do Next e exportando a nossa função de Link. É importante falar que esse Link do Next nós podemos chamar de next link, você pode dar o seu atalho para trabalhar com ele. Então eu vou colar aqui embaixo, NextLink e NextLink, e o nosso componente de link já está pronto, funcionando bonito.

[07:13] Essas outras props nós podemos passar direto para o nosso `<a>`, porque pode ter algum class name, algum on click, alguma outra coisa que vamos receber nesse link, alguma propriedade de acessibilidade, por exemplo, já vai ser passado direto aqui. Então vamos salvar.

[07:30] E aqui agora vamos chamar o nosso componente, `<Link></Link>`, que agora vai vir de `import Link from ‘../src/components/Link’;`. Então está aqui, importamos o nosso link, se você clicar para navegar ele traz o nosso componente recém criado e embaixo, no `<Link>`, nós colocamos Ir para a página do FAQ, com href=“/faq”.

[08:08] Então “Ir para a página do FAQ”, foi. Aba “Network”, limpar tudo aqui, não está baixando nada quando trocamos, e agora já temos o nosso componente aqui funcionando maravilhosamente. Aqui seria só apagarmos esse `<a>` e ajustar o import. Então na página do FAQ é `import Link from ‘../src/components/Link’;`. “Ir para a home”, “Ir para o FAQ”, de novo limpei, funcionando tal como o nosso primeiro exemplo.

[08:42] É importante dizer aqui que nós fazemos essa separação porque a pasta “pages” é o que o Next usa para fazer uma página dinâmica, o que ele usa para fazer a página 404.

[08:53] Por exemplo, se eu criar aqui à esquerda a pasta “404.js” e só para ganharmos tempo, eu vou copiar o código do FAQ aqui, seria export default function Page404(), ir para home, aqui, `<h1>Você se perdeu e caiu na página 404 :0</h1>`.

[09:25] Uma vez que caímos nessa página 404, ele vai nos trazer agora para essa página que criamos, só de criar o “404.js”.

[09:33] Se eu digitar na URL qualquer coisa, ele mostra aqui: “Você se perdeu e caiu na página 404”. “Ir para a home”, baixa o código da home, “Ir para o FAQ”, ele vai para o FAQ e a nossa página já está funcionando no modelo SPA, e ele já está também mostrando aqui todo o nosso conteúdo pré-renderizado.

[09:54] Se eu procurar esse Alura Cases página do FAQ aqui, no view source da página ele traz todo o nosso conteúdo aqui, coisa que uma app com o create-react-app não fazia, mas que vão sair mais detalhes no próximo vídeo.

### Faça como eu fiz: passHref

É muito comum a utilização de bibliotecas e/ou frameworks como o styled-componentes, Material UI e Chakra UI na construção de interfaces gráficas. Essas ferramentas fornecem seus próprios componentes de âncora (tag `<a>` do HTML), mas seus propósitos são apenas aplicar a estilização.

Sendo assim, é comum a composição do componente `<Link>` do Next.js com os componentes dos frameworks citados anteriormente, gerando um novo componente que possui tanto a funcionalidade de navegação quanto a estilização desejada.

Vamos simular a utilização de um desses frameworks e entender mais sobre o passHref mencionado no vídeo anterior.

1) Crie o componente LinkEstilizado, que irá apenas trocar a cor do texto do link para vermelho.
    - OBS: Este componente foi criado baseado no exemplo da documentação. Não se preocupe com o React.forwardRef nesse momento, pois ele e os atributos onClick href e ref são necessários para que o Next.js consiga implementar a navegação SPA corretamente.

        import React from 'react';

        const LinkEstilizado = React.forwardRef(({ onClick, href, children }, ref) => {
        return (
            <a href={href} onClick={onClick} ref={ref} style={{ color: 'red' }}>
            {children}
            </a>
        );
        });

        export default LinkEstilizado;
    
2) Substitua a tag `<a>` dentro do Link criado no vídeo anterior pelo componente `<LinkEstilizado>`.

        // Componente Link
        import NextLink from 'next/link';
        import LinkEstilizado from '../LinkEstilizado';

        export default function Link({ children, href, ...props }) {
        return (
            <NextLink href={href}>
            <LinkEstilizado {...props}>{children}</LinkEstilizado>
            </NextLink>
        );
        }

3) Rode o servidor com yarn dev.

4) Abra o DevTools do seu navegador e inspecione a tag `<a>`.

5) Retire o atributo passHref do componente Link, salve e inspecione novamente a tag `<a>` no documento.

#### Opinião do instrutor

O atributo passHref do NextLink força a passagem do href para seus componentes filhos. Ou seja, o href passado para o Link é implicitamente passado para o LinkEstilizado. Por isso que o href está presente na tag `<a>` do HTML e não precisamos escrever.

        <LinkEstilizado href={href}>

Código da Alura Cases Home Page. Atributo href destacado no DevTools da página

O valor default do passHref é false, então, após executar o passo 5 você verá que a tag `<a>` não possui mais o href. A tag está no documento e as suas estilizações provavelmente ainda estarão lá, mas a funcionalidade de navegação não funciona mais. Portanto, a acessibilidade e SEO da sua página serão prejudicados.

Código da Alura Cases Home Page. Tag a destacada no DevTools da página

Segundo a documentação sobre o Link do Next.js, o passHref é mandatório quando o filho do NextLink é um componente que envolve uma tag `<a>`, como é caso do LinkEstilizado e qualquer outro componente de navegação dos frameworks citados no início.

### Para saber mais: Referências da aula

- [Guillermo Rauch]('https://twitter.com/rauchg')
- [7 principles of rich web applications - Guillermo Rauch]('https://rauchg.com/2014/7-principles-of-rich-web-applications')
- [Como a internet funciona]('https://www.submarinecablemap.com/')
- [Onde ficam os servidores?]('https://jachoos.net/amazon-web-services-locations/')
- [Problemas, SEO e Web Vitals]('https://web.dev/vitals/')
- [JamStack Arquivos estáticos]('https://jamstack.org/')
- [Performance Web I: otimizando o front-end]('https://www.alura.com.br/curso-online-otimizacao-performance-web?gclid=CjwKCAiA78aNBhAlEiwA7B76pyarbX78QH2cLA9zcfvbwKHd9JFQJCkShSEAF5TU9oq0RGE_iGN09hoCmusQAvD_BwE')

### O que aprendemos?

- O que é Next.js?
    - Next.js é um framework baseado em React que pode entregar tanto conteúdo estático quanto gerado no servidor.
- A criar um projeto Next.js
    - Pode-se criar um projeto Next.js adicionando os pacotes do framework manualmente num projeto Node.js.
- Componente Link
    - Este componente permite a navegação SPA de aplicações Next.js.

## 2. Build e SEO na prática
### Entendendo o Build do Next.js

1. No terminal para que o projeto tenha um melhor desemepenho:

        yarn build && yarn start

2. No PACKAGE.JSON adicione: [Static HTML Export]('https://nextjs.org/docs/advanced-features/static-html-export#next-export')

        "scripts": {
                ...,
                "export": "next build && next export",
                ...
        }

3. Instalando um novo servidor

        npx http-server ./out -c-1

---

[00:00] Chegou a hora de entendermos um pouco mais do que o Next.js gera, porque até então ele parece igual o Create React App, que nós conseguimos criar a nossa aplicação, conseguimos vê-la rodando e ter o feedback e tudo mais.

[00:14] É nesse vídeo aqui que se você já conhece essa ferramenta, nós veremos o diferencial do Next em si. Nossa app está rodando aqui bonita.

[00:22] Eu comentei que todo esse código que estamos vendo, todo esse `<h1>` aqui e tudo mais, se dermos o “View Page Source”, nós conseguimos vê-lo, ou seja, ele está sendo pré-carregado aqui.

[00:35] Isso bate bastante com essa estratégia de fazer o tal do Server Side Render, ou seja, o HTML vai vir pronto para os nossos usuários e o usuário só vai baixar o conteúdo que queremos que ele tenha acesso.

[00:50] Para conseguir simular isso aqui, eu vou assumir que você vai hospedar o seu site em algum lugar, então você vai contratar um servidor, uma máquina, seja na AWS, seja no Heroku ou até mesmo na Vercel, que é onde faremos o nosso deploy em um momento futuro aqui do curso, por enquanto.

[01:10] Ou até mesmo tem a tal da Umbler, que se eu não me engano é uma empresa brasileira, que tinha hospedagem para Node, eu não lembro se eles têm ainda, mas eu lembro que durante uma época eles tinham.

[01:19] Então passei vários clientes, AWS, Heroku, a Vercel. Se você tem a sua aplicação rodando a nível de servidor, você conseguiu colocá-la nesses lugares aqui.

[01:30] Como seria esse rodar no servidor? Basicamente o seu código vai ser baixado em um desses servidores, vai ter uma máquina que vai ler o seu código, tal como a minha máquina que está rodando esse projeto aqui agora. E lá vai rodar o comando yarn build && yarn start.

[01:53] Repara que ele está buildando aqui, ele otimiza tanto a nossa página 404 quanto o FAQ aqui e tudo mais. E repara que tem um segredo, ele fala que tudo está sendo gerado como estático, mas eu já falo sobre isso.

[02:07] Se abrirmos o localhost:3000, que é onde estávamos, está aqui o nosso código. Parece que ele não mudou nada. Se dermos um view page source aqui, está tudo do mesmo jeito, estão aqui os arquivos Next. Eu posso até fechar e abrir de novo para vocês, aqui, $ next start, started server on.

[02:39] O que mudou aqui? Basicamente agora, se eu vier na nossa home e mudar aqui, `<h1>Alura Cases - Home Page bla</h1>`, repara que ele não muda mais de acordo com as alterações que fazemos. Ou seja, ele está só pegando a versão já gerada e jogando-a para o nosso usuário. É isso que vai acontecer no servidor.

[03:04] Porém, mesmo os servidores, é mais barato rodarmos os arquivos de forma estática. “O que seriam os arquivos de forma estática, Mario?”, seria pegar somente o HTML, o CSS e o JavaScript e servir. Então o usuário acessa uma URL, o servidor interpreta que teve a requisição e manda só um arquivo HTML estático. Você não tem o processamento do servidor de gerar o arquivo e depois mandar, que é uma coisa que acontece muito.

[03:29] O Next dá suporte para o Server Render, nós vamos vê-lo em outro momento desse curso ainda, mas por hora o que o Next está fazendo parece Server Render, mas vai gerar um monte de arquivos estáticos, ele está gerando um monte de arquivo estático para nós.

[03:42] “Mario, como assim arquivo estático? Eu não estou conseguindo entender isso”. Seguinte, aqui tem um build, que gera os arquivos estáticos e o servidor do próprio Next, otimizado para rodar o Next, que roda isso. É isso que está acontecendo.

[04:00] Porém, eu posso vir aqui e rodar o seguinte comando, eu vou até pegar a documentação, isso aqui é uma feature avançada do Next, que é esse Next Export, para você conseguir visualizar esses arquivos que eu estou falando.

[04:14] Eu vou criar aqui um comando chamado “export”:, no meu “package.json”, e eu vou dizer que esse “export”:, quando eu rodar yarn export, é um atalho para “next build && next export”. Basicamente eu estou fazendo um atalho para rodar isso aqui.

[04:40] Você fala: “Mario, beleza, então esse export é um atalho para next build e next export, show. Como isso funciona?”, vamos ver na prática. yarn export, vamos rodar.

[04:57] Repara que surgiu uma pasta “out”, à esquerda e dentro dela tem o “index.html”, o “faq.html” e a página “404.html”. Ele também tem esse monte de “chunks”, esse monte de arquivos JavaScript. Tudo que está aparecendo aqui que o Next gera, está aparecendo aqui também.

[05:16] Você fala: “Tá, Mario, mas qual é a vantagem disso?”. Eu consigo copiar o path para esse arquivo na minha máquina e colar isso no navegador, então “/Users/mariosouto/dev/alura/01-nextjs-course/out/index.html” e ele abriu.

[05:33] E se eu clicar para ir para o FAQ, ele quebra, por quê? Porque desse jeito aqui só os arquivos estáticos mesmo ele não está 100% preparado para rodar, precisaria minimamente ter algum outro servidor rodando.

[05:44] Tem um que eu uso bastante para testes, que é esse aqui, o npx http-server ./out, que é a pasta, e vou desabilitar o cache dele aqui, vou passar esse -c-1. Ele vai instalar.

[06:02] Esse http-server é um servidor básico, tal como qualquer coisa que você quiser botar online na internet, disponível para os usuários, vai ter que ter, tem que ter alguém recebendo as requisições, que é o servidor. Agora se eu acessar a porta 8080, “localhost:8080”, o mesmo conteúdo, só que agora ele funciona.

[06:27] Com essa estratégia nós não precisamos do servidor do Next, você pode pegar esses arquivos aqui e fazer diferentes estratégias de botá-lo no ar. Você pode colocá-lo no ar dentro de uma estrutura comum do AWS. Essa aqui nós não vamos abordar no curso, mas seriam os buckets do S3.

[06:48] Conversa com o pessoal de infraestrutura da sua empresa para fazer algumas contas de: vale a pena botar na Vercel? Aí você negocia o preço com eles. Faz uns testes de botar o seu site nesse bucket do S3, faz um teste de botar em outro lugar, tenta hospedar em lugares diferentes para você ver qual o custo-benefício melhor para a sua empresa.

[07:05] Já adianto que isso aqui só funciona para sites que são mais estáticos, então sites de página de campanha, hotsites e tudo mais.

[07:13] Se for um site um pouco maior, que tiver alguma coisa dinâmica, uma coisa dinâmica de verdade, que já falaremos mais para frente o que é dinâmico para valer na web, você teria que ter um servidor mesmo, com uma máquina rodando, processando todas as requisições, que o seu time vai configurar, ou vai ter que usar um Heroku da vida ou a própria Vercel.

[07:32] Desses aqui a Vercel é o mais tranquilo e eu acho um custo-benefício bem bom no final das contas, mas não é agora que faremos o deploy lá, esse vídeo foi só para te mostrar que você tem esse export estático aqui, você tem o build normal do Next.js, que é o que você vai usar para rodar qualquer servidor que você configurar, vai rodar build e start.

[07:56] E agora eu posso até arrumar a minha home aqui, `<h1>Alura Cases - Home</h1>`, que eu tinha bagunçado só para fazer esse exemplo para vocês. Nos vemos na nossa próxima aula.

### SEO na prática

[00:00] Um vídeo que não poderia faltar, é a dúvida que mais aparece, que é o pessoal tentando entender essa parte de SEO.

[00:06] Eu comentei do ponto de vista de Web Vitals, que são as coisas que o Google considera como métricas para ranquear melhor e tudo mais, o lance do LCP, do Firts Input Delay.

[00:17] Porém, a parte do conteúdo é o principal. Se o seu conteúdo não é bom e ele não renderiza no HTML, por mais que tenham estudos que provem que hoje em dia renderiza, tem rankings, então quanto mais demora para o seu conteúdo aparecer, mais tempo para o Googlebot rodar e você acabar sofrendo alguma penalidade.

[00:37] Qual é o ideal? Eu tenho uma app rodando com o Create React App e o nosso projeto aqui do curso. Se vocês forem olhar, o projeto com o Create React App é um projeto novo. Aqui à esquerda, “App.css”, “App.js”, tem o logo, edit, tudo igual está aparecendo aqui para vocês. Eu segui basicamente o “Getting Started” da documentação, não fui nada muito longe do que mostra aqui na própria documentação do Create React App.

[01:08] E de cara eu já consigo mostrar para vocês esse view page source dele. Isso aqui é estático. Ele fala que esse arquivo HTML é um template, se você abrir diretamente no navegador, você vai ver uma página em branco.

[01:20] Você pode adicionar fontes e tudo mais, mas você só vai conseguir ver o conteúdo quando o client renderizar, ou seja, o servidor vai responder com esse HTML os scripts que tem, vai terminar de baixar o javascript, vai rodar o React no navegador, aí sim ele sai do estado de loading.

[01:38] Enquanto que o Next.js, por mais que geremos o estático, tal como vimos no vídeo anterior, esse arquivo estático que ele gera já tem os conteúdos HTML. Se eu procurar por h1, ele tem uma tag h1 aqui, diferente do Create React App, que se eu olhar no view source dele, que está aberto aqui do lado, ele não traz nada.

[02:01] Se você olhar inspecionando o elemento, inspecionando ele tem. Existe aqui o “Edit”. Então está aqui, existe. No view source não existe. Se procurarmos aqui “Alura Cases - Home Page” no inspect, existe, e no view source também existe.

[02:29] Era só isso aqui, só para deixar claro para você e nós vamos nos aprofundar ainda mais em quando roda servidor, quando roda client, que é uma coisa super importante de aprender, mas isso fica para próximos vídeos, que agora precisamos aprender a estilizar a nossa aplicação.

### Exercício: Sobre o Next.js

Uma aplicação web criada com Next.js:

a) **Alternativa correta:** Tem opiniões fortes de como organizar a estrutura de pastas.

b) **Alternativa correta:** Possibilita Server Side Rendering (SSR).
- _Alternativa correta! O Next.js consegue pré-renderizar o HTML para cada requisição._

c) **Alternativa correta:** Possibilita geração de conteúdo estático (Static Site Generation - SSG).
- _Alternativa correta! O Next.js consegue pré-renderizar o HTML durante o build que será reutilizado em todas as requisições._

d) Impede a renderização do lado do cliente (Client Side Rendering).

e) **Alternativa correta:** Tem melhor SEO.
- _Alternativa correta! O SSR e SSG facilitam o escaneamento dos motores de busca, como resultado a aplicação tem uma melhor nota de SEO._

### Faça como eu fiz: create-next-app

Durante a aula você aprendeu a adicionar pacotes do Next.js e do React a um projeto Node vazio.

Para facilitar a vida dos desenvolvedores, os criadores do Next.js criaram a ferramenta create-next-app que instala todas as dependências do framework e cria a estrutura de pastas recomendada com uma linha de comando.

Que tal experimentar? Abra um terminal, navegue até uma pasta desejada e execute o comando:

        yarn create next-app nome-do-projeto

Para os usuários de NPM o comando é:

        npx create-next-app@latest

Para criar um novo projeto Next.js. substitua "nome-do-projeto" por algo do seu desejo e aguarde a instalação.

Abra a pasta no seu editor de código e tente encontrar as semelhanças e diferenças do que foi mostrado em aula!

VER OPINIÃO DO INSTRUTOR

Opinião do instrutor

Durante a aula criamos manualmente a pasta Pages e inserimos os comandos relacionados ao Next.js no package.json. O create-next-app já executou esses passos por você.

Estrutura de pastas do projeto padrão

A pasta api e o arquivo _app.js são particularidades do Next que serão explicados ao longo desta formação.

Além do Next, React e React-DOM, outra ferramenta muito utilizada foi instalada: o ESLint. O time do Next.js tem suas próprias sugestões de configuração, então acompanhado dele está o eslint-config-next.

A pasta public é utilizada para armazenar arquivos estáticos, como imagens e ícones.

A pasta styles não é obrigatória e você tem liberdade para utilizar o framework CSS de sua escolha. O projeto padrão utiliza o CSS Modules.

Para saber mais, visite a documentação do [create-next-app}('https://nextjs.org/docs/api-reference/create-next-app').

### O que aprendemos?

- Como buildar um projeto Next.js. O comando gera os arquivos que serão utilizados no ambiente de produção.

        next build && next export
  
- SEO no Next.js
  - O Next.js entrega o conteúdo da página diretamente, enquanto no Create React App ele é gerado após o carregamento. Como resultado o SEO é melhor.
- create-next-app
  - Essa ferramenta realiza o setup inicial por você, facilitando o início de uma aplicação Next.js.

## 3. Estilizando o projeto
### Onde colocar meu CSS?

[CSS-in-JS]('https://nextjs.org/docs/basic-features/built-in-css-support')

Podemos tornar nossas TAGS CSS genéricas com NEXT.JS:

1. No INDEX.JS:

        function Title( {children, as} ) {
                const  Tag = as;
                return (
                        <React.Fragment>
                                <Tag>
                                        {children}
                                </Tag>
                                <style jsx>{`
                                        ${Tag} {
                                                color : red;
                                                font-family : sans-serif;
                                        }
                                `}</style>
                        </React.Fragment>
                );
        }

        export defaulf function HomePage() {
                return (
                        <div>
                                <Title as="h1">Alura Cases - Home</Title>
                                ...
                        </div>
                )
        }

---

[00:00] O nosso curso de Next.js continua e chegou a hora de começarmos a estilizar a nossa aplicação, começar a cumprir aquela promessa que eu tinha feito no primeiro vídeo. E a promessa era no final nós termos um projeto essa cara aqui.

[00:14] Com imagem externa, com CSS. Quando mudamos de página tem uns estilos bacanas aqui. Então precisamos ter isso até o final.

[00:22] E para conseguir fazer isso, é importante aprendermos a entender como trabalhamos com estilos dentro de um projeto com o Next.js, porque até agora só vimos como fazemos essa parte geral da aplicação, mas não aplicamos nenhum CSS nosso, só aprendemos a criar página, fazer o link e tudo mais.

[00:42] Agora vamos começar a ver uma parte do Next, que é como trazer essa parte do CSS para cá. E veremos com a abordagem que o pessoal chama de CSS-in-JS, que é você criar o seu código CSS a partir do JavaScript, e com isso você ganha algumas vantagens de evitar a ter conflito de escopo, ter que pensar em nome de classe.

[01:04] Basicamente você vai criar o seu componente e conseguir usá-lo sem ter vários daqueles problemas gerais das páginas de CSS global e tal.

[01:13] E se você gosta de usar CSS, se você tem o index CSS, se você gosta de styled components, que é outra forma de fazer esse tal desse CSS-in-JS, fica tranquilo, que até o final dessa aula eu vou te passar um guia de como você pode trabalhar com essas outras referências, e é um guia do próprio time do Next.js, então confia em mim. Por hora, vamos seguir a abordagem padrão aqui do Next.

[01:38] Ele sugere aqui o CSS-in-JS. Ele mostra que o próprio React já dá suporte para isso, quando na tag style você passa um objeto com valor, e com isso já podemos passar um CSS dentro do JS dinâmico.

[01:53] Só que ele tem uma abordagem que é por meio dessa tag que tem o styled, styled-jsx, essa tag especial do Next.js. Como fazemos para usá-la aqui?

[02:04] Vamos voltar para a nossa página e vamos tentar fazer esse título, tentar deixá-lo grande, bold e com essa fonte mais redonda, sem ser com essa fonte serifada que temos aqui, que ela tem essa haste no canto.

[02:21] Para fazer isso, a primeira coisa acho que é criar o nosso componente do título. Eu venho aqui e vou fazer function Title(). E não se preocupa com relação a organização, como vamos quebrar, esse não é o foco tanto dessa aula aqui, o foco dessa aula é você ver as possibilidades e nas próximas nós começarmos a quebrar, organizar.

[02:40] E você também está aberto para organizar do jeito que você achar melhor. Essa coisa de arquitetura não existe muito uma regra, existem algumas direções e eu vou passar algumas direções que eu sigo aqui para vocês.

[02:54] O nosso componente Title() basicamente precisa retornar o `<h1>`, ele precisa passar o {children}, que é qualquer conteúdo que ele receber, ele vai passar para frente. E vamos trocar esse `<h1>` aqui embaixo pela tag `<Title>` que fizemos. E se salvarmos, tem que estar funcionando igual.

[03:17] Próximo passo aqui é botar uma tag `<style>`, prestar atenção que ele reclama, ele fala que expressões JSX têm que ter um elemento parente comum. Se olharmos, ele tem essa `<div>` aqui em volta, só que eu quero que esse componente seja só o título, que ele não tenha uma div.

[03:35] Podemos vir aqui, em volta de tudo, e colocar um `<React.Fragment>`, em volta dessa estrutura toda. Esse React.Fragment, para quem já usa o React, sabe que ele vai só substituir uma div ou algo do gênero, e permitir que coloquemos vários elementos HTML aqui dentro para renderizar sem ter um pai necessariamente em volta deles.

[04:00] Seguindo para os estilos, que é a nossa meta agora dentro do VS Code, se baseando no navegador, repara que ele pede aqui para colocarmos esse jsx e ele também tem essa sintaxe de código dinâmico, para falar que é o código do JavaScript ali dentro, pode rodar também.

[04:20] Vamos colocar aqui no `<style esse jxs>` e vamos respeitar essa sintaxe de botar os bigodinhos e a template string, {`}`, para poder botar algum valor aqui dentro.

[04:31] Como temos aqui o `<h1>`, vamos pegar esse h1 e vamos dizer que o color: red; dele vai ser red, acho que nada mais justo que botar um color: red; aqui, só para testarmos primeiro e depois colocamos o font-size, o font-weight que eu falei que vocês. Desculpa, o font-family.

[04:50] Carreguei aqui, repara que renderizou, está funcionando bonito. E o legal desse estilo ser dinâmico, é porque nós conseguimos expandir muito isso aqui. Por exemplo, por padrão aqui está renderizando com uma tag h1. Só que se quisermos mudar para uma tag h2, por exemplo, podemos vir aqui e mudar, para ser uma tag `<h2>`.

[05:15] Só que ele para de pegar o estilo. Ele está recebendo aqui um class dinâmico, que não definimos, mas ele não tem nada aplicando para esse h2. O que podemos fazer?

[05:25] Podemos vir aqui e, ou mudar esse h2 aqui embaixo também, que funciona, ele pega aqui embaixo h2., esse código grande para evitar conflitos de CSS. Ou você pode começar a fazer um código mais meta, que o pessoal chama, um código que gera um código.

[05:43] Que seria o seguinte, nós recebermos aqui um parâmetro de as }), que é para dizer que esse Title é como está o tag, ou vai renderizar como alguma coisa.

[05:55] E aqui embaixo nós falamos que queremos isso aqui como um `<Title as=“h1”>`, então passamos essa propriedade. Isso aqui é só para vocês verem o potencial dinâmico da coisa.

[06:08] E como temos esse as aqui agora, podemos dizer que todos esses valores h2 vão ser o valor da tag que estamos passando aqui embaixo, no Title. Então podemos vir aqui em cima passar um const Tag = as;.

[06:24] E vamos pegar essa tag e vamos botar no lugar do h2, no lugar aqui também. Lembrando que aqui vai ter esse valor do h1, que vamos receber daqui de baixo, de quem chamar. E aqui, como estamos dentro da estrutura dinâmica do React, podemos passar um valor dinâmico também. Eu passo aqui ${Tag}.

[06:47] Todo componente agora é super genérico, e se voltarmos para o navegador, ele agora aplica os estilos no h1. E ele também vai aplicar esses estilos se eu passar aqui agora um h2. Ele mudou para h2 e mudou o estilo aqui também.

[07:04] Essa abordagem é muito poderosa, ela nos permite estender muito as capacidades do CSS e, de fato, gerar um código, se olharmos aqui na página, você vai ver que está gerando um style CSS, então está realmente gerando uma coisa dinâmica e eu vejo que tem muito valor nessa forma de trabalhar, em aumentar a consistência.

[07:24] Porque, por exemplo, como agora você está criando todo o estilo dentro do componente, se você apagá-lo, você elimina o tal do dead code, que é aquele código morto, que fica muitas vezes, em muitos códigos que nós fazemos.

[07:35] Eu, particularmente, gosto bastante dessa abordagem, gosto bastante também da lib do styled components, que é uma lib que nos permite trabalhar com essa parte do CSS-in-JS. Mas fica tranquilo, que você vai escolher a forma que você achar melhor. Estamos usando essa porque esse curso é para o que o Next tem para oferecer para nós.

[07:59] Em sequência aqui, podemos querer, por exemplo, definir que essa fonte não vai aquela fonte serifada que eu falei. Podemos vir e botar o font-family: sans-serif;, que é o sem serifa. E ele resolveu. Só que ele resolveu só para o nosso h1.

[08:23] Minto, não é o nosso h1, é o nosso título, porque agora ele pode ter qualquer tag. Como ele resolveu só para cá, às vezes queremos ter um estilo que é global.

[08:33] E para fazer estilo global, para botar uma coisa que pega a aplicação inteira, vamos expandir para mais uma parte do Next.js, só que vai ser no próximo vídeo. Vejo você no próximo vídeo.

### Como lidar com estilos globais

[Custom APP]('https://nextjs.org/docs/advanced-features/custom-app')

1. Em src/theme/GlobalStyle.js:

        export default function GlobalStyle() {
                return (
                        <style global jsx> {`
                                body {
                                        font-family : sans-serif;
                                }

                        `} </style>
                )
        }
        
2. Em pags/_app.js:

        function MyApp({ Component, pageProps }) {
                return {
                        <>
                                <GlobalStyle />
                                <Component {...pageProps} />
                        </>
                        }
        }

        export default MyApp;

---

[00:00] Vamos dar continuidade a resolver o nosso problema de criar estilos globais, porque aqui estamos criando um CSS que é completamente escopado e tudo mais, e vocês vão ver que é bem tranquilo de criar.

[00:15] Inicialmente, tudo que precisamos fazer é: eu vou criar aqui um componente para isolar esses estilos globais, então vou criar aqui o function GlobalStyle(), é igual a return e aqui vou botar só a tag `<style>` com esse esquema que já vimos, o jsx, e vou botar aqui a estrutura da template string, {`}`.

[00:44] E nós vamos pegar esse font-family: sans-serif; aqui embaixo e vamos botar dentro da tag body. Nós botamos nela porque a tag body, todo mundo herda de body no CSS, então se aplicarmos para o body, todo mundo, em teoria, vai pegar esse font-family: sans-serif;. Então removi do Title e trouxe para cá.

[01:06] Se salvarmos e voltarmos para a página, repara que nada mudou, por quê? Porque só criamos o componente e não o usamos em nenhum lugar ainda.

[01:14] Numa primeira instância eu vou chamar esse GlobalStyle aqui que criamos, dentro da nossa HomePage. E se eu carregar a página, ele não funcionou. E você fica: “Mario, mas como assim? Você fez todo um rodeio, você começou a explicação e...”. Calma, respira.

[01:35] Aqui no Next, se scrollarmos um pouco a mais, repara que ele mostra aqui o `<style global jsx>`. Para criarmos esse estilo global, temos que, além de criar o nosso componente, declarar que esse CSS daqui é global.

[01:51] Então nós salvamos aqui de novo o arquivo agora e ele aplica para todo mundo, funciona perfeitamente. Só que quando trocamos de página, ele deixa de funcionar. Ele é global, só que para o escopo da home, ele é global no contexto que colocamos aqui.

[02:09] Isso é importante, porque pode ser que você queira ter um estilo gigantesco para uma landing page, para algo que você pediu de um fornecedor externo ou algo do gênero.

[02:18] Eu super vejo valor nessa possibilidade, porém, quando falamos de dia a dia, que você quer compartilhar as coisas no seu projeto para valer, o ideal é virmos na nossa pasta “pages”, à esquerda, e criarmos mais um arquivo do Next.js.

[02:33] E esse, eu vou até procurar com vocês, é o arquivo “_app.js”. E nós temos aqui à esquerda esse link do Custom App, que eu vou abrir aqui.

[02:48] O pessoal da Next sempre tem uma descrição de cada uma das coisas. Eu convido você a ler a documentação com calma, aproveitar. Os textos são sempre super bem otimizados, bem escritos e eles explicam muito bem o porquê de cada uma das coisas, isso eu gosto bastante do pessoal do Next.

[03:04] Aqui basicamente nós vamos criar esse arquivo “_app”, e qual é o papel dele? Ele vai ser como se fosse um centralizador, um middleware que o pessoal chama, o meio de campo entre qualquer página que o nosso usuário acesse e qualquer componente de página que nós vamos renderizar.

[03:20] Por componente de página, entenda que é cada componente que é exportado como default de um page, então 404, o FAQ, o index.js ou qualquer outro que venhamos a criar depois.

[03:34] Vamos criar esse cara aqui à esquerda, é o “app.js”, e vamos seguir o passo da documentação. Eu vou copiar esse function MyApp aqui e vamos copiar esse import App from ‘next/app’ dele também. Ele tem aqui “To override the default App, create the file `./pages/app.js` as shown below”.

[03:58] No caso, ele nem está mostrando esse import aqui para nós, como se nem precisasse importar, então vamos deixar do jeito que está aqui, sem problema nenhum. E vamos só fazer o export default desse componente. Então nós o criamos aqui e fizemos o export default MyApp;.

[04:16] Se viermos no navegador, não mudou nada, criou esse componente e não mudou nada. Eu vou até abrir o terminal para mostrar para vocês que ele tinha dado um erro aqui quando criamos a página, mas agora, sempre que salvamos, está tudo certo.

[04:31] Fica sempre de olho no terminal, essa é uma dica importante, para você pegar algum erro, algum problema que venha a acontecer. Acho que essa dica é super válida.

[04:40] Você fala: “Tá, Mario, mas o que isso está fazendo?”. Se eu envolver esse return em um parêntese, podemos quebrá-lo de linha. E se eu envolvê-lo ou no fragment ou nessa estrutura aqui, <></>, que é um react fragment abreviado, nós conseguimos vir aqui e botar, por exemplo, um teste. Então teste de componente middleware, componente agregador, o que passa em volta de todo mundo ali.

[05:09] Repara que esse texto renderizou tanto na home quanto na página do FAQ. Ele está aqui, ele está acima da div da nossa página. Ele está mais perto dessa div do Next aqui.

[05:23] O ideal é esse nosso estilo global que criamos aqui dentro, esse GlobalStyle, sair da nossa página home, ele vai sair daqui, vou até apagar a chamada que temos para ele aqui embaixo, `<GlobalStyle />`, e vou trazê-la para dentro de uma pasta chamada de tema, dentro de source.

[05:43] Essa página não existia antes, eu a criei enquanto eu estava fazendo um teste, mas vou até apagá-la de novo. O de vocês vai estar assim, pasta “src” com “components” e “Link”. Vou criar essa pasta “theme” agora e na pasta “theme” eu vou criar o “GlobalStyle.js”. Vou colar aqui e vou fazer o export default desse componente.

[06:09] Copiei aqui agora e vamos importá-lo dentro do “app.js”. Então vou apagar esse nosso teste e chamar o nosso `<Global Style />`. Aqui o próprio VS Code vai me ajudar, então ele fez o import de ’../src/theme/GlobalStyle’;, porque o “app.js” está aqui à esquerda, então ele sobe da pasta “pages”, acessa a pasta “src”, acessa a pasta “theme” e acessa o nosso “GlobalStyle.js”.

[06:35] Percorrido este caminho, se viermos no navegador, o GlobalStyle foi aplicado de novo. Se formos para o FAQ, ele também está sendo aplicado agora e se o comentarmos aqui, você vê que ele também está sendo trocado aqui.

[06:54] Você pode usar essa página de diferentes formas, você pode às vezes querer carregar um menu, um footer aqui, tem diferentes formas. Para carregar menu e * footer* talvez essa não seja a melhor abordagem, mas dependendo do seu cenário, pode funcionar, e se você ver que não funciona, você pode só criar um componente e chamá-lo em volta de cada uma das nossas páginas.

[07:13] Você poderia criar só um componente que abraça a página home, que abraça a página do FAQ, enfim, podemos até mostrar um caso desse, mas eu queria mostrar isso aqui, porque esse “_app.js”, para estilos e configurações gerais que você tem, providers e outras coisas, esse aqui vai ser o lugar que você vai chamar.

[07:33] Nós vamos voltar nele em outros momentos ainda, mas é importante você já ter consciência de que nós criamos o nosso arquivo custom app aqui na nossa aplicação e criamos o GlobalStyle.

[07:44] Reforçando que essa sintaxe do style e tudo mais, nos ajuda bastante em questão de organização, por ela fazer o escopo para nós. Elimina a necessidade de ter que pensar em: “Como eu vou um nome nesse estilo aqui?”, então ajuda bastante na produtividade e em ganhar otimização de ter menos problemas para se preocupar.

[08:06] Para esse vídeo aqui é só. No próximo vamos começar a trazer os componentes que eu preparei para nos facilitar a fazermos esses estilos. Lembrando que isso não é um curso de CSS, é um curso de Next, e junto com ele vão ter algumas outras dicas legais de CSS-in-JS, então fica aí para você ver logo no próximo vídeo, até mais.

### Preparando o ambiente: Recursos da aula 3

Nos próximos vídeos utilizaremos algumas bibliotecas externas e alguns componentes já prontos.

Font Awesome
Utilize o comando:

        yarn add @fortawesome/fontawesome-svg-core @fortawesome/free-solid-svg-icons @fortawesome/react-fontawesome

Para instalar a biblioteca de ícones Font Awesome que será utilizada no vídeo 2.3.

Imagens
As imagens utilizadas no site no próximo vídeo, podem ser baixadas nos links abaixo:

[Imagem Alura Cases]('https://github.com/alura-cursos/01-nextjs-course/blob/aula2.5/public/images/alura-cases.png')
[Logo Alura]('https://github.com/alura-cursos/01-nextjs-course/blob/aula2.5/public/images/alura-logo.svg')

Componentes
Como o foco deste curso é o Next.js, não será ensinado em vídeo como a estilização de cada componente base foi feita. Você é livre para criá-los utilizando as técnicas que você já conhece.

Você pode visualizar o código dos componentes no GitHub ou logo abaixo.

theme.js
        const partition = {
        'x1/1': '100%',
        'x1/2': '50%',
        'x1/3': '33.333333%',
        'x2/3': '66.666667%',
        'x1/4': '25%',
        'x2/4': '50%',
        'x3/4': '75%',
        'x1/5': '20%',
        'x2/5': '40%',
        'x3/5': '60%',
        'x4/5': '80%',
        'x1/6': '16.666667%',
        'x2/6': '33.333333%',
        'x3/6': '50%',
        'x4/6': '66.666667%',
        'x5/6': '83.333333%',
        'x1/12': '8.333333%',
        'x2/12': '16.666667%',
        'x3/12': '25%',
        'x4/12': '33.333333%',
        'x5/12': '41.666667%',
        'x6/12': '50%',
        'x7/12': '58.333333%',
        'x8/12': '66.666667%',
        'x9/12': '75%',
        'x10/12': '83.333333%',
        'x11/12': '91.666667%',
        };

        const container = {
        xcontainer_xs: '0', // '440px'  /* 27.5rem */,
        xcontainer_sm: '640px'  /* 40rem */,
        xcontainer_md: '768px'  /* 48rem */,
        xcontainer_lg: '1024px' /* 64rem */,
        xcontainer_xl: '1280px' /* 80rem */,
        };

        const space = {
        ...partition,
        ...container,
        x0: '0',
        xpx: '1px',
        'x0.5': '2px', // 0.125rem
        x1: '4px', // 0.25rem
        'x1.5': '6px', // 0.375rem
        x2: '8px', // 0.5rem
        'x2.5': '10px', // 0.625rem
        x3: '12px', // 0.75rem
        'x3.5': '14px', // 0.875rem
        x4: '16px', // 1rem
        x5: '20px', // 1.25rem'
        x6: '24px',// 1.5rem
        x7: '1.75rem',// 1.75rem
        x8: '32px', // 2rem
        x9: '36px', // 2.25rem
        x10: '40px', // 2.5rem
        x11: '44px', // 2.75rem
        x12: '48px', // 3rem
        x14: '56px', // 3.5rem
        x16: '64px', // 4rem
        x20: '80px', // 5rem
        x24: '96px', // 6rem
        x28: '112px', // 7rem
        x32: '128px', // 8rem
        x36: '144px', // 9rem
        x40: '160px', // 10rem
        x44: '176px', // 11rem
        x48: '192px', // 12rem
        x52: '208px', // 13rem
        x56: '224px', // 14rem
        x60: '240px', // 15rem
        x64: '256px', // 16rem
        x72: '288px', // 18rem
        x80: '320px', // 20rem
        x96: '384px', // 24rem
        };

        export const theme = {
        breakpoints: {
                "Breakpoints.xs": 0,
                "Breakpoints.sm": 480,
                "Breakpoints.md": 768,
                "Breakpoints.lg": 992,
                "Breakpoints.xl": 1200,
        },
        colors: {
                primary: {
                "050": "#EAE2F8",
                "100": "#CFBCF2",
                "200": "#A081D9",
                "300": "#8662C7",
                "400": "#724BB7",
                "500": "#653CAD",
                "600": "#51279B",
                "700": "#421987",
                "800": "#34126F",
                "900": "#240754",
                },
                neutral: {
                "000": "#FFFFFF",
                "050": "#F7F7F7",
                "100": "#E1E1E1",
                "200": "#CFCFCF",
                "300": "#B1B1B1",
                "400": "#9E9E9E",
                "500": "#7E7E7E",
                "600": "#626262",
                "700": "#515151",
                "800": "#3B3B3B",
                "900": "#222222",
                "999": "#111111",
                }
        },
        typography: {
                fontFamily: 'Open Sans',
                variants: {
                display1: {
                        fontSize: {
                        xs: "48px",
                        md: "60px"
                        },
                        letterSpacing: {
                        xs: '-0.04px',
                        },
                        fontWeight: {
                        xs: '900',
                        }
                },
                heading1: {
                        fontSize: {
                        xs: "36px",
                        md: "48px"
                        },
                        letterSpacing: {
                        xs: '-0.04px',
                        },
                        fontWeight: {
                        xs: '900',
                        }
                },
                heading2: {
                        fontSize: {
                        xs: "24px",
                        md: "36px",
                        },
                        letterSpacing: {
                        xs: '-0.04px',
                        },
                        fontWeight: {
                        xs: '900',
                        }
                },
                heading3: {
                        fontSize: {
                        xs: "20px",
                        md: "30px",
                        },
                        letterSpacing: {
                        xs: '-0.04px',
                        },
                        fontWeight: {
                        xs: 'bold',
                        }
                },
                heading4: {
                        fontSize: {
                        xs: "16px",
                        md: "20px",
                        },
                        letterSpacing: {
                        xs: '-0.04px',
                        },
                        fontWeight: {
                        xs: 'bold',
                        }
                },
                heading5: {
                        fontSize: {
                        xs: "14px",
                        md: "16px",
                        },
                        letterSpacing: {
                        xs: '-0.04px',
                        },
                        fontWeight: {
                        xs: 'bold',
                        }
                },
                body1: {
                        fontSize: {
                        xs: "18px",
                        },
                        fontWeight: {
                        xs: '400',
                        },
                },
                body2: {
                        fontSize: {
                        xs: "16px",
                        },
                        fontWeight: {
                        xs: '400',
                        },
                },
                body3: {
                        fontSize: {
                        xs: "14px",
                        },
                        fontWeight: {
                        xs: '400',
                        },
                },
                body4: {
                        fontSize: {
                        xs: "12px",
                        },
                        fontWeight: {
                        xs: '400',
                        },
                },
                }
        },
        space,
        }

Componentes

        import React from 'react';
        import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
        import * as iconSet from "@fortawesome/free-solid-svg-icons";

        import { theme } from './theme';

        function capitalize(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
        }

        function renderCSSValue(cssPropName, cssPropValue) {
        if (cssPropName.includes('horizontal')) {
        return `
        ${cssPropName.replace('horizontal', 'left')}: ${cssPropValue};
        ${cssPropName.replace('horizontal', 'right')}: ${cssPropValue};
        `;
        }
        if (cssPropName.includes('vertical')) {
        return `
        ${cssPropName.replace('vertical', 'top')}: ${cssPropValue};
        ${cssPropName.replace('vertical', 'bottom')}: ${cssPropValue};
        `;
        }

        return cssPropName + ':' + cssPropValue + ';';
        }
        function renderCSS(props, currentBreakpoint) {
        if (!props) return '';

        return Object
        .keys(props)
        .map((prop) => {
        const cssPropName = prop.split(/(?=[A-Z])/).join('-').toLowerCase();
        const cssPropValue = props[prop];
        const isCssPropValueAnObject = Object.prototype.toString.call(cssPropValue) === '[object Object]';
        const currentCssPropValue = cssPropValue[currentBreakpoint];

        if (currentBreakpoint == 'xs' && !isCssPropValueAnObject) {
                return renderCSSValue(cssPropName, cssPropValue);
        }

        if (currentCssPropValue) {
                return renderCSSValue(cssPropName, currentCssPropValue);
        }
        }).filter(Boolean).join('');
        }

        export function Box({
        as,
        styleSheet: { focus, hover, srOnly, ...styleSheet },
        ...props
        }) {
        const Tag = as || 'div';

        return (
        <React.Fragment>
        <Tag {...props} className={`${props.className ? props.className : ''} ${srOnly ? 'sr-only' : ''}`} />
        <style jsx>{`
                ${Tag} {
                ${renderCSS(styleSheet, 'xs')};
                }
                ${Tag}:hover {
                ${renderCSS(hover, 'xs')};
                }
                ${Tag}:focus {
                ${renderCSS(focus, 'xs')};
                }
                @media screen and (min-width: ${theme.breakpoints['Breakpoints.sm']}px) {
                ${Tag} {
                ${renderCSS(styleSheet, 'sm')};
                }
                ${Tag}:hover {
                ${renderCSS(hover, 'sm')};
                }
                ${Tag}:focus {
                ${renderCSS(focus, 'sm')};
                }
                }
                @media screen and (min-width: ${theme.breakpoints['Breakpoints.md']}px) {
                ${Tag} {
                ${renderCSS(styleSheet, 'md')};
                }
                ${Tag}:hover {
                ${renderCSS(hover, 'md')};
                }
                ${Tag}:focus {
                ${renderCSS(focus, 'md')};
                }
                }
                @media screen and (min-width: ${theme.breakpoints['Breakpoints.lg']}px) {
                ${Tag} {
                ${renderCSS(styleSheet, 'lg')};
                }
                ${Tag}:hover {
                ${renderCSS(hover, 'lg')};
                }
                ${Tag}:focus {
                ${renderCSS(focus, 'lg')};
                }
                }
                @media screen and (min-width: ${theme.breakpoints['Breakpoints.xl']}px) {
                ${Tag} {
                ${renderCSS(styleSheet, 'xl')};
                }
                ${Tag}:hover {
                ${renderCSS(hover, 'xl')};
                }
                ${Tag}:focus {
                ${renderCSS(focus, 'xl')};
                }
                }
        `}</style>
        </React.Fragment>
        )
        }

                /* @media screen and (min-width: ${theme.breakpoints['Breakpoints.md']}px) {
                ${renderCSS(styleSheet, 'md')};
                :hover {
                ${renderCSS(hover, 'md')};
                }
                :focus {
                ${renderCSS(focus, 'md')};
                }
                }
                @media screen and (min-width: ${theme.breakpoints['Breakpoints.lg']}px) {
                ${renderCSS(styleSheet, 'lg')};
                :hover {
                ${renderCSS(hover, 'lg')};
                }
                :focus {
                ${renderCSS(focus, 'lg')};
                }
                }
                @media screen and (min-width: ${theme.breakpoints['Breakpoints.xl']}px) {
                ${renderCSS(styleSheet, 'xl')};
                :hover {
                ${renderCSS(hover, 'xl')};
                }
                :focus {
                ${renderCSS(focus, 'xl')};
                }
                } */

        Box.defaultProps = {
        styleSheet: {},
        };

        export function Icon({ as, styleSheet, ...props }) {
        const {
        iconVariant,
        ...restStyleSheet
        } = styleSheet;
        const styleSheetUpdated = restStyleSheet;

        console.log('iconVariant', iconVariant);

        return (
        <Box
        as={FontAwesomeIcon}
        icon={iconSet[`fa${capitalize(iconVariant)}`]}
        crossOrigin="anonymous"
        styleSheet={{
                width: '1.5ch',
                height: '1.5ch',
                ...styleSheetUpdated
        }}
        {...props}
        />
        )
        }

        export function Text({ as, styleSheet, ...props }) {
        const {
        textVariant = {
        fontSize: 'inherit',
        },
        ...restStyleSheet
        } = styleSheet;
        const styleSheetUpdated = { ...textVariant, ...restStyleSheet };
        const tag = as || 'span';
        return (
        <Box
        as={tag}
        styleSheet={styleSheetUpdated}
        {...props}
        />
        )
        }
        Text.defaultProps = {
        styleSheet: {},
        };

        export function Image({ as, ...props }) {
        const tag = as || 'img';
        const {
        children,
        dangerouslySetInnerHTML,
        ...imageProps
        } = props;

        return (
        <Box as={tag} {...imageProps} />
        );
        }
        Image.defaultProps = {
        styleSheet: {},
        };

        export function Input({ as, styleSheet, ...props }) {
        const tag = 'input';
        const finalStyleSheet = {
        transition: 'all 0.2s ease-in-out',
        outline: 0,
        textVariant: theme.typography.variants.body2,
        color: theme.colors.neutral[900],
        boxShadow: `0 5px 7px -5px ${theme.colors.neutral[999]}43`,
        display: 'block',
        width: theme.space["x1/1"],
        border: `1px solid ${theme.colors.neutral[300]}`,
        borderRadius: theme.space.x2,
        paddingHorizontal: theme.space.x5,
        paddingVertical: theme.space.x3,
        focus: {
        border: `1px solid ${theme.colors.primary[500]}`,
        boxShadow: `0 5px 10px -5px ${theme.colors.neutral[999]}43`,
        },
        ...styleSheet,
        };

        return (
        <Text as={tag} styleSheet={finalStyleSheet} {...props} />
        );
        }
        Input.defaultProps = {
        styleSheet: {},
        };

        export function Button({ as, styleSheet, ...props }) {
        const {
        buttonVariant = 'primary',
        ...restStyleSheet
        } = styleSheet;
        const tag = 'button';

        const finalStyleSheet = {
        cursor: 'pointer',
        textVariant: theme.typography.variants.body2,
        color: theme.colors.neutral["000"],
        boxShadow: `0 5px 7px -5px ${theme.colors.neutral["999"]}43`,
        display: 'block',
        outline: 0,
        width: theme.space["x1/1"],
        border: `${theme.space.xpx} solid ${theme.colors[buttonVariant][900]}`,
        borderRadius: theme.space.x2,
        paddingHorizontal: {
        xs: theme.space.x5,
        sm: theme.space.x10
        },
        paddingVertical: theme.space.x3,
        transition: 'all 0.2s ease-in-out',
        backgroundColor: theme.colors[buttonVariant][600],
        hover: {
        backgroundColor: theme.colors[buttonVariant][500],
        boxShadow: `0 5px 10px -5px ${theme.colors.neutral[999]}73`,
        },
        focus: {
        backgroundColor: theme.colors[buttonVariant][700],
        boxShadow: `0 5px 10px -5px ${theme.colors.neutral[999]}93`,
        },
        ...restStyleSheet,
        };

        return (
        <Text as={tag} styleSheet={finalStyleSheet} {...props} />
        );
        }
        Button.defaultProps = {
        styleSheet: {},
        };

Footer

        import { theme } from '../../../theme/theme';
        import { Box, Text } from '../../../theme/components';

        export default function Footer() {
        return (
        <Box
        as="footer"
        styleSheet={{
                backgroundColor: theme.colors.neutral[900]
        }}
        >
        <Box
                styleSheet={{
                overflow:"hidden",
                maxWidth: theme.space.xcontainer_xl,
                marginLeft: "auto",
                marginRight:"auto",
                paddingVertical:{
                xs: theme.space.x12,
                },
                paddingHorizontal:{
                xs: theme.space.x4,
                sm: theme.space.x6,
                lg: theme.space.x8,
                },
                }}
        >
                <Text
                as="p"
                styleSheet={{
                textVariant: theme.typography.variants.body3,
                textAlign: "center",
                color: theme.colors.neutral[400],
                }}
                >
                &copy; {new Date().getFullYear()} DevSoutinho. Todos os direitos reservados.
                </Text>
        </Box>
        </Box>
        )
        }

GlobalStyle

        import { theme } from './theme';

        export default function GlobalStyle() {
        return (
                <style global jsx>{`
                * {
                box-sizing: border-box;
                padding: 0;
                margin: 0;
                }
                a {
                text-decoration: none;
                }
                body {
                font-family: ${theme.typography.fontFamily}, sans-serif;
                }
                img, video {
                max-width: 100%;
                height: auto;
                }
                audio, canvas, embed, iframe, img, object, svg, video {
                display: block;
                vertical-align: middle;
                }
                .sr-only {
                position: absolute;
                width: 1px;
                height: 1px;
                padding: 0;
                margin: -1px;
                overflow: hidden;
                clip: rect(0,0,0,0);
                border: 0;
                }
                /* ================== */
                /* NextJS */
                /* ================== */
                html {
                height: 100%;
                }
                body,
                #__next {
                height: 100%;
                }
                #__next {
                display: flex;
                flex-direction: column;
                }
                #__next > * {
                flex: 1;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                align-items: stretch;
                }
        `}</style>
        )
        }

HomeScreen

                        import Footer from '../../components/patterns/Footer'
                        import Link from '../../components/Link'
                        import { theme } from '../../theme/theme';
                        import { Image, Box, Text, Icon, Input, Button } from '../../theme/components';

                        const LOGO_ALURA_URL = 'http://placehold.it/94x44';
                        const SIDE_IMAGE_URL = 'http://placehold.it/2878x1640'

                        function SideImage() {
                        return (
                        <Box
                        styleSheet={{
                                paddingHorizontal: {
                                md: theme.space.x8,
                                },
                                marginHorizontal: {
                                sm: 'auto'
                                },
                                maxWidth: {
                                sm: theme.space.xcontainer_md,
                                }
                        }}
                        >
                        <Box
                                styleSheet={{
                                top: 0,
                                bottom: 0,
                                right: {
                                lg: theme.space.x0
                                },
                                width: {
                                lg: theme.space["x1/2"],
                                },
                                paddingTop: {
                                xs: theme.space.x12,
                                sm: theme.space.x16,
                                },
                                paddingBottom: {
                                lg: theme.space.x16,
                                },
                                position: {
                                sm: 'relative',
                                lg: 'absolute',
                                }
                                }}
                        >
                                <Box 
                                styleSheet={{
                                height: {
                                lg: theme.space["x1/1"],
                                },
                                maxWidth: {
                                sm: theme.space.xcontainer_md,
                                lg: 'none'
                                },
                                position: 'relative',
                                paddingHorizontal: {
                                sm: theme.space.x0,
                                },
                                paddingLeft: {
                                lg: theme.space.x12,
                                },
                                marginRight: {
                                lg: `-${theme.space.x40}`,
                                },
                                marginHorizontal: {
                                sm: 'auto',
                                },
                                }}
                                >
                                <Image
                                styleSheet={{
                                boxShadow: `0 5px 16px 0px ${theme.colors.neutral[999]}73`,
                                borderRadius: {
                                        md: theme.space.x4,
                                },
                                maxWidth: {
                                        lg: "none",
                                },
                                width: {
                                        lg: "auto",
                                },
                                height: {
                                        lg: theme.space["x1/1"],
                                },
                                }}
                                src={SIDE_IMAGE_URL}
                                alt="Treinamento com a roberta arcoverde no alura cases, falando sobre o stackoverflow"
                                />
                                </Box>
                        </Box>
                        </Box>
                        )
                        }

                        export default function HomeScreen() {
                        return (
                        <Box>
                        <Box
                                as="main"
                                styleSheet={{
                                flex: 1,
                                backgroundColor: theme.colors.neutral["050"],
                                }}
                        >
                                <Box
                                styleSheet={{
                                overflow: 'hidden',
                                position: {
                                lg: 'relative',
                                },
                                paddingTop: {
                                xs: theme.space.x6,
                                sm: theme.space.x12,
                                },
                                paddingVertical: {
                                md: theme.space.x20,
                                lg: theme.space.x24,
                                },
                                }}
                                >
                                <Box
                                styleSheet={{
                                marginHorizontal: 'auto',
                                paddingHorizontal: {
                                        xs: theme.space.x4,
                                        sm: theme.space.x6,
                                        lg: theme.space.x8,
                                },
                                maxWidth: {
                                        sm: theme.space.xcontainer_md,
                                        lg: theme.space.xcontainer_lg,
                                },
                                display: {
                                        lg: "grid",
                                },
                                gap: {
                                        lg: theme.space.x24,
                                },
                                gridTemplateColumns: {
                                        lg: "repeat(2, minmax(0, 1fr))",
                                }
                                }}
                                >
                                <Box>
                                <Box>
                                        <Image
                                        styleSheet={{
                                        width: "auto",
                                        height: theme.space.x11,
                                        }}
                                        src={LOGO_ALURA_URL}
                                        alt="Logo Alura"
                                        />
                                </Box>
                                <Box
                                        styleSheet={{
                                        marginTop: {
                                        xs: theme.space.x16,
                                        sm: theme.space.x20,
                                        },
                                        }}
                                >
                                        <Box>
                                        <Link
                                        href="/faq"
                                        styleSheet={{
                                        display: "inline-flex",
                                        alignItems: {
                                                xs: "flex-start",
                                                sm: "center",
                                        },
                                        flexDirection: {
                                                xs: "column",
                                                sm: "row",
                                        },
                                        }}
                                        >
                                        <Text
                                        styleSheet={{
                                                textVariant: theme.typography.variants.body4,
                                                fontWeight: "600",
                                                borderRadius: theme.space.x64,
                                                color: theme.colors.primary["400"],
                                                backgroundColor: theme.colors.primary["100"],
                                                paddingHorizontal: theme.space['x2.5'],
                                                paddingVertical: theme.space['x1'],
                                                marginRight: theme.space.x2,
                                                marginBottom: {
                                                xs: theme.space.x2,
                                                sm: theme.space.x0
                                                },
                                        }}
                                        >
                                        O que tem de novo?
                                        </Text>
                                        <Text
                                        styleSheet={{
                                                textVariant: theme.typography.variants.body4,
                                                fontWeight: "600",
                                                display: 'inline-flex',
                                                borderRadius: theme.space.x64,
                                                color: theme.colors.primary["400"],
                                                alignItems: 'center',
                                        }}
                                        >
                                        <Text>Confira as principais dúvidas</Text>
                                        <Icon
                                                styleSheet={{
                                                iconVariant: 'chevronRight',
                                                marginLeft: theme.space.xpx,
                                                }}
                                                aria-hidden="true"
                                        />
                                        </Text>
                                        </Link>
                                        </Box>
                                        <Box
                                        styleSheet={{
                                        marginTop: theme.space.x6,
                                        maxWidth: theme.space.xcontainer_sm,
                                        }}
                                        >
                                        <Text
                                        as="h1"
                                        styleSheet={{
                                        textVariant: theme.typography.variants.heading1,
                                        color: theme.colors.neutral["900"],
                                        }}
                                        >
                                        Alura Cases
                                        </Text>
                                        <Text
                                        as="p"
                                        styleSheet={{
                                        textVariant: theme.typography.variants.body1,
                                        color: theme.colors.neutral["500"],
                                        marginTop: theme.space.x6,
                                        }}
                                        >
                                        Aqui você vai ter acesso a discussões avançadas: as principais decisões sobre arquitetura e design de sistemas. Aprenda através das descobertas que as principais empresas de tecnologia enfrentam!
                                        </Text>
                                        <Text
                                        as="p"
                                        styleSheet={{
                                        textVariant: theme.typography.variants.body1,
                                        color: theme.colors.neutral["500"],
                                        marginTop: theme.space.x6,
                                        }}
                                        >
                                        Quer testar antes de todo mundo?
                                        </Text>
                                        </Box>
                                        <Box
                                        as="form"
                                        action="#"
                                        styleSheet={{
                                        display: {
                                        sm: 'flex',
                                        },
                                        marginTop: theme.space.x12,
                                        width: {
                                        sm: theme.space['x1/1'],
                                        },
                                        maxWidth: {
                                        sm: theme.space.xcontainer_lg,
                                        }
                                        }}
                                        >
                                        <Box
                                        styleSheet={{
                                        minWidth: 0,
                                        flex: 1,
                                        }}
                                        >
                                        <Text
                                        as="label"
                                        htmlFor="email"
                                        styleSheet={{
                                                srOnly: true,
                                        }}
                                        >
                                        Email address
                                        </Text>
                                        <Input
                                        id="email"
                                        type="email"
                                        placeholder="Coloque seu email aqui"
                                        />
                                        </Box>
                                        <Box 
                                        styleSheet={{
                                        marginTop: {
                                                xs: theme.space.x4,
                                                sm: theme.space.x0,
                                        },
                                        marginLeft: {
                                                sm: theme.space.x3,
                                        },
                                        }}
                                        >
                                        <Button
                                        type="submit"
                                        // button variant
                                        >
                                        Cadastrar
                                        </Button>
                                        </Box>
                                        </Box>
                                </Box>
                                </Box>
                                </Box>

                                <SideImage />
                                </Box>
                        </Box>
                        <Footer />
                        </Box>
                        )
                        }

### Componentes do layout

[00:00] E seguindo na nossa missão de estilizar, finalmente eu vou passar para vocês os estilos que temos para fazer essa página acontecer.

[00:09] Nós vamos parte por parte adicionando coisas que vão ser comuns a todos os projetos, e vocês podem seguir mais ou menos o mesmo fluxo que eu vou fazer aqui para fazer no projeto de vocês.

[00:19] Como esse é um capítulo meio de cola, eu vou bem com calma, vocês vão ter o link aqui na descrição para pegar todos os arquivos, o passo a passo, então assiste comigo, acompanha, e depois você segue o tutorial para preencher o seu projeto.

[00:32] Nós vamos montar primeiro a nossa home, a nossa página inicial. Para isso, a primeira coisa que faremos é trazer as fontes para o nosso projeto.

[00:41] E eu optei por usar o Font Awesome, que é um repositório com muitas fontes, tem várias delas que são open source, tem o plano pago deles também, mas o plano open source já tem muita coisa e vai te ajudar a colocar ícones nos seus projetos também. Eu quero que você saia desse curso e tenha material para fazer as suas próprias coisas.

[00:59] Primeira coisa que eu vou fazer, para adicionarmos isso aqui no nosso projeto, é parar o nosso processo aqui, eu vou dar um “Ctrl + C” e vou colar esse comando grande aqui embaixo, que eu vou passar depois na descrição para vocês.

[01:13] Ele vai trazer três libs, o core do Font Awesome, a versão dos ícones sólidos deles e o componente para trabalhar com o React do Font Awesome, são essas três coisas que eu vou botar para instalar. E enquanto isso, eu tomo uma água aqui. Foi super rápido.

[01:39] Agora eu acho que o próximo passo que podemos começar a fazer aqui é só olhar o nosso “package.json”, ver que ele teve aquelas alterações que ele sofreu e tudo mais.

[01:51] Nós adicionamos essas libs, só que calma que tem mais algumas estruturas para fazermos tudo isso aqui aparecer.

[01:56] Esse projeto todo aqui tem várias coisas específicas dele, ele tem a fonte que está sendo carregada, ele tem também as cores, as definições de borda. Tem muita coisa de definição aqui que normalmente eu guardo num arquivo que fica dentro dessa pasta do tema, e arquivo, eu justamente o chamo de tema, então é o “theme.js”.

[02:23] E esse tema, pensa que ele vai ser traduzido a partir de algum arquivo do Figma. Pensa que o designer vai ter o Photoshop ou Figma ou Sketch, algum arquivo de design, que ele vai descrever lá quais são as cores, quais são as fontes, quais são as bordas.

[02:37] No nosso caso, já pegamos todas essas descrições do designer e convertemos num código, que vai ficar dentro desse arquivo que chamamos de “theme.js”, e esse código, eu vou copiá-lo e vou colar. Lembrando que você não precisa entender a fundo esse código aqui, mas eu vou te passar alguns detalhes.

[02:55] Basicamente, ele tem várias especificações como, por exemplo, quais são os breakpoints que trabalhamos, qual tamanho de tela é o XS, qual é a tela média, qual é a tela mais larga, a tela maior, a tela grande, qual é a cor primária do nosso projeto, quais são as cores neutras.

[03:11] Daria para ter também as cores de feedback, as cores neutras, as cores positivas, então dá para ir adicionando mais cores aqui, nós trouxemos o mais geral, que é só para vocês terem contexto.

[03:22] Mas repara que ele traz aqui as variantes de texto, ele tem o texto 1, texto 2, texto 3, texto 4, o tamanho de corpo 1, corpo 2, corpo 3. Tem muitas definições aqui para nós, para normalizar essa parte de design e sistematizar o core do que o pessoal chama de design system, são os tokens, é o que os designers vão usar para montar as páginas e nós vamos ter pré-documentado e já pré-registrado aqui na code base. Esse arquivo serve para isso.

[03:53] De princípio, ele também não vai renderizar nada, porque ele precisa do set de estrutura que fizemos para ligar esse componente com essa parte do tema aqui.

[04:06] Essa parte de estrutura vai ficar dentro de um arquivo que eu vou criar aqui dentro de “theme” também, chamado de “components.js”. Esse components também vai ter uma estrutura que traremos pronta para vocês e tem bastante código aqui. Eu recomendo vocês darem uma olhada. De novo, isso é para acelerarmos, ganharmos tempo aqui no curso, não ser o foco fazer essa parte de layout em si.

[04:29] Mas aqui estamos importando a lib do Font Awesome, importando o set de ícones que eles têm. Aqui temos várias funções que vão lidar com CSS, tem essa função caixa, que vamos usar para fazer todos os componentes da parte de quadrados que temos na página.

[04:45] Temos também toda a parte de ícone, tem o ícone aqui, tem a parte de texto, tem a parte de imagem, input, botão. Vários componentes padrões que precisamos, tem todo o projeto, já estão aqui e já está pronto para você usar.

[05:00] Pega toda essa parte, com todas essas referências, o Box, ele já lida com resolução de tela, várias coisas para nós, vamos minimizar isso, tirar um pouco dessa carga e essa é a parte mais pronta que eu vou dar para vocês.

[05:17] Agora vamos ver como essa parte pronta vai nos ajudar a fazer as coisas na prática. Eu preciso rodar de novo o projeto, então venho no terminal, yarn dev. Eu vou trazer para nós agora, na nossa home page, o componente de footer, inicialmente, vamos trazer um `<Footer />`.

[05:39] Esse `<Footer />`, nós já temos o código deles e eu também vou passar para vocês, então vou pegá-lo da minha cola, vou colar essa parte aqui do components.

[05:47] Aqui dentro de “components” eu vou criar uma pasta chamada de “patterns”, que é o nome que eu convencionei a dar nos projetos que eu trabalho para componentes que são maiores que só um botão, só um título, só um link, componentes que são agregados de coisas. Coisas que são comuns, tipo menu, footer, sidebar e outras coisas assim, e que não são simples demais.

[06:08] Fica meio subjetiva essa regra, mas é como eu convencionei. Se você quiser chamar de outra forma, fique à vontade, o projeto é seu também, segue o que você achar melhor.

[06:17] Mas aqui eu vou criar a pasta “Footer”, vou criar o arquivo “index.js” e vou colá-lo aqui dentro. E aqui eu queria fazer uma tour com vocês de como isso funciona, porque basicamente eu estou importando daquele “theme/components” que eu trouxe agora para vocês, a caixa e o texto.

[06:37] Por quê? Porque esse footer aqui nada mais é do que uma caixa preta, com um padding, margem e um texto. Então basicamente nós importamos esses dois componentes aqui, Text e Box.

[06:47] E uma das vertentes dos CSS-in-JS é você definir todo o seu estilo via propriedades, então repara que cada propriedade eu estou acessando um valor do meu tema. Por exemplo, o backgroundColor eu sei que é a cor do tema neutro 900.

[07:02] Se você quiser saber qual é, você passa o mouse aqui em cima, você consegue ver que temos o valor. Se você clicar e acessar, ele mostra. Se você segurar o “Command” ou o “Ctrl” no Windows, ele vai nos mostrando quais são os valores das [ININTELIGÍVEL - COISAS], você pode clicar também e ir vendo aqui. Então o 900 é um atalho para isso aqui.

[07:21] Por que essa estrutura? Porque você tem o poder de mudar a cor primária e deixar o projeto um pouco mais com a sua cara, ou mudar as cores neutras. A minha ideia é você poder customizar o projeto e deixar do seu jeito também. E também é o que eu faço, trabalhando no dia a dia, então essa estratégia, eu acredito bastante nela e funciona super bem.

[07:40] Aqui embaixo, os espaçamentos também estão padronizados, o x12 é 48 pixels, o x4 16, o x6 é 24 pixels. Mesmo os tamanhos menores de texto também estão padronizados e tudo está nessa estrutura aqui.

[07:54] Uma vez nessa estrutura, fica super tranquilo de eu pegar esse Footer aqui em cima e importá-lo na nossa home. Então de novo, saindo do diretório “pages”, vindo para o “src”, acessando a pasta “components”, acessando a pasta de “patterns”, acessando a pasta de “Footer”, pega o Footer, traz nessa variável para nós, salva e bota o Footer ali no final.

[08:20] Se voltarmos aqui no navegador, nós temos nosso footer. Ele já está renderizado, com as cores que ele precisa ter, tudo certo, não teremos que nos preocupar com estilo agora.

[08:30] Teremos que nos preocupar, só que teremos que nos preocupar com a parte do nosso global style, repara que ele não está resetando essa margem que tem do body, repara que o body tem margem de 8 pixels aqui, vamos arrumar essas coisas agora. E para isso eu vou trazer um global style que está mais encorpado também.

[08:50] Eu vou lá de novo no “GlobalStyle.js”, e esse nosso que era simples, que ele só arrumava as fontes, vai ser substituído por esse aqui. Eu colei agora, que ele tem mais propriedades, ele tem esse box-sizing e border-box, ele muda o link.

[09:05] Ele pega do tema qual é o font family que vamos carregar, que eu já vou trazer isso para vocês em uma próxima aula, mostrar essa parte de lidar com fontes externas e tudo mais.

[09:15] Ele trouxe o sans-serif por default, tem essa de [ININTELIGÍVEL - SCREEN READER], esse sr-only, alguns ajustes do Next para o footer ficar sempre embaixo ali.

[09:25] Se carregarmos aqui, por enquanto o footer não está sempre embaixo, falta um pouco mais de coisas aqui, mas repara que ele já sumiu com esse padding da lateral. E agora podemos começar a aplicar outras coisas no nosso projeto.

[09:39] Essas outras coisas incluem trazer o código final da nossa tela inicial. Que, seguindo mais uma convenção, eu vou colocar dentro dessa pasta “screens”, que eu já tinha até previamente criado, no seu caso, você vai ter que criar. Vou até apagar aqui para simular junto com vocês.

[09:57] O “src” de vocês vai estar só “components” e a pasta “theme”, você vai criar aqui uma pasta chamada de “screens” e dentro dela uma pasta chamada de “HomeScreen”, e dentro um arquivo “index.js”.

[10:10] Aqui dentro eu vou pegar o arquivo que eu deixei pré-criado da nossa home, o mesmo que eu estou usando no outro código, tem só o link das imagens que vamos trabalhar numa próxima aula aqui.

[10:24] E uma vez que fizemos essa “HomeScreen”, podemos vir na nossa home, comentar tudo que fizemos até agora e só fazer o export dessa HomeScreen;. Fazemos o export default dessa HomeScreen que está dentro de screens aqui.

[10:42] Se eu salvar e carregar, está aparecendo aqui, não tem ainda o logo da Alura e a imagem, nós já vamos trazer isso, mas repara que está ficando já no mesmo estilo. Ajustei o espaçamento, está começando a ter mais a cara aqui. Tem algum ajuste de fonte para fazermos, mas calma, vai vir ainda.

[11:03] O importante que eu quero trazer é que aqui dentro eu fui repetindo essa estrutura, sempre pego uma caixa, boto padding nela, vou definindo baseado nos estilos. E repara que cada estilo já tem os breakpoints, evita de você ter que criar mais um arquivo para guardar o CSS, ajuda deixar a página mais dinâmica.

[11:21] Tem até um projeto open source que eu tenho puxado bastante, que é o SkynexUI, que ele tenta padronizar um pouco essa parte de estilo, que ele segue basicamente essa API aqui. Outros projetos também seguem, o próprio xstyled, que é um projeto bem famoso de CSS-in-JS, ele também segue essa estrutura de definir as coisas como propriedade.

[11:43] No meu caso aqui, estamos padronizando através desse styleSheet, que é uma prop que recebe tudo que vamos usar.

[11:53] Essa aula foi basicamente para ajustarmos os estilos do nosso projeto, para eu mostrar para vocês essa parte dos ícones, como carregamos as coisas, algumas coisas gerais. Mas por enquanto o nosso FAQ continua feio, mas a home já está bonita e na próxima aula veremos como lidar com essas imagens aqui, como baixá-las e ter os arquivos estáticos.

[12:18] Porque você pode ver que imagem externa, basta carregar o logo da Alura aqui como uma propriedade source num componente de imagem, que basicamente é uma tag `<Image`, se olharmos aqui, esse `<Image` aqui é basicamente um Image, ele segue aquela mesma estrutura do componente do título que fizemos no começo, ele recebe a tag como as aqui, passa um Image.

[12:45] E se inspecionarmos a página, ele só é uma imagem normal que tem o jsx, igual viemos fazendo até agora. Se você quiser explorar esse arquivo “components”, que eu passei para vocês, fique à vontade.

[12:58] O código que está aqui é bastante rico, tem bastante detalhe de fazer meta programação, de gerar componentes aqui, super recomendo. Mas para essa aula foi mais essa normalização, na próxima vemos os arquivos, então até já.

### Para saber mais: Organização de projeto

[YouTube: Como estruturar um projeto REACT]('https://www.youtube.com/watch?v=mJK5oGixSYo')

### Trabalhando com arquivos estáticos

1. Em public/robots.txt. Criamos o arquivo para auxiliar o google na localização da página.

        User-Agent: *
        Allow: *

---

[00:00] A nossa última aula foi um pouco mais pesada, tivemos que carregar muitos arquivos, ver muito contexto, mas agora acho que está mais claro e eu vou usar esse momento para dar uma revisada com vocês.

[00:10] Agora temos a pasta “pages”, que é do Next.js, e guarda o “app.js”, que é o arquivo que gerencia todos os nossos componentes de página, então tudo que vai renderizar no site passa pelo arquivo “app.js” e depois passa para aquela página. O usuário acessa, o primeiro arquivo que bate nele é o “_app.js” e depois tem o “404.js”, o “faq.js” e o “index.js”, de acordo com a URL que o usuário acessa.

[00:36] Como essa pasta “pages” é do Next, ela tem só os arquivos do Next, nós separamos todas as nossas páginas em si dentro dessa pasta de “screens”, de telas.

[00:46] Lá na pasta “src”, onde tem o nosso código-fonte, temos a nossa parte de “screens” e temos a nossa “HomeScreen” aqui dentro, com toda essa estrutura de CSS, esse esquema mais declarativo de montar que eu comentei com vocês. E deixei para vocês explorarem. Não é obrigatório para esse curso, se você quiser refazer do jeito que você achar melhor, segue o seu coração e faz aí.

[01:10] E vou até dar a dica antes de resolvermos essa parte das imagens, de que o próprio Next tem vários exemplos na documentação deles. Você pode vir aqui e procurar, por exemplo, por “sass”, e tem um exemplo de como usar o Next.js com Sass, o que você tem que ter no seu “package.json”, quais são as dependências que você tem que instalar.

[01:32] Ele também vai trazer um exemplo de como fica a pasta “pages”, ele importa aqui o componente, esse <HelloWorld />, e se navegarmos nesse HelloWorld, ele carrega um module.css, ele escreve aqui um CSS dele.

[01:52] Acho que eu troquei de exemplo. Perdão. Agora voltei. Para o de Sass e aqui dentro temos os componentes e ele tem aqui “.module.css”, ele está criando variável e tal. Então você está livre para usar o que você quiser, seja o tailwindcss, seja o styled components.

[02:18] Esse aqui, inclusive, eu já até contribuí com esse projeto, você pode ver a minha cara aqui. Realmente é super fácil de customizar as coisas com o Next e é só você olhar essa pasta de exemplos. “Quero usar com redux”, vai ter o exemplo com o redux aqui. “Quero usar com o graphql”, tem o exemplo com graphql. Então confia, segue aqui e vai.

[02:39] Mas por hora queremos servir os arquivos, ao invés de pegar de uma URL externa, pegar essas imagens e baixar no nosso projeto e servir por eles. Que é uma dúvida que muita gente tem, servir os arquivos estáticos. Que serve também para criar arquivo robots.txt, sitemap e vários outros que temos.

[02:58] Como faremos isso? Eu vou minimizar todas as pastas e vou criar uma nova chamada de “public”. “Mario, public?”. Se eu abrir agora o site da “alura.com.br” e eu procurar por “/robots.txt”, ele tem alguns arquivos que você controla para o robô do Google indexar ou não, é super importante.

[03:23] E para o Next, você ter isso aqui, basta você vir aqui à esquerda e criar esse arquivo dentro da pasta “public”, “robots.txt”. E aqui você pode pegar e colocar o User-Agent: *, para todos os buscadores, tem o do Google, do Bingo, da Microsoft. E botar para habilitar todos, você quer habilitar todo mundo, Allow: *.

[03:50] E você pode desabilitar algumas páginas, enfim, você escolhe o que você quer habilitar ou desabilitar. Mas na prática, só de ter criado esse arquivo e eu botar aqui na barra de endereço “localhost:3000/robots.txt”, nós não conseguimos acessá-lo. Não conseguimos porque o projeto não está rodando.

[04:10] Se eu rodar yarn dev, está pronto, funcionando. Olha que maravilha. E não só ele. Se quisermos pegar, por exemplo, essa imagem aqui do Alura Cases, eu vou basicamente clicar para salvar, então vou expandir, eu vou salvar no meu desktop.

[04:28] Minto, eu vou salvar dentro da pasta do projeto já, então vai ser dentro de “dev > alura > 01-nextjs-course > public” e vou salvar a imagem do Alura Cases.

[04:40] Não só ela, eu vou salvar também o logo da Alura em SVG, esse logo da cor preta. Então clico para salvar e dentro da mesma pasta que estávamos agora há pouco, eu vou salvar o “alura-logo”.

[04:53] Fechei essa URL, fechei essa, fechei também o projeto base que estávamos comparando até agora o tempo todo, vou fechá-lo aqui. Vou fechar o site da Alura e vamos a partir do nosso aqui.

[05:06] O que eu vou fazer agora? Temos as duas imagens que eu salvei aqui e para não virar bagunça, eu vou organizá-las com vocês. Vou criar a pasta “images” e vou jogar aqui dentro essas duas imagens.

[05:20] Agora, se eu clicar com direito em “alura-logo”, colocar “Copy Relative Path” e colar depois aqui da URL, ele deu 404, por quê? Porque nós copiamos o nome da pasta public, a pasta public vai embora, você pode ignorá-lo sempre. E ele já acessa a imagem que você colocou.

[05:41] A pasta public é só onde você guarda, mas na URL ela não reflete em nada, você pode escrever tranquilamente. Tanto que eu posso vir agora no nosso arquivo do “screens > index.js” e mudar a URL do logo da Alura, para pegar a URL sem o public, só ’/images/alura-logo.svg’;.

[06:00] E se voltarmos na nossa home, logo depois de eu salvar aqui, ele trocou. E essa imagem do lado é a mesma coisa, clico na pasta “public”, abro “images”, clico no “alura-cases.png” com o direito, “Copy Relative Path”, colo no nosso SIDE_IMAGE_URL. Só que ao invés de public, deixo só o ’/images, dentro da pasta public. E nós conseguimos ter a nossa imagem carregando e você consegue colocar qualquer arquivo ali dentro.

[06:40] Se você quiser gerar algum arquivo, tiver algum script para gerar, por exemplo, o sitemap, que o da Alura tem também, “alura.com.br/sitemap.xml”. No caso, o da Alura não tem, mas podemos fazer uma busca no Google por “sitemap.xml” e você pode ver alguns casos aqui.

[07:03] Deixa eu pegar algum outro site, por exemplo, esse da Rock Content. Vamos acessar o “/robots.txt” deles, beleza. E vamos ver se eles têm o “/sitemap.xml”. Aqui apareceu.

[07:23] Que normalmente é um arquivo que você gera com todas as URLs que você tem no seu site. Esse sitemap.xml normalmente é para isso. É um arquivo que você gera, então você não tem obrigação de fazer CSS nele.

[07:34] Normalmente o pessoal de SEO da empresa, de marketing, vai falar como você faz, e você pode ou criar na mão, igual fizemos o robots, ou você cria de acordo com o que o pessoal te pedir, procura no Google, segue tutorial e tudo mais.

[07:48] Essa foi a dica de como lidar com arquivos estáticos e como fazemos para dar essa revisada na nossa estrutura, que está ficando mais complexa e com mais cara de projeto do dia a dia. Então até o próximo vídeo, onde vamos começar a explorar mais recursos do Next.js em si.

[08:05] Vamos começar a abordar a parte que confunde muita gente, que é o tal Server Side Render, vamos começar a trabalhar com essa parte de Server Render, vamos trabalhar com getStaticProps, que é um valor que muita gente ouve. Vai ter também o getServerSideProps. Vai ter muita coisa, mas nas próximas aulas aqui do curso, vejo você em breve. Até mais.

### Arquivos estáticos

Você recebeu uma tarefa de adicionar ícones no projeto. A equipe de design te passou alguns arquivos svg para serem utilizados e foi decidido que esses arquivos devem ser colocados dentro de uma pasta chamada icones.

Onde essa pasta deve ser colocada e como os arquivos devem ser referenciados no código?

a) **Alternativa correta:** Dentro da pasta public na raiz do projeto.
- const srcDoIcone = “/icones/nome-do-icone.svg”
- _Alternativa Correta! Arquivos estáticos e imagens devem ser colocadas dentro da pasta public. Para referenciar o arquivo dentro dessa pasta, devemos começar o caminho com “/” e também colocar a extensão no final._

b) Dentro da pasta src.
- const srcDoIcone = “src/icones/nome-do-icone.svg”

c) Dentro da pasta public.
- const srcDoIcone = “/public/icones/nome-do-icone.svg”
- _O caminho não deve começar com a palavra “public”._

d) Dentro da pasta public.
- const srcDoIcone = “/icones/nome-do-icone”
- _Além do caminho relativo à pasta public, devemos também informar a extensão do arquivo._

### O que aprendemos?

- Estilização no Next.js
  - Existem diversas maneiras de estilizar sua aplicação Next.js e você é livre para escolher a que mais lhe agrada.
- Arquitetura de aplicação
  - Podemos criar novas pastas para agrupar componentes com propósitos semelhantes.
- Lidar com arquivos estáticos
  - Conseguimos acessar os arquivos dentro da pasta public diretamente pela URL da aplicação.

## 4. Dados dinâmicos no Next.js
### Preparando o ambiente: Recursos da aula 4

No próximo vídeo utilizaremos a [URL]('https://gist.githubusercontent.com/omariosouto/0ceab54bdd8182cbd1a4549d32945c1a/raw/578ad1e8e5296fa048e3e7ff6b317f7497b31ad9/alura-cases-faq.json') para buscar os dados das páginas.

### [getStaticProps]('https://nextjs.org/docs/basic-features/data-fetching/get-static-props')

Método do NextJS que foca em performance de carregamento dos dados para carregar mais rápido um conteúdo da página.

---

[00:00] Agora que a nossa app está com mais cara de projeto profissional, está com um design bonito, nós conseguimos ver as coisas e tudo mais, chegou a hora de fazer a próxima parte dela, que é fazer o nosso FAQ funcionar.

[00:11] Num primeiro momento nós não vamos aplicar nenhum estilo, porque a ideia é fazermos esse FAQ funcionar pegando dados externos que vão vir de alguma API.

[00:21] O importante aqui é você saber que tudo que você já sabe de React, ou seja, usando useEffect, Affect Api e usando o Axios ou alguma outra lib que faça requisições para pegar dados, fica tranquilo que todo esse conhecimento vai ser reaproveitado aqui no Next também. Tudo que você já sabe de React funciona por padrão aqui.

[00:42] A vantagem é que o Next tem algumas funções a mais que nos ajudam a ter algumas vantagens, principalmente quando queremos trabalhar com performance.

[00:53] Pega a sua pipoca e vamos seguir aqui na aula, por conta do seguinte, antes de falar do recurso do Next, eu acho que é importante eu relembrar um pouco essa parte do próprio React puro, até para mostrar os contrapontos.

[01:08] Eu estou na página do FAQ agora, que, lembrando, não vou botar o estilo agora, nós vamos botar o estilo só depois. Então vou abrir aqui, vou minimizar todas as pastas, “pages > faq.js”. Está aqui.

[01:23] Num primeiro momento eu vou pegar a URL da API que vamos trabalhar, que vai trazer os dados. Repara que até o nosso boilerplate dá como pergunta 1, pergunta 2. O pessoal do conteúdo foi atualizando aos poucos isso, então agora eu tenho em mãos a URL atual, que é essa aqui.

[01:44] Repara que até mudaram as perguntas, é até bom que a nossa versão vai estar mais atualizada e acho que as respostas vão atualizar depois também, então fica tranquilo que isso aqui ainda vai mudar.

[01:53] Mas por hora eu vou pegar essa URL e vou basicamente criar o useEffect() aqui dentro, já importei o react ali, vou criar uma função, vou falar que eu só quero que execute uma vez, quando o componente carrega. E aqui faremos o fetch() para a nossa const FAQ_API_URL, para deixar padronizado, igual estamos fazendo.

[02:26] Vamos pegar nossa FAQ_API_URL e vou aqui embaixo fazer um .then para observarmos a resposta, então .then((respostaDoServidor) => {, console.log(respostaDoServidor); e vamos ver no que deu isso.

[02:47] Carreguei o site, eu estou com o console aqui aberto já, vou dar um zoom. Você que usa Axios, eu sei que você pula essa etapa, mas eu quero mostrar só para falar que aqui nós não temos o conteúdo inteiro, ele está nesse ReadableStream.

[03:03] Eu preciso pegar essa respostaDoServidor e falar que se vier JSON disso, converte para mim para um objeto do JavaScript, return respostaDoServidor.json();. E aqui embaixo temos a resposta para valer, .then((resposta) => {. Então venho aqui agora e console.log(resposta);.

[03:27] Agora sim, um array com três objetos, com resposta e pergunta, é exatamente o que precisávamos. Para fazer isso aparecer na tela, precisamos de um state, então vou ter que vir aqui, const [faq, setFaq] =, vai ser um useState([]); que no começo vai ser um array.

[03:52] E aqui embaixo eu vou botar até uma `<div>` para separarmos. Ou melhor do que uma div, vou botar só uma `<ul>` e vou botar `{<li></li>}` aqui embaixo. E nós vamos fazer {faq.map(() => e para cada item do map vamos retornar uma li pegando aqui, porque temos o answer e a question, ou seja, a resposta e a pergunta. {faq.map(({ answer, question }) =>.

[04:30] Dá até para quebrarmos de linha melhor, botar o `<li></li>` aqui embaixo. Vamos botar só {question} no momento, só para debugarmos aqui.

[04:45] Recarregou, e não aconteceu nada, porque eu só desenhei aqui, mas eu não setei o status, então depois que pega a resposta temos que fazer o setFaq(resposta);.

[05:00] Ele reclamou, tinha que ter uma unique key em cada valor, então vamos pegar a pergunta e botar como `<li key={question}>`. Poderíamos ter algum ID, alguma coisa, mas por enquanto só temos a pergunta mesmo, cada uma é única, então vai resolver para nós.

[05:15] “Quem tem acesso?”, “Existe algum certificado?” já está renderizando. Dá até para virmos além e botarmos aqui dentro do li um `<h2>{question}</h2>`, e botar aqui um `<article>`, porque teremos essa pergunta inteira.

[05:29] Isso é código natural, o que você já está acostumado de fazer quando trabalha com React, aqui vai se repetir da mesma forma, basicamente só renderizamos aqui o código agora.

[05:46] O que muda? Se analisarmos esse código, carreguei a página, está vendo que ele dá uma piscada? Eu vou até forçá-la, eu venho no código e ao invés de fazer o set imediatamente, eu vou dar um setTimeout(() => {. E nesse setTimeout eu vou passar que eu quero que ele demore três segundos, que é 3 * 1000); milissegundos.

[06:16] Três segundos depois ele trouxe a nossa resposta. O que isso impacta? Lá no começo eu mostrei aquele tal de Web Vitals, que são aqueles links de performance do Google. Eu vou até tentar abrir primariamente essa parte do Web Vitals, ele é muito sobre as métricas.

[06:40] Por exemplo, aqui temos o Largest Contentful Paint, o que isso impacta? Eu não vou entrar no detalhe do número, eu vou entrar só como fazemos para ter essa percepção e você pode se aprofundar lá nos cursos de performance, como fazer essa microanálise e usar os recursos do navegador. Eu já deixei essa dica logo no começo do curso para vocês.

[07:00] Mas é importante dizer que quando estamos carregando, aqui no nosso projeto, esse tempo que ele demora para trazer o conteúdo impacta no tempo que o usuário demora para ver o conteúdo aparecendo na página, impacta muito nesse de loading, do Largest Contentful Paint.

[07:21] Quanto mais rápido o usuário tiver acesso ao conteúdo que ele mais vai utilizar na página, melhor para a experiência do usuário e para a performance.

[07:29] Se abrirmos, por exemplo, o YouTube, eu vou até dar um “Mute Site” na aba e abrir aqui um vídeo. Repara que o YouTube baixa primeiro o vídeo e depois os outros pedaços.

[07:42] No nosso caso, só temos texto, mas se quiséssemos fazer uma coisa carregar por padrão e não ter esse loading aqui, do jeito normal do React, a coisa precisa precisaria estar aqui no meio do código, chumbada no código.

[07:54] E por padrão, no React, você sempre vai ter o seu Largest Contentful Paint um pouco demorado, por quê? Porque depende de processar o JavaScript, acessar a API, baixar o conteúdo, para só depois o usuário ver alguma coisa na tela. Então impacta diretamente na parte do carregamento aqui.

[08:12] “Mario, por que você está falando isso?”, eu estou falando isso porque o Next traz uma proposta para conseguirmos fazer algo que nem o YouTube faz, para conseguirmos seccionar. Você trazer um pedaço primeiro e os outros depois.

[08:24] Quer dizer que você não vai deixar de usar o Fetch, mas o Next vai te dar um auxílio para você contornar um problema que o React tem, que é essa renderização inicial que, inclusive, impacta em SEO também.

[08:36] Porque se olharmos o navegador e eu der um “View Page Source”, por exemplo, repara que ele não tem nenhum conteúdo aqui, ele não tem a nossa UL. Minto, ele tem a UL, mas ela está vazia, ele não tem nenhum conteúdo dentro dessa parte. Eu posso até dar um zoom para facilitar, mas a UL está vazia aqui.

[08:59] Minha missão aqui com vocês agora vai ser fazer isso vir pré-preenchido. Como fazemos isso? Vamos na documentação, Next, getStaticProps, e eu vou copiar essa função aqui, getStaticProps.

[09:15] Para que ela serve? O que ela faz? Eu vou botá-la até aqui em cima do nosso FAQPage(). Por enquanto esse (context) nós não vamos usar, esse é um curso mais inicial, não vamos nos aprofundar tanto nessas coisas mais internas do Next, vai ser em outros cursos.

[09:34] Mas aqui podemos ler até a dica que o próprio Next dá, isso aqui vai ser passado como props para o seu componente de página. O que isso quer dizer? qualquercoisa: ‘que eu passar aqui’ vai ser recebido como prop aqui embaixo. Esse objeto vai ser copiado e vai ser passado para cá, FAQPage(), no nosso componente.

[10:04] Se eu der um console.log(props); aqui, repara que “qualquer coisa que eu passar aqui” foi injetado no nosso componente, ele foi carregado ali e nós estamos recebendo esse valor.

[10:26] O que isso impacta? Eu posso dar o “View Page Source” e se eu procurar por “qualquercoisa”, repara que existe um script chamado NEXT DATA que tem acesso a essas props iniciais que eu passei ali.

[10:45] Se eu der um zoom maior, esse valor do “qualquercoisa” está sendo carregado aqui na página de alguma forma. Coisa que as nossas perguntas, o “Quem tem acesso?” não está sendo.

[10:59] O que podemos fazer para inverter esse jogo? De alguma forma esse getStaticProps() do Next fez a coisa funcionar, então alguma magia ele está fazendo acontecer aqui.

[11:08] Vamos tentar trocar agora, esse fetch(FAQ_API_URL), não vamos mais fazê-lo via useEffect, vamos copiar esse código daqui, dar um “Ctrl + X” nele, vou comentar essa parte de baixo e agora eu vou colá-lo aqui no getStaticProps().

[11:31] E como isso aqui é async, podemos fazer o return da nossa resposta; e aqui em cima, const faq = await fetch(FAQ_API_URL), e agora nós pegamos no props as respostas do FAQ.

[11:52] E nesse props agora teremos o nosso faq, FAQPage({ faq }), console.log(faq);. “Como assim, Mario? O que você está fazendo?”. Vamos que você já vai ver.

[12:06] Carreguei a página, nosso conteúdo está aqui. No console ele também apareceu, o console.log que eu botei está mostrando aqui. E o mais legal é que se eu carregar o view page source, antes não tinha o “Quem tem acesso?”, se eu procurar, agora tem. Tanto no `<h2>`, dentro da nossa `<ul>`, que antes estava vazia, quanto no “Quem tem acesso?”. Esse objeto aqui que é carregado nesse NEXT DATA.

[12:38] Como funciona? O Next por debaixo dos panos tenta sincronizar todos os dados que estão nesse NEXT DATA que nós conseguimos ver até pelo próprio script aqui, deixa eu tentar achá-lo aqui no meio, “NEXT_DATA”.

[12:58] O Next pré-monta esse script que tem as coisas aqui, ele joga o dado direto na página e ele carrega para nós a informação e ele tenta sincronizar, é como se ele desenhasse o HTML inicial e esse conteúdo, e ele tenta validar com o React, para ver se ele precisa renderizar algum conteúdo extra.

[13:16] É um trabalho que o Next faz junto com o React, usando a função de Server Side Rendering, e por debaixo dos panos ele faz tudo isso aqui tudo funcionar bonito, tudo certo.

[13:26] O que é o mais legal disso? Do jeito que ele está fazendo, quando fazemos aquele nosso build, ele vai gerar a versão estática desse conteúdo, ou seja, ele vai gerar um HTML que vai ter todo aquele conteúdo direto.

[13:39] Ou seja, quando o nosso usuário acessar a página, ele vai vir aqui no FAQ, abriu, não vai ter tempo de loading, vai carregar instantaneamente, que é a mesma coisa que o YouTube faz com a parte do vídeo dele.

[13:51] E com isso você pode usar o Next para pré-carregar o conteúdo mais importante e carregar depois algo que o usuário vai ver depois, te dá mais poder de conseguir trabalhar com o React de uma forma eficiente, focando em performance e, principalmente, pensando nessa métrica de loading dos Web Vitals.

[14:09] Esse vídeo ficou um pouco maior, mas eu queria trazer esse contexto num vídeo só para vocês, para vocês conseguirem ver e aprender.

[14:19] Nos vemos no próximo vídeo, que vamos nos aprofundar um pouco mais nessa questão de pegar conteúdo dinamicamente do Next, que tem alguns detalhes importantíssimos de perceber. Até já.

### [getServerSideProps]('https://nextjs.org/docs/basic-features/data-fetching/get-server-side-props')

1. Fazer um novo build do site getStaticProps:

        yarn export

2. Com o getServerSideProps:

        yarn build && yarn start

- **getServerSideProps:** roda a cada acesso que vc recebe;
- **getStaticProps:** roda somente em build time;

3. Teste para verificar onde esta rodando:

        console.log('Texto para ser impresso.')

---

[00:00] Eu tenho certeza que você viu o getStaticProps na última aula e provavelmente deve tê-lo achado muito legal, você falou: “Nossa, esse getStaticProps realmente parece que resolve esse problema de SEO, de performance, de carregar as coisas antes. Mas, Mario, como ele funciona?”. Vamos nos aprofundar agora.

[00:18] Eu vou até mostrar a dupla do getStaticProps – eu vou até duplicar a aba para ficar mais fácil de navegarmos – que é o getServerSideProps. E vou explicar também como conseguimos não nos perder trabalhando com o Next.js, que é uma coisa importante.

[00:38] Primeiro de tudo, o getStaticProps surge para você fazer sites estáticos, sites que você vai publicar dentro do GitHub Pages, num bucket do S3 da Amazon ou até mesmo no seu servidor customizado.

[00:51] É na mesma pegada da pasta “out” aqui, ou seja, sempre que você usar o getStaticProps, pensa que o conteúdo que você está trabalhando nunca vai ser alterado, por mais que o conteúdo da API mude. Você vai precisar fazer um novo build do site para isso aqui mudar. Eu vou mostrar mais na prática.

[01:12] Deixa eu vir aqui no terminal e fazer um yarn export, que é aquele comando que tínhamos, que gerava o site. Se eu fizer um yarn export, repara que ele até mostra aqui, no próprio build do Next ele nos ensina como ele está buildando as coisas.

[01:34] Ele tem aqui o /faq, que está sendo buildado com essa bolinha branca, quer dizer Static Site Generator. Ele está usando o getStaticProps e ele consegue fazer uma gestão que ele usa uns JSONs e algumas coisas do Next para fazer com que, mesmo que o site seja buildado. No caso, eu desliguei aqui.

[01:58] Deixa eu até subir aquele npx http-server ./out -c-1, na pasta “out”, só para conseguirmos ver o que eu falei agora. Vou abrir, ao invés de “localhost:3000”, o “localhost:8080”.

[02:11] Para conseguir fazer a navegação entre páginas no modo SPA, se eu começar pela home e limpar aqui, quando vamos para a página nova, ele tem que baixar, em teoria, só o essencial, para conseguir carregar outra página.

[02:30] No caso, como tem pouca coisa, ele está até nem baixando, ele está baixando tudo junto, mas conforme o projeto vai crescendo, o Next tem estratégias de ir quebrando os conteúdos para nós.

[02:41] Ele faz de uma forma esperta as coisas aqui, eu posso até trocar aqui. Ele tem aqui o faq.json, exatamente isso. Ele traz todas as informações que passamos, agora deu para mostrar mais bonito.

[02:56] E o lance é esse, gerou estático, ele vai gerar essa pasta aqui, “_next”, e é só essa pasta, ele nunca vai pegar algo dinâmico. Se a API cair fora do ar, se acontecer qualquer coisa, o seu código vai estar de pé, do mesmo jeito que ele estava.

[03:08] Isso só funciona para as coisas que botamos no getStaticProps, ou seja, o conteúdo que você quer carregar quando a aplicação recarregar.

[03:18] Eu estou fazendo essa tour para explicar, porque com isso você consegue trabalhar no modelo da Jamstack, que é aquele modelo que o pessoal falava de você trabalhar com JavaScript, código assíncrono e Markdown, você conseguir pegar conteúdo dinâmico e renderizar, o Next é um dos principais players favoritos para isso, ainda é hoje.

[03:40] E a vantagem de ter tudo estático é que a infraestrutura fica mais barata, você consegue botar cache em tudo e você consegue botar um CloudFront da vida, uma CloudFlare, você consegue hospedar o site no GitHub Pages, hospedar dentro dos buckets do S3, tem várias estratégias de hospedagem para lidar com isso que são baratas.

[03:58] Se você procurar lá na parte de precificação, são mais baratas perto de subir uma máquina [ININTELIGÍVEL] servidor, hospedar as coisas, começa a virar uma infra mais complexa que exige monitoramento, às vezes cai do nada, enfim, tem várias coisas que podem acontecer. E com a parte dos estáticos facilita.

[04:18] Você pode fazer o seu site de campanha, até o seu blog você conseguiria fazer nessa estratégia aqui. Funciona bem, super bacana, eu indico bastante.

[04:28] Algumas vezes você quer que: “A página do FAQ precisa estar em sincronia com... se mudar o conteúdo desse FAQ eu preciso conseguir pegar versão mais recente dele. Como fazemos isso, Mario?”.

[04:41] Fazemos da seguinte forma, esse getStaticProps também pode ser esse getServerSideProps. E como funciona? Se eu colar getServerSideProps no lugar de getStaticProps e tentar fazer aquele yarn export de novo, repara que ele quebrou, ele não vai conseguir. Por quê? Porque o yarn export, que é o que gera todo o projeto estático, você não pode ter nenhum comando que rode toda vez que o usuário acessar a página.

[05:17] Ou seja, em tempo de build, quando estamos rodando o projeto, quando eu venho aqui, getStaticProps(), vou colocar console.log(‘Rodando no build’), yarn build. Vai rodar o nosso log aqui.

[05:38] Rodou muito mais coisa, deixa eu comentar esse faq que tem aqui embaixo e vou colocar o rodando no build agora. yarn build, cadê? Ficou perdido, mas está aqui, “Rodando no build”. Ou seja, esse getStaticProps é rodado no build e só no build, nunca mais.

[06:03] Por outro lado, se usarmos o getServerSideProps, o yarn export para de funcionar e o único jeito que teremos de rodar o nosso projeto é rodando yarn build && yarn start. Que é pior? Não, inclusive é a forma que o Next recomenda que você rode o projeto [ININTELIGÍVEL - NO GERAL], porque você tira todas as vantagens de usar o Next no geral.

[06:39] Essa página do FAQ agora, se eu vier no navegador e acessar o “localhost:3000”, quando eu abrir aqui, repara que ele não está rodando só no build mais, toda vez que eu dou um page load, ele roda mais uma vez.

[07:03] Como funciona isso? O getServerSideProps roda a cada acesso que você recebe. Enquanto o getStaticProps roda somente em build time. Deu para pegar essa ideia?

[07:32] Eu estou tentando explicar com calma e fazendo essa tour, porque é importante. Eu vou até apagar essa parte do useState do React, nós não vamos trabalhar aqui no projeto, eu vou até deixar mais limpo.

[07:44] Mas eu acho importante vocês terem clareza disso, porque se você estiver hospedando no servidor ou hospedando na Vercel, como faremos no último módulo, você pode usar tranquilamente o getServerProps, porque o servidor vai gerenciar e você recebe a requisição.

[07:58] Mas no geral, sempre prefira ter a página estática. Só a faça dinâmica se você precisar que ela seja dinâmica, acho que esse é um aviso bem importante de ter, porque o estático sempre vai ter a resposta mais rápida e sempre vai chegar mais rápido para o usuário, por questões de disponibilidade, de poder cachear, tem n pontos em cima disso. Para um site mais normal getStaticProps resolve, precisou de mais coisas dinâmicas, getServerSideProps.

[08:23] Vou rodar agora o mesmo comando, yarn build && yarn start, para você ver que quando usamos o getStaticProps, ele vai rodar uma vez no build time, roda somente em build time. E toda vez que eu acesso a página de novo, ele não roda mais a função. Você está vendo na prática como funciona. Quando está buildando o projeto, tem esses dois casos.

[08:52] “Mario, e quando eu estou desenvolvendo?”. yarn dev, vamos abrir o navegador agora, acessei. Em desenvolvimento, cada uma dessas funções sempre vai rodar. Eu vou até deixar outro comentário, (‘Em modo DEV, sempre roda! A cada acesso’). A mesma coisa para o getStaticProps, em modo dev sempre roda a cada acesso.

[09:24] Eu espero que isso tenha ajudado você, porque essa parte é um grande poder do Next.js, mas entender quando cada uma dessas funções roda é uma coisa que buga muito a cabeça e demora para entender.

[09:38] Sempre que você estiver com dúvida, bota um console.log, está rodando onde? E vai testando. Está rodando o FAQPage, se eu der console.log(‘Isso roda no servidor???’), carrego a página, rodou no navegador.

[09:58] Só que ele rodou também aqui no servidor, por quê? Porque esse componente precisa ser pré-carregado em tempo de build, no modo de desenvolvimento, ou no build para produção ou quando acessa a página usando serverSideProps, porque o servidor do Next precisa saber qual é o HTML.

[10:16] Pelo menos uma vez ele precisa rodar esse código aqui e saber, “É esse código que eu mando para o navegador”, então está em modo dev? Mudou alguma coisa? Atualiza esse código para mim. Na dúvida, sempre roda um console.log, que eu acho que é o melhor caminho para você conseguir se virar e entender.

[10:32] Essas duas funções aqui, recapitulando, é sempre esses dois casos que eu coloquei, o getServerSideProps em dev o tempo todo e a cada acesso que você recebe em prod. StaticProps em dev o tempo todo e somente no tempo de build, ou seja, buildou o projeto, ele baixa o conteúdo e não vai mudar mais, até você fazer outro build.

[10:56] Já a parte do FAQ vai variar, mas no geral vai sempre rodar no navegador e uma vez no build time ou no servidor, caso você esteja rodando a página no Server Render.

[11:07] E aqui é até bom para falarmos os diferentes tipos de nomes que tem. Se você ver por aí Static Site Generator é SSG. Se você ver SSR, é igual a Server Side Rendering. Você pode ver diferentes nomes. Tem até outro, que é o Incremental Static Generation, seria até o ISG. O Next traz várias dessas siglas, eu quero que você não se confunda.

[11:41] O Incremental é como se fosse uma mistura desses dois aqui, o SSG e o SSR, que nós não veremos por hora nesse curso, mas você pode procurar no Google e explorar, a ideia aqui era só passar esse modo de debug para você conseguir entender o que você está fazendo e trabalhar com mais tranquilidade nos seus projetos.

[11:59] Para essa aula é só, até a próxima. Lembrando que na próxima começaremos a mexer no head das páginas, vamos carregar a fonte do projeto também, que não estamos carregando aqui a oficial. Tem bastante coisa legal, fica aí, nos vemos já.

### Exercício: Busca de dados

Sua empresa lançará um novo produto e você será responsável por montar o site de apresentação e venda.

O site será composto por 2 páginas: a página inicial e um painel de controle.

A página inicial terá os seguintes requisitos:

= Ser atrativa visualmente para os clientes;
= Ter bom SEO para aparecer nas pesquisas dos motores de busca;
= Ter um baixo tempo de carregamento;
= Descrever o produto;
= Redirecionar para a parte de compra (que será desenvolvido por outra equipe);
= Uma vez pronta, serão necessários pequenos ou quase nenhum ajuste.

O painel de controle terá os seguintes requisitos:

- Mostrar os dados de venda atualizados;
- A informação deve ser personalizada para cada cargo (vendedor, administrador, patrocinador etc);
- Não deverá ser visto pelos motores de busca nem pelos clientes;
- O tempo de carregamento não é prioridade.

Após analisar os requisitos, você percebeu que o Next.js fornece as ferramentas necessárias para atendê-los bem.

Qual é a estratégia de busca de dados ideal para a página inicial e do painel de controle, respectivamente?

a) **Alternativa correta:** SSG e SSR.
- _Alternativa correta! O ponto forte do SSG é a entrega rápida de conteúdos estáticos, então ele é a melhor estratégia para a página inicial. Com o SSR, você poderá construir um painel de controle personalizado e atualizado para cada requisição._

b) SSR e SSG.

c) Ambos SSR.

d) Ambos SSG.

### Como manipular o Head das páginas

[00:00] Agora que já vimos o core do Next.js, que é o getStaticProps e o getServerSideProps, chegou a hora de começarmos a colocar mais detalhes no nosso projeto que todo projeto tem que ter, seja ele Server Side ou estático, você vai querer customizar esses valores também.

[00:17] O nosso próximo passo aqui vai ser ajustar tanto o title da nossa página quanto carregar a fonte oficial que temos, porque se eu abrir aqui, esse site tem a fonte mais redonda, mais bonita e o nosso está com a fonte meio estranha, meio diferente.

[00:33] Para fazer isso, vamos usar um recurso do Next que é o next/head, é o componente do Next para lidar com o cabeçalho das nossas páginas. Como vamos trabalhar com ele?

[00:43] Basicamente eu vou copiá-lo, import Head from ‘next/head’, e você pode pegar, por exemplo, a home, vou pegar nossa home page. Está aqui nossa home page. Eu vou até abrir o HomeScreen, que é onde está todo o nosso código da home agora. Vou minimizar esse SideImage aqui no VS Code e vou fazer o nosso import, vou importar. import Head from ‘next/head’.

[01:09] Para funcionar parece que é super complexo, mas basta você vir no meio da sua página e chamar o código assim, `<Head>`, e você passar o código que você quer carregar. Aqui eu vou colocar `<title>Home - Alura Cases Campanha</title>`. Só de botar isso, nós conseguimos mudar o head da nossa página.

[01:36] Mudou rápido, não sei se você percebeu, mas aqui, tirei o `<Head>`, “localhost:3000”, voltei com o `<Head>`, mudou nossa página aqui também.

[01:46] Isso pode se aplicar para o FAQ. Podemos vir aqui e no FAQ colocar também os ajustes para o head aparecer. Aqui seria o `<title>FAQ - Alura Cases Campanha</title>` e precisamos importar o Head dentro da nossa página do FAQ. E vocês vão ver que tanto a home quanto o FAQ, quando nós mudamos ele muda aqui na barra também e funciona tranquilamente.

[02:22] Outra coisa que dá para fazermos, agora que sabemos disso, é carregar as fontes para todas as páginas. Eu vou no Google Fonts, já está aberto o site do Open Sans, eu vou fazer um crime aqui, eu vou baixar todos os tamanhos.

[02:36] O ideal é que no seu projeto você tenha pré-selecionado quais tamanhos você vai usar para baixar menos conteúdo, não gastar tanto a rede do usuário, mas aqui estamos no modo experimental, testando, eu vou botar tudo.

[02:48] E eu vou copiar essa tag link que ele gera aqui à direita, para baixarmos. E o ideal é que uma tag link você sempre bote dentro do head da página. No caso, eu quero que todas as páginas carreguem, então eu vou no nosso “_app.js”, vou escrever aqui dentro `<Head>`, vou colar esse conteúdo aqui dentro.

[03:12] Fica ligado, você vai precisar fechar a tag que você está copiando. Inclusive, cada uma das linhas eu precisei fechar por conta do JSX do React.

[03:23] Agora que estamos carregando aqui a fonte, falta importarmos o import Head from ‘next/head’;, e nosso texto agora está com a cara do nosso projeto base, olha só que bonito.

[03:40] Se não baixarmos a fonte, se eu vier aqui e comentar isso, bagunçou tudo. Voltou a fonte, tudo funciona normal como esperávamos. E vindo para o FAQ, como carregamos no “_app.js”, carrega para todas as nossas páginas e agora mais um recurso do Next que estamos usando, otimizando e fazendo valer no nosso projeto.

[04:01] No próximo veremos como carregar scripts externos, tem alguns outros cuidados que temos que tomar, mas também vamos ao head e a outros recursos aqui do Next. Vejo você na nossa próxima aula.

### Faça como eu fiz: Encapsulamento do title

Na aula 1 você criou o seu próprio <Link> para ter melhor controle sobre o componente que é fornecido pelo framework.

Que tal fazer o mesmo para controlar o título de cada página? Utilize seus conhecimentos sobre componentes React e o que foi aprendido no vídeo anterior para criar o componente PageTitle.

Este componente deve possibilitar a modificação do título da página.

#### VER OPINIÃO DO INSTRUTOR

Opinião do instrutor

1) Importe o Head de “next/head”.

2) Crie o componente PageTitle que aceita a prop children.

3) Faça com que o componente retorne children dentro de `<title>` e `<Head>` como visto em vídeo.

4) Não se esqueça de exportar o componente.

        import Head from 'next/head';

        function PageTitle({ children }) {
          return (
            <Head>
              <title>{children}</title>
            </Head>
          );
        }

        export default PageTitle;

5) Importe o PageTitle na HomeScreen e substitua o código:

        <Head>
                <title>Home - Alura Cases Campanha</title>
        </Head>

Por

        <PageTitle>Home - Alura Cases Campanha</PageTitle>


6) Importe o PageTitle no faq.js e substitua o código:

        <Head>
               <title>FAQ - Alura Cases Campanha</title>
        </Head>

Por

         <PageTitle>FAQ - Alura Cases Campanha</PageTitle>

### Para saber mais: Referências da aula

- getStaticProps [(Static Generation)]('https://nextjs.org/docs/basic-features/data-fetching#getstaticprops-static-generation')
- [useEffect]('https://pt-br.reactjs.org/docs/hooks-reference.html#useeffect')
- [Web.dev - Web Vitals]('https://web.dev/i18n/pt/vitals/')
- getServerSideProps [(Server-side Rendering)]('https://nextjs.org/docs/basic-features/data-fetching#getserversideprops-server-side-rendering')
- [Jamstack]('https://jamstack.org/')
- SSG - Static Site Generation
- SSR - Server Side Rendering
- ISG - Incremental Static Generation

### O que aprendemos?

- getStaticProps
  - Essa função busca os dados durante o build. Ou seja, essa função é executada apenas uma vez.
- getServerSideProps
  - Essa função busca os dados do lado do servidor para cada requisição.
- Ao modificar o título da página
  - Com o componente <Head> conseguimos editar os metadados de cada página, como, por exemplo, o título.

## 5. Publicando seu projeto
### Projeto da aula anterior
### next.config.js e Redirects
### Preparando o ambiente: Recursos da aula 5
### Publicando na vercel
### Publicação do projeto
### Faça como eu fiz: SSR e SSG
### Para saber mais: Referências da aula
### Projeto final do curso
### O que aprendemos?
