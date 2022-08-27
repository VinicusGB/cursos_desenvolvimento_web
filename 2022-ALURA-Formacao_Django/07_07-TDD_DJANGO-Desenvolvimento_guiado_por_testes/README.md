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
### Faça como eu fiz
### O que aprendemos?
## 02. Requisitos, testes funcionais e unitários
### Projeto da aula anterior
### LiveServerTest e Selenium
### Configurando o navegador
### URL do servidor e teste falha
### Banco de dados
### Para saber mais: História do TDD
### Faça como eu fiz
### O que aprendemos?
## 03. RequestFactory e templates
### Projeto da aula anterior
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
