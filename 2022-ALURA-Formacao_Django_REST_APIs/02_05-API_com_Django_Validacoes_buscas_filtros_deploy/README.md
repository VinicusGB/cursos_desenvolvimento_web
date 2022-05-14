# 2. API com Django 3: Validações, buscas, filtros e deploy - 8h
**Disponível:** [ALURA]('https://cursos.alura.com.br/course/api-django-3-validacoes-buscas-filtros-deploy') \
**Professor:** Guilherme Lima \
**Conteúdo:**
- Faça esse curso de Python web e:
- Aprenda como validar os campos de sua API, utilizando Django Rest Framework
- Saiba como incluir filtros, buscas e ordenação em seus endpoints
- Crie uma boa arquitetura em seus projetos Django Rest API
- Coloque sua API no ar realizando o deploy
- Descubra como criar suas próprias APIs com Django

## 1. Iniciando o projeto Ver primeiro vídeo
### Introdução

[00:00] Olá, meu nome é Guilherme Lima e eu serei o seu instrutor nesse treinamento de API com Django 3, validações, buscas, filtros e deploy.

[00:08] Nesse treinamento, o que vamos aprender? Vamos aprender a incluir validações nos nossos modelos, nos nossos serializers, como trabalhar com mensagens de erro, vamos incluir nos nossos endpoints, paginação, ordenação, buscas, filtros e o mais legal de tudo, vamos colocar a nossa API no ar, vamos realizar o deploy da nossa API.

[00:29] Fazendo esse curso, vamos desenvolver o seguinte projeto. Observe que estou rodando esse projeto no meu escopo local. Então, eu tenho aqui a minha lista de clientes e os meus campos com as devidas validações, nome, email, CPF, RG, celular e uma flag para indicar se esse cliente é ativo ou não na minha API.

[00:46] Quando eu colocar minha API no ar e ligar e clicar para listar esses e- mails é necessário que eu faça uma autenticação. Então vou colocar meu nome, minha senha e quando dou um “enter”, observem que vamos disponibilizar os dados da nossa API com todos os filtros que citei.

[01:00] Então vamos conseguir filtrar só os clientes que estão ativos, só os clientes que não estão ativos, vai conseguir ordenar através do nome de forma ascendente ou descendente e pesquisar os clientes através do campo nome ou do campo CPF.

[01:15] Quais são os pré-requisitos para realizar esse treinamento? É importante que você tenha familiaridade com a linguagem de programação “Python” e já tenha trabalhado com projeto de Django Rest Framework, que você saiba os fundamentos de uma aplicação criada com esse framework, saiba o que é um “Serializer”, o que é um “Modelo”, o que é um “View”, o que é um “View7”, o que é um “Default Router”. Isso são requisitos importantes para realizarmos esse treinamAento.

[01:41] E para quem é esse curso? Esse curso é recomendado para todas as pessoas que querem aperfeiçoar os seus conhecimentos nesse framework, incluindo validações, trabalhando com mensagens de erro, ou seja, aprendendo bastante coisa legal. Porém, se você já é um profissional que trabalha nessa área e já trabalhando com Django Rest Frame e há muitos anos já está inserido no mercado, talvez esse curso não seja recomendado para você.

[02:10] Bom, sabendo de tudo isso, vamos começar?!

### Preparando o ambiente

Olá!
É muito bom receber você neste curso de Django Rest API.

Espero que seja uma experiência de aprendizado incrível e que possamos vencer todos os desafios juntos. Neste curso, vamos aprofundar nosso conhecimento utilizando o Django, criando um API junto a biblioteca do Django Rest Framework.

Este curso, apesar de ser o segundo curso de Django Rest Framework, não é uma continuação do projeto desenvolvido no curso anterior. Porém, é importante e recomendado que você tenha uma base de conhecimento passado no curso anterior.

Divisão das aulas
Aula	O que vamos aprender nesta aula?
Iniciando o projeto	Vamos carregar o projeto e incluir validações no modelo
Validações no Serializer	Vamos aplicar diferentes tipos de validações no Serializer
Importando validações	Vamos importar uma lib de validação e utilizar expressões regulares
Paginação, Ordenação, Buscas e Filtro	Vamos adicionar na API busca, filtros, ordenação e paginação
Deploy	Vamos publicar a API e incluindo autenticação
Preparando ambiente
Além disso, para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

    Python 3.7.4
    Django 3.1
O Django pode ser instalado através do comando:

    pip install Django==3.1

#### Projeto base inicial \
[Neste link]('https://github.com/guilhermeonrails/projeto_inicial_drf_clientes/archive/master.zip'), você encontra o projeto inicial na qual daremos continuidade e usaremos para aplicar novos conceitos. Sendo assim, faça o download deste projeto e siga as instruções passadas pelo instrutor na próxima atividade.

Em caso de dúvida na instalação ou durante o curso, conte sempre com o fórum da Alura!

:)

### Conhecendo o projeto

[00:00] Vamos iniciar então o desenvolvimento da nossa API e aprofundar o nosso conhecimento com o Django Rest?

[00:05] Para começar, já temos um projeto que vamos utilizar como base e você pode fazer download deste projeto na atividade anterior a esse vídeo, no “Preparando Ambiente”.

[00:15] Eu fiz o download do projeto aqui, e a primeira coisa que vou fazer é mudar esse nome “drf_projeto_inicial_master”. Vou chamar de “Projeto_clientes”.

[00:29] Vou utilizar o “VScode” como editor de código, vou abrir ele aqui dentro, então vou arrastar ele para dentro do nosso projeto. Temos então o nosso projeto que vamos utilizar nesse curso para aprender vários outros fundamentos e aprofundar nossos conhecimentos.

[00:47] Para começar, temos “clientes” que é um app e temos setup, onde vamos manter toda a configuração desse projeto.

[00:57] Para começar, vou clicar em “settings” “PROJETO_CLIENTES > setup > settings.py” para entendermos como que está e o que tem nesse “settings.py”. Assim que eu abro o ´settings.py´, abre uma mensagem de erro que fala “ Aqui é um arquivo Python e você não selecionou nenhum interpretador “Python” para esse ambiente”. Vou fechar e já vamos resolver esse problema logo mais.

[01:18] Então vamos ver, descendo um pouco a página, as informações importantes são Apps Instalados “INSTALLED_APPS” e temos rest_framework e tem o app de “clientes”. Já vamos descobrir.

[01:29] O nosso banco de dados para esse curso vai ser o “SQLite3” mesmo e poderíamos utilizar o Postgres ou uma SQL, assim como conteúdos que já vimos em outros cursos também. Mas, para esse curso o “SQLite3” é suficiente para nós.

[01:45] A língua nativa LANGUAGE_CODE = pt=br vai ser o português do Brasil e o time zone TIME_ZONE vai ser o horário de São Paulo, então America/Sao Paulo .

[01:52] Indo em “urls.py” “PROJETO_CLIENTES > setup > urls.py” vamos ver que já existe uma rota criada, um registro criado para o nosso cliente, e já temos o ´ClientesViewSet´ preparado para funcionar.

[02:03] Vamos conhecer então o app de clientes. Em “PROJETO_CLIENTES>clientes” temos a parte de migrações, temos o ´admin.py´ cadastrado e preparado para o nosso app de clientes, temos um modelo com nome, e-mail, CPF, RG, celular e um campo “Boolean” indicando se ele é ativo ou não.

[02:24] Temos já o “serializer” , o cliente “serializer” criado através do modo ´serializer´ e para finalizar, em “view.py”, temos o ´ClientesViewSet´ . Todo o conteúdo que está descrito nesta aplicação são conteúdos que já vimos no curso anterior.

[02:41] Como eu faço para essa aplicação funcionar aqui na minha máquina? Observe que estamos falando de uma aplicação “Django“ que tem o “Django Rest Framework” instalado, que tem vários outros módulos e pacotes instalados. Quais são os pacotes que eu preciso instalar e aonde eu vou instalar esses pacotes?

[03:00] Bom, para começar vamos criar um ambiente virtual para essa aplicação e vai instalar todos os módulos necessários para esse projeto funcionar descritos no arquivo txt. “requeriments.txt” .

[03:15] Tudo que esse projeto precisa para ele funcionar está em “PROJETO_CLIENTES > requeriments.txt” . Ele vai precisar do “Django”, do “djangorestframework”, vai precisar do ´lazy-object-proxy´ e todos os outros módulos descritos, os 14 módulos descritos.

[03:28] Como vamos fazer isso? Vou abrir meu terminal com "Cmd + J” e fechar essa linha do lado com “Cmd + B” e vou começar a criar um ambiente virtual para essa aplicação.

[03:38] Então primeiro ´python -m venv ./venv´ e quando dou um “enter”, ele criou a minha ´venv´ e ele já percebeu que criamos um ambiente virtual. Vou fechar essa mensagem do VScode pra fazermos mais manual.

[03:56] Então criei a minha “venv”, vou ativá-la colocando ´source venv/bin/activate´. Ativei minha “venv”. Quais são os módulos que já tenho instalado nesse “venv”? Vamos descobrir?

[04:13] Se eu digito ´pip freeze´ e dou um “enter”, observe que não acontece nada. Ele vem para baixo, não temos nenhum módulo instalado e vamos precisar de todos esses módulos que temos em ´requirements.txt´.

[04:27] Será que vou ter que instalar um a um na mão? Não. Tem uma forma que podemos pedir para o “pip” instalar todos esses módulos para nós. Vamos colocar ´pip install - r requirements.txt´ .

[04:51] Quando der um “enter” o que vai acontecer? Ele vai começar a pegar um a um e vai instalar todas as dependências desses módulos e todas as dependências que estão descritas no nosso “arquivo txt”.

[05:05] Assim que terminamos ele pergunta se não queremos atualizar nosso “pip”. Vamos fazer isso também, então ´pip install --upgrade pip´ e eu vou instalar o “pip” e para finalizar. Observe que temos aqui na barra inferior do programa, em amarelo, “Selected python interpreter”. O VScode está quase gritando “Por favor, seleciona para nós o interpretador python”.

[05:25] Quando clicamos na mensagem e scrollamos para baixo vamos ter o Python da ´venv´, que é o que queremos. Então vou selecionar essa opção ´Python 3.7.4 64-bit (venv: venv) ´.

[05:35] Então já temos o interpretador, já tem o ambiente virtual, já tem todos os módulos instalados para essa “venv” aqui. O que eu vou fazer? Vou rodar minha aplicação ´pyhton manage. py runserver´.

[05:50] Assim que eu rodo, observe. Ele dá uma mensagem assim: “Você tem 17 migrações pendentes, talvez seu projeto não funcione como você espera porque ele vai precisar da estrutura no banco de dados do “admin”, “auth”, “contenttypes” e “sessie” “. Ele falou “Considere rodar o arquivo, executar no nosso terminal, o ´python manage.py migrate´” .

[06:14] O que eu vou fazer? Vou parar meu servidor, vou nem abrir meu projeto e vou rodar dois códigos. O primeiro é para ele verificar se tem alguma migração para ele gerar essas migrações para mim.

[06:23] Então vou utilizar o comando ´python manage.py makemigrations´ e vou dar um “enter”. O que ele percebeu? Que existe uma migração de clientes.

[06:35] O que vou fazer agora? Vou criar toda a estrutura que o Django precisa, mais essa estrutura de clientes. Então vou utilizar o comando ´python manage.py migrate´ e quando eu der um “enter” ele vai gerar no banco de dados toda a estrutura para mim.

[06:51] Para finalizar eu vou rodar de novo o ´python manage.py runserver ´e não temos mais aquela mensagem. Subiu a minha aplicação e se eu for numa aba e digitar “localhost: 8000” eu vou conseguir ver que minha aplicação está sendo executada corretamente..

[07:07] Se eu clico no app de “clientes” eu consigo criar os meus clientes com todos os campos já descritos. então vou criar o primeiro cliente, vai ser eu mesmo. então Guilherme, email vai ser gui@alura.com, e o cpf sabemos que o cpf tem 11 dígitos então vou deixar 11 dígitos mas tudo com numero 1. O RG tem 9 dígitos então tudo com 1 também. Vou colocar um número de celular 11990909090 e vou dizer que esse cliente Guilherme é ativo.

[07:45] Quando eu dou um post temos lá o cliente Guilherme registrado. Só que se pararmos para pensar, vamos supor que todas essas informações de RG, CPF, celular, são válidas, um usuário super bonzinho que estava mexendo na nossa API.

[08:00] Mas e se eu quiser registrar um usuário com nome de : 1234, e-mail: 1234, CPF: 1234, RG: 1234, e celular: 1234. O que vai acontecer com a nossa aplicação? O que vai acontecer com o nosso código? Quando eu dou um post observe que vamos ter uma mensagem de erro. De todos os campos ele só conseguiu identificar uma mensagem, que foi o campo e-mail que ele fala “Insira um endereço de e-mail válido”.

[08:30] Por que isso está acontecendo? Isso acontece porque lá no nosso modelo, se eu abro “PROJETO_CLIENTES > clientes > models.py” temos uma descrição do campo e-mail com o ´models.EmailField´. Por causa desse campo conseguimos entender que o nosso e-mail precisa ter o arroba, precisa ter o “ponto com” alguma coisa.

[08:57] Então se eu vier no campo do e-mail e colocar “1234@” e der um post, ele ainda está inválido. Se eu colocar “1234@alura.com” e der um post conseguimos registar. E a única verificação, validação de campo que tivemos, foi no campo e-mail, só que o nome 1234, RG, CPF, celular tudo 1234, não está muito legal.

[09:20] Então o que vamos aprender nas aulas seguintes? A validar esses campos. Como que garantimos ou fazemos o máximo possível para garantir que não entre dados incorretos na nossa base da nossa API?

### Valor único

As validações podem ser feitas pelo MODELS.PY do APP que o próprio SERIALIZERS.PY utiliza o método VALIDATOR.

---

[00:00] Agora que já entendemos melhor como funciona a nossa API e clientes e como estão esses campos, parece que de todos esses campos que temos, o único campo que exige uma verificação um pouco melhor é o e-mail por conta do nosso modelo ´models.EmailField´. Ele espera que tenhamos o nome do e-mail, o “arroba” e o “ponto com” alguma coisa.

[00:22] O que eu quero fazer agora é aos poucos colocar validação, e tentar garantir que os dados que a nossa API vai receber são dados corretos. Podemos começar com o CPF. Não vamos validar o número do CPF exato, existe um algoritmo que faz essa validação, não vamos fazer isso agora, vamos fazer mais para frente no curso.

[00:41] O que eu quero fazer é garantir que nenhum CPF vai ser igual ao outro, quero garantir a exclusividade do CPF. Mas isso eu faço onde? Faço no meu modelo ou faço no serializer? Bom, podemos fazer no modelo e verificar se o nosso serializer puxa essa validação que vem do nosso modelo ´models.py´. Vamos fazer isso?

[01:03] O que eu vou fazer é o seguinte, no nosso campo CPF dentro do nosso ´models.py´ eu vou colocar uma tag indicando que ele deve ser único, então vou colocar a propriedade ´unique=True´ . Vou falar que o CPF precisa ser único.

[01:18] Vou “salvar” e abrir meu terminal, deixa eu parar esse servidor com “Crtl + C” e vou rodar o ´python manage.py makemigrations´ que alteramos nossa base de dados. Ele percebeu. Opa, apareceu que existe um campo alterado, uma alteração no campo CPF de clientes, é isso que queremos, e eu quero migrar isso para o nosso banco de dados agora.

[1:45] Vou colocar então ´python manage.py migrate´, apliquei essa migração. O que vou fazer agora? Vamos subir nosso servidor com ´python manage.py runserver´. E o que eu quero fazer é tentar criar mais uma pessoa com esse RG que colocamos de 111111111.

[2:09] Então vou até copiar esse RG para garantirmos esses 11 dígitos apenas com 1 e vamos ver que isso não vai ser possível. então vou usar o mesmo nome e e-mail, o CPF vou usar 11111111111 o RG vou colocar 1234, celular vou colocar qualquer celular e vou falar que ele é ativo

[2:28] Quando eu der um post ele vai falar “cliente com CPF já existe”. Era o que queríamos. Mas essa validação está acontecendo no momento da instância do modelo ou no nosso serializer? Vamos verificar isso?

[02:41] Para isso vou abrir um outro terminal, observe que já estou com minha ´venv´, vou fazer o seguinte, vou acessar o “Shell” do Python para importarmos essa classe de clientes “serializer´ e vamos verificar que é o CPF. Existe uma propriedade das validações, o “serializer” puxa a validações que estão nos nossos modelos.

[03:08] Então para eu acessar o meu shell, vou colocar ´python manage.py shell´, com dois L’s . Acessei o “Shell”, o que vou fazer agora é importar para meu módulo interativo essa minha classe de clientes ´serializer´.

[03:29] Então vou fazer da seguinte forma, vou dizer que do meu ´clientes.serializers´ eu quero importar o meu ClienteSerializer, ficando >>> from clientes.serializers import ClienteSerializer´. E dou um enter.

[03:49] Eu importei o cliente e o que eu vou fazer? Agora que eu trouxe esse meu cliente ´serializer´, eu vou dizer que o meu serializer é igual a ClienteSerializer e vou dizer que ele é uma instância desse meu cliente ´serializer´, então >>> s = ClienteSerializer(). Então meu “s” é uma instância de clientes ´serializer´.

[04:10] O que eu quero fazer agora é visualizar, então vou colocar um “print”, a forma como esse meu cliente está sendo representado. Então vou colocar repr para representar esse meu cliente serializer, fechando a função do s e o segundo parênteses do “print” ficando >>>print (repr(s)).

[04:26] Quando dou um “enter” observe que ele vai mostrar para nós os detalhes desse meu cliente serializer, então o id é um IntegerField com label ID, disponível apenas para o modo de leitura, o nome é um ´CharField´ de no máximo 100 caracteres, o e-mail com no máximo 30, o CPF é um CharField com no máximo 11 caracteres e dentro do CPF temos o ´validators´.

[04:49] Observe que interessante, ele trouxe e incluiu esse validators e indicando que temos um valor único mostrado em ´UniqueValidator´. Ou seja, dessa forma te garantimos que todas as validações que incluirmos no nosso modelo serão puxadas pelo nosso serializer também.

[05:11] Então, por exemplo, podemos testar também. Vou criar um RG com mais números. Então no nosso RG vou colocar “1234123412341234”, eu ultrapassei os números do meu RG. Observe que depois que damos o post, aparece uma mensagem em vermelho dizendo “certifique-se que esse campo não tenha mais do que 9 caracteres”.

[05:28] Não escrevemos essas mensagens de erro, mas só de inserirmos esses detalhes nos nossos modelos, já conseguimos puxar essas validações para o nosso serializer também

[05:39] O que vamos ver na sequência? Vamos aprender a incluir as validações direto no serializer e ver quais são as vantagens dessa atitude.

### Para saber mais: Documentação oficial

O Django Rest Framework é uma biblioteca poderosa para desenvolver web APIs de forma rápida, segura e simples. Para maiores informações sobre validações no Django Rest Framework, acesse o manual ou a documentação oficial [neste link]('https://www.django-rest-framework.org/api-guide/validators/')

### Exercício: Aplicação integrável

Durante os vídeos, Lucas desenvolveu o seguinte código no models.py e serializers.py respectivamente:

models.py

    class Cliente(models.Model):
        nome = models.CharField(max_length=100)
        email = models.EmailField(blank=False, max_length=30)
        cpf = models.CharField(max_length=11, unique=True)
        rg = models.CharField(max_length=9)
        celular = models.CharField(max_length=14)
        ativo = models.BooleanField()

        def __str__(self):
            return self.nome

serializers.py

    class ClienteSerializer(serializers.ModelSerializer):
        class Meta:
            model = Cliente
            fields = '__all__'

Com base nos trechos de código acima, podemos afirmar que:

a) Não haverá validação em nenhum campo.

b) **Alternativa correta:** Mesmo sem validações no serializers.py, haverá algum tipo de validação nos campos.
- _Alternativa correta! Certo! O campo email por exemplo, por conta do models.EmailField é esperado que esse campo tenha o símbolo do @ e um domínio (gmail.com por exemplo). Além disso, haverá uma validação em todos os campos que excederem o tamanho máximo definido pelo max_length._

c) **Alternativa correta:** No Django Rest, a validação é realizada inteiramente na classe do serializador.
- _Alternativa correta! Como vimos em aula, a restrição de exclusividade no campo cpf está sendo explicitamente aplicada por um validador no campo do serializador._

### O que aprendemos?

- Carregamos o projeto em nosso ambiente local;
- Incluímos uma restrição de valor único no campo CPF;
- Vimos que as restrições do modelo são executadas no serializer..

## 2. Validações no Serializer
### Validando no serializer
Para criar validações no SERIALIZER.PY definimos funções dentro das class Serializer.

    class SERIALIZER(serializers.ModelSerializer):
        class Meta:
            model = 
            fields = '__all__'

            def validate_campo(self, campo):
                raise serializers.ValidationError('Mensagem') # mensagem de erro
                return campo
---

[00:00] Nós vimos que as validações do modelo são explicitamente executadas no nosso “serializer.py” e conseguimos criar as nossas validações do “serializer” e garantir que tenhamos os dados corretos no nosso modelo de clientes.

[00:15] Por exemplo, colocamos a exclusividade única no nosso modelo e ele falou “o cliente com esse CPF já existe” só que se eu tiro um dígito do CPF e deixo um CPF com 10 dígitos, podemos até contar aqui, que é um CPF inválido também e dou um post, observe que a mensagem do CPF desaparece. Ou seja, podemos ter um CPF que tenha 10 dígitos ou menos.

[00:46] Vou colocar um CPF com apenas um dígito e observe que nenhuma mensagem será exibida, e não é isso que queremos. Queremos que o CPF tenha 11 dígitos. Como podemos fazer isso? Podemos fazer uma verificação para saber se o tamanho do CPF não for igual a 11, falamos que o CPF tem que ter 11 dígitos, por exemplo.

[01:04] Então vamos criar essa validação. Essa validação nós não vamos criar no nosso modelo, nosso modelo deixamos a tag de unique=True garantindo que nosso CPF seja único. Só que no serializer vamos incluir algumas validações, e ver como que podemos incluir algumas validações, no nosso caso o CPF. Eu quero garantir que o CPF tenha 11 dígitos.

[01:27] Então o que eu vou fazer? Vou criar uma função, dentro de "serializer.py” e vou chamar de validate_cpf(parameter_list), com nome do campo que eu quero. Como um parâmetro eu vou passar a instância que estamos utilizando naquele momento e quero passar também o CPF, então vai ficar validate_cpf(self, cpf).

[01:45] E na linha de baixo vou colocar f.len(cpf) . !=11 .Vou perguntar se o tamanho do CPF, utilizando aqui o ´len´, não for igual a 11, o que eu quero fazer? Quero dar uma mensagem de erro. E podemos usar o ´raise.serializers.ValidationError´ e dentro vou passar o erro que quero utilizar.

[02:16] Então quero dizer que o CPF tem que ter 11 dígitos, por exemplo. Então vou escrever uma string e vou escrever “ O.CPF.deve.ter.11.dígitos” .

[02:31] O que fizemos? Eu criei uma função ainda no escopo desse meu ClienteSerializer, passando como argumento o ´self´ e o ´cpf´ e verifiquei. Se o tamanho do CPF não for igual a 11, eu quero exibir uma mensagem de erro e eu exibo essa mensagem de erro.

[02:52] Porém, se ele for igual a 11 eu preciso retornar alguma coisa, então vou colocar um ´return´ e vou passar o CPF, ficando return.cpf. Agora sim.

[03:05] Vou abrir meu terminal, vou sair do meu shell, não vamos usar o shell agora, então >>>quit(). Vou deixar o “terminal 2” caso tenhamos mais algum exemplo, e agora o que vou fazer? Eu tenho aqui o meu servidor rodando, vou fazer esse teste. Deixei o CPF com 1 dígito, vou dar um post e aparece aqui “O CPF deve ter 11 dígitos’.

[03:33] Se eu digito aquele monte de 11 e dou um post ele dá a mensagem de “O CPF já existe”, se eu mudo um dígito, esse CPF ainda continua sendo um número inválido, vamos arrumar isso. Só que observe que essa mensagem já não vai aparecer mais, garantimos que o CPF tenha 11 dígitos apenas.

[03:55] Se eu colocar outro CPF, mas colocar um dígito a menos, e dou um post, temos a mensagem do “O CPF deve ter 11 dígitos” . Essa é uma forma bem simples de conseguirmos incluir uma validação no nosso “serializer”.

### Validando todos os campos

[00:00] Nós vimos que as validações do modelo são explicitamente executadas no nosso “serializer.py” e conseguimos criar as nossas validações do “serializer” e garantir que tenhamos os dados corretos no nosso modelo de clientes.

[00:15] Por exemplo, colocamos a exclusividade única no nosso modelo e ele falou “o cliente com esse CPF já existe” só que se eu tiro um dígito do CPF e deixo um CPF com 10 dígitos, podemos até contar aqui, que é um CPF inválido também e dou um post, observe que a mensagem do CPF desaparece. Ou seja, podemos ter um CPF que tenha 10 dígitos ou menos.

[00:46] Vou colocar um CPF com apenas um dígito e observe que nenhuma mensagem será exibida, e não é isso que queremos. Queremos que o CPF tenha 11 dígitos. Como podemos fazer isso? Podemos fazer uma verificação para saber se o tamanho do CPF não for igual a 11, falamos que o CPF tem que ter 11 dígitos, por exemplo.

[01:04] Então vamos criar essa validação. Essa validação nós não vamos criar no nosso modelo, nosso modelo deixamos a tag de unique=True garantindo que nosso CPF seja único. Só que no serializer vamos incluir algumas validações, e ver como que podemos incluir algumas validações, no nosso caso o CPF. Eu quero garantir que o CPF tenha 11 dígitos.

[01:27] Então o que eu vou fazer? Vou criar uma função, dentro de "serializer.py” e vou chamar de validate_cpf(parameter_list), com nome do campo que eu quero. Como um parâmetro eu vou passar a instância que estamos utilizando naquele momento e quero passar também o CPF, então vai ficar validate_cpf(self, cpf).

[01:45] E na linha de baixo vou colocar f.len(cpf) . !=11 .Vou perguntar se o tamanho do CPF, utilizando aqui o ´len´, não for igual a 11, o que eu quero fazer? Quero dar uma mensagem de erro. E podemos usar o ´raise.serializers.ValidationError´ e dentro vou passar o erro que quero utilizar.

[02:16] Então quero dizer que o CPF tem que ter 11 dígitos, por exemplo. Então vou escrever uma string e vou escrever “ O.CPF.deve.ter.11.dígitos” .

[02:31] O que fizemos? Eu criei uma função ainda no escopo desse meu ClienteSerializer, passando como argumento o ´self´ e o ´cpf´ e verifiquei. Se o tamanho do CPF não for igual a 11, eu quero exibir uma mensagem de erro e eu exibo essa mensagem de erro.

[02:52] Porém, se ele for igual a 11 eu preciso retornar alguma coisa, então vou colocar um ´return´ e vou passar o CPF, ficando return.cpf. Agora sim.

[03:05] Vou abrir meu terminal, vou sair do meu shell, não vamos usar o shell agora, então >>>quit(). Vou deixar o “terminal 2” caso tenhamos mais algum exemplo, e agora o que vou fazer? Eu tenho aqui o meu servidor rodando, vou fazer esse teste. Deixei o CPF com 1 dígito, vou dar um post e aparece aqui “O CPF deve ter 11 dígitos’.

[03:33] Se eu digito aquele monte de 11 e dou um post ele dá a mensagem de “O CPF já existe”, se eu mudo um dígito, esse CPF ainda continua sendo um número inválido, vamos arrumar isso. Só que observe que essa mensagem já não vai aparecer mais, garantimos que o CPF tenha 11 dígitos apenas.

[03:55] Se eu colocar outro CPF, mas colocar um dígito a menos, e dou um post, temos a mensagem do “O CPF deve ter 11 dígitos” . Essa é uma forma bem simples de conseguirmos incluir uma validação no nosso “serializer”.

### Melhorando o código
Para o código do SERIALIZERS.PY não ficar com muitas linhas, podemos dividir nosso código de validação em um arquivo diferente. VALIDATOR.PY

---

[00:00] Agora que nós incluímos as validações no nosso “Serializer”, vamos pensar em deixar o nosso código um pouco mais organizado? O que eu quero propor? Vamos tirar essas regras de validações e colocar num arquivo que só mantém essas validações, deixando nosso “Serializer” mais limpo.

[00:17] Por exemplo, essa verificação de se o CPF tem 11 dígitos, ou se o nome é alfa numérico ou se o RG não tem 9 dígitos. Vamos colocar todas essas validações num outro arquivo e de alguma forma pegamos essas informações e mandamos para que sejam verificadas, tornando nosso serializador mais limpo.

[00:38] Para começar, vou criar outro arquivo dentro do nosso app de clientes em “PROJETO_CLIENTES>clientes” chamado de “validators.py”. Dentro desse nosso ´validator.py´ eu quero incluir nossas validações que estão no nosso ´serializer.py´ do CPF. Dei um "Ctrl+X" na validação do CPF e um “Ctrl + V” dentro do nosso ´validators.py´ e incluí e trouxe para cá.

[00:58] Está vendo que ele ficou com dois espaços do lado esquerdo do if len(cpf) “=11: , dou um “Cmd + abre colchetes” e empurramos para o lado. Então abri e coloquei essa validação, só que eu quero que essa validação tenha um outro nome.

[01:10] Observe que sempre que chamamos ´validate_´ e o nome do campo, já estamos especificando qual é o campo que queremos validar. Vamos fazer de uma outra forma.

[01:18] Eu vou comentar essas outras linhas para não ficarmos confusos. E em cima eu vou criar uma função. Essa função eu vou chamar de apenas validate e não validate e o nome do campo. Então se eu quero validar um campo específico no serializer eu posso? Posso, da forma que tínhamos feito, cria uma função validate_ e no nome do campo, passando a instância e o nome do campo que queremos validar.

[01:42] Agora vai ser um pouco diferente, vamos passar a instância e como segundo parâmetro vamos passar o “data”. Então fica validate(self, data):. O que isso vai significar? O que vai representar na nossa aplicação? Que vamos ter acesso a todas as informações quando passamos o “data”, do nosso serializer.

[02:00] Então a partir do “data” vamos buscar o nome, o e-mail, o CPF, o RG, o celular, e assim por diante os demais campos.

[02:08] Eu criei um “validator.py” e eu quero que o campo ´validate_cpf´ se chame cpf_valido. Não precisamos da instância, só vamos precisar do CPF, para ficar mais claro vou colocar numero_do_cpf, ficando cpf_valido(numero_do_cpf): e vamos verificar se o número do CPF é esse.

[02:33] Não vou precisar do if do if len. Eu quero que o if seja apenas um return, quero que ele volte para mim o número do CPF, quero verificar se ele é igual a 11, então return len(numero_do_cpf) ==11 .

[02:47] Caso ele não seja igual a 11, essa verificação vamos precisar importar para o ´serializers.py´. Então o que vou fazer? Vou colocar from clientes.validators import . Vou colocar um asterisco para ele trazer tudo, trazer todas as informações que temos.

[03:07] E embaixo vou criar um if, if cpf_valido() e precisamos passar o número do CPF, como passo o número do CPF que está no “data”? Não temos mais um campo específico. Simples, escrevemos ´data´ e entre colchetes vamos digitar o nome do campo que queremos, entre aspas, então if cpf_valido(data[‘cpf’] e ele vai verificar para mim se o CPF é válido. Se ele não for, exibimos a mensagem de erro.

[03:40] Então olha como vai ficar a leitura do nosso código, se o CPF não for válido, exibimos uma mensagem de erro. Observe que colocamos o not aqui, então if not cpf_valido(data[‘cpf’]): , se não for válido o CPF, passamos o CPF e exibimos essa mensagem de erro.

[04:00] E no final, depois que validamos os campos, já deixamos nosso código limpo, retornamos apenas o “data” em ´return data’ . Vou salvar o validators.py também. Esqueci de tirar os dois pontos do final de return len(numero_do_cpf) ==11: pois não é uma função.

[04:14] Então pensa comigo antes de executarmos lá o seguinte exemplo: vamos supor que o ´len´ do número do CPF é 10. 10 é igual igual 11? Não, isso é falso. Então o que vamos ter como resultado disso é um false.

[04:38] O que vamos ter disso 10 == 11 é um valor falso, então ele vai retornar para nós um valor falso. O que vai acontecer? Lembra que o resultado dessa operação é um falso, só que para eu conseguir exibir a mensagem de erro eu preciso de uma condição verdadeira, se for verdadeira ele faz alguma coisa. E como transformamos do falso para o verdadeiro? Com o not na frente.

[05:00] Então ele falou “10 não é igual a 11” aqui ele está mandando falso, só que como colocamos o not na frente em if not cpf_valido(data[‘cpf’]): vamos inverter. O que era falso, lá no nosso serializer vai virar verdadeiro e então vamos conseguir entrar nessa função.

[05:20] Salvei, abriu o terminal, parece que está tudo ok. Então vamos voltar e tentar salvar o cliente. Vou dar um post e aparece uma mensagem estranha non_field_errors e “O CPF deve ter 11 dígitos” .

[05:36] Por que ele não apareceu grifando o campo CPF igual estávamos vendo antes? Porque vamos precisar especificar. Existe uma mensagem de erro mas não sabemos onde, pegamos a informação do “data” mas em nenhum momento falamos “Essa mensagem de erro se refere a esse campo”. E como fazemos isso?

[05:53] Vamos fazer assim, vou colocar abre chaves e fecha chaves em raise serializers.ValidationError({“O CPF deve ter 11 dígitos”}). Observe que aqui eu tenho o parênteses da minha função validationError, quando eu abro chaves eu vou colocar entre aspas o nome do campo então ‘cpf ‘: ‘. Então coloquei o nome do campo, fechei chaves, fechei as aspas, coloquei dois pontos e o nome da mensagem de erro, fechei aspas e fechei o parênteses. Vai ficar 'cpf‘ :”O CPF deve ter 11 dígitos".

[06:18] Se eu salvo e executo mais uma vez, aparece “cpf”, temos aquela validação como estávamos vendo antes. Então o que vai mudar do validate para uma função que valida direto um campo? Vamos pegar as informações através do “data” e vai pegar as mensagens de erro e indicar nas nossas ValidationError o nome do campo entre chaves, dois pontos, e a mensagem de erro.

[06:43] Então vou fazer isso agora para os outros campos também. Vou fazer para o meu validation nome. Vamos colocar esse do nome também, vou selecionar o validate_nome no nosso serializers.py, apertar “Command + X” e colar dentro de validations.py. Selecionei tudo, com “Command + barra” eu tiro o comentário e “Command + abre colchetes” eu empurro tudo. Eu quero saber se o nome só tem caracteres alfabéticos, então é isso o que eu quero retornar.

[07:11] Então, na linha de baixo de validate_nome vou retornar return nome.isalpha. Vou tirar o ́return nome´ que não vamos mais usar e o campo do ´raise serializer.ValidationError´ ele vai para o nosso serializador.

[07:26] A única coisa que precisamos aqui é o nome, então vou deixar validate_nome(nome) . Vou salvar essa verificação e vamos criar dentro de serializers.py. Vamos alterar o ´validate_nome´ em validator.py e vamos colocar nome_valido(nome) . Então if nome_valido(data[‘nome’]). .

[07:56] Crio a minha função e passo a mensagem de erro na linha de baixo com raise serializer.ValidationError({“Não inclua números neste campo”) . Qual é o campo que estamos utilizando aqui e queremos exibir a mensagem de erro? No campo nome. Nome entre aspas, dois pontos, quando fecha o campo ele fecha a nossa string e colocamos também fechando as aspas. Ficando ({‘nome’: ”Não inclua números neste campo”).

[08:16] No ´return data´, vai precisar ser a última coisa que fazemos depois de executar as nossas validações, então vou colocar ele na linha de baixo do nosso raise serializers.ValidationError. Vamos fazer esse teste, se o nome for válido exibimos uma mensagem de erro? isso está um pouco estranho.

[08:31] Então vamos supor, se o nome for “123”, ele é alfa numérico? Não, então vamos receber um falso aqui. Para conseguirmos acessar e exibir mensagens de erro, a condição precisa ser verdadeira, então o que eu faço? Coloco um not no if, então if not nome_valido(data[‘nome’]).

[08:47] Então colocando um not ali, já conseguimos verificar. Vamos ver. Então vou colocar 1234 no nome, e o CPF “1234512345” e o “1” para indicar os 11 dígitos e quando dou um post aparece no nome “Não inclua números neste campo”. deu certo. Vamos fazer o próximo?

[09:07] O RG, copiei de serializers.py , tiro o comentário com “Command + X”, vamos no validator.py e com “Crtl + colchetes abrindo” puxamos para a esquerda. Vou chamar de rg_valido só para manter o padrão, passando apenas o número do RG, então rg_valido(numero_do_rg).

[09:43] E vou passar o número do RG para if len(numero_do_rf) !=9: , vou tirar o ´return rg´ porque não preciso dele, e vou retornar direto nessa condição. No lugar do if´eu vou ter um return. Então return len(numero_do_rf) !=9: e vou tirar o raise serializers.ValidationError porque essa mensagem vai ficar no nosso serializer, e vou verificar dentro de serializers.py.

[10:05] Para manter já o padrão vamos colocar if rg_valido(data[‘rg’]) e embaixo a mensagem de erro . Se o RG não for válido, então vamos mudar para if not rg_valido . Vamos ver qual a verificação que estamos fazendo para ver se o RG é válido ou não?

[10:30] Vou passar o ´return data´ para baixo, selecionando ele e utilizando “Ctrl+X” e colando com “Ctrl+V”. Então nosso “validate” está assim e vamos ver qual é a verificação. O que eu quero ver é se o RG não for válido, exibimos uma mensagem de erro. Como estamos verificando o RG? Se ele não for igual a 9. Então vamos fazer diferente, se ele for igual igual a 9.

[10:55] Vou colocar um exemplo aqui embaixo, o len do RG veio com 8. 8 é igual igual a 9? Não, não é igual, então ele vai receber uma mensagem de falso, na mensagem de falso ele não vai conseguir exibir essa condição do if not rg_valido. Porque para cairmos nessa condição, o if precisa ser verdadeiro, então vamos inverter a ordem, deixamos o RG com a condição verdadeira.

[11:18] Vamos ver? Então se eu dou um nome mesmo de “Gustavo” e dou um post, observe que caímos numa mensagem de erro, deixa eu ver o que eu errei. Eu esqueci de tirar o nosso exemplo de 8 == 9.

[11:30] Tirei o exemplo e vamos voltar para conseguirmos visualizar melhor. Se eu dou um post, deu as mensagens de non_field_errors e “O RG deve ter 9 dígitos” . Então voltando no ´serializer.py´ eu só esqueci de marcar o campo que vamos utilizar, que é o campo RG, então vou adicionar ´ ‘rg’ ´ em raise serializers.ValidationError({‘rg’: “O RG deve ter 9 dígitos”}).

[11:53] E o ´return data´ no final. Se eu dou um post mais uma vez, vai aparecer “rg” e “O RG deve ter 9 dígitos”, grifado de vermelho nosso campo do RG.

### Exercício: Motivo para validar

Você foi contratado para trabalhar exclusivamente com validação de dados. Partindo dos princípios que você estudou, qual o principal motivo de realizarmos validação de dados em uma API?

a) **Alternativa correta:** Para mantermos a qualidade da informação.
- _Alternativa correta! Certo! O processo de validação ajuda a garantir que estamos lidando com dados reais e válidos._

b) Para não comprometermos a usabilidade da API.

c) Para não comprometermos o uso do banco de dados com dados inválidos.

### O que aprendemos?

- Aprendemos como validar campo a campo criando uma função, por exemplo:

        def validate_<nome_do_campo>(self, nome_do_campo):
        if len(nome_do_campo) < 11:
            raise serializers.ValidationError("O campo deve ter 11 dígitos")
        return nome_do_campo

- Vimos que podemos criar uma função chamada validate para validar todos os campo, validate(self, data) e acessar cada campo com data['<nome_do_campo>'];

- Melhoramos nosso código removendo a lógica de validação do serializer.

## 3. Importando validações e gerando clientes
### Expressões regulares
São expressões para validação dos dados.

    import re

    def celular_valido(num_celular):
        modelo = ‘[0-9]{2} [0-9]{5}-[0-9]{4}´
        return re.findall(modelo, numero_celular)

---

[00:00] Passamos a lógica da validação aqui pro validators.py e tiramos ele no nosso serializer.py. O que vamos fazer agora? A validação do celular, só que eu quero que o celular tenha um padrão, um modelo.

[00:13] Por exemplo, quando vamos lá na nossa aplicação, quero que o celular tenha o DDD, o espaço, o número 9, aí temos 4 dígitos, quero que tenha um traço e mais 4 dígitos. Qualquer coisa diferente disso eu quero que não seja aceito pela nossa API, não seja um dado válido.

[00:31] Então como podemos criar esse nosso modelo e garantir que o celular possui um número válido? Vamos usar expressões regulares. Se você não conhece expressões regulares, abaixo desse link temos um curso aqui na Alura que fala bastante sobre expressões regulares e validações e você vai poder assistir para entender melhor.

[00:52] Mas como nosso exemplo é simples, queremos construir esse modelo de celular, vamos ver como integramos isso no nosso Djang Rest e fazemos nossa validação.

[01:03] Para começar o que vamos fazer? Em “serializer.py” eu vou tirar a função que temos do celular, vou desconectar, com “Command + espaço” , vou dar “Ctrl + X” nela e vou trazer ela para dentro do “validators.py” . E vamos ter uma função que vai validar o celular. Vou usar “Command + colchete” só para trazer para o lado, vou falar que o nome dessa função vai ser celular_valido . E vamos precisar apenas do número do celular.

[01:32] Então posso até mudar, vou colocar celular_valido(numero_celular). Então não queremos verificar apenas se o número do celular possui 11 dígitos, vamos fazer uma outra verificação. O ´raise´ vamos jogar para lá e vamos tirar o return celular. Depois vamos ter outra mensagem de retorno, para retornar um valor verdadeiro falso para utilizarmos no nosso serializer.

[01:56] Como eu utilizo expressões regulares no meu código? Eu dei dois enters e na primeira linha eu vou importar um código que já está no nosso projeto, que é o ´re´, então ´return re´e a partir dele vamos conseguir utilizar expressões regulares.

[02:13] Então vou até criar um doc string para ficar mais claro com o que essa função vai fazer. Coloquei três aspas e vou falar por exemplo “”“Verifica se o celular é válido”””. Posso deixar um exemplo, então o que eu quero que tenhamos é um 11, um espaço, o número 9, 4 dígitos, um traço e 4 dígitos. Ficando “””Verifica se o celular é valido (11 91234-1234)””” ´

[02:42] Só para ficarmos com essa estrutura, esse modelo que queremos criar bem marcado. A primeira coisa que iremos fazer é criar esse modelo utilizando expressões regulares. Vou remover nesse código ́if len(celular) < 11.

[02:54] A primeira coisa que vou fazer é criar uma variável que vou chamar de modelo e vou criar esse modelo utilizando expressões regulares. Então entre aspas vou colocar um colchete e quero que esse primeiro valor, que é o DDD, que pode ser 11, 15, 21, dependendo do estado que a pessoa estiver, pode ser um número entre 0 e 9. E quantos dígitos vamos ter? Dois, então vou colocar isso entre chaves.

[03:22] Depois o que eu quero é um espaço, coloquei um espaço, e temos depois 5 dígitos que vou fazer a mesma coisa. Entre colchetes eu vou dizer que posso ter um número de 0 a 9, e eu tenho entre chaves o número 5, indicando que eu tenho 5 dígitos. Tenho um traço, e tenho a mesma coisa só que agora com 4 dígitos. Então tem um número de 0 a 9, só que agora com 4 dígitos. Pronto, criamos nosso modelo modelo = ‘[0-9]{2} [0-9]{5}-[0-9]{4} ´

[03:54] Olha só, temos o DDD, 2 dígitos e um espaço, 5 dígitos, o traço, e depois os 4 dígitos. Criei meu modelo e agora quero verificar se o número do celular que vai entrar nessa função corresponde a esse modelo que criamos, então vou chamar isso de resposta.

[04:17] E essa resposta vai ser assim, existe uma função que vai verificar se o número do celular corresponde a esse modelo. Essa função se chamar re.findall e entre parênteses eu preciso passar o modelo e preciso passar o número de celular, então resposta = re.findall(modelo, numero_celular).

[04:41] Agora a partir disso eu consigo verificar se o meu modelo em reposta = re.findall(modelo, numero_celular) corresponde a esse número de celular em celular_valido(numero_celular), se o número do celular se enquadra nesse modelo que eu criei. A única coisa que eu preciso fazer é retornar a resposta, então return resposta.

[04:59] Vamos no nosso código e importar essa nossa verificação de celular válida. Salvei o validators.py . Vou voltar para o meu serializer e antes de retornarmos o dado vamos verificar se o celular nessa nossa função é válido, passando o número de celular através do data if celular_valido(data[‘celular’]).

[05:26] Então vamos verificar, se o número do celular for um número válido, o que queremos fazer? Se esse modelo for verdadeiro ele vai retornar para nós um True, e se ele retornar um True ele vai entrar na nossa função e não é isso que queremos. Então iremos inverter, se o número de celular não for válido, queremos exibir a mensagem de erro, então no lugar de ´if celular_valido´ , vamos colocar if not celular_valido.

[05:47] Copiei a mensagem de erro, então precisamos entre chaves quando abrimos o ValidationError indicar o campo que queremos utilizar para fazer essa validação, que é o celular, dois pontos, a nossa mensagem e fecha chaves, ficando raise serializers.ValidationError({‘celular’:”O celular deve ter 11 dígitos”}).

[06:05] Vamos fazer essa verificação? O que eu vou fazer? Vou colocar um número de RG válido, e vou colocar um número de celular inválido, então 1112345-12345. Se eu der um post observe que aparece “O celular deve ter 11 dígitos” .

[06:28] Na verdade precisamos melhorar essa nossa mensagem de erro, então podemos expressar essa mensagem de erro como, por exemplo, “o número do celular deve seguir esse padrão”.. Então posso deixar assim “O número de celular deve seguir este modelo: 11 91234-1234. ”

[07:12] E podemos dar uma explicação, de “deve ter dois dígitos, um espaço” vai do nosso cuidado em passar essa mensagem para quem está utilizando a nossa API.

[07:28] Então por enquanto acho que assim está suficiente. Posso até colocar por exemplo, aqui na nossa função, “respeitando os espaços e traço.”

[08:59] Bom, se vamos lá e damos um post de novo, aparece em vermelho a mensagem que criamos de “O número do celular deve seguir este modelo: 11 91234-1234, respeitando os espaços e traço.” Respeitando acho que podemos até deixar entre parênteses, acho que já está suficiente, dá para entendermos como devemos criar esse nosso modelo de celular.

[08:24] Bom, o que eu quero fazer agora é criar um número de celular válido. Então vou criar um DDD 15 91234-1234, e vou marcar embaixo que Gustavo é um cliente ativo. Quando dou um post, conseguimos cadastrar o Gustavo com o número de celular com este modelo também.

### Importando validações
Validação de documentos brasileiros (validate_docbr)

[Documentação]('https://pypi.org/project/validate-docbr/')

    pip install validate-docbr

---

[00:00] Inserimos validações nos campos do CPF, do nome válido, do RG, e do celular. Porém, se formos na validação que verifica se o CPF é válido no nosso arquivo “validators.py” , observe o que fazemos. Só verificamos se o CPF não tem 11 dígitos, e isso não está legal. Porque se observarmos o CPF que conseguimos cadastrar, onze números 1, depois 12345123451. Onze dígitos mas esse CPF não é válido.

[00:31] Se digitarmos “CPF” e der um “enter” e abrir a página no Wikipedia vamos ver que existe uma regra para os números do CPF, para os dígitos, e tem até um algoritmo que poderíamos implementar isso na mão.

[00:45] Mas se pararmos para pensar um cadastro de cliente e um cadastro com o campo CPF é algo comum em muitos sistemas, então outros desenvolvedores e desenvolvedoras já passaram por esse problema, já tiveram que implementar essa solução do cadastro de CPF para verificar se o CPF é válido, e tem aqui todo o algoritmo. Se você entra na página do Wikipedia você vai conseguir ver detalhes de como é a implementação dos dígitos do CPF.

[01:12] Então o que vamos fazer? Vamos ter que criar essa implementação do zero? Não, existe uma biblioteca onde podemos incorporar ao nosso projeto e pedir para que ela faça as verificações. Vou deixar a aba do Wikipedia aberta, e acessando ela temos todo o formato do CPF, como ele é feito, como são gerado os dígitos verificadores e o algoritmo dele.

[01:42] Existe uma biblioteca chamada “validate_docbr” e quando pesquisamos no Google, o primeiro link da nossa pesquisa é a biblioteca que vamos utilizar. Vou clicar no link e temos a forma como instalamos esse módulo, então ele fala “Um pacote do Python para validação de documentos brasileiros”. Então com esse pacote podemos fazer a validação do CPF, CNH, CNPJ e vários outros documentos. Para o nosso caso precisamos só da validação do CPF.

[02:25] Então ele fala quais são os métodos para utilizarmos e como utilizamos esse pacote no nosso projeto. O que vamos fazer? Primeira coisa, para instalar o projeto eu vou copiar pip install validate-docbr. Lá no nosso projeto, vou abrir meu terminal, parar meu servidor e vou rodar aquele código dando um “Ctrl + V” , o validate-docbr.

[02:59] Vou dar um “enter” e ele vai instalar. Disse que a instalação foi concluida com sucesso então vou subir meu servidor de novo manage.py runserver. E o que ele fala? Ele fala “agora você vai importar do validate_docbr, importar o CPF, criar uma instância do CPF e depois para validar você pode fazer cpf.validate e passa o número do CPF”.

[03:29] Toda essa lógica do CPF podemos inserir onde? No nosso código de “validators.py”. Então já temos o import das expressões regulares, que vamos criar e vou colocar o import também do validate_docbr . A instância cpf = CPF() não vou deixá-la do lado de fora, vou dar “Ctrl + X” nela e vou colocar ela dentro do cpf_valido(numero_do_cpf) , quando formos validar o CPF.

[03:56] Então temos a instância do CPF e depois só perguntamos se o CPF é válido, passando o número do CPF. Então vou perguntar se o CPF é válido, e ao invés de passar o número “012.345.678-90” dentro do ´cpf.validate´ vou passar o número do cpf, ficando cpf.validate(numero_do_cpf).

[04:13] E eu não quero retorno para saber se só tem 11 caracteres, eu quero retorno dessa condição do cpf.validate(numero_do_cpf). Então vou colocar ela para baixo no return return cpf.validate(numero_do_cpf) e vou voltar.

[04:23] O que fizemos aqui agora? Importamos o validate_docbr, criamos a instância do CPF e falou assim “CPF, validate, valida para mim esse número de CPF” e ele vai retornar um verdadeiro ou falso.

[04:41] Para conseguirmos cadastrar um número de CPF válido existe um site na internet que gera números de CPF para testarmos, para nós que somos desenvolvedores ou desenvolvedoras testar.

[04:52] Então na aba de pesquisa podemos colocar “gerador de CPF” e clicar no primeiro link onde está escrito “Gerador de CPF - 4Devs” e vou pedir para gerar um CPF. Vou utilizar o CPF gerado e copiar o CPF com “Ctrl+C”. Eu não vou utilizar no nosso projeto traços para o CPF, se observamos no ´validate br´ existe uma forma de conseguirmos criar uma máscara para ele.

[05:22] Ele fala assim: "O CPF foi gerado assim, mas podemos gerar ele com uma máscara utilizando esse parâmetro ́cpf.generate(True) ´”. Eu não vou utilizar isso, não vamos investir mais tempo nessa validação da máscara mas está bem tranquilo, a documentação está bem legal e conseguimos gerar.

[05:40] Então o que eu vou fazer? Subi meu servidor e lá na nossa aplicação eu vou criar mais uma pessoa, que vai ser a Ana. O e-mail dela vai ser ana@alura.com, o CPF dela eu vou colocar o número de CPF 40532778090 que geramos no site visto anteriormente só que vou tirar os traços. O RG vou colocar 123451234, 9 dígitos, e o celular vou colocar 11 91234-1234. Vou marcar que Ana é uma pessoa ativa.

[06:15] Esse número de CPF é um número de CPF válido. Eu vou inverter. Vou dar um “Ctrl + C” no número do CPF e vou colocar um CPF inválido 2222222222. Quando eu der um post olhe o que ele vai falar: “ O CPF deve ter 11 dígitos” .

[06:33] Aqui está um pouco estranho, porque temos 11 dígitos, essa não é a mensagem correta. Poderíamos dizer apenas: “CPF invalido”. Então lá no nosso serializers.py vamos mudar nossa mensagem de erro.

[06:45] Então em serializers.ValidationError vamos colocar serializers.ValidationError({‘cpf’: “Número de CPF inválido”}). Salvei, e se volto na aplicação e dou um post outra vez, ainda com o CPF inválido 2222222222, aparece a mensagem de erro “Número de CPF inválido”.

[07:07] O que vou fazer? Vou colocar aquele número que copiamos, que usamos do gerador de CPF, e quando dou um post temos lá o cadastro da Ana com um número de CPF agora válido. Não apenas com 11 dígitos, mas seguindo todas as regras nacionais, dos padrões nacionais.

[07:25] Então dessa forma aprendemos como podemos incorporar outras validações, outras soluções que outras pessoas criaram aqui no nosso código. E observe como nosso código ficou organizado, temos o validate_docbr só na parte da lógica da validação em “validators.py” e no “serializers.py” só perguntamos se o CPF não for válido, damos uma mensagem de erro.

### Script para gerar clientes

    import os, django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
    django.setup()

    from faker import Faker
    from validate_docbr import CPF
    import random
    from clientes.models import Cliente

    def criando_pessoas(quantidade_de_pessoas):
        fake = Faker('pt_BR')
        Faker.seed(10)
        for _ in range(quantidade_de_pessoas):
            cpf = CPF()
            nome = fake.name()
            email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
            email = email.replace(' ', '')
            cpf = cpf.generate()
            rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
            celular = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
            ativo = random.choice([True, False])
            p = Cliente(nome=nome, email=email, cpf=cpf, rg=rg, celular=celular, ativo=ativo)
            p.save()

    criando_pessoas(50)

### Populando banco de dados
Biblioteca Faker: auxília na criação de dados para popular o banco de dados.

[Documentação]('https://faker.readthedocs.io/en/master/')

    pip install Faker

    from faker impor Faker

---

[00:00] Incluímos a validação do CPF e ficou bem legal. Só que na minha base de dados eu já tinha alguns clientes cadastrados, como o Guilherme e o Gustavo, que o CPF contém um valor inválido, contém dígitos inválidos.

[00:14] E o que eu gostaria de fazer? Queria criar uma série de clientes. Quero criar uma forma de gerar vários clientes com base nos dados que já geramos e validações que já incluímos na nossa aplicação.

[00:29] Por exemplo, quero que o CPF seja um número de CPF válido para esse cliente. Quero que seja um nome válido, quero que o RG tenha 9 dígitos, e quero que o celular tenha esse modelo que inserimos.

[00:41] Mas como vamos criar esses clientes na nossa base de dados? A primeira coisa que vamos fazer é, se observamos, o cadastro da Ana está correto, tem o nome Ana, e-mail da Ana, o CPF é um CPF válido.

[00:55] O RG não vamos nos preocupar com a regra porque cada estado do Brasil tem uma regra específica para o RG, então não tem como vincularmos uma regra geral. Por isso no RG vamos deixar com que tenha 9 dígitos mesmo e no celular queremos usar essa máscara.

[01:12] Como que vou gerar esses clientes? Para começar, vou deletar o cliente Gustavo e Guilherme na aba de Administração do Django. Vou selecionar o nome deles, selecionar a Ação “Remover clientes selecionados” e clicar em “Ir”, e depois “Sim, eu tenho certeza” .

[01:32] Agora que deletei esses clientes, na atividade anterior a esse vídeo, temos um link onde mostra um script escrito em Python para gerarmos clientes na nossa base de dados. E o script é esse, você também terá acesso a ele.

[01:48] Então vamos criar um arquivo na nossa aplicação chamado populate_script.py , vamos colar esse script e gerar uma série de pessoas e vamos entender um pouco melhor como esse script foi criado.

[02:06] Então vou copiar todos os dados do script com “Ctrl + C” e na nossa aplicação observe que temos nosso app de clientes, setup, e vou criar um novo arquivo em “PROJETO_CLIENTES”. Vou clicar no ícone de adicionar do lado direito de “PROJETO_CLIENTES” ,opção “New File”, e não de pasta, e vou criar um arquivo chamado “populate_script.py” .

[02:36] Dentro deste arquivo eu vou dar um “Ctrl+V” e vamos entender o que tem nesse arquivo. Primeira coisa, ele faz o import do ´django´ e do ambiente virtual do ´django´, e do setup de desenvolvimento do Django para conseguirmos acessar nosso projeto. E tem também uma instância do ´django.setup() ´.

[03:01] Depois temos uma biblioteca chamada faker, from faker import Faker e essa biblioteca não temos na nossa aplicação, vamos precisar instalar essa biblioteca para que esse código, esse script, que vai gerar nossos clientes, sejam gerados.

[03:18] Então se formos na internet e digitarmos na busca “faker django”, clicando no primeiro link da pesquisa “Welcome to Faker’s documentation! - Faker 4.1.1… “ observe que temos aqui uma instalação básica dele que é o pip install Faker.

[03:39] Vou copiar o pip install Faker e no nosso código em populate_script.py vou abrir no nosso terminal e vou dar um “Ctrl + C” para parar. “Ctrl + V” pip install faker e instalou. Subi no nosso servidor mais uma vez ´manage.py runserver´ e agora já temos o faker instalado na nossa aplicação.

[04:01] O validate_docbr já tínhamos instalado e ele tem um import do random, o import random e já traz também um modelo de cliente from clientes.models import Cliente .

[04:09] Tudo isso é possível porque utilizamos essas duas linhas, a linha 3 e 4, que constam os.environ.setdefault(‘DJANGO_SETTING_MODULE’, ‘setup.settings’) e django.setup(), onde dizemos que vamos utilizar as configurações do nosso projeto de setup e diz também qual a instância do ´django setup´.

[04:25] O que esse script vai fazer? Existe uma função nesse script chamado “criando pessoas”, onde vamos passar o valor da quantidade de pessoas que queremos criar. Temos a instancia do faker para o português Brasil, porque se não setar essa propriedade, ele vai gerar com nomes em inglês, ou se eu setar estiver com outros nomes também ele pode gerar com nomes italianos, japonês, e várias outras possibilidades.

[04:53] Lembrando que isso estamos utilizando para teste. Então vamos setar com a localização em português. Esse ´Faker.seed(10)´ o que vai acontecer? Quando definirmos o ´seed´ ele vai gerar a mesma sequência de nome para mim. Então quando rodarmos essa aplicação ele vai gerar os mesmos nomes para mim e vai gerar os nomes para você também.

[05:13] E aqui temos um for como for _ in range(quantidade de pessoas) onde temos dentro uma instância do CPF cpf = CPF() e pedimos para ele gerar um nome fake nome = fake.name() . Temos um email que vai ser gerado com base nesse nome, então vamos pegar o nome da pessoa e vai colocar no primeiro espaço entre chaves, depois vai ter um arroba, depois vamos ter fake.free_email_domain()) que vai ser gmail, yahoo, e outros e-mails gratuitos, domínios gratuitos, e vamos gerar esse e-mail.

[05:40] Depois vamos pedir para o nosso CPF do docbr gerar para nós o número do CPF válido e depois vamos gerar um RG com aquela formatação que já temos, com os números certos. Também vamos gerar o número do celular utilizando aquele formato que já tínhamos, dois dígitos, o 9, depois quatro dígitos celular = “{} 9{}-{}.

[06:05] E vai ter um random choice ficando ativo = random.choice([True, False]) para deixarmos a nossa aplicação escolher se esse cliente vai ser um cliente ativo ou não, se vai ser true ou false para esse nosso cliente. Para ver se ele está ativo.

[06:19] Vamos falar que “p” vai ser a instância desse cliente passando todas essas propriedades p = Cliente(nome=nome, email=email, cpf=cpf, rg=rg, celular=celular, ativo=ativo) . Então vamos ter um cliente com nome, que geramos em cima em nome = fake.name(), e-mail e depois configurar todas essas variáveis.

[06:33] Salvamos este cliente. Se esse código for executado com sucesso temos a mensagem de print (‘Sucesso!’) e em criando_pessoas(50) estamos executando essa função criando 50 pessoas.

[06:46] No início eu considero que seja muito interessante e válido para conseguirmos dar continuidade que você crie também com 50 pessoas a execução desse script.

[06:59] Vamos executar esse script e gerar essas pessoas? Se eu for no meu código e atualizar minha lista de clientes eu só tenho a Ana, vamos gerar então 50 pessoas, 50 clientes para a nossa base de dados.

[07:11] Abrindo meu terminal eu vou abrir uma janela clicando no ícone no canto direito com um sinal de “mais”. Observe que já estou com a minha venv e é muito importante sempre validarmos isso. Vou pedir para o ´python´ executar esse script, então vou dizer: “Python executa para mim esse script population_script.p. Então vou colocar python populate_script.py.

[07:36] Quando dou um enter observe que ele vai pensar um pouco e mandou uma mensagem de “Sucesso!”. Se dou um “Ctrl + J” é a mensagem de Sucesso depois que executamos a nossa função que vai gerar essas pessoas.

[07:50] Se eu volto no meu código e atualizo, observa que agora eu tenho muitos nomes, tenho Ana, Isabel, Mirella, Emanuella, a senhorita Olivia Melo e vários outros nomes que foram gerados com base nas validações que já criamos.

[08:06] Mas Guilherme, por que eu estou gerando todos esses nomes? Porque mais para a frente vamos aprender a criar filtros, a incluir paginação na nossa API, vamos aprender como verificar se já temos um CPF cadastrado ou não.

[08:25] Então aqui eu tenho “localhost:8000/clientes” , se eu coloco o ID 10 “localhost:8000/clientes/10” ele vai me mostrar o Luiz Otávio que é nosso cliente 10. Só que ele tem o CPF aqui, eu quero conseguir buscar um cliente por CPF, e se fossemos criar todos os clientes na mão íamos demorar muito tempo. Por isso, disponibilizamos esse script para popular nossa base de dados e assim dar continuidade na nossa aplicação.

[08:50] Na sequência vamos ver como gerar filtros. Eu quero todos os clientes que são ativos, ou todos os clientes que não estão ativados, que estão desativados na minha API, ou eu quero verificar se esse RG está cadastrado, ou seja, se já é um cliente cadastrado aqui na nossa aplicação. Tudo isso vamos ver na sequência.

### Exercício: Dividir para conquistar

Como vimos na aula, podemos utilizar expressões regulares, importar bibliotecas de validação ou criar nossas próprias validações.

Porém, qual a vantagem(ou vantagens) de remover a lógica de validação do serializer e manter em outro arquivo?.

a) **Alternativa correta:** Melhora a legibilidade do código para outros desenvolvedores.
- _Alternativa correta! Certo! Com o código dividido em partes, a compreensão e entendimento por parte de outras pessoas será facilitada._

b) Carregamento mais rápido da API.

c) **Alternativa correta:** Facilite a edição e manutenção do código.
- _Alternativa correta! Certo! Com um arquivo mantendo apenas a lógica das validações, facilitamos a atualização ou edição das validações sem incrementar muitas linhas de código no serializer._

### O que aprendemos?

- Aprendemos como validar os campos da API utilizando expressões regulares;
- Vimos que é possível importar outras bibliotecas de validação para utilizar no nosso projeto;
- Executamos um script para criar vários clientes de uma só vez em nossa base de dados.

## 4. Paginação, ordenação, busca e filtro
### Paginação
Paginação enviar os dados seguiemntados.

[Documentação]('https://www.django-rest-framework.org/api-guide/pagination/')

Adicionamos no SETTINGS.PY:

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 100
    }

---

[00:00] Incluímos o script, que cria vários clientes na nossa base de dados, e isso ficou bem legal. Porém, precisamos pensar na usabilidade da nossa API porque com todas as requisições para “localhost8000/clientes” o que vai acontecer? A outra aplicação vai ver o nosso código assim.

[00:17] Estamos jogando todos os clientes de uma só vez, que temos na nossa base de dados, para ele. E no lugar de respondermos essa requisição listando todos os clientes de uma só vez, por que não incluímos uma paginação, algo semelhante ao que temos no nosso “Django Admin”?

[00:33] Observe que vou para a página 1, tenho 10 clientes, vou para a página 2, tenho 10 clientes. É muito mais fácil de conseguir navegar entre essas páginas. E observe que cada página que eu mudo, ele muda também na url. Se estou na página 2, aparece “localhost:8000/admin/clientes/cliente/?p=2” .

[00:49] Isso já está no “Django Admin”, já veio nele. Como? Se acessarmos nosso projeto_clientes apertando “Ctrl + P” e digitar “admin” e acessar o “admin.py clientes”, observe que temos essa configuração list_per_page = 10 .Ou seja, em cada página eu quero exibir 10 clientes.

[01:05] Por que não fazemos isso e incluímos isso na nossa API no lugar de exibir todos os clientes de uma só vez? Vamos fazer isso?

[01:12] Para fazer isso vou pesquisar na internet “django rest pagination” e nesse primeiro link temos “Pagination - Django REST framework” . Vamos clicar e ao abrir temos uma explicação bem passo a passo de como funciona a paginação nos modelos, nas views diferentes, views genéricas e views sets.

[01:38] Que é o que estamos utilizando, e ele fala: “Para utilizarmos a paginação existe uma paginação default onde vamos definir qual a quantidade de clientes que eu quero exibir por página.

[01:54] E conseguimos colocar essa paginação como? Só irmos no nosso settings.py criando a variável REST_FRAMEWORK = { ‘DEFAULT_PAGINATION_CLASS’ : rest_framework.pagination.limitOffsetPagination’, ‘PAGE SIZE’ : 100 e definimos quantos clientes queremos exibir por página.

[02:16] Vou copiar esse código com “Ctrl + C” , vou abrir meu “settings.py”, lembrando que “Ctrl + P” eu abro a janela na parte superior do programa e posso digitar ´settings.py´ e embaixo vou dar um “Ctrl + V” e vou salvar.

[02:35] Só que não quero exibir 100 por página, no caso do nosso Admin, estamos exibindo 10 por páginas, então vamos colocar 10 e vamos testando até achar um número que melhore a usabilidade da nossa API também.

[02:49] Então PAGE_SIZE’ : 10. E o que precisamos fazer agora? Precisamos testar nossa API. Então vou voltar na nossa API e atualizar e observe que já temos uma paginação, já foi incluída essa paginação. Como ficou a rota de clientes? Se clicarmos na seta do lado direito do ícone GET em azul, e selecionando “json”.

[03:17] Observe que ele já fala, temos 51 cadastros, temos o ´localhost 8000´ e depois passamos não todos os clientes de uma vez, mas esses primeiros cadastros, dos primeiros 10 clientes que queremos exibir.

[03:32] Mas e se eu quiser exibir da página 2? Quando eu clico na página 2 ele aparece como "localhost:8000/clientes/?offset = 10” e isso significa que estamos exibindo os outros 10, só que eu queria exibir a paginação assim, igual temos no “Django Admin”.

[03:46] Então o que vamos fazer? Vamos alterar essa propriedade que colocamos anteriormente dentro do nosso ´settings.py ´. Ao invés de ser ´pagination.LimitOffsetPagination´, vamos colocar ´pagination.PageNumberPagination’ . “P” maiúsculo no Page, o Number com “N” maiúsculo, e o Pagination igual tava antes.

[04:14] Quando eu salvar, observe o que vai acontecer aqui nessa propriedade do ´offset´ . Vou tirar ele, dar um “enter” só em “localhost:8000/clientes/ “ e temos aqui o ‘ “count”: 51’ , ele contou 51 clientes cadastrados. Se vou para a página 2, e temos “localhost:8000/?page=2”. Muito melhor. Quando vamos para a página 3, temos “localhost:8000/?page=3” e assim exibimos melhor.

[04:38] Vou lá testar clicando novamente na seta do lado direito do ícone GET em azul, selecionando ´json´ e observe que estamos exibindo só os clientes da página 3, ele está falando que tem outras páginas e está mostrando detalhes dos clientes da página 3. E temos página 4, página 5.

[04:58] Para testarmos vou no nosso “Django Admin” e vou colocar na página 1. Ele está listando o nosso cliente Pedro Henrique. Se viermos na janela da nossa API, colocar na página 1, ele está listando a Ana, porque está ao contrário. Então se eu for para a última página ele vai me mostrar aquele cliente Pedro Henrique. Com o mesmo CPF também.

[05:28] Se vou para a página 5 na API temos a Pietra, e na página 2 do nosso Administração Django, o que seria nossa página 5, está a Pietra também. O admin está ao contrário porque ele está listando com os últimos ID’s , e na nossa API estamos listando através dos primeiros ID’S. Então ID 5, 6, 7, 8, e assim por diante.

[05:52] Incluímos a paginação na nossa API, ficou muito mais fácil navegar, podemos escolher se 10 clientes por página é pouco e quero exibir mais, posso colocar 25 PAGE_SIZE: 25 no meu settings.py e salvar. Na minha API quantas páginas eu tenho? Vou ter 3 páginas, porque eu tenho 51 clientes.

[06:13] Na página 3 vou ter só o Pedro Henrique, na página 2, 25 clientes, e na página 1, 25 clientes. Então fica ao seu critério escolher quantos clientes, qual a necessidade da sua API de exibir uma quantidade específica de clientes.

### Ordenação
DJANGO-FILTER-BACKEND: [Documentação]('https://www.django-rest-framework.org/api-guide/filtering/')


    pip install django-filter

Adicionar no SETTINGS.PY:

    INSTALLED_APPS = [
        'django-filters',
        ...
    ]

Adicionar no VIEWS.PY do app:

    from rest_framework import viewsets, filters
    from django_filters.rest_framework impor DjangoFilterBackend

    class ClieentesViewSet(viewsets.ModelViewSet):
        queryset = Cliente.objects.all()
        serializer_class = ClienteSerializer
        filter_backends = [DjangoFilterBackend, filters.OrderingFilter] #
        ordering_fields = ['nome'] #

---

[00:00] Incluímos a paginação na nossa API, isso ficou bem legal, só que algo está diferente na nossa aplicação. Se observarmos a nossa API, nós listamos sempre os nossos clientes com uma ordenação através do ID de forma ascendente. Então temos o 5, 6, 7, 8 e assim por diante.

[00:17] Porém, lá no nosso “Django Admin”, essa ordenação está ao contrário, ela está de forma descendente através do ID e eu não queria uma ordenação pelo ID, eu queria uma ordenação pelo nome para exibirmos os nomes das pessoas de forma ordenada, ia ficar muito mais fácil para conseguirmos navegar.

[00:35] Então vamos começar pelo admin do Django, eu quero listar isso por nome. Lá no nosso código vou apertar “Ctrl + P” e vou digitar “admin” e vai aparecer admin.py clientes. Acessando ele existe uma propriedade que podemos passar para nossa classe de clientes, que se chama ordering .

[00:55] Vou falar que ordering = (‘nome’,) e vou colocar uma vírgula depois que fechei as aspas. Salvei e voltando no nosso “Django Admin”, assim eu que atualizo, observe que já temos a ordenação por nome, não mais pelo ID. Então tem Alexandre, Ana, Ana Beatriz Fogaça e Ana Beatriz Ribeiro, Ana Costa, e ficou legal.

[01:17] Incluímos aqui a ordenação e podemos ver que está certinho em ordem alfabética. O que eu quero fazer agora? Essa mesma ordenação que eu passei para o meu admin, eu quero passar também para a minha API, quero que minha API tenha essa ordenação por nome.

[01:34] Então se pesquisarmos na internet digitando “django rest filter” e clicarmos no primeiro link escrito “Filtering - Django REST framework” da própria documentação, podemos ver que existe uma forma de conseguirmos alterar os dados, a exibição dos nossos dados.

[01:53] E se rolarmos a página para baixo, temos a forma de incluir busca e ordenação e é o que queremos, queremos incluir ordenação na nossa aplicação, na nossa API. E descendo mais a página, em API Guide, temos o “DjangoFilterBackend”. Ele fala que é uma biblioteca, que suporta algumas customizações de campo, que vamos incluir na nossa aplicação.

[02:18] Então para usar esse DjangoFilterBackend precisamos instalar através do pip install django-filter e depois temos que adicionar o django-filter lá no nosso app instalado.

[02:32] Só tem um detalhe que vale a pena tomarmos cuidado é que quando vamos instalar, o pip install django-filter está no singular, porém quando vai adicionar no nosso app instalado, é django_filters no plural.

[02:45] Então vamos fazer em partes. Vou instalar essa biblioteca. Lá no meu servidor vou parar o meu servidor “Ctrl + C”, limpei minha tela “Ctrl + V”, e adicionei pip install django-filter no singular, dei um enter e ele instalou. A instalação foi feita com sucesso.

[03:04] Legal, limpei minha tela e vou habilitar mais uma vez nosso servidor python manage.py runserver. Voltando lá, precisamos adicionar o django_filters lá nos nossos apps instalados.

[03:17] Então, o que vou fazer? Vou minimizar meu servidor, meu terminal, vou apertar “Ctrl + P” e vou digitar “settings” e vai aparecer settings.py setup . Dentro dele, lá nos nossos apps instalados, o INSTALLED_APPS vamos dar um enter e colocar django_filters, no plural e com uma vírgula.

[03:37] Salvei e pronto. Agora já temos o django filters instalado na nossa aplicação. Claro que se formos na nossa aplicação e executamos, nada está acontecendo, tudo está como estava antes. Porque precisamos passar para quem é responsável por criar essa página, criar os dados, qual é o “Core Set” que estamos utilizando, qual a classe serializer.

[03:57] Ou seja, precisamos ir no nosso arquivo de view e dizer para a nossa view: “View, essa lista de clientes possui uma ordenção”. E é isso que vamos fazer agora.

[04:06] Vou fechar as abas de admin.py e settings.py para não ficarmos confusos, e vou abrir views.py. Acessando nossa view observe que temos algumas propriedades, que passamos algumas variáveis que criamos aqui e ela faz toda a mágica para nós.

[04:20] O que quero fazer agora? Quero trazer lá do nosso rest_framework um cara chamado filters. Então from rest_framework import viewsets, filters. Maravilha. O que eu preciso fazer? Vamos usar o filters e vamos usar a biblioteca que acabamos de instalar na nossa aplicação.

[04:41] Então, lá do django_filters no plural, queremos importar o DjangoFilterBackend, no singular, então vamos colocar from django_filters.rest_framework import DjangoFilterBackend. Vou salvar esse arquivo, e vamos entender a diferença do DjangoFilterBackend para o filters.

[05:16] Vamos lá, o que precisamos fazer? A primeira coisa é preparar o nosso Backend para que possamos incluir as ordenações, temos que falar “Olha, existem filtros nos campos que nós queremos criar”.

[05:30] A primeira coisa que faremos vai ser falar: “Vai criar uma variável chamada filter_backends agora no plural”. É um pouco confuso essa parte de uma hora está no singular e outra hora está no plural, mas conforme formos criando e testando outras API’s e for escrevendo outros códigos nós acostumamos.

[05:55] Então filter_backends = [ ] e dentro dele eu vou falar que ele vai ser uma propriedade no DjangoFilterBackend, e quero utilizar uma ordenação, e essa ordenação vamos usar do filters , então vai ser filters.OrderingFilter.

[06:14] Olha o que fizemos, criamos uma variável chamada filter_backends no plural, e dentro dela falamos que vamos utilizar o DjangoFilter para que possamos ver a ordenação acontecer na API, e quem vai ser responsável vai ser alguém de filters.Ordering. filter_backends = [DjangoFilterBackend, filters.OrderingFilter].

[06:33] Criamos esses dois e a última coisa que precisamos fazer agora é criar uma variável chamada ordering_fields no plural, e dentro eu vou passar nome porque eu quero ordenar por nome, então ordering_fields = [‘nome’]. Salvei.

[06:54] Assim que voltamos na nossa aplicação e atualizamos, aparece uma propriedade chamada “Filtra”. Quando eu clico nela, aparece uma janela onde temos “Ordenado”, e as opções “nome - ascendente” e “nome - descendente” . Se eu coloco o “nome - ascendente” nós temos o Alexandre, a Ana, a Ana Beatriz.

[07:12] Lá no nosso ““Django Admin”” também temos o Alexandre, a Ana, e a Ana Beatriz. Conseguimos incluir então a ordenação na nossa aplicação.

### Busca e filtro
Utilizando a mesma documentação anterior no VIEWS.PY:

    class ClieentesViewSet(viewsets.ModelViewSet):
        queryset = Cliente.objects.all()
        serializer_class = ClienteSerializer
        filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter] #
        ordering_fields = ['nome']
        search_fields = ['nome','cpf',] #
        filterset_fields = ['ativo']
        
---

[00:00] Já incluímos a ordenação, aqui apareceu essa propriedade do filtro com “nome - ascendente” e “nome - descendente” no nome, e aparece na nossa url o “localhost:8000/clientes/?ordering=nome”.

[00:12] Através disso conseguimos disponibilizar para outros sistemas que forem consumir nossa API essa ordenação para facilitar o uso da nossa lista de clientes.

[00:22] Porém algo está um pouco difícil de entender. Vamos supor que eu precise pesquisar um determinado cliente por CPF. Como faço isso? Ou eu preciso visualizar todos os clientes que estão ativos.

[00:33] Isso vai ficar muito difícil, por mais que eu tenha essa paginação, eu teria que olhar cliente a cliente para saber se eles estão ordenados ou não. E isso não está muito fácil.

[00:43] Se observamos lá no nosso “Django Admin”, existe um filtro que podemos colocar para todos os clientes ativos quando clicamos no ícone Filtro e selecionamos o “sim” , ou quando colocamos “não”, todos os clientes que não estão ativos na nossa aplicação. E isso é bem legal.

[00:57] Além disso, temos também o campo de busca. Se eu digito, por exemplo, Ana e clico em pesquisar, observe que aparece a Ana Beatriz Ribeiro.

[01:05] Conseguimos visualizar clientes com o nome de Ana, e se eu for no ícone “FILTRO” e selecionar a opção “todos”, olha que interessante.

[01:12] Ele vai me trazer a Ana, a Ana Beatriz Fogaça, a Ana Beatriz Ribeiro, Ana Costa, Ana Lívia, Joana, por causa do “Ana” e Mariana por causa do “Ana” que aparece também.

[01:23] Isso é muito legal pois vai facilitar para as pessoas que estiverem mexendo na nossa API, consumindo a nossa API. Eu quero visualizar se esse cliente já está cadastrado ou não. Só com o nome já conseguimos visualizar, ou através do número de CPF também.

[01:38] O que eu quero fazer? Vamos começar criando esse campo de busca e depois criando esse filtro para conseguirmos visualizar os clientes que estão ativos, e os clientes que não estão ativos, e realizar também uma busca por nome ou CPF.

[01:53] Para começar, se observamos lá na documentação do Django Filter, temos uma propriedade chamada SearchFilter. E observe que a única coisa que vamos precisa fazer é o import do filter, que já fizemos, que já estamos utilizando.

[02:10] E depois lá no nosso filter_backends vamos dizer que vamos ter um filtro de busca, um filters_Searchfilter dessa própria lib que importamos. Depois, vamos especificar com search_fields quais campos queremos disponibilizar para essa busca.

[02:27] Lá no nosso código, em views.py, a primeira coisa que vamos fazer é, já temos os filters instalados, do rest_framework. Vou colocar uma vírgula e vamos ter de filters no plural filters.SearchFilter , ficando então filter_backends = [ DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter] .

[02:41] Agora o que precisamos fazer é indicar quais campos queremos buscar, então vou escrever search_fields = [‘nome’] e o nome do campo que queremos buscar, que no caso é o nome.

[02:55] Salvando, vou atualizar nossa API. Se eu vou no ícone filtra em branco no lado superior direito da nossa aplicação, observe que aparece um “Pesquisar”. Vou realizar a mesma busca que fiz no admin e escrever “Ana”.

[03:05] Se eu clicar em Search, observe que aparece aqui todos os nomes que contenham a “Ana”, a Ana Beatriz, Mariana, Joana, Ana Costa, Ana Lívia, e a Ana.

[03:15] Só que além do nome, eu quero realizar uma busca pelo CPF, então o que eu vou fazer? Quero visualizar todos os clientes. Vou escolher um determinado cliente, o Isaac Martins. Vou copiar o CPF dele e quero permitir que essa busca também receba um número de CPF.

[03:35] O que eu preciso fazer? Voltar lá em views.pye adicionar uma vírgula e cpf em search_fields = [‘nome’, ‘cpf’] . Então o nosso search_fields vai ser igual ao nome, vírgula, e ao CPF também, entre aspas. Então vamos permitir que consigamos realizar uma busca pelo nome e pelo CPF.

[03:51] Se eu volto na nossa aplicação, digito CPF do Isaac e dou um Search, observe que vai aparecer o cliente Isaac Martins. Como ficou o nosso endpoints? Como que outras pessoas vão conseguir realizar essas buscas?

[04:02] Temos na url localhost:8000/clientes/?search . Quero realizar uma busca, e essa busca vai permitir nomes ou os dígitos do CPF.

[04:15] Temos além da busca, além da ordenação, o que falta para deixarmos tanto nosso admin, quanto a nossa API igual, é o filtro por clientes ativos e não ativos. E para isso vamos precisar criar outra variável em views.py chamada filterset_fields .

[04:32] Então vou escrever filterset_fields = [‘ativo’] , ou seja, essa vai ser uma busca exata, eu quero que esses valores de verdadeiro ou falso sejam usados como filtro para exibir os meus clientes na base de dados.

[04:57] Observe que se eu atualizar a nossa aplicação, e for novamente no ícone “filtra” em branco no lado superior direito da nossa aplicação, vamos ter mais uma propriedade que é o “Filtra de campo”.

[05:05] Se eu colocar o filtra de campo como “Desconhecido”, e clicar em “Enviar”, observe que na url fica “localhost:8000/clientes/?ativo= “, ativo igual a nada, então posso até tirar o ?ativo= da *url * que vai dar na mesma.

[05:17] Ele então vai trazer clientes que não estão ativos e clientes que estão ativos na nossa API, verdadeiro e falso. Se eu coloco o “Filtra de campo” como “Ativo” e seleciono o “Sim” e dou um enviar, observe que no nosso endpoint vai ficar “localhost:8000/clientes/?ativo=true” e ele vai me trazer todos os clientes que são ativos. Observe que só temos true em toda a página.

[05:41] Agora se eu coloco na nossa url “localhost:8000/clientes/?ativo=false” e dou um enter, observe que ele vai mostrar todos os clientes que não estão ativos na nossa API. E se clicarmos em “Filtra” e olhar em “Filtra de campo”, a busca ficou com o ativo “não”.

[05:52] Conseguimos colocar uns clientes que não estão ativos ordenados de forma descendente, olha que coisa interessante. Aos poucos vamos começar a manipular melhor os dados da nossa API facilitando a usabilidade dela.

[06:06] Dessa forma permitimos que tanto o admin, como a nossa API, tenham essas mesmas buscas. Eu vou permitir também que o CPF esteja na busca do nosso admin. ]

[06:17] Se eu colocar um CPF na busca do nosso Administração Django e clicar em “Pesquisar”, não mostrou nada. Vamos alterar isso também?

[06:21] No nosso código vamos apertar “Ctrl + P” e vamos acessar nosso admin, digitando “admin.py clientes” e observe que em search_fields = (‘nome’) temos o nome. Vai ter também uma vírgula e entre aspas cpf, e vou colocar uma vírgula e salvar como search_fields = (‘nome’,’cpf’).

[06:38] Se eu vou em Administração Django e aperto em “pesquisar” mais uma vez, ele traz para mim o nome da Ana Beatriz. Então vou pesquisar um outro CPF para visualizarmos nos dois.

[06:45] Vou colocar o CPF do Joaquim Almeida, vou copiar esse número de CPF, colar na barra de pesquisa do Django Admin, e se clico em “Pesquisar” ele trouxe para mim o Joaquim Almeida.

[06:59] Se fizermos isso na nossa API, então temos todos esses dados, vou clicar em “Filtra” para pesquisar, no “Filtra de Campo” vou colocar o ativo como “Desconhecido” , nome ascendente mesmo, e para pesquisar vou colocar aquele CPF. Quando eu digito ele traz para nós o Joaquim Almeida.

[07:14] Padronizamos tanto o nosso admin e as funcionalidade que o admin nos dá, como a nossa API também.

### Exercício: Busca por RG

Uma pessoa seguiu todos os passos deste curso e resolveu mostrar a API para um amigo, porém não informou que a busca é feita com base nos campos nome e CPF, conforme ilustra o código abaixo:

    class ClientesViewSet(viewsets.ModelViewSet):
        """Listando todos os clientes"""
        queryset = Cliente.objects.all()
        serializer_class = ClienteSerializer
        filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
        ordering_fields = ['nome']
        search_fields = ['nome', 'cpf']
        filterset_fields = ['ativo']

Seu amigo realizou a requisição get, passando um número de RG:

    http://localhost:8000/clientes/?ordering=nome&search=541382893

Com base nesse exemplo, podemos afirmar que:

a) O Django Rest Framework fará a busca pelo RG, mesmo sem incluir o campo no search_fields, pois se trata do mesmo modelo.

b) Os dados de um cliente chamada Luiz Miguel Cardoso será exibido como resposta.
- _O cliente Luiz não será exibido no retorno desta requisição. Como a busca não é aplicada ao campo RG, o retorno desta requisição será:_

        { "count": 0, "next": null, "previous": null, "results": [] }.  

c) **Alternativa correta:** Nenhum cliente será exibido.
- _Alternativa correta! Certo! Com base no código acima, a busca é feita apenas nos campos nome e CPF. Para realizar a busca pelo RG e exibir o cliente Luiz, é necessário incluir o campo como ilustra o seguinte exemplo:_

        search_fields = ['nome', 'cpf', 'rg']

### O que aprendemos?

- Aprendemos como ordenar os campos da API de forma ascendente e descendente;
- Vimos como incluir paginação e filtros nos campos;
- Desenvolvemos a busca de clientes pelo número de CPF ou pelo nome.

## 5. Deploy
### Preparando o deploy
Deploy seria torna nossa aplicação on-line. No português "desdobramento em linhas". Transferir nosso código/script/aplicação para um servidor. \
[Documentação]('https://www.heroku.com/python')

No Heroku:
- Python >3.x
- Postgree l ocal
- Heroku CLI local


1. Clicar em: Create New App
    
    **App name:** drf-clientes \
    **Choose a region:** United States

2. Após criado o App, no Terminal HEROKU CLI:

    heroku login

---

[00:00] Nossa API ficou bem legal, temos um cadastro de clientes com todos os campos, validações, ordenação, buscas, pesquisa por filtro, ou seja, muita coisa bacana.

[00:12] Se somarmos o conteúdo do primeiro curso que aprendemos a criar os modelos, quais eram os arquivos necessários, os passos necessários do modelo para o serializer, para o view, para as nossas urls, ou seja, conseguimos criar bastante coisa. Temos bastante conteúdo visto.

[00:30] Só que no primeiro curso e nesse, se eu somo os dois conteúdos, a minha API só funciona local, ou seja, só o meu computador consegue fazer essa API funcionar e atender a essas requisições.

[00:43] E se pararmos para pensar, não é só isso. Toda vez que eu quero executar a minha API, o que eu preciso fazer? Subir minha venv, rodar o python manage.py runserver e aí sim minha API está funcionando e conseguimos cadastrar clientes e alterar, atualizar, deletar, várias outras ações também.

[01:03] O que eu quero propor agora é: vamos realizar um deploy dessa nossa aplicação de uma forma bem simples, não levando em conta todo o conteúdo denso que é o deploy.

[01:13] Com o deploy é necessário que pensemos em segurança, necessário que pensemos em escalabilidade e vários outros assuntos. Daria um curso só de deploy.

[01:22] Porém, eu quero mostrar que é possível realizarmos um deploy de maneira tranquila, um passo a passo bem claro entendendo o que estamos fazendo e sem precisar ter um custo por isso.

[01:35] Lembrando que o objetivo do nosso treinamento, deste curso, é preparar você para uma aplicação maior, uma aplicação que vai crescendo.

[01:45] Então a cada curso que temos aqui na Alura vamos aprofundando os nossos conhecimentos. Então vamos ver um passo bem simples de como realizar um deploy.

[01:54] Para começar, vamos fazer deploy no Heroku. Então vou pesquisar na internet “heroku” e se eu clico no primeiro resultado da pesquisa “Heroku: Cloud Application Plataform” ele fala que é uma plataforma para conseguir colocar nossa aplicação na nuvem.

[02:08] Observe que quando eu clico no Heroku eu já estou logado na minha conta. Caso você não esteja logado na sua conta, é só você criar uma conta. Vou sair da minha conta para você visualizar. Estou fazendo o log out.

[02:22] “Eu não tenho conta no Heroku, não tenho nenhum conteúdo no Heroku”, então você pode criar. Se você não tem conta, você pode clicar em “Sign up” embaixo da barra de Log In, ou no canto superior direito da página que vai aparecer também.

[02:34] E você vai colocar seu nome, seu email, a companhia que você trabalha, se você trabalha como estudante pode por que você é estudante ou algo desse tipo. Fala que você não é um robô e cria a sua conta.

[02:45] Se você já tem conta é só clicar para fazer o Log In, colocar suas credenciais e acessar a página do Heroku.

[02:54] Quando eu clico no Log In para realizar a minha conta, eu acesso alguns apps que eu já tenho ativo no Heroku e conseguimos realizar o deploy da nossa API de forma gratuita, sem precisar cadastrar cartão de crédito, sem cobranças por isso, pelas aplicações que vamos fazer.

[03:15] Então observa, vai ser um conteúdo simples mas muito eficaz. Vamos ter de fato nossa aplicação no ar.

[03:20] Primeira coisa que vamos fazer é: observe que estou utilizando aqui uma conta personal, eu não tenho um time cadastrado para realizar as alterações.

[03:31] Eu estou com uma conta pessoal, vou clicar no ícone “New” posicionado no canto superior direito da página e depois selecionar a opção “Create new app” .

[03:35] Esse app vou chamar de “drf-clientes”. Esse nome precisa ser único, então observe que , neste momento, esse nome está disponível.

[03:47] Você pode achar depois algum outro nome interessante para você, como “clientes”, “api de clientes”, alguma coisa assim que esteja disponível.

[03:54] A região vamos utilizar Estados Unidos mesmo, nossa aplicação vai ficar num servidor de lá, e vou clicar em “Create app” para criar o nosso app aqui no Heroku. Legal, criou o app, já temos um passo bem importante feito. Agora vou abrir uma outra aba e vou escrever “python heroku” na pesquisa.

[04:16] Quando eu abro essa aba, tem aqui no segundo link da pesquisa “Deploy and scale Python & Django in the cloud” no próprio site da Heroku. Vou clicar e quando abrir a página ele tem um vídeo mostrando como faz esse deploy, mas quero mostrar bem passo a passo para você.

[04:33] Então vou clicar no ícone em azul “VIEW THE DOCS” localizado no canto superior direito da página para visualizarmos as documentações e o que queremos é realizar o deploy de uma aplicação em Python utilizando o Django.

[04:44] Olhando para baixo temos o ícone roxo de “Get started with Python” , vou clicar nele para começarmos com uma aplicação em python.

[04:52] Então ele fala que a primeira coisa que precisamos ter para conseguir realizar um deploy é uma conta na Heroku, que já fizemos, e precisamos do python da versão 3.7 instalada local, e precisamos também do Postgres instalado local, essa é uma requisição importante.

[05:08] Porém, se você já realizou os cursos de Django lá da aplicação das receitas, você já tem o postgres instalado local, já tínhamos feito essa instalação. Então, como eu já tenho também o postgre instalado local, eu só vou clicar em “I’m ready to start”, que já estou pronto para começar. Lembrando que essa versão do python instalada local tem suporte para o Mac, Windows e Linux.

[05:31] Caso você não tenha o postgre, “Ah Guilherme, eu não vi os cursos do Django sem ser de API, de aplicações”. Então você pode clicar no link em cima “Postgres installed” e realizar o deploy, o download do postgre.

[05:50] Vou colocar na busca “postgres download” para vermos. Clicando no primeiro link temos o download do postgre, então no Linux, Mac, Windows e outros sistemas operacionais também. Vou fechar.

[06:07] Já estou certinho, tenho a conta, tenho a versão 3.7 instalado, meu sistema operacional é o Mac mas tem suporte para o Linux e para o Windows e estou com o postgre instalado local. Então vou clicar em “I’m ready to start”, estou pronto para continuar.

[06:21]O que vamos fazer agora? Para pegarmos todos os arquivos do nosso código, os clientes, setup, tudo que precisamos para o nosso projeto funcionar e mandar para o Heroku, vamos precisar de um comando do Heroku mesmo.

[06:37] Tenho que falar assim: “Heroku, eu quero enviar esses arquivos para você”. Para isso, vamos instalar um CLI, um “Command Line Interface” , a interface de linha de comando do Heroku na nossa aplicação.

[06:49] Então caso você esteja utilizando um Mac, você pode instalar com o instalador ou utilizar o brew para instalar, “brew install heroku/brew/heroku” , aí você faz o download.

[07:02] Se estiver utilizando o Windows, se for de 64-bit ou 32-bit, é só clicar no instalador e se seu caso for um Ubuntu é só dar o comando sudo snap install heroku --classic e você vai conseguir realizar o Heroku, o Log In do Heroku na sua aplicação.

[07:17] Depois que você realizou esses passos, eu já instalei o Heroku CLI na minha máquina e vou executar o comando heroku login. Vou abrir nosso código, e vemos nosso servidor, e vou abrir um segundo terminal, clicando no ícone de “mais”.

[07:36] Já estou com a venv, vou dar um heroku login e ele fala assim: “Pressione qualquer tecla para abrir o browser para ver se você pode realizar o login”. Vou pressionar a letra “A”, pode ser qualquer tecla menos o “Q” senão eu vou sair. Olha o que vai acontecer.

[07:51] Pressionei, ele abre uma página do Heroku para mim e vou clicar em “Log In”. E pronto, já estou logado, aparece uma mensagem na tela dizendo “You can close this page and return to your CLI. It should now be logged in”

[08:05] Então, por eu estar logado anteriormente na página da instalação do Heroku, ele já permitiu que eu realizasse o Log In. Ele falou: “Opa, você já está logado aqui com seu nome”. Maravilha.

[08:13] Então já começamos bem, já temos um Log In feito na nossa máquina, já temos o CLI do Heroku, já tenho instalado o CLI, e o que ele fala? Bom, agora você vai precisar preparar o seu arquivo, realizar um git do seu arquivo.

[08:28] Só que antes de realizarmos esses passos, o que eu preciso fazer na parte do Django? E é isso que vamos ver no próximo vídeo.

### Realizando o deploy

Realizando as configurações no meu Projeto DJANGO:

1. Instalar o HEROKU no projeto:

    pip install django-heroku

2. No SETTINGS.PY:

    import django_heroku

    django_heroku.settings(locals())

3. Instalar o GUNICORN no projeto: [DOCUMENTAÇÃO]('https://gunicorn.org/')

    pip install gunicorn

4. Criar um arquivo Procfile:

    web: gunicorn setup.wsgi

5. Atualizar o requirements.txt com todas as dependências do projeto:

    pip freeze > requirements.txt

6. Iniciar um o GIT:

    git init
    git commit -m "deploy do projeto"

7. No HEROKU CLI:

    heroku git:remote -a nome_do_app_remoto # vinculando o repositório git
    git push heroku master                  # envidando os dados para o heroku

    # Parabésn!!! Se não apareceu uma mensagem de erro sua aplicação esta on-line, mas ainda não acabou falta alguns passos continue --->

    heroku run python manage.py migrate     # migrações do banco de dados na aplicação do servidor, criando as tabelas
    heroku run python manage.py createsuperuser # criar um super usuário no meu admin

---

[00:00] Realizamos as configurações do Heroku, agora vamos realizar as configurações do lado do Django.

[00:06] A primeira coisa que vamos fazer será instalar o Heroku no nosso Django também. Existe um modo, uma lib responsável por fazer essa integração e preparar essa configuração também para postarmos nosso app no Heroku.

[00:20] Então no nosso código eu vou instalar pip install django-heroku. Dou um enter e ele vai instalar para mim o Heroku no meu ambiente, na minha venv.

[00:34] Instalou o Heroku e o que eu vou fazer? Vou minimizar, apertar “Ctrl + P” e vou em setting.py acessar o settings do Heroku e vou importar a configuração que vamos realizar agora no settings do nosso projeto de clientes.

[00:49] É muito simples, eu vou importar import django_heroku e lá no final da página, na última parte, na última linha, no caso a linha 131, vamos colocar uma única linha de configuração, que vai ser django_heroku.settings(locals()) , abre e fecha parênteses executando essa função.

[01:17] A única configuração necessária no settings para subirmos nossa aplicação é essa. “Ah, mas a nossa aplicação está utilizando o data base sqlite, e o Django utiliza o postgre. Mas nós já temos o postgre instalado e ele vai ser responsável por fazer toda essa mágica acontecer.

[01:35] Vamos lá, um ponto importante aqui. Se observamos na nossa aplicação, temos uma chave de segurança a SECRET_KEY.

[01:47] E essa chave de segurança é ideal eu pegar essa chave, gerar uma nova chave, colocar uma variável de ambiente e manipular as configurações do Django também para conseguir acessar essa minha variável de ambiente.

[02:00] Isso seria uma aplicação em produção, valendo, não é o nosso caso aqui, não é o escopo do nosso projeto.

[02:07] Temos uma API, um crood de clientes com validações , com ordenação. Então, não vamos focar no denso conteúdo que é realizar um deploy pensando em todos os pontos possíveis.

[02:20] Então que fique bem claro que estamos fazendo um deploy para facilitar o nosso trabalho, o nosso desenvolvimento da nossa API, mas não vamos suprir todos os densos conteúdos que são realizar um deploy de uma aplicação.

[02:39] Então o que vamos fazer? Fez um import do Heroku, colocou no final django_heroku.settings(locals()) , e a outra coisa que vamos fazer é ter que instalar gunicorn. E o que ele vai fazer? Vamos acessar a página dele para visualizarmos.

[02:57] Vou na busca na internet e vou digitar “gunicorn”. E ele fala que o gunicorn é um servidor HTTP de interface Gateway do servidor Web Python, é um modelo de trabalho pré-fork, transportado do projeto Ruby Gunicorn.

[03:12] Se clicarmos no primeiro resultado da pesquisa “Gunicorn - Python WSGI HTTP Server for UNIX” , quando acessamos, o que ele quer dizer? Todas essas palavras difíceis, ele vai ser responsável por realizar o compartilhamento de recursos entre os nossos servidores, de forma leve e simples.

[03:27] O legal é que ele é feito, escrito na linguagem Python também. Então, vai ser muito mais fácil conseguirmos instalar ele na nossa aplicação. E esse WSGI é uma interface bem de baixo nível, de comunicação entre servidores Web, aplicações Web, frameworks.

[03:45] Então ele vai funcionar debaixo dos panos, como uma interface mesmo entre os nossos servidores, do Heroku. As requisições que estão chegando ele vai ser responsável.

[03:58] Então, vamos instalar. Vou no nosso código, em settings.py e vou abrir o terminal “Ctrl + J”. Não vamos usar mais nenhuma configuração no settings, então vou limpar minha tela com “Ctrl + L” e vou instalar o gunicorn na nossa aplicação.

[04:12] Então vou digitar pip install gunicorn==20.0.4 que vai ser a versão que vamos utilizar. Dou um enter e ele vai instalar o Gunicorn 20.0.4. Instalamos o Django Heroku, instalamos o Gunicorn, o que vamos precisar fazer é, temos um arquivo chamado requirements.txt em “PROJETO_CLIENTES>requirements.txt” .

[04:37] Se olharmos, esse arquivo tem todas as dependências do nosso projeto, e instalamos outras dependências como o Django Heroku e o Gunicorn . Vamos precisar passar essas dependências também para o nosso Gunicorn.

[04:49] Então vamos colocar pip freeze > requirement.txt , ele vai pegar todas as dependências dessa aplicação e eu vou passar para o requirements.txt. Quando dou um enter ele colocou aqui todos os outros módulos que precisamos, todas as outras dependências.

[05:09] Então se olharmos em requirements.txt temos aqui o whitenoise, temos o nosso ´gunicorn ´ também, e django- heroku . Maravilha. O que falta agora para realizarmos o deploy da nossa aplicação? Falta duas etapas bem tranquilas.

[05:24] Próxima etapa que vamos fazer , vamos precisar indicar que essa nossa aplicação web vai ser executada com base no gunicorn. Para isso, vamos no ícone de “mais” do lado direito de “PROJETO_CLIENTES” e vamos criar um arquivo chamado “Procfile”.

[05:43] Dentro desse arquivo vamos colocar o seguinte conteúdo: web: gunicorn .E agora vamos pegar o nome da nossa aplicação que deixamos como setup então vou colocar web: gunicorn setup.wsgi.

[06:00] Então, dessa forma já estamos vinculando todas as responsabilidade, as requisições e a comunicação entre os servidores para o gunicorn. Então temos aqui o setup.wsgi. Legal, fiz tudo isso e agora podemos mandar todo o nosso código pro servidor do Heroku.

[06:23] Vou minimizar, fechar a aba do requirements.txt e deixar aberto só o Procfile para vermos bem. Primeira coisa que vou fazer, já tenho o git instalado na minha máquina.

[06:33] Se você não tiver, pode acessar o código do git, buscando na internet por “github download” e fazer o download do GitHub, clicando no segundo link da pesquisa “GitHub Desktop - Simple collaboration from your desktop”.

[06:48] E é o que vamos utilizar, no meu caso ele já está mostrando meu sistema operacional mas ele vai mostrar o seu sistema operacional.

[06:53] Faz o download, e assim que fazemos o download já precisamos iniciar o git no nosso código. Não vou passar tantos detalhes do git porque na plataforma do Alura temos vários cursos ensinando o passo a passo do git.

[07:06] Então vamos lá, vou iniciar um novo repositório com git init e agora eu quero pegar todo o conteúdo que eu tenho, todos os arquivos que eu tenho no meu “PROJETO_CLIENTES” e falar: “Olha, meu próximo comit eu quero ter todos esses arquivos vinculados.

[07:25] Então vamos colocar git add.Vou dar um enter e vou colocar na linha de baixo também git comit -m “deploy do projeto" Dou um enter e ele criou para mim toda a configuração do comit.

[07:47] Bom, agora para eu mandar pro Heroku eu preciso vincular, preciso falar: “Olha, esse meu app vai ser utilizado para eu fazer o deploy”.

[07:57] Então temos aqui um comando que se chama heroku git:remote -a drf-clientes , que é o nome do app que criamos. Ele vai mostrar o nome do app que você criou, então vai ficar um pouco diferente pra você.

[08:12] Vou dar um “Ctrl + V” no nosso terminal, dou um enter e pronto. Ele já vinculou esse meu git com o git do remoto do Heroku. Para finalizar, a última coisa que preciso fazer é colocar um git push heroku master.

[08:32] Dou um “Ctrl + C”, venho no meu terminal e dou “Ctrl + V” , e aguardo ele enviar todos os arquivos que eu tenho do git para o Heroku.

[08:43] Agora que ele terminou de realizar o deploy de todos os arquivos que tenho, vamos visualizar como ficou a nossa aplicação? Vou copiar o link “https://drf-clientes.herokuapp.com/” que esse é o endereço agora de onde a minha API vai ficar hospedada , não é mais “localhost”.

[08:59] Então dei um “Ctrl + C” nesse link, vou abrir uma página na internet com esse link e apareceu aqui. Só que quando eu clico no link em vermelho no meio da página, observe o que vai acontecer. Temos um erro.

[09:12] Um erro falando que não existe a tabela clientes, não tem um contador de clientes. Porque em nenhum momento realizamos o manage.py migrate. Temos as migrações para subir nossa aplicação no Heroku, mas não criamos essas tabelas do banco de dados lá no Heroku.

[09:32] Vamos fazer isso agora? Então limpei meu terminal, e o que eu vou fazer? Vou digitar heroku run python manage.py migrate ou seja, vou dizer: “Heroku, roda um determinado comando”.

[09:44] E qual comando eu quero executar? o python manage.py migrate. Quando dou um enter ele vai gerar toda a migração lá no Heroku, vai criar todas as tabelas com base nos nossos modelos lá no Heroku também.

[10:11] Agora que ele criou todas as tabelas la no Heroku, quando eu clicar no link em vermelho novamente, olha o que vai acontecer. Vamos conseguir visualizar já a nossa API funcionando, já conseguimos criar os nossos clientes.

[10:23] Para finalizar, um ponto importante também, vamos criar um admin. Porque mesmo sendo uma aplicação no Heroku, não perdemos nosso Django Admin também. Então vamos precisar criar um administrador para ter acesso nessa página também do admin do Django.

[10:40] Então no nosso código vou colocar heroku run python manage.py createsuperuser. Dou um enter e ele está rodando esse comando.

[10:59] Agora ele está pedindo para eu criar um usuário, esse usuário eu vou criar com o nome de Guilherme, vou deixar a senha e endereço de email, e vou criar uma senha mais segura agora.

[11:26] E vai aparecer a mensagem de “Super usuário criado com sucesso”. Vou acessar meu admin com o usuário e senha que acabei de criar.

[11:36] Certo, vai abrir a página da “Administração do Django “ e se eu clico em “clientes” vamos visualizar que está tudo certo, todos os campos aparecendo certinho, o filtro, o campo de busca. Só que não temos nenhum cliente.

[11:47] Só que tínhamos no nosso código um arquivo para executarmos, para criar nossos usuários lá na base de dados, e tínhamos usado como teste.

[11:58] No próximo vídeo vou mostrar algumas funcionalidades. Como executamos esse comando também e algumas funcionalidades também em relação a autenticação.

[12:07] Porque a medida que executarmos e criarmos usuários no Heroku, não queremos que qualquer pessoa que chegue tenha acesso a esses usuários, então vamos proteger a nossa aplicação, criar uma forma de autenticação para consumir os recursos da nossa API.
    
### Atualizando API
Autenticação para controle de acesso na aplicação:

No VIEWS.PY:

    from rest_framework.authentication import BasicAuthentication
    from rest_framework.permissions import IsAuthenticated

    class ClientesViewSet(viewsets.ModelViewSet):
        ...
        authentication_classes = [BasicAuthentication]
        permission_classes = [IsAuthenticated]

---
Atualizações de alterações no projeto on-line:

No terminal:

    git status
    git add .
    git commit -m "atualização"
    git push

---

[00:00] Estou com meu projeto local na página principal e eu tenho aqui o meu endpoint de clientes, e quando eu clico ele vai listar todos os clientes.

[00:08] O mesmo acontece com o meu projeto no Heroku drf-clientes.herokuapp.com . Observe que eu tenho essa página e quando eu clico no link em vermelho no meio da página ele vai listar os clientes que eu tenho.

[00:20] Por enquanto não tenho nenhum cliente cadastrado e eu não queria isso, não queria que qualquer pessoa que tivesse acesso a esse endereço drf-clientes.herokuapp.com/clientes/ , visse todos os meus clientes. E vimos como inserir uma autenticação básica na nossa aplicação. Vamos fazer isso?

[00:30] Então vou no meu código em views.py e vou importar from rest_framework. authentication import BasicAuthentication , vamos importar o BasicAuthentication.

[00:49] Vamos colocar embaixo também como authentication_classes aqui no nosso ClientesViewSet e vou falar que ele vai ser igual, e entre colchetes vou passar o BasicAuthentication, ficando authentication_classes = [BasicAuthentication].

[01:10] Além disso, eu preciso dar as permissões necessárias porque eu quero que apenas as pessoas que estejam autenticadas tenham permissão de realizar o que o nosso ViewSet realiza.

[01:23] Então se observarmos, quando criamos uma classe ViewSet com ModelViewSet estamos permitindo que as pessoas que tiverem acesso possam realizar o crood completo básico.

[01:36] Porém, da forma como nosso projeto está implementado é possível criar um outro usuário que pode listar a API mas, por exemplo, não pode acessar a parte do admin. E eu quero testar isso com vocês.

[01:48] Então o que acontece? Temos dois cenários aqui. Deixa eu importar essa classe, então vou digitar from rest_framework.permissions import IsAuthenticated. Legal. Agora o que eu vou fazer é criar essa configuração de permission, então permission_classes = [IsAuthenticated].

[02:23] Coloquei esses dois e isso vai está rodando, funcionando no meu projeto local porque ainda não fiz o deploy para o meu Heroku app, então ele vai estar funcionando local.

[02:34] Se eu atualizar a minha página da aplicação, observe que ele já pediu o username e password, vou precisar acessar com meu usuário local.

[02:43] No nosso Administração do Django não temos esse problema porque não subimos as alterações que fizemos na view lá no nosso Heroku, então precisamos realizar um deploy. Bom, salvei a views.py, vou dar um “Ctrl + J” e vamos realizar o deploy.

[02:57] Fizemos alterações nos nossos arquivos, alteramos o nosso código view, então podemos ver isso utilizando o git status . Ele vai falar: “Opa, tem uma modificação na pasta de clientes, no views.py”. Então vou falar para o git pegar todas essas alterações que eu fiz e vou fazer um novo commit, ficando git commit -m “incluindo atenticação”.

[03:30] A única coisa que preciso fazer é o push no Heroku. Então vou colocar git push heroku master, dou um enter e ele vai dar o push do Heroku, das alterações que inclui no meu código.

[03:46] Então observe, vamos ter o passo agora de realizar as alterações, realizar os testes locais. Teve o resultado que esperamos, nossa aplicação teve o comportamento que esperamos, damos o git, adicionamos essas alterações no git e damos o push no Heroku. E ele está realizando aqui o push no Heroku.

[04:05] Ele terminou de realizar o deploy e o que eu vou fazer? Vou copiar esse link “https://drf-clientes.herokuapp.com/” de novo e vou abrir em uma aba anônima. Dei um enter, está carregando.

[04:23] Vou clicar em “clientes” com o link em vermelho no meio da página, e ele pediu a minha senha. Vou colocar a senha que criei de superusuário e quando eu clico eu consigo visualizar. Legal, nossa API está um pouco mais protegida.

[04:41] Vou acessar o admin e vou criar outro usuário. Esse usuário eu quero que ele tenha acesso aos dados da nossa API. Quero que ele consiga criar um novo cliente, deletar, atualizar os clientes, mas não quero que ele tenha acesso com o meu admin. “Ah, mas Guilherme, eu não queria que ele pudesse deletar os clientes”.

[05:04] Isso por enquanto não vai ser possível porque estamos utilizando o ModelViewSet, assim que eu falo que o usuário está autenticado, ele vai conseguir realizar todas as alterações na nossa API. Só que eu consigo não permitir que ele entre no admin, e é isso que quero mostrar agora.

[05:22] Então vou acessar o admin e vou criar o usuário e vou chamar o usuário de Ana. Vou criar uma senha para a Ana, confirmar a senha, e vou clicar em Salvar.

[05:49] A senha da Ana foi salva e é muito importante essa parte das informações pessoais. Nome Ana, último nome vou deixar nada, o email vai ser “ana@alura.com”.

[06:00] Vou dizer em permissões que é um usuário ativo. E ele até fala, no lugar de excluir um usuário, eu só desativo essa flag de ativo, só desmarcar.

[06:15] Observe essas outras configurações, membro da equipe indica que o usuário consegue acessar esse site. Vou marcar que não, ele não vai conseguir acessar o site de administração do Django. Nem ter status de superusuário.

[06:30] Então mais para baixo tem alguns filtros, eu não tenho nenhum grupo, e a permissão que eu vou dar para esse usuário são relacionadas a clientes. Vou colocar que vai poder adicionar um cliente, mas observa que essas permissões estão mais relacionadas ao admin.

[06:46] Então vai permitir adicionar clientes, vou selecionar que pode alterar os clientes, pode deletar cliente, e pode visualizar os clientes. Pode fazer tudo relacionado a clientes, mas não quero que tenha acesso ao admin. E é isso que vamos testar agora. Salvei.

[07:14] Então eu tenho dois usuários, o Guilherme que é superusuário e membro da equipe e tenho a Ana, com o email da Alura.

[07:22] Eu vou encerrar essa sessão clicando em “ENCERRAR SESSÃO” no canto superior direito do Administração do Django. Vou acessar novamente e vou começar com a conta da Ana. Vou colocar “ana@alura.com” e vou colocar a senha que criei para a Ana.

[07:38] Vou clicar em “acessar” e observe que recebemos uma mensagem escrita “Por favor, insira um usuário e senha corretos para uma conta de equipe.

[07:53] Note que ambos campos são sensíveis a maiúsculas e minúsculas.” A Ana não tem acesso ao admin, mesmo eu colocando a senha dela certinho. Vou colocar mais uma vez, e não consigo.

[08:02] Mas eu consigo consumir essa API, vamos ver? Vou colocar na url só “drf-clientes.herokuapp.com/” e consigo acessar a página. Vou clicar no link em vermelho para conseguir visualizar todos os clientes.

[08:15] Consigo, então olha que bacana, conseguimos dar permissão da pessoa criar um novo usuário, criar um novo cliente e realizar todas as outras alterações, mas eu não dei permissão para a pessoa acessar a parte de admin.

[08:31] Vou subir aquelas alterações que fizemos com o populate_script.py. “Ah, mas eu não quero executar esse script que cria vários clientes no Heroku, eu quero criar os clientes corretos, ou alguma coisa mais real, não quero gerar através disso”.

[08:52] Fica a seu critério, não tem necessidade de você realizar esse passo que vou fazer agora. Vou apenas mostrar como é possível de forma simples popularmos, criar os clientes que temos local, lá no nosso Heroku também.

[09:07] Então vai ser de uma forma bem simples. Vou executar o comando heroku run python populate_script.py . Dou um enter e ele vai executar esse script e vai gerar as pessoas que tínhamos local, lá no nosso script. Lembrando que isso não é obrigatório, você pode gerar sua própria lista de clientes se você quiser.

[09:45] Ele terminou, parece que houve um erro em alguma parte dos modelos que fizemos. Só que se formos lá no nosso app do Heroku, e eu clicar no link em vermelho no meio da página novamente, observamos que vamos ver todos os clientes criados. Então temos os mesmos clientes.

[10:03] Vamos testar os campos? Se clicarmos em “Filtra” e testarmos os campos, colocando a opção Ativo “sim” , quero apenas os clientes que são ativos. E então visualizamos só os clientes que são ativos.

[10:12] Se eu quiser visualizar só os ordenados de forma ascendente, temos aqui também. Se quero todos os clientes, coloco Ativo “Desconhecido” e deixamos todos os clientes. Vou ordenar por nome de forma ascendente, e conseguimos.

[10:26] Então, desta forma,vamos finalizando o nosso conteúdo, o nosso curso. Você pode testar e criar seus próprios clientes no seu app, no Heroku também. Mas espero que você tenha gostado.

[10:42] Então observa, agora temos dois tipos de aplicação, uma rodando local que dá para testarmos as coisas, e depois que testamos e ficou bacana podemos fazer um push direto para o Heroku, para a nossa API.

### Exercício: Exibindo ID

Para colocar a API de clientes no ar, utilizamos o Heroku para hospedar nossa aplicação. Agora, precisamos ativar a venv e executar o runserver para rodar local, porém, no Heroku nossa API estará sempre disponível.

Sabendo disso, podemos afirmar que:

a) **Alternativa correta:** Para alterar ou atualizar a API no Heroku, é necessário realizar um push na master do Heroku.
- _Alternativa correta! Certo! Após alterar ou atualizar o código, realizamos um commit adicionando todos os arquivos que queremos alterar e alteramos a API com o comando git push heroku master._

b) Não precisamos mais da aplicação local.

c) **Alternativa correta:** Temos um ambiente local de desenvolvimento e um em produção no Heroku.
- _Alternativa correta! Certo! Podemos realizar a manutenção ou atualização no escopo local e subir essas alterações para o Heroku respectivamente._

### O que aprendemos?

- Configuramos nosso projeto local para realizar o deploy;
- Realizamos o deploy e colocamos a API no ar;
- Vimos como atualizar a API no Heroku.
