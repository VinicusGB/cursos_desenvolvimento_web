# API com Django 3: Versionamento, cabeçalhos e CORS - 6h
**Professor:** Guilherme Lima

**Disponível:** [ALURA]('https://cursos.alura.com.br/course/api-django-3-versionamento-cabecalhos-cors')

**Conteúdo:**
- Aprenda na prática o que é versionamento de API
- Saiba como definir diferentes níveis de permissões de usuários
- Aprenda como limitar o número de requisições dos recursos
- Inclua informações extras no cabeçalho das requisições
- Descubra como integrar uma API Django com um React front-end

## 1. Versionamento
### Apresentação

[00:00] Meu nome é Guilherme Lima e seja muito bem-vindo ao treinamento de Django REST Framework: Versionamento de API. O que nós vamos fazer nesse curso?

[00:09] Nesse curso vamos pegar o modelo do projeto criado no curso 1 de API, só que com algumas alterações que vamos ver e vamos aprender como criar versionamento de API, como eu atualizo a minha API sem perder os endpoints que já estavam funcionando.

[00:28] Vamos aprender também como lidar com níveis de permissões diferentes na nossa API. Então um determinado usuário vai poder realizar certas ações, outro usuário vai fazer outras ações, como fazemos isso aqui no Django REST.

[00:43] Vamos entender também como lidar com permissões de uma forma um pouco diferente, como conseguimos limitar o número de requisições de um determinado recurso da nossa API ou o uso até da nossa API mesmo. Então eu vou falar: “Se for um usuário anônimo, vou permitir 50 requisições, cinco requisições”. Vamos aprender isso nesse curso também.

[01:03] E vamos aprender sobre modelo de maturidade, como deixamos nossas APIs REST com um nível de maturidade um pouco maior. E para finalizar esse curso, vamos integrar a nossa API, desenvolvida com o Python e Django REST, com uma API desenvolvida com React.

[01:21] Então temos na nossa API alunos, cursos, matrículas e nessa parte de cursos eu quero conectar a minha API que está funcionando local com uma aplicação local também, desenvolvida em React. O que acontece? Quais são os passos necessários para eu conseguir ligar a minha API React com a minha API Django REST Framework?

[01:43] Sabendo de tudo isso, o que teremos em mente durante esse treinamento? Vamos disponibilizar um projeto inicial e todos os passos dados serão bem guiados para vocês, para que todo mundo consiga seguir esse treinamento.

[02:00] Esse projeto em React, nós vamos entregar para vocês, mas o nosso foco principal é a parte do Django REST, não vamos mexer em nenhuma linha de código do React, vamos simplesmente executar o comando, instalar o que é necessário para o React funcionar e executar o comando para subir o nosso servidor.

[02:18] E vamos ver quais são as implicações, o que acontece, como eu faço um projeto em uma linguagem conversar com outro projeto, o front-end com oback-end, tudo isso nós veremos nesse curso.

[02:31] Eu espero que você se sinta empolgado, eu super recomendo que você tenha visto os cursos anteriores de Django. Se você viu e se você está preparado para esse desafio, eu te convido a começar esse treinamento.

### Preparando o ambiente

Olá!
É muito bom receber você neste curso de API com Django 3: Versionamento, cabeçalhos e CORS.

Espero que seja uma experiência de aprendizado incrível, e que possamos vencer todos os desafios juntos. Neste curso, aprofundar nossos conhecimentos no Django Rest Framework e aprender como versionar a API, incluir diferentes níveis de permissões, CORS e como integrar um frontend REACT com a API.

Preparando ambiente
Além disso, para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

    Python 3.7.4
    Django 3.0.7

O Django pode ser instalado através do comando:

    pip install Django==3.0.7

Este projeto é inspirado no projeto do curso API com Django 3, porém não é uma continuação.

Sendo assim, para o acompanhamento é altamente recomendado realizar o download do projeto base [neste link]('https://github.com/guilhermeonrails/drf-escola-projeto_inicial/archive/master.zip'), e na próxima atividade, seguir os passos para carregar o projeto e aprender muito.

Em caso de dúvidas durante o curso, conte com o fórum da Alura, pois sua questão pode ser respondida pela nossa comunidade!

:)

### Carregando o projeto

[00:00] Vamos iniciar então os nossos estudos de API com Django REST? Nós queremos evoluir uma API. Eu tenho uma API que está funcionando e eu quero incluir novas funcionalidades, novos recursos, remover um determinado recurso.

[00:15] E o que eu preciso fazer? Primeiro lugar, precisamos de uma API. Pensando nisso, na atividade anterior temos um link para você fazer download do projeto base que vamos utilizar no decorrer de todo esse treinamento.

[00:29] Eu já fiz o download desse projeto, vou renomear esse projeto para “drf-clientes”, já que vamos trabalhar com a ideia de outros clientes consumindo os recursos da nossa API, então vou deixar “drf-clientes”.

[00:47] Vou abrir o VS Code como editor de código. Arrastando o projeto aqui para dentro, temos esse projeto aqui. Podemos dar uma olhada, é um projeto de escola, onde temos nos nossos modelos um aluno, um curso e fazemos as matrículas, vinculando o aluno e o curso, e indicando o período dessa matrícula.

[01:13] Mas como eu carrego esse projeto aqui na minha máquina? Que ele já é um projeto que foi feito. Nós utilizamos como referência o projeto criado na primeira parte do nosso curso de Django REST Framework, então ele é um projeto referência, existem algumas mudanças e eu recomendo que você também faça o download e continue o projeto a partir desse stage que temos aqui.

[01:40] Fizemos o download do projeto, primeira coisa que vamos fazer para carregar outro projeto Django é criar um ambiente virtual para ele.

[01:48] Se observarmos, temos aqui à esquerda a “escola”, o “setup”, onde ficam todas as configurações desse projeto, temos o “manage.py”, temos um arquivo chamado “requirements.txt”, onde vamos listar todas as dependências e módulos necessários para esse projeto, e temos aqui um arquivo chamado “seed.py”, que eu já vou falar dele.

[02:08] A primeira coisa que vamos fazer vai ser criar um ambiente virtual para esse projeto aqui. O que eu vou fazer? Vou fechar esse aqui, “seed.py”, só para ficarmos com a tela mais limpa e vou jogar nosso terminal aqui para cima.

[02:19] Para criarmos um ambiente virtual, assim como vimos em todos os cursos de Django, python -m venv ./venv. Dou um “Enter” aqui, nós veremos que vai aparecer uma “venv” aqui à esquerda, uma pasta, era o que queríamos. O que eu vou fazer agora vai ser ativar essa minha venv. Para ativar, source venv/bin/activate. Dou um “Enter” e eu ativei a minha venv.

[02:53] O que eu preciso fazer agora? Eu preciso pegar todas as dependências deste projeto e instalar nesse ambiente virtual que eu acabei de criar. Como eu faço isso? Para instalar as dependências, pip install.

[03:06] Para eu pegar todas as dependências desse meu arquivo e conseguir instalar nesse meu ambiente virtual, o que eu vou fazer? Vou utilizar a flag -r e vou passar o nome desse arquivo aqui, requirements.txt. E quando eu dou um “Enter” ele vai pegar todas essas dependências, tudo que o meu projeto precisa para funcionar, e vai instalar nesse meu ambiente virtual.

[03:34] Lembrando que estamos na fase 1 do nosso projeto, nós queremos evoluir uma API, qual API? Essa API que estamos instalando aqui e fazendo as configurações na nossa máquina.

[03:45] Fiz aqui a instalação, vou atualizar o pip com o comando pip install --upgrade pip’. Se essa mensagem não apareceu para você, não se preocupe você continua no próximo passo que houver aqui.

[04:00] Então já instalamos as dependências, se eu coloco aqui pip freeze, vamos poder visualizar aqui as mesmas dependências descritas no “requirements.txt”, que são as dependências que temos aqui também.

[04:14] Lembra que eu mostrei para vocês que nesse app de escola eu tenho modelos que têm aluno, que têm cursos e matrículas? Eu preciso agora criar o meu banco de dados para manter esses recursos também.

[04:29] Para eu gerar o script para criar no banco de dados, já sabemos, vou utilizar python manage.py makemigrations. Vou dar um “Enter” e ele vai gerar as migrações. Ele criou o script, agora eu preciso de fato pegar esses scripts e criar a minha base de dados, então eu uso python manage.py migrate, quando eu dou um “Enter” ele vai aplicar todas as migrações.

[04:56] O que eu vou fazer agora? Eu vou subir o meu servidor, python manage.py runserver e vou abrir aqui uma nova aba, no “localhost:8000”, e temos alunos, cursos e matrículas. Quando eu clico em “alunos”, ele pede uma senha. Precisamos criar uma senha de super usuário para conseguir navegar na nossa API.

[05:22] O que eu vou fazer? Vou parar o meu servidor, depois eu o carrego mais uma vez. E para criarmos um superusuário, nós utilizamos o comando python manage.py createsuperuser.

[05:41] O nome que eu vou dar para ele é um nome super simples, para facilitar o nosso ambiente de desenvolvimento, então vou deixar só o “gui”, não vou colocar e-mail, vou colocar a senha mais simples. A senha mais simples de novo, ele falou que a senha é muito curta, você já sabe qual senha eu coloquei, eu dou aqui um y que quero confirmar e eu criei o meu super usuário.

[05:58] Vou rodar mais uma vez o meu servidor, abrindo aqui o “localhost:8000/alunos/”. Deixa eu voltar aqui, vou clicar em “alunos” para eu visualizar, vou colocar o “gui”, que é o usuário que eu criei, e a senha que você já sabe qual é, e não temos nenhum aluno aqui. Podemos dar um post para criar.

[06:16] Só que esse tempo de criarmos aluno, ficarmos criando cursos e matrículas na mão, vamos gastar um tempo não necessário, queremos focar em coisas novas no nosso treinamento. Então o que eu fiz?

[06:28] Temos aqui um script chamado “seed.py”. Esse script vai nos gerar uma determinada quantidade de alunos e cursos, e ele não vai nos gerar uma quantidade de matrículas, por quê? Isso nós veremos no decorrer do curso e vamos criando no decorrer do nosso treinamento. Eu quero rodar esse script e gerar aqui 200 alunos e cinco cursos. Como eu faço?

[06:53] Lá no meu terminal, deixa eu parar o meu terminal de novo, eu vou utilizar o comando python para rodar esse script passando o nome dele, python seed.py. Quando eu dou um “Enter” não apareceu nenhuma mensagem.

[07:09] Vou rodar meu servidor de novo, abrindo a nossa lista de alunos, quando eu atualizar observe que agora eu tenho uma lista com 200 alunos. Vou scrollar tudo aqui, para vermos lá no final, 200 alunos. E se eu for em “cursos”, eu tenho todos os cursos também que eu criei, tem cinco cursos diferentes.

[07:32] O que eu quero fazer agora? Temos a nossa API funcionando, eu preciso incluir novos recursos, eu preciso incluir novas funcionalidades na minha API, porém eu preciso garantir que as pessoas e sistemas que já consomem a minha API vão continuar utilizando. Eu não posso criar uma API nova e não posso colocar as mudanças que eu quero na minha API local.

[07:53] No próximo vídeo vamos entender como existem formas diferentes de evoluirmos a nossa API e criar versões da nossa API, garantindo que essas novas funcionalidades funcionem para os clientes que precisem consumir nossa API e os clientes que já utilizavam as versões anteriores vão continuar utilizando a nossa API. Isso nós veremos a seguir.

### Tipos de Versionamento

O DJANGO-REST possui o versionamento de API, onde é possivel adicionar novas funcionadlidades e criar uma nova versão da API sem inutilizar a versão anterior. 5 tipos:

- **AcceptHeaderVersioning**
    - _Transferência do número da versão através do cabeçalho da requisição._
        
            GET /alunos/ HTTP/1.1
            Host: exemplo.com
            Accept: application/json; version=1.0

- **URLPathVersioning**
    - _Adiciona a versão no endereço do recurso de uma variável (o caminho é especificado no DRF por meio do parâmetro VERSION_PARAM)._

            urlpatterns = [
                url(r'^(?P<version>(v1|v2))/alunos/$', alunos_listname='alunos-lista'
                )
            ]

- **NamespaceVersionig**
    - _A versão é informada através do namespace da url._

            urlpatterns = [
                ulr(r'^v1/alunos/',include(alunos.urls', namespace='v1')),
                ulr(r'^v2/alunos/',include(alunos.urls', namespace='v2'))

            ]

- **HostNameVersioning**
    - _A versão é definida pelo nome de domínio._

            http://v1.exemplo.com/alunos/
            http://v2.exemplo.com/alunos/

- **QueryParameterVersioning**
    - _Transfere a versão através do parâmetro GET._

            http://exemplo.com/alunos/?version=1
            http://exemplo.com/alunos/?version=2

---

[00:00] Nessa aula vamos aprender o que é versionamento de API. Para começar, vamos pensar nesse seguinte cenário, já temos a nossa API funcionando e vamos imaginar que a nossa API funciona para dois tipos de clientes diferentes, um cliente mobile e um cliente web, um sistema web.

[00:17] E eu preciso atualizar a minha API incluindo novas funcionalidades ou outras informações dos recursos que disponibilizamos. Só que essas mudanças e essas novas funcionalidades nós não vamos colocar direto na API, vamos criar uma nova versão da nossa API.

[00:34] Isso não significa que vai ser uma API nova, vai ser outra versão da API que já temos, para atender os clientes que precisam dessas novas funcionalidades e continuar atendendo os clientes que já utilizavam a versão anterior da nossa API.

[00:50] No Django REST existem alguns tipos de versionamento que podemos escolher, dependendo da abordagem de cada cenário que nós vamos analisar aqui.

[01:01] Existe um tipo de versionamento chamado AcceptHeaderVersioning, o que ele significa? Nós passamos o número da versão através do cabeçalho da requisição. Então nós vamos fazer um get de alunos, por exemplo, e eu vou passar lá a versão específica que eu quero utilizar. Esse tipo tem esse nome, AcceptHeaderVersioning.

[01:22] Existe outro tipo também chamado URLPathVersioning, que nós vamos adicionar no recurso de uma variável a versão que queremos utilizar. Então teremos lá a nossa URL e vamos passar qual versão iremos utilizar, se é a versão 1 ou a versão 2 da nossa API. E lá na nossa view nós recuperamos esse valor através desse parâmetro “VERSION_PARAM”. Esse é outro tipo também.

[01:54] Temos outro tipo chamado NamespaceVersioning, então a versão é fornecida através do namespace da URL. Então temos “v1/alunos/’, include(aluno.urls’,namespace=’v1’))” e ele tem aqui as URLs e todos os arquivos responsáveis por aquela versão que estamos utilizando, ou a versão 2 e todos os arquivos responsáveis pela versão 2. Esse tipo se chama NamespaceVersioning.

[02:20] Existe outro também chamado HostNameVersioning, onde vamos incluir a versão da nossa API definida através do domínio, junto com o domínio do nosso host. Temos aqui “v1.exemplo.com/alunos/” ou “v2.exemplo.com/alunos/”.

[02:38] E existe outro tipo também chamadoQueryParameterVersioning, o que ele significa? Significa que vamos transferir, através do parâmetro get, a versão que queremos utilizar. Então eu tenho aqui o meu host “/alunos/?version=1” ou “version=2”.

[02:58] E por questão de tempo infelizmente nós não conseguimos mostrar na prática, criando vídeos, todos esses tipos de versionamentos de API, então vamos utilizar esse tipo aqui, QueryParameterVersioning.

[03:10] No próximo vídeo vamos criar um cenário onde eu preciso criar uma versão 2 da minha API, atendendo todos aqueles requisitos que eu já passei. Eu quero continuar atendendo os clientes que já utilizavam a minha API, que já consumiam os recursos, só que eu preciso incluir novas funcionalidades e eu vou utilizar esse QueryParameterVersioning no próximo vídeo.

### Query Parameter Versioning

1. Para utilizar ´QueryParameterVersioning´ devemos criar uma nova versão da class SERIALIZERS.py;
2. No VIEWS.PY devemos adicionar na ´class VIEWSETS´  um condicional para acessar versão correta do SERIALIZERS.py;
        
        class AlunosViewSet(viewsets.ModelViewSet):
            queryset = 
            authentication_classes = 
            permission_classes =
            def get_serializer_class(self):
                if self.request.version == 'v2':
                    return AlunoSerializerV2
                else:
                    return AlunoSerializer

3. No SETTINGS.PY devemos adicionar um novo parâmetro: [DOCUMENTAÇÃO]('https://www.django-rest-framework.org/api-guide/versioning/')

        REST_FRAMEWORK = {
            'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning'
        }

---

[00:00] Vamos criar na prática o QueryParameterVersioning na nossa API? Como ele funciona? Nós vamos colocar “?version=” e vamos escolher a versão que estamos utilizando na nossa API.

[00:12] Para deixar esse exemplo mais prático, eu quero criar uma versão 2 da nossa API onde eu tenho mais um campo. Além desses campos que eu tenho aqui, eu quero ter o campo celular, porque um determinado cliente, outro sistema precisa dessa nova funcionalidade aqui nos recursos que nós disponibilizamos de alunos.

[00:31] O que eu vou fazer? Primeira coisa, vamos criar lá no nosso modelo um campo em aluno chamado celular, então vou chamar aqui celular, ele vai ser igual a um models.CharField, eu vou colocar aqui um (max_length=11, e vou colocar um valor default=””) para ele também, como uma string vazia.

[01:00] Criei aqui um novo campo, esse campo celular. Deixa eu tirar ali do lado, só para enxergarmos melhor. Então criei aqui o meu campo celular dentro do meu modelo aluno. O que eu vou fazer agora vai ser abrir o meu terminal, “Command + J”, vou abrir uma nova aba do terminal, deixa eu ativar a minha venv, source venv/bin/activate.

[01:33] No primeiro terminal aqui nós estamos rodando nosso servidor, no segundo eu quero rodar essa migração, eu quero realizar essas mudanças que eu fiz aqui no meu modelo lá no meu banco de dados.

[01:45] Então vou rodar o python manage.py makemigrations e ele vai falar: “Nós adicionamos um novo campo celular no aluno”, é isso que nós queríamos. Agora o que eu quero fazer é de fato incluir essa migração no banco de dados, python manage.py migrate, eu dou um “Enter” e ele aplicou essas migrações.

[02:08] O que eu vou fazer na sequência vai ser, lá no meu serializer eu tenho o meu serializer de aluno e eu vou criar o outro serializer para incluir esse novo recurso, que é o celular. Então eu vou copiar todo esse código, todas essas informações, vou colocar aqui embaixo, eu vou colar essa informação do nosso aluno.

[02:36] Então temos o AlunoSerializer, eu vou colocar aqui AlunoSerializerV2, para lembrarmos que é a versão 2 do nosso serializador de aluno. E depois temos nos campos o ID, o nome, vou colocar uma vírgula aqui, vou colocar o nosso campo novo, celular. Salvei.

[02:56] Agora lá na minhas views, vou dar aqui um “Command + P”, vou digitar “views”, aparece aqui a view de escola, nós temos o AlunosViewSet.

[03:04] E olha que interessante, já temos uma classe serializer específica, nós falamos assim: “A classe serializer para esse nosso ViewSet de aluno é o AlunoSerializer”. Não é o que queremos. Dependendo da versão da API que recebermos lá no nosso parâmetro, nós queremos exibir ou a versão 1, que é sem o celular, ou a versão 2, com o celular.

[03:30] Então o que eu vou fazer? Eu vou colocar esse código para baixo, eu segurei o “Option” para baixo e ele veio aqui. Então eu vou definir essa classe com base na versão que vamos utilizar na nossa API. Eu vou tirar esse código aqui, serializer_class = AlunoSerializer, e vou criar uma função onde eu vou definir o meu serializer.

[03:53] A função que define o serializer é get_serializer_class. E como parâmetro vamos passar a instância que estivermos utilizando, o (self):. E aqui dentro eu vou começar.

[04:08] Eu vou perguntar primeiro, se a requisição dessa instância for igual a V2, então if, requisição que está vindo, self.request.version == ‘v2’, quem queremos utilizar como serializer? O AlunoSerializerV2, então vou colocar aqui um return AlunoSerializerV2, nós precisamos trazê-lo aqui, então temos o AlunoSerializerV2 aqui em cima. Já fiz o import dele.

[04:57] Agora, se eu não passei nenhuma informação, se eu não tenho a versão 2 na requisição, o que eu quero fazer? else:, eu quero retornar o nosso AlunoSerializer que nós já tínhamos antes. Salvei essa informação.

[05:17] A última coisa que vamos precisar fazer agora vai ser indicar para as nossas configurações que a nossa API utiliza o QueryParameterVersioning.

[05:28] Então eu vou abrir os sets da nossa aplicação, venho aqui em cima, à esquerda, fechar a “escola”, “setup > settings.py”. Lá no final eu vou criar, na linha 124, um parâmetro chamado REST_FRAMEWORK =, tudo maiúsculo, e aqui vamos passar as configurações do REST_FRAMEWORK.

[05:58] Se formos lá na documentação e digitarmos “Versioning - Django REST Framework”, teremos na própria documentação da nossa API vários tipos explicando todos aqueles tipos de documentação que utilizamos.

[06:13] E observe que temos aqui um “’DEFAULT_VERSIONING_CLASS’”, que é o que precisamos, passando “’rest_framework.versioning”, só que não estamos utilizando “NamespaceVersioning”, que vimos no nosso primeiro vídeo, estamos utilizando o QueryParameterVersioning.

[06:29] Então vou procurá-lo aqui, vou digitar “QueryParameterVersioning”, que é esse cara aqui. Agora sim, copiei, .QueryParameterVersioning’, fechei. Abrindo o nosso terminal 1 para ver se está tudo certo. Recebemos uma mensagem, vou rodar mais uma vez, manage.py runserver, parece que está tudo ok. Vamos testar isso daqui.

[06:58] Estou no alunos, atualizei. E quando eu atualizei ele colocou essa versão 2, porque eu acho que eu já tinha no cache aqui marcado. Então coloquei “?version=v2”, ele já trouxe para mim o ID, nome e o celular, o celular está vazio, podemos incluir o celular depois nesses alunos. Mas você percebe que já temos esse campo celular.

[07:23] Agora, se eu não passo nenhuma informação e dou só um “/alunos/”, observe que aquele campo celular não está mais presente, nem para eu fazer o meu post.

[07:36] Conseguimos criar duas versões da nossa API, uma versão 2, onde incluímos esses novos recursos e uma versão 1, atendendo os clientes e serviços que já consumiam a nossa API.

### Para saber mais: Tipos de versionamento

No Django Rest, existem algumas formas de versionar uma API. Vejamos a seguir alguns exemplos:

- QueryParameterVersioning \
    - _Transfere a versão através do parâmetro version_

    Exemplo:

        http://exemplo.com/alunos/?version=1
        http://exemplo.com/alunos/?version=2

- HostNameVersioning \
    - _A versão é definida pelo nome de domínio_

    Exemplo:

        http://v1.exemplo.com/alunos/
        http://v2.exemplo.com/alunos/

- NamespaceVersioning \
    - _A versão é fornecida através do namespace da url_

    Exemplo:

        urlpatterns = [
            url(r'^v1/alunos/', include(alunos.urls', namespace='v1')),
            url(r'^v2/alunos/', include(alunos.urls', namespace='v2'))
        ]

- URLPathVersioning \
    - _Adiciona a versão no endereço do recurso de uma variável (o caminho é verificado através do parâmetro VERSION_PARAM)_

    Exemplo:

        urlpatterns = [
            url(r'^(?P<version>(v1|v2))/alunos/$', alunos_list
                name='alunos-lista'
            )
        ]

- AcceptHeaderVersioning \
    - Transferência do número da versão através do cabeçalho da requisição

    Exemplo:

        GET /alunos/ HTTP/1.1
        Host: exemplo.com
        Accept: application/json; version=1.0

Não podemos esquecer de incluir o tipo de versionamento na variável de ambiente do REST_FRAMEWORK no arquivo settings.py. Por exemplo:

    REST_FRAMEWORK = {
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
    }

### Exercício: Vantagens do versionamento

Nesta aula, criamos um novo serializer que inclui o campo celular, conforme ilustra o código abaixo:

    class AlunoSerializerV2(serializers.ModelSerializer):
        class Meta:
            model = Aluno
            fields = ['id', 'nome', 'celular','rg', 'cpf', 'data_nascimento']

Mesmo assim, mantemos o serializer chamado AlunoSerializer que não possui o campo celular:

    class AlunoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Aluno
            fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

Sabendo disso, analise as afirmações abaixo e indique aquela que contém a vantagem de versionar uma API.

a) Ao versionar uma API, a velocidade e desempenho das respostas dela são aumentados significativamente.

b) **Alternativa correta:** Os clientes existentes podem continuar a usar a versão antiga da API compatível com a nova versão.
- _Alternativa correta! Mudanças e novas funcionalidades devem ser implementadas nas novas versões da API, não apenas em uma mesma versão._

c) Ao versionar uma API, a velocidade e desempenho das respostas dela caem significativamente.

### O que aprendemos?

- Carregamos o projeto base local e executamos o arquivo seed.py, para criar alunos e cursos;
- Entendemos que no Django Rest Framework existem várias formas e versionar a API;
- Vimos na prática como versionar a API com Query Parameter Versioning.

## 2. Permissões
### Definindo permissões
Definição padrão do DJANGO ADMIN, adicionamos as permissões conforme necessidade.

---

[00:00] Neste vídeo vamos aprender na prática como funcionam as permissões no Django REST. E para isso vou criar dois tipos de usuários com permissões diferentes.

[00:09] A primeira vai ser a Ana, ela vai ser responsável pelas matrículas da nossa aplicação. Então todo recurso relacionado à matrícula a Ana vai ter permissão de criar novas matrículas, de atualizar, de editar, mas ela não vai poder deletar as matrículas.

[00:25] O mesmo eu quero para o Marcos, só que para outros recursos. Eu quero que o Marcos seja capaz de criar alunos, listar alunos, editar os alunos, criar cursos, editar cursos também, mas ele também não vai ser capaz de deletar os cursos nem os alunos. Vamos ver isso na prática como funciona?

[00:41] A primeira parte que vamos fazer vai ser configurar o admin do Django com essas seguintes permissões para cada usuário. Vamos começar pela Ana.

[00:50] Vou acessar o Django admin, “localhost:8000/admin”, vou colocar aqui o nome do meu super usuário e a minha senha, e eu vou vir em “Usuários” e nós vamos poder visualizar que temos um usuário só, que é o “gui”.

[01:06] Vou adicionar mais um usuário, que vai ser a usuária “Ana”. Vou criar uma senha para a Ana, vou confirmar a senha, vou salvar. Vou dar aqui o primeiro nome, vai ser “Ana”, último nome vai ser “Ana” também, o endereço de e-mail vou deixar sem nada por enquanto.

[01:27] Vou indicar que é um usuário ativo na nossa aplicação. Não vamos criar grupos de permissões, mas poderíamos fazer isso também, não faremos isso agora, eu só quero lidar com as permissões específicas para este usuário.

[01:41] Eu quero que a Ana seja capaz de cuidar dos recursos de matrículas, então vou falar aqui que a Ana vai poder adicionar uma nova matrícula, ela vai poder atualizar, mudar uma matrícula, visualizar uma matrícula, só que ela não vai poder deletar uma matrícula. E essas são as permissões da Ana. Eu venho aqui embaixo, dou um “Salvar” e eu criei a Ana.

[02:06] Vamos criar agora o usuário Marcos, que vai ser capaz de manter os recursos de alunos e cursos. “Adicionar usuário”, “Marcos”, vou criar uma senha para ele, vou salvar. Primeiro nome, “Marcos”, último nome vou deixar “Marcos” também.

[02:36] Scrollando para baixo, quais são as permissões do Marcos? O Marcos vai conseguir criar um aluno, alterar e visualizar um aluno. Ele vai poder adicionar curso, editar um curso, e visualizar um curso também. Vou passar isso aqui para o lado, então ele tem todos esses recursos.

[03:01] Observe que em nenhum momento nós falamos nem para o Marcos e nem para a Ana que eles podem deletar os recursos que eles gerenciam. Vou salvar aqui. Então eu tenho o Marcos e tenho a Ana.

[03:15] Do lado do admin do Django o que temos que fazer é isso. Agora o que vamos precisar fazer? E u vou precisar ir lá nas minhas views e falar que eu preciso desse modelo de permissões aqui do admin na minha aplicação mesmo. E é isso que nós vamos ver no próximo vídeo.

### Testando as permissões

Para que nossa API herde as permissões conforme as permissões do DJANGO-ADMIN, devemos:

1. No VIEWS.PY:

        ...
        from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

        class AlunosViewSet(viewsets.ModelViewSet):
            ...
            permission_classes = [IsAuthenticated, DjangoModelPermissions]
            ...

---

[00:00] Agora que nós criamos no lado do admin as permissões da Ana para manter os recursos de matrícula e do Marcos para manter recursos de alunos e cursos, como nós pegamos essas modificações que nós fizemos no Django admin e passamos para a nossa API?

[00:16] Então nós queremos que aquelas modificações, aquelas permissões que nós incluímos no admin tenham efeito aqui no lado da nossa API.

[00:23] Primeira coisa que vamos precisar fazer para testar isso é, desse módulo, rest_framework.permissions, vou colocar uma vírgula aqui, nós vamos importar outro módulo para indicar que queremos utilizar o modelo de permissões do Django. Eu vou escrever aqui DjangoModelPermissions, no plural.

[00:48] Trouxe o DjangoModelPermissions, o que eu vou fazer? Observe que temos uma classe de permissões e dentro dessa classe temos uma verificação para analisar se já estamos logados. Além disso, vou colocar uma vírgula e vou passar esse DjangoModelPermissions para esse nosso modelo de permissão de classes também.

[01:09] Isso que fizemos está relacionado com o aluno. O curso, matrícula, lista de matrículas também precisam desse nosso DjangoModelPermissions, dentro dessa nossa variável das classes de permissões.

[01:25] Então o que eu vou fazer? Eu vou copiar essa linha aqui, permission_classes = [IsAutenthicated, DjangoModelPermissions], estamos vendo que o nosso código já está bem duplicado, várias coisas, nós vamos melhorar isso. Mas vou colocar aqui, no lugar do permission_classes só com IsAuthenticated, eu vou alterar, eu vou colocar também o DjangoModelPermissions, os dois. Vou fazer isso para todos.

[01:53] Salvei o meu código, o que eu vou fazer agora? Eu quero testar, vamos testar um por um. Eu vou começar testando a Ana, a responsabilidade dela é manter os recursos de matrículas, então eu vou visualizar.

[02:05] Para isso podemos fazer duas coisas, posso abrir uma aba privada do Chrome para fazer esse teste, posso abrir em outro navegador uma aba privada, aqui, por exemplo, digitar “localhost:8000” e quando eu clico, por exemplo, em “matrículas”, ele vai pedir um username, vou passar “Ana”, vou passar a senha da Ana que eu criei. Quando eu dou um “Sign in” eu consigo visualizar as matrículas.

[02:32] Observe que eu não tenho nenhuma matrícula criada, então vou criar. Vou colocar aqui período matutino, a Isabel Martins, no curso de Python Fundamentos. Vou alterar, vou colocar Python Avançado. Vou dar um “Post” e conseguimos. Parece que está tudo ok.

[02:49] Vamos testar agora algo que ela não pode fazer? Observe que o nosso delete não aparece mais aqui. Se eu acessar, por exemplo, a “/matriculas” aqui, colocar “/1”, e visualizar essa matrícula, temos o “Put”, nós conseguimos atualizar, conseguimos realizar o “Get”, o “Options” dessa requisição, só que não temos o verbo delete.

[03:09] O que eu vou fazer agora? A Ana não pode criar e manter alunos, por quê? Manter e criar alunos são recursos e permissões válidas para o Marcos. Mas vamos testar isso daqui. Vou clicar em “cursos” e observe que quando eu scrollo para baixo em cursos, nem aparece a aba do post. Para nós fez sentido isso daqui.

[03:32] Se eu acesso aqui “matrículas”, ele mostra para mim as matrículas e aqui embaixo eu tenho um HTML e um form, indicando que eu posso aqui executar um post e criar um novo recurso.

[03:42] Agora, se eu coloco, por exemplo, em “alunos”, eu vou listar todos os alunos e quando acabar essa lista de alunos eu não consigo fazer nada, ou seja, o get eu consigo visualizar, da Ana, dos recursos de aluno, cursos, mas eu não tenho ação nenhuma, a Ana não tem permissões de manipular esses recursos.

[04:02] Para testar o Marcos eu vou utilizar o Postman, mas se você não quiser utilizar o Postman, se você quiser utilizar aqui mesmo, abrir outra aba anônima e fazer o teste, você pode. Então vou fechar isso daqui, vou lá no Postman e vamos só relembrar o que o Marcos pode fazer.

[04:20] O Marcos é responsável por criar alunos e cursos, mantendo esses recursos. O que eu vou fazer? Vou pegar esse aluno, de cópia, só para ganharmos tempo, vou vir no Postman e vou dar um post nesse endpoint, deixa eu copiar o código, colocar aqui no “Body”. O nosso código não é XML, é JSON. Não tem o ID, eu já vou alterar esses dados para conseguirmos visualizar melhor.

[04:58] O que eu vou fazer agora? Vou pegar esse nosso end-point, “localhost:8000/alunos/”, eu quero dar um post, e vou colocar aqui no nome “teste do Postman”. O RG vai ser esse RG, deixa eu mudar só um número para ele não ficar igual, vou colocar aqui na frente “2”, aqui no CPF vou colocar “2” também e a data de nascimento eu vou deixar essa mesmo.

[05:26] O que eu preciso fazer? Eu preciso ter uma autorização. Então venho em “Authorization”, vou colocar que é um “Basic Auth” de authorization e vou colocar o Marcos com a senha dele.

[05:39] Aqui no “Body” eu vou dar um “Send”, vamos visualizar, e parece que foi criado, o ID 203. Vamos ver lá do lado da nossa API? Em “/alunos”, se eu colocar “/203/”, eu tenho aqui o teste do Postman. Maravilha, fez sentido.

[05:54] Só que observa que do Marcos, quando eu estou visualizando, eu estou logado com o meu admin, então eu vejo o delete. Será que o Marcos consegue deletar esse aluno? Vamos testar?

[06:07] Selecionei esse end-point, se eu dou um get nesse end-point, “http://localhost:8000/alunos/203/”, dou um “Send”, ele vai mostrar para nós esse recurso que criamos.

[06:17] Eu não quero dar um get nesse recurso, eu quero deletar, então vou colocar aqui o verbo delete e vou tentar. Quando eu dou um “Send” observe que legal a mensagem que ele já dá: “Você não tem permissão para executar essa ação”. Muito bacana.

[06:32] Mas e se eu quisesse alterar alguma coisa? Então eu vou dar aqui um put, e eu vou mudar o nome, “Postman atualizado”, só para visualizarmos lá. Se eu dou um “Send”, temos “Postman atualizado”. Será que alterou aqui para nós também? Clicando aqui em atualizar, alterou, “Postman atualizado”.

[06:58] Olha que bacana, quando criamos usuários e determinamos as permissões desses usuários do lado do Django admin, para trazermos essas informações para cá, nós utilizamos a classe DjangoModelPermissions e passamos para o nosso ViewSet, lá no permission_classes esse módulo que importamos também.

[07:18] Isso ficou bem legal, só que tem um ponto que está um pouco estranho no nosso código, observe a quantidade de código duplicado que temos, principalmente para essa parte de autenticação e permissão. Será que nós conseguimos melhorar o nosso código removendo essa quantidade de código duplicado? É isso que vamos ver no próximo vídeo.

### Refatorando o código

Podemos criar uma função para permission_classes e authenticated_classes. 

1. No SETTINGS.PY podemos adicionar uma outra permissões

        REST_FRAMEWORK = {
            'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
            'DEFAULT_PERMISSION_CLASSES': [
                'rest_framework.permissions.IsAuthenticated',
                'rest_framework.permissions.DjangoModelPermissions'
            ],
            'DEFAULT_AUTHENTICATION_CLASSES': [
                'rest_framework.authentication.BasicAuthentication',
            ]
        }

2. NO VIEWS.PY podemos remover:

        authentication_classes = 
        permission_classes = 

---

[00:00] Conseguimos incluir as permissões que queríamos na nossa aplicação, porém se observarmos o nosso código da views, temos várias linhas repetidas.

[00:08] Por exemplo, o authentication_classes e o permission_classes estão iguais em praticamente todos os nossos viewsets, porém, como conseguimos minimizar esse código duplicado? É isso que veremos nesse vídeo. Vamos melhorar o nosso código, deixá-lo mais legível, sem tanta repetição e sem alterar o comportamento da nossa aplicação.

[00:27] Para isso vamos acessar os settings da nossa aplicação, aqui, “setup > settings.py”, e dentro desse REST_FRAMEWORK podemos indicar outras configurações padrões, por exemplo, eu quero indicar o authentication_classes.

[00:44] Da mesma forma que temos aqui um DEFAULT_VERSIONING_CLASS, indicando o QueryParameter, eu vou colocar aqui uma vírgula e vou colocar outro tipo de verificação, vai ser o DEFAULT_PERMISSION_CLASSES, no plural. Então as permissões das nossas classes, as permissões padrões. Dois pontos, entre colchetes, aqui dentro eu vou passar quais são essas permissões. E temos duas.

[01:21] Lá do nosso rest_framework.permissions – vou copiar esse código, vou colocá-lo aqui, entre aspas também – temos duas permissões, a primeira, IsAuthenticated, para saber se ele está autenticado, vou copiá-lo aqui, .Isauthenticated’,.

[01:40] Aqui embaixo eu tenho esse mesmo código, ’rest_framework.permissions.IsAuthenticated’, vou dar aqui um “Enter”, só que no lugar do IsAuthenticated nós vamos utilizar o DjangoModelPermissions, vou colocá-lo aqui. Nós passamos então para cá.

[01:56] O que eu já poderia fazer? Todas essas linhas de classes de permissões eu já posso tirar daqui, porque eu coloquei-a lá no setup da nossa aplicação. Então nós dizemos que por default essas são as nossas autenticações. Então todas essas linhas nós vamos tirar, permission.

[02:16] O que podemos fazer também é para a parte de autenticação. Temos aqui do rest_framework.authentication, vou criar o default dele, vou colocar aqui uma vírgula, porque nós fechamos esse permission, DEFAULT_PERMISSION_CLASSES, entre aspas vou colocar ’DEFAULT_AUTHENTICATION_CLASSES’:, no plural, entre colchetes vou passar o meu valor.

[02:48] Então temos, lá do Django Rest Authentication, entre aspas ’rest_framework.authentication.’, queremos verificar que a pessoa está autenticada, e nós utilizamos o BasicAuthentication, então vou passar aqui .BasicAuthentication’.

[03:09] Salvei, o que eu posso fazer? Vou remover essa linha de autenticação, essas linhas também, authentication_classes = [BasicAuthentication]. Salvei esse aqui, posso remover essa linha, from rest_framework.authentication import BasicAuthentication, não estou utilizando.

[03:29] Então nosso código já ficou bem mais fácil de entendermos. E nós vamos continuar com o mesmo comportamento. Vou colocar aqui uma vírgula, só para o nosso terminal não parar. Vamos testar para ver se tudo está funcionando bem?

[03:45] O que eu vou fazer? Aqui eu estou no “alunos” com autorização do Marcos, o Marcos pode fazer as atualizações de alunos, então vou colocar “Postman atualizado 2.0”, algo desse tipo, vou dar um “Send” e temos o “Postman atualizado 2.0”.

[04:03] Vou tentar deletar esse aluno 203, e nós recebemos que não temos a permissão, ou seja, nossas permissões continuam funcionando, então o nosso código continua igual e nós melhoramos bastante a questão das nossas views, deixamos muito melhor.

[04:22] Outro ponto que podemos melhorar na nossa aplicação é a navegação. Se observarmos no nosso código, quando eu clico aqui, “alunos”, ele vai pedir autenticação, vou logar como o usuário admin, que eu quero mostrar outro ponto que podemos melhorar, e observe que aqui temos o “localhost:8000/alunos/”. Se eu coloco aqui, por exemplo, o aluno 2, temos os detalhes do aluno 2 e assim por diante.

[04:45] Se eu quiser visualizar todas as matrículas desse aluno, o que eu tenho que fazer? Vamos visualizar lá em “setup” as nossas URLs.

[04:53] Na nossa URL eu tenho aluno, no singular, o ID desse aluno, barra matrículas. Então eu teria que tirar esse S, “localhost:8000/aluno/2/matriculas/”. Quando eu dou um “Enter” ele não tem nenhuma matrícula, eu acho que fizemos a matrícula para o aluno 1. Deixa eu voltar aqui. Isso, para a aluna 1. Então temos aqui as matrículas da aluna 1.

[05:17] Só que observe que faz mais sentido pensarmos na nossa API como uma navegação entre pastas. Se eu mantenho tudo no plural, vai ficar muito mais fácil eu conseguir manipular os dados, melhorar os meus end-points.

[05:30] Por exemplo, se eu coloco “localhost:8000/alunos/1/”, temos detalhes do ID 1. Se eu quiser visualizar as matrículas, faria mais sentido se eu tivesse aqui “localhost:8000/alunos/1/matriculas”, dou um “Enter” e visualizo as matrículas desse aluno.

[05:43] Ou seja, posso padronizar os meus end-points, como? Tudo no singular ou tudo no plural, para ficar mais fácil essa navegação. Vamos alterar isso então?

[05:52] Vou deixar “alunos”, vou deixar “cursos”, então temos end-point de alunos, end-point de cursos e de matrículas. Se eu quero visualizar, por exemplo, as matrículas de um determinado aluno, eu vou utilizar no plural por conta da navegação da minha aplicação também. Então se eu atualizo aqui, deu um erro. Vou atualizar mais uma vez, ele conseguiu trazer.

[06:16] Se eu coloco, por exemplo, as matrículas do aluno 2, ele vai mostrar que esse aluno não tem nenhuma matrícula. O mesmo acontece para os nossos cursos. Eu tenho um curso, eu passo o ID desse curso, barra, e quero ver todas as matrículas que esse curso possui, vai ficar muito mais fácil a nossa navegação.

[06:33] E de onde nós tiramos essa ideia? Vamos pensar bem nos nossos end-points como uma navegação entre pastas. É uma analogia muito simples, mas que vai fazer sentido e vai ficar muito mais fácil conseguirmos navegar nos nossos end-points.

[06:50] O que nós fizemos? Colocamos lá nos settings da nossa aplicação as propriedades default das nossas classes, tanto os de permissões como os de autenticação, e nós melhoramos os nossos end-points padronizando tudo no plural, para ficar mais fácil essa navegação.

### Exercício: Django Admin e API

Nesta aula, criamos 2 tipos de usuários utilizando o Django Admin com permissões diferentes, em que cada um é responsável por um recurso.

Sabendo disso, analise as afirmações abaixo e marque a que está correta em relação ao Django Admin.

a) **Alternativa correta:** As alterações feitas no Django Admin podem ser aplicadas na API Rest, respeitando as boas práticas de programação.
- _Alternativa correta! Podemos incluir as configurações em cada viewset ou apenas uma única vez no settings.py do projeto._

b) As alterações feitas no Django Admin não podem ser aplicadas na API Rest.

c) As alterações feitas no Django Admin podem ser aplicadas na API Rest. Porém, uma série de códigos duplicados será necessária para o funcionamento.

### O que aprendemos?

- No Django Admin, criamos a usuária Ana, com permissão de manter os recursos de Matrículas, como criar, ler e atualizar; e o usuário Marco, com permissão para manter os recursos de Alunos, podendo criar, ler e atualizar;
- Configuramos o Django Rest para utilizar as permissões do Django Admin e testamos as permissões no Postman;
- Melhoramos a qualidade do nosso código removendo o código duplicado das views.

## 3. Viewset e permissões
### Projeto da aula anterior
### Métodos HTTP
### Limitando requisições
### Faça como eu fiz
### Tipos de Views
### O que aprendemos?
## 4. Modelo de maturidade e Location
### Projeto da aula anterior
### Modelo de maturidade
### Cabeçalho Location
### Faça como eu fiz
### A glória do REST
### O que aprendemos?
## 5. Teste de unidade na view e model
### Projeto da aula anterior
### Preparando o ambiente
### O que é CORS?
### CORS no Django
### Faça como eu fiz
### Permitindo compartilhamento
### Projeto do curso
### O que aprendemos?
### Parabéns
### Conclusão
