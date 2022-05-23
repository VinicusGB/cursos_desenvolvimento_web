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
### Projeto da aula anterior
### Entendendo o Build do Next.js
### SEO na prática
### Sobre o Next.js
### Faça como eu fiz: create-next-app
### O que aprendemos?
## 3. Estilizando o projeto
### Projeto da aula anterior
### Onde colocar meu CSS?
### Como lidar com estilos globais
### Preparando o ambiente: Recursos da aula 3
### Componentes do layout
### Para saber mais: Organização de projeto
### Trabalhando com arquivos estáticos
### Faça como eu fiz: Pegar imagens do projeto
### Arquivos estáticos
### O que aprendemos?
## 4. Dados dinâmicos no Next.js
### Projeto da aula anterior
### Preparando o ambiente: Recursos da aula 4
### getStaticProps
### getServerSideProps
### Busca de dados
### Como manipular o Head das páginas
### Next e Google Analytics
### Faça como eu fiz: Encapsulamento do title
### Para saber mais: Referências da aula
### O que aprendemos?
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
