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
### Projeto da aula anterior
### Definindo permissões
### Testando as permissões
### Refatorando o código
### Faça como eu fiz
### Django Admin e API
### O que aprendemos?
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
