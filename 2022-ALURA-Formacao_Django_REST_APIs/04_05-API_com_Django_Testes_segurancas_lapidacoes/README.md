# API com Django 3: Testes, segurança, e lapidações - 6h
**Professor:** Guilherme Lima

**Disponível:** [ALURA]('https://cursos.alura.com.br/course/api-django-3-testes-seguranca-lapidacoes')

**Conteúdo:**
- Aprenda na prática como trabalhar com arquivos estáticos
- Saiba na prática como armazenar o caching no Redis
- Crie testes para verificar as principais requisições e suas respostas
- Internacionalize sua API para diversos idiomas com base nas requisições
- Descubra como proteger seus projetos feitos em Django aumentando a segurança

## 01. Upload de arquivos estáticos Ver primeiro vídeo
### Apresentação

[00:00] Olá! Meu nome é Guilherme Lima e eu serei o seu instrutor nesse treinamento de API com Django 3 Testes, Segurança e Lapidações. O que nós vamos aprender nesse curso? Nesse curso vamos aprender a incluir uploads de arquivos nas requisições e na API, vamos aprender a trabalhar com Caching e vincular o Django com Redis.

[00:19] Vamos aprender a realizar a internacionalização das nossas requisições para diferentes idiomas. Vamos realizar os testes das principais requisições que temos e vamos dar uma pitada de segurança nas aplicações desenvolvidas com Django para deixarmos o nosso projeto bem legal e completo.

[00:37] Quais são os pré-requisitos para esse curso? É muito importante que você tenha feito os cursos anteriores de Django para nós mantermos uma continuidade também nos nossos estudos. Principalmente nos cursos de desenvolvimento de API.

[00:51] Qual é o público alvo desse curso? Se você quer aprender a trabalhar com Caching, Segurança, desenvolvimento de API e aprofundar os seus conhecimentos, você é muito mais do que convidado para realizar esse treinamento comigo! Sabendo de tudo isso, vamos começar?

### Preparando o ambiente

Olá!
É muito bom receber você neste curso de API com Django 3: Testes, segurança e lapidações.

Espero que seja uma experiência de aprendizado incrível, e que possamos vencer todos os desafios juntos. Neste curso, aprofundar nossos conhecimentos no Django Rest Framework e aprender como incluir arquivos estáticos em nossas requisições, caching, internacionalização, testes e segurança.

Preparando ambiente
Além disso, para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

        Python 3.7.4
        Django 3.0.7

O Django pode ser instalado através do comando:

        pip install Django==3.0.7

Este projeto é inspirado no projeto do curso API com Django 3: Versionamento, cabeçalhos e CORS, porém não é uma continuação. Usaremos o projeto do curso citado acima. Caso não tenha visto, é recomendado para um bom proveito deste treinamento.

Sendo assim, para o acompanhamento é altamente recomendado realizar o download do projeto base [neste link]('https://github.com/alura-cursos/drf_lapidacoes/archive/projeto_inicial.zip') caso não tenha feito o curso de versionamento de API com Django 3.

Após o download do projeto base, abra o projeto em seu editor de código preferido e crie uma nova venv com o comando `python -m venv ./venv` e ative conforme seu sistema operacional.

Para sistemas MacOS ou Linux:

        source venv/bin/activate

Já no Windows:

        venv\Scripts\activate.bat

Após ativação, faça a instalação dos módulos necessários com o seguinte comando:

        pip install -r requirements.txt

Para finalizar, vamos carregar os dados iniciais executando o comando:

        python seed.py

Para garantir que tudo deu certo, suba o servidor:

        python manage.py runserver

Na próxima atividade, vamos aprofundar ainda mais seus conhecimentos utilizando esta incrível ferramenta de desenvolvimento.

Em caso de dúvidas durante o curso ou carregamento do projeto, conte sempre com o fórum da Alura!

: )

### Incluindo campo foto

Para incluir fotos devemos trabalhar com a biblioteca [Pillow]('https://pillow.readthedocs.io/en/stable/installation.html').

        pip install pillow

1. Em settings.py:

        ...
        STATIC_URL = '/static/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
        MEDIA_URL = '/media/'

2. Em models.py

        class Aluno(models.Model):
                ...
                foto = models.ImageField(blank=True)
                ...

3. Em serializers.py:

        class AlunoSerializerV2(serializers.ModelSerializer):
                class Meta:
                        ...
                        fields = ['id','nome','celular','rg','cpf','data_nascimento','foto']
                        ...

---

[00:00] Olá, pessoal! Sejam muito bem-vindos a mais um treinamento da Alura! Vamos iniciar os nossos estudos? Na atividade anterior a esse vídeo tivemos um passo a passo de como você carrega esse projeto. Esse projeto é uma continuação do projeto anterior. Então se você fez, poderá dar sequência.

[00:16] Se você quer aprender os assuntos desse projeto, desse escopo do nosso treinamento, você pode carregar esse projeto. Temos o passo a passo de como você faz isso. Então, vamos lá! Esse curso se trata de uma API onde nós vamos disponibilizar recursos de alunos, cursos e matrículas. Então temos uma série de alunos que já deixamos certa, para você conseguir carregar também essa base de dados.

[00:41] Temos alguns cursos e nas matrículas não temos nenhuma matricula ainda, porque não vamos trabalhar com elas por enquanto. Vou voltar. Qual é nosso foco inicial? Se acessamos http://localhost:8000/alunos/, nós podemos observar que temos o “id”, o “nome”, o “rg”, o “cpf” e a “data_nascimento”.

[01:01] E se observarmos no curso anterior, o que havíamos feito? No “escola > serializer.py” nós temos um outro Aluno. Uma versão 2 desse Aluno, onde disponibilizamos mais um recurso, que é o recurso de celular. Então se eu coloco, por exemplo, “?version=v2”, nós podemos ver que o campo “Celular” aparece para alguns alunos.

[01:22] Se eu volto na versão normal, ele não aparece. Só que agora ele tem uma seguinte situação: para ambas as versões nós vamos precisar incluir uma foto para os alunos, um arquivo estático. Como fazemos isso no Django? Como configuramos o Django para que ele continue a receber uploads de arquivos?

[01:45] Então, além desses campos, eu quero criar mais um campo chamado “foto”. Vamos fazer isso? Vamos fechar o “serializer.py”. A primeira coisa que vamos fazer é: existe um módulo que vai nos auxiliar com essa transição das fotos, porque quando fizermos um post de um aluno com uma foto, é necessário que a foto vá para um lugar e armazenemos o caminho daquela foto. Como fazemos isso?

[02:12] Existe um módulo que vamos instalar com o pip install, chamado pillow. Ele vai ser responsável por fazer esse meio de campo para nós. Podemos até acessar ele aqui. Vou digitar pillow django para conseguirmos ver. Aqui, o pillow. Esse é um módulo que vamos instalar. Então ele vai nos auxiliar com essa manipulação de imagens dentro da API.

[02:48] Instalamos o pillow para mantermos o bom funcionamento da nossa API e dos arquivos e do que estamos fazendo. No “requirements.txt” é importante passarmos esse módulo que criamos. Vou fazer como? Vou colocar um pip freeze > requirements. Deixe-me só confirmar se escrevi certo... Está requirements.txt, parece que sim.

[03:14] E aparece o Pillow para nós. Vou fechar. Qual é nosso próximo passo? Se acessarmos o “setup - settings.py” vamos ver que já existe um “STATIC_URL”. Podemos até ver que ele fala “Follow link (cmd + click) JavaScript, Images”. Já temos essa configuração, mas é necessário que incluamos mais duas configurações para que nossos arquivos estáticos e que nossa foto, funcionem na API.

[03:50] O que vou fazer? Vou jogar esse STATIC_URL = '/static/' lá para baixo. Vou deixar ele aqui mesmo. Ia jogar ele ali para baixo, mas como está certo, deixe-me só tirar esses outros para não ficarmos confusos.

[04:00] O que vou fazer? Temos um caminho para os arquivos estáticos. Agora vamos precisar criar um root para essas medias. Vou chamar de “MEDIA_ROOT”. Qual vai ser a responsabilidade desse arquivo? Ele vai falar “a mídia dos arquivos estáticos está nesse caminho”, então vamos passar um caminho, os.path.join. Vou dizer que ele está no diretório principal, no BASE_DIR e vou dizer que o nome dele vai ser media_root.

[04:40] Uma outra variável que vamos precisar setar no “settings.py” é o MEDIA_URL. Por quê? Quando acessarmos a nossa API não vamos exibir a foto de todos os alunos, vamos exibir a URL indicando a foto para cada aluno. Então vou colocar MEDIA_URL = '/media/'. Todas as MEDIA_URL terão a referência do MEDIA_ROOT. Vou tirar esses espaços para não ficarmos com um monte de linhas sobrando.

[05:20] Configuramos o “settings.py”, por aqui não precisamos mexer mais. Vou no modelo de escola onde temos todas as bases do aluno e vou incluir um novo campo, que vou chamar de foto = e ele vai ser do tipo models.ImageField(). Olhe que legal, já temos uma propriedade para indicarmos essas fotos.

[05:43] E aqui tem um ponto importante: as fotos podem ser preenchidas e indicadas no novo recurso. O que acontece? Quando formos dar um post, poderá ter uma foto ou não. Então vou indicar a propriedade blank=true. Então vamos permitir que alguns alunos tenham fotos e outros não.

[06:06] Só que o true aqui precisa ser com letra maiúscula, então True. Apertei as teclas “Command + J”. Nós vamos fazer essa migração para a base de dados. Deixe-me virar nossa tela. O que vou fazer? A primeira coisa: python manage.py makemigrations para ele migrar esse cenário de inclusão de fotos em alunos.

[06:32] Ele falou que está adicionando o campo foto no aluno. O que vou fazer agora? Vou migrar, vou passar essas migrações para o banco de dados, python manage.py migrate. Beleza, a foto foi criada!

[06:45] Vou subir meu servidor mais uma vez, digitando manage.py runserver”, apertando a tecla “Enter” e voltando na nossa aplicação. Vou fechar a documentação do pillow. Está atualizando.

[06:56] Observe que não estamos conseguindo enxergar nada. Por quê? Porque colocamos essas alterações no nosso modelo, mas não passamos pelo Serializer. Lembra que temos dois serializers e ambos, é um escopo, um cenário fictício da nossa aplicação, eles precisam do campo “foto”.

[07:17] Então vou colocar , 'foto' no AlunoSerializer. No AlunoSerializerV2 também vou colocar vírgula , 'foto'. Salvei. Voltando para o Django e atualizando.

[07:31] Observe que agora apareceu lá ““foto”: null”. Se eu scrolar lá para o final, olhe o que vai acontecer! No final temos o campo “Foto” para escolhermos.

[07:40] Não faça o upload da foto ainda. Vamos fazer isso na sequência, no próximo vídeo.

### Upload de arquivos

Para que as imagens sejam carregadas devemos indicar para o DJANGO que as imagens precisam ser carregadas.

1. Em urls.py:

                from django.conf import settings
                from django.conf.urls.static import static

                urlpatterns = [
                        ...
                ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

---

[00:00] Vamos realizar o teste incluindo uma nova foto? Criei alguns dados só para realizarmos esse teste nos campos “Nome”, “RG” e “CPF” e “Data nascimento”. Tenho duas fotos que vou usar. Tenho essa foto aqui e depois vamos testar o update dessas fotos. Vamos lá!

[00:19] Vou criar, vou selecionar no campo “Foto > Choose File > foto-1.png > Open”. Ele carregou a “foto-1.png”. Se observarmos nos nossos arquivos, nós temos “escola”, “setup”, “venv”, o “git” e outras informações.

[00:40] Quando eu clicar em “POST”, observem o que vai acontecer. Ele incluiu a URL de “foto-1.png” e no projeto ele criou o “media_root” onde tem a “foto-1.png”. Vou clicar na “foto-1.png” e nós temos um “Page not found”. Que estranho! Por que isso está acontecendo? Olhe que interessante.

[01:05] Configuramos no “setting.py” do arquivo de “setup > setup - setting.py”. O que fizemos? Fizemos uma configuração e falamos assim: “temos a raiz, o MEDIA_ROOT onde vamos manter nossas imagens e temos o MEDIA_URL“. Só que em nenhum momento falamos para a nossa aplicação, para o path das nossas aplicações que temos arquivos estáticos para serem carregados - e precisamos fazer isso.

[01:36] Onde fazemos isso? Se eu preciso indicar as minhas URLs que tenho em arquivos estáticos, eu vou em “urls.py”. Vou fechar o “settings.py”. Vou deixar essa tela maior para conseguirmos ver. Acessando a “urls.py” nós vamos importar aquelas duas propriedades: o settings e o static. Lá do “django.conf” quero importar os settings e também quero importar from django.conf.urls.static import static.

[02:17] Então olhe só, temos as rotas de cada recurso e as URLs da aplicação. O que vou precisar indicar? Vou precisar falar assim: “além de todos esses paths, eu tenho a inclusão de arquivos estáticos e nós fazemos isso com sinal de maior”. Vou colocar static e vou passar essas duas variáveis.

[02:37] Vou passar lá do “(settings.MEDIA_URL(” e vou passar também o local onde estão os nossos documentos, as nossas imagens e arquivos estáticos, para isso vou colocar “document_root=settings.MEDIA_ROOT”. Fechei os parênteses? Não fechei. Deixe-me fechar os parênteses. Salvei. Abrindo o servidor parece que está tudo OK.

[03:30] Quando volto na aplicação e atualizo, olhe que interessante, a imagem carrega. O que precisamos fazer, então? Duas etapas: configuramos o settings para que ele tenha o caminho certo do MEDIA_URL e da MEDIA_ROOT, onde de fato nossos arquivos estáticos vão ficar. Depois aqui no “urls.py” nós indicamos que temos arquivos estáticos para serem carregados.

[03:59] Então, o que podemos fazer agora? Olhe só no navegador, criamos o aluno “201”. Vou acessar a página localhost:8000/alunos/201. Acessando esse aluno temos todas essas informações. Todas as vezes que acessamos às informações, conseguimos ver que tem a “foto-1.png”.

[04:14] Só que por padrão do HTML, do funcionamento, a imagem não aparece aqui. Ela fica vinculada ali em cima. Vou alterar. Então vou utilizar a “foto 2” para esse teste, em “Choose File > foto-2.png > PUT”. Ele alterou.

[04:31] Então nós temos o valor “201”, só que agora utilizando a “foto-2”. Dessa forma, conseguimos incluir os recursos de alunos arquivos estáticos!

### Upload de PDF

Uma pessoa que desenvolve precisava alterar sua API feita em Django Rest para receber imagens JPG e PNG e arquivos PDF.

Sendo assim, ela inclui o seguinte código:

                class Curso(models.Model):
                    codigo_curso = models.CharField(max_length=10)
                    descricao = models.CharField(max_length=100)
                    foto = models.ImageField(blank=True)
                    arquivo_pdf = models.FileField(blank=True, default='')

Após realizar a migração do modelo acima no banco de dados e configurar sua classe serializer, podemos concluir que:

a) A propriedade models.FileField não existe. Um erro será indicado ao subir o servidor.

b) O campo arquivo_pdf não era necessário, já que podemos realizar o upload de arquivos PDF com a propriedade ImageField.

c) **Alternativa correta:** Tanto o upload de imagens como de PDF vão funcionar como esperado.
- _Alternativa correta! Certo! As propriedades ImageField e FileField são atributos para realizar o upload de imagens e arquivos respectivamente._

### O que aprendemos?

**Nesta aula:**
- Carregamos o projeto base local e executamos o arquivo seed.py, para criar alunos e cursos;
- Aprendemos como trabalhar com arquivos estáticos no Django Rest Framework;
- Vimos na prática como realizar uma requisição POST e PUT de uma foto.

**Na próxima aula:**
Vamos entender o que é caching e como armazenar seu conteúdo num banco chave valor como Redis!

## 02. Caching
### [Caching]('https://www.django-rest-framework.org/api-guide/caching/')

NOTE: The cache_page decorator only caches the GET and HEAD responses with status 200.

Podemos colocar que nossa aplicação salve em cache alguns conteúdo e assim não precisa solicitar a todo momento para o servidor.

1. Em views.py:

                ...
                from django.utils.decorators import method_decorator
                from django.views.decorators.cache import cache_page

                class MatriculaViewSet(viewsets.ModelViewSet):
                        ...
                        @method_decorator(cache_page(20))
                        def dispatch(self, *args, **kwargs):
                                return super(MatriculaViewSet, self).dispatch(*args, **kwargs)

---

[00:00] Nessa aula vamos deixar a nossa API ainda mais performática. Como vamos fazer isso? Vamos utilizar um recurso conhecido como cache ou cachê. O que é o cache? O cache é uma forma que temos para resolver problemas de encadeamento de serviços.

[00:15] Então o cache pode ser entendido como uma cópia da fonte dos dados, por exemplo. Então podemos ter um cache de uma página Web, o cache de um XML, o cache de um disco rígido ou dos recursos que estamos disponibilizando na API.

[00:30] Podemos colocar praticamente vários conteúdos diferentes e armazenarmos no cache. Então o cache HTTP é um mecanismo de armazenamento que gerencia a adição, recuperação e remoção de respostas do servidor de origem para o cache. O cache vai tentar lidar com as solicitações que usam métodos armazenável em cache. O que isso significa?

[00:54] Significa que determinado recurso, pode ser “aluno”, “cursos” ou “matrícula” - eu vou falar “quero armazenar isso em cache”. No lugar de ficar pedindo para o servidor, o servidor pede para o URM, o URM espera uma resposta do banco de dados, devolve e traz todo esse meio de campo. Vamos armazenar isso no cache.

[01:17] Mas quem toma conta do cache? Todos os tipos de cache, os dados de objetos que são colocados nessa memória, são gerenciados também pelo servidor. Então as próximas solicitações, as informações que queremos recuperar virão do cache e não da fonte, virão do cache dos recursos que permitimos.

[01:39] Então se o item de um cache expira - seja por questão de tempo ou por alguma dependência que colocamos, alguma lógica que colocamos na nossa aplicação - o cache vai ser invalidado e a próxima solicitação vai recuperar o conteúdo e vai armazenar aquela informação no cache.

[01:59] Então isso é o cache, essa é uma forma que temos de deixar a API mais performática! Se acessarmos o Django Rest Framework e digitarmos Caching, vamos ver que uma pequena explicação sobre como o Caching funciona e como podemos usar os decorators para indicarmos que queremos armazenar em cache determinado recurso.

[aula2_video1_imagem1]

[02:25] Então antes de começarmos, tem uma nota muito importante: aqui embaixo no final temos uma nota que diz que esse cache page decorator armazena apenas requisições get e head com status 200.

[aula2_video1_imagem2]

[02:45] Então não queremos armazenar um “Page not found 404” ou alguma coisa assim no nosso cache. Não faz sentido. Então, o que armazenamos em cache? Requisições get e head com o status 200. Como coloco o cache na nossa aplicação? O local do cache onde vamos colocar vai variar de sistema para sistema e de aplicação para aplicação. Vai depender bastante do cenário.

[03:13] No nosso caso, eu vou deixar os alunos e cursos da forma como estamos trabalhando. Porém as matrículas quero armazená-las no cache. Não preciso atualizar todas as vezes as informações, os recursos disponibilizados por matrícula reais. Vou chamar de “reais”.

[03:32] Então vou pedir: “tenho essas matrículas e de tempo em tempo...” No mundo real poderíamos atualizar as matrículas de hora em hora, a cada duas horas ou dependendo da aplicação - mas eu vou colocar 30 segundos por conta no nosso tempo.

[03:57] Então, o que vou fazer? Vou acessar o usuário “admin” do Django, vou criar uma matrícula e vou pedir para essa matrícula ser armazenada em cache. Quando atualizarmos a página, lembrem que eu pedi para ela armazenar aquela informação, ele vai guardar no cache. Quando eu atualizar de novo, vou ver aquela informação lá.

[04:16] Vou criar uma outra matrícula ainda nesse tempo do escopo do cache, o tempo que o cache vai durar, e vou criar uma segunda matrícula. Quando eu atualizar a página não vou conseguir ver porque só tenho as matrículas que estão armazenadas no cache. Não estou indo no servidor toda hora buscar as matrículas. Dessa forma, vamos deixar a API mais performática.

[04:36] Então, vamos fazer isso? Para começarmos, vamos fazer a configuração para indicarmos que queremos que as nossas matrículas sejam armazenadas no cache. Então não é difícil, é supersimples! Vamos precisar de dois módulos. O primeiro é o Django Utils Decorators, então em “views.py” vou digitar from.django.utils.decorators, no plural.

[aula2_video1_imagem3]

[05:07] Vou importar o method_decorator. O segundo que vamos importar vai ser do Django Views Decorators Cache. Então vou importar, from.django.views.decorators.cache. Vou importar o cache_page. Trouxe os dois imports. Não estamos usando, por isso eles estão em cinza.

[aula2_video1_imagem4]

[05:39] Tenho o aluno, cursos e matriculas. Esse é o que quero visualizar, esse é o recurso que eu quero disponibilizar para ser armazenado no cache. Como indicamos que temos informações para serem armazenadas? A primeira coisa é armazenar o método - e esse é o método que vou indicar que quero enviar esses dados para o cache. Vou chamá-lo de dispatch, de “despachar”.

[06:09] Então, dispatch. Método def dispatch(self, args, kwargs):. Você pode me perguntar: “Guilherme, o que são esses métodos args e kwargs? Na Alura nós temos um vídeo no Alura + explicando passo a passo do que é o args e kwargs. Vou deixar ele no link da próxima atividade. Então na atividade “Para Saber Mais Args e Kwargs” vou indicar esse vídeo, que temos uma explicação bem legal para ganharmos tempo.

[06:50] Segundo! Vai ficar return super(MatriculaViewSet, self).dispatch(*args, kwags);. Salvei. Abrindo o servidor parece que está tudo OK. O que vou fazer agora? Vamos criar um super usuário para essa aplicação que não criamos ainda. Se você já tem um super usuário você já pode criar. Abri um segundo terminal.

[07:47] Então tem o primeiro rodando no servidor. O segundo vou criar um super usuário, digitando python manage.py createsuperuser. Apertei a tecla “Enter”. Vou criar um usuário chamado gui, sem endereço de e-mail. A senha é aquela que você já sabe. Nem preciso falar, é a senha curta, tem menos de 8 caracteres e é só numérica. Criei o super usuário!

[08:09] Vou fechar essa parte do meu servidor. Estou com meu servidor rolando no terminal 1. Acho que estou, se não fechei. Não, não fechei meu servidor. Vou subir, python manage.py runserver. Maravilha!

[08:26] Voltando na nossa aplicação no navegador e atualizando. Beleza, tudo funcionando! Vou acessar com o super usuário, “gui” com aquela senha supersegura.

[08:36] Em “Matrículas” eu vou criar uma nova matrícula, então vou em “ADICIONAR MATRÍCULA +”. Deixe-me minimizar aqui do lado. A matrícula vai ser para a Isabel Martins, para o curso de “Python intermediário” no horário matutino. Vou clicar em “SALVAR”. A matrícula foi criada! Volto e acesso a matrícula. Temos a nossa matrícula!

[08:57] Você pode me perguntar: “mas, Guilherme, onde controlamos o tempo para conseguirmos armazenar essas informações no cache?” É isso o que precisamos fazer também! Então, além do método dispatch para indicarmos os dados que queremos colocar o MatriculaViewSet para despacharmos no cache, vamos utilizar o method@decorators(cache_page(20)). Acho que consigo em 20 segundos mostrar.

[09:32] Abrindo o servidor está tudo OK. Olhe o que eu vou fazer. Vou atualizar. Nós temos essas informações.

[09:37] Vou criar mais uma matrícula em “ADICIONAR MATRÍCULA +”. Então a matrícula vai ser do Renan Melo para o curso de “Python intermediário” também no período matutino. Salvei. Temos duas matrículas. Quando vou lá e atualizo as matrículas, só tenho uma matrícula exibida.

[09:53] Por quê? Porque não estou indo no servidor. Estou buscando as informações que estão armazenadas no cache. Quanto tempo essas informações serão expiradas? Serão expiradas em 20 segundos, que foi o tempo que coloquei.

[10:08] Porém se eu ficar atualizando, em um determinado momento nós teremos a segunda matrícula sendo exibida. Essa é uma maneira de deixarmos a nossa API mais performática.

### Para saber mais: args e kwargs

Como havia comentado, segue um link sobre [args e kwargs - multiplos parâmentros no Python]('https://cursos.alura.com.br/args-e-kwargs-multiplos-argumentos-em-python-c253').

**A solução mais prática: a variável args**
- O uso de args _possibilita múltiplos argumentos_ a serem recebidos _em uma fuunção_
- Não precisamos mais montar a lista de antemâo: os argumentos adicionais dentro args são _armazenados_ automaticamente _em uma tupla dentro da função_

**A solução mais dinâmica: a variiável kwargs**
- O uso de kwargs _possibilita múltiplos argumentos chaves_ a serem recebidos _em uma função_
- Esses argumentos são adaptados _como chaves de um dicionário_. Podemos interpretar essas chaves _independente da ordem em que foram chamadas_

### Instalando o Redis

Redis é um banco de dados de chave/valor servidor de cache. Disponível em: https://redis.io/download

1. No terminal na pasta do arquivo de downloads:

                make

2. No terminal para subir o servidor devemos:

                src/redis-server

---

[00:00] Incluímos na memória em cache as informações de matrículas, alguns recursos de matrículas. Isso ficou muito legal. Só que em um cenário real, em um projeto do mundo real, o que acontece? Geralmente, a memória em cache é armazenada em algum lugar - e um dos lugares utilizados no mundo real, nos projetos grandes é o Redis. Um possível lugar. Existem outros.

[00:25] Mas o que é o Redis? O Redis é um banco de dados de chave e valor onde nós podemos utilizar como banco de dados ou armazenar o cache. O que podemos fazer? Podemos instalar o Redis na nossa máquina, configurar, subir o servidor do Redis, configuração o Django para conversar com o Redis e armazenar as informações do cache no Redis.

[00:49] Continuamos utilizando banco de dados em que estamos, mas o cache vai ser armazenado no Redis. Vamos fazer isso? Para começarmos, vamos precisar fazer o download do Redis. Então na página do Redis eu vou vir em “Download”.

[01:02] Temos várias versões, mas eu recomendo utilizar essa versão estável. Nesse momento do curso é a versão 6.0. Então faça o download do 6.0.9. Eu já fiz o download para economizarmos tempo. Então quando estiver fazendo download, se você quiser, pode dar um pause no vídeo. Depois continuaremos.

[01:21] Então já fiz o download do Redis. O que vou fazer? Para eu instalar o Redis na minha máquina, vou abrir um terminal e vou acessar a pasta do Redis. Então vou digitar “cd” com o diretório de onde está essa pasta.

[01:38] No meu caso é Users/guilhermelima/Downloads/deis-06.0.9, mas no seu caso você indicar o caminho dessa pasta. Aperto a tecla “Enter”. Se eu digito ls, nós podemos ver que estou nessa pasta. Para eu conseguir instalar o Redis, vou digitar make e apertar a tecla “Enter”. Ele vai começar a instalar uma série de dependências.

[01:56] Dois pontos importantes enquanto está instalando: na Alura nós temos um treinamento de Redis. Então você que quer aprofundar seus conhecimentos nesse banco de dados chave e valor, tem um treinamento na Alura. Você pode aprofundar seus conhecimentos também no Redis e entender como esse banco trabalha e pode utilizar esse banco para armazenar outras informações também. O curso é superlegal. Eu super recomendo também!

[02:20] Fiz a instalação do Redis, executei o make e depois ele dá até uma boa ideia, que é rodar o make test. Se você quiser executar o make test, você pode executar para ver se houve algum erro. Enquanto está instalando você pode dar uma olhada no curso de Redis, bater uma flexão ou tomar um suco de laranja. Fique tranquilo!

[02:44] Executei o make, executei o make test e vi que está tudo OK. Vamos subir o servidor do Redis. Para isso vou digitar src/redis-server. Quando aperto a tecla “Enter”, olhe lá o servidor do Redis já no ar!

[03:00] Está funcionando o meu Redis! Ainda não configuramos ele para conversar com o Django, mas só para fazermos um teste para entendermos como o Redis funciona, a primeira coisa que vou fazer é abrir uma outra aba do terminal.

[03:22] Utilizei as teclas “Command + T” para abrir outra aba, vou acessar a pasta do Redis. e o que vou fazer agora vai ser acessar essa pasta “src”, então vou digitar cd src. Aqui temos uma série de comandos do Redis.

[03:43] Esses comandos estão listados na página da documentação dele. Então temos esse “Commands”, que tem uma série de comandos e série de coisas que podemos fazer com o Redis.

[03:552] Vou fazer a coisa mais simples e possível, que é abrir a linha de comando dele. Vou colocar um ./redis-cli no terminal. Apareceu aqui 127.0.0.1:6379, que é porta onde ele está sendo utilizado. Então, o que quero armazenar?

[04:11] Quero armazenar um determinado valor. Vou colocar set “valor” 5. Beleza, ele deu um “OK”. Se eu digitar get valor, ele me devolverá o 5!

[04:31] E o Redis funciona dessa forma. Muito simples!

[04:33] O que vamos fazer no próximo vídeo? Vamos configurar o Django para conversar com o Redis, para conectar o Django e o Redis e falar: “o que for memória cache eu quero armazenar no Redis”.

### Integrando Django e Redis

[DJANGO-REDIS]('https://pypi.org/project/django-redis/')

1. Para instalar, no terminal:

                pip install django-redis

1. Em settings.py, devemos:

                ...
                CACHES = {
                        "default": {
                                "BACKEND":"django_redis.cache.RedisCache",
                                "LOCATION":"redis://127.0.0.1:6379/1",
                                "OPTIONS":{
                                        "CLENT_CLASS":"django_redis.client.DefaultClient",
                                }
                        }
                }


                #Para que não haja uma interferência do REDIS no ADMIN do DJANTO

                SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
                SESSION_CACHE_ALIAS = "default"

---

[00:00] Subimos o nosso servidor no Redis, temos a aplicação Django rodando. Como fazemos para conectarmos uma com a outra? Em primeiro lugar, existe um módulo que nos auxilia nessa comunicação do Djago com o Redis. Quero mostrar ele para você. Se eu digitar django-redis no campo de pesquisa do Google, observe que vai aparecer no “django-redis PyPl”.

[00:24] É uma biblioteca que vai nos auxiliar nessa comunicação entre o Django, a API com o Redis. Vamos ver! Cliquei para copiar e instalar essa dependência com as teclas “Command + J”. Vou parar nosso servidor, vou apertar as teclas “Command + V”.

[00:44] Então digito pip install django-redis no Sulbime, aperto a tecla “Enter” e ele instala. Só para mantermos nosso projeto organizado, vou digitar pip freeze > requirements.txt e apertar a tecla “Enter”. Maravilha”

[00:59] O que preciso fazer agora? Instalamos o Django Redis. Agora precisamos fazer uma configuração para de fato conectarmos o Django com o Redis em relação ao cache, porque queremos guardar o cache lá. Vou abrir o “setup > settings.py” e escrever um pouco para fazer essa configuração.

[01:18] Em primeiro lugar, como queremos alterar o cache da nossa aplicação, vamos criar uma variável chamada CACHES =. Vou dizer algumas configurações. Em primeiro lugar, vou passar uma configuração default. Então vou criar default: { e vou passar as nossas configurações.

[01:44] Em primeiro lugar, o que vamos precisar especificar? Vamos precisar dizer qual é o nosso back-end no Redis e quem vai ser responsável por realizar esse back-end no Redis. Então vou escrever “BACKEND”:. Agora vou especificar essa biblioteca que estamos utilizando, que é o django_redis.cache.RedisCache.

[02:22] Então informei que nosso BACKEND vai ser django_redis. Deixe-me tirar aqui do lado só para não nos confundirmos, cache.RedisCache. Vou passar uma vírgula aqui e passar mais uma configuração, qual é a porta, qual é o caminho para o Redis. Então vou escrever ”LOCATION”: e vou passar o caminho do Redis.

[02:48] Então vou passar entre aspas também, “redis://” e o endereço. Podemos ver esse endereço quando fizemos aquele teste. Então vou digitar 127.0.0.1: 6379. Aqui vou passar uma configuração que eu quero que seja especificado essa porta no Redis.

[03:15] Então vou utilizar aqui um /1 para especificar que é essa porta que vamos ter como principal nesse LOCATION. Vou passar por último uma configuração para a nossa classe de cliente. Então vou colocar entre aspas um “OPTIONS”: e vou passar entre chaves o “CLIENT”.

[03:47] “CLIENT_CLASS”: e vou passar entre aspas também “django_redis.client.DefaultClient” com a letra de “d” maiúscula. Vou passar uma vírgula também. Salvei e vamos rodar o servidor para vermos se está tudo certo.

[04:23] Parece que está tudo OK. Então essa é a configuração que precisamos fazer no lado do Redis em relação aos nossos caches.

[04:31] Uma outra coisa importante é que precisamos especificar o mecanismo de seção nas nossas configurações. É importante fazermos isso para o Redis não interferir no painel de administração do Django e na seção atual. Por exemplo: queremos que o Redis guarde os nossos caches de seção, mas no admin do Django queremos que o Redis não interfira nas seções do nossa admin.

[04:57] Então, para isso, vamos criar uma variável chamada SESSION_ENGINE =django.contrib.sessions.backends.cache. O que isso significa? Significa que não queremos que o Redis interfira no nosso painel de administrador do Django. Para finalizar, vou passar uma SESSIONS_CACHE_ALIAS = e vou dizer qual vai ser a nossa seção de cache principal, que vai ser o ”default”.

[05:49] Então vou criar uma SESSIONS_CACHE_ALIAS = “default”, que acabamos de configurar ali. Vamos ver o servidor. Vou parar e rodar mais uma vez só para ficarmos com nossa tela limpa. Maravilha!

[06:23] Essas são as configurações necessárias para conseguirmos conectar o Redis com uma aplicação Django e armazenar o cache lá. Legal, só que precisamos fazer um teste. Se observarmos aqui, vou deixar na porta do servidor, observe que não temos nenhuma informação passando.

[06:40] O que vou fazer? Na nossa aplicação vou clicar em “http://localhost:8000/matriculas”. Quando vamos para o servidor, parece que está tudo OK também. Vou criar aqui também uma nova matrícula. Vai ser no período matutino, o aluno é “Ana Lívia” para o “Python para Data Science”. Vou deixar esse mesmo. Clico em “POST”. Ele criou. Se voltamos nas nossas listas de matrículas, veremos que só temos duas.

[07:04] Por quê? A outra informação está armazenada no Redis. E vai durar quanto tempo? O tempo que especificamos na nossa view command p. Vou acessar as nossas “views.py” para vermos. Olhe só, deixamos 20 segundos.

[07:16] Esse tempo, se você quiser utilizar em outros lugares também, poderia criar no “settings.py” uma variável nova chamada CACHE_TTS, por exemplo, e informar o tempo e utilizar essa variável na nossa “views.py”. Se quisermos padronizar o tempo de cache de todos as nossas informações.

[07:37] Então, se eu atualizo e já tinha passado dos 20 segundos, aparecerá a nossa outra informação. Dessa forma, nós conseguimos visualizar todas as informações que passamos para o Redis também. Então estamos utilizando o Redis agora na nossa base de dados. Então, isso ficou bem legal!

[07:55] O último teste que quero fazer com vocês é o seguinte: eu vou derrubar o Redis. Derrubei o Redis. Se voltar na aplicação e atualizo, olhe o que vai acontecer.

[08:07] Tivemos um erro de conexão! Então é importante que quando formos utilizar o Redis, que nos lembremos de subir um servidor. Se estivermos utilizando o Docker, por exemplo, podemos fazer um docker compose e subir todos os servidores, todas as dependências e bancos que precisamos na nossa aplicação. Porém, se o Redis não estiver habilitado não vamos conseguir subir. É uma informação importante para o nosso curso!

[08:33] Temos essa configuração Redis, eu vou deixá-la disponível para vocês. Vou só comentar ela aqui, deixe-me só minimizar. Vou comentar e olhe o que vai acontecer. Quando eu comento essas linhas, salvo e atualizo a minha aplicação, nós voltamos para a página de matrículas. Só que nesse caso, estamos utilizando não mais o Redis, estamos utilizando o cache mesmo do nosso servidor, armazenando as informações no nosso servidor local.

[08:57] Então foi só para manter nosso curso um pouco mais rápido, fica a seu critério. Se você quiser deixar assim, o Redis aberto e utilizando o cache, é só você tirar o comentário dessas linhas no Sublime. Se você não quiser utilizar o Redis, você pode deixar ele assim. Eu só quis mostrar mais ou menos como funciona, como exemplo.

### Definindo cache

Nesta aula, integramos o Django com o Redis para armazenar o cache da API, e isso ficou muito legal. Agora, analise as sentenças abaixo:

        1 - Um cache é uma cópia de uma fonte de dados.
        2 - É possível ter um cache de páginas da web.
        3 - É possível ter um cache de um JSON ou cache de XML.

Após analisar as afirmações abaixo, marque a resposta que indique as verdadeiras.

a) Apenas as afirmações 1 e 3 são verdadeiras.

b) A afirmação 3 não é verdadeira. Apenas as afirmações 1 e a 2.

c) **Alternativa correta:** Todas as afirmações são verdadeiras.
- _Alternativa correta! Certo! O cache é uma maneira de resolver o problema de velocidade de encadeamento de serviços. Um cache é uma cópia de uma fonte de dados. Você pode ter um cache de páginas da web, um cache de XML ou um cache de um disco rígido. Você pode ter um cache de praticamente qualquer coisa._

### O que aprendemos?

**Nesta aula:**
- Aprendemos como melhorar a performance da API utilizando cache;
- Instalamos e subimos o servidor do Redis;
- Integramos o Django e o Redis.

**Na próxima aula:**
Vamos internacionalizar a API e aprender na prática como negociar o tipo de mídia do conteúdo da resposta de uma requisição!

## 03. Limitando ações no Viewset e Permissões
### Internacionalização - i18N

Podemos internacionalizar a requisições a nossa API.

[DJANGO-i18n]('https://docs.djangoproject.com/en/3.2/_modules/django/views/i18n/')
[DJANGO-REST-i18n]('https://www.django-rest-framework.org/topics/internationalization/')

1. Em settings.py:

                MIDDLEWARE = [
                        ...
                        'django.middleware.locale.LocaleMiddleware',
                ]

---

[00:14] Elas aparecem em português por conta do language code da nossa aplicação. Então aqui está português do Brasil. Se coloco, por exemplo, LANGUAGE_CODE = ‘en’. Vamos receber essas mensagens em inglês. Então vou voltar e realizar mais uma requisição post. Temos essas mensagens em inglês.

[00:30] Vou deixar como português do Brasil mesmo, só para conseguirmos visualizar, vou deixar nossa aplicação como estava. O que quero fazer agora é deixar a minha API compatível com todos os idiomas. Então, dependendo da requisição, eu quero exibir essas mensagens em espanhol ou em inglês.

[00:51] E existe uma forma de fazermos isso! Vamos internacionalizar a nossa API. Se digitar i18n django rest na pesquisa do Google, olhe só! Nesse primeiro link que vai aparecer, “Internacionalization – Django REST framework”.

[01:03] Existe uma forma muito fácil e muito simples de internacionalizarmos a nossa API incluindo um Middleware, um LocalMiddleware no MIDDLEWARE_CLASS. Dessa forma, o que vai acontecer? Quando eu incluir esse código, com base na requisição eu vou poder dizer se quero exibir essas mensagens em português, em inglês, espanhol ou em outros idiomas que o Django dá suporte.

[01:25] Então no Sublime vou subir a página, vou no “MIDDLEWARE = [” e vou colocar ele no final, com as teclas “Ctrl + V”, mais a vírgula. Teclas “Command + J” e está tudo certo no servidor.

[01:35] Para executar esse teste eu vou utilizar o post, só para visualizarmos. Então na página no navegador aberto e com o “POST” para alunos vazio. Quando clico em “Send”, aparece que este campo é obrigatório. Se vou no “Headers”, vou colocar mais um atributo. Vou colocar aqui, vou alterar esse último mesmo. Esse não consigo. Vou alterar o debaixo.

[01:59] Então vou colocar Accept-Language e vou poder escolher um idioma. Vou deixar como, por exemplo, en. Quando clico em “Send”, observe que temos agora essa requisição com os campos em inglês.

[02:14] Se eu quiser deixar, por exemplo, o espanhol da Espanha, digito es-es. Quando clico em “Send”, aparece “Este campo es requerido”. Eu não sei falar em espanhol, mas é alguma desse tipo.

[02:26] Olhe que simples! Incluímos o LocalMiddleware. Agora nas requisições, se incluirmos no “Headers” um Accept-Language indicando o idioma que queremos, nós internacionalizamos a API. E se eu não passar esse valor? Se eu não deixar esse valor? Nós receberemos as mensagens padrões por conta do LANGUAGE_CODE do português do Brasil.

### Alterando mensagens padrões

Podemos padronizar as mensagens de erro do DJANGO:

1. Criar uma pasta na raiz do projeto, path Locale

1. Em settings.py:

                ...
                LOCALE_PATHS = (
                        os.path.join(BASE_DIR,'locale/')
                )

1. No terminal, devemos dar o comando para o DJANGO:

                python manage.py makemessages -l pt_BR

1. O DJANGO vai criar um arquivo com todas as mensagens em inglês, devemos escrever em mgstr a nova mensagem.

1. No terminal devemos compilar para o DJANGO:

                python manage.py compilemesages -l pt_BR

---

[00:00] Vimos como internacionalizarmos a API. Isso ficou bem legal, só que existe um passo a mais que podemos dar. Por exemplo: essas mensagens que vimos tanto no português, no inglês e no espanhol são mensagens padrões. Só que é possível alterar essas mensagens padrões.

[00:21] Por exemplo: no lugar de usar “Este campo é obrigatório”, se eu utilizar o Accept Language com o inglês, por exemplo, posso identificar o conteúdo dessa mensagem e colocar uma outra mensagem - e é isso que vamos ver nesse vídeo, como alterar essas mensagens padrões e personalizar essas mensagens.

[00:41] Então vou utilizar o exemplo só do português. Por questão de tempo não vamos conseguir alterar as mensagens de espanhol e inglês, mas o princípio vai ser o mesmo. Em primeiro lugar, vamos criar uma pasta e indicar no “settings.py” onde ficarão os arquivos com a localização de cada idioma. O que vou fazer? Vou criar uma pasta dentro de “setup”? Não, vou criar aqui fora!

[01:09] Vou chamar essa pasta de “locale”. Criei essa pasta. Agora, aqui dentro do “settings.py” vou indicar o caminho dessa pasta como a localização. Então vou digitar LOCALE_PATHS, no plural, vai ser igual, entre parênteses vou passar as localizações dessa pasta. Então, (os.path.join(BASE_DIR, 'locale/')).

[01:49] O que fizemos? Indicamos que existe uma pasta com a localização das mensagens personalizadas que vamos criar. O que eu vou fazer agora? Vou abrir o terminal. Deixe-me parar. Vou abrir o terminal e pedir para que o “manage.py” do Python crie para mim as mensagens indicando o idioma do português do Brasil.

[02:14] Então vou digitar python manage.py makemessages -l para indicar o idioma e colocar pt_BR. Apero a tecla “Enter” e ele vai processar e criar essa pasta para nós. Legal! Processou e criou uma pasta. Vamos abrir aqui do lado e minimizar só para vermos o que tem nesse arquivo “locale”.

[02:47] Temos um português do Brasil, uma pasta com “LC_MESSAGE” e tem um arquivo chamado “django.po”. O que é esse arquivo? Esse arquivo contém todas as mensagens padrões que temos na nossa aplicação. Vou procurar essa mensagem. Esse campo é requerido e não pode ficar em branco. Vou apertar as teclas “Ctrl + F” e “Ctrl + V”. Achei essa mensagem.

[03:09] Quero alterar essa mensagem. Falar assim: msgstr “Opa, deu ruim. Esse campo não pode ficar em branco”. Salvei. O que vou fazer agora? Alterei esse arquivo. Salvei. Vou subir meu servidor mais uma vez, digitar manage.py runserver. Estou com um erro aqui que é uma lista e não uma tupla. Deixe-me ver o que eu errei. Esqueci da vírgula nesse “locale”! É isso mesmo, esqueci a vírgula.

[03:45] Agora abrindo com as teclas “Command + J”, vou rodar o servidor mais uma vez. Maravilha, está funcionando! O que vou fazer? Vou na página da aplicação e clicar em “Send”. Está com a mensagem Language_Code em português. Vou tirar porque temos o padrão e não apareceu. Continua “Este campo é obrigatório”.

[04:00] E a mensagem que tínhamos programado era “Opa, deu ruim. Esse campo não pode ficar em branco”. Por quê? Sempre quando fazemos uma alteração nessas mensagens padrões, é necessário que compilemos essas mensagens para o Django entender que as mensagens padrões foram alteradas. Como faço essa compilação dessas mensagens?

[04:20] Muito simples! Vou abrir o terminal mais uma vez. Parei e vou digitar python manage.py e pedir para ele compilemessages, no plural também, - l para indicar a mensagem que quero compilar, pt_BR. Vou apertar a tecla “Enter” e ele vai compilar essas mensagens. Pronto, fez a compilação! Vou subir o servidor mais uma vez e quando eu pedir para dar um “POST” em http://localhost:8000/alunos/ com todos os campos vazios, teremos a mensagem personalizada.

[05:03] Então apareceu “Opa, deu ruim”. Qualquer outra mensagem que você quiser achar, observe que naquele arquivo “django.po” temos uma flag, que é msgid, o id da mensagem.

[05:18] Então ele pede um valor numérico, uma data válida. Você pode alterar todas essas mensagens, se caso você queira personalizar e não utilizar a padronização que o Django já traz dos idiomas, a tradução. Isso você pode fazer para qualquer outro idioma.

[05:34] “Eu preciso personalizar as mensagens do inglês, uma coisa específica”. Então você pode criar lá, um makemessages – l com en, por exemplo, do inglês. Vai criar esse arquivo “django.po”. Você faz as alterações que quiser. Quando esse arquivo estiver finalizado nas alterações dessas mensagens você só vai fazer o compilemessages.

[05:57] É importante indicar a flag - l com o nome, porque senão ele vai compilar todas as mensagens em todos os idiomas que ele tem. Quando fazemos assim, fica muito mais rápido. Então essa é uma forma que temos para personalizarmos as mensagens padrões do Django.

### Content Negotiation

[DJANGO_REST-PARSERS]('https://www.django-rest-framework.org/api-guide/parsers/')

[DJANGO_REST-RENDERS]('https://www.django-rest-framework.org/api-guide/renderers/')

---

[00:00] Sempre que faço uma requisição para um determinado recurso da API, seja ele matrículas, alunos ou curso, eu recebo a resposta da requisição no formato de som. Temos esse visual bonito do Django REST, mas na verdade a informação importante que está sendo passada para essa requisição, a nossa resposta, está no formato de som.

[00:24] Podemos garantir isso abrindo o Postman. Na página vou escolher um “GET” em http://localhost:8000/cursos/. Nós temos o formato JSON. Qual é o formato além do formato JSON que o Django REST fornece como suporte? Existem outros tipos de mídia que podemos responder às requisições? Existe!

[00:44] Vamos acessar a documentação. Vou digitar django rest na barra de pesquisa do Google e clicar no primeiro link. Acessando a página principal do Django REST, vou vir no “API Guide > Parsers”, para darmos uma olhada. Observe que temos uma explicação vasta de como funciona essa questão de parsear as nossas respostas, modificar o tipo da mídia em que estamos trabalhando.

[01:09] Então temos, por exemplo: YAML e existe um módulo para respondermos as requisições do tipo YAML e XML também. O que eu quero fazer? A nossa API funciona bem com o formato JSON. Então, tanto da parte do Postman como a nossa navegação, que é esse cenário que o Django REST proporciona para testarmos as nossas requisições.

[01:33] Quando inserimos um Parser de XML de YAML perdemos os recursos desse layout, desse visual do Django REST. Porém, isso não é tão relevante. Por quê? O mais importante serão as outras aplicações, sistemas ou até outras APIs consumindo nossa API.

[01:51] Então o relevante é o que estamos passando aqui. O que eu quero mostrar? Será que é possível nós alterarmos a nossa API para falarmos assim: “olhe, quero essa resposta JSON ou quero essa resposta em XML” e passarmos os dados com base na nossa requisição, mesmo que não tenhamos mais essa parte visual? É interessante. Vamos mostrar como fazemos isso?

[02:13] Para isso, vou seguir a documentação. Vamos precisar instalar um módulo chamado djangorestframework-xml. Vou copiá-lo. Vou parar o servidor e digitar pip instal djangorestframework-xml. Ele instalou. Só para não perdermos o costume, pip freeze > requeriments.txt. Maravilha!

[02:41] Lá no “requeriments.txt” já temos agora o djangorestframework.xml instalado. O que preciso fazer também? Vamos ver na documentação. Existem duas classes que são importantes modificarmos para conseguir responder as requisições em XML ou em JSON que é lá das configurações do REST_FRAMEWORK, o DEFAULT_PARSER_CLASSES e o DEFAULT_RENDERER_CLASSES. Vou fazer o seguinte.

[03:10] Vou copiar esse link e abrir o Renderers, para já deixarmos no esquema para visualizarmos. Então olhe só, por padrão olhe o que temos. Temos as respostas feitas em JSON. Para garantirmos isso, se dou um “GET” em http://localhost:8000/cursos/. Não apareceu nada porque meu servidor não está de pé. Então vamos subir o servidor, manage.py runserver. Beleza, agora sim.

[03:37] Dou um “GET” e os cursos vão aparecer aqui embaixo. Onde mudo para identificar qual é o tipo de resposta da mídia que vou querer? Existe uma propriedade chamada Accept, um header no cabeçalho. Então no “Accept” vou indicar que quero um application/json e quando clico em “Send”, dá. Quando digito application/xml, por exemplo, olhe o que acontece.

[04:08] “Não foi possível satisfazer a requisição do cabeçalho Accept”. Vamos precisar configurar! Então, o que eu vou fazer? Vou nas configurações. Vou copiar essas duas propriedades. Repare que isso é uma informação importante. O DEFAULT_PARSER e o DEFAULT_RENDERER, essas duas propriedades, essas duas configurações. Vou em “setup > settings.py”. Observe que estou nas configurações do rest_framework, vou colocar uma vírgula e copiar aqueles dois.

[04:37] Salvei a informação. O meu servidor executou mais uma vez. Está tudo OK. Vou para a página da aplicação e clicar mais uma vez em “Send”. Olhe que interessante, agora recebemos a resposta da requisição em XML.

[04:49] Isso ficou legal! Se eu colocar application/json no campo “Accept”, vamos ver o que vai acontecer? Quando clico em “Send” aparece a mensagem “Não foi possível satisfazer a requisição”. Ganhamos o XML, mas perdemos o JSON - e mais: se formos na nossa navegação, olhe como ficou o http://localhost:8000/cursos/.

[05:07] Está um XML aqui, mas não temos condições de mandar requisição post igual tínhamos quando era o json. Então, o que vou fazer? Vamos precisar também, além de habilitar o XML, habilitar o JSON. Então vamos precisar de um Renderer do JSON. Vou copiar do rest_framework.renderers.JSONRenderer e vou passar ele aqui também. Ele vai falar Existe o JSONRenderer e eu vou precisar do Parser do JSON também. Então lá em cima temos o Parser do JON. Vou copiar esse e colar ele aqui também. Salvei.

[05:44] Se volto para a página da aplicação e dou mais uma requisição, temos um JSON. Se volto e coloco XML, temos a resposta em XML. Maravilha! Então conseguimos dizer para o rest_framework que existem duas classes principais para as respostas das nossas requisições. Temos o JSON e o XML e elas serão definidas através desse cabeçalho Accept. Por outro lado, na navegação vamos continuar sempre com esse visual estranho do localhost:8000, um XML não semântico.

[06:26] Uma outra informação interessante é que quando eu digito application/sml no campo “Accept”, observe que o XML que aparece aqui não é o XML mais semântico, mais intuitivo e claro possível. Ele faz uma lista de itens, de cursos.

[06:39] No nosso caso, o que temos não seria nem o nome do curso. Ele faz uma lista de cursos e devolve esse XML não tão semântico, mas funciona e faz sentido. Por outro lado, perdemos aquela navegação da nossa tela principal.

[07:00] Você vai continuar daqui. Você fala: "não vou, Gui". Essa parte da navegação da tela só vou consumir a API agora com outras APIs ou outras aplicações e outros sistemas. Você deixa a sua configuração assim com o JSON e o XML.

[07:19] Não vou utilizar o XML. Mostrei para você, mas não vou utilizar. O que posso fazer? Comento essas linhas 143 e 147 de “setup > settings.py” e salvo. Se eu voltar e atualizar, nós temos uma navegação estranha.

[07:31] Vou derrubar meu servidor e subir mais uma vez. Nós vamos ver que ele vai estar agora com as configurações certas. Olhe só, não deu certo também!

[07:40] Deixe-me atualizar mais uma vez. Para garantir, vou até abrir uma aba anônima só para visualizarmos, no http://localhost:8000/cursos... Nós temos só a resposta em XML. Isso pode estar acontecendo porque ficou armazenado no cache dele que eu quero as respostas no XML. O que posso fazer para tentar recuperar a parte do admin do Django?

[08:09] Vou tirar essas duas classes e falar que não tenho essas propriedades, da linha 141 até a 148 de “setup > settings.py”. Só essas duas, não vou tirar todas as configurações. Salvei. Vamos atualizar e ver. Agora sim, beleza! Então aparecerem os dois.

[08:24] Você pode me falar: “não quero usar essa parte visual do Django”. Não tem problema. Se você não quiser usar essa parte visual, pode deixar com o XML, com o JSON. Por que eu vou deixar? Vou deixar porque nós vamos fazer mais alguns testes e faze sentido executarmos aqui e não precisarmos ir para Postman também.

[08:48] Mas em uma aplicação real, fica a seu critério atender às requisições de XML, de JSON - ou como vimos, os Parserers para YAML, por exemplo e outros tipos.

### Negociação de conteúdo

Quando criamos uma API com Django Rest Framework, o JSON é o tipo de mídia padrão das respostas. Porém existem outros tipos de mídia como XML ou YAML por exemplo.

Sabendo disso, em relação ao Django Rest, podemos afirmar que:

a) **Alternativa correta:** O tipo de mídia padrão pode ser definido globalmente, ao incluir o DEFAULT_PARSER_CLASSES e o DEFAULT_RENDERER_CLASSES nas configurações do REST_FRAMEWORK do settings.
- _Alternativa correta! Certo! A estrutura REST inclui várias classes Parser e Renders integradas, que permitem aceitar solicitações com vários tipos de mídia._

b) Na estrutura do Django Rest, o único tipo aceito é o JSON.

c) Na estrutura do Django Rest, os tipos de mídia aceitos são JSON e YAML.

### O que aprendemos?

**Nesta aula:**
- Vimos como inclui um middleware de internacionalização;
- Aprendemos como alterar as mensagens padrões do Django;
- Incluímos na prática a negociação de conteúdo, seja ele um JSON ou XML com base no cabeçalho Accept.

**Na próxima aula:**
Vamos aprender como escrever testes automatizados das requisições GET, POST, PUT e DELETE de um determinado recurso!

## 04. Testes
### Cenário de Teste

1. Em tests_cursos.py:

                from rest_framework.test import APITestCase
                from escola.models import Curso
                from django.urls import reverse

                class CursosTestCase(APITesteCase):
                        def setUp(self):
                                self.list_url = reverse('Cursos-list')
                                self.curso_1 = Curso.objects.create(
                                        codigo_curso='CTT1', descricao='Curso teste 1', nivel='B'
                                )
                                self.curso_2 = Curso.objects.create(
                                        codigo_curso='CTT2', descricao='Curso teste 2', nivel='A'
                                )
                        
                        def test_falhador(self):
                                self.fail('Teste falhou de propósito.')

2. No terminal:

                python manage.py test

---

[00:00] A API tem um comportamento que esperamos. Porém, em nenhum momento escrevemos algum teste. Um teste é um assunto muito denso, daria mais de um curso fácil na Alura. Porém, para termos uma base do que se trata e como realizamos os nossos primeiros testes, eu sugiro que nós façamos um teste relacionado às requisições que fizemos na API.

[00:23] Então se eu acessar a pesquisa do Google e digitar django rest teste, por exemplo, observe que nesse primeiro link tem uma explicação vasta de como utilizamos o teste utilizando esse APIRequestFactory.

[00:37] Eu quero mostrar uma forma um pouco mais simples de realizar os testes seguindo essa mesma ideia. Realizar um teste de algum recurso da nossa API, por exemplo, de um curso. Quero realizar o teste das principais requisições. Por exemplo: o GET, o PUT, o DELETE e o POST.

[01:01] Temos a documentação ensinando como utilizamos a APIRequestFactory. Só que quero mostrar uma forma um pouco mais simples. A primeira coisa, o que vamos fazer?

[01:15] O teste que vamos aprender a realizar pode ser aplicado nos nossos outros recursos também. Tanto para alunos, como para matrículas ou para outros módulos e outros recursos que você está desenvolvendo. A primeira coisa: sempre temos uma pasta de “tests.py”. Não vamos utilizar esse arquivo. Por quê?

[01:36] Quero criar um teste relacionado ao curso e quero deixar o desafio para você os outros testes de alunos e matrículas. Então, no lugar de escrever todo o teste aqui, eu vou criar uma pasta que vou chamar de “tests”. Como vamos ter mais de um arquivo, vou criar um arquivo “initpy”, para nós conseguirmos executar.

[02:06] Vou criar um arquivo chamado “tests_cursos.py” e aqui vamos criar os nossos testes de curso. Você pode me falar: “vou criar o teste para testar as requisições de alunos”. Aí você cria um outro arquivo e nós mantemos o nosso código organizado. Então, vamos lá! A primeira coisa que vamos fazer é importar as bibliotecas necessárias para realizarmos o teste.

[02:33] O primeiro módulo que vamos importar vai ser do rest_framework. Temos um módulo de teste chamado APITestCase. Então, from rest_framework.test import APITestCase.

[02:50] Outra coisa - vamos testar o quê? Vamos testar as principais requisições de curso. Então vou precisar do módulo de curso. Então vou trazer também o módulo de curso, from escola.models import Curso. Vamos escrever a nossa classe de teste.

[03:12] Essa classe vou chamar de class CursosTestCase(): e aqui dentro vou passar a propriedade que importamos, a APITestCase. Agora acontece o quê? Não quero utilizar para os meus testes os dados da API, os dados que no caso estão em local, mas já estão em produção. Não quero utilizar esses dados. Eu quero que outros dados sejam gerados para teste, quero um cenário de teste.

[03:39] Então, para isso, nós vamos criar uma função chamada setUp. O que acontece? Cuidado com a forma que você vai escrever esse def setUp():. Vou passar a instância que vamos estar trabalhando com o self. Então a primeira coisa que vamos precisar fazer é falar assim: “quais são as URLs que vamos trabalhar? Qual a lista de URLs que vamos trabalhar?”

[04:08] Então se apetarmos as teclas “Command + P” e digitarmos URLs, nós registraremos uma rota de cursos onde demos esse basename Cursos - e é esse basename que vamos precisar passar para essa nossa lista de URLs. Por que estou falando isso? Observe que quando estamos em Cursos eu posso testar um GET, posso testar um POST, eu posso testar um GET com detalhes de um determinado curso.

[04:38] Então nessa lista não vou precisar ficar passando manualmente, localhost//8000/cursos/1, por exemplo. Não! Eu quero que esse próprio cenário de teste entenda quais são as principais URLs desse recurso. Então vou passar list_url. Então vou passar esse basename que criamos de cursos.

[05:05] Porém, é importante que utilizamos um outro módulo para conseguirmos fazer essa manipulação das URLs de curso. Lá do django.urls existe um módulo chamado reverse. Então lá do django.urls import reverse. Aqui dentro vou falar para o reverse que quero toda a lista de URLs relacionada a cursos. Só que aqui tem uma coisa interessante.

[05:33] Vou passar um -list e ele vai trazer para mim e vai conseguir manipular todas as listas dos cursos que temos. Tenho as URLs principais que vou trabalhar na minha aplicação, armazenadas nesse list_url. O que preciso fazer também? Preciso criar um curso para essa instância!

[05:52] Lembra que eu falei que nós não vamos utilizar os cursos que temos na base de dados. Então vou criar um self.curso_1 e vou dizer que esse curso vai ser um Curso do nosso modelo .objects.create e vou passar as propriedades do curso que quero criar.

[06:10] Eu vou abrir o model só para termos certeza das informações que estamos passando. O curso tem um código. O curso tem uma descrição e tem também um nível, que eu já vi lá. O código do curso, como estamos em um cenário de teste vou falar “curso de teste, teste 1”, por exemplo, a descrição desse curso vai ser Curso teste 1. O nível passamos uma das três letras. O básico para o B, intermediário e avançado. Vou dizer que esse vai ser o básico.

[06:48] Legal, criei o curso 1 e vou criar o curso 2. Apertei a tecla “Enter” e criei o curso 2. O curso 2 vai ser o CTT2, o Curso de teste 2 e aqui do básico vai passar para o A, por exemplo. Salvei.

[07:04] Se abro o terminal, como executo o teste? Vou parar o servidor e vou executar o comando python manage.py test. Quando aperto a tecla “Enter” recebo uma mensagem de erro. Isso porque escrevi errado. Deixe-me ver se escrevi mesmo. Deixei a pasta “tests” no plural e ela deve estar no singular. Então temos uma pasta com “test” e dentro dessa pasta temos o teste de curso e assim por diante.

[07:32] Então vou executar mais uma vez e limpar a tela. Desculpe-me, pessoal. Vamos ver. Beleza, rodamos e ele falou que checou tudo e que está tudo OK. Então, uma coisa interessante que podemos ver é que ele não encontrou nenhum erro. Tanto que faz sentido porque não executamos um teste em si, nós criamos um cenário de teste. Vou criar um cenário de teste para falhar, para nós visualizarmos como vai ser um teste que vai dar errado.

[08:01] Então vou criar um método. Nesse método preciso chamar de test_, o nome desse teste vou chamar de falhador e aqui vou passar a instância que estivermos utilizando, self. Para esse teste falhar vou falar test.fail e passar a mensagem do teste. Então vou passar, por exemplo: Teste falhou de propósito, não se preocupe.

[08:35] Salvei. Estou abrindo o terminal mais uma vez. Vou rodar o python manage.py test e o olhe que interessante! Agora recebemos algumas informações que são relevantes.

[08:46] Ele disse que criou um banco de dados de testes com o apelido de default. Então ele não utiliza o nosso banco de dados. Ele deu um F. Deu F, deu ruim, falhou. Ele fala qual é o teste que falhou. Então falhou o test_falhador. Onde está esse teste? Lá em escola.test.tests_cursos.CursosTestCase. Passou toda a identificação do caminho. Ele falou o motivo da falha, “O teste falhou de propósito, não se preocupe”.

[09:16] Criamos o cenário de teste e criamos um teste para falhar. No próximo vídeo vamos criar os testes para as nossas requisições.

### Testando GET e POST

1. Em tests_cursos.py:

        ...
                def test_requisicao_get_para_listar_cursos(self):
                        response = self.client.get(self.list_url)
                        self.assertEqual(response.status_code, status.HTTP_200_OK)

                def test_requisicao_post_para_criar_curso(self):
                        data = {
                                'codigo_curso':'CTT3',
                                'descricao':'Curso teste 3',
                                'nivel':'A'
                        }
                        response = self.client.post(self.list_url, data = data)
                        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

---

[00:00] Preparamos o nosso cenário de teste e o que eu quero fazer agora é verificar se a requisição get para listar todos os cursos vai funcionar, ou se já está funcionando na aplicação. Quero garantir que esse comportamento aqui esteja certo. Para isso, eu vou criar um novo teste. Esse teste que falha vou deixar comentado. Não vamos precisar dele porque já vimos que está certo e funcionando.

[00:23] Então vou criar um teste, uma função para verificar se a requisição get para listar os cursos está funcionando. Seguindo os padrões preciso usar a palavra test_requisicao_get_para_listar_cursos. Vou passar a instância que estamos utilizando, o self. Vou passar uma docstring para deixar nosso teste certo e bem documentado.

[01:00] Então, Teste para verificar se a requisição GET está... não. Teste para verificar a requisição GET para listar os cursos. Algo desse tipo. Então demos um nome que faz sentido para nosso teste e falamos que queremos que queremos fazer o teste com essa docstring. Vou mostrar a importância disso também.

[01:33] A primeira coisa é pedir para um determinado cliente fazer uma requisição para essa URL que verifica os cursos. Eu tenho uma resposta e preciso armazenar essa resposta. Vou colocar, response = self..

[01:53] Lembra do que eu disse? Alguém vai fazer essa requisição. Então vou colocar Client.get, que é o verbo que a pessoa vai utilizar. Para eu passar a URL, vou utilizar self.list_url que criamos aqui em cima no “setup” quando preparamos os testes.

[02:14] Fiz a requisição e vou fazer a verificação. Então, self.assertEqual. Como vou verificar agora para saber se essa resposta está correta ou não? Posso utilizar o status_code. Então vou falar, por exemplo: se response.status_code, se nesse response eu fiz a requisição e recebi uma resposta, qual é a resposta que recebemos?

[02:48] Quando fizemos uma requisição e veio a página certa e veio tudo certo. OK, é o status200. Para garantirmos que vamos trabalhar com o status certo, vou importar também o módulo que cuida desses status, lá do rest_framework.

[03:03] Então, from rest_framework import status. Aqui vou utilizar, tenho o status da resposta da requisição que o cliente fez, do get. Agora vou utilizar status. – lembra que fizemos a requisição, deu tudo certo e voltou? Então foi um 200. Vou dar um 200_OK. Maravilha!

[03:29] Salvei. Teclas “Command + J”. Vamos executar esse teste? Digitei python manage.py test e executei o teste.

[03:34] E observe que ele executou no mesmo esquema, criou a base de dados default, executou o teste e deu um ponto. Deu tudo certo. Se esse teste tivesse falhado, por exemplo, olhe só. No lugar do status_code 200 vou dar, por exemplo, um HTTP_404_NOT_FOUND na linha 23. Olhe o que vai acontecer! Só para visualizarmos essas mensagens de erro.

[03:58] Então ele falou assim, Falhou um teste. Teste para verificar a requisiçãoGETpara listar os cursos. Então olhe só, nós recebemos como resposta, o response.status_code foi 200. Deixe-me colocar aqui em cima. Deu OK, só que 200 não é igual a 404. Então quando recebemos um status_code diferente do que esperamos, recebemos uma mensagem, uma indicação dessa falha.

[04:26] Fez a requisição e deu certo, mas voltou o 200? Executamos o nosso teste, voltei para 200 e está OK. Garantimos que a requisição get para listar os cursos está funcionando. Preciso fazer agora um método para verificar se a nossa requisição post vai funcionar. Vou criar uma função, que vou chamar de def test_requisicao_post_para_criar_curso():.

[04:57] Sempre com o underline entre as palavras. Vou criar uma mensagem também. Vou copiar essa e alterar só o que precisamos. Vou incluir a docstring também. Deixe-me ver se está lá em cima. Deixa, depois mostro para vocês. Observe que essa docstring que nós digitamos aparece na mensagem de teste também.

[05:21] Então, Teste para verificar a requisição POST para criar um curso. Então, vamos lá! O que preciso para criar um curso? Em primeiro lugar, das informações do curso que quero criar. Vou criar os dados desse curso. Então data, abre chaves e vou dizer, por exemplo, o código do curso, vou falar que o codigo_curso:.

[05:51] Criamos o curso CTT1 e CTT2 e vou criar o CCT3, “curso teste, teste 3”, por exemplo. Vou colocar uma vírgula. Temos também uma descricao : Curso teste 3. Para finalizarmos, temos o nivel: 'A'. Vai ser o nível avançado.

[06:22] Criei os dados que quero enviar uma requisição POST. O que preciso fazer agora? Vou ter um response, que é o que quero avaliar o status_code dessa resposta. Então response vai ser o cliente que estamos utilizando, o Self.client.post, que é o que queremos fazer.

[06:43] Preciso passar a URL certa do curso e o localhost, não preciso? Então, o que vou passar? O Self.list e list_url e vírgula. Vou dizer que a data, os dados que quero passar são esses dados que temos e passei as informações. Vamos fazer agora a verificação, self.assertEquals, no plural.

[07:17] Vou deixar o de cima também no plural, Self.assertEquals. O que quero fazer? Quero verificar se essa resposta que tive aqui, o response.status_code, é igual status. de criação. Olhe só, temos um 201. É isso aí! Salvei, apertei as teclas “Command + J” e agora estou limpando o terminal e executando o teste... Esse teste falhou!

[07:48] Ele deu 201, não é igual a 100. Deixei como 100, não é o 100_CONTINUE. É o 201_CREATED. Deixe-me tirar aqui porque ficou dois status. É status_HTTP_200_OK. O teste deu errado por causa do código que escrevi. Executei agora e deu certo. Deixe-me minimizar um pouco para baixo só para verificarmos.

[08:15] Então, o que fizemos para verificar o teste do POST? Criamos uma requisição, os dados e falamos que um determinado cliente vai fazer uma requisição POST para a lista de cursos que temos, para o end point de cursos.

[08:29] Esses são os dados. Quero verificar se a resposta desse método POST que esse cliente fez é igual a 201 - e quando executamos deu certo.

### Testando PUT e DELETE

1. Em tests_cursos.py:

                ...
                def test_requisicao_delete_para_deletar_curso(self):
                        response = self.client.delete('/cursos/1/')
                        self.assertEquals(response.status_code, status.HTTP_405_METHOT_NOT_ALLOWED)

                def test_requisicao_put_para_atualizar_curso(self):
                        data = {
                                'codigo_curso':'CTT1',
                                'descricao':'Curso teste 1 atualizado',
                                'nivel':'I'
                        }
                        response = self.client.put('/cursos/1/', data = data)
                        self.assertEquals(response.status_code, status.HTTP_200_OK)

---

[00:00] Temos dois testes. Um para verificar a requisição GET e outro para verificar uma requisição POST, para listarmos um curso e para criarmos um curso. O que quero fazer agora é testar uma requisição, um DELETE, por exemplo. Só que quero fazer algo diferente.

[00:15] Observe que estou com a minha API rodando. Subi o servidor. Quando entro, por exemplo, em /alunos e coloco um determinado aluno - por exemplo, localhost:8000/alunos/1/ - tenho a opção de deletar esse recurso. O mesmo acontece com os cursos. Se eu acesso localhost:8000/cursos/1/, tenho essa opção de DELETE.

[00:36] Vamos supor que por uma regra de negócio nós não vamos permitir mais requisições DELETE para removermos um curso da nossa base de dados. Então, o que vou fazer? No Sublime eu vou colocar http_method_names. Http_method_names = [‘get’, ‘post’, ‘put’, ‘path’].

[01:08] Isso significa que vou conseguir listar um curso, criar um curso e atualizar um curso. Mas não vou ser capaz de deletar um curso. Salvei e o servidor subiu. Na página da aplicação, quando atualizar o DELETE, não aparece mais. Até aí tudo bem.

[01:23] O que eu quero fazer agora é criar um teste que garanta que esse comportamento vai se manter, ou seja, que quando eu for testar, eu fale assim: “vou tentar deletar um produto”. Vou precisar receber um status que indique que não tenho permissão de deletar esse produto.

[01:43] Vamos começar escrevendo o teste. A primeira coisa vai ser def test_. Vou colocar, por exemplo, o nome desse teste como requisicao_delete_para_deletar_curso. Alguma coisa assim nesse sentido. Vou passar a instância self e vou começar a escrever o teste. Para deixar nosso teste semântico e bem documentado, eu vou colocar a docstring indicando Teste para verificar a requisição DELETE não permitida para deletar um curso.

[02:35] Vou colocar na minha “View > Toggle Word Wrap”, só para nós conseguirmos visualizar em uma tela só. Criei a docstring. Ele está documentado. Então, Teste para verificar a requisição DELETE não permitida para deletar um curso.

[02:52] O que preciso fazer? Preciso ter um cliente tentando deletar um determinado curso, então vou colocar self.client.delete. Então um cliente vai tentar fazer uma requisição DELETE para um determinado curso. Nessa função de setup nós queremos o curso 1 e o 2. Observe que quando fui tentar deletar o curso 1 eu passei localhost:8000/cursos/1/.

[03:20] Vou precisar passar esse mesmo caminho. Vamos supor que já tenho o curso 1 feito, então vou querer deletar o localhost:8000/cursos/1/. Fechei. Quero tentar deletar esse curso. Preciso armazenar essa requisição em algum lugar, então quero armazenar a resposta. Vou colocar response = self.client.delete(/cursos/1/).

[03:46] Para finalizarmos, vamos fazer uma assertação, self.assertEquals. O que quero fazer? Quero verificar o status dessa resposta. Então vou passar response.status_code. O que vou fazer agora? Preciso garantir qual é o status_code que quando quero tentar deletar um determinado recurso e não tenho permissão? Podemos colocar o status 405.

[04:23] Então vou colocar status. e vai aparecer uma lista de status. Vou descer, descer e descer. Poderia pensar em colocar o “não autorizado” mas vou colocar o 405. Então HTTP_405_METHOD_NOT_ALLOWED.

[04:42] Salvei. Abrindo o terminal, vou parar o servidor e rodar o manage.py test. Quando aperto a tecla “Enter”, olhe o que acontece.

[04:53] Ele executou e passou. O nosso teste deu certo. Para garantirmos que nosso teste realmente deu certo, o que vamos fazer? Lá em “views” nós falamos: olhe, os métodos permitidos para cursos são esses. Vou alterar, vou colocar o delete no final da linha 22. Ou seja, quando eu deletar vou receber um outro status_code e vamos ver se isso vai refletir no nosso teste.

[05:13] Quando executamos, nós recebemos um status_code 204 e falamos que 204 não é igual a 205 e temos “Teste para verificar a requisição DELETE não permitida para deletar um curso”.

[05:27] O que acontece? Através desse teste nós conseguimos garantir um comportamento para a API. Vou remover esse delete. Foi só para garantirmos mesmo que nosso teste está sendo executado de forma tranquila.

[05:37] Para finalizar, eu quero criar um teste que vai garantir uma atualização de um curso. Se observarmos no nosso método setUp temos o curso_1 e o cursp_2. Eu quero atualizar o curso_1 em duas partes. Quero mudar a descrição. Quero colocar Curso teste 1 atualizado e mudar o nível dele de básico para intermediário.

[05:59] Vamos fazer isso? A primeira coisa que vamos fazer vai ser criarmos o nome desse teste. Então, test_requisicao_put_para_atualizar_curso(self): e nós vamos começar com a docstring mantendo nosso código documentado. Então, Teste para verificar requisição PUT para atualizar um curso.

[06:42] Colocamos lá! A primeira coisa que vou fazer vai ser pensar no dado que quero atualizar, no dado de teste. Então vou criar um chamado data = {}. Então um curso tem um código, codigo_curso:. Qual é o código do curso?

[07:05] É o CTT1 - que é esse curso que quero atualizar. Então coloquei o curso CTT1. Quero também modificar a descrição, descricao:. Na verdade, esse não modifiquei, eu mantive o mesmo. Quero modificar agora a descrição. Então a descrição que temos aqui em cima é essa, Curso teste 1. Vou pegar esse Curso teste 1 e vou colocar ele aqui. Curso teste 1 atualizado.

[07:36] Coloco a vírgula e para finalizar, nós temos o nível, nivel:. Nesse nível quero passar o intermediário (I). Criei os dados que quero atualizar desse curso! Para finalizar preciso ter um cliente fazendo a requisição PUT para atualizar esse curso. Então, self.client.put. Em primeiro lugar, lembra que quando acessamos localhost:8000/cursos/1/ aparece informações do curso e aqui embaixo o PUT para eu, de fato, atualizar esse curso?

[08:08] Então, da mesma forma que queremos deletar, ele pergunta o que eu quero deletar. Eu quero deletar o curso com esse ID. Então quero atualizar o curso com esse ID. Vou fazer o mesmo, vou passar entre aspas o /cursos/1 que é o primeiro curso que quero atualizar que é o curso CTT1. Vou colocar uma vírgula.

[08:28] Observe o segundo parâmetro, o que temos? Os dados. Se quero atualizar, quais são os dados que quero passar? Passamos isso através do parâmetro data. Então vou passar que data é igual a data dos dados atualizados.

[08:43] Para finalizarmos, vamos fazer a assertação Self.assertEquals e vou passar. Em primeiro lugar preciso verificar se a resposta dessa requisição, que não armazenei e preciso dela, response = self.client.put(/curso/1/,data=data).

[09:01] Agora sim! Vou digitar self.assertEquals(response.status_code, status.HTTP_200_OK). Deu tudo certo. Você conseguiu atualizar, aí está um sucesso! Aí conseguimos continuar. Podemos garantir que esse teste foi aprovado.

[09:22] Salvei esse arquivo. Estou carregando o terminal e vou executar mais uma vez, digitando python manage.py test. Ele executou e passou. Deu tudo certo.

[09:32] Vimos nesses testes que escrevemos algo bem simples. Posteriormente vão existir outros cursos, outros treinamentos de Django REST focados em teste. Depois vamos entrar em uma discussão sobre testes de integração, testes de unidade. Mas só para conseguirmos ter uma base e os fundamentos de como conseguimos verificar as principais requisições da API e os principais comportamentos.

[10:01] Por exemplo: tenho um determinado recurso que não posso deletar em hipótese alguma na minha API. Como testo para garantir esse funcionamento? Fizemos o método de DELETE. Eu quero atualizar, quero testar atualizando em um determinado recurso da minha API.

[10:18] Vimos como testar as principais requisições da API: GET, POST, DELETE e PUT.

### Função setUp

Após desenvolver uma API e testar manualmente as principais requisiçòes, uma pessoa decidiu escrever testes automatizados e começou com o seguinte código:

                from rest_framework.test import APITestCase
                from escola.models import Animal
                from django.urls import reverse

                class AnimaisTestCase(APITestCase):

                    def setUp(self):
                        self.list_url = reverse('Animais-list')
                        self.animal_1 = Animal.objects.create(
                            nome='Urso'
                        )

Com base no código acima e analisando as afirmações abaixo, podemos afirmar que:

a) O método setUp() é executado quando os métodos de testes são concluídos.

b) **Alternativa correta:** Existe um cenário de teste com um animal cadastrado, porém sem nenhum teste.
- _Alternativa correta! Certo! Através da função setUp() o cenário de teste foi montado com as rotas de animais e o animal_1 foi criado apenas para os testes, sem vincular os dados reais da aplicação e nenhum teste ou afirmação foi desenvolvida._

c) **Alternativa correta:** Qualquer método em uma subclasse TestCase que comece com o prefixo test_ será executado sempre que executarmos o python manage.py test
- _Alternativa correta! Certo! Assumindo que não adicionamos um argumento para excluí-lo, o método será executado._

### O que aprendemos?

**Nesta aula:**
- Aprendemos como criar um cenário de teste, sem utilizar os dados da aplicação;
- Escrevemos os testes das principais requisições do recurso de cursos.

**Na próxima aula - cereja do curso!**
Vamos aprender como aumentar a segurança das aplicações Django e incluir um pote de mel!

## 05. Segurança
### Projeto da aula anterior
### Pensando em segurança
### Pote de mel
### Acesso não autorizado
### Faça como eu fiz
### O que aprendemos?
### Parabéns
### Conclusão
