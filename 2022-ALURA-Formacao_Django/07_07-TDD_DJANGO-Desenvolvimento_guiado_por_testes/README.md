# TDD no Django 3: Desenvolvimento guiado por testes - 8h
**Instrutor:** Guilherme Lima \
**Disponível em:** [ALURA]('https://cursos.alura.com.br/course/tdd-django-3-testes') \
**Conteúdo:**
 - Aprenda na prática o que é TDD
- Saiba como escrever diferentes tipos de testes
- Aprenda a testar suas rotas, modelos e views
- Crie diferentes cenários e instâncias para seus testes
- Desenvolva uma aplicação do início ao fim sendo guiado pelos testes

## 01. Fundamentos do TDD Ver primeiro vídeo
### Apresentação

[00:00] Olá, meu nome é Guilherme Lima e eu serei o seu instrutor no curso TDD no Django 3: Desenvolvimento guiado por testes. Nesse treinamento vamos aprender a escrever diferentes tipos de testes, sejam eles testes funcionais ou testes de unidade. E como que podemos desenvolver as nossas URLs, modelos e views com base nos nossos testes, sendo guiados através dos nossos testes.

[00:23] Fazendo esse treinamento - esse curso - vamos desenvolver uma aplicação chamada Busca Animal onde eu digito o nome de um animal, por exemplo, gato, quando eu dou “pesquisar” ele vai me mostrar o nome do animal que eu pesquisei, se ele é um predador, se ele é venenoso e se ele é doméstico.

[00:39] Essa é a aplicação que vamos desenvolver. Se eu digito, por exemplo, urso, ele vai me mostrar: o urso é um predador, ele não é venenoso, mas ele também não é doméstico.

[00:48] Então, fazendo esse curso vamos desenvolver essa aplicação. Quais são os pré-requisitos para criar nesse curso e você ter um bom resultado no seu treinamento? É importante que você tenha familiaridade com a linguagem de programação Python, e que você já tenha utilizado o Django.

[01:03] Porém, se você já é um profissional muito experiente, já escreve muitas linhas de código e o teste é algo que já faz parte da sua rotina como desenvolvedor, talvez esse curso não seja recomendado para você, porque vamos consolidar os nossos fundamentos no que é um desenvolvimento guiado pelos testes. Então, sabendo disso, vamos começar?

### Preparando o ambiente

Olá!
É muito bom receber você neste curso de TDD no Django 3: Desenvolvimento guiado por testes.

Espero que seja uma experiência de aprendizado incrível, e que possamos vencer todos os desafios juntos. Neste curso, vamos desenvolver uma aplicação guiada através de testes.

Preparando ambiente
Para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

    Python 3.7.4
    Django 3.1.1

O Django pode ser instalado através do comando:

    pip install Django==3.1.1COPIAR CÓDIGO

Em caso de dúvida na instalação ou durante o curso, conte sempre com o fórum da Alura!

### TDD na prática

[00:00] Vamos iniciar, então, os nossos estudos em relação ao TDD. A primeira etapa do TDD, antes de escrevermos qualquer linha de código, é encontrar uma forma de testar o aplicativo, alguma funcionalidade que queremos criar. Para exemplificar isso, vamos criar o seguinte programa.

[00:17] Eu quero criar uma função que descobre a idade de uma pessoa em um determinado ano. Então, nós vamos precisar de algumas informações, duas informações para ser preciso. Primeiro, o ano de nascimento da pessoa, e segundo, qual é o ano que ela quer saber a idade dela. Pode ser o ano atual ou um ano futuro. Com base nessas informações, nós retornamos a idade da pessoa.

[00:38] Vou colocar aqui o meu exemplo. Eu nasci no ano de 1991, e quero saber: em 2050, quantos ano eu terei? Em 2050, eu terei 59 anos. Legal. Para nós humanos, é fácil entender isso, mas como que nós criamos essa função utilizando a metodologia do TDD e garante que esse teste vai passar e nós vamos seguir todos os passos do TDD e vamos ter essa afirmação verdadeira que se eu nasci no ano de 91, e coloquei o ano de 2050, o resultado dessa função é 59.

[01:14] Vamos ver isso na prática? Vou criar um novo folder, uma nova pasta que vou chamar de tdd_idade, vou abrir o VS Code, arrastar essa pasta do tdd_idade para dentro, e vou criar um novo arquivo no VS Code, um new file, chamado de idade.py

[01:38] Então, primeira coisa, o que fazemos no TDD? Vamos encontrar uma maneira de testar isso que estamos querendo criar. Então, eu vou afirmar, vou colocar aqui um assert que diz que descobrir_idade com esse cenário de testes: 1991 e 2050, então, 1991,2050) == 59. Salvei, “Command + J”, abriu meu terminal.

[02:17] Vou executar python idade.py. Quando eu executo, nós temos um primeiro erro, um NameError, e ele diz assim: o name descobrir_idade não é definido, e faze sentido, nós não criamos essa função para descobrir idade, então vamos criar essa função chamada descobrir_idade, não vou passar nenhum parâmetro e temos aqui um pass, uma função mais básica do Python.

[02:47] python idade.py, executando mais uma vez no terminal, nós temos um outro erro, um TypeError. Ele fala assim: descobrir_idade, não foi passado nenhum argumento, e dois argumentos são esperados, que é o 1991, que é o ano de nascimento, vou colocar aqui em def descobrir_idade (ano_nascimento, ano) que é o ano que a pessoa quer saber a idade dela.

[03:09] Salvei. No meu terminal, executando mais uma vez, nós temos mais um erro. Ele fala assim: erro de afirmação. Essa afirmação não é verdadeira. Se eu passo descobrir_idade(1991,2050) não é 59 e, de fato, não é mesmo. A nossa função não retorna nada. Então, vou colocar na segunda linha um return onde vamos executar esse cálculo: “ano-ano de nascimento”.

[03:35] Limpando o terminal e executando. Nenhuma mensagem foi exibida, vou executar mais uma vez. Maravilha! Nada foi exibido. O que eu vou fazer: para nós executarmos essa função, vou criar outra coisa, vou criar um print, por exemplo, para mostrar a idade do meu irmão em um determinado ano. Então, print(descobrir_idade) do meu irmão, eu vou colocar, por exemplo, que meu irmão nasceu em 1996 e eu quero saber quantos anos ele vai ter em 2060, por exemplo. Isso vai ser exibido no nosso console.

[04:08] “Command + J”, aqui no nosso terminal, quando eu dou um python idade.py, 64 anos. Vou minimizar um pouco o terminal só para conseguirmos ver. Agora sim, olha só que interessante: nós criamos essa função de descobrir a idade utilizando a metodologia do TDD, nós escrevemos um teste, esse teste falha e nós vamos modificando o nosso código até a medida que esse teste passe.

[04:33] Depois até podemos melhorar o nosso código, mas observe que nós ensinamos o nosso computador a realizar o teste, a verificar se de fato essa função tem o comportamento que nós esperamos desde o início.

[04:48] No próximo vídeo, vamos fazer uma análise dessas etapas que executamos, e encontrar algumas vantagens de desenvolver uma aplicação utilizando a metodologia do TDD.

### O ciclo do TDD

- **Código mais objetivo:** Desenvolver com um objetivo final em mente
- **Menor ocorrência de erros:** O risco de um código apresentar erros diminui
- **Retoração:** Auxilia a refatoração, edição e manutenção do código
- **Tempo:** Apenas o necessário será deesenvolvido
- **Cumpre os requisitos:** Aliança entre histórias do usuário e seu código
- **Melhoria incremental:** Cada teste aprovado será uma pequena vitória

---

[00:00] Criamos uma função seguindo um conjunto de testes para verificar se o comportamento que esperávamos daquela função fosse atendido, e passamos no nosso teste. Por isso, se observarmos, houve um ciclo nas atividades que nós criamos.

[00:16] O primeiro ciclo foi: nós escrevemos um teste que falhou, depois colocou um código, criou um código que fosse aprovado naquele teste, depois podemos refatorar e melhorar o nosso código. Se observarmos esses três ciclos, eles têm nomes definidos: Red, Green e * Refactor*, Vermelho, Verde e Refatorar, no TDD.

[00:42] Lembrando que esse é o menor ciclo do TDD, essas três etapas. Então, essas são as etapas básicas do TDD. Sempre que quisermos criar uma aplicação seguindo essa metodologia, nós vamos ter essas etapas.

[00:56] Mas, qual a vantagem de utilizar a metodologia TDD? Eu vou listar algumas vantagens para vocês. A primeira, o nosso código vai ficar muito mais objetivo, nós vamos desenvolver de fato o nosso código para que ele seja aprovado naquele teste, ou seja, para atender um determinado objetivo final.

[01:15] Depois, menos ocorrência de erros. O risco de apresentar erros na nossa aplicação diminui. Isso não significa que a nossa aplicação não tenha mais erro, não vá conter nunca mais nenhum erro. Não! Isso não existe. Nossa aplicação pode apresentar alguns erros, mas a ocorrência de erros quando desenvolvermos utilizando o TDD diminui.

[01:34] Outra coisa, refatoração, quando precisarmos refatorar, editar ou dar alguma manutenção em um código que foi criado com testes, vai ficar muito mais fácil também, porque, geralmente quando modificamos uma parte do sistema, outras partes do sistema podem ser alteradas também.

[01:54] Se nós criamos uma aplicação, uma funcionalidade, com base no TDD, vamos saber exatamente onde quebrou e como que consertamos, em qual momento está, sem precisar ficar debugando com muitos detalhes.

[02:07] Outra coisa interessante é o tempo. O que acontece? A sensação que temos é que seria muito mais fácil criar essa função de descobrir_idade de uma vez e já colocar os print com algumas idades que queremos descobrir, porém, se observarmos em um escopo maior, em uma aplicação maior, nós podemos ter algumas distrações do tempo.

[02:30] Então, nós começamos desenvolvendo alguma determinada funcionalidade, aí nós achamos outra coisa legal e queremos inserir no código, e acabamos saindo do objetivo principal que queríamos alcançar. Então, o TDD garante que o tempo gasto será em cumprir os objetivos principais daquela aplicação, daquele código. Esse é um ponto importante também.

[02:56] Outra coisa: cumpre os requisitos, ou seja, o usuário, ou a pessoa que precisa daquela aplicação, precisa daquele software, tem algumas requisições, e nós vamos cumprindo essas requisições com base em testes.

[03:14] Mais para frente, nós vamos realizar isso, na prática, mas o que acontece é o seguinte, vamos pegar a história do usuário e ele vai falar: eu preciso de uma função que descubra a idade de uma pessoa, e com base nessa história, nós vamos desenvolvendo o nosso código, então existe uma aliança entre as histórias do usuário e o nosso código também.

[03:35] E para finalizar, uma das mais importantes vantagens de utilizar o método TDD é a melhoria incremental. Cada teste que for aprovado, significa que uma parte daquele projeto muito grande que temos foi finalizada, então já podemos passar para outra parte, para outro objetivo. Então, nesse texto ele até diz, cada teste aprovado será uma pequena vitória na nossa aplicação. Isso é bem legal.

### Para saber mais: Resumo do TDD

TDD(Test Driven Development ou em português Desenvolvimento guiado por testes) é uma das práticas de desenvolvimento de software sugeridas por diversas metodologias ágeis, como [XP]('https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_extrema').

A ideia é fazer com que o desenvolvedor escreva testes automatizados de maneira constante ao longo do desenvolvimento. Mas, diferentemente do que estamos acostumados, TDD sugere que o desenvolvedor escreva o teste antes mesmo da implementação.

Essa simples inversão no ciclo traz diversos benefícios para o projeto. Baterias de testes tendem a ser maiores, cobrindo mais casos, e garantindo uma maior qualidade externa. A prática nos ajuda a escrever um software melhor, com mais qualidade, e um código melhor, mais fácil de ser mantido e evoluído.

Esses dois pontos são importantíssimos em qualquer software, e TDD nos ajuda a alcançá-los. Toda prática que ajuda a aumentar a qualidade do software produzido deve ser estudada.

Um ponto que é sempre levantado em qualquer discussão sobre testes manuais versus testes automatizados é produtividade.

O argumento mais comum é o de que agora a equipe de desenvolvimento gastará tempo escrevendo código de teste; antes ela só gastava tempo escrevendo código de produção. Portanto, essa equipe será menos produtiva.

A resposta para essa pergunta é: o que é produtividade? Se produtividade for medida através do número de linhas de código de produção escritos por dia, talvez o desenvolvedor seja sim menos produtivo.

Agora, se produtividade for a quantidade de linhas de código de produção sem defeitos escritos por dia, provavelmente o desenvolvedor será mais produtivo ao usar testes automatizados.

[..] Aniche, Maurício. Test Driven Development: Teste e Design no Mundo Real. [Casa do código]('https://www.casadocodigo.com.br/products/livro-tdd')

### Para saber mais: Teste Funcional e de unidade

Existem muitas maneiras de descrever tipos de testes. Para nossos propósitos, vamos diferenciar entre testes de unidade e testes funcionais. A distinção é semântica, mas informará nossa estratégia de teste.

- **Teste de Unidade**
O teste de unidade se concentram nas _preocupações do desenvolvedor_ e geralmente são pequenos. São executados em microsegundos e _testa uma única parte do projeto_.

- **Teste Funcional**
O teste funcional é focado na _experiência do usuário_ e podem ser grandes e levar mais tempo quando comparado aos testes de unidade. Geralmente, _simulam aquilo que um usuário faria_.

Para maiores informações, clique [neste link]('https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing') e descubra outros tipos de testes(texto em inglês).

### Definindo o TDD

Nesta aula, criamos uma função utilizando o TDD de forma prática e entendemos as vantagens de utilizar essa metodologia para desenvolver um software.

Sabendo disso, podemos afirmar que:

a) No TDD, a primeira etapa sempre é escrever o código de produção e em seguida, escrever o teste para garantir o resultado ou comportamento esperado.

b) **Alternativa correta:** O menor ciclo do TDD envolve 3 etapas (escrever o teste, escrever o código para ser aprovado e refatorar).
- _Alternativa correta! Certo! Essas etapas são: escrever o teste que vai falhar(red), escrever o código para ser aprovado(green) e refatorar o código aprovado(refactor)._

c) Um software criado com TDD, jamais apresentará algum tipo de erro, bug ou comportamento estranho.

### O que aprendemos?

**Nesta aula:**
- Aplicamos a metodologia do TDD para desenvolver uma função que descobre a idade;
- Entendemos que o menor ciclo do TDD possui 3 etapas: escrever o teste que falha, escrever o código necessário para ser aprovado e refatorar o código.

**Na próxima aula:**
Vamos aplicar essa técnica num projeto Django e descobrir como podemos desenvolver uma aplicação sendo guiado por testes!

## 02. Requisitos, testes funcionais e unitários
### LiveServerTest e Selenium

[Test tools]('https://docs.djangoproject.com/en/4.1/topics/testing/tools/')

1. Existe um comando em DJANGO para testar nossa aplicação, no terminal:

        python manage.py test

1. Podemos utilizar o selenium para realizar nossos testes:

        pip install selenium

2. Podemos fazer testes com LiveServerTestCase, crie um arquivo em setup tests.py:

        from django.test impor LiveServerTestCase
        from selenium impor webdriver

        class AnimaisTestCase(LiveServerTestCase):
            def setUp(self):

---

[00:00] Vamos iniciar, então, o nosso desenvolvimento com base no TDD dessa nossa aplicação. Bom, para começar, vamos criar um ambiente virtual, instalar o Django, assim como estamos acostumados e já vimos esse contexto nos cursos anteriores.

[00:14] Então, eu vou criar uma pasta que eu vou chamar de “tdd_busca_animal”. Vou arrastar essa pasta para o VS Code. Aqui dentro vou criar, “Command + J” para abrir o nosso terminal, vou criar um novo ambiente virtual para esse projeto, então python -m venv ./venv dou “Enter”, ele vai já vai criar a venv para nós , vou ativar a minha venv, source venv/bin/activate.

[00:54] O que eu vou fazer agora vai ser instalar o Django. Então, pip install django. Maravilha, vou fazer aqui o upgrade do pip. O que vamos fazer agora? Vamos iniciar um projeto Django, então vou utilizar o comando Django-admin startproject, vou chamar esse projeto de setup ., onde vamos manter toda a configuração da nossa aplicação e deixar o ponto para não ficar reduntante.

[01:35] Vou fechar o meu terminal, “Command + J” e abrindo aqui, se eu seleciono o arquivo manage.py, até faço questão que você faça esse passo também, observe que ele vai pegar aqui uma versão do python. Se ele não pegar o python da sua venv, é só clicar nele, e se scrollar até você selecionar o python da venv. Daí vem aqui em “setup > settings.py”, parece que está tudo certo.

[01:55] O que nós já podemos fazer? Bom, quando nós iniciamos um projeto utilizando o Django, existe um comando do Django para executar os testes da nossa aplicação, então, mesmo sem escrevermos nenhum teste, é possível já executarmos para ver se tivemos algum problema no ambiente de desenvolvimento nosso, e o comando é esse: python manage.py test, quando eu dou um “Enter” observe o que vai acontecer.

[02:26] Houve uma verificação de erros e nenhum erro foi encontrado, está tudo OK. Ele dá o tempo também que os testes foram executados. Se nós tivéssemos algum problema do nosso ambiente, nós já veríamos nesse teste também

[02:42] Nós queremos desenvolver uma aplicação web. Para nós conseguirmos testar uma aplicação web é necessário subir o nosso servidor. Então, como que vamos fazer isso? Muito semelhante ao que fazemos com python manage.py runserver e sobe o servidor. Nós queremos também esse cenário só que para o teste, e existe uma subclasse chamada LiveServerTestCase, e é a que vamos utilizar para subir o nosso servidor de teste.

[03:09] Mas, onde que eu escrevo essa classe? Bom, para começar, o que podemos fazer? Observe que não criamos nenhum app ainda. Então, eu vou criar em setup um novo arquivo, um new file que eu vou chamar de “tests.py”, vou dar “Enter” aqui nesse meu arquivo, e nesse arquivo nós vamos importar lá do django.test essa subclasse para subir o nosso servidor.

[03:34] Vou colocar aqui from django.test import LiveServerTestCase. Importei. Nós vamos precisar dele para subir o nosso servidor, porém, para que consigamos simular a funcionalidade, testar a funcionalidade da nossa aplicação, por exemplo, abrir uma página de um navegador, clicar em um determinado ícone da tela, realizar essas ações, para isso nós vamos utilizar o Selenium.

[04:09] Então, essas funções, como clicar na tela, realizar, simular uma pessoa, serão responsabilidades do Selenium.

[04:17] Então, o que vamos fazer: lá no meu terminal, eu vou dar um pip install Selenium, vou dar um “Enter”, ele vai instalar o Selenium para nós e nós vamos importar o Selenium para essa nossa classe também. Instalamos o Selenium. O que eu vou fazer agora vai ser importar o Selenium para esse nosso arquivo de teste. Então, from selenium import webdriver, ele vai ser responsável por realizar as manutenções, realizar as ações na nossa classe.

[04:56] Vou criar uma classe agora que vai ser responsável por um teste de um dos nossos aplicativos, que vai ser o nosso aplicativo de animais. Nossa aplicação se resume, mais ou menos, em buscar determinados animais e trazer algumas informações sobre esses animais. Só que como que eu vou fazer isso? Eu vou criar uma classe chamada AnimaisTestCase, e dentro dessa AnimaisTestCase eu vou passar como argumento aquele LiveServerTestCase que trouxemos.

[05:30] A primeira coisa que nós vamos fazer é: sempre que nós iniciamos uma classe, quando criamos uma classe de teste, é importante que seja falado assim: antes de executar os testes, faz algumas ações, como, por exemplo, subir um servidor, e realizar alguns passos iniciais que nós podemos criar, como criar instâncias, vamos ver isso mais para a frente.

[05:53] Então, eu vou criar uma função que vai ser responsável por iniciar o nosso teste. O que vai acontecer? Antes de rodar os testes, eu tenho algumas etapas que eu quero cumprir, e essas etapas nós fazemos uma função chamada setUp. Aqui, um ponto muito importante: esse nome setUp precisa ser S minúsculo, tudo minúsculo, e só apenas o U maiúsculo. Se você escrever setUp com S maiúsculo ou com U minúsculo, nós vamos ter um erro.

[06:22] Vou deixar aqui com o pass, dessa forma. O que vou fazer? Minimizar a parte do lado, abrir o meu terminal de novo, deixa eu só baixar um pouco o terminal para conseguirmos ver, eu vou rodar o teste de novo. python manage.py test. Observe o que vai acontecer. Dei um “Enter” e nenhum erro foi encontrado. Isso significa que ele também executou essa nossa classe de teste.

[06:44] O que vamos fazer na sequência? O Selenium utiliza como navegador principal o Safari, e nós não vamos utilizar o Safari, nós vamos utilizar o Google Chrome para realizar os nossos testes. Na aula seguinte nós vamos fazer essa configuração.

### Configurando o navegador

Configurando o Selenium para utilizar o Google Chrome como navegador de teste.

[Selenium Python]('https://selenium-python.readthedocs.io/')

2. Em tests.py:

        from django.test impor LiveServerTestCase
        from selenium impor webdriver

        class AnimaisTestCase(LiveServerTestCase):
            def setUp(self):
                self.browser = webdriver.Chrome('caminho do chromedriver')

            def tearDown(self):
                self.browser.quit()

---

[00:00] O que nós vamos fazer agora é configurar o Selenium para utilizar o Google Chrome como navegador de teste. Para fazer isso, vou acessar aqui uma nova aba do Google Chrome e vou digitar selenium python. No primeiro link, nós temos a documentação do Selenium utilizando o Python.

[00:18] Aqui na aba de instalações, no 1.3, nós temos uma propriedade chamada Drivers, e podemos observar que o Selenium requer alguns drivers e ele é compatível com o Google Chrome, com o Edge, o Firefox e o Safari. O que nós queremos utilizar é o Google Chrome, então eu vou clicar no link ao lado do Google Chrome.

[00:38] Quando eu abro esse link, aparecem algumas versões do Chrome, então é importante que você veja qual a versão do Chrome que você está utilizando. Vou selecionar no Chrome e temos aqui “About Chrome”.

[00:48] E aparece aqui a versão que eu estou utilizando é a 85.0.41 e continua. Só isso aí já é suficiente para nós. Então 85.0.41 e continua 83... maravilha, é isso mesmo. Vou clicar nessa versão do Chrome com o Selenium, aparece aqui as opções com base nos sistemas operacionais. Vou selecionar a minha opção, que é o Mac, se eu estiver utilizando Windows ou Linux, você seleciona conforme o seu sistema operacional.

[01:19] Fiz o download desse arquivo. O que eu vou fazer agora? Eu vou dezipar esse download que fizemos, deixa eu minimizar a tela do Chrome para visualizarmos. Clico duas vezes, ele abre esse chromedriver. Observe que ele é um arquivo executável.

[01:35] Se você estiver utilizando o Windows, ele vai estar lá “.exe”. Só por questão de segurança, e para manter o nosso código organizado, com os drivers organizados, vou colocar esse chromedriver aqui dentro da nossa pasta do projeto, do “tdd_busca_animal”. Notaremos que ele está aqui na barra lateral e vamos configurar agora para utilizar o nosso Google Chrome como navegador principal da nossa aplicação. Como que fazemos isso?

[02:04] Primeira coisa que precisamos fazer é indicar para o webDriver que o driver que vamos utilizar é o chromedriver que vamos utilizar para rodar os nossos testes. Então, como que fazemos isso? Vou pegar a instância que estivermos utilizando do browser, self.browser, e vou falar que ela vai ser igual ao webdriver.Chrome. Como argumento, nós vamos passar o caminho do chromedriver para ele.

[02:45] Então vou acessar na pasta “tdd_busca_animal”. Se você estiver utilizando o Windows, vai aparecer em cima o caminho desta pasta, você coloca aquele caminho, o nome chromedriver.exe.

[02:58] No nosso caso do Mac, existe um atalho que é o “Option + Command + C”, ele vai copiar o caminho deste arquivo para mim, eu venho no código, coloco aspas simples, deixa eu abrir minha tela só para visualizarmos, dou um “Command + V” e ele coloca para nós o arquivo. Então, lembre, se estiver utilizando Windows, chormedriver.exe, com o nome certo, endereço ponto exe.

[03:22] O que vamos fazer? Eu vou executar o chromedriver aqui agora. Vou abrir, vamos executar um teste, então, deixa eu fechar ali ao lado para visualizarmos bem. manage.py test, como sempre fizemos, dou um “Enter” e nenhum erro acontece.

[03:37] O que pode acontecer na sua casa ou no seu sistema operacional? Pode ser que surja um erro de o chromedriver foi bloqueado, porque não foi identificado o desenvolvedor, alguma coisa assim. Se você estiver utilizando o Mac, vai lá em System Preference, “Preferência de Sistema > Segurança e Privacidade”, e vai aparecer aqui embaixo: ochromedriver tentou acessar alguma coisa, daí você vai lá e dá permissão, dá um allow anyway, e o seu chromedriver já vai estar configurado. Isso aqui no nosso caso do Mac.

[04:19] Então, feito isso, rodei o teste mais uma vez. Aparentemente está tudo certo, e vamos entender outra coisa bem legal também. Observe que temos uma função que inicia, prepara o nosso cenário de testes que é essa função setUp. Só que existe uma função também que é executada após os métodos de teste finalizarem, que é uma função chamada tearDown.

[04:45] O que acontece? Nós subimos um servidor, nós não conseguimos ver esse webdriver ainda, nós vamos ver daqui a pouco, mas nós subimos um servidor e de alguma forma nós precisamos limpar, falar assim: depois que abrimos a janela do navegador do Chrome e realizou o teste, nós queremos fechar essa janela também. E como que fazemos isto?

[05:06] Nós vamos colocar aqui a função tearDown. Deixa eu colocar embaixo do código, deixa eu minimizar aqui o terminal, vou criar aqui mais um função que eu vou chamar de tearDown, tear tudo minúsculo, e o D maiúsculo do Down, tearDown, passar aqui a instância que tivermos, que vamos utilizar, e aqui do jeito bem tranquilo, nós falamos: esta instância, nós vamos fechar o nosso browser, browser.quit.

[05:35] O que acontece? O que isso significa? Significa que, quando formos realizar o nosso primeiro teste, nós configuramos o webdriver do navegador que queremos utilizar que é o Chrome, nós vamos realizar uma série de testes. Depois, quando os nossos testes forem executados, nós vamos fechar a nossa aba do Chrome com essa função tearDown.

[05:59] Elas precisam ter esses nomes especificamente. Então, setUp, vamos preparar o nosso teste, configurar o nosso webdriver e tudo que precisamos, tearDown nós fechamos o nosso browser.

### URL do servidor e teste falha

[00:00] Configuramos o webdriver, criamos uma função que inicia o driver, depois outra que fecha o nosso browser, só que, será que, de fato isto está acontecendo? Eu ainda estou na dúvida. Vamos criar um método para testarmos se o nosso navegador de fato está abrindo uma nova janela e depois se ele fecha. E mais, vamos tentar abrir o site da Alura, por exemplo.

[00:26] Então, eu vou criar aqui um teste, e o teste vai ser definido assim, vai ser também uma função, e eu vou dizer o seguinte: test _, e aqui já temos uma primeira dica importante. Sempre quando vamos testar utilizando a subclasse do LiveServerTestCase. É importante, quando formos criar os métodos de teste, utilizarmos test_ e o nome do teste que queremos criar. Então, test_para_verificar_se_a_janela_do_browser_esta_ok, se está abrindo.

[01:26] Aqui dentro, o que eu vou fazer? Eu vou precisar colocar a instância do nosso browser e falar para ele, vai neste endereço, e vou fazer isso assim: pegar a instância que estivermos utilizando: self.browser.get para ele ir para uma determinada página. Vou colocar aqui o endereço da Alura. Claro que eu tenho aqui o endereço da Alura em algum lugar. Vou pegar aqui este endereço, vou colocar ’https://www.alura.com.br’ no código.

[01:57] Agora sim, vamos rodar isto aqui para ver o que acontece: o computador vai explodir, se vai abrir a janela mesmo do webdriver. Bom, python manage.py test, dei um “Enter”, criou, está fazendo algumas coisas e temos uma mensagem, olhe que interessante. Aquela mensagem que eu havia dito para vocês. Ele falou assim: o chromedriver não pode funcionar, porque não sabemos se ele é um malware, nós não temos certeza quem é o desenvolvedor dele.

[02:24] E o que vamos fazer? Vamos jogar ele para o lixo? Não. Nós vamos cancelar. Eu vou abrir aqui o meu System Preference, Preferências do Sistema, acessar aqui o Security, e aqui tem: chromedriver foi bloqueado porque não conseguimos identificar o desenvolver. Eu vou dizer: pode abrir, pode confiar no chromedriver. Se eu estou falando que pode confiar, pode confiar.

[02:44] Vamos executar o nosso teste de novo, mais uma vez: python manage.py test, quando eu dou um “Enter” aparece uma mensagem perguntando: o chromedriver, você tem certeza mesmo que quer abrir? Eu vou dizer, tenho, pode abrir. Dou um Open e vamos ver o que acontece.

[03:03] Abriu o site da Alura. Fechou o site da Alura. E aconteceu um monte de coisa legal, e deu um ok aqui no terminal, e temos um ponto no terminal também. E agora, senta aí que vamos entender tudo que aconteceu. Vou até jogar o meu terminal aqui para cima para visualizarmos tudo que aconteceu.

[03:19] Olha só, eu digitei python manage.py test, o que aconteceu? Ele criou um test database for alias, um apelido default. Olha que interessante: quando nós rodamos um teste que criamos, este teste não vai pegar os dados da nossa base de dados para testarmos. Não, é criado um database para executar este nosso teste, depois ele checa os erros do nosso sistema. Se nenhum erro for encontrado, nós temos um ponto.

[03:54] Então cada ponto vai ser uma alegria, vocês não têm noção a alegria que vai ser cada ponto durante este curso.

[04:01] E ele fala em quanto tempo este teste, um teste foi rodado, ele deu aqui um OK. No final, ele deu o OK, porque executou todos os testes e então destruiu o nosso database. Isso ficou bem bacana, ficou bem legal. Mas eu não quero abrir a página da Alura no nosso sistema, nós queremos testar uma funcionalidade para buscar animais, para saber se o animal é doméstico, venenoso e assim por diante.

[04:32] Então, o que eu vou fazer? Vou precisar indicar que a janela que eu quero testar, que eu quero abrir para realizar este teste é a janela do meu servidor. Então vou alterar aqui o nome do teste, vou colocar outro nome test_abre_janela_do_chrome. E aqui, no lugar de todo o endereço da Alura, eu não quero usar o endereço da Alura, eu vou pegar self.live_server_url. Dessa forma, o que vai acontecer? Nós vamos executar os nossos testes com base no nosso servidor, na instância do nosso servidor.

[05:20] Vou executar mais uma vez para visualizarmos. “Command + J”, executando, ele está criando. Nós não vimos janela nenhuma, ele apareceu ali nada, porque o nosso servidor ainda, de fato, não tem nada. E só para ficar legal, para começarmos a entender melhor como funciona este nosso caminho de teste, eu vou colocar um teste que vai falhar para entendermos esse cenário.

[05:44] Cenário lindo! Apareceu o ponto aqui no nosso teste, teste aprovado. Mas se, de fato, o nosso teste falhar? Então eu vou criar o teste falhador. Vou chamar o def test_falhador, ou test_deu_ruim. Vou colocar aqui test_deu_ruim. E aqui, eu vou colocar de propósito um erro para o nosso teste falhar. Vou colocar um docstring aqui só para ficar mais claro também. Então ”””teste de exemplo de erro”””.

[06:23] O que vamos fazer agora é falar: esta instância que estamos utilizando, self, vou adicionar um teste que vai falhar, com a palavra fail,self.fail, e aqui eu posso colocar a mensagem de erro (‘Teste falhou – deu ruim mesmo’).

[06:46] Rodando aqui o nosso terminal, manage.py test, observa, nós temos um teste que passa que é o nosso teste do servidor, e um teste que vai falhar para entendermos e começarmos a ficar acostumados com as mensagens de erro da nossa aplicação, com os testes que vão falhar.

[07:02] Dei um “Enter”, ele executou, está criando, abriu a janela, passou o primeiro, aí aconteceu algo e ele deu um erro. Vamos entender o que aconteceu. Ele rodou dois testes em 5.969 segundos, e ele falou: um teste falhou.

[07:20] Se subirmos no terminal, nós temos o primeiro ponto do nosso teste do servidor que passou e um F maiúsculo, gigante falando aqui, F, FAIL, deu ruim. Então, o test_deu_ruim lá do setup.tests.AnimaisTestCase, então ele nos deu o caminho, então setup.tests.AnimaisTestCase. Ele falou assim: o “test_deu_ruim”, que é este nosso teste que deu ruim, este teste falhou, e aqui nós colocamos a docstring e ele falou teste de exemplo de erro.

[07:55] Observe que interessante: a medida em que formos testando a nossa aplicação e criando os nossos códigos, esta docstring vai ser muito importante para entendermos o que de fato estamos tentando testar. Lembra: quando escrevemos uma aplicação, um software, um método, não é para que só eu entenda, ou só para você entender. É para que outros desenvolvedores, desenvolvedoras, entendam o que estamos escrevendo.

[08:21] Então, este teste que falha, apesar de ter uma aparência um pouco assustadora, feio, um monte de coisa, fica tranquilo: o computador não vai explodir, não vai acontecer nada disso. Ele dá FAIL, deu o nome do teste que falhou, embaixo ele exibiu a docstring indicando detalhes sobre o teste que estávamos executando.

[08:43] O que vamos fazer na sequência? Na sequência, vamos começar a pensar na nossa aplicação mesmo, na funcionalidade da nossa aplicação. Então, nós executamos aqui um teste que abre o navegador, verifica se o navegador está funcionando na URL que queremos, o teste foi aprovado, o servidor da nossa aplicação ele subiu, está funcionando. Nós colocamos um teste que falha, para começarmos a nos acostumar com estas mensagens de erro também.

### Banco de dados

Sempre que executamos nossos testes com manage.py test é criado um banco de dados, como ilustra a seguinte imagem:

        python manage.py test            

        Creating test database for alias 'default'
    
    Quando nossos testes acabam:

    Destroying test database for alias 'default'

Qual a importância dessa ação de criar o banco para os testes, executar os testes e quando são concluídos, deletar o banco de dados de teste?

a) Manter a atomicidade dos dados.

b) **Alternativa correta:** Manter a integridade e consistência dos dados de produção.
- _Alternativa correta! Certo! Esse processo ajuda a garantir que os dados de teste ficam separados dos dados reais e válidos do ambiente de produção._

c) A ação de criar e deletar um banco de dados apenas para os testes é demorada e não é tão importante assim, já que os dados deste banco não servem para nada.

### Para saber mais: História do TDD

TDD ficou bastante popular após a publicação do livro TDD: By Example, do Kent Beck, em 2002. O próprio Kent afirma que TDD não foi uma ideia totalmente original. Ele conta que, em algum momento de sua vida, leu em algum dos livros de seu pai (que também era programador) sobre uma técnica de testes mais antiga, com a qual o programador colocava na fita o valor que ele próprio daquele programa, e então o desenvolvia até chegar naquele valor.

Ele próprio conta que achou a ideia estúpida. Qual o sentido de escrever um teste que falha? Mas resolveu experimentar. Após a experiência, ele disse que "as pessoas sempre falavam para ele conseguir se separar o que o programa deve fazer da sua implementação final, mas ele não sabia como fazer, até aquele momento em que resolveu escrever o teste antes."

Daquele momento em diante, Kent Beck continuou a trabalhar na ideia. Em 1994, ele escreveu o seu primeiro framework de testes de unidade, o SUnit (para Smalltalk). Em 1995, ele apresentou TDD pela primeira vez na OOPSLA (conferência muito famosa da área de factor, já que muitas novidades tendem a aparecer lá).

Já em 2000, o JUnit surgiu e Kent Beck, junto com Erich Gamma, publicou o artigo chamado Test Infected (2000), que mostrou as vantagens de se ter testes automatizados e como isso pode ser viciante. Finalmente em 2002, Kent Beck lançou seu livro sobre isso, e desde então a prática tem se tornado cada vez mais popular entre os desenvolvedores.

### O que aprendemos?

**Nesta aula:**
- Configuramos o Selenium para utilizar o Google Chrome;
- Subimos um servidor de teste com LiveServerTestCase;
- Criamos um método para falhar e vimos como essa falha é exibida quando o teste é executado.

**Na próxima aula:**
Vamos aprender o que é história do usuário, criar nosso app e testar as urls da aplicação!

## 03. RequestFactory e templates
### História do usuário

[00:00] Nós vimos como funciona um teste que é aprovado e um teste que falha, e como, com o tempo, desenvolver habilidades para conseguir ler estas linhas de testes que falharam.

[00:15] Vamos começar uma nova etapa no nosso desenvolvimento, nossa experiência com o TDD. Nós sabemos que vamos criar um teste para verificar, ou um trecho pequeno de código, que chamamos de teste de unidade, ou um teste muito maior, que é um teste funcional, e vai, de fato, simular um cenário, um usuário clicando em alguma parte do nosso site, da nossa aplicação.

[00:42] Para começar, vamos utilizar, para este curso, o foco da busca de um determinado animal. Então, vamos criar a seguinte história para o nosso projeto, a história de um usuário, que é assim: Vini deseja encontrar um novo animal para adotar. Ele encontra o “Busca Animal” e decide usar o site, porque vê no menu do site escrito “Busca Animal”. Já que ele quer adotar um animal.

[01:11] Ele vê um campo para pesquisar animais pelo nome, então vai digitar ali, em algum lugar vai ter um campo onde ele vai digitar o nome do animal que vai exibir, algo vai acontecer. Ele digita, ele pesquisar, leão, e clica no botão pesquisar. Observa que cada desta vai ser um teste que vamos realizar. O site exibe quatro características do animal pesquisado. Ele desiste de adotar um leão.

[01:37] Vamos copiar esta história do usuário. Eu vou deixar este link lá na atividade anterior a este vídeo, e vou colar este código, este link aqui. Vini deseja encontrar um novo animal que ele quer adotar, ele encontra o site, e tem a história completa aqui. O que este teste faz? Este teste vai verificar se, de fato, um usuário consegue buscar um animal, é isto que este teste faz.

[02:10] Então, o que eu vou fazer? Eu vou criar um novo teste, vou digitar test_, uma nova função que eu vou digitar test_buscando_um_novo_animal. Como parâmetro eu vou utilizar a instância que vamos utilizar, e temos aqui um pass. Eu vou colocar todo este código da história para lá. Selecionei tudo, “Command + ]”, ele vem para dentro de test_buscando_um_novo_animal. Vou pegar este pass e vou jogar lá para baixo de tudo. Para não ter erro, nossa função não ter nenhum erro.

[02:54] Nós vimos a importância do docstring para quando vamos executar um novo teste. Então, vamos colocar também, para manter o nosso padrão, uma docstring aqui explicando para que serve este teste. Uma coisa importante, nós não precisamos ter medo de ser prolixo aqui. O nosso teste, apesar de ter o nome test_buscando_um_novo_animal, nós podemos descrever um pouco melhor aqui na nossa docstring

[03:18] Então vou escrever aqui, por exemplo, Teste se um usuário encontra um animal na pesquisa, por exemplo. Então, temos aqui uma definição um pouco melhor. test_buscando_novo_animal, Teste se um usuário encontra um novo animal pesquisando, acho que fica mais legal.

[03:58] E aqui, nós temos o nosso cenário com as histórias do usuário, com os requisitos do nosso sistema. Então, ele quer encontrar um novo animal, nós temos um contexto, existe um cenário. Lembra quando criamos o TDD da idade, que passamos os valores 1991 e 2050, que eram o cenário de teste? Vamos ter o mesmo aqui. Nós já temos o cenário de teste. O que vamos fazer agora? Vamos começar a atacar para que cada etapa deste cenário de teste, desta história do usuário seja atendido.

[04:32] Então, vamos lá. Ele encontra o Busca Animal e decide usar o site, porque ele vê no menu do site escrito Busca Animal, e é isso que vamos fazer nos próximos vídeos.

### ATUALIZAÇÃO

Na próxima atividade, será mostrado uma funcionalidade de código na qual ocorreu uma atualização. O código exibido na aula pelo instrutor será:

        find_element_by.css_selector('exemplo')

**Porém esse código não funciona mais dessa forma.** A forma correta será:

        find_element(By.CSS_SELECTOR, 'exemplo')

Por gentileza, considerar apenas o exemplo acima para alcançar o mesmo resultado!

Mais informações estão disponíveis na documentação do [selenium.webdriver.common.by]('https://selenium-python.readthedocs.io/api.html')

### Criando o app

[00:00] Ao observarmos a história do usuário, notaremos que é mencionado que ele encontra o site, decide usar o site, encontra o “Busca Animal”, e vê no menu do site escrito "Busca Animal". Duas etapas aqui. Primeira: precisamos criar um teste para verificar se o nosso site, de fato, está no ar. Se a nossa home page está no ar. Vamos fazer isto, então?

[00:22] Bom, para começar, vou criar a nossa home page aqui, vou dar um “Enter” aqui embaixo desta história, eu vou criar home_page, e vou criar, subir a nossa home page. Só que aqui, tem algo interessante. Observa que a nossa home page é justamente o código que testa se abre uma janela. Então, vai lá no browser e pega a URL no nosso servidor. Vou dar um “Command + X” em self.browser.get(self.live_server_url) e vou remover.

[00:48] Estes dois testes nós utilizamos como exemplo: o test_abre_janela_do_chrome e o test_deu_ruim nós não vamos utilizar, então vamos remover eles daqui para ficar bem limpo este nosso código, e vou passar aquele conteúdo self.browser.get(self.live_server_url) para baixo da história, nós subimos o nosso servidor.

[01:02] Aqui tem um ponto interessante: para deixar a nossa sintaxe, o nosso código mais semântico, o que acontece? Quando subimos o servidor com o runserver, por exemplo, localhost:8000 barra algo, então, só para deixar aqui bem semântico, vou colocar também o mais concatenando com a nossa barra para dizer que a página principal, home da nossa aplicação.

[01:27] Subi aqui a nossa home page, vou salvar. Se eu executar aqui o nosso teste, vamos ver, manage.py test, ele foi lá e tudo certo, nossa página, nossa home page subiu. Ele vê no site , no menu do site escrito Busca Animal. Como que vamos fazer isto?

[01:46] Para conseguirmos verificar um determinado elemento na página, nós podemos usar o Selenium. Existe uma propriedade no Selenium chamada find_element_by_css_selector, que é a que vamos utilizar agora. O nome é maluco, mas fica tranquilo que é tranquilo. Fica tranquilo que vamos conseguir entender.

[02:06] brand_element, que é o elemento que queremos buscar na tela, e vou falar assim, vai lá no self.browser, lá na página, e vamos dar aqui um .find_element_by_css_selector, e aqui dentro, nós vamos passar o nome do elemento css, como string. Então, vou colocar aqui ’.navbar’. Então, eu falei: vai lá na nossa página e pega um elemento chamado navbar, e ele vai pegar este brand_element.

[02:46] Outra coisa importante também, ele vê no menu do site escrito Busca Animal, então vamos precisar garantir que este elemento, o texto deste elemento é Busca Animal. Então, vamos fazer isso.

[03:00] Vamos colocar aqui na próxima linha, self.assertEqual, no singular o Equal, aqui como que vamos fazer? O primeiro parâmetro vai ser o que queremos escrito neste elemento. Então, queremos escrito ’Busca Animal’, o segundo parâmetro é o nosso brand_element, porém o conteúdo dele, o texto dele. Vamos pegar brand_element.text

[03:43] Abrindo o nosso terminal de novo, executando o nosso teste, olha só o que vai acontecer. Ele vai abrir a nossa página home e um erro aconteceu. Nós já esperávamos este erro. Nós temos uma série de informações na tela para entender agora. Parece que explodiu aqui um monte de coisa.

[04:03] Se nós pararmos para observar, para analisar esta mensagem. Ele fala aqui: nenhum elemento foi capaz de identificar este navbar, este selector. Nós não identificamos este css selector com este conteúdo do navbar.

[04:20] O que acontece? Olha só que bizarro, nós realizamos um teste agora, mas nós não temos nem o app, nenhuma rota cadastrada, nenhuma página, nem um template. Nós não temos simplesmente nada. Para solucionar este problema, o que precisamos fazer? Nós precisamos criar o nosso app de animais e, nele, escrever alguns testes para garantir que este nosso teste funcional vai passar.

[04:41] Então, o que vou fazer? Vou minimizar o terminal. Não vou minimizar, desculpe. Aqui no nosso terminal, vou criar o app de animais. Então, vamos lá: python manage.py start app animais e dou um “Enter”, e ele vai criar o nosso app de animais que podemos visualizar aqui no menu ao lado que agora nós temos setup, as configurações da nossa aplicação, e o nosso app de animais.

[05:10] O que precisamos fazer é garantir que este app de animais faça parte do nosso projeto. Lá em settings.py, nos apps instalados, eu vou colocar também o ’animais’,.

[05:26] Agora, como toda aplicação web, o que vamos precisar fazer é aceitar solicitações http em certas URLs, e esse é o ponto inicial da nossa aplicação. Porém, o que vamos precisar fazer? Nós não queremos criar as URLs direto, nós queremos garantir que estas URLs, com estes determinados endereços sejam corretos, sejam aceitos na nossa aplicação.

[05:54] Então, precisamos testar isto também. Então, o que vamos fazer na sequência? Nós vamos criar um arquivo de teste para as nossas rotas URLs.

### Testando URLs

[TestCase]('https://docs.djangoproject.com/en/2.2/_modules/django/test/testcases/')
[Test]('https://docs.djangoproject.com/en/4.1/topics/testing/overview/')

1. Criamos um arquivo chamado test_urls.py:

        from django import TestCase
        from django.urls import reverse
        from animais.views import index

        class AnimaisURLSTestCase(TestCase):
            def test_rota_url_utiliza_vies_index(self):
                root = reverse('/')
                self.assertEqual(root.func, index)

---

[00:00] Nós criamos um teste funcional, onde é necessário que exista um navbar com determinado texto escrito. Para isso, nós criamos o nosso app de animais e agora vamos começar a testar para chegar neste teste funcional aprovado.

[00:17] Para começar, para exibirmos uma página com determinada URL, com uma view renderizando a página correta, com um template escrito aquilo, observe que são várias etapas. Vamos começar agora os nossos testes de unidade.

[00:32] O que vamos fazer? Quando criamos um app aqui no Django nós temos este arquivo “tests.py”. Eu vou deletar este arquivo, vou deletar porque eu vou criar vários testes de unidade. Um teste para URL, um teste para o modelo, um teste para a nossa view. Então, eu vou criar, dentro de animais, um new folder, uma nova pasta, que eu vou chamar de “tests”. Dentro desta pasta, nós vamos executar os conteúdos, os testes que nós temos aqui dentro.

[00:59] Então eu vou colocar “init.py” para ele executar estes testes e vamos começar com o nosso teste de URL. “tests_urls.py”. O que eu quero que a minha URL faça? Qual o objetivo deste meu teste de unidade? Eu quero ver se determinada requisição é atendida por uma view específica, então vamos lá.

[01:27] A primeira coisa, eu vou precisar importar lá do “django.test” um cara chamado TestCase, então vou colocar aqui from Django.test import testCase. Vamos ler um pouco sobre este TestCase? Clicando com o botão direito, vou abrir uma nova aba e vou digitar no Google “TestCase Django”. Aqui tem uma pequena explicação sobre o que são estes nossos testes e qual a ideia destes nossos testes de unidade.

[02:12] Então, quando clicamos nesta página nós temos uma pequena explicação. A classe mais comum para escrevermos testes em Django. É o que queremos, é o suficiente. Tem uma explicação quando não formos usar um banco de dados, nós podemos usar o SimpleTestCase também, mas fica aí o desafio para você ler este trecho desta documentação, está bem tranquilo para entender.

[02:32] Importamos o TestCase, agora nós queremos testar URLs, nós precisamos de alguma forma verificar as URLs que nós vamos testar na nossa aplicação. Então, eu vou fazer assim: from django .urls eu quero importar, import, um reverse. Ele vai ser responsável por identificar qual a URL que estamos utilizando.

[02:56] E para finalizar, para que se chegue em uma URL, precisamos de um método na view, fazendo a mediação. Então, vou colocar aqui from animais.views, eu quero importar o index, já que queremos testar a nossa classe, o nosso método raiz da nossa aplicação, nossa URL raiz.

[03:28] Então, eu vou colocar class AnimaisURLSTestCase, por exemplo, acho que faz sentido, e nós vamos utilizar como argumento o TestCase.

[03:41] Então, o primeiro método que eu quero testar é o seguinte: eu quero verificar se nós estamos utilizando a index da view, então test_rota_url_utiliza_view_index. Como argumento, eu vou passar a instância que nós temos, e aqui abaixo nós vamos começar o nosso teste.

[04:17] Então eu vou fazer assim: o root principal da nossa aplicação é o localhost:8000/, o barra vai ser o nosso endereço principal. Então vou colocar aqui um reverse(‘/’). Fora isto, vou criar aqui uma assertação, uma afirmação, assertEqual, e vai ser o seguinte: eu quero verificar se a função que eu estou utilizando no meu root.

[04:51] Então: root.func, vai ser atendido pela minha index. Salvei isto aqui para deixarmos o nosso código ainda mais prolixo, vamos colocar docstring, vou colocar aqui, por exemplo. ”””Teste se a home da aplicação utiliza a função index da view”””, por exemplo.

[05:20] Salvei. Vamos executar este teste? “Command + J”, vem aqui no terminal python manage.py test. Ele começa a fazer, verificar. Maravilha! Nós temos dois erros. Primeiro erro: test_buscando_novo_animal que ele não achou o css, faz sentido.

[05:38] E depois, o animais.tests.test_urls que é este arquivo que escrevemos e ele falou: o nome index não pode ser importado do animais.views index, e faz sentido. Nós não criamos a nossa view, então vamos criar a nossa view.

[05:53] Então vamos vir aqui, em “views.py” e vamos criar uma função chamada index que eu não vou passar nenhum argumento, vou deixar ela assim. Vamos executar mais uma vez. Executando. O nosso teste falhou, ele executou outro teste, vamos dar uma lida, testando test_buscando_novo_animal, que é o nosso teste funcional, e aqui o nosso test_rota_url_utilizar_view_index, testa se a home da aplicação utiliza a função index da view.

[06:29] Nós temos uma mensagem aqui: reverse (‘/’) not found, significa que não conseguimos encontrar este endereço na nossa aplicação. Então, o que precisamos fazer? É importante que, quando criamos uma URL, nós registremos esta URL lá no setup, nas URLs do nosso projeto. Vamos fazer isto também.

[06:57] O que é comum, lá em “setup > urls.py”, e aqui todas as URLs do nosso código, eu vou importar lá de animais.views import index, e aqui nós vamos dizer assim: existe um path para o endereço raiz da aplicação que vai ser atendido pela index.

[07:24] Vou executar de novo. Um erro, que é o primeiro erro do nosso teste. O segundo, se scrollarmos um pouco, observe que nós continuamos com este erro. Ele diz que não foi encontrado. Isto tem relação com as requisições e solicitações do http.

[07:43] Mas o que eu preciso fazer agora? Observa, nós precisamos de uma ferramenta capaz de ajustar estas requisições, solicitações http dentro do nosso teste, e existe um cara responsável por isto, que é o RequestFactory que vamos ver no próximo vídeo.

### RequestFactory

[Advanced Test]('https://docs.djangoproject.com/en/4.1/topics/testing/advanced/')

1. Em test_urls.py:


        from django import TestCase, RequestFactory
        from django.urls import reverse
        from animais.views import index

        class AnimaisURLSTestCase(TestCase):
            def setUP(self):
                self.factory = RequestFactory()

            def test_rota_url_utiliza_vies_index(self):
                request = self.factory.get('/')
                response = index(request)
                self.assertEqual(reesponse.status_cod)

---

[00:00] Então o que precisamos para testar, para finalizar o nosso teste aqui da view é de uma ferramenta capaz de criar e ajustar as solicitações HTTP para que possamos testar as nossas URLs, e a ferramenta que vamos utilizar é o RequestFactory, ele também será um import do nosso django.test.

[00:22] Então, vou colocar aqui: RequestFactory, e nós vamos criar, assim como fizemos no nosso funcional, uma classe responsável por criar o nosso cenário de teste aqui de unidade também.

[00:39] Então, vou criar uma nova função que eu vou chamar de setUp, ou seja, assim que começar este teste eu já quero preparar algumas coisas, passei ali o self e vou falar assim: self.factory = RequestFactory. O que vamos mudar? Nós sabemos que para conseguir uma requisição, em um determinado método, nós vamos utilizar o RequestFactory no lugar do reverse.

[01:23] Então eu vou fazer o seguinte: vou criar uma variável para manter a nossa requisição, vou falar assim: request = self.factory.get e aqui eu vou passar qual endereço que eu quero testar. Eu quero testar, quero armazenar este endereço (‘/’). E a resposta que vamos ter desta requisição, vou colocar aqui um response, ele vai ser igual a index utilizando o request que fizemos.

[02:00] Agora, nós vamos ter que mudar um pouco a nossa forma de verificar isto aqui, já que estamos vinculando a nossa resposta à index. Observe uma coisa importante: para conseguirmos verificar se, de fato, estamos fazendo a requisição para aquela view e aquela view está mandando um resultado correto, nós podemos usar aqui o self.assertEqual(response.status_code, 200). Ou seja, deu certo. Vamos executar este teste para vermos o que vai acontecer?

[02:35] Vou executar. Primeiro não funcionou, ele deu um erro aqui do navbar e ele falou assim, olha só que interessante: a sua index não tem nenhum argumento passado, nenhum argumento é esperado. Você sabe, qual o argumento esperado aqui para a nossa função view da index? A requisição, o request, nós precisamos passar esta nossa requisição também para a index. Então, eu vou passar def index(request).

[03:07] Vamos executar mais uma vez. Limpei o meu terminal, executando um teste mais uma vez. Deu ruim ali, vamos verificar, aqui é o erro do funcional, e aqui ele disse assim: “‘NoneType’ object has no atribute ‘status_code’”.

[03:23] Vamos ver. Então lá na nossa view, ele chegou aqui na nossa view e ele falou: nós não temos nenhum status_code aqui, nós precisamos de um status_code aqui. E qual a forma mais simples de falarmos: olha, recebemos uma requisição e nós queremos uma resposta http. Nós podemos alterar aqui, por exemplo, vou buscar do django.http, vou importar um módulo chamado HttpResponse. E o que eu vou fazer? Vou retornar ele, return HttpResponse. Só isso.

[03:58] Vamos verificar para ver o que vai acontecer agora? Rodando o nosso teste mais uma vez, um ponto. OIha! Uma coisa boa. Teve o erro lá do CSS que ele não achou, mas nós tivemos um ponto aqui, o que é este ponto? Nós já sabemos, o nosso teste de URL foi aprovado. O que aconteceu? O que fizemos? Nós criamos uma função que testa para ver se esta URL vai ser atendida pela nossa index correta, e isto aconteceu.

[04:28] Nós estamos conseguindo manter o ciclo certo: nós tivemos uma requisição, a requisição foi a index, uma requisição para barra, para o home principal, ela foi para a index, esta index voltou o status_code 200, isto está certo.

[04:43] Qual vai ser o nosso próximo passo agora? Agora, o que falta? Já que nós temos a index voltando o status_code certo, nós podemos ter uma index renderizando uma página com aquele menu, e é isto que vamos fazer na sequência.

### Análise do código

Uma pessoa durante o curso de TDD com Django desenvolveu o seguinte trecho de código:

        class AnimaisURLSTestCase(TestCase):
            def setUp(self):
                self.factory = RequestFactory()

Com base no código acima e analisando as afirmações abaixo, podemos afirmar que:

a) **Alternativa correta:** RequestFactory é uma ferramenta para criar e ajustar solicitações HTTP.
- _Alternativa correta! Certo! Podemos pensar nele como uma versão simplificada do WebDriver do Selenium._

b) **Alternativa correta:** Qualquer método em uma subclasse TestCase que comece com o prefixo test_ será executado sempre que executarmos o python manage.py test.
- _Alternativa correta! Certo! Assumindo que não adicionamos um argumento para excluí-lo, o método será executado._

c) O método setUp() é executado quando os métodos de testes são concluídos.

### O que aprendemos?

**Nesta aula:**
- Vimos a importância da história do usuário para guiar nossos testes;
- Criamos o app de Animais;
- Testamos a url principal da aplicação.

**Na próxima aula:** Vamos criar nosso primeiro template e dar continuidade no teste funcional, verificando se alguns elementos HTML estão presentes em nossa index!

## 04. Template e cenário de teste
### Template

1. Em test_urls.py:


        from django import TestCase, RequestFactory
        from django.urls import reverse
        from animais.views import index

        class AnimaisURLSTestCase(TestCase):
            def setUP(self):
                self.factory = RequestFactory()

            def test_rota_url_utiliza_vies_index(self):
                request = self.factory.get('/')
                with self.assertTemplateUsed('index.html')
                    response = index(request)
                    self.assertEqual(reesponse.status_cod)

---

[00:00] Nosso teste de unidade passou, mas ainda não avançamos no nosso teste funcional, precisamos de um template.

[00:07] Vamos configurar o nosso teste de unidade lá no nosso test_urls para verificar se a nossa resposta da view usa um template e para isso, nós vamos aprender a utilizar um gerenciador de contexto, que é a cláusula with, junto com um método chamado assertTemplateUsed para verificar se, com base naquele contexto, estamos utilizando um determinado template. Existem várias afirmações e testes que são utilizados desta forma que vamos ver agora.

[00:42] Então, para começar, o que vamos fazer? Nós vamos testar se o template é chamado na nossa função view index. Então, o que eu vou fazer? Nós pegamos a requisição e eu já vou colocar aqui embaixo a cláusula with, o que vai acontecer? Quando utilizamos o with nós vamos verificar um contexto.

[01:04] Então, eu vou passar aqui self.assertTemplateUsed e vamos utilizar o nome do template que gostaríamos de verificar se está usando, vou passar aqui index.html, dou os dois pontos, passo as respostas anteriores para cá. Selecionei as linhas 14 e 15, “Command + ]” e ele arrasta para o lado.

[01:33] Olha só, o que fizemos? Nós passamos um contexto, criamos um contexto para o nosso teste perguntando: estamos utilizando este template index? E colocou ali a resposta. Vamos executar o nosso teste para o que acontece? python manage.py test. Falhou, já vamos verificar. E recebemos dois erros.

[01:58] Um erro informando que teste se a home utiliza a função index da view e nós temos uma mensagem, index.html não foi renderizada. Não tem este template, este template não foi renderizado. E nós já sabíamos disso. Nós não temos a página ainda, o nosso template criado.

[02:18] Então, o que vamos fazer? Antes de criar o template, vamos deixar a nossa view preparada para renderizar um template.

[02:25] Então, lá na minha view, minimizando o meu terminal, eu não vou mais utilizar o django.http response só para ele jogar uma resposta, eu vou utilizar lá do django.shortcuts import render e vou falar um retorno que conhecemos muito bem: return render, e vamos renderizar quem? Devolvendo a request, podemos visualizar o primeiro parâmetro, request, segundo parâmentro, a nossa página index.html.

[02:59] Vou executar mais uma vez. Você já imagina o que vai acontecer. Executei. Vai ter um erro e vamos visualizar o que diz este erro, o que este erro está querendo nos dizer. Bom, temos aqui um erro do CSS que não foi encontrado, lá do nosso teste funcional, e nós temos outro erro.

[03:22] django.template.exception. Template não existe: index.html. Agora, vamos botar a mão na massa, vamos criar o template e vamos criar o nosso arquivo index.html. Vou criar dentro da minha pasta, do meu escopo de animais mesmo, new folder, vou chamar de templates, dentro de templates eu vou criar um novo arquivo chamado index.html.

[03:53] Vou alterar aqui a minha página para colocar HTML e vou colocar html. Então alterei aqui embaixo no meu VS Code, só para ele gerar um HTML, vou colocar html: 5 e ele vai gerar para nós um documento.

[04:09] O título vai ser Busca Animal, agora, aqui no <body> eu vou colocar o navbar que estamos querendo tanto querendo encontrar. Então, o navbar eu vou passar aqui, nós não temos nenhum href por enquanto, só uma classe.

[04:25] Então, a classe que eu vou chamar de navbar, e o conteúdo deste navbar vai ser Busca Animal. O que vamos fazer agora? Vamos testar. Abrindo aqui o meu terminal. python manage.py test, o primeiro teste passou e o segundo teste passou. Olha que interessante: os nossos dois testes, dois pontos ali indicando que os nossos testes passaram.

[04:55] Vamos só relembrar o que fizemos aqui: nós criamos um arquivo para verificar se uma rota, se a rota principal da nossa aplicação chama uma determinada página html utilizando a cláusula with para gerar este nosso contexto. Depois, lá nas views nós renderizamos esta página index, devolvendo a requisição e a página e criamos o nosso template com a nossa página Busca Animal e colocou o navbar com o conteúdo Busca Animal.

[05:28] Isto ficou bem legal. O que acontece? Nós passamos um teste funcional, depois este teste funcional, por algum motivo falhou e fomos criando este teste em alguns testes de unidade. Então, nós verificamos se as nossas URLs estavam certas, com base nos erros das URLs nós fomos arrumando aqui, configurando a nossa aplicação e isto ficou bem legal.

### Testando campo de busca

[00:00] Vamos dar continuidade agora para os nossos testes funcionais. Acessando tests.py lá do meu setup, o que acontece? Nós temos uma próxima propriedade, um próximo requisito da nossa aplicação, ele vê um campo para pesquisar animais pelo nome.

[00:15] Vamos criar um teste para garantir que o campo estará lá e para garantir também que é possível identificar este campo, que seja fácil do usuário só olhar aquele input, aquela caixa para digitar, ele sabe que é para pesquisar animais pelo nome. Por exemplo, nós podemos criar um placeholder para este botão.

[00:36] O que eu vou fazer? Vou criar aqui o buscar_animal_input = self.borwser.find_element_by_css_selector (), e dentro do parêntesis eu vou colocar o botão que eu quero criar. Eu quero criar um input no html e vou dar um nome para ele, uma identificação que eu vou chamar de buscar-animal.

[01:12] Além disto, eu quero criar também um placeholder para este meu botão. Então, vamos criar um placeholder para este botão. vou colocar aqui self.assertEqual, e aqui eu vou pegar o meu botão buscar_animal_input.get_attribute(), qual atributo que eu quero pegar? O placeholder. Então, entre aspas, ’placeholder’.

[01:43] E qual o conteúdo deste placeholder? Ou seja, tem um botão. Quando eu olhar para este botão vai ter um texto escrito, qual o texto que quero colocar nele? Eu vou colocar, por exemplo, entre aspas, ’Exemplo: leão’. Criamos duas propriedades. Vamos rodar um teste para vermos.

[02:06] Antes de rodar o teste, eu esqueci de tirar o pass depois da história do usuário, eu vou tirar. Não precisamos mais dele no nosso código. Voltando para o terminal, vou rodar o teste. Passou no primeiro, executou e falhou o outro. Ele não encontrou um determinado elemento, input#buscar-animal, então nós temos aqui uma mensagem: elemento não foi encontrado. Vamos criar este elemento, então.

[02:31] Venho aqui na minha index.html, tenho aqui o meu navbar escrito Busca Animal, e eu vou criar o meu campo input, então eu vou digitar aqui input, observe que só de eu digitar input ele já está identificando que é uma página HTML, isto acontece aqui embaixo. Se tivermos django template, é só digitar “html” na formatação de linguagem e ele já vai formatar as nossas tags.

[02:56] Então, é do tipo texto e eu quero que tenha uma identificação, este meu input, que seja ”buscar-animal”. Salvei. Executando o nosso teste de novo. Falhou, e aconteceu um erro interessante aqui. Nós temos um erro de assertação, que ele falou assim: nada não é igual a ‘Exemplo: leão’ e faz muito sentido. Por quê? Lá no nosso teste nós criamos uma verificação para falar: olha, o placeholder deste botão é Exemplo: leão. Vamos criar, nós não criamos.

[03:32] Então do lado de input type = “text” id=”busca-animal” vou colocar placeholder= “Exemplo: leão”. Vou rodar aqui. Passamos no teste. Quero mostrar uma coisa interessante para vocês. Olha só como esta parte do teste é muito legal. Vamos supor que eu mude o placeholder do meu teste. Exemplo: leão, urso... algo assim.

[04:03] Quando eu rodar o meu teste de novo, olha a mensagem de erro que vai ser exibida. Olha só que legal. Um erro de assertação, conforme nós vimos, e ele falou assim: ‘Exemplo: leão’ não é igual a Exemplo: leão, urso.... E aqui ele colocou assim: o que eu tenho, o código que eu tenho e o que está a mais, então, ele marcou: a vírgula é um conteúdo a mais, uma string a mais, e colocou todos os conteúdos.

[04:30] Observe que a medida que nós vamos ganhando experiência com o TDD, as nossas mensagens de erros, apesar de ser este negócio maluco que explode na tela, vai nos auxiliar. Então, eu vou mudar, eu vou colocar o placeholder igual ao que eu coloquei aqui no meu teste. Então, volto lá na minha index.html, leão, urso.... Deixa eu ver se eu escrevi certo mesmo.

[04:55] Vamos rodar o teste. Se eu não escrevi nós arrumamos isto, mas passou. Então, o que acontece? Nós temos um campo e um placeholder, que é um texto dentro daquele botão. Quando a pessoa clicar neste botão, aquele texto desaparece, esta é a função do * placeholder*.

[05:14] Nós garantimos então: ele consegue ver um campo, e está lá um exemplo: leão, urso, maravilha. Vamos passar para os nossos próximos testes agora.

### Send keys

        buscar_animal_input.send_keys('leâo')
        self.browser.find_element_by_css_selector('form button')

---

[00:00] Vamos partir para a próxima parte da história do usuário? Para começar, ele diz assim: Ele pesquisa por Leão e clica no botão pesquisar. Duas ações. Então, nós precisamos testar, criar o cenário de teste onde a pessoa digita algo e clica em um botão. Então, vamos lá.

[00:17] Primeira coisa que vamos fazer vai ser pegar este botão, que é o buscar_animal_input para enviarmos uma entrada em um determinado campo, nós vamos usar o send_keys e aqui passamos o conteúdo que queremos digitar neste campo. Bom, o conteúdo que eu quero digitar, nós colocamos pesquisa por leão, vou colocar leão mesmo, com a letra minúscula, ele pesquisa por leão.

[00:45] Então, alguma coisa precisa acontecer e nós precisamos clicar, então self.browser.find_element_by_css_selector(‘form button’).click, este form tem um botão que eu vou clicar. Então: self.browser.find_element_by_css_selector(‘form button’).click, maravilha!

[01:16] Vou testar aqui o nosso código, e temos uma mensagem de erro. Nenhum elemento foi encontrado, foi localizado neste form button, e por que isto acontece? Nós sabemos que para tentarmos enviar um dado de entrada para um determinado elemento, nós vamos precisar vincular este elemento a um formulário e nós não fizemos isto ainda, por isso que não conseguimos enviar. Vamos, incluir, então, um form e adicionar o nosso botão para a pessoa clicar?

[01:50] Lá na nossa página index.html, eu vou colocar aqui o form, não vou ter uma action por enquanto, vou colocar </form> lá para baixo do input e vamos identar o input, além do nosso form e do nosso input para digitar, nós vamos ter agora também um botão. Vou escrever aqui button, e o nosso botão vai ser do tipo submit, type = submit e neste botão eu vou colocar o conteúdo, por exemplo, Pesquisar.

[02:50] Salvando. Abrindo o nosso terminal e executando mais uma vez, vamos ver: maravilha! Tudo passou no nosso teste. O que eu quero fazer agora com vocês é uma coisa que ainda não fizemos neste curso.

[03:03] Se você não foi muito curioso, provavelmente você não passou por isto, mas se você for muito curioso eu tenho certeza que você já rodou python manage.py runserver para nós visualizarmos de fato como esta aplicação está ficando. Vamos ver.

[03:20] Então, ele falou que tem as migrações ali, o que eu vou fazer aqui? Vou abrir uma nova aba anônima acessando: http://localhost:8000/, e temos aqui Busca Animal, tem o texto, o campo que vamos digitar o animal que queremos pesquisar, e aqui nós temos um botão de pesquisar. Olha só, nós estamos garantindo que esta funcionalidade passe na nossa aplicação.

[03:42] “Só que, Guilherme, eu não consegui ver o texto sendo digitado, as coisas acontecendo”. Vou parar aqui o meu servidor. Vamos voltar para os nossos testes. Eu não consegui ver esse texto acontecendo. O que podemos fazer é o seguinte: eu vou importar o time e nós vamos colocar um sleep na hora que digita o texto e clica no botão pesquisar para passarmos para a próxima ação.

[04:04] Então, eu vou colocar abaixo de busca_animal_input.send_keys (‘leão’) um time.sleep(2) de dois segundos para visualizarmos. Então, eu vou chegar aqui e ele vai parar. Vou rodar o nosso teste de novo. python manage.py test, então rodou o teste, vai subir o servidor, digitou o leão, clicou no pesquisar e nosso teste passou. Mais uma funcionalidade, mais uma história do usuário que conseguimos alcançar.

[04:35] Vou tirar este time.sleep, isto foi só para visualizarmos mesmo a coisa acontecendo, o nosso cenário de teste acontecendo. Na sequência nós damos continuidade na história do usuário.

### AssertGreater

        caracteristicas = self.browser.find_elements_by_css_selector('.result-description)
        self.assertGreate(len(caracteristicas),3)

---

[00:00] Vamos dar continuidade a nossa história do usuário, e o nosso próximo passo é o seguinte: o site exibe quatro características do animal pesquisado. Então, o Vini fez a pesquisa do leão, clicou no botão pesquisar e agora vamos encontrar alguns resultados desta pesquisa, quatro características.

[00:17] Então, vou colocar aqui, características = self.browser, vamos pegar estas características, e aqui tem um ponto interessante. Para conseguirmos buscar estas características, nós vamos utilizar um find_elements no plural, por quê? Porque vamos precisar contar quantas características nós temos, nós precisamos exibir mais de três características, para dar quatro características.

[00:53] Então, aqui eu vou usar o find_elements no plural, não no singular. find_elements_by_css_selector. O nome do css que eu vou atribuir vai ser o result-description.

[01:13] Salvei. Embaixo, eu vou fazer a minha assertação. Então, self.assertGreater, ou seja, se ele for maior que a quantidade que eu tenho de resultados, as minhas características, então len(características) ele vai contar quantas características que tenho. É maior que três? Se ele for maior que três nós estamos aprovados neste teste.

[01:39] “Command + J”, executando aqui mais uma vez, e falhou. Zero não é maior que três. Óbvio. Nós não colocamos na nossa página index.html esta nossa div. Vamos colocar.

[01:53] Então vou colocar uma div só, e vou colocar uma classe para ela. class=“result-description”. Coloquei uma. Vou executar o teste de novo, só para vermos se estamos no caminho certo. Um não é maior que três. Então vamos copiar a linha

`. Então, “Shift + Option” para baixo e vamos copiar três vezes, ou “Ctrl + Shift” para baixo nós copiamos. Portanto, nós temos quatro aqui.
[02:30] Executando mais uma vez. Maravilha. Ficou legal, nós passamos neste nosso teste funcional, só que se observarmos, nós passamos este resultado sem nada, nós não atribuímos nenhum valor para estes resultados e seria importante se conseguíssemos exibir, de fato, qual é o resultado deste nosso teste, quais são as características deste animal que foi pesquisado, e é isso que vamos começar a ver na sequência.

[03:01] Se pararmos para pensar nas características, é necessário que a nossa view busque de algum modelo estes dados, e a nossa view renderize estes dados pesquisados, passe estes dados por contextos para um determinado template e é isso que vamos fazer na sequência.

### Buscando por id

Uma pessoa escreveu o seguinte teste:

        # Ele vê um campo para pesquisar animais pelo nome.
        
        buscar_animal_input = self.browser.find_element_by_id('buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão, urso...')

Observando o teste acima, podemos ver que a busca do input não está vinculada ao find_element_by_css_selector e sim pelo find_element_by_id.

Sabendo disso, podemos afirmar que:

a) O input não será encontrado, já que o código certo deveria ser:

        self.browser.find_element_by_id('input#buscar-animal')

- _O input será encontrado com o código self.browser.find_element_by_id('buscar-animal'), pois ao realizar a busca através do find_element_by_id, devemos informar apenas o ID do elemento buscado._

b) Um erro será exibido informando que o input não foi encontrado, mesmo que no template exista um input com esse ID.
- _Caso o template tenha esse input com esse ID, ao executar o teste o input será encontrado._

c) **Alternativa correta:** Buscar pelo ID é mais segura, já que a classe do css pode mudar.
- _Alternativa correta! Certo! Ao realizar a busca pelo ID, temos a liberdade de alterar as classes do CSS sem impactar nosso código._

### O que aprendemos?

**Nesta aula:**
- Criamos uma pasta e o template chamado index.html;
- Testamos se o campo de busca estava presente na index;
- Vimos como simular a digitação de um usuário do sistema em um cenário de teste.

**Na próxima aula:**
Vamos aprender como testar a view, o model e garantir que nossa busca possua um comportamento esperado!

## 05. Teste de unidade na view e model
### View teste

1. Em test_views.py:

        from django.test import TestCase, RequestFactory
        from django.db.models.query import QuerySet

        class IndexViewTestCase(TestCase):
            def setUp(self):
                self.factory = RequestFactory()
            
            def test_index_view_retorna_retorna_caracteristicas_animal(self):
                response = self.client.get('/',
                    {'caracteristicas':'resultado'}
                )
                self.assertIs(type(response.context['caracteristicas']),QuerySet)

---

[00:00] A forma que passamos o último teste não ficou tão legal. Nós colocamos as quatro características sem nada aqui, e o que queremos fazer? Nós queremos, de fato, pegar estas características que estão no banco de dados, renderizar, colocar isto em um contexto e renderizar isto em uma página, para vermos, de fato, estas características.

[00:20] E é isso que nós vamos fazer agora. Só que para realizar isto, precisamos garantir que a nossa view seja configurada corretamente, que o nosso modelo esteja correto e que nossa página seja renderizada de forma correta também.

[00:35] Para garantirmos cada etapa, vamos criar testes de unidades para cada uma delas. Para começar, vamos criar um teste para a nossa view. O que a nossa view precisa fazer? Ela precisa pegar o contexto da resposta e colocar este contexto na resposta também, este nosso QuerySet, quais são as características deste animal? Então pega as características e exibe para nós. É isso que vamos fazer agora.

[00:59] Vou fechar a minha index.html e o meu tests.py e vamos começar agora um teste relacionado para validar a nossa view. Então, nós temos o teste de URL, e vou criar mais um arquivo que vou chamar de test_views.py. Neste teste, nós vamos utilizar do django.test as duas classes que já estamos acostumados que é o nosso TestCase para o nosso teste de unidade e o RequestFactory.

[01:37] Deixa eu fechar ali do lado só para ficar mais fácil de vermos. Nós vamos precisar também de um QuerySet para verificarmos se, de fato, estas informações estão vindo lá do ORM do Django. Então vou colocar aqui from django.db.models.query import QuerySet .

[02:07] O que vamos fazer? Vamos criar uma classe para testarmos a nossa index. class IndexViewTestCase(TestCase), e vamos aqui começar a escrever a nossa classe. Primeira coisa, nós temos um método setUp para começar este nosso teste de unidade. Vamos passar a instância como argumento e pegar a instância do RequestFacotry aqui. Então: self.factory = RequestFactory, a instância dele.

[02:53] Bom, nós já temos a instância do RequestFactory, o que nós vamos precisar fazer agora é o seguinte: eu preciso criar um teste que verifique se a minha view, se a minha IndexView está retornando as características do animal. Vou criar aqui um método que eu vou chamar de test_index_view_retorna_caracteristicas_do_animal. Como parâmetro nós vamos passar a instância, e agora vamos começar a escrever o nosso teste.

[03:44] Então, colocando a docstring só para mantermos o nosso código organizado. Então é um ““teste que verifica se a index retorna as características do animal pesquisado””. Temos aqui o nosso teste, temos aqui a documentação do nosso teste.

[04:17] Primeira coisa que vamos fazer: temos que entender que quando enviamos uma solicitação e esperamos algo por contexto nesta nossa resposta, nós vamos utilizar outra propriedade no lugar do RequestFactory, que vai ser o SelfClient, ele é um tipo de navegador fictício que enviamos as solicitações para a URL e temos acesso ao response content desta nossa requisição, para nós termos certeza que a nossa view está construindo a resposta correta.

[04:48] Então, eu vou criar aqui o response = self.client.get e o nosso path vai ser o path na raiz da nossa aplicação. Então, entre aspas simples eu coloquei a barra, e agora vamos precisar devolver um determinado contexto para esta nossa requisição.

[05:18] Então vamos dar dois “Enter” só para ficar certo e vou colocar aqui. Ele vai devolver em um dicionário, eu vou colocar o nome que vai ser ‘características’: e eu vou passar o resultado destas características, então eu vou colocar aqui ’resultado’.

[05:48] Além disto, eu vou precisar criar um teste para verificar se o tipo deste nosso resultado é uma QuerySet, então self.assertIs(type(response.context[‘características’]), QuerySet). Antes de fechar, queremos ver se isto é um QuerySet.

[06:49] Executando este nosso teste, vamos ver. Limpei aqui. Executando um teste, deu um erro no teste de unidade, já vamos encontrar. O teste verifica se a index retorna as características do animal pesquisado. Vamos ver o nosso teste então. Deu uma mensagem KeyError, observe, erro na chave, já que não existe este contexto de características.

[07:25] Nós temos aqui um KeyError nas características. Não existe este contexto ainda, é necessário criar isto. Então, vamos criar. O que eu vou fazer? Eu vou criar do jeito mais simples possível para o nosso teste ser aprovado até chegarmos na nossa próxima etapa.

[07:40] Então, eu vou abrir lá da minha “animais > view.py”, preciso passar um contexto, então vou colocar aqui: context = vou passar aqui os animais que queremos, as características, em string, ’caracteristicas’: None . E, para finalizar, nós já temos aqui, estamos renderizando esta página index, nós vamos passar também o context.

[08:25] Salvando. Executando mais uma vez, vamos ver. Tivemos um erro agora muito interessante. Ele disse assim: a classe ‘NoneType’ não é QuerySet, é isto que este erro está dizendo. Onde nós caímos neste erro? Observa: ele dá até a linha. Linha 14 lá do nosso test_views.py. A linha 14 do nosso test_views.py diz assim: isto aqui vai estar certo se estas características elas forem do tipo QuerySet e elas não são.

[09:00] O que isto significa? Significa que nós precisamos definir o que é um animal, e quais são estas características do animal. Vamos fazer isto no próximo vídeo?

### Model teste

1. Em test_models.py:

        from django.test import TestCase, RequestFactory
        from animais.models import Animal

        class AnimalModelTestCase(TestCase):
            def setUp(self):
                self.animal = Animal.objects.create(
                    nome_animal = 'Leão',
                    predador = 'Sim',
                    venenoso = 'Não',
                    domestico = 'Não'
                )
            def test_animal_cadastrado_com_caracteristicas(self):
                self.assertEqual(self.animal.nome_animal,'Leão')

---

[00:00] Assim que executamos o nosso teste, observe que nós temos uma coisa interessante. NoneType não é um tipo QuerySet, vamos torná-lo um. Como? Vou colocar um código mais simples possível, vou dizer, por exemplo, que Animal.objects.all, que é a classe que nós vamos criar, nosso modelo que vamos criar.

[00:24] Executamos aqui. Nós temos algum erro, vamos ver. Ele não achou o css. Ele falou que Animal não está definido. Bom, vamos definir. De onde vai vir Animal? Do nosso modelo. Então from animais.model import Animal. Vou executar mais uma vez e já temos um erro. Nem executou o nosso código e ele falou assim: eu não posso importar Animal de animais.model, porque nós não criamos lá no nosso modelo este Animal, e é o que vamos precisar fazer agora.

[01:01] Então, para solucionar este problema, eu vou vir aqui no meu app de animais, vou vir aqui em models.py e vou criar do jeito mais básico vou dizer assim: Animal = None. Salvei. Revisando tudo. Executando mais uma vez, vamos ver. O erro do css aqui, um pouco mais para cima: NoneType não possui o atributo objects, e faz sentido. Nós queremos que o nosso animal tenha os atributos, e quer que ele seja um objeto. Então, vamos precisar criar o nosso modelo.

[01:51] Então, eu vou criar um modelo no lugar deste Animal = None, vou criar uma classe que eu vou chamar de Animal(models.Model): e a minha classe simplesmente não faz nada ainda. Só estou importando. Vamos executar mais uma vez para visualizarmos o que acontece?

[02:14] Executei o meu teste e temos um erro operacional agora. Ele fala assim: “no such table animais_animal”. O que o Django está tentando nos dizer com este erro? Ele está tentando dizer que no nosso banco de dados não existe nenhuma tabela de animal, porque nós ainda não fizemos a migração do nosso modelo de animal.

[02:36] E você deve ter percebido que, em nenhum momento do nosso desenvolvimento, nós executamos manage.py migrate ou até mesmo o runserver. Nós executamos uma vez para ver, mas não executamos o migrate, e quando executamos o runserver aquela vez, nós vimos que existiam migrações pendentes da estrutura do Django.

[02:56] Então, o que acontece? Nós podemos pedir para o Django gerar para nós a migração, mas, para realizar estes testes não é necessário nem que eu realize o migrate por enquanto. Então, o que eu vou fazer? Vou realizar apenas o makemigrations e com base nele, o Django vai utilizar para realizar os nossos testes, quando ele cria o nosso banco de dados.

[03:20] Então, python manage.py makemigrations, dou um “Enter” e ele gerou a nossa migração, criou o nosso modelo de Animal. Executando o teste mais uma vez, vamos ver, dois testes passaram, os três testes passaram. Está OK. Nós passamos no nosso teste, então lá no view.py ele viu que o Animal.objects.all é um QuerySet, só que, quem garante mesmo que nós estamos recebendo os dados do nosso modelo ou que as nossas características estão vindo de lá?

[03:59] Precisamos criar um teste para garantir que as características do animal pesquisado é esta: o animal ele tem um nome, ele é um tipo predador? Sim ou não. Ele é do tipo venenoso? Ele é doméstico? E, para isso, podemos criar um teste para o nosso modelo. Então, é o que vamos fazer agora.

[04:18] Vou fechar estas abas aqui, e vou criar lá em “animais > tests”, vou criar “test_models.py”. Neste teste, nós vamos ter, vou até copiar de “test_views.py”, vamos roubar um pouco. Vamos ter do django.test o nosso TestCase e o RequestFactory.

[04:45] Além destes dois, para testarmos o nosso modelo é importante que se tenha quem? O próprio modelo, então eu vou trazer também o nosso modelo: from animais.model import Animal. Agora vamos criar a nossa classe para testar o nosso modelo.

[05:05] class AnimalModelTestCase, por exemplo, e vou passar o TestCase. Quando nós iniciamos o nosso teste de modelo, sabe o que podemos fazer? Nós podemos criar uma instância deste animal, como os atributos que esperamos para esta nossa classe.

[05:34] Então, vou criar aqui uma função que eu vou chamar de setUp, vamos passa a instância que estivermos utilizando, o self, e abaixo eu vou fazer assim: self.animal = Animal.objects.create(), e nos parêntesis eu vou passar as características deste animal que eu quero criar.

[06:07] Mas, Guilherme, este animal que você está criando neste teste não vai para o seu banco de dados em produção? Não. Observa que em nenhum momento nós fizemos a migração para o nosso banco de dados, nós realizamos o makemigration e através deste makemigration, quando nós subimos os nossos testes, ele vai utilizar apenas estes dados para realizar o nosso teste, criando o cenário ideal para realizar o nosso teste.

[06:36] O animal vai ter um nome, vou chamar de nome_animal = ‘Leão’, além do nome do animal, outra característica, eu esqueci da vírgula após leão. O animal, depois queremos saber se ele é um predador, então predador = ‘Sim’, o leão é um predador. Vou deixar como string, não vou passar isto para booleano para ficar mais simples ainda a nossa explicação. Além disso, queremos saber se ele é venenoso, venenoso =’Não’, o leão não é um animal venenoso, então vou colocar aqui Não. Eu acho, pelo menos, depois podemos dar uma pesquisada nisso aí. E, para finalizar, se ele é um animal doméstico. domestico = ‘Não’. Não é também. Uma pena, mas não é.

[07:35] Temos a nossa instância de animal e agora nós temos características para este animal, que são as características que queremos exibir lá nosso teste. O que eu vou fazer? Vou criar outro teste, outra função para testar se, de fato, este animal existe.

[07:55] Então vou colocar assim: test_animal_cadastrado_com_caracteristicas e vou passar como parâmetros, self, e dentro, para deixar bem bonito, colocar aqui a nossa docstring então: “““Teste que verifica se o animal está cadastrado com suas respectivas características”””.

[08:48] Vou tirar este pass, nós não precisamos dele. Vamos lá, o que eu vou fazer? Vou usar um assertEqual, então self.assertEqual e vou pegar quem? A instância que tivermos, que estamos utilizando: self.animal.nome, por exemplo. Vou colocar uma vírgula. Peguei o nome do animal que eu tenho a instância e vou falar se o nome dele, de fato, é ’Leão’, que é o animal que geramos ali em cima.

[09:29] Vou realizar este teste, abrindo aqui o nosso terminal, realizando o teste do modelo. E um teste de unidade quebrou. Vamos ver. Olha lá, que interessante. Isto é muito bacana. Ele disse assim: Animal está com um keyword não esperado, que é o keyword nome_animal. O que isto significa? Significa que, no nosso modelo, nós temos uma palavra-chave que não estamos esperando, que é o nome do animal. Por quê?

[10:02] Se observarmos o nosso modelo, vou abrir aqui o “models.py”. O nosso modelo não tem nenhuma característica, nenhum atributo, melhor dizendo. Então, o que vamos fazer? Vamos criar os atributos deste modelo. Vou criar aqui o Animal, ele vai ter o nome, eu vou chamar de nome_do_animal, acho que vai ficar mais claro também.

[10:20] Deixa eu mudar no nosso teste que vai ficar melhor também. Vou deixar só nome_animal mesmo. Nós temos outra característica que é o predador, nós temos outra característica que é se ele é venenoso e, para finalizar, deixa eu só lembrar qual a outra, domestico.

[10:47] Nós temos estas características, então vamos lá: de models.CharField eu quero que o Animal tenha no máximo, max_lenght=20, acho que não vai ter um nome de animal. Animal não é o nome científico, é só o nome dele normal. Então, vou colar aqui nas outras características, só que no predador e estes outros nomes eu vou usar 5 de espaço, nem isso. Não vou usar por enquanto booleano para deixar mais rápido o nosso curso, para conseguirmos ir mais longe.

[11:28] Coloquei estas características. Preciso dizer também qual é a forma que eu vou representar este animal, qual a forma que eu vou mostrar este animal via texto. Então eu vou criar aqui uma função, __str__(self), e aqui dentro eu vou colocar um return self.nome_animal.

[11:58] Criamos. Aqui, os atributos do animal. O que eu preciso fazer para que estes atributos entrem no meu teste de modelo? Eu preciso rodar mais um vez o makemigrations é isto que eu vou fazer.

[12:14] Rodando o makemigrations mais uma vez ele perguntou: se você tiver algum animal e você quer colocar alguma característica, ou prover um dado default para ele. Vou colocar que sim, opção 1, e vou colocar de dado default um n/a. Então, se caso nós tivéssemos dado, já vou colocar isto como propriedade default. Dou “Enter”.

[12:34] Ele vai perguntar a mesma coisa, vou selecionar a opção 1, vou colocar entre string, n/a e vou fazer isto para os outros campos também. Seleciono a opção 1, e para finalizar, a opção 1 também para ver se ele é um animal doméstico. Se não tiver nada, nós vamos definir n/a.

[12:58] Nós provemos as características deste nosso animal. Vamos rodar o teste mais uma vez? Então, “Command + J”, python manage.py test e um teste nosso quebrou, vamos ver o que aconteceu. E ele falou o seguinte: Animal não tem o atributo nome, porque eu passei aqui o nome errado. Não é atributo nome é nome_animal, agora sim.

[13:29] Vamos rodar mais uma vez. Sucesso. O que isto significa? Significa que é possível hoje, com a estrutura que estamos, criar um modelo de animal com estas características. Isto ficou bem legal.

### Testando a busca

[00:00] Se nós observarmos o nosso teste que faz a pesquisa para ver as características do animal, nós fizemos aqui uma trapaça, na verdade. Nós colocamos aqui quatro div com a classe ”result-description” para sermos aprovados naquele teste. Só que vamos deixar a nossa funcionalidade principal da nossa aplicação que é a busca, vamos criar um teste para garantir que ela vai ter o comportamento que esperamos.

[00:28] Então, o que eu vou fazer? Lá no nosso teste de unidade, lá no nosso tests_view.py, nós temos um teste que verifica se a index retorna as características do animal pesquisado, e nós não demos continuidade neste nosso teste. Então, o que vamos fazer? Eu vou colocar aqui, eu vou criar um teste, para nós, de fato, verificarmos se um determinado animal pesquisado é exibido as características: nome, se ele é predador, venenoso e assim por diante.

[00:56] A primeira coisa que eu vou fazer vai ser criar uma instância de um animal. Para isto, eu preciso trazer aqui, lá do meu animais.models import Animal. E eu vou criar lá onde fazemos a instância do RequestFactory, vou criar mais uma instância, que eu vou chamar de self.animal, colocar a nossa classe Animal.objects.create, e criar o nosso animal.

[01:31] Então o animal tem um nome, nome_animal, eu vou criar um animal, vocês podem escolher o animal que vocês querem. Eu vou criar o animal calopsita, por exemplo. Eu vou colocar se ele é um predador = ’Não’, se ele é um animal venenoso, venenoso = ‘Não’ também.

[01:57] Não é um animal venenoso também, coitado, tão bonito. E domestico = ‘Sim’. Na casa dos meus pais tem uma calopsita que anda pela casa mesmo, parece um cachorro. Anda, voa, se chama ele vem, é muito legal. Então, ele é um animal doméstico.

[02:16] O que eu vou fazer agora? Vamos mudar as nossas características do animal pesquisado. Então, observa que temos aqui um ’caracteristicas’:’resultado’. Não é o que queremos. O que eu quero é que, de alguma forma, aquele nosso input da nossa index, eu consiga pegar o conteúdo que está nele. Para isto, eu vou dar um nome para ele.

[02:35] Então, name = ‘buscar’. Daí, o que eu vou fazer? Lá no meu teste da view eu vou falar assim: se ’buscar’ tiver o conteúdo ’calopsita’, eu quero, de alguma forma, visualizar este meu conteúdo.

[02:51] Então, o que fizemos? Nós tínhamos aqui um self.assertIs, se o tipo deste context característico for um QuerySet, este é nosso primeiro teste, se ele for um QuerySet ele está aprovado. Eu posso colocar mais uma característica. E, para garantir que este nosso teste vai trabalhar somente com esta instância, eu vou pegar este animal pesquisado então, por exemplo, vou fazer assim: característica_animal_pesquisado = response, porque eu quero pegar o conteúdo desta resposta .context [‘caracteristicas’].

[03:44] E olha só que interessante. Eu peguei o contexto de características, deste animal que foi pesquisado. O que eu posso fazer agora, é verificar, por exemplo, se o nome deste animal é calopsita. Então, self.assertEqual(característica_animal_pesquisado[0].nome_animal), quero verificar se isso, se de fato, o animal que eu pesquisei, se ele é, entre aspas, ‘calopsita’.

[04:32] Então, desta forma, nós criamos uma instância do animal, conseguimos pegar este nome ’calopsita’ lá do nosso input de busca, e aqui nós vamos verificar se, de fato, esta característica de animal pesquisado no índice zero, que é o nome do animal, se for calopsita nosso teste vai ser aprovado.

[04:50] Executando aqui o nosso teste. Nosso teste foi aprovado, o que precisamos fazer agora é alterar, configurar a nossa view para que ele, de fato, mande este nosso animal, as características do animal que qualquer pessoa pesquisar, digitar, ele seja exibido na tela. Isto que vamos fazer na sequência.

### Teste de unidade e funcional

Durante o curso, somos guiados por uma série de testes para desenvolver nossa aplicação. Dentre eles, os testes de unidade e funcional.

Sabendo disso, podemos afirmar que:

a) Um teste funcional geralmente é pequeno, executado em microsegundos e focado nas preocupações do desenvolvedor.

b) **Alternativa correta:** Tanto os testes funcionais como os testes de unidade, são importantes para uma aplicação ou software.
- _Alternativa correta! Certo! Ambos tem o seu valor, seja para garantir as necessidades do desenvolvedor ou desenvolvedora, ou, garantir que a soma total dos dados e a lógica do aplicativo corresponde a funcionalidade prometida ao usuário._

c) **Alternativa correta:** Um teste de unidade geralmente é pequeno, executado em microsegundos e focado nas preocupações do desenvolvedor.
- _Alternativa correta! Certo! Os testes de unidade geralmente validam uma única parte do sistema._

### O que aprendemos?

**Nesta aula:**
- Entendemos como testar a view e o model de um app;
- Criamos um cenário para testar a busca de um determinado animal.

**Na próxima aula:**
Vamos alterar a view para realizar a busca, carregar alguns animais em nossa base de dados e alterar o frontend da aplicação!

## 06. Finalizando o projeto
### Alterando a view

[00:00] Pessoal, para nós fecharmos o nosso treinamento de TDD, o que acontece? O site exibe quatro características do animal pesquisado, lá do nosso setup. O que nós fizemos lá na nossa index.html? Nós colocamos quatro div e manteve este conteúdo aqui e não está legal. Por quê? Da forma que está nós não estamos exibindo conteúdo, não tem nada: o nome do animal, se ele é venenoso, se ele é predador, e nós precisamos alterar isto também.

[00:28] O que fizemos no vídeo anterior? Nós criamos um teste para busca do animal e ele funcionou, porém, nós precisamos exibir aqui o ”result-description” com o conteúdo, de fato, do animal pesquisado, com as características do animal pesquisado. Então, para isso, o que vamos fazer? Nós vamos alterar a nossa view.

[00:47] Só que antes, só para deixar legal, nós criamos uma instância de um determinado animal, de um calopsita, para realizar o teste da view. O que eu quero fazer agora é criar uma instância para realizar um teste aqui. Então vou fazer aqui: self.animal =. Preciso importar o animal aqui também. from animais.models import Animal e aqui vai ser self.animal = Animal.objects.create.

[01:25] Aqui nós vamos colocar o nome_animal e vou chamar esse animal de leão, que é o animal que o Vini pesquisou na nossa história do usuário, vou falar que ele é um predador, ’Sim’, ele é um predador, se ele é venenoso, venenoso = ‘Não’, o leão não é um animal venenoso, e infelizmente ele não é um animal doméstico.domestico, vou falar aqui que ’Não’. Já pensou um leão doméstico? Ia ser bizarro.

[01:59] Criei a instância deste meu animal. O que eu vou fazer agora? Lá na minha view eu vou preparar um contexto para este nosso animal pesquisado, então eu vou dizer assim: eu tenho um animal que eu pesquisei, que o Vini fez a pesquisa aqui, que é o leão, e ele vai exibir, de fato, as características deste animal - que vai pegar o conteúdo deste animal.

[02:21] Então, vamos parar de burlar a nossa index utilizando o ”result-description” sem nada, e vamos colocar de fato as características deste animal.

[02:29] Primeira coisa que vamos fazer, olha só, nós passamos por contexto alguma coisa. Se eu não pesquisei nenhum animal, não vai exibir nada por contexto, então eu vou colocar aqui um None.

[02:41] Então, temos aqui um contexto sem nada, com características vazias, e vou verificar: se a minha busca, se o meu buscar, que é o meu input, observe que nós colocamos aqui no nosso input de busca o name = ‘buscar’. Eu vou verificar: se eu tiver alguma coisa dentro deste buscar, então if ‘buscar’ in request.GET: tudo maiúsculo, eu quero de fato realizar a busca de um animal.

[03:10] Então, primeira coisa: vamos fazer bem passo a passo. Eu vou pegar todos os animais. animais = Animal.objects.all. Depois, eu vou querer pegar detalhes do animal pesquisado, então animal_pesquisado =, ele vai ser o animal que está vindo desta requisição, então request.GET[‘buscar’].

[03:39] Então, quando eu tiver um animal para buscar, vai estar buscar igual a alguma coisa, leão, por exemplo. Então, nós queremos pegar aquele leão, o nome que vai ser pesquisado e colocar aqui no animal_pesquisado.

[03:50] Depois, nós precisamos buscar as características deste animal. Então, vou escrever caracteristicas = no plural, então vou colocar aqui todos os animais: animais.filter, que eu quero filtrar os animais através do nome. Então eu vou colocar nome_animal e aqui tem um ponto interessante: nós podemos pesquisar, nós temos, por exemplo, cavalo e cavalo-marinho na nossa base de dados.

[04:21] Eu quero que só o cavalo, só o que a pessoa digitou, eu quero exibir todos os cavalos que temos na aplicação, então vai exibir cavalo-marinho, cavalo e todos os detalhes destes animais e características e eu vou decidir na minha aplicação para exibir todos os animais. Você pode dar uma olhada, eu vou deixar um link depois deste vídeo com um post ensinando como que trabalhamos com os filtros com o ORM do Django.

[04:54] Então, eu vou criar um filtro para exibir tudo que contenha este animal pesquisado. Então se tiver cavalo-marinho e cavalo eu vou exibir os dois. E fazemos isso como? Coloco dois underlines depois do nome_animal e coloco icontains, então se ele contém algo, se ele achar algo na nossa base de dados com o animal_pesquisado ele vai realizar este filtro para nós.

[05:24] Para finalizar, a única coisa que fazemos é passar para o contexto, context, montar um outro contexto, onde eu tenho as caracteristicas, que ela vai ser baseada nas caracteristicas, e estas características que temos aqui do animal que nós já pesquisamos. Para finalizar, na nossa index.html, nós queremos exibir o nosso contexto, quer exibir estas características, pegar as características dos contextos e renderizar ela aqui.

[05:53] E nós vamos criar um for, que podemos ter mais de um animal, {% for característica in caracateristicas %}, o que eu quero fazer? Para deixar só indentado aqui, selecionei todas as quatro div, “Command + [só para arrastar para o lado, e já vou fechar o meuendfor, então{% endfor %}`.

[06:26] Aqui eu vou passar as características do animal abrindo duas chaves, vou fazer assim {{caracterstica.}}, e vou copiar este aqui, só para ganharmos um tempo. “Command +C”, vem aqui nos outros div, “Command +V”, “Command +V”, “Command +V” . Então, a primeira característica que temos é o nome_animal que eu quero exibir, a segunda, se ele é um predador, se ele é venenoso, e se ele é domestico. Salvei.

[07:06] Vamos executar o nosso teste. Maravilha! Executamos o nosso teste e nós passamos neste teste, o que eu vou fazer agora, no próximo vídeo, nós vamos, de fato, subir esta aplicação, realizar o migrate desta aplicação, criar uns animais só de exemplo na nossa base de dados e começar a pesquisar alguns animais para visualizar esta funcionalidade de fato na nossa aplicação.

### Preparando o ambiente

No próximo vídeo, vamos alterar a visualização do projeto, incluindo um css bem lindão e criar uma lista de animais no banco de dados. Para isso, clique [neste link]('https://github.com/alura-cursos/material_extra_tdd/archive/master.zip') para realizar o download dos materiais necessários para próxima aula.

Após o download realizado, vamos alterar?

### Realizando buscas

[00:00] Agora que finalizamos os nossos testes, vamos executar a nossa aplicação? Vou rodar aqui um python runserver pra visualizarmos a nossa aplicação rodando. Vou abrir aqui uma nova aba e acessar http://localhost:8000/, e temos aqui o nosso site. Se eu pesquisar, por exemplo, leão e dou aqui um pesquisar, nós temos uma mensagem de erro indicando que nós não temos esta tabela de animais_animal do nosso app de animais, a nossa tabela de animal.

[00:30] Faz muito sentido, porque em nenhum momento nós criamos os nossos dados no banco de dados, nós falamos: tem estes dados para serem criados com o makemigration, mas nós não migramos estes dados para a nossa base. Vamos fazer isto agora?

[00:44] Então, a primeira coisa que eu vou fazer, deixa eu minimizar a barra lateral para nós enxergarmos legal. Vou colocar aqui python manage.py migrate, ou seja, pega todas as migrações que você tem e aplica lá no banco de dados. Se executarmos mais uma vez, agora aquela mensagem indicando que nós tínhamos migrações pendentes não aparece e, quando atualizamos, nós não temos nada.

[01:07] Apareceu aqui: buscar = leão, só que ele não exibe nada. Por quê? Porque nós não temos nenhum animal na nossa base de dados de leão, e nenhum animal cadastrado. Como que nós podemos cadastrar? Nós podemos utilizar, por exemplo, o admin.py do Django, criar um novo registro de modelos aqui para o nosso admin, ou, eu deixei na atividade anterior a esse vídeo, um material extra do curso, e tem aqui um lista_animais.py.

[01:38] O que eu vou fazer? Dentro deste lista_animais.py tem uma lista com uma série de animais, com as características que nós estamos utilizando na nossa aplicação e o que acontece? Com base nestas características nós podemos visualizar, criar vários animais de forma rápida aqui na nossa aplicação.

[01:57] Então, o que eu vou fazer? Vou copiar este lista_animais.py aqui para o nosso projeto, então dei um “Ctrl + C” “Ctrl +V”, ou só arrastei, e observa, aqui nós temos uma lista de animais, então, tem um dicionário, o nome, urso, javali, búfalo, elefante, pato, girafa, ou seja, vários animais.

[02:13] E lá, se nós scrollarmos para o final, nós temos aqui preparando o nosso ambiente para conseguir criar estes animais na nossa base de dados. Fez a importação do modelo e falou: para cada animal que tiver desta lista define estas características, estes atributos e cria um animal e salva o animal na base de dados, e nós geramos estes animais. Vamos fazer isto agora?

[02:36] Então, parei meu servidor. “Ctrl + C”, o que eu vou fazer agora? Agora eu vou fazer o seguinte, eu vou rodar este script, então python lista_animais.py, quando eu dou um “Enter” observe que ele fala animais gerados. Então, vou subir meu servidor mais uma vez, e vamos acessar o nosso projeto.

[02:59] Então, se eu digitar aqui, por exemplo, deixa eu atualizar, deixar sem nada. Quando eu só atualizei, não coloquei nada, ele trouxe todos os animais para mim. Não é o que eu quero. O que eu quero é ver só o leão.

[03:09] Então, quando eu dou aqui um pesquisar, ele traz aqui dois animais: o leão e o leão marinho. Se eu digito aqui, por exemplo, cavalo, vamos ver o que ele fala. Ele traz aqui o cavalo marinho, então ele fala aqui: cavalo marinho e as três características. Só que se nós pararmos para pensar, nosso visual ficou bem feio. Nós testamos várias partes da nossa aplicação para esta funcionalidade passar, ser aprovada, só que o nosso visual está feio.

[03:30] Para nos ajudar nesta tarefa, a Juliana Negreiros, que é desenvolvedora aqui na Alura também, ela criou um front-end bem bonito para nós utilizarmos na nossa aplicação. Então, vamos colocar este front-end para funcionar? Primeira coisa que eu vou fazer: nós poderíamos utilizar o Bootstrap, qualquer outro assim, mas ela preferiu fazer na mão o css bem lindo.

[03:52] Então, dentro do nosso arquivo de setup eu vou criar um folder que eu vou chamar de static. Dentro deste arquivo eu vou copiar este arquivo style.css, vou lá na nossa pasta do nosso projeto, na pasta do nosso “tdd_busca_animal > setup > static” eu vou dar um “Ctrl +V” daquele nosso arquivo style.css, com todos os dados que precisamos.

[04:17] Se vamos utilizar o style.css, precisamos definir no nosso “settings.py” a rota principal deste nosso arquivo e onde está este static file, qual que é o diretório principal dele. Então vamos definir estas duas variáveis de instância aqui.

[04:40] Então, nós temos o STATIC_ROOT. Aqui nós precisamos importar, além do path, ,os para conseguir navegar entre as nossas páginas aqui. Então STATIC_ROOT = os.path.join e nós vamos utilizar do nosso diretório principal do BASE_DIR, vou passar aqui o nome do arquivo onde vai ser encontrado a raiz dos nossos arquivos estáticos, então ’static’.

[05:14] Defini STATIC_ROOT, vou definir agora também o STATICFILES_DIRS, todas as letras maiúsculas, dos diretórios dos nossos arquivos estáticos, e eu vou falar que ele está lá em os.path.join vai ser na base da nossa aplicação mesmo, no BASE_DIR, vou falar qual é o componente que vai ser responsável por manter todos os nossos arquivos estáticos, então é ’setup/static’. Estas duas configurações são as únicas necessárias para a nossa aplicação.

[05:57] Então, nós temos aqui um CSS muito maluco, muito bonito que Ju fez, o que vamos fazer? Agora nós precisamos alterar lá do nosso app de animais o nosso template, nossa index.html, vamos precisar alterar. Então vai precisar carregar o arquivo estático e utilizar esta classe que está usando. Só que para isso, a Ju já deixou um esquema para nós.

[06:18] Então, nós temos um arquivo que eu vou abrir com o VS Code, então eu tenho o meu arquivo do Busca Animal que está assim, e tem o “Busca Animal” que está com as características bem legais aqui do static. O que eu vou fazer? Vou copiar todo este conteúdo e vou colar no index.html, já utilizando as classes e tudo que ele precisa.

[06:39] Só uma alteração que eu vou fazer aqui: observa que o venenoso ficou aqui venenoso, e no final, no doméstico ele está aqui, eu estou usando a característica do venenoso e não é, é caracteristica.domestico. Agora sim está certo.

[06:56] Vamos dar uma olhada neste arquivo. Então, nós temos aqui os static, definimos este load static aqui, está carregando o ’style.css’ através do static e o resto nós estamos utilizando todas as classes lá do css para alterar, para manipular o nosso form.

[07:15] Então, nós temos aqui o nosso form de característica, onde pegamos o nome do animal e exibimos o nome do animal, se ele é predador exibindo se ele é predador, venenoso, venenoso e doméstico, nós alteramos aqui para doméstico.

[07:27] Agora, para eu utilizar os arquivos estáticos que eu incluí lá na minha aplicação, nós precisamos executar o collect static que vimos lá no nosso primeiro curso de Django. Então, vou rodar aqui python manage.py collectstatic. Dou um “Enter”. Agora, sim, e ele já fez a referência para todos os arquivos estáticos que precisamos.

[08:10] Agora, eu vou subir o meu servidor mais uma vez, vou acessar aquele meu site, quando eu atualizar: olha que bonito isto aqui! Ju, ficou muito bacana isto aqui! Os alunos vão agradecer bastante, e eu vou pesquisar. Olha só, nós tínhamos colocado a pesquisa como cavalo e ele mostrou cavalo marinho. É um predador? Não. É venenoso? Não. É doméstico? Não.

[08:30] Eu vou colocar aqui um gato, por exemplo, que todo mundo gosta de gato. Gato é um predador? Sim. Ele é venenoso? Não. Ele é doméstico? Sim. E o urso? Ele é predador? Sim. Ele é venenoso? Não? Ele é doméstico? Também não. E o nosso clássico, nossa pesquisa do leão, do Vini.

[08:46] O leão aparece dois: aparece o leão e o leão marinho, olha que legal. Então, o leão é um predador, ele não é venenoso e ele não é doméstico, uma pena, mas ele não é doméstico o leão. O leão marinho também é um predador, ele não é venenoso e também não é doméstico.

[09:00] Se eu não colocar nada e der um pesquisar ele listar todos os animais que temos na nossa base de dados que podemos exibir. Então tem a girafa e vários outros animais super legais também. O hamster é um animal doméstico. Então, eu espero que vocês tenham gostado e continue aí, antes de finalizar o curso para as próximas atividades.

### Próximo passo

Testamos e criamos uma aplicação que busca animais em uma base de dados e isso ficou bem legal. Para isso usamos diversas ferramentas e módulos como: LiveServerTestCase, Selenium, webdriver, TestCase, reverse, RequestFactory, entre outras.

Porém, além das ferramentas, devemos ter em mente que:

a) Devemos estudar apenas as ferramentas e módulos de teste.

b) **Alternativa correta:** Existem outros tipos de testes com outros objetivos além do funcional e de unidade.
- _Alternativa correta! Certo! Existem outros tipos de testes, cada um com um objetivo diferente._

c) **Alternativa correta:** Conhecer o sistema que será desenvolvido através dos testes, entendendo os fluxos e regras, fará grande diferença na criação dos testes.
- _Alternativa correta! Certo! Entender o objetivo do sistema é essencial para o sucesso dos testes._

### O que aprendemos?

Nesta aula:
Alteramos a view para exibir os resultados da busca;

Incluímos um css, executamos o collectstatic e alteramos o arquivo index.html para deixar o visual da aplicação bem lindão;

Projeto final do curso
Aqui você pode baixar o zip da aula 06 ou acessar os arquivos no [Github]('https://github.com/alura-cursos/django_tdd/tree/aula_6')!

### Conclusão

[00:00] Se você chegou até aqui, parabéns! Você está finalizando mais um treinamento da Alura. Neste treinamento, o que fizemos? Nós criamos um projeto em Django e escreveu uma história de usuário, onde um determinado usuário pesquisava por um animal e ele encontrava um animal, encontrava características daquele animal.

[00:18] Com base nesta história, nós desenvolvemos os nossos testes e começamos com o teste funcional, depois passamos para o teste de unidade nos nossos modelos.

[00:29] Deixa eu abrir aqui em animais: testes com nossos modelos, com nossas URLs, com nossa view para garantir que esta funcionalidade de busca seria atendida. Isto ficou muito bacana.

[00:39] No final, nós ficamos com essa aplicação, onde nós conseguimos pesquisar um determinado animal e exibir as quatro características sobre ele. Isto ficou muito legal. Só que, um ponto que eu quero deixar aqui para vocês é assim: não é apenas a base de testes deste curso que vai te fazer um grande tester, uma grande QA ou algo deste tipo, não. Continue estudando testes, continue buscando conteúdos a respeito de testes.

[01:05] Nós pensamos em criar este conteúdo de forma mais lúdica e mais legal possível, mas isto é muito importante: a sua prática de teste vai fazer você escrever cada vez mais testes melhores e, cada vez mais, garantir que o seu software entregue aquilo que ele precisa entregar, tenha o comportamento que precisa.

[01:24] Então, quero deixar meu forte abraço, continue estudando teste, continue escrevendo linhas de código a respeito de testes, abre o GitHub, digita lá TDD com Python e começa a copiar vários códigos, escrever bastante para deixar esta parte motora bem legal e você entender outras funcionalidades relacionadas a testes com Django ou com outras linguagens também. Forte abraço e nos vemos no próximo curso.
