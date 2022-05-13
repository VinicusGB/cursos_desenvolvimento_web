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
### Projeto da aula anterior
### Expressões regulares
### Importando validações
### Script para gerar clientes
### Populando banco de dados
### Dividir para conquistar
### Faça como eu fiz
### O que aprendemos?
## 4. Paginação, ordenação, busca e filtro
### Projeto da aula anterior
### Paginação
### Ordenação
### Busca e filtro
### Busca por RG
### Faça como eu fiz
### O que aprendemos?
## 5. Deploy
### Projeto da aula anterior
### Preparando o deploy
### Realizando o deploy
### Atualizando API
### Exibindo ID
### Faça como eu fiz
### Projeto do curso
### O que aprendemos?
