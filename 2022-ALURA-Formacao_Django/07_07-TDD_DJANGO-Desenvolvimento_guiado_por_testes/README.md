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
### ATUALIZAÇÃO
### Criando o app
### Testando URLs
### RequestFactory
### Análise do código
### Faça como eu fiz
### O que aprendemos?
## 04. Template e cenário de teste
### Projeto da aula anterior
### Template
### Testando campo de busca
### Send keys
### AssertGreater
### Buscando por id
### Faça como eu fiz
### O que aprendemos?
## 05. Teste de unidade na view e model
### Projeto da aula anterior
### View teste
### Model teste
### Testando a busca
### Teste de unidade e funcional
### Faça como eu fiz
### O que aprendemos?
## 06. Finalizando o projeto
### Projeto da aula anterior
### Alterando a view
### Preparando o ambiente
### Realizando buscas
### Próximo passo
### Faça como eu fiz
### O que aprendemos?
### Parabéns!
### Conclusão
