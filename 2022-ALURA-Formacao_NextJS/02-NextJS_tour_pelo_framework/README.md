# Next.js: tour pelo Next.js - 10h
**Instrutor:** Mario Souto
**Disponível:** [Alura]('https://cursos.alura.com.br/course/next-js-tour-next-js')
**Conteúdo:**
- Aprenda a criar rotas dinânicas
- Conheça as estratégias de pré-renderização do Next.js
- Entenda como os recursos do Next.js ajudam na performance da sua aplicação
- Saiba como é possível gerar rotas de API com o Next.js
- Realize o deploy da sua aplicação

## 1. O desenvolvimento Front-end Ver primeiro vídeo
### Apresentação

[00:00] Olá, pessoas, eu sou Mario Souto, diretamente do canal “Dev Soutinho” em parceria com a Alura, para trazer para você esse curso sensacional, fazendo uma tour pelo Next.js.

[00:10] Sim, você não leu errado, vamos fazer uma tour pelo Next. Esse, que é o framework que está proporcionando uma das melhores experiências de desenvolvimento front-end que já tivemos, e a minha ideia nesse curso é tirar aquela dúvida que eu sei que todo mundo tem, que é: Dá para usar Next se eu for fazer um site, se eu for fazer um blog, se eu for fazer um e-commerce? Que tipo de projeto faz sentido usar Next.js?

[00:32] A minha ideia não é construir um projeto do zero e fazê-lo até o deploy, mas sim ensinar você a entender quais são os cenários que você pode aplicar os recursos do Netx.js, e você, aí sim, conseguir entender e tirar as suas conclusões se ele faz sentido. Vamos fazer essa exploração e aprender mais sobre o Next.js comigo?

### 7 princípios para construir web apps

    LPC | FID | CLS

    Loading
        LPC - Largest Contentful Paint
        Tempo de carregamento da página
    Interactivity
        FID - First Input Delay
        Tempo de resposta as requisições dos usuários
    Visual Stability
        CLS - Cumulative Layout Shift
        Tempo de atualização da página

---

[00:00] E antes de começarmos a nos aprofundar no Next.js, e ver código, colocar a mão na massa, eu acho que é importante falar com você sobre alguns tópicos. Eu quero pegar um dos principais artigos, que o criador do Next.js fez, o Guillermo Rauch, e quero pegar também, uma coisa que hoje em dia é essencial para quem trabalha com web, tentando sair um pouco de números mágicos e vindo um pouco mais para métricas, vou falar de Web Vitals com vocês.

[00:23] Quando trabalhamos com programação, muito se ouve que você tem que fazer um código performático, seu código tem que rodar bem, mas eu acho que a performance pela performance, ela não faz sentido. Se você está otimizando alguma coisa, você precisa ter ciência de alguns pontos antes, que são os seguintes: Você precisa ter um acompanhamento disso, você precisa saber quanto você tem melhorando e você precisa ter noção do impacto que você está causando.

[00:48] Apagar uma função, criar uma classe, criar menos variáveis, é difícil metrificar essas coisas, são coisas que são complicadas de você entender. E a minha ideia é tentar mostrar no âmbito de web sites, como o Next como ferramenta vai te ajudar nisso, mas guiando em cima das coisas que eu vou te trazer nessa aula agora, e eu vou estar o tempo todo recapitulando e fazendo referências a elas.

[01:10] Então a primeira que eu vou trazer são os Web Vitals do Google. Que é um conjunto de métricas, em que elas se resumem basicamente 3 pontos que impactam muito a experiência das pessoas usando um site.

[01:24] O seu site pode até não ser o mais rápido do mundo, o melhor do mundo, mas ele precisa conseguir atingir essa métrica do LCP, em um número bom. Esse largest contentful paint, que é muito relativo, a renderização do seu conteúdo. Não só essa primeira parte, pensa que o seu site, em termos de web e de performance, ele é considerado como se ele fosse um jornal. Então essa primeira parte dele é chamada de conteúdo above the fold.

[01:53] O ideal é que o seu site pré-carregue esse CSS junto ou um pouco mais que é a segunda parte. Quanto mais rápido você conseguir carregar isso, melhor vai ser a sua pontuação nessa métrica de LCP. Porque quando o seu usuário abrir o seu site, ele vai conseguir deslizar a tela e vai conseguir ver que a aplicação carregou, que ela não está sendo preenchida conforme ele vai carregando, ou a parte de cima está pintada e o resto está com um monte de texto bizarro.

[02:22] É muito pensado na experiência. Eu vejo muito que as pessoas falam que os apps são muito bons, são legais. Mas se você for parar para pensar, todos os apps têm o LCP bom. Quando você abre um app, muito provavelmente, ele já tem todo o conteúdo pré-carregado, você não sente que as coisas estão sendo muito dinâmicas, a menos que seja uma lista muito grande, como o feed do Twitter ou do Facebook, mas ainda assim lá, você dificilmente vê algo carregando, ao menos que você scrolle muito rápido. No comportamento normal dos usuários, sempre vai ter alguma coisa próxima carregada ali.

[02:53] E com relação a ter alguma coisa próxima, é importante também essa questão de interatividade o first input delay, o quando que vai demorar para o seu usuário apertar um botão, para ele dar um clique em alguma coisa. Isso é uma coisa que o Google hoje em dia colocou um número, e você consegue medir isso em ferramentas, que eu vou mostrar até o final do curso com vocês.

[03:13] E a última que eu quero trazer, é o cumulative layout shift, que ele se resume bastante ao seu site não ter aquele comportamento que eu chamo de “pipocar”, que é você abrir um site, e às vezes ele tem tanta propaganda, que geralmente é o que impacta isso, que ele vai descendo o conteúdo, e a pessoa acha que ela vai clicar em um botão de like, e de repente aparece uma propaganda e ela acaba clicando nela.

[03:34] Então isso impacta bastante. E eu trouxe isso, porque são números, são metrificáveis e eu vou mostrar para vocês uma ferramenta para conseguir, tanto monitorar, quanto conseguir fazer o acompanhamento dessa parte.

[03:46] Mas eu quero pautar de verdade o que eu vou estar falando, muito nesse artigo no Guillermo Rauch, que é o criador do Next, como eu havia dito. Esse artigo tem 7 anos e ele continua atual. Porque os problemas que ele traz, os pontos que ele cita, que são 7, ele fala que páginas pré-renderizadas não são opcionais, agir imediatamente no input do usuário e várias outras coisas.

[04:13] E você repara, nem vamos ler o texto agora, vou deixar mais para frente, mas esse “Agir imediatamente no input do usuário” bate diretamente com essa questão do first input delay. Então se o usuário clicar, ele tem que conseguir ter esse feedback claro. Essa parte do pre-rendered pages are not optional, bate bastante com o lagest contentful paint, que é essa questão do carregamento, a página estar pronta quando o usuário baixa.

[04:38] Eu sei que agora, se você não mexe muito com essa parte de performance, está um pouco abstrato para você, eu estou passando um conteúdo muito mais teórico, mas eu quero deixar para vocês agora de indicação, tanto esse artigo para você ler, vale colocar no Google Tradutor, se você não tiver o conhecimento de inglês, dando uma aprofundada, porque muitos pontos que tem nesse artigo, o próprio Guillermo Rauch trouxe vários exemplos que ele vai explicando como as coisas carregam nos sites.

[05:05] O curso da Alura de performance do Sérgio Lopes, tem várias dicas, eu até disse isso em outro curso da Alura falando de Next.js, mas nesse vamos falar de muito mais features, vamos nos aprofundar em várias features e ver com problemas do mundo real, pegando casos de e-commerces grandes como a Amazon, sites que têm uma concorrência de acesso muito grande, como por exemplo o site da Mega Sena, como você faz para aguentar essa quantidade de grande requests, alternativas que temos para isso.

[05:31] Então ele vai explicando cada um dos pontos, eu recomendo a leitura. E caso você curta também, tem a versão da palestra que o Guillermo Rauch deu na BrazilJS, esse post veio da palestra que ele deu, então ele deu a palestra em 2014 e fez esse artigo. E esse é um material que eu queria passar para pautar.

[05:55] Então vamos falar bastante sobre performance e vamos passar por cada um desses pontos, tentando entender como o Next ajuda a prever o comportamento do usuário, conseguir fazer updates de código quando sem o usuário perceber tanto que teve alguma mudança, enfim. Não vou me aprofundar tanto, senão vou dar spoiler, mas fica ligado, que na próxima aula, já vamos começar com código, vamos fazer uma tour geral para clarear as coisas do Next.js, e depois vamos pontuando cada cenário passo a passo, a partir da segunda aula.

[06:27] Então fica no próximo vídeo e na segunda aula vamos ter vários casos de uso. Vejo você lá.

### Estrutura de projeto I

1. Iniciando um projeto NEXT.JS:

    npm init -y

2. Instalando as dependências:

    npm install next react react-dom

3. Na pasta ROOT do projeto

    npx gitignore node

4. Rodar o projeto

    npm run dev

---

[00:00] Chegou a hora de começarmos a colocar a mão na massa e darmos uma recapitulada para você que já conhece um pouco do Next e para você que não conhece, e ver um pouco dos recursos principais dessa ferramenta, para termos a base para construir um site. E em cima dessa base, vamos adicionar os novos recursos que essa ferramenta tem, que são muito ligados a parte de build, e que vão impactar vários daqueles pontos do artigo dos 7 princípios que o Guillermo Rauch fez.

[00:26] Então, eu tenho aberto o site do Next.js, cliquei em um link aleatório. Mas basicamente, ele se posiciona hoje em dia como o SDK da Web, ou seja, é o kit de desenvolvimento de software da Web. O que eles querem dizer com isso? Basicamente, eles querem ter uma experiência supernatural e direto ao ponto, para que você consiga criar os seus projetos.

[00:46] Então eu cliquei nessa parte do “Docs”, eu quero mostrar, primeiro esse get started deles, que tem toda uma parte de setup, explicando como você cria o projeto, tem setup para você criar com TypeScript também, mas é super fácil de converter, eu vou mostrar para você ainda nesse curso como faz para lidar com essa parte, um projeto já pronto, como você converte, então fica tranquilo.

[01:07] Outra coisa que vamos fazer também é essa parte desse manual setup, porque eu quero que você, que está fazendo esse curso, você tenha controle do que está acontecendo no seu projeto, que você consiga ir se acostumando com o que está rolando e tudo mais.

[01:21] Por onde começamos? Está vendo que eu tenho esse a1.3? Esse a1.3 é relativo a aula que eu estou agora, então no repositório final, você vai ter várias dicas que eu vou colocar, junto com a pasta de cada uma das aulas. Para cada aula, ponto específico do curso, você vai ter o exato código que eu estou fazendo, para você poder consultar, praticar e tentar criar sua versão enquanto você está acompanhando.

[01:49] Então vamos começar a criar essa estrutura de projeto. Eu vou usar o NPM para fazermos essa estrutura. Então eu vou acessar essa parte “a1.3”, então cd aulas01/a1.3, que é a primeira parte que estamos tendo código neste curso, é o terceiro vídeo dessa aula 1.

[02:11] Então vou rodar npm init -y, para darmos um “sim” para tudo, para ele criar essa base do projeto, e eu vou rodar o comando que eu copiei do site, para instalarmos essas 3 coisas.

[02:26] Logo na sequência ele pede para colocarmos esse monte de scripts dentro do nosso “package.json”, então se o Next está pedindo a documentação, vamos fazer. Então eu vou em “package.json” e vou apagar essa parte de scripts e vou colar tudo que o Next deu e colocar uma vírgula, para ele parar de reclamar.

[02:58] Outra coisa que eu vou fazer agora, é na raiz, eu vou voltar duas pastas, estou na pasta base do projeto e vou rodar o comando npx gitignore node, só para ele gerar um arquivo gitignore, para eu poder dar um git init nessa pasta, e vocês irem vendo quais são os arquivos que eu estou mexendo sem versionar a pasta “node.modules”. Isso é bem importante.

[03:21] E vamos tentar rodar esse ”next dev”, vamos ver o que acontece, para começarmos a desenvolver. Então cd aula01/a1.3. Vamos para a pasta “a1.3”, e dentro eu vou rodar npm run dev, vou rodar esse comando.

[03:40] Ele dá um erro e ele fala que não achou um diretório “pages”. Eu queria até seguir os passos da documentação, e você pode seguir, tem um curso mais básico, que explicamos, mas eu vou basicamente só copiar esse componente de bem-vindo que ele sugere para colocarmos na pasta ./pages/index.js, e te mostrar que todo o setup do Next e feito para melhorar sua experiência.

[04:01] Então ele vai facilitar, vai ter tudo documentado, fácil de você passar para alguém novo que chegar no seu time, isso ajuda a diminuir o tempo de onboarding das pessoas, porque a estrutura base do seu projeto está documentada, você passa pela documentação, está lá, funciona, prático e ela usa em cima.

[04:17] Então eu vou criar a pasta “pages” desse nosso projeto, e vou criar o arquivo “index.js”. E vou colar esse homepage.

[04:28] Só por questão de indentação, eu vou criar um outro arquivo chamado de “editorconfig”, vou criá-lo. Eu tenho uma extensão que gera, por isso eu consegui gerar clicando com o botão direito do mouse, mas você pode procurar por “editorconfig”, instalar no seu editor de código, e ele vai trazer para você.

[04:48] Isso é só para ele padronizar para mim, que eu quero sempre usar o espaçamento de 2 e que ele sempre coloque uma linha a mais no final do arquivo, que é mais um padrão para o GitHub ficar sincronizado, meio que padrão. Mas já vai estar pronto para vocês, você pode só copiar esse arquivo que vamos passar para você também.

[05:06] Então fizemos o nosso “editorconfig”, agora, eu vou formatar esse documento, e vou tentar de novo rodar no terminal npm run dev. Eu vou no navegador, e vou colocar “localhost:3000”.

[05:38] Abri, ele já nos trouxe “Bem-vindo ao Next.js!”. Nesse curso eu não vou criar nenhum app com vocês, eu só quero mostrar coisas comuns que temos app. Então, por exemplo, todo projeto é muito comum você ter mais de uma página. Então para criar home, criamos o index. Se eu quiser criar mais uma página, eu crio um novo arquivo, por exemplo, a página “sobre.js”, o nome é sempre o nome que queremos acessar na URL, então vai ser o /sobre que vamos criar agora. E tudo que precisamos fazer é ter essa mesma estrutura.

[06:14] Então a function SobrePage() {, ficou uma mistura de “portuinglês” muito boa, e embaixo eu faço export default SobrePage;. E fazer embaixo da function return {, e embaixo uma div de Você está na página Sobre.

[06:35] Perfeito, está bonito, está tranquilo. Então se eu der um “F5”, estou na página /sobre. Então temos a sobre e o “Bem-vindo a Next.js”. É nesse nível de padronização que o Next vai trazer as coisas para você.

[06:59] Outra coisa que eu queria mostrar para vocês e mostrar, é que se você quiser ter uma página 404, é muito comum os sites terem essa página tendo algum joguinho, alguma coisa assim, ou só para contabilizar a quantidade de pessoas que estão caindo na página 404 no seu site.

[07:13] Então para cair na página 404, você precisa digitar qualquer coisa na URL, então você digita qualquer coisa e cai.

[07:19] O Next, por padrão tem uma dele, que ele carrega para você, mas você pode, tranquilamente, criar um arquivo “404.js”, dentro dessa pasta “pages”, vou copiar essa estrutura que ele sugere para customizar.

[07:41] De novo, é só um componente com export default, se eu salvar esse arquivo e voltarmos para o projeto, ele carregou o que colocarmos, o nosso arquivo, “404 – Nosso arquivo do curso”.

[08:01] Então nessa brincadeira, já estamos vendo bastante coisa, já vimos criar páginas, como customizar a página 404, e dá para colocarmos muito mais coisas, porque já vimos a parte do setup, essa parte da página 404, e podemos customizar até algumas coisas mais gerais da aplicação, como por exemplo.

[08:24] Eu abri esse link da documentação, esse “custom App”, que se você procura sozinho, você não entende para que você vai usar isso. Vou dar um problema para você: Temos a home, a página sobre a nossa página 404. Repara que a fonte está feia em cada uma dela, poderíamos tentar padronizar, colocar uma fonte sem serifa, sem ter essa base em todas as nossas páginas. Para fazer isso, precisamos ter um componente que abrace todas as páginas que temos. É aí que entra o tal do App.

[09:02] Para usá-lo, tudo que precisamos fazer é: Dentro de “Pages”, criar um arquivo “app.js”. Então vou fechar tudo que eu tenho aberto, vou criar o arquivo “app.js”. Dentro eu vou copiar essa estrutura que o Next me sugere.

[09:29] E somos livres para colocar qualquer estrutura que quisermos. Eu vou colocar um fragmento, que é basicamente abrirmos e fecharmos a tag, sem colocar nada, para poder colocar Texto em todas as páginas. Colocando isso, depois colocamos embaixo export default MyApp.

[10:03] Então só fazendo esse export default, já conseguimos ter o nosso Sobre com o texto em todas as páginas, esse texto que eu coloquei, conseguimos ter a nossa home com esse texto e até a nossa página 404.

[10:27] Então ficou bem genérico. Para aplicar um estilo, basta escrevermos uma tag style dentro. Então eu posso colocar </style>, e podemos colocar, por exemplo, que todo mundo vai ter o font-family: sans-serif.

[10:52] Vou salvar, e repara que ele quebrou. O que fazemos agora? Isso acontece, porque dentro de um arquivo React, usar essas chaves representa que você quer trabalhar com alguma coisa que é dinâmica, então ele espera que isso fosse como se fosse um espaço para colocar uma variável. Para colocar uma tag style no meio do Next, você tem que recortar esse código, a tag vai ter que ter duas coisas, ela vai ter que ter uma chaves e uma template string.

[11:29] A partir desse momento, qualquer coisa que eu escrever dentro, vira um estilo válido, ele parou de reclamar no terminal, sempre importante olhar no terminal para ver o que está acontecendo. E agora, ele aplicou o CSS que criamos. Se eu inspecionar, repara que ele colocou esse estilo acima da nossa div da home.

[11:54] Se eu for na nossa página sobre, ele colocou acima da página sobre. Então ele está mantendo esse padrão para conseguirmos aplicar os estilos e trabalhar em cima dessa estrutura base que temos na página.

[12:10] Agora, a minha ideia é mostrar para você, não só essa parte do Custom App, mas mostrar também que podemos customizar até a tag document, até essa parte mais externa, como vai renderizar a tag body e tudo mais.

[12:22] Tudo isso já tem na documentação também. Então, para terminarmos essa aula, eu vou mostrar essa parte do documento, e vou deixar um gostinho para você ver o que vamos quebrar na próxima.

[12:35] Então eu vou copiar essa parte desse document que temos, você deve achar estranho que estamos copiando um código, mas isso é um código do framework, não tem muito o que fazer. Você vai copiar essa estrutura, respeitá-la e customizar conforme você precisa. Por exemplo, é muito comum em um site, na tag do HTML você dizer qual é o lang do site, você dizer que o site é em português, o site é inglês. Então esse tipo de coisa vamos passar nesse arquivo “_ documento.js”.

[13:04] Então vou criar esse arquivo, vou colar essa estrutura. Se formos olhar no projeto, não mudou nada. Mas agora, conseguimos colocar o lang nessa tag no meio do HTML, consigo colocar lang=”pt-BR”, por exemplo. Salvando isso, aplicamos o lang.

[13:30] Então você vê que nesse vídeo conseguimos aprender a criar uma página, basta colocar dentro da pasta “pages” um arquivo e o nome dele vai servir como índice, o index é a home, todos os outros, como home, contato, vai ser só colocar o nome .js, vimos como criar a página 404, também vimos como colocar algo que fique em volta de todas as páginas. No React e muito comum ter providers, tema, outras configurações que ficam mais externos nessa parte do app, inclusive nesse curso você ainda vai ver um outro caso usando uma lib, mais próximo do dia a dia.

[14:06] E para poder mexer na estrutura inteira do HTML do Next com o React, usamos esse arquivo “_document”, onde você importa vários componentes do Next que estão prontos para se integrar no meio do processo de rodar as coisas dele, mas que permitem que modifiquemos as coisas, estendermos e fazermos o projeto ter a nossa cara, ter a nossa identidade.

[14:33] Então, esse vídeo vai ser quebrado em duas partes, eu vejo você no próximo, que é para mostrar para vocês como podemos fazer um pouco do roteamento nessa parte mais dinâmica, como podemos fazer para conseguir ter uma página que tem um ID específico ou fazer link entre páginas. Vamos fechar essa primeira aula vendo esse conteúdo que é super importante e todo mundo precisa. Até daqui a pouco.

### Exercício: App personalizado

Sobre o arquivo _app.js, selecione as alternativas corretas:

a) **Alternativa correta:** Com ele, é possível compartilhar recursos entre páginas.
- _Alternativa correta! Os layouts e estados criados dentro deste componente estarão presentes em todas as páginas da aplicação._

b) **Alternativa correta:** Deve obrigatoriamente ser criado dentro de /pages.
- _Alternativa correta! O _app é específico do Next.js, então precisamos seguir as regras do framework para que ele funcione corretamente._

c) **Alternativa correta:** Deve obrigatoriamente conter um componente React como default export.
- _Alternativa correta! O _app é específico do Next.js, então precisamos seguir as regras do framework para que ele funcione corretamente._

d) Sem ele, a aplicação não inicializa.

e) Deve ser criado na raiz do projeto.

### Estrutura de projeto II



### Rotas dinâmicas com Next.js

Na página devemos:

  import { userRouter } from 'next/router';

  export default function Post() {
    const router = useRouter();

    console.log(router);
  }

---

[00:00] Eu prometi que no próximo vídeo você ia ver como criar rotas dinâmicas, porque até agora só criamos página estática. Então criamos a página sobre, criamos a nossa home, criamos a 404, que é qualquer coisa que digitarmos errado, então isso está pronto.

[00:18] Vamos agora ver onde encaixa, para fazermos essas páginas dinâmicas. Como por exemplo, eu até gosto do exemplo do Next, essa parte de lidar com posts. Então vamos ver como fazemos na prática.

[00:31] Ponto importante: Todos os links que eu estou te mostrando, são links da documentação, porque eu quero que você tenha autonomia de conseguir sair desse curso e procurar por você mesmo, indicar para pessoas que você conhece em ter esse material. Você tem que conseguir ter autonomia, estou aqui para te dar as ferramentas para você conseguir fazer.

[00:50] Então, seguindo essa linha, uma das ferramentas é a explicação, então vamos puxar agora. Então eu tenho a nossa pasta “Pages”, e se formos um projeto, podemos ter um blog, vamos ter a pasta “/posts”, então vou colocar “/posts”, e vamos ter dentro, os posts, então por exemplo, eu posso ter o “post.js”. E seria mais ou menos a mesma estrutura, então export default function Post() {, embaixo return {, embaixo <div>, e embaixo Página de post.

[01:30] Só de eu salvar, o Next está esperto, eu posso até parar e subir de novo, mas normalmente eu não preciso, você não precisa. Se eu criar alguma coisa dentro da “pages”, automaticamente o Next vai ler e vai adicioná-la nas rotas do seu projeto. Ela vira mais uma página que é possível acessarmos pela URL do navegador.

[01:50] Então eu vou abrir e vou tentar acessar “posts/post”. Página de post. Só que em um site, vamos ter a URL do post, então “post-sobre-nextjs”, acho que esse é um bom título para colocarmos.

[02:07] Então, se eu acessar esse título, onde deveria cair? Na página de post ou na 404? Caímos na 404. Porque esse valor é estático. Tal como a 404, tal como o index, tal como o sobre, os que tem underline são arquivos de configuração, então podemos ignorar por enquanto. Mas tudo que é fixo, está desse jeito.

[02:33] O que podemos fazer? Para dar essa diferença e conseguirmos pegar esse valor dinamicamente, gerar página e conseguir ter acesso, eu preciso colocar “[]”. Eu chamo de parênteses quadrado, seria o squared brackets, brackets se você for pegar inglês, e vou dizer que para cada post vamos ter a slug desse posto ou o ID desse post. Slug é o nome do posto, o título principal dele, só que resumido, encurtado em uma URL sem acento, sem espaço, tudo mais. Mas vou chamar de ID, só para ficar mais fácil e mais comum.

[03:13] Então mudei, chamei de ID, então “[id].js”. Já rodou de novo a build do projeto. E se eu for carregar essa mesma página de novo, deu 404, vocês viram, carreguei de novo e passa a funcionar.

[03:27] E o mais legal, agora deveríamos poder conseguir acessar esse conteúdo, faz sentido? Deveríamos conseguir poder pegar isso e pedir para um back-end o conteúdo dessa página. E é exatamente o que vamos fazer agora. Não vamos pegar do back-end, mas eu vou te mostrar como você acessa esse dado.

[03:44] Então o Next nos deu a estrutura para criar as páginas. Então criamos essa pasta, tanto que eu até falo que essa pasta “Pages” é do Next, evita colocar qualquer outro arquivo que não seja uma página, senão você pode confundir o Next e dar alguns erros. Então coloca só as coisas da página. Eu vou passar mais para frente, formar de arquitetar, de estrutura, mas é importante você ter em mente agora.

[04:09] Então vamos fazer o import de algo do Next que vai nos ajudar a lidar com essa parte de roteamento, que vai nos ajudar a mudar de página, pegar alguma informação, fazer algo mais específico. Esse recurso vem do “next/router”, então import {useRouter } from ‘next/router’. Isso já está instalado quando fizemos o install do Next. Só de ter o Next como dependência, você já tem esse ‘next/router’. E dentro das chaves eu vou trazer o useRouter, que tal como useState, useEffect, é um Hook do React para trabalharmos com essa parte de roteamento.

[04:48] E junto com isso, eu vou colocar const router = useRouter(). Eu vou até desligar o GitHub Copilot, porque senão ele vai começar quebrar as nossas sugestões, vai ficar meio estranho.

[05:04] E vou dar um console.log nesse Router para vocês verem, então console.log(router);. Vou abrir o navegador, vou voltar no console e vou abrir a página.

[05:15] Repara que ele roda uma vez, que é logo quando a página carrega, e ele traz várias informações, ele traz o path da página que estamos, ele traz se é isFallback, isPreview, tem um monte de coisa, tem o path de novo, enfim, tem muitas coisas. Tem um monte de query, reload, se formos olhar o de baixo, repara que ele tem um query: {id: ‘post-sobre-nextjs’.

[05:41] Exatamente o valor que passamos dentro do parênteses quadrado, ele traz como um prop dentro do .query. Então se eu acessar .query.id, eu posso até pegar o código e colocar no meio, id do post atual.

[06:03] Se eu carregar a página, ele trouxe esse valor. E se eu mudar, colocar “mudei-o-id”, ele muda o ID.

[06:14] E ao longo das próximas aulas, eu vou mostrar para vocês como podemos lidar com isso, como que lidamos se for cair em uma página 404, como lidamos com toda essa parte mais geral. E também essa parte de pegar o conteúdo de uma outra parte, vocês vão ver, tem bastante coisa legal.

[06:33] Então até agora já vimos muita coisa, nessa aula vimos como fazer rota dinâmica, então já é um ponto a mais nessa aula, faltou vermos como navegar entre páginas, porque até agora, criamos as páginas, criamos o sobre, estamos fazendo o nosso blog, mas não fazemos nenhum link. Para fazer link, o Next tem um componente dele, só que o jeito de usar é meio diferente, você vai ver agora.

[06:58] Eu vou copiar esse import do Next link, que é o componente que vamos usar, e vou importá-lo. Só que o Next link não funciona sozinha, você precisa colocar o Next link e precisa colocar uma tag A, então <a>Ir para a home</a>, e você passa o href nesse Next link.

[07:23] Então vou passar Link href=”/”. Vou abrir a página, vou selecionar para mostrar para vocês. Repara que ele printou somente a tag a, mas se não colocarmos a tag a e salvar, ele dá erro, ele fala que multiple children were passed to quando devia ter somente um. Ele dá um erro bem bizarro na hora que eu troquei.

[07:51] Então eu vou voltar, vou descomentar o link do VS Code e vou voltar para o navegador. Agora está certo de novo. Você pode até colocar dentro de uma <ul>, por exemplo, e colocar em uma <li>. Então se eu clicar agora em “Ir para a home”, ele fez a navegação.

[08:20] E um ponto importante, eu mostrei esse componente next/link, mas você não precisa obrigatoriamente usá-lo. Como assim? Eu acabei de mostrar e não preciso usar? Olha só. Eu mostrei algumas coisas que são padrão, então, por exemplo, o app não tem muito o que mexer, é essa estrutura e inserimos coisas a mais para ficar em volta do componente que envolve, que sai de cada uma das páginas.

[08:44] Então esse homepage, quando carrega a aplicação ele vai para o app e passa corretamente. O document, total do Next, só tem os componentes dele, mexe uma coisa ou outra, mas é total do Next as coisas que tem nele.

[08:57] Já esse link, podemos usar a tag link sozinha, eu posso comentar esse link que tem na nossa página na home, então “localhost:3000/posts/posts-sobre-nextjs”, só que eu preciso colocar o <a href=”/”>Ir para a home</a> no código, que é importante, salvei e carreguei.

[09:22] O que muda? Está vendo que ele tem um x no canto superior esquerdo? Sempre que eu clico ele dá um X. Porque ele está baixando todo o conteúdo de novo. Então se eu for olhar na aba “network”, baixamos todos esses arquivos. Eu vou colocar até na home, que eu acho que é mais fácil. Vamos organizar para ficar mais fácil de visualizarmos esse caso. Então vou copiar essa ul e vou colocar dentro da nossa home.

[10:07] Eu vou colocar esses links, e na home eu vou colocar o link do Next.js. E eu vou colocar <a href”/”>Ir para a /sobre< /a>. E dentro da sobre eu vou colocar para voltar para a home.

[10:34] Só que sem o componente link do Next. Então página Sobre sem o componente Link do Next, a home com o link, faltou copiar o import, não esqueçam de importar as coisas que são importante, e desculpe por essa piada horrível.

[10:57] Esse é o nosso link. Então da home vai para o Sobre e do sobre volta para a home. A home usa o link do Next, a Sobre não usa o link do Next.

[11:08] Repara, baixamos todos esses arquivos, clicamos para ir para a Sobre, ele baixou mais 3 arquivos. Se eu vou para a Home, ele baixa tudo de novo. Como assim? Sobre, ele baixa só mais 3. Se eu clicar para ir para a Home, ele faz um refresh de tudo.

[11:35] Quando eu clico para ir para a sobre, ele baixa mais 3 arquivos, se eu clicar para voltar, ele faz o carregamento e manda tudo de novo. Se abrirmos a aba “Elements”, fica até mais claro.

[11:45] Estou na sobre, eu vou para a home. Ele pisca. E quando eu venho da home para a sobre, ele só muda esse pedaço e mantém até a tag style. Isso é o comportamento de SPA, single page application. Que é o que o Gmail é, muitas outras aplicações são, onde ele só muda exatamente o que ele precisa mudar na nossa aplicação.

[12:11] Então isso é um comportamento super importante, eu precisava que vocês vissem isso na prática, e nas próximas aulas vocês vão ver como podemos organizar mais isso. Mas eu queria que vocês tivessem essa noção de, por exemplo, você quer criar um projeto com Next, como você organiza as pastas, como você organiza as coisas?

[12:28] E tem até um detalhe mais importante que eu esqueci de colocar, eu já ia esquecer. Tem uma coisa super importante, que é você conseguir colocar arquivos estativos no Next. Então por exemplo, eu vou no navegador e vou colocar no GitHub, vou te passar um segredo, se eu colocar “github.com/omariosouto.png”, no seu perfil do GitHub, você consegue pegar a sua foto de perfil.

[12:48] Eu vou salvar essa foto no path “dev > alura > cursos > curso 2 > aula 1 > aula 3 > pages”, dentro disso eu vou criar uma nova pasta chamada de “public”. E dentro dela eu vou colocar o meu avatar, minha foto.

[13:14] Na verdade, o “public” fica dentro da raiz, ele não fica dentro de “pages”, então fica “pages > public”. Por que eu estou mostrando isso? Porque é uma dúvida que todo mundo tem, que é a seguinte, tem a home do meu site, eu quero carregar uma imagem, se ela for de uma URL externa, é fácil de colocar “https://github.com/peas.png”, peas é o nome do Paulo Silveira, o dono da Alura.

[13:44] Então se eu salvar, e abrir no meu projeto, voltando para a home, ele carregou o Paulo com a touca de unicórnio dele.

[13:55] Agora, e se eu quiser carregar a nossa foto, que eu acabei de colocar nessa pasta “public”? Para acessá-la, basta você olhar qual é o nome do arquivo que você quer acessar, então no meu caso é o “avatar.png”.

[14:12] Tudo que está na pasta “public”, automaticamente você consegue acessar só colocando uma barra. Então se eu quiser organizar um pouco mais essa pasta, podemos colocar “images”, e o avatar vai dentro dela.

[14:28] Se eu abrir de novo, quebrou, 404. Se eu usar “localhost:300/image/avatar.png”, ele traz corretamente. E podemos pegar “/images/avatar” abrir a nossa home. E para fechar com chave de ouro esse vídeo dessa aula 1, eu posso trocar, carregar o source de /images/avatar.png.

[14:52] E ele traz a nossa foto corretamente, pronta para usar. Se eu tentar jogar na URL, ele abre nossa pasta interna. E isso é a base de Next.js que você precisa para poder acompanhar as nossas próximas aulas e ver os diferentes cenários de como usar o Next.js para um e-commerce, para um blog, para um site superconcorrido como o da Mega Sena, e vários outros que você pode ter na sua cabeça, e pode até trabalhar em um deles, e vamos focar nos conceitos e como aplica-los na prática. Vejo você na aula 2. Tchau.

### Rotas dinâmicas com aninhamento

Você pode aprender mais sobre rotas dinâmicas neste artigo [Navegação com Next.Js utilizando rotas dinâmicas]('https://www.alura.com.br/artigos/navegacao-next-js-utilizando-rotas-dinamicas#:~:text=O%20que%20s%C3%A3o%20rotas%20din%C3%A2micas%20e%20por%20que%20utiliz%C3%A1%2Dlas,para%20cair%20na%20p%C3%A1gina%20desejada.').

### O que aprendemos?

No vídeo anterior, aprendemos que a presença de [] em volta do nome da rota significa que ela é uma rota dinâmica. Também foi mostrado que é possível aninhar rotas através da estrutura de pastas. Ou seja, a seguinte estrutura de pastas torna a rota http://localhost:3000/posts/curso-next/ possível:

<img src='https://caelum-online-public.s3.amazonaws.com/2431-tour-next-js/01/aula1-img1.png'>
Estrutura Pages/Posts/JS[id].js

Neste exercício, será implementado o código necessário para tornar a rota http://localhost:3000/posts/curso-next/comentarios disponível.

VER OPINIÃO DO INSTRUTOR
Opinião do instrutor

Para atingir nosso objetivo, devemos aninhar a rota /comentarios à rota /posts/id já existente. Como o [id].js é um arquivo, o primeiro passo é transformá-lo em uma pasta e mover o código dentro dele para /posts/[id]/index.js.

Estrutura Pages/Posts/[id]/JS index.js

Após essa mudança, o comportamento da rota /posts/id continua exatamente igual, pois [id].js e [id]/index.js são equivalentes (detalhes na documentação [index routes]('https://nextjs.org/docs/routing/introduction#index-routes').

A partir de agora, qualquer arquivo .js criado dentro de /posts/[id] será uma rota aninhada. Sendo assim, ao criar o arquivo /posts/[id]/comentarios.js a rota /posts/id/comentarios estará disponível!

Código do arquivo /posts/[id]/comentarios.js:

  /* 
    /posts/[id]/comentarios.js
    Código praticamente igual ao [id]/index.js
    - o texto foi modificado para mostrar que é a página de comentarios
    - uma li com um Link foi adicionada para voltar para a página do post
  */

  import Link from "next/link";
  import { useRouter } from "next/router";

  export default function Comentarios() {
    const router = useRouter();

    return (
      <div>
        comentários do post com id: {router.query.id}
        <br />
        <ul>
          <li>
            <Link href="/">
              <a>Ir para a home</a>
            </Link>
          </li>
          <li>
            <Link href={`/posts/${router.query.id}`}>
              <a>Ir para o post</a>
            </Link>
          </li>
        </ul>
      </div>
    );
  }


Em [id]/index.js vamos adicionar um Link para a página de comentários. O código final deve ficar assim:


  /* 
    /posts/[id]/index.js
  */

  import Link from "next/link";
  import { useRouter } from "next/router";

  export default function Post() {
    const router = useRouter();

    return (
      <div>
        Id do post atual: {router.query.id}
        <ul>
          <li>
            <Link href="/">
              <a>Ir para a home</a>
            </Link>
          </li>
          <li>
            <Link href={`${router.query.id}/comentarios`}>
              <a>Ir para comentarios</a>
            </Link>
          </li>
        </ul>
      </div>
    );
  }

Para ver o resultado acesse o post com id “curso-next” pela URL http://localhost:3000/posts/curso-next e interaja com os links da página!

Clique no link “ir para comentarios” e veja que a URL muda para http://localhost:3000/posts/curso-next/comentarios.

Por enquanto, a página de comentários é igual para todos os posts. Nas próximas aulas, você aprenderá como personalizar os dados das páginas dinâmicas!

- Como o Next.js melhora suas métricas da web;
- Sobre arquivos específicos do Next.js como o _app.js, _document.js e 404.js e suas funcionalidades;
- Como criar e utilizar rotas dinâmicas.

## 2. Páginas com Next.js
### Projeto desta aula
### Static Site Generation I
### Static Site Generation II
### getStaticPaths
### SSR: Server Side Render
### Incremental Static Generation
### Revalidate do Next.js
### Search Params
### O que aprendemos?
## 3. Recursos adicionais do Next.js
### Projeto desta aula
### Link Prefetch
### Prefetch
### Dynamic Imports
### Next.js com TypeScript
### JavaScript com tipos?
### Tipagens do Next.js
### O que aprendemos?
## 4. Next.js é framework FullStack?
### Projeto desta aula
### API Routes
### API Routes com typescript
### Tipos de build da ferramenta
### Benefícios do ISR
### O que aprendemos?
## 5. Dicas finais e deploy
### Fazer o deploy do projeto
### Componentes e features novas
### Desafio: de onde vem as props da página?
### Desafio: ordem de execução
