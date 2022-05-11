# 1. Introdução ao Django: Modelo, Rotas e Views
**Fonte:** Guilherme LIma<br>
**Disponível:** <a href="https://cursos.alura.com.br/course/fundamentos-django-2" target="_blank">ALURA</a><br>
**Conteúdo:**
- Aprenda a desenvolver aplicações web utilizando a linguagem Python
- Desenvolva uma aplicação do zero, seguindo as principais convenções e boas práticas
- Saiba como configurar e conectar sua aplicação com um banco de dados sql
- Melhore seu código, reaproveitando em outras partes da aplicação
- Entenda a arquitetura de uma aplicação feita com Django
---
## 01. Iniciando aplicação e subindo o servidor Ver primeiro vídeo
### Introdução
### Saudações e Ambiente
Olá!

É muito bom receber você neste curso. Espero que seja uma experiência de aprendizado incrível e que possamos vencer todos os desafios e aprender os fundamentos do Django, utilizando a linguagem Python.

#### Preparando ambiente

Para conseguir acompanhar este curso, é recomendado que você tenha o <a href="https://www.python.org/downloads/">Python3</a> instalado.

Caso necessite ajuda para instalação do Python, recomendamos os seguintes links:

- Passo a passo para instalar o Python3 no Windows. <a href="https://cursos.alura.com.br/course/python-3-introducao-a-nova-versao-da-linguagem/task/22687" target="_blank">aqui</a>
- Passo a passo para instalar em outros sistemas operacionais.<a href="https://cursos.alura.com.br/course/python-3-introducao-a-nova-versao-da-linguagem/task/22688" target="_blank"> aqui</a>

Além disso, para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

- <a href="https://www.python.org/downloads/release/python-374/" target="_blank">Python 3.7.4</a>
- <a href="">Django 2.2.6</a>

O Django pode ser instalado através do comando:

    pip install Django==2.2.6

Em caso de dúvida na instalação ou durante o curso, conte sempre com o fórum da Alura!

Vamos começar? :)

### Django e venv

Vamos dar início ao desenvolvimento de nossa aplicação em Python utilizando o framework do Django.

Começamos entrando neste link para baixar e instalar a última versão de Python disponível para cada sistema operacional.

Com o programa instalado, abrimos o terminal com o atalho "Tecla Windows + R" para digitar "cmd" e encontrar com "Enter" no caso de Windows, e "Command + Espaço" para digitar "terminal" em Mac OS.

Verificamos a versão instalada digitando python -- version. O resultado é diferente do que foi apresentado no site de Python mas não há nenhuma necessidade de remover, pois é a versão utilizada por nosso sistema operacional. Para visualizarmos a versão que instalamos, escrevemos python3 -- version.

Caso seja necessário, na atividade anterior "Saudações e ambiente" há um passo-a-passo para instalar o Python3 nos três principais sistemas operacionais.

Agora, partimos para a instalação de Django através deste link, onde temos uma maneira de instalar a última versão. Se apenas digitarmos a linha apresentada no terminal, o sistema instala no ambiente de sistema operacional, e não é o que queremos; precisamos desenvolver uma aplicação e queremos que o Django esteja instalado somente nesta.

Para isso, utilizamos ambientes virtuais; digitando "python venv" no navegador e acessamos este endereço que possui uma descrição sobre o fornecimento de ambientes virtuais leves através deste módulo de Python, contendo seus próprios diretórios, arquivos binários, versões e módulos independentes do sistema operacional.

Para criar, há a parte "Creating virtual environments" com a linha python3 -m venv /path/to/new/virtual/environment. De volta ao terminal, para manter nosso código organizado em um local, criamos uma pasta no desktop digitando cd desktop e depois mkdir para a pasta aplicacao que mantém todo o código da aplicação. Acessamos com cd aplicacao e observamos seu conteúdo vazio com ls.

Em seguida, limpamos o terminal com "Ctrl + L", criamos o ambiente virtual de Python dentro da aplicação escrevendo python3 -m venv ./venv e finalizamos com a tecla "Enter".

Se digitarmos ls, podemos visualizar a pasta venv que possui o arquivo "bin", "include" e "lib". Este primeiro contém o arquivo necessário para carregarmos este ambiente. Há diferenças entre os sistemas operacionais; na documentação, vemos orientações específicas para carregar em cada um.

No decorrer da aplicação, editamos e alteramos o código usando o Visual Studio Code, mas outros editores como PyCharm, Sublime Text ou Atom também são eficientes. Abrindo-o, acessamos a pasta "aplicacao > venv" e abrimos o terminal com "Command + J".

Na janela "Terminal", carregamos o ambiente virtual digitando pwd para copiar e colar o caminho após escrever source na linha seguinte. Em seguida, escrevemos /venv/bin/activate na sequência do caminho para acessar a pasta e inicializar com "Enter". Temos confirmação quando aparece (venv) antes do diretório.

Agora, podemos aplicar o comando de pip install presente na página do Django. Se estivermos utilizando Windows, a diferença está no acesso ao arquivo, e neste caso é necessário escrever /venv/Scripts/activate.bat.

Copiamos e colamos o comando em nosso terminal, sem precisar especificar a versão, pois a última já está presente no site de origem, e portanto apenas adicionamos pip install django.

Após a instalação de todos os pacotes necessários, existe uma forma de ver se foi instalado corretamente que consiste em digitar pip freeze para visualizar todos os módulos presentes neste ambiente virtual.

Feito isso, podemos partir para a criação da aplicação.

### Projeto e subindo servidor

Com nosso ambiente virtual configurado e ativado, podemos dar início ao nosso projeto.

Para descobrir o comando de Django que executa e inicializa o projeto, escrevemos django-admin help na janela de terminal dentro do Visual Studio para visualizar uma série de comandos que podemos usar; dentre estes, existe o startproject.

Limpamos o terminal com "Ctrl + L" e adicionamos este comando seguido do nome do projeto alurareceita. Se simplesmente apertarmos a tecla "Enter" neste momento, o sistema cria uma pasta com nosso trabalho contendo outro diretório com o mesmo nome, e não é o que queremos. Precisamos gerar uma pasta principal do projeto, e para isso apenas adicionamos . após o título e apertamos "Enter", e assim podemos ver "alurareceita" na lista lateral de diretórios contendo quatro outros documentos e um arquivo separado chamado manage.py que possui um código inicial.

Nos documentos criados dentro de "alurareceita", temos o __init__.py que diz ao Python que este diretório deve ser considerado um pacote.

Já settings.py é um arquivo extremamente importante e útil para nosso trabalho, pois contém todas as configurações relacionadas a nossa aplicação, e inclusive podemos mudar o idioma da aplicação, substituindo en-us por pt-br em LANGUAGE_CODE =. Já o TIME_ZONE = será usado para São Paulo, e para descobrir o que escrever, digitamos "django timezone list" na busca do navegador para acessar este link que possui uma lista para cada localidade. Descoberta a referência, substituímos UTC por America/Sao_Paulo e salvamos o arquivo. Com isso, a hora marcada na aplicação corresponde a este fuso horário.

O Visual Studio apresenta uma caixa de diálogo indicando a recomendação da extensão de Python, e clicamos em "Install". Também sugere a instalação de Linter pylint, e também clicamos em "Install".

O arquivo urls.py é a declaração de todas as urls para nosso projeto, como um índice do site movido dentro de Django onde serão cadastradas.

Por fim, o wsgi.py é um ponto de integração para servidores Web compatíveis ao WSGI. Não veremos sobre esta questão neste treinamento, pois abordaremos somente as partes mais elementares.

Agora, é interessante visualizarmos algo após as alterações feitas subindo um servidor para ver uma página, da mesma forma como fazemos com o Google. Abrimos uma nova aba no navegador e digitamos um endereço qualquer para abrir um site, e é isso que queremos para nosso projeto também, mesmo que seja apenas um local da máquina.

Para isso, não utilizamos mais o admin do Django, e sim o arquivo manage.py. No terminal, digitamos python manage.py seguido de um comando runserver para subir o servidor, descoberto da mesma forma com help na sequência.

> python manage.py runserver

O sistema apresenta uma mensagem alertando que há algumas migrações a serem feitas. Não é necessário nos preocuparmos com isso neste momento. Em seguida, aponta a porta na qual o servidor subiu.

Pressionando "Command", clicamos nesta porta para abrir no navegador, o qual exibe uma mensagem de sucesso da instalação em português, como configuramos. Para testar, basta escrevermos "localhost:8000" na barra de endereços do navegador padrão.

Como não queremos a animação apresentada pelo Django na nova página e sim nosso projeto com as receitas, configuraremos seguir.

### Servidor e app de receita

Antes de darmos continuidade à aplicação, é importante levar em conta que estamos configurando e executando o código Python no mesmo em que estamos usando no ambiente virtual, ou seja, se acionarmos "Command + Shift + P" e digitar ">python select interpreter", o interpretator Python que queremos utilizar é o que está em venv. Selecionamos esta opção para garantir essa interpretação do código.

Dando sequência, queremos visualizar nossa própria página no navegador. Para isso, criamos um app como conceito de aplicação que faz algo em Django, e não um aplicativo de celular. Por exemplo, em nosso sistema web, queremos ver receitas, e sua forma de criação é um app.

Quando iniciamos o projeto, usamos o comando startproject, que é diferente de app. Um projeto é uma coleção de configurações, e muitos apps podem fazer parte de seu escopo, ou seja, um trabalho pode conter diversos apps, e um mesmo app pode estar presente em vários projetos.

Portanto, devemos pensar na presença de destes recursos para gerar um site, e o app é uma aplicação que faz uma determinada ação e função.

Agora que já subimos um servidor para conseguirmos visualizar no browser, abrimos outro terminal clicando no ícone de "+" ou "New Terminal", que carrega automaticamente o venv. Um terminal é usado para executar o código ao longo do desenvolvimento da aplicação chamado "2: bash" e outro para executar o próprio servidor chamado "1: Python".

O servidor possui um carregamento automático, logo não é necessário que reinicializar a cada alteração de código, e faremos isso somente em alguns casos mas não durante o desenvolvimento do projeto.

Para criar um app, aplicamos o comando help após pedir ao manage.py da mesma maneira já feita. Com isso, descobrimos que devemos utilizar startapp seguido do nome que queremos criar no terminal que executa o código.

> python manage.py startapp receitas

Com "Enter", o sistema gera a pasta "receitas" presente na lista lateral, e os apps podem ficar em qualquer lugar dentro do ambiente. Em nosso caso, deixamos ao lado do arquivo manage.py para ficar mais fácil de identificar, enquanto "alurareceita" é referente às configurações da aplicação.

Então, é a partir de "receitas" que criamos nosso site. O primeiro passo mais importante é registrar o app, pois podemos ter vários dentro de um projeto como já dito; em app.py, visualizamos a classe ReceitasConfig() com um name que deve ser igual a receitas que é utilizado para seu registro, dizendo às configurações de que esse app criado faz parte do projeto.

Em settings.py, adicionamos 'receitas' à lista de apps. Ao salvar, este está registrado no trabalho. Agora, precisamos acessá-lo entrando na pasta "receita" que ainda não tem nada relacionado a url.

Sempre que digitamos localhost:8000 é aberta a página padrão do Django, e queremos uma url própria para a aplicação. Para isso, criamos um novo arquivo clicando no ícone de "New file" para nomear como urls.py. Neste novo arquivo, importamos as urls para poder usá-las escrevendo:

> from django.urls import path

Em seguida, importamos todas as urls com . e views relacionadas.

> from django.urls import path<br>
> from . import views

A arquivo de views.py é quem faz a manipulação de qual urls queremos devolver e exibir na tela. Depois, criamos urlpatterns inserindo o primeiro path() lembrando que a página localhost:8000 seja de receitas. Para isso, o primeiro parâmetro é '', o segundo deve ser views.index como o responsável para atender a requisição e o terceiro é name='index' sendo o namespace do aplicativo para estas entradas urls.

> from django.urls import path<br>
> from . import views
>
>urlpatterns = [
    path('', views.index, name='index')
]

Salvamos o arquivo e vemos um erro em views que indica que não há nenhum elemento chamado receitas.

Portanto, precisamos criar indo ao arquivo views.py para gerar o arquivo de receitas. Começamos com def para aplicar index() que recebe uma requisição como parâmetro. Ainda não possuímos HttpResponse e precisamos importá-lo de django.http.

Dentro de index(), inserimos request. Em seguida, devolvemos com return o HttpResponse() recebendo a tag de html com h1 para nomear como "Receitas".

> from django.shortcuts import render><br>
> from django.http import HttpResponse<br>
> def index(request):<br>
    return HttpResponse('<h1>Receitas</h1>')

Salvamos este arquivo e voltamos ao urls.py para salvar também. Para visualizar, vamos ao browser para atualizar a página e ver que nada aconteceu de diferente.

Da mesma forma que registramos o app para "alurareceita", precisamos registrar para as nossas rotas. Para isso, acessamos a pasta em questão para abrir o arquivo urls.py que apresenta path() com include na documentação. Deletamos as linhas de comentários e adicionamos mais um path() em urlpatterns para o caminho do localhost vazio com '', seguido da inclusão com include que precisa ser importado também. Depois, indicamos qual o argumento a ser incluído, sendo 'receitas.urls'.

> from django.contrib import admin<br>
> from django.urls import path, include
>
>urlpatterns = [
    path('', include('receitas.urls')),
    path('admin/', admin.site.urls),
]

Salvamos o arquivo e testamos as alterações no navegador ao atualizar a página.

Assim, temos escrito "Receitas". Podemos continuar adicionando a tag para segunda linha com a mensagem "Bem vindo"

>from django.shortcuts import render<br>
>from django.http import HttpResponse<br>
>def index(request):<br>
    return HttpResponse('<h1>Receitas</h1> <h2>Bem vindo<h2/>')

Porém, se desenvolvermos todo o site somente com as tags html em HttpResponse, o texto fica de difícil manutenção. Portanto, o melhor caminho é ter um arquivo próprio para receber todo o código e retornar o html.

### Exercício: Benefícios da venv

Para desenvolver uma aplicação web em Python utilizando o framework Django, criamos um ambiente virtual utilizando a venv.

Sabendo disso, analise as afirmações abaixo e marque apenas as que são verdadeiras em relação a utilização da venv:

a) Assim que um ambiente virtual é inicializado, é impossível desativá lo.
b) O módulo venv fornece um suporte para criação de ambientes virtuais, de forma complexa, dependendo dos diretórios do sistema.
c) Utilizando o módulo venv, podemos separar as dependências de cada projeto.
- _Certo! Desta forma, cada projeto possui suas próprias dependências, não precisando utilizar os módulos no escopo global._

### Projeto e app

Durante o desenvolvimento da nossa aplicação, utilizamos dois comandos:

>django-admin startproject, seguido do nome do nosso projeto;

>python manage.py startapp, seguido do nome app.

Sabendo disso, marque as opções verdadeiras com base nesses comandos:

a) Um projeto só pode ter um único app.

b) Um app pode estar em múltiplos projetos.
- _Certo! Um app pode ser compartilhado entre diferentes projetos._

c) Um app é uma aplicação que realiza uma determinada ação ou que faz alguma coisa.
- _Certo! No nosso exemplo do curso, criamos o app de receitas, para mostrar as receitas do nosso site._

d) Um projeto é uma coleção de configurações e apps para um site.
- _Certo! Todas as configurações da nossa aplicação web ficam em um projeto._

### Para saber mais: Django

Princípios do Django
animação com texto, produtividade, código limpo e documentação

<img src="https://caelum-online-public.s3.amazonaws.com/1489-django+parte+1/aula+1/gif+aula+1+-+principios+django.gif">

A questão dos frameworks web do século 21 é fazer com que aspectos enfadonhos do desenvolvimento web sejam rápidos. Django deve permitir que o desenvolvimento de aplicações web seja incrivelmente rápido.

Aplicações Django devem usar o mínimo possível de código; elas não devem ter código padrão. Django deve aproveitar as características dinâmicas do Python, como <a href="https://pt.wikipedia.org/wiki/Introspec%C3%A7%C3%A3o_%28computa%C3%A7%C3%A3o%29" target="_blank">introspecção</a>.

Caso queira saber mais sobre filosofia do Django:

- <a href="https://docs.djangoproject.com/pt-br/2.2/misc/design-philosophies/" target="_blank">Filosofia do Django segundo a documentação oficial</a>

## 02. Template, rotas e views
### Criando a pasta template

Como não queremos desenvolver toda a página HTML no espaço de HttpResponse(), é melhor termos um arquivo próprio para isso, mantendo o código mais bem organizado. Já conseguimos visualizar o que escrevemos, mas iremos renderizar o arquivo HTML de fato.

Para começar, criamos um novo folder chamado "templates" dentro de "receitas" clicando no ícone de "new folder". Dentro desta pasta, geramos um novo arquivo através de "new file" chamado index.html.

Se digitarmos html:5 e apertarmos a tecla "Enter", o sistema já cria o código inicial. Entre o title> para o valor do cabeçalho, escrevemos Alura Receitas.

Em body, adicionamos as tags h1 para digitar Alura Receitas. Se voltarmos ao navegador e atualizarmos, não aparecem alterações; isso acontece porque não informamos ao views.py que é necessário renderizar a página. Para isso, substituímos HttpResponse() por render(), sendo que já temos esta extensão importada. O segundo import feito para a função anterior não é mais utilizado, logo sua linha pode ser removida.

Em seguida, como queremos renderizar o arquivo recém-criado, substituímos o conteúdo de render() por 'index.html'. Porém, a função em questão exige uma requisição quando adicionamos uma vírgula antes do arquivo.

> from django.shortcuts import render
> 
>def index(request):
>    return render(request, 'index.html')

Salvamos e atualizamos a página do navegador novamente para ver o resultado. Somente com a criação da pasta "template" e feita a requisição para expor o arquivo, conseguimos ver o que escrevemos.

De volta ao body> do index.html, adicionamos a tag h2> com uma mensagem de boas vindas ao site. Desta forma, temos um arquivo onde podemos criar nossas próprias receitas e editá-las.

Além disso, queremos visualizar uma página de receita. Em body, criamos table recebendo thead com uma linha tr para termos alguns campos usando um atalho td*3 que cria três linhas de td com o nome da receita, os ingredientes e o modo de preparo.

Após /thead, criamos o corpo da tabela com tbody> incluindo uma linha tr> com três linhas td> novamente para preenchermos os campos da receita de suco verde.

<body>
    <h1>Alura receitas</h1>
    <h2>Boas vindas ao site</h2>
    <table>
        <thead>
            <tr>
                <td>Nome da receita</td>
                <td>Ingredientes</td>
                <td>Modo de preparo</td>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Suco verde</td>
                <td>Folhas verdes, 1 maça, 1 cenoura</td>
                <td>Bata tudo no liquidificador</td>
            </tr>
        </tbody>
    </table>
</body>

Salvamos para atualizarmos a página no navegador e avaliarmos o resultado. Ainda que visualmente desagradável, nossas informações são impressas.

A seguir, veremos como fazer para obter um visual mais interessante através de um front-end pronto que será incorporado ao nosso site com arquivos estáticos.

### Preparando o ambiente

**Melhorando o visual da nossa aplicação**

<a href="https://caelum-online-public.s3.amazonaws.com/1489-django+parte+1/site_receitas.zip" target="_blank">Neste link</a>, você fará download de um projeto com html, css e javascript bem lindão, que integraremos com nossa aplicação Django.

Sendo assim, faça o download deste arquivo e deixe sua aplicação de receitas com um visual bem legal!

### Arquivos estáticos

Nesta etapa, melhoraremos bastante o visual do nosso site.

Criamos um arquivo index.html para manter a página, porém está sem CSS, imagens e JavaScript. Na atividade anterior, temos um arquivo com um protótipo de um portal a ser desenvolvido. Neste podemos visualizar ícones, logotipo e outras receitas com uma melhor navegação. Quando clicamos em algum item, uma outra página se abre com suas informações.

Para descobrir como incorporar este modelo ao site com aplicação Django, acessamos a documentação de gerenciamento de arquivos estáticos neste endereço, onde encontramos orientações sobre servir arquivos adicionais como imagens, JavaScript ou CSS através de django.contrib.staticfiles.

De volta ao setting.py com as configurações do projeto, vamos à parte de TEMPLATES para o site referenciar e saber onde estão as páginas HTML. Em nosso caso, temos apenas o app de receitas com o template index.html. Logo, precisamos especificá-lo.

Na linha de 'DIRS': [], escrevemos os.path.join() recebendo a base do diretório BASE_DIR e o caminho 'receitas/templates'.

>TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'receitas/templates')],
//código omitido
    },
]

Essa especificação é necessária a medida que nosso projeto cresce e novas páginas aparecem, viabilizando seu mapeamento.

Além disso, precisamos especificar ao Django onde estão os arquivos estáticos, pois precisam ser referenciados em algum lugar da mesma forma que fizemos com as páginas estáticas.

Ao final do texto de setting.py, adicionamos STATIC_ROOT que é o local onde deixamos os arquivos estáticos, sendo os.path.join(BASE_DIR, 'static'). Como já temos o STATIC_URL, falta-nos dizer quais os diretórios que os contém com STATICFILES_DIRS.

Dentro da pasta "alurareceita", criamos uma nova chamada "static". Assim, passamos para STATICFILES_DIRS o caminho 'alurareceita/static'.

>STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'alurareceita/static')
]

Salvamos o arquivo e atualizamos a página no navegador pra ver que ainda está funcionando como antes.

Feito o download do protótipo, temos a nova pasta "site_receitas" salva em nossa máquina. Abrindo a pasta "static" dentro de "alurareceita", precisamos copiar alguns documentos para esta última. Com o atalho "Ctrl + C", copiamos os diretórios "css", "fonts", "img", "js", "scss" e o arquivo "site.css" para colar com "Ctrl + V" em "static".

Com isso, estes novos arquivos aparecem na lista lateral do Visual Studio. Agora, precisamos informar ao Django que temos arquivos estáticos e precisamos de ajuda para referenciá-los; abrimos um segundo terminal já com venv carregada, o que é bastante importante de se verificar para todos os processos, e escrevemos python manage.py help para descobrir alguns comandos de [staticfiles], como collectstatic.

Em seguida, limpamos o terminal, digitamos python manage.py collectstatic e apertamos a tecla "Enter" para que o sistema faça uma cópia dos arquivos e consiga manipulá-los melhor.

Agora, queremos o html visualmente agradável do modelo baixado. De volta à pasta "site_receitas" salva no computador, copiamos os arquivos "index.html" e "receita.html" presentes nesta e colamos na pasta "templates" dentro de "receitas", substituindo o arquivo anterior que fizemos.

Feito isso, voltamos ao navegador e atualizamos a página para ver que um erro TemplateSyntaxError é apresentado.

Verificando se os arquivos aparecem na lista lateral do Visual Studio, recarregamos clicando no ícone "refresh" e atualizamos a página novamente.

Ainda não obtemos um site visualmente agradável, e veremos como deixá-lo bonito como o modelo a seguir.

### Carregando estáticos

Queremos que nosso site fique com o visual do protótipo, muito diferente do que está atualmente somente com links.

De volta ao index.html no Visual Studio, o primeiro passo é especificar informando ao Django que existem arquivos estáticos através da execução do código Phyton com {% load static %}. Se atualizarmos no navegador, não há nenhuma alteração.

Para obter o ícone da aba, precisamos especificar que o caminho presente em Favicon não vem de qualquer lugar, e sim dos arquivos estáticos que acabamos de carregar. Portanto, adicionamos {% static antes do caminho entre aspas simples fechando com %} nas aspas de href.

> <!-- Favicon -->
> <link rel="icon" href="{% static 'img/core-img/favicon.ico' %}">

Salvamos e retornamos ao navegador para atualizar a página novamente, prestando atenção ao ícone da aba.

Então, concluímos que para carregar os arquivos estáticos, é necessário que informemos o caminho correto com o código Python. Fazemos a mesma coisa com Stylesheet.

><!-- Favicon -->
><link rel="icon" href="{% static 'img/core-img/favicon.ico' %}">
>
><!-- Stylesheet -->
><link rel="stylesheet" href="{% static 'site.css' %}">

Ao recarregar a página no navegador, vemos que não funciona como esperamos, pois inicialmente o que é carregado não são os arquivos .css e sim os arquivos JavaScript JQuery ao final do texto de index.html, onde encontramos todos os script> que devem receber o mesmo sufixo {% static fechando com %} sem esquecer das aspas simples nos locais como já vimos.

Feito isso em todas as linhas de src, voltamos à página do projeto para atualizar e ver as alterações no visual. Temos toda a distribuição do layout, mas ainda não temos as imagens necessárias.

Para obter as figuras de cada receita, aplicamos a mesma metodologia de código Python para todos os arquivos de imagens nas linhas com <img> presentes em index.html na sequência de Best Receipe Area Start. Para o logotipo, fazemos a mesma coisa na linha de <img> da parte de Logo.

Salvamos e atualizamos a página para visualizar as alterações.

Dessa forma, temos as imagens de cada receita com logotipo, fontes e containers iguais ao protótipo. Porém, ao clicar em algum dos itens, o navegador não encontra a página.

A seguir, veremos como resolver esta questão.

### Exercício: Configurando estáticos

Em todo desenvolvimento Django, geralmente vamos criar apps, incluir urls e cadastrar rotas, trabalhar com templates utilizando css, javascript e imagens.

Porém, quais configurações devem ser realizadas no arquivo settings.py para possibilitar o uso de arquivos estáticos?

a) Alternativa correta: Nas configurações, incluímos o STATIC_ROOT.
- Certo! Usamos esta configuração para indicar o caminho absoluto, onde o collectstatic coletará os arquivos estáticos.

b) Nas configurações, incluímos o STATICFILES_TRUE, indicando que em nossa aplicação, teremos arquivos estáticos.<br>
c) Alternativa correta: Nas configurações, incluímos o STATICFILES_DIRS.
- Certo! Essa configuração define os locais adicionais que o aplicativo staticfiles percorrerá se o localizador FileSystemFinder estiver ativado, por exemplo. Se você usar o comando de gerenciamento collectstatic ou findstatic ou usar a exibição de exibição de arquivo estático.

d) Alternativa correta: Nas configurações, incluímos o STATIC_URL.
- Certo! Usamos esta configuração para referência a arquivos estáticos localizados no STATIC_ROOT.

### Exercício: {% load static %}

Após realizar todas as configuraçoes em settings.py, indicando que trabalharemos com arquivos estáticos, o que é necessário fazer para carregar uma imagem ou um arquivo css na nossa aplicação?

a) Usar apenas a template tag load static no início da página html.

b) Usar apenas a template tag static mais a URL para o caminho relativo.

c) Alternativa correta: Usar a template tag load static e a tag static para construir a URL para o caminho relativo.
- Certo! Dessa forma, podemos exibir tanto uma imagem, como carregar arquivos css ou js.

### Para saber mais: Templates

Templates

<img src="https://caelum-online-public.s3.amazonaws.com/1489-django+parte+1/aula+2/gif+aula+2+-+templates.gif">

Os templates do Django definem o layout e a formatação final enviados aos usuários finais após o término do processamento de uma solicitação, podendo ser escrito no formato html ou csv, entre outros formatos.

Caso queira saber mais sobre Templates:
- <a href="https://docs.djangoproject.com/en/2.2/topics/templates/" target="_blank">Templates segundo a documentação oficial do Django (texto em inglês)</a>

## 03. Links, extends e partials
### Links, urls e views

Deixamos o visual de nossa página ainda melhor, mas os links ainda não estão funcionando; quando clicamos em algum, recebemos uma mensagem de erro do servidor.

Quando criamos a aplicação de receitas, geramos uma rota para a página principal dizendo que temos uma função chamada index() dentro de views.py, a qual renderiza nosso site.

Porém, index.html não está funcionando, o que gera a mensagem de erro. Neste arquivo, temos a parte Logo que diz respeito ao logotipo principal da página, e para ativar seu link é preciso utilizar código Python novamente; em href=, retiramos o sufixo .html para então embedar com {% url 'index' %}, e assim direcionar para a página url index ao clicar no logo.

><!-- Logo -->
><a class="nav-brand" href="{% url 'index' %}">
><img src ="{%static 'img/core-img/logo.png' %}" alt=""></a>

É importante mudar o arquivo de loading em <!-- Preloader --> inserindo o código Python para arquivos estáticos como já conhecemos.

Desta forma, quando clicamos em "Alura Receita" com o logotipo, vemos uma pequena imagem de uma pizza ao centro para marcar o carregamento.

Agora precisamos lidar com os demais links e com o logotipo que deve estar presente no footer; alteramos da mesma maneira feita anteriormente para carregar a url com código Python em index.html nas partes de Nav Start e Footer Logo, bem como para arquivos estáticos na imagem deste último.

><!-- Footer Logo -->
><div class="footer-logo">
>    <a href="{%url 'index' %}">
>    <img scr="{% static 'img/core-img/logo.png' %}" alt=""></a>
></div>

Salvamos e retornamos à página para verificar as alterações. Porém, ao clicarmos em "Receitas", ainda é exibida a mensagem de erro no navegador.

Em nossa aplicação, não temos uma rota para receitas. Ao final de urls.py, adicionamos mais uma linha de path() recebendo o caminho 'receita', o método da view responsável por atender a receita e um nome para esta função.

>urlpatterns = [
    path('', views.index, name='index'),
    path('receita', views.receita, name='receita')
]

Salvamos e observamos um destaque em views, indicando que não existe a função receita() ainda. Logo precisamos criá-la em views.py de forma parecida com a feita em index(), pegando a requisição e retornando com a renderização de request e da página de receita.html.

>def index(request):
    return render(request, 'index.html')
>
>def receita(request):
    return render(request, 'receita.html')

Salvo o arquivo, vemos que em url.py há um destaque em vermelho, logo precisamos salvar este último arquivo também, pois há necessidade de uma ordem.

De volta ao navegador, clicamos nos links para testar. Ao clicar em "Receitas", ainda é apresentada uma falha; isso aconteceu porque não alteramos receita.html em Nav Start no arquivo index.html para código Python que informa a url como já vimos.

><!-- Nav Start -->
><div class="classynav">
>    <ul>
>        <li><a href="{% url 'index' %}">Home</a></li>
>        <li><a href="{% url 'receita' %}">Receitas</a></li>
>    <ul>
>
>//código omitido
></div>

Feito isso, podemos retornar à aplicação para atualizar a página e clicar no link de "Receitas". Porém, o visual ainda não está como queremos, e veremos na próxima etapa como melhorar essa questão.

Também lidaremos com a disposição dos arquivos html, pois não precisamos trabalhar com duplicados já que o Django possui um recurso interessante para isso.

### Estendendo html

Nossa página principal está funcionando como esperado. Porém, quando clicamos em "Receitas", acessamos uma página com o visual ainda inadequado. Neste passo, melhoraremos essa questão através de nosso código.

Em index.html, fazemos o carregamento dos arquivos estáticos e suas importações, enquanto em receita.html temos quase todos os mesmos arquivos duplicados de forma parecida. Para evitar isso e deixar nosso código mais elegante, criamos um novo arquivo básico que recebe toda a parte inicial de ambos os códigos até as importações ao final de body>. Será a partir deste que os demais estenderão os recursos.

Dentro da pasta "templates", criamos um novo arquivo chamado base.html. Em index.html, recortamos todo o intervalo de código desde load static até body> ficando somente a partir de Preloader, e colamos no novo arquivo. Em seguida, recortamos todo o trecho final de JavaScript em All Javascript Files e colamos em base.html.

Para indicar que futuramente queremos inserir pedaços de código de outras páginas html entre os recém colados em base.html, usamos código Python para block content, indicando que existe um bloco de conteúdo passado para o trecho em questão encerrado por endblock após body> e antes dos arquivos JavaScript, neste caso.

Salvamos este arquivo e retornamos para index.html. O primeiro passo é adicionar {% load static %} no topo para carregar arquivos estáticos também. Agora, precisamos estender de base.html utilizando o comando extends com o nome do arquivo entre aspas simples em código Python da mesma forma.

    {% extends 'base.html' %}
    {% load static %}

Feito isso, podemos voltar ao navegador e atualizar a página novamente.

O site está todo em branco, pois não indicamos ao index.html que o bloco estendido começa a partir da linha de block content inserida depois do comando que carrega arquivos estáticos e vai até a última linha do texto com end block no formato de código Python.

Desta forma, ao invés de receita.html carregar o trecho individualmente, estendemos do arquivo base.html, carregamos arquivos estáticos e indicamos o início e fim de bloco da mesma maneira que fizemos com index.html.

De volta ao navegador, recarregamos a página e clicamos em "Receitas" para ver o visual mais agradável do que antes. Porém, nem o logotipo nem as imagens são exibidas; aplicamos o código Python para direcionar a url de 'index' e passar as imagens com static na parte de Logo, sem esquecer de inserir as aspas simples no caminho das figuras também.

Testamos a página de receitas novamente. Falta-nos ajustar o footer e as imagens principais da mesma maneira em Receipe Slider e Footer Logo.

Assim, ao invés de carregarmos várias vezes os mesmos arquivos em códigos duplicados, utilizamos base.html com todo o head>, arquivos JavaScript e inserção de trechos de outras páginas com block content e endblock com código Python.

Em nosso projeto, os links estão funcionando, mas se formos à página de receitas e clicar no menu "Home", o navegador aponta um erro. Isso acontece porque temos um Navbar para a página de receitas e outro para index, e não é o que queremos.

### Partials

No passo anterior, aprendemos a estender um arquivos html, mas podemos melhorar ainda mais nosso site através de partials que são pequenos trechos de código html que podem ser compartilhados com outras páginas.

Quando clicamos nos links, tudo está funcionando como esperado. Porém, estando na página de receitas e clicando em "Home", o navegador apresenta um erro. Isso acontece porque não temos o mesmo código da página principal em "Home", e precisamos duplicá-lo.

Indo em receita.html no Visual Studio, temos a parte de Nav Start que deve ser alterada. Mas não queremos ficar alterando em todas as páginas, pois podem ser muitas e seria bastante trabalhoso inserir o código Python para a url de 'index' em todas elas.

Para facilitar, usamos as partials, ou seja, pegamos estes trechos de código do header> e os compartilhamos com outras páginas; desta forma, se precisarmos alterar alguma coisa no menu principal, basta focarmos em um ponto para atingir todas as demais.

Começamos criando uma nova pasta em "templates" chamada "partials". Dentro desta, geramos dois novos arquivos chamados menu.html e footer.html.

Como já temos nosso código Header Area Start correspondente à parte superior da aplicação em index.html, queremos que todas as páginas tenham este cabeçalho também. Para isso, recortamos todo este bloco até /header> e colamos em menu.html.

Salvamos e indicamos ao menu.html que queremos inserir a partial através da inclusão de {% include 'partials/menu.html' %} no local onde estava o bloco recortado de index.html, trazendo este pedaço de volta.

De volta ao navegador, clicamos no logotipo e vemos que um erro de arquivos estáticos não carregados no menu.html é apresentado. Portanto, também precisamos fazer esta indicação escrevendo {% load static %} no topo deste arquivo.

Testamos novamente salvando e atualizando o site no navegador. Estando na página de receitas, clicamos em "Receitas" mais uma vez e observamos o mesmo erro anterior.

Indo em receita.html, acessamos o início de header>, recortamos todo seu trecho de código e embedamos o código Python com include 'partials/menu.html' da mesma maneira.

Salvamos e testamos os acessos pelos links mais uma vez. Como também não queremos código replicado para o footer>, aplicamos a mesma metodologia de recortar este pedaço, colar em footer.html, inserir {% load static %} no início do seu texto, finalizando com a escrita de include 'partials/menu.html' antes de endblock em receita.html.

Fazemos a mesma coisa removendo todo o grande bloco de footer> de index.html para fazer a inclusão das partials de footer.html neste arquivo também.

Testamos o funcionamento dos links em nossa página no navegador.

Portanto, para não termos muitos códigos replicados, criamos as partials e estendemos por um arquivo base.html, melhorando bastante a manutenção e edição de nossos templates.

### Faça como eu fiz na aula
### Exercício: Extends, include e partials

Sabemos que código duplicado não é uma boa prática tornando a manutenção e edição do código muito mais difícil. Pensando nisso, melhoramos o código dos templates utilizando algumas templates tags.

Com base nisso, analise as informações abaixo e marque as verdadeiras em relação a refatoração dos templates.

a) **Alternativa correta: 
A tag usada no template para incluir uma partial é {% include 'nome_da_partial' %}.**
- _Certo! Quando queremos incluir apenas um bloco específico e não uma template completo, utilizamos a tag include._

b) A tag extends pode ser indicada em qualquer parte do template.

c) **Alternativa correta: No Django, podemos evitar código duplicado utilizando herança de template.**
- _Certo! A herança de template permite criar um modelo, como um "esqueleto", contendo elementos comuns que podem ser compartilhados através da tag extends._

## 04. Modelo e banco de dados
### Nomes de receitas dinâmicas

Na etapa anterior, melhoramos o código de nossos templates que estão funcionando tanto na página principal quanto na de receitas.

Agora, precisamos exibir o nome das diferentes receitas que temos. Inicialmente, podemos alterar a nomenclatura em h5> da primeira parte Single Best Receipe Area de "Nome da receita" para "Sopa de legumes", na segunda para "Sorvete" e na terceira para "Lasanha" em index.html.

Salvamos e vemos as três imagens com os nomes recém alterados ao atualizar a página no navegador. Se quisermos inserir uma nova receita, copiamos o bloco de div> e colamos na sequência para alterar seu título.

Desta forma, nossa página exibe o novo item ao ser atualizada. Porém, é bastante trabalhoso fazer isso a cada nova receita incluída, e queremos que seja gerado de forma dinâmica ao só fornecer os nomes diretamente. Em Django, existe uma maneira que consiste em passar uma informação ao template na hora de renderizar a página principal.

Para isso, deletamos os blocos com as receitas para deixar apenas a primeira "Sopa de legumes". Em seguida, acessamos views.py para ver a função render() que recebe a requisição e a página. Ao incluir mais uma vírgula ao argumento, o sistema indica que podemos passar um context com informações em formato de dicionário como terceiro parâmetro.

Dentro dos parênteses de render(), incluímos {} que recebem 'nome_da_receita' e 'Sorvete'. Salvamos e atualizamos a página no navegador.

Como não aparecem alterações, precisamos informar ao template onde nome_da_receita deve aparecer. Para isso, voltamos ao index.html para retirar "Sopa de legumes" da h5>; como queremos que este código seja executado e exiba o resultado na tela, não usamos código Python e sim {{}}. Dentro das chaves, passamos o nome do dicionário nome_da_receita.

    <!-- ##### Best Receipe Area Start ##### -->
    <section class="best-receipe-area">
        <div class="container">
            <div class="row">
                <!-- Single Best Receipe Area -->
                <div class="col-12 col-sm-16 col-lg-4">
                    <div class="single-best-receipe-area mb-30">
                        <img src="{% static 'img/bg-img/foto_receita.png' %}"></img>
                        <div class="receipe-content">
                            <a href="receita.html">
                                <h5>{{ nome_da_receita }}</h5>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

Salvamos e atualizamos a página para ver o novo item gerado com o nome "Sola de legumes". Portanto, podemos passar um dicionário com todas as informações.

Para ficar mais claro, criamos uma variável chamada dados em index() de views.py, passando 'nome_das_receitas' sendo do tipo dicionário receitas. Antes, passamos o dicionário no mesmo local como receitas sendo igual a {} e dentro desta, enumeramos 'Lasanha', 'Sopa de legumes' e 'Sorvete'.

Ao invés de passar nome_da_receita em render(), passamos os dados.

    def index(request):

        receitas = {
            1:'Lasanha',
            2:'Sopa de legumes',
            3:'Sorvete'
        }

        dados = {
            'nome_das_receitas' : receitas
        }
        return render(request, 'index.html',dados)

    def receita(request):
        return render(request, 'receita.html')

Salvamos e acessamos o arquivo index.html para que seja gerado um novo card a cada item que incluirmos no dicinário de forma dinâmica. Abaixo da linha de class="row", processamos um código Python para sabermos quantas receitas temos ao escrever for para cada chave em valor in nome_das_receitas.

Como queremos o valor de cada item, colocamos .items ao final de nome_das_receitas. Além de indicar que temos for, precisamos dizer onde este acaba após <div> da sequência.

E no lugar de nome_da_receita, queremos exibir o valor; portanto, substituímos valor por nome_da_receita. Desta forma,

    <!-- ##### Best Receipe Area Start ##### -->
    <section class="best-receipe-area">
        <div class="container">
            <div class="row">
                {% for chave, nome_da_receita in nome_das_receitas.items %}
                <!-- Single Best Receipe Area -->
                <div class="col-12 col-sm-16 col-lg-4">
                    <div class="single-best-receipe-area mb-30">
                        <img src="{% static 'img/bg-img/foto_receita.png' %}"></img>
                        <div class="receipe-content">
                            <a href="receita.html">
                                <h5>{{ nome_da_receita }}</h5>
                            </a>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

Salvamos e voltamos à aplicação para atualizar a página e avaliar as alterações. Para termos certeza do funcionamento, incluímos um quarto item ao dicionário em views.py, chamada 4:'Bolo de chocolate'. Atualizamos no navegador novamente.

Apesar do visual da página principal estar satisfatório, os links das receitas ainda não estão funcionando, exibindo uma mensagem de erro após serem clicados, pois ainda não trabalhamos nestas partes.

Estamos criando os nomes das receitas e passando informações de views aos templates, mas é arriscado manter todo os dados principais da aplicação em um arquivo. Portanto, é mais interessante mantê-los em um banco com a nomenclatura e seus detalhes como veremos a seguir.

### Banco de dados

Em nossa aplicação, nossas informações das receitas são as que mais importam para este projeto. Portanto, não é interessante armazenar em dicionários e sim em um banco de dados seguro.

Não utilizaremos o banco de dados SQLite que vem com o Django, e sim o PostgreSQL disponível para download aqui. De acordo com o sistema operacional, clicamos no link correspondente para depois clicar em "Download the installer".

Em seguida, é apresentada uma tabela de versões com links de download e observamos que até a versão 10.10 há suporte para todos os sistemas operacionais que já é suficiente para nós, visto que não é um curso específico desta ferramenta, enquanto as superiores existem somente para Mac OS X e Windows x86-64.

Feito o download, damos início à instalação. Salvamos no diretório de nossa preferência e selecionamos todos os comandos disponíveis para dar continuidade. O Setup pede uma senha bastante importante, pois é a que permite o acesso ao sistema. Escolhida uma senha confiável, o instalador pede uma porta para o servidor que pode ser a mesma já sugerida. Em seguida, definimos o "Locale" como "[Default locale]" e finalizamos a instalação com "Finish" após o progresso concluído.

Abrimos o PostgreSQL buscando por pgAdmin 4.app em nosso caso, que inicia o servidor onde fica toda a nossa base de dados. Assim que é aberto, o programa pede a mesma senha definida na instalação para acessar.

Após isso, precisamos criar um tipo de servidor que se conecta à aplicação Django. Na lista lateral, clicamos em "Servers" e selecionamos a opção "Create > Server..." para abrir uma nova janela e nomear como "dbserver" na aba "General". Indo em "Connection" na barra superior de opções desta caixa, preenchemos o campo obrigatório "Hostname/address" com "localhost" de nossa própria máquina que mantém o servidor do PostgreSQL. Em seguida, inserimos a senha para acessá-lo e finalizamos esta etapa no botão "Save" para visualizar nosso novo servidor na lista lateral.

De volta à nossa aplicação Django, alteramos toda a configuração indo no arquivo setting.py em nosso projeto de "alurareceita" para acessar a parte de DATABASES. Nesta, vemos que o database default é o sqlite3, e devemos alterar para o banco de dados que queremos utilizar; mas antes, é necessária a instalação do módulo PostgreSQL para que a aplicação consiga se conectar.

Para descobrir qual é o arquivo que serve como ponte entre ambos, abrimos o terminal que apresenta a venv aberta e digitamos pip install psycopg2 para finalizar com a tecla "Enter" e instalar o módulo. Ainda, é preciso instalar outro escrevendo pip install psycopg2-binary para obter os arquivos binários. Desta forma, conseguimos fazer com que ambos se conectem. Minimizamos o terminal com "Command + J" ou "Ctrl + J".

De volta ao DATABASES, substituímos a extensão .sqlite3 por postgresql em 'ENGINE'. Já em 'NAME', devemos passar o nome do banco de dados; para criá-lo, voltamos ao PostgreSQL para clicar com o botão direito sobre "dbserver" e selecionar "Create > Database...". Na janela, nomeamos o campo "Database" como "alura_receitas" e clicamos em "Save" para ver o novo banco na lista lateral.

Agora, podemos substituir o conteúdo de 'NAME' por somente 'alura-receita' e passamos mais algumas configurações. Para preencher com o 'USER', voltamos ao PostgreSQL, clicamos sobre "dbserver" com o botão direito e acessamos as propriedades para ver que o "Username" da aba "Connection" é "postgres"; logo, escrevemos 'postgres para o usuário principal. Em seguida, passamos o 'PASSWORD' com a senha usada na aplicação entre aspas simples. Por fim, definimos o 'HOST' como 'localhost' e finalizamos esta etapa.

### Psycopg2

O Psycopg é o adaptador de banco de dados PostgreSQL mais popular para a linguagem de programação Python. Ele foi projetado para aplicativos altamente multithread que criam e destroem muitos cursores e produzem um grande número de INSERT ou UPDATE s simultâneos.

#### Instalação
Para instalar este adaptador, dentro de sua venv, execute o seguinte comando:

    pip install psycopg2

Você também pode obter um pacote independente, sem exigir um compilador ou bibliotecas externas, instalando o pacote psycopg2-binary, para instalar execute o seguinte comando:

    pip install psycopg2-binary

>Para conectar nossa aplicação com o banco de dados, é necessário a instalação destes dois módulos!

### Modelo de receita

Instalamos o PostgreSQL, configuramos nossa aplicação para atender o novo banco de dados e agora precisamos salvar informações e exibi-las em nosso site de receitas.

Inicialmente, trabalhamos com outra abstração de código fornecida pelo Django chamada modelos. Acessando esta parte de "Models" na documentação, vemos que são fonte única e definitiva de informações sobre dados, ou seja, criamos um molde a ser usado como base por todos os itens dizendo que toda nova receita possui um nome, data de publicação, tempo, rendimento, categoria, origem do envio, ingredientes e modo de preparo.

Cada modelo Python é uma subclasse de models.Model e cada atributo da classe representa um campo na base de dados. O Django nos fornece uma API com acesso a banco de dados gerado de forma automática, então não precisamos fazer as queries SQL manualmente; inclusive, a página de documentação possui um link "Making queries" com mais informações. Ainda, nos apresenta um exemplo de como escrevemos o código para criar a classe e sua representação no banco.

Para começar a gerar o modelo de receitas no Visual Studio, acessamos o app de receitas na pasta "receitas" e abrimos o arquivo models.py. O primeiro passo é criar a classe Receita() recebendo models.Model, e podemos partir para a criação dos campos.

Como já sabemos os atributos, escrevemos nome_receita sendo igual a um campo com um limite de escrita com a propriedade models.CharField(), a qual contém vários argumentos a serem passados para modularizar da forma como precisamos, e para limitar a escrita do campo a 200 caracteres, aplicamos max_lenght=200.

Em seguida, temos os ingredientes e o modo_preparo que precisam ter uma caixa de texto para uma maior quantidade de palavras através de models.TextField().

Depois, há o tempo_preparo que deve ter um número inteiro pela propriedade models.IntegerField() e o rendimento que pode ter várias formas de preenchimento com letras e números com um limite de 100 caracteres, ficando models.CharField(max_lenght=100).

Por enquanto não trabalharemos com a usuária ou usuário que nos enviou a receita no campo de origem "Por:". Partindo para a categoria, sua descrição é bem curta, então também é models.CharField(max_lenght=100).

Por fim, queremos visualizar a data de publicação da receita através da importação do o módulo datetime a partir de datetime no topo do código. Desta forma, o date_receita é igual a models.DateTimeField() sendo por default=datetime.now, ou seja, teremos o registro do momento da criação da receita. Caso não consigamos pegar esta informações por algum motivo, podemos deixá-lo em branco passando black=true como segundo argumento.

    from django.db import models
    from datetime import datetime

    class Receita(models.Model):
        nome_receita = models.CharField(max_length=200)
        ingredientes = models.TextField()
        modo_preparo = models.TextField()
        tempo_preparo = models.IntegerField()
        rendimento = models.CharField(max_length=100)
        categoria = models.CharField(max_length=100)
        date_receita = models.DateTimeField(default=datetime.now, blank=True)


Assim, temos as principais informações que queremos publicar em nosso site salvas neste arquivos. Agora, devemos passar este modelo para o banco de dados PostgreSQL abrindo um segundo terminal no Visual Studio, sempre conferindo se a venv está ativa.

Para isso, precisamos informar que existem dados antes mesmo de enviá-los através de um código chamado makemigration, o qual prepara migrações a serem feitas. Então, escrevemos python manage.py makemigrations e apertamos a tecla "Enter" para gerar na lista lateral uma nova pasta chamada "migrations" que possui um arquivo 0001_initial.py com todas as informações passadas ao modelo.

De volta ao PostgreSQL, acessamos "dbserver > Databases > alura_receita > Schemas > public > Tables" para clicar neste último item com o botão direito e selecionar a opção "Refresh..." para atualizar as tabelas. Como ainda não há nada, precisamos passar os dados efetivamente, ou seja, criamos uma lista de itens que queremos migrar mas ainda não mandamos de fato.

Na primeira vez que subimos o terminal, apareceu uma mensagem indicando que temos migrações pendentes a serem aplicadas. Estas são relacionadas ao Django Admin que será visto adiante, mas é através dele que todos os apps registrados em models.py são criados, deletados, editados, visualizados e etc., gerando um crude destes modelos.

Como desde o início da aplicação existiam migrações a serem feitas juntando com o modelo que criamos, pedimos ao Python escrevendo python manage.py migrate no terminal. Executando esta ação, o sistema cria tudo o que é necessário para funcionar tanto a parte de Admin quanto a classe e o modelo utilizado.

De volta ao PostgreSQL, atualizamos as "Tables" novamente para ver que, desta vez, são criadas várias tabelas com questões relacionadas ao Admin do Django e nossa receitas_receita ao final. Clicando com o botão direito sobre esta última, selecionamos a opção "View/Edit Data > All Rows" para visualizar todas as linhas presentes e observamos que um campo id é gerado automaticamente conforme a documentação já explicitava.

No passo seguinte, criaremos um Admin para gerar as receitas no banco de dados.

### Exercício: {{ }} e {% %}

Durante o desenvolvimento da nossa aplicação, utilizamos duas formas para embedar código python nos templates, sendo eles:

    {{ }} {% %}

Sabendo disso, podemos dizer que:

a) Alternativa correta: Utilizamos {% %}, para processamento sem exibir na tela, como {% load static %} por exemplo.
- Certo! Quando queremos processar um código sem exibir na tela, por exemplo, utilizando as tags load static, static, if ou for, utilizamos dentro das marcações {% %}.

b) Alternativa correta: Utilizamos {{ }}, para renderizar variáveis no template por exemplo.
- Certo! Quando queremos exibir um conteúdo na página, utilizamos está marcação.

c) Utilizamos {% %}, para renderizar variáveis no template por exemplo.

d) Podemos utilizar qualquer um dos dois, em qualquer parte do template, que teremos o mesmo resultado.

### Exercício: Models no Django

Um modelo é uma forma única e definitiva de informações sobre seus dados. Ele contém os campos e comportamentos essenciais dos dados que você está armazenando.

Sabendo disso, analise as afirmações abaixo e selecione as verdadeiras.

a) Cada modelo é sempre dividido em 6 tabelas diferentes no banco de dados.

b) Alternativa correta: Cada atributo do modelo representa um campo no banco de dados.
- _Certo! Por exemplo:_

        class Person(models.Model):
            first_name = models.CharField(max_length=30)
    Ficaria representado no banco como:

        CREATE TABLE myapp_person (
            "id" serial NOT NULL PRIMARY KEY,
            "first_name" varchar(30) NOT NULL,

c) Alternativa correta: Todo modelo é uma classe Python, subclasse de django.db.models.Model.
- _Certo! Todo modelo é uma classe, conforme podemos ver na documentação._

### Exercício: makemigration e migrate

Após configurar o banco de dados na aplicação, criamos no modelo, a classe Receita, com seus atributos para representar a tabela e seus campos respectivamente.

Sabendo disso, verifique as afirmações abaixo e marque as corretas.

a) O comando makemigrations sincroniza o estado do banco de dados com o conjunto atual de modelos e migrações.

b) Alternativa correta: O comando migrate sincroniza o estado do banco de dados com o conjunto atual de modelos e migrações.
- _Certo! Podemos encontrar mais acessando a documentação._

c) O comando migrate cria novas migrações com base nas alterações detectadas nos modelos.

d) Alternativa correta: O comando makemigrations cria novas migrações com base nas alterações detectadas nos modelos.
- _Certo! Podemos encontrar mais acessando a documentação._

### Para saber mais: Models

#### Models

Vimos que cada modelo é uma classe Python que geralmente é mapeado para ser uma tabela no banco de dados.

Caso queira saber mais sobre Models do Django:

- <a href="https://docs.djangoproject.com/en/2.2/topics/db/models/" target="_blank">Models segundo a documentação oficial do Django (texto em inglês)</a>

## 05. Admin, parâmetros e receitas
### Django Admin

Já conectamos nossa aplicação Django com o banco de dados e criamos um modelo de receitas pela classe Receita(). Nesta etapa, exibiremos as informações do database em nossa página através do Django Admin, o qual é uma das partes mais poderosas segundo a documentação específica sobre esta parte acessível aqui.

Em nosso app de receitas no Visual Studio, temos uma categoria chamada admin.py que possui uma mensagem dizendo para registrarmos nossos modelos neste arquivo. Com isso, conseguiremos acessar uma parte da criação integrada ao projeto Django capaz de criar, deletar e editar receitas, ou seja, teremos um crude completo de receitas.

Para fazer este registro em admin.py, importamos nossa classe Receita de .models no topo do código. Como isso ainda não é suficiente, pedimos ao arquivo que registe o modelo através do código admin.site.register(Receita) e salvamos.

Quando criamos nossa aplicação, temos o arquivo urls.py na pasta "alurareceita" já com o caminho de admin configurado em urlpatterns. Para ter certeza, vamos ao navegador e digitamos "localhost:8000/admin" na barra de busca para ver campos de login da Administração do Django já em português conforme configuramos.

O próximo passo é criar o Admin, visto que o Django não o cria automaticamente. No terminal, digitamos python manage.py seguido do comando createsuperuser. Quando teclamos "Enter", o sistema nos pede um nome de usuário, um e-mail caso queira e uma senha de acesso seguindo as orientações de segurança que o Django nos fornece.

Feito isso, retornamos ao login da Administração do Django no navegador e inserimos o nome do usuário e senha. Ao acessar a página, visualizamos o modelo de receita que registramos no admin.py. Clicamos em "Receitas" para abri-la e clicamos no botão "adicionar receita +" para acessar a parte que nos permite preencher os campos conforme definimos no modelo.

Testamos o funcionamento inserindo informações aos campos e clicando em "Salvar" para conseguirmos visualizar o "Receita object (1)" na lista. Clicando neste item, voltamos aos campos desta receita e testamos alterações no nome ou em qualquer outro atributo.

Agora, precisamos saber se essas informações foram salvas no banco de dados. Voltamos ao PostgreSQL e clicamos com o botão direito em "receitas_receita" dentro de "Tables" na lista lateral selecionando "Refresh...", e depois vemos todas as linhas para conferir se os dados foram realmente salvos.

Estando todas as informações salvas tanto no Admin quanto no banco de dados, significa que estamos realizando a integração da forma como precisamos.

Por fim, resta-nos verificar se os novos itens são exibidos na página principal da nossa aplicação.

### Exibindo dados dos banco

Na etapa anterior, cadastramos uma nova receita com informações nos campos disponíveis na página de Admin do Django. Agora, visto que o arquivo está salvo no banco de dados, não queremos mais visualizar em nosso site o dicionário passado por contexto.

No app de receitas, acessamos views.py e passamos as 'receitas' por contexto aos dados, e não mais 'nome_das_receitas'. Em seguida, deletamos o conteúdo do dicionário em receitas e disponibilizamos o modelo criado ao importar Receita de .models no topo do código.

Com o modelo de receitas acessível, inserimos Receita.objects.all() para trazer todos os objetos salvos no banco de dados. Feito isso, o sistema destaca Receita e exibe uma mensagem dizendo que esta classe não possui objects como membro, o que é uma indicação do próprio Visual Studio e não uma falha de nosso código.

    from django.shortcuts import render
    from .models import Receita

    def index(request):
        receitas = Receita.objects.all()

        dados = {
            'receitas' : receitas
        }
        return render(request, 'index.html', dados)

    def receita(request):
        return render(request, 'receita.html')

Copiamos esta mensagem e a colamos na barra de busca do navegador para clicar no primeiro link do Stack Overflow que nos sugere uma correção a partir de pip install pylint-django que deve ser adicionado em um novo terminal do Visual Studio com venv ligada.

Instalado o pylint-django, a página do Stack Overflow nos orienta a adicionar outro comando às configurações do Visual Studio para evitar este destaque da classe. Copiamos e colamos em setting.json dentro de ".vscode" na aba de "Aplicacao" da lista lateral de arquivos.

    {
        "python.pythonPath": "venv/bin/python",
        "python.linting.pylintArgs": [
            "--load-plugins=pylint_django"
        ],
    }

Assim que este arquivo é salvo, o destaque de Receita desaparece, pois incluímos esta nova verificação de código Django ao Visual Studio.

Se voltarmos à aplicação e atualizarmos a página, todas as receitas somem. Isso acontece porque retiramos o dicionário de views.py e ainda não carregamos os dados do banco para serem visualizados.

Abrindo a pasta "templates", acessamos o arquivo index.html para observamos que aplicamos for para o dicionário, mas agora estamos passando um objeto de fato. Logo, removemos todo o conteúdo do código Python deixando apenas o for. Em seguida, aplicamos outro código Python antes para indicar que, se tivermos o valor receitas armazenado no contexto de dados com if, executamos o código subsequente. Caso não tenhamos com else, nada acontece com endif também em código Python.

Tendo as receitas, queremos pegar cada uma com in dentro da lista de receitas e exibimos seus nomes com receita.nome_receita ao invés de nome_da_receita em <h5>.

    <!-- ##### Best Receipe Area Start ##### -->
    <section class="best-receipe-area">
        <div class="container">
            <div class="row">
                {% if receitas %}
                {% for receita in receitas %}
                <!-- Single Best Receipe Area -->
                <div class="col-12 col-sm-6 col-lg-4">
                    <div class="single-best-receipe-area mb-30">
                        <img src="{% static 'img/gb-img/foto_receita.png' %}" alt=""></img>
                            <div class="receipe-content">
                            <a href="receita.html">
                                <h5>{{ receita.nome_receita }}</h5>
                            </a>
                        </div>
                    </div>
                </div>
                {% endfor %}
                {% else %}
                {% endif %}
            </div>
        </div>
    </section>

Com esse código salvo, retornamos ao navegador e atualizamos nossa aplicação.

Desta forma, o novo item cadastrado no banco de dados é exibido na página inicial mas não acontece o que queremos ao clicar neste item. Adiante, veremos como acessar a página com os detalhes das receitas.

Para garantir o funcionamento, voltamos à página de Admin do Django e cadastramos mais uma receita com suas informações, como "Sorvete" por exemplo. Com o novo objeto exibido na lista, voltamos à aplicação e atualizamos a página novamente.

Com isso, o novo item é apresentado com sucesso. A seguir, resolveremos a questão do "Page not found" que aparece ao clicar no ícone da receita.

### Parâmetro na url

Sempre que clicamos em algum dos itens, não conseguimos visualizar os detalhes da receita em uma próxima página como podemos ver ao clicar no link "Receitas".

Para resolver essa questão, acessamos o index.html no Visual Studio e alteramos o conteúdo de href na parte de Single Best Receipe Area com código Python para encaminhar a url 'receita'.

Salvamos e testamos na página do navegador. Agora somos direcionados à página de receitas, mas queremos visualizar os dados específicos que salvamos no banco. Por exemplo, se clicarmos em "Sorvete", o correto seria acessar as informações que dizem respeito à este item em especial.

Para isso acontecer, passamos um identificador de cada receita que é gerado automaticamente a cada cadastro feito no banco de dados, como vimos anteriormente. Por exemplo, o primeiro item "Sopa de legumes" possui um id 1 e o segundo "Sorvete" é id 2.

Portanto, no mesmo href de Single Best Receipe Area, adicionamos receita.id na sequência do conteúdo com código Python. Isso ainda pode gerar problemas, então precisar antecipar o recebimento de um id neste link de 'receitas' indo em url.py e adicionando '<int:receita_id>' no começo do conteúdo da segunda linha de path().

    urlpatterns = [
        path('', views.index, name='index'),
        path('<int:receita_id>', views.receita, name='receita')
    ]

Feito isso, voltamos ao views.py para indicar o recebimento deste parâmetro em receita().

    def receita(request, receita_id):
        return render(request, 'receita.html')

Se salvarmos o arquivo, retornarmos à aplicação e atualizarmos a página, recebemos um erro "NoReverseMatch at/" indicando que tentamos acessar as receitas mas não foi encontrado nenhum argumento. O navegador nos mostra a falha na segunda linha href na parte de Nav Start, onde aponta para uma 'receita' sem especificar qual.

Então acessamos o arquivo menu.html dentro de "partials" para alterar este mesmo trecho com o erro já indicado. Retiramos esta linha para exibirmos apenas as receitas presentes no banco de dados. Feito isso, voltamos à aplicação, atualizamos a página e vemos que o link "Receitas" não aparece mais enquanto reparamos também que, ao posicionar o cursor sobre o item de cada receita, aparece uma pequena aba no navegador com localhost:8000 seguido do número do id, indicando que está em correspondência.

Porém, ao clicar nos itens principais acessamos a página de receitas sem as informações específicas que queremos. Nesta parte, a barra do navegador indica o endereço terminado com o id do item que está aberto.

Voltamos ao views.py e capturamos o link que contém o id certo da receita dentro de receita(). Para isso, criamos uma nova variável chamada receita a ser exibida e utilizamos get_object_or_404() para fazer a captura do objeto ou exibir um erro 404. Dentro, passamos o modelo Receita e indicamos que o número identificador é uma primary key ou pk igual ao valor.

Em seguida, passamos a informação à página através de receita_a_exibir sendo igual à um dicionário que indica que 'receita' é a receita trazida.

Por fim, adicionamos o mesmo receita_a_exibir como terceiro argumento de render().

    def receita(request, receita_id):
        receita = get_object_or_404(Receita, pk=receita_id)

        receita_a_exibir = {
            'receita' : receita
        }

        return render(request, 'receita.html', receita_a_exibir)

Desta forma, buscamos o valor e vemos um destaque de erro em get_object_or_404() porque ainda não importamos este módulo de django.shortcuts; para isso, adiciomanos uma vírgula após render no import no topo do código e escrevemos get_list_or_404 seguido de vírgula e get_object_or_404.

Salvamos o arquivo e não vemos mais o destaque.

De volta à aplicação no navegador, atualizamos a página e testamos os cliques nos links para ver se está funcionando como esperado.

Ainda não conseguimos visualizar o nome de uma receita específica apesar de termos passado as informações para a página. Acessamos receita.html e observamos a parte Receipe Content Area onde aparece o Nome da receita na linha <h2>. Nesta, substituímos seu conteúdo para exibirmos a receita buscada em views.py através da escrita de '{{receita.nome_receita}}' conforme estabelecemos no modelo.

Salvamos o arquivo, voltamos ao navegador e atualizamos a página para testar os links.

Aparecendo o nome corretamente, retornamos ao receita.html para exibirmos a data da postagem substituindo o conteúdo de span> por '{{receita.date_receita}}' também como também fizemos no modelo. Aplicamos as mesmas alterações com código Python para os demais campos de acordo com os atributos estabelecidos.

Mais adiante na parte Single Preparation Step, substituímos o texto genérico Lorem ipsum pelo modo de preparo '{{receita.modo_preparo}}' e na parte seguinte Ingredientes substituímos o mesmo conteúdo de p> por '{{receita.ingredientes}}'. Desta forma:

    <!-- Receipe Content Area -->
    <div class="receipe-content-area">
        <div class="container">

            <div class="row">
                <div class="col-12 col-md-8">
                    <div class"receipe-headline my-5">
                        <span>{{ receita.date_receita }}</span>
                        <h2>{{ receita.nome_receita }}</h2>
                        <div class="receipe-duration">
                            <h6>Preparo: {{ receita.tempo_preparo }} minutos</h6>
                            <h6>Rendimento: {{ receita.rendimento }}</h6>
                            <h6>Categoria: {{ receita.categoria }}</h6>
                            <h6>Por: Pessoa</h6>
                        </div>
                    </div>
                </div>

            <div class="row">
                <div class="col-12 col-lg-18">
                    <!-- Single Preparation Step -->
                    <div class="single-preparation-step d-flex">
                        <p>{{ receita.modo_preparo }}</p>
                    </div>
                </div>

                <!-- Ingredientes -->
                ,div class="col-12 col-lg-4">
                    <div class="ingredients">
                        <h4>Ingredientes</h4>
                        <div class="ingredients">
                            <p>{{ receita.ingredientes }}</p>
                        </div>
                    </div>

    //código omitido
    </div>

Salvamos o arquivo e conferimos nossa aplicação novamente.

Estando todas as informações corretas de cada item na disposição e forma como elaboramos, podemos testar algumas outras exibições, como inverter a ordem dos campos no código, adicionar mais texto ao modo de preparo para visualizarmos como ficaria com mais descrição e etc.

### Ajudando alguém

Ao longo do curso de Django da Alura, uma das pessoas matriculadas se deparou com um comportamento estranho ao acessar a página em desenvolvimento, que exibiu o seguinte comportamento:

O trecho de código da index:

    <div class="receipe-content">
        <a href="{% url 'receita' receita.id %}">
            <h5>{{ receita.nome_receita }}</h5>
        </a>
    </div>

O trecho de código da views.py:

    def receita(request):
        receita = get_object_or_404(Receita, pk=receita_id)

        receita_a_exibir = {
            'receita' : receita
        }

O trecho de código da urls.py:

    urlpatterns = [
        path('', views.index, name='index'),
        path('<int:receita_id>', views.receita, name='receita')
    ]

A partir disso, onde está o erro e porque temos este comportamento?

a) Alternativa correta: A solução seria adicionar como argumento da função receita, o receita_id.
- _Certo! É necessário indicar o id da receita como argumento da função. Dessa forma, o erro não ocorrerá mais._

b) A solução seria alterar a tag de

    <h5>{{receita.nome_receita}}</h5> para

    <h5>{{receita.nome_receita == receita_id}}</h5>

c) Este erro ocorre por conta do código encontrado no index.html.

d) Este erro ocorre por conta do código encontrado no urls.py.

e) Alternativa correta: Este erro ocorre por conta do código encontrado no views.py.
- Certo! Existe um erro neste trecho de código.

### Para saber mais: Admin

Uma das partes mais poderosas do Django, é sua interface de admin.

Se você quiser saber mais sobre o Django admin, confira a documentação do Django::

- <a href="https://docs.djangoproject.com/en/2.2/ref/contrib/admin/" target="_blank">Django admin segundo a documentação oficial (texto em inglês)</a>

# 2. Integração de modelos no Django: Filtros, buscas e admin
**Fonte:** Guilherme LIma<br>
**Disponível:** <a href="https://cursos.alura.com.br/course/fundamentos-django-2" target="_blank">ALURA</a><br>
**Conteúdo:**
- Realize filtros e crie listas no seu site
- Crie e integre modelos
- Faça o admin do seu site com o Django admin
- Saiba como criar uma página de busca com páginação
---
## 01. Ajustando o Django admin Ver primeiro vídeo
### Introdução

Boas vindas!

Sou o instrutor Guilherme Lima do curso Integração de Modelos no Django 2.

Anteriormente, elaboramos um modelo na primeira parte do treinamento, e agora iremos integrá-lo a um novo que será criado em nossas aulas.

Além disso, faremos algumas configurações para deixar nosso Django Admin muito mais confortável para editarmos nossas receitas.

Daremos continuidade ao desenvolvimento da aplicação, seguindo boas práticas de programação. Aprimoraremos ainda mais o visual, adicionando imagens para cada receita na página principal e um campo de busca por palavras.

Criaremos um outro app para manter armazenadas as pessoas que postaram a receita no Django Admin, que terá um display muito mais agradável. Na parte de receitas, aprenderemos como alterar algumas configurações para termos filtros.

Com isso, aprofundaremos ainda mais nossos conhecimentos sobre Django.

Os pré-requisitos para este curso são ter feito a primeira parte do treinamento, ter noções básicas de Python, HTML, CSS e JavaScript além de darmos continuidade ao que começamos a aprender sobre PostgreSQL.

Ao final de nossas aulas, poderemos criar app mais poderosas utilizando este framework de Django com a linguagem Python, o que é muito relevante para todos que se interessam em desenvolver aplicações web com essas ferramentas.

Vamos lá!

### Listando receitas por nome

Daremos continuidade ao desenvolvimento da aplicação Alura Receita.

Começamos pela atualização de uma receita, como a "Sopa de legumes" por exemplo: queremos modificar o tempo de preparo de 40 para 30 minutos e o rendimento de 6 para 4 porções.

Para isso, acessamos o Admin adicionando /admin ao endereço do navegador, clicamos no link "Receitas" para visualizar a lista com os itens, abrimos a "Receita object" correta e alteramos as informações dos campos finalizando em "Salvar". Retornamos à página da aplicação e atualizamos para ver se os dados foram alterados corretamente.

Porém, a exibição desses itens na lista de Receitas em Admin não estão informativos o suficiente para saber a quais receitas correspondem, e precisamos clicar em cada um para descobrir do que se tratam, o que é pouco prático principalmente pensando no crescimento constante dessa lista. O ideal seria visualizar o id e o nome para ficar claro.

Indo ao nosso código no Visual Studio, acessamos nosso app de "receitas" e abrimos o arquivo admin.py. Observamos que passamos nosso modelo Receita como argumento para admin.site.register(), e podemos criar uma nova classe para este chamada ListandoReceitas() que recebe admin.ModelAdmin. Dentro desta, passamos uma edição para o display da nossa lista pelo código list_display, indicando que queremos o 'id' e o 'nome_receita', o qual deve ser o mesmo presente em models.py.

De volta ao Admin do Django, atualizamos a página com a lista e não vemos nenhuma diferença; isso se deu porque criamos a classe ListandoReceitas() e ainda não a passamos ao admin.site.register() quando registramos a aplicação. Além de fazer o registro do modelo, queremos também a configuração do display que acabamos de implementar.

    from django.contrib import admin
    from .models import Receita

    class ListandoReceitas(admin.ModelAdmin):
        list_display = ('id', 'nome_receita')

    admin.site.register(Receita, ListandoReceitas)

Salvamos e voltamos à página para atualizar e ver que agora são apresentados os id e nomes das receitas na lista de Admin.

Se quisermos exibir também outros campos como a categoria e o tempo de preparo por exemplo, basta adicionar 'categoria' e 'tempo_preparo' ao list_display, ou qualquer outro atributo do modelo. Desta forma, está muito mais claro saber qual item corresponde a qual receita.

Para acessarmos os itens da lista, devemos clicar somente nos números de id, mas é interessante podermos transformar os nomes das receitas em links de acesso também. Para isso, basta adicionar list_display_link sendo igual a id e 'nome_receita' na classe ListandoReceitas().

    from django.contrib import admin
    from .models import Receita

    class ListandoReceitas(admin.ModelAdmin):
        list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo')
        list_display_links = ('id', 'nome_receita')

    admin.site.register(Receita, ListandoReceitas)

Salvando o arquivo com estas configurações, podemos clicar também nos nomes das receitas para acessá-las. Inclusive, podemos fazer edições nos campos para testar a atualização.

Com tudo funcionando corretamente, podemos seguir adiante.

### Busca, Filtros e paginação

No passo anterior, alteramos nosso código para que nossos itens sejam visualizados de forma bem mais clara na lista do Django Admin.

Nesta etapa, veremos novas configurações para manipular melhor nossa receitas, como a implementação de um buscador por palavras.

Indo à classe ListandoReceitas() no arquivo admin.py, começamos incluindo search_fields sendo igual ao campo que queremos buscar, como 'nome_receita' por exemplo e salvamos o arquivo.

De volta à página de Admin do Django, atualizamos e um erro aparece. Voltamos ao terminal do Visual Studio para receber uma mensagem de erro dizendo que o valor search_fields precisa ser uma lista ou uma tupla, e passamos um valor específico. Então, adicionamos uma vírgula após 'nome_receita' para o erro não ser exibido novamente.

Atualizando a aplicação, vemos um campo de busca no topo da lista de receitas na Administração. Podemos testar escrevendo "sorvete" por exemplo para encontrarmos apenas a receita com essa palavra, ou partes desta palavra.

Para manipularmos melhor nossas receitas, podemos exibir um filtro por categoria através da propriedade list_filter sendo igual a ('categoria',), sem esquecer a vírgula para evitar o problema já visto.

De volta à aplicação, aparece um novo espaço com o filtro por categoria de acordo com o que estabelecemos, lembrando de manter a grafia correta.

Criamos mais uma receita de "Pudim" para incluir na categoria de "sobremesa", a mesma do sorvete. Preenchemos os campos com um texto qualquer somente para conseguirmos visualizar e testar o funcionamento das buscas e do filtro.

Pensando no crescimento de nosso projeto com cada vez mais itens, nossa lista pode ficar gigantesca e pouco prática. Para melhorar essa questão, criamos uma paginação para a lista de forma bastante simples através da propriedade list_per_page que pode receber um número específico de receitas por página. Como ainda temos poucos elementos, fazemos igual a 2.

    from django.contrib import admin
    from .models import Receita

    class ListandoReceitas(admin.ModelAdmin):
        list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo')
        list_display_links = ('id', 'nome_receita')
        search_fields = ('nome_receita',)
        list_filter = ('categoria',)
        list_per_page = 2

    admin.site.register(Receita, ListandoReceitas)

Voltamos ao Admin do Django e percebemos as páginas exibidas com o número de itens que estabelecemos. Podemos adicionar ainda mais receitas para testarmos essa nova configuração. Desta forma, podemos buscar receitas e organizá-las em páginas de forma mais agradável.

### Exercício: Melhorando o admin

Para melhorar o admin do Django, exibindo informações como id, nome da receita, categoria e tempo de preparo, além de incluir links para editar a receita, filtros e paginação, uma pessoa incluiu o seguinte código:

    from django.contrib import admin
    from .models import Receita

    class ListandoReceitas(admin.ModelAdmin):
        list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo')
        list_display_links = ('id', 'nome_receita')
        search_fields = ('nome_receita',)
        list_filter = ('categoria',)
        list_per_page = 2

    admin.site.register(Receita)

Sabendo disso, o que vai acontecer quando a pessoa acessar o app de receita através do admin?

a) O admin será carregado apenas com o filtro e a paginação funcionando.

b) Alternativa correta: O admin será carregado, porém sem nenhuma das configurações citadas acima.
- _Certo! É necessário passar a classe ListandoReceitas no momento que registramos o app, como segundo argumento: admin.site.register(Receita, ListandoReceitas)._

c) O admin não será carregado, e um erro será exibido.

d) O admin será carregado com todas as configurações citadas acima.

## 02. Quem postou a receita?
### Criando um modelo de pessoas

Criamos algumas novas receitas e melhoramos a página de Admin para organizar melhor as informações. Mas podemos aperfeiçoar a aplicação ainda mais, como veremos nesta etapa.

Sempre que acessamos uma receita a partir da página principal, vemos os dados e características específicas de cada uma. Porém, em todas elas, ainda é exibida a origem da postagem como "Por: Pessoa", e queremos que seja visível o nome de quem enviou a receita.

Da mesma forma que criamos e registramos o app para manipular a Administração de forma mais eficaz, criaremos um outro para gerar algumas pessoas e vincular este novo app com o de receitas.

Começamos abrindo uma nova janela de terminal no Visual Studio conferindo se a venv está realmente ligada para dizer ao Python que queremos criar um novo app para as pessoas que enviam receitas. Escrevemos python manage.py startapp pessoas e quando apertamos a tecla "Enter", o sistema cria um novo diretório chamado "pessoas".

Para fazer com que pertença à nossa aplicação, vamos ao "alurareceita" onde estão as configurações em settings.py para visualizarmos os apps instalados, como o 'receitas'. Adicionamos 'pessoas' seguido de , ao INSTALLED_APPS.

Feito isso, nosso app está registrado. Agora, criamos algumas pessoas na aplicação indo ao arquivo models.py dentro de "pessoas" e geramos uma classe chamada Pessoa() que será representada como uma tabela no banco de dados com cada campo sendo um atributo.

Esta nova classe recebe models.Model como argumento. Em seguida, queremos que a pessoa tenha um nome sendo igual a um tipo de texto models.Charfield() passando um limite de max_length igual a 200. Também queremos que cada pessoa registrada possua um email com a mesma propriedade e limite anterior.

    from django.db import models

    class Pessoa(models.Model):
        nome = models.CharField(max_length=200)
        email = models.CharField(max_length=200)

Criado este modelo, precisamos registrá-lo no admin.py deste mesmo diretório, para que este seja capaz de criar essas pessoas. Primeiro, importamos o modelo Pessoa de .models no topo do código e depois inserimos que admin.site.register() deve registrar Pessoa como argumento.

    from django.contrib import admin
    from .models import Pessoa

    admin.site.register(Pessoa)

Salvamos e abrimos o terminal para executar o comando python manage.py makemigrations que cria a migração de pessoas com a tecla "Enter". É criada uma nova pasta "migrations" com o arquivo 0001_initial.py com a migração.

De volta ao admin.py de "pessoas", abrimos o terminal e inserimos o comando python manage.py migrate para gerar a pessoa no banco de dados. Com isso, abrimos o PostgreSQL e clicamos em "Tables" com o botão direito para selecionar "Refresh..." e atualizar as tabelas para ver se a tabela "pessoas_pessoa" é apresentada na lista lateral.

Em seguida, atualizamos a página de Admin do Django e vemos o item "Pessoas" na lista. Ao clicar neste link, não há nenhuma pessoa registrada ainda e criamos uma nova clicando em "Adicionar pessoa", preenchendo os campos com dados de nome e e-mail e finalizando em "Salvar".

Feito isso, temos uma nova pessoa na lista sob nome de "Pessoa object (1)". Da mesma forma que fizemos anteriormente, queremos melhorar a visualização das informações indo ao app "pessoas" para abrir o arquivo admin.py. Podemos abrir a classe de "receitas" para seguir a metodologia de filtros aplicada em seu admin.py para a classe ListandoReceitas() como exemplo.

Adaptando e simplificando a lista de pessoas, criamos uma classe ListandoPessoas() de admin.ModelAdmin em admin.py de "pessoas". Dentro desta classe, passamos o list_display com o 'id','nome' e o 'email' da pessoa e, como queremos que mais aspectos sejam links clicáveis, adicionamos list_display_links para id e 'nome'.

Ainda, podemos adicionar as propriedades search_fields e list_per_page sendo 'nome' e 2 respectivamente para o campo de busca e a paginação, sem esquecer a vírgula após o argumento desta primeira. Por fim, passamos a nova classe para o registro.

    from django.contrib import admin
    from .models import Pessoa

    class ListandoPessoas(admin.ModelAdmin):
        list_display = ('id', 'nome', 'email')
        list_display_links = ('id', 'nome')
        search_fields = ('nome',)
        list_per_page = 2

    admin.site.register(Pessoa, ListandoPessoas)

Salvo este arquivo, retornamos à página de Admin do Django e atualizamos a parte da lista de pessoas para ver se as configurações foram efetuadas.

Podemos testar criando outras pessoas e conferir se está tudo funcionando como esperado.

A seguir, vincularemos as pessoas às receitas, dizendo que quem enviou a receita exibida no site.

### Integrando modelos

No passo anterior, criamos "pessoas_pessoa" no banco de dados e o app que mantém um crude completo deste elemento. Agora, vincularemos às nossas receitas informando quem enviou uma determinada receita.

Acessando a página de "Models" da documentação do Django neste link, temos uma parte falando sobre relacionamentos entre tabelas e classes em "Relationships"; nesta, há um exemplo que nos permite ver algo parecido com nossa aplicação.

As duas classes do exemplo criam um relacionamento entre si através da chave estrangeira models.ForeignKey(), onde a segunda se refere à anterior. Além de receber a primeira classe como argumento, esta chave também recebe on_delete=models.CASCADE, significando que o Django aplica um comportamento de restrição ao SQL e também exclui o objeto que contém a ForeingKey(), sendo exatamente o que precisamos para nossa aplicação.

Em nosso projeto atual, se criarmos e vincularmos as receitas com as pessoas, podemos gerar um erro de integridade, pois já possuímos dados anteriores que não têm um registro de quem os enviou. Como apenas criamos receitas de exemplo para testarmos, podemos removê-las para dar continuidade.

De volta à Administração de Django, acessamos "Início > Receitas > Receitas" para deletar os itens da lista clicando em "Selecionar todos receitas" e escolhendo a opção "Remover receitas selecionados" para finalizar em "Ir". Em seguida, o sistema confirma a ação e prosseguimos.

Com os objetos excluídos e fora da aplicação, podemos manipular nossos dados. Acessando o models.py de "receitas", informamos que sempre há uma pessoa vinculada quando uma receita é gerada por meio de um novo campo pessoa sendo igual a models.ForeignKey() da mesma forma que o modelo de exemplo da documentação. Para a chave estrangeira, passamos a classe de Pessoa e on_delete=models.CASCADE. Por fim, precisamos somente importar Pessoa de pessoas.models no topo do código e salvamos o arquivo.

    from django.db import models
    from datetime import datetime
    from pessoas.models import Pessoa

    class Receita(models.Model):
        pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
        nome_receita = models.CharField(max_length=200)
        ingredientes = models.TextField()
        modo_preparo = models.TextField()
        tempo_preparo = models.IntegerField()
        rendimento = models.CharField(max_length=100)
        categoria = models.CharField(max_length=100)
        date_receita = models.DateTimeField(default=datetime.now, blank=True)

Com isso, fazemos uma alteração em nossa classe que referencia as tabelas e campos no banco de dados. Para inserir isso no database, geramos uma migração no segundo terminal com a venv ligada e escrevemos python manage.py makemigration para executar o comando com "Enter".

O sistema indica que estamos tentando popular alguns campos que possuem algumas linhas, e nos oferece duas opções: podemos prover um valor defaut agora ou podemos adicionar este valor em models.py. Optamos pela primeira opção digitando 1 como resposta ao terminal. Em seguida, definimos uma String vazia com '' para este valor default, fazendo com que seja gerada a migração de receita.

Desta forma, migramos para o banco de dados pelo comando migrate no terminal como já vimos. De volta à aplicação, atualizamos a página para ver que os itens desaparecem, pois as removemos.

Na página de Admin, clicamos em "Receitas > Receitas" para adicionar um novo item. O primeiro campo apresentado é o "Pessoa" com uma barra contendo as opções criadas sob nome de "Pessoa object". Continuamos preenchendo os campos somente como teste e finalizamos em "Salvar".

A seguir, veremos como obter uma identificação mais clara dentro do campo "Pessoa" da forma como se apresentam na lista com seus nomes corretos.

### Exibindo nome das pessoas

Agora, sempre que criamos uma nova receita, temos um campo chamado "Pessoa"; porém, sua identificação não é clara pois não são nomeados adequadamente, apenas como "Pessoa Object" seguido do número identificador.

Em nossa lista de Pessoas no Admin do Django, vemos que cada id corresponde à um nome específico, sendo justamente o que queremos visualizar no novo campo de cadastro.

Para fazermos isso, voltamos ao models.py de "pessoas" e definimos uma nova classe em Pessoa com def chamada __str__(). Dentro, referenciamos o próprio objeto que queremos exibir através de self e, em seguida, retornamos seu nome adicionando .nome para substituir "Receita Object".

    from django.db import models

    class Pessoa(models.Model):
        nome = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        def __str__(self):
            return self.nome

Com isso, o objeto referenciado sempre retornará o nome próprio de quem enviou a receita. Salvamos o arquivo e atualizamos a página de cadastro de novos itens no Admin para ver a alteração no campo "Pessoa".

Estando as identificações corretas, podemos ver mais claramente a usuária ou usuário que postou a receita. Porém, quando retornamos à página principal da aplicação e clicamos em um item, o campo "Por:" ainda é preenchido por "Pessoa" nas informações.

Para conseguirmos visualizar o nome e alterarmos essa exibição, acessamos receita.html dentro de "templates" para observar a forma como trouxemos os demais campos da receita. Como adicionamos a referência de pessoa ao modelo de receitas e já buscamos todas as Receitas em views.py, a pessoa também está vinculada; logo, apenas substituímos Pessoa pelo código Python {{}} contendo receita.pessoa em Por: na linha <h6> de receita.html, conforme temos na classe de Receita() do modelo.

De volta à aplicação, vemos o nome da usuária ou usuário no campo "Por:" da página de detalhes. Fazemos um teste adicionando uma nova receita à lista para ter certeza de que a origem da postagem é exibida pela nomenclatura correta.

Estando a visualização de acordo com o que queremos, significa que criamos e vinculamos os modelos com sucesso tanto em nossos templates quanto nas referências aos objetos, tornando o acesso muito mais prático e claro.

### Exercício: '__str__'

Para descobrir quem postou a receita, criamos o app de pessoa e o modelo, conforme o código abaixo.

    from django.db import models

    class Pessoa(models.Model):
        nome = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        def __str__(self):
            return self.nome

Analisando o código acima, podemos afirmar que:

a) O método __str__ indica que os atributos nome e email são do tipo texto.

b) O método __str__ indica que o atributo nome é do tipo texto.

c) Alternativa correta: O método __str__ substitui o nome padrão dos objetos dessa classe para o nome da pessoa.
- _Certo! Dessa forma, no lugar do nome Pessoa object(1), podemos ver o nome armazenado no atributo nome da classe Pessoa._

## 03. Filtros e categorias
### Filtro receitas publicadas

Gostaríamos de criar algumas receitas mas sem publicá-las no site para realizarmos algumas edições. Com base no que já temos, criamos uma nova receita chamada "Bolo de chocolate (edição)" de categoria "bolo" para fazer este teste preenchendo os campos com informações e selecionando alguma das pessoas.

Porém, quando atualizamos a aplicação, esta receita aparece e não é o que queremos. Para evitar que seja exibida pois pode ser que haja algo a alterar, criamos uma forma de indicar quais itens queremos publicar e quais estarão em modo de edição sem visualização na página.

No Visual Studio, acessamos o app de "receitas" para abrir models.py e criamos um novo campo determinando verdadeiro ou falso para sabermos se a receita está publicada ou não. Se sim, corresponde a True e se não, a False.

Na classe Receita(), adicionamos o novo campo chamado publicada sendo igual a models.BooleanField(). O primeiro argumento é o valor defaut do item como False; desta forma, quando criamos uma nova receita, não queremos que fique com publicada como flag verdadeira.

Como alteramos a classe, devemos subir a atualização para o banco de dados através do comando python manage.py makemigrations no terminal para criar a migração, sempre atentando à venv. Feito isso, migramos com migrate da mesma forma que já conhecemos.

Salvamos e retornamos à lista de "Receitas" no Admin do Django. Abrindo o item "Bolo de chocolate", notamos um novo campo "Publicada" com a opção de marcação vazia, pois o padrão é False. Salvamos e voltamos à página principal para atualizá-la e ver que esta receita em modo de edição ainda está aparecendo. Ao verificarmos as outras receitas que estão exibidas, estas também não estão marcadas como publicadas com True.

Criamos este novo atributo e indicamos se é verdadeiro ou falso, mas ainda não alteramos o código no momento em que as informações são enviadas para serem renderizadas.

Para conseguirmos visualizar somente os valores das receitas marcadas com True, precisamos modificar a views.py de "receitas" no Visual Studio. Na definição de index(), pegamos todas as receitas com objects.all() sem considerar a flag que implementamos.

Primeiro, alteramos a forma como estamos buscando nossos objetos retirando .all() e depois indicamos um filtro com .filter() recebendo o campo publicada somente com valor True.

    def index(request):
        receitas = Receita.objects.filter(publicada=True)

        dados = {
            'receitas' : receitas
        }
        return render(request, 'index.html', dados)

Ao atualizarmos a página principal da aplicação, todas as receitas desaparecem conforme esperamos, já que nenhuma está com essa marcação positiva. Editamos um dos itens para marcar a opção de "Publicada", salvamos e voltamos ao nosso site para ver que somente esta é exibida, significando que fizemos a configuração com sucesso.

### Ordenação e edição no admin

Anteriormente, criamos uma forma de exibir apenas as receitas que possuem a flag de "Publicada" como verdadeira. E sabemos que basta marcar essa opção positivamente para fazer com que um item em edição seja visível na página principal.

Porém, também é interessante apresentar essa marcação na linha de cada receita da lista da Administração do Django ao invés de somente na parte exclusiva de edição dos campos. Desta forma, acessamos mais rapidamente a informação de quais itens estão publicados e quais não estão.

Para isso, acessamos o arquivo admin.py da pasta "receitas". Neste, temos a classe ListandoReceitas() exibindo quatro dados na lista com list_display, e adicionamos mais 'publicada' à este.

    class ListandoReceitas(admin.ModelAdmin):
        list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')
        list_display_links = ('id', 'nome_receita')
        search_fields = ('nome_receita',)
        list_filter = ('categoria',)
        list_per_page = 2

Salvamos, voltamos à lista do Admin e atualizamos a página para ver se a flag da opção "Publicada" é exibida na lista. Em seguida, visualizamos mais receitas alterando o conteúdo de list_per_page para 5, vendo se o novo campo é apresentado com seu status.

Estando as modificações corretas, podemos prosseguir; se quisermos alterar o status de publicação de uma receita, precisamos acessar sua parte de edição dos campos, desmarcar a opção "Publicada", salvar e somente assim podemos ver um "x" neste item recém retirado da página principal, o que é um passo bem grande.

Para simplificar a marcação das receitas publicadas e não publicadas, queremos que esta opção esteja disponível na listagem e não somente na edição interna.

Como já temos o campo 'publicada' em list_display, precisamos criar uma nova forma de indicar que este pode ser editado na lista através de list_editable sendo igual a 'publicada' entre parênteses seguido de uma vírgula, visto que também se trata de uma tupla.

    class ListandoReceitas(admin.ModelAdmin):
        list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')
        list_display_links = ('id', 'nome_receita')
        search_fields = ('nome_receita',)
        list_filter = ('categoria',)
        list_editable = ('publicada',)
        list_per_page = 2

Salvamos, voltamos à lista do Admin, atualizamos a página e vemos as marcações editáveis em cada linha de receitas, facilitando a publicação ou não destas. Também, aparece um botão de "Salvar" para executar as edições, e podemos testar seu funcionamento vendo se aparecem ou não na página principal da aplicação.

Outra alteração interessante diz respeito à forma como exibimos os nossos campos, pois se acessarmos models.py de 'receitas", temos date_receita que pode ser usada para que a lista seja ordenada por data de publicação.

Primeiro, para alterar a ordenação, acessamos views.py que possui um filtro de exibição em index() e criamos um segundo adicionando order_by() recebendo 'date_receita' em Receitas.objects de receitas. Para que as mais recentes apareçam primeiro, adicionamos - ao início do novo comando.

    def index(request):
        receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

        dados = {
            'receitas' : receitas
        }
        return render(request, 'index.html', dados)

Salvamos, voltamos à página principal da aplicação e avaliamos se as receitas estão ordenadas da mais recente para a mais antiga. Podemos adicionar mais itens publicados para este teste também.

Feito isso, podemos dar continuidade.

### Foto para cada receita

No passo anterior, alteramos nosso Admin para editarmos as receitas que podem ou não ser publicadas no site, gerando um resultado bem interessante.

Porém, os itens ainda estão com uma imagem padrão na tela principal e na página de detalhes, e precisamos adicionar fotografias específicas referentes à cada receita.

Começamos alterando o modelo no app de "receitas" para incluir um novo campo de armazenamento de imagem, chamado foto_receita sendo igual a models.ImageField() recebendo o local de upload da foto. Em nosso projetos, estamos executando localmente direto da máquina como vimos no curso anterior, portanto precisamos salvar em um diretório exclusivo para nossas imagens.

Dentro de models.ImageField(), aplicamos upload_to para indicar o caminho sendo igual a 'fotos/, seguido de %d, %m e %Y para ser baseado no dia, mês e ano de criação sem termos problemas de sincronização conforme as receitas são criadas. Depois, como segunda opção, adicionamos blank=True para que o comportamento seja de deixar em branco caso o item não possua uma imagem própria.

    from django.db import models
    from datetime import datetime
    from pessoas.models import Pessoa

    class Receita(models.Model):
        pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
        nome_receita = models.CharField(max_length=200)
        ingredientes = models.TextField()
        modo_preparo = models.TextField()
        tempo_preparo = models.IntegerField()
        rendimento = models.CharField(max_length=100)
        categoria = models.CharField(max_length=100)
        date_receita = models.DateTimeField(default=datetime.now, blank=True)
        foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
        publicada models.BooleanField(default=False)

Salvamos e acessamos setting.py de "alurareceita" para gerarmos dois novos comportamentos na aplicação que indicam o uso de arquivos de mídia como imagens do site. Neste arquivo, temos uma rota para arquivos estáticos e adicionamos outra rota para estes novos tipos de documentos para possibilitar o upload das fotos.

Ao final do texto, inserimos MEDIA_ROOT sendo nosso próprio diretório os.path.join() passando BASE_DIR seguido de 'media'. Em seguida, escrevemos outra configuração chamada MEDIA_URL para referenciar '/media/', pois no banco de dados é salvo o caminho para uma determinada imagem, e não esta propriamente dita.

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'alurareceita/static')
    ]

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

Feitas essas alterações nas configurações e no modelo, precisamos rodar as migrações no terminal com python manage.py makemigrations. Ao executar, o sistema aponta a necessidade da instalação do módulo Pillow através do comando pip install pillow. Em seguida, atualizamos a versão de pip escrevendo pip install --upgrade pip e terminamos fazendo a migração efetiva novamente.

Desta forma, podemos visualizar a migração no novo arquivo 0004_receita_foto_receita.py na pasta "migrations". Depois, mandamos para o banco de dados abrindo o terminal e escrevendo python manage.py migrate, como já conhecemos.

Podemos ver no aplicativo PostgreSQL ao clicar com o botão direito em "receitas_receita" da lista lateral para escolher a opção "View/Edit Data > All Rows". Assim, visualizamos todas as linhas e vemos um novo campo "foto_receita" como aplicamos.

Se voltarmos à lista do Admin do Django e atualizarmos a página, o navegador aponta uma falha; indo ao primeiro terminal no Visual Studio, o sistema indica que instalamos o Pillow mas não subimos o servidor novamente. Limpamos a tela do terminal e escrevemos python manage.py runserver.

Retornamos à lista do Admin para atualizarmos a página mais uma vez. Sendo exibida sem problemas, clicamos em "Adicionar receita" e vemos um novo campo "Foto receita:" com a opção de escolher uma imagem para upload através do botão "Choose File". Também é possível editar uma receita já existente e carregar sua fotografia.

Escolhida uma fotografia de nossa preferência para um item específico do site, podemos voltar ao PostgreSQL, clicar com o botão direito sobre nossa tabela e visualizar todas as linhas para observar que o campo "foto_receita" possui um caminho indicado na receita que recebeu o upload de uma imagem.

Nosso próximo passo é conseguir exibir as fotos nas receitas das páginas principais e na página de seus detalhes.

### Configurações do Admin

Durante o desenvolvimento de uma aplicação Django, dividimos nossa aplicação em 2 partes: nosso site e o admin do Django, onde criamos os conteúdos que serão exibidos no site.

Porém, no Django é possível filtrar ou ordenar os objetos que queremos renderizar no site.

Sabendo disso, analise as afirmações abaixo e marque as verdadeiras.

a) Não é possível ordenar os objetos por datas maiores primeiro.

b) Alternativa correta: É possível adicionar mais de um filtro.
- _Certo! Podemos adicionar mais de um filtro, por exemplo: Receita.objects.order_by('-data_receita').filter(publicada=True).filter(tempo_preparo=10)._

c) Alternativa correta: É possível buscar todos os objetos, sem filtros e sem ordenação.
- _Certo! Podemos buscar todos os objetos, por exemplo: Receita.objects.all()._

## 04. Buscando receitas
### Exibindo a foto

Feito o upload da fotografia que queríamos para uma receita específica, precisamos exibi-la no lugar da imagem padrão presente na página principal e na de detalhes.

Para isso, acessamos urls.py em "alurareceita" para indicar o uso das configurações de mídia recém incluídas em settings.py. Começamos incluindo + ao final de urlpatterns seguido de static() que recebe setting.MEDIA_URL onde estão os caminhos, seguido de document_root igual a settings.MEDIA_ROOT.

    from django.contrib import admin
    from django.urls import path, include

        urlpatterns = [
            path('', include('receitas.urls')),
            path('admin/', admin.site.urls),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Desta forma, indicamos que estes arquivos cujos uploads foram permitidos podem ter suas urls utilizadas pela aplicação.

Quando adicionamos a foto à receita, um novo folder "media" aparece na lista lateral do Visual Studio, contendo o caminho de pastas de acordo com o dia, mês e ano de publicação que leva ao arquivo final de mídia propriamente dito.

Quando salvamos o código, um destaque de erro em static() é apresentando, pois o sistema não conhece nem este nem o arquivo de settings, ou seja, precisamos fazer seus imports no topo do código.

    from django.contrib import admin
    from django.urls import path, include
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path('', include('receitas.urls')),
        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Assim, os erros desaparecem quando salvamos e tornamos possível encontrar o caminho para carregar a imagem no banco de dados.

Agora, criamos uma verificação que avalia se uma receita possui uma fotografia e, caso não possua, queremos carregar a imagem padrão que aparece na página principal. Para isso, acessamos index.html e observamos que há a linha <img> na parte de Single Best Receipe Area que carrega o ícone quando não temos uma foto.

Portanto, dentro do loop de receita, escrevemos código Pyhton para processamento {% %} recebendo if para verificar o caso de receita.foto_receita ser igual a nulo, o que exibe a imagem padrão.

Caso não seja null, o site deve apresentar a url dos arquivos de mídia configurada na aplicação, ou seja, o objeto manipulado receita.foto_receita.url também com código Python de processamento, bastante parecido com o que usamos nos arquivos estáticos. Em seguida, fechamos a verificação com endif.

    <!-- ##### Best Receipe Area Start ##### -->
    <section class="best-receipe-area">
        <div class="container">
            <div class="row">
                {% if receitas %}
                {% for receita in receitas %}
                <!-- Single Best Receipe Area -->
                <div class="col-12 col-sm-16 col-lg-4">
                    <div class="single-best-receipe-area mb-30">
                        {% if receita.foto_receita == '' %}
                            <img src="{% static 'img/bg-img/foto_receita.png' %}">
                        {% else %}
                            <img src="{{ receita.foto_receita.url }}" alt="">
                        {% endif %}
                            <div class="receipe-content">
                            <a href="receita.html">
                                <h5>{{ receita.nome_receita }}</h5>
                            </a>
                        </div>
                    </div>
                </div>
                {% endfor %}
                {% else %}
                {% endif %}
            </div>
        </div>
    </section>
Salvamos e retornamos à aplicação para atualizar a página principal e ver se a imagem esperada é apresentada. Depois, clicamos no item para abrir a parte de detalhes da receita e ver que a fotografia ainda é a padrão, e não a que foi carregada.

Conforme estabelecido, a padrão deve ser exibida quando não tivermos uma imagem específica. Voltamos ao código index.html para copiar a linha de if, else, caminho do arquivo e endif que acabamos de escrever, e colar na parte Receipe Slider em receita_html que contém o local da foto padrão.

    <!-- Receipe Slider -->
    <div class="container">
        <div class="row">
            <div class='col-12">
                <div class "receipe-slider owl-carousel">
                    {% if receita.foto_receita == null %}
                        <img src="<% static 'img/bg-img/tomate_banner.jpg' %}"
                    {% else %}
                        <img src="{{ receita.foto_receita.url }}" alt="">
                    {% endif %}
                </div>
            </div>
        </div>
    </div>

Salvamos e voltamos à aplicação para testar o funcionamento das modificações. Podemos adicionar mais receitas sem upload de imagens ou publicar as que não possuem nenhuma para terminar a verificação, vendo se a foto padrão é exibida nesses casos.

Quando estamos na página de detalhes e clicamos em "Alura Receita" para voltar ao index, o navegador apresenta um erro; isso acontece porque utilizamos null em index.html e receita.html, e precisamos alterar para apenas uma string vazia com '' nos dois arquivos.

Feito isso, podemos observar os itens que possuem e os que não possuem uma fotografia específica referente à receita, de acordo com as configurações que fizemos.

Desta forma, garantimos tanto as imagens de upload quanto as padrões da aplicação.

### Criando a página de busca

Incluímos uma imagem para nossas receitas e, caso não tenhamos, exibimos apenas a foto padrão. Para nosso site ficar ainda melhor, é interessante que todas as receitas visíveis na página principal tenham sua própria fotografia.

Começamos marcando como publicadas as receitas que queremos exibir e fazemos o upload de uma imagem para elas. Assim que terminamos e atualizamos a página principal, temos um visual bem mais agradável. Entramos em cada uma para ver os detalhes e se a imagem é apresentada nesta parte também.

Todos os links presentes parecem estar funcionando; porém, ao clicar no ícone de busca representada por uma lupa, escrever alguma palavra e finalizar com "Enter", o navegador aponta um erro com a mensagem "Proibido".

Queremos que o site apresente os itens do resultado da busca. Para resolver este problema, criamos uma rota para identificar o caminho buscado.

Indo ao código de urls.py dentro de "receitas" no Visual Studio, observamos os path() para views.index e views.receita, e precisamos criar para a busca também.

Nomeamos este novo path() como 'buscar' e adicionamos o método views.buscar, linkando o nome do caminho por meio de 'buscar'.

    from django.urls import path

    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
        path('<int:receita_id>', views.receita, name='receita'),
        path('buscar', views.buscar, name='buscar')
    ]

Desta forma, quando quisermos encontrar este path(), utilizamos código Python digitando url e 'buscar' através de name.

Salvamos e vemos um destaque em views indicando que não há 'buscar' em views.py de "receitas", portanto precisamos criá-lo. Acessamos este último arquivo e definimos o novo método buscar() recebendo a request. Sempre quando conseguimos receber este método, precisamos renderizar para ter outra página carregada com return e render() recebendo a requisição como primeiro parâmetro e o template buscar.html.

    def buscar(request):
        return render(request, 'buscar.html')

Salvamos este arquivo e o urls.py para resolver a questão do destaque apresentado. Como ainda não temos este template relacionado à busca, precisamos criá-lo na pasta "templates".

Abrindo-a, clicamos no ícone de "New file" e nomeamos como buscar.html. Neste, testamos o fluxo colocando uma linha h1> com o escrito "Buscar". De volta ao index.html, acessamos a parte de busca em Search Wrapper para ver form que aponta ao símbolo "#", o qual não é o que queremos utilizar, pois pretendemos renderizar a imagem de fato e encaminhar ao index.html.

Fazemos isso apagando somente o trecho "#" method="post">da linha a partir de '<form action= para que este receba "{% url 'buscar' %}">', embedando código Python de processamento.

Este 'buscar' é o mesmo name criado em urls.py anteriormente, e quando clicarmos o formulário de busca, o sistema encaminha à url para carregar a página buscar.html com escrito de "Buscar". Com isso, criamos um novo path e um novo método em views.py para atender esta requisição.

Voltamos à aplicação, atualizamos a página e clicamos no ícone da lupa para abrir a barra de busca. Digitamos alguma palavra-chave existente em alguma das receitas para testar. Quando teclamos "Enter", conseguimos carregar a nova página e visualizar a mensagem "Buscar" conforme planejado.

Na barra de endereço do navegador, aparece "search=" seguida da palavra buscada, mas queremos que apareça "buscar" em seu lugar. De volta à parte Search Wrapper do index.html, temos a linha com input type="search" name="search"; ao invés de "search" em type, escrevemos "text" e no lugar de "search" como conteúdo de name, apenas digitamos "buscar" para realizar esta alteração.

    <!-- Search Wrapper -->
    <div class="search-wrapper">
        <!-- Close Btn -->
        <div class="close-btn"><i class= "fa fa-times" aria-hidden="true"></i></div>

        <div class "container">
            <div class="row">
                <div class="col-12">
                    <form action="{% url 'buscar' %}">
                        <input type="text" name="buscar" placeholder="O que está procurando..."></input>
                        <button type="submit"><i class="fa fa-search" aria hidden="true"></i></button>
                    </form>
                </div>
            </div>
        </div>
    </div>

Voltamos a aplicação, atualizamos e testamos a busca novamente para ver as mudanças na barra de navegação.

Porém, não é interessante apenar exibir uma página com um título "Buscar" quando a usuária ou usuário realizar uma busca por palavras; queremos que o resultado seja apresentado devidamente, e podemos exibir o mesmo layout da página inicial somente com as receitas filtradas pela procura.

Para isso, começamos acessando o arquivo index.html, copiamos todo seu código e colamos em buscar.html após deletar a linha <h1>Buscar</h1> para facilitar o trabalho, já que ambas devem ser parecidas.

Para a página renderizar, passamos receitas com if em Best Receipe Area Start, enquanto em views.py o render() da função buscar() não recebe nenhuma receita.

Salvamos o arquivo buscar.html e retornamos para a aplicação, atualizando sua página inicial. Abrimos a barra de busca acessível pela lupa e escrevemos alguma palavra existente nos títulos das receitas publicadas para testarmos o direcionamento.

Fazendo isso, aparece nosso site sem nenhuma receita. É o que planejamos, mas é interessante apresentar alguma mensagem à usuária ou usuário quando nenhum resultado é encontrado para a busca, como "Receita não encontrada".

Para isso, vamos ao template buscar.html e vemos a pergunta if para exibir cada receita em loop com o código subsequente caso ela exista, e não implementamos nenhuma ação para o caso else de não haver nenhuma. Portanto, usamos este último elemento para informar a ausência de resultados para a busca.

Copiamos a linha div class="col-12 col-sm-6 col-lg-4"> e a colamos logo após {% else %}. Em seguida, abrimos um parágrafo p> para digitar "Receita não encontrada".

Retornamos à aplicação, atualizamos a página e fazemos uma busca qualquer para ver a nova mensagem incluída.

Porém, mesmo que a palavra buscada exista nos títulos de receitas publicadas, não visualizamos os resultados corretos que deveriam ser exibidos. Portanto, veremos a seguir como exibir as devidas receitas buscadas a partir do que foi digitado pela usuária ou usuário.

### Resultado da busca

Nesta etapa, exibiremos os resultados da busca. Por exemplo, se temos uma receita de "Suco verde", queremos que esta seja exibida como resultado da procura pela palavra "suco".

Para isso, alteramos o código de views.py de "receitas" para conseguirmos obter todos os objetos e filtrá-los pelo conteúdo da busca posteriormente, seguindo a mesma metodologia aplicada para as receitas publicadas ou não com filter().

Começamos copiando a primeira linha de index() deste arquivo que possui o recurso filter() e colando em buscar() mais adiante no texto. Como trouxemos todas as receitas, alteramos o nome da variável de receitas para lista_receitas.

Agora, verificamos se de fato temos algum escrito na barra de 'buscar' com if, vendo se há valor na requisição com in request. Caso haja conteúdo, adicionamos .GET: seguido de nome_a_buscar que representa o nome da receita, sendo igual ao valor presente na barra de endereço do navegador quando procuramos alguma palavra em nossa aplicação através da marcação "buscar", ou seja, request.GET['buscar'].

Em seguida, perguntamos com if se temos de fato temos um valor de busca e devemos filtrar com filter() desta lista lista_receitas sendo igual a lista_receitas.filter() recebendo nome_receita, da mesma forma que escrevemos em nosso modelo.

Para verificarmos se o que foi digitado está presente em algum dos nomes das receitas, colocamos __ após nome_receita seguido de icontains, o qual procura tudo relacionado ao valor inserido na barra de busca. Na sequência, comparamos com = se é nome_a_buscar.

Feito isso, criamos a variável de dados da mesma forma feita em index() para passarmos os valores ao momento de serem renderizados. Então, escrevemos 'receita' do tipo lista_receitas já com o filtro por data e publicação e, caso tenhamos o valor na busca, exibimos somente a lista de receitas entre chaves.

Como fizemos a verificação em receitas na função de buscar.html, não precisamos realizar nenhuma alteração. Por fim, passamos esta informação de dados como contexto de render() para o template.

    def buscar(request):
        lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

        if 'buscar' in request.GET:
            nome_a_buscar = request.GET['buscar']
            if nome_a_buscar:
                lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

        dados = {
            'receitas' : lista_receitas
        }

        return render(request, 'buscar.html', dados)

Salvamos, retornamos para a aplicação no navegador, atualizamos a página e testamos o mecanismo de busca por alguma palavra ou letra presente nos títulos das receitas.

Estando tudo funcionando com os itens filtrados pela procura ou todas as receitas exibidas em caso do campo vazio, precisamos fazer com que a página de busca seja exibida ao realizarmos outra pesquisa por palavra ou letra estando na parte de detalhes da receita aberta, pois quando o fazemos, o navegador apresenta um erro com "Proibido".

Para resolver essa questão, precisamos que as linhas de \<form>, \<input> e \<button> presentes na parte de busca do index.html seja idêntico ao da página receita.html; copiamos e colamos para que sejamos direcionados corretamente.

    <!-- Search Wrapper -->
    <div class="search-wrapper">
        <!-- Close Btn -->
        <div class="close-btn"><i class= "fa fa-times" aria-hidden="true"></i></div>

        <div class "container">
            <div class="row">
                <div class="col-12">
                    <form action="{% url 'buscar' %}">
                        <input type="text" name="buscar" placeholder="O que está procurando..."></input>
                        <button type="submit"><i class="fa fa-search" aria hidden="true"></i></button>
                    </form>
                </div>
            </div>
        </div>
    </div>

Salvamos e testamos o funcionamento da aplicação.

Estando tudo conforme esperado, percebemos um código duplicado do formulário de busca em ambos os templates. Isso pode ser problemático, pois se alterarmos algo em um dos trechos, devemos modificar o outro da mesma forma para que se mantenham iguais.

Mais adiante, melhoraremos este nosso código quebrando-o em partials.

### Foto no banco de dados

Para possibilitar o upload de imagens para cada receita, adicionamos o seguinte atributo no models.py de receitas:

foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)

Porém, o que será salvo no banco de dados?

a) A imagem da receita no tamanho real.

b) Alternativa correta: A url com o caminho da foto.
- _Certo! Será salvo o caminho da imagem da receita, e não a imagem propriamente dita._

c) A imagem da receita comprimida.

## 05. Autorização e melhorando o código
### Autorização e usuários

Quando acessamos a página de detalhes da receita, há um campo de busca em formato de lista com opções como "Comida típica brasileira", por exemplo.

Nesta fase do curso, não criaremos as edições para este elemento, mantendo esta mesma edição. Então, comentamos este trecho de código em receita.html envolvendo todo o bloco de Receipe Post Search em <!-- no início e --> ao final.

Salvamos, retornamos para a aplicação e vemos o desaparecimento deste campo. Por enquanto, deixaremos o layout assim pois desenvolveremos esta parte em outra etapa do curso.

Neste passo, nos voltamos para a página de Administração do Django; em nosso treinamento, utilizamos os apps de "Receitas" e "Pessoas", criando um relacionamento entre ambas e gerando-o no banco de dados. Porém, ainda não lidamos com a parte de "Autenticação e Autorização" que contém "Grupos" e "Usuários".

Dentro de Django, é possível criar um determinado tipo de usuário capaz de tomar decisões e realizar modificações e outro grupo que não possui essas autorizações.

Clicando no item "Usuários", acessamos uma lista e clicamos no botão "Adicionar usuário" para inserir um nome fictício no campo "Usuário" e uma senha qualquer. Clicando em "Salvar", acessamos outra página com outros campos de observações, informações pessoais e permissões.

Na parte de "Permissões", temos três opções que podem ser marcadas: "Ativo", "Membro da equipe" e "Status de superusuário". O primeiro significa que este usuário pode criar outros e fazer login, o segundo permite que acesse a parte de Administração do Django e o terceiro indica que possui todas as permissões sem atribuí-las explicitamente. Começamos marcando apenas as duas primeiras opções.

Mais adiante, temos a parte de "Permissões do usuário" que possui as ações que a usuária ou usuário cadastrados podem tomar, como criar pessoas ou receitas na aplicação, ou até mesmo atribuir algumas autorizações. Nesta seção, selecionamos as opções que queremos liberar na janela "permissões do usuário disponíveis" e com a seta as transferimos para a janela de "permissões do usuário escolhido(s)". Segurando a tecla "Command" ou "Ctrl", selecionamos mais de uma opção para a transferência.

Desta forma, estabelecemos quais funções a usuária ou usuário pode exercer. Feito isso, finalizamos em "Salvar" e retornamos à lista para ver o novo item cadastrado.

Para acessar a página de Admin com outro usuário, clicamos em "Encerrar Sessão" e depois em "Acessar novamente" para fazer o login com os novos dados registrados. Dependendo de como foram estabelecidas as permissões, a página de Administração do Django apresenta diferenças de lista, acesso e ações.

Quando modificamos algum dado como o nome do item por exemplo, após salvar aparece uma faixa informando que o "Receita object" foi alterado com sucesso. Já sabemos como alterar para o nome correto da receita, então acessamos o arquivo models.py de "receitas" e definimos uma nova função na classe Receita() chamada __str__() recebendo a propriedade self. Em seguida após o :, indicamos o retorno de self.nome_receita.

    from django.db import models
    from datetime import datetime
    from pessoas.models import Pessoa

    class Receita(models.Model):
        pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
        nome_receita = models.CharField(max_length=200)
        ingredientes = models.TextField()
        modo_preparo = models.TextField()
        tempo_preparo = models.IntegerField()
        rendimento = models.CharField(max_length=100)
        categoria = models.CharField(max_length=100)
        date_receita = models.DateTimeField(default=datetime.now, blank=True)
        foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
        publicada models.BooleanField(default=False)
        def __str__(self):
            return self.nome_receita

Salvamos e atualizamos a página de Admin do Django. Editamos a informação de algum item novamente para ver se seu nome correto é exibido na mensagem de confirmação da alteração. Se a nomenclatura certa é apresentada, fica bem mais fácil identificarmos qual receita foi modificada.

Agora, encerramos a sessão e acessamos novamente com nosso login de superusuário original com todas as funções disponíveis para ver a página de Administração da forma como a víamos anteriormente.

Este é uma parte poderosa de Django que nos permite a fácil manutenção e gestão da aplicação; podemos ter pessoas para cada função com diversos níveis de autorização, distribuindo atividades com o recurso de "Permissões".

### Partial e refatoração

Para evitarmos códigos duplicados no formulário de busca interna em nossas páginas buscar.html, receita.html e index.html, bem como erros em caso de alteração em algum desses arquivos que demandariam as mesmas mudanças em todos, criamos uma nova partial chamada busca.html.

Selecionamos "partials" e clicamos no item de "new file" para nomear como busca.html na lista lateral do Visual Studio. Este novo arquivo deve receber todo o bloco de código de Search Wrapper, e com isso podemos apagar os trechos duplicados das páginas já citadas.

Nas demais partials, indicamos o carregamento de arquivos estáticos escrevendo {% load static %} no topo do código, e replicamos este mesmo comando em busca.html.

    {% load static %}

    <!-- Search Wrapper -->
    <div class="search-wrapper">
        <!-- Close Btn -->
        <div class="close-btn"><i class= "fa fa-times" aria-hidden="true"></i></div>

        <div class "container">
            <div class="row">
                <div class="col-12">
                    <form action="{% url 'buscar' %}">
                        <input type="text" name="buscar" placeholder="O que está procurando..."></input>
                        <button type="submit"><i class="fa fa-search" aria hidden="true"></i></button>
                    </form>
                </div>
            </div>
        </div>
    </div>

Salvamos o arquivo e agora podemos incluir a partial de busca.html em cada umas das três páginas que antes continham o código duplicado, escrevendo então `{% include 'partials/busca.html' %}` no lugar dos trechos recortados de Search Wrapper.

Indo ao index da aplicação, atualizamos e testamos a busca por palavra tanto na página principal quanto na de detalhes da receita novamente, para então confirmar que os arquivos estão funcionando como esperado.

Portanto, basta utilizar a partial de busca com include embedando Python nos arquivos necessários para evitar os potenciais problemas de códigos duplicados.

É comum indicar as partials com um undeline na frente de seu nome. Clicamos com o botão direito sobre busca.html na lista lateral e selecionar "Rename" para alterar para _busca.html. O mesmo se aplica aos demais, ficando _footer.html, _menu.html.

Com isso, precisamos atualizar os trechos de código que reutilizam essas partials para o nome corrigido com _, como é em index.html, receita.html e buscar.html. Testamos a aplicação para ver se tudo foi alterado corretamente e está funcionando como esperado.

    {% include 'partials/_busca.html' %}

Com isso, deixamos bem mais claro que se trata de partials. Caso tenhamos qualquer alteração em alguma delas, temos mais segurança de que sejam compartilhadas e executadas corretamente nos demais arquivos que as utilizam.

### Exercício: Template tags

Para evitar código duplicado, refatoramos o código html para evitar duplicidade de código, criando a partial _busca.html.

Em relação às templates tags, analise as afirmações abaixo e marque as verdadeiras.

a) Alternativa correta: Usamos a template tag `{% extends %}` para herdar outro template.
- Certo! Por exemplo, caso queira herdar um template base, o código seria: `{% extends 'base.html' %}`.

b) Dentro do template, devemos utilizar para carregar arquivos estáticos {% include static %}.

c) Para adicionar uma partial chamada minhapartial.html, poderia adicionar o código `{{ include 'partials/minhapartial.html' }}`

# 3. Autenticação no Django? formulários, requisições e mensagens
**Fonte:** Guilherme LIma<br>
**Disponível:** <a href="https://cursos.alura.com.br/course/fundamentos-django-2" target="_blank">ALURA</a><br>
**Conteúdo:**
- Aprenda a criar um sistema de autenticação de usuários não vinculado ao Django admin
- Saiba como trabalhar com formulários no Django
- Desenvolva uma aplicação com requisições protegidas, evitando falsificação de requisições
- Melhore a experiência dos usuários do seu site, enviando mensagens de sucesso e de erro
- Crie uma aplicação inspirada num produto real
---
## 01. App de usuários
### Introdução

Meu nome é Guilherme Lima, muito boas vindas à terceira parte do nosso treinamento de Django 2.

Nesse momento do curso, abriremos nossa aplicação para Autenticação de Usuários, aprenderemos a trabalhar com Formulários e com algumas Validações.

Sempre que desejássemos criar uma nova receita na nossa aplicação, tínhamos que colocar o nome como do administrador principal.

Com o acesso no admin, clicávamos nas opções "Receitas > Adicionar receita", e criávamos uma receita nova. Para visualizá-la, marcávamos a flag de "publicada" ou não.

Vamos fechar a aba da aplicação e agora, nessa terceira parte das aulas, abriremos a possibilidade de outras pessoas criarem novas receitas, não-vinculadas com nosso admin do Django.

Criaremos um formulário de cadastro em que será possível criarmos nossa própria conta. Em seguida, realizaremos o login com uma conta, por exemplo, "gui@alura.com", com a senha "123".

Acessaremos a conta e então veremos que alguns links iniciais mudaram. Teremos a Página Principal, na qual veremos todas as aplicações.

CLicando em Minhas Receitas, haverá receitas que não estarão disponíveis para a aplicação no geral, apenas para o usuário.

Selecionando a foto de algum alimento na página, por exemplo, o pão, será aberto o Modo de Preparo, detalhes e Ingredientes do pão, assim como a torta de morango.

Assim, conseguiremos criar nossas próprias receitas. Quando clicarmos em "Criar Receita" no menu, não seremos direcionados para o admin, mas para um novo formulário com campos para preencher.

Aprenderemos como obter os valores dos campos, criar os formulários, ligar as informações que buscamos com o admin do Django, e assim por diante.

Além de tudo, poderemos fazer o Logout, e novamente veremos alterações na página se sairmos da conta. Visualizaremos somente o cadastro e o login.

Teremos o campo de busca, que já desenvolvemos anteriormente em treinamentos.

Como pré-requisito, é aconselhável já ter acompanhado os cursos de Django 1 e 2, pois sendo uma continuidade, o aprendizado fará muito mais sentido.

Aprenderemos os conceitos básicos de formulário numa aplicação com Django nesse curso, direcionado, provavelmente, para quem ainda não é um super desenvolvedor Django que já trabalha com a ferramenta há algum tempo.

Ele tem como base os principais passos de como trabalhar com as requisições, formulários, tabelas, como vincular tabelas com informações que queremos inserir fora do admin. Então, é bastante indicado fazer o treinamento para quem quer dar continuidade aos cursos de Django 1 e 2.

Sabendo de tudo isso, vamos começar.

### Saudações e ambiente

É muito bom receber você nesta terceira parte do curso. Espero que seja uma experiência de aprendizado incrível e que possamos vencer todos os desafios e continuar o desenvolvimento utilizando o Django.

Divisão das aulas
Aula	O que vamos aprender nesta aula?
App de usuários	Vamos criar um formulário para cadastrar usuários no nosso site
Formulários no Django	Vamos aprender como trabalhar com formulários no Django
Autenticação de usuários	Vamos autenticar os usuário efetuando o login e logout
Formulário de receita	Vamos permitir que usuários logados criem suas próprias receitas
Refatoração e mensagens	Vamos exibir mensagens de sucesso e de erro, além refatorar nosso código
Preparando ambiente
Este curso é a terceira parte dos treinamentos de Django 2 da Alura. Portanto, é recomendado que você tenha feito a segunda parte do curso – Integração de modelos no Django 2: Filtros, buscas e admin.

Para conseguir acompanhar este curso, é recomendado que você tenha o Python3 instalado.

Caso necessite ajuda para instalação do Python, recomendamos os seguintes links:

Passo a passo para instalar o Python3 no Windows.

Passo a passo para instalar em outros sistemas operacionais.

Além disso, para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

Python 3.7.4
Django 3.0.3

O Django pode ser instalado através do comando:

    pip install Django==3.0.3

Em caso de dúvida na instalação ou durante o curso, conte sempre com o fórum da Alura!

Vamos começar?

:)

### Criando o app de usuários

Daremos continuidade no desenvolvimento da nossa aplicação em Django.

Temos nosso site, que está bonito, porém, sempre que precisamos criar uma nova receita, temos que acessar a parte do Administrador e digitar nome e senha.

Depois, acessamos "Receitas", onde veremos as receitas que já estão publicadas, e selecionamos "Adicionar receitas", para preencher os campos e gerar a nova receita.

Quando marcamos a flag de "Publicada", a receita então aparece no site.

Há 3 receitas publicadas, o Suco verde, o Bolo de chocolate e a Sopa. Se voltarmos às receitas no admin, veremos que as 3 publicadas estão com a flag de publicação corretamente selecionada. A "Receita teste" não está publicada, e portanto, não a visualizamos na nossa página.

Mas queremos que qualquer pessoa que faça um cadastro no site e realize um login possa criar e visualizar suas próprias receitas, como se esse fosse um diário de receitas de cada um, não-vinculadas com as receitas publicadas na nossa aplicação.

Para isso, um caminho que poderemos utilizar será o "auth_user", uma tabela para conseguir vincular um usuário na aplicação, que depois será validado para poder criar uma receita.

Aprenderemos várias maneiras de exibir as receitas de cada usuário não vinculando com a aplicação. E caso nós administradores do projeto acharmos alguma receita específica interessante, marcando a flag "Publicada" ela passará a aparecer também na nossa página.

Para começar, vamos ao nosso código, onde o terminal estará aberto, rodando nossa aplicação. Abriremos mais um terminal.

Como queremos abrir nossa aplicação para que mais usuários utilizem nosso site, criaremos um novo app, sem vinculá-lo com o app de pessoas. Vamos vincular com o app de usuários, para utilizar as características do "auth_user" do Django.

Para gerar o novo app usaremos o comando python manage,py startapp e daremos um nome para ele. Como queremos um app de usuários, vamos chamá-lo de usuarios. Pressionaremos o "Enter" e ele será criado para nós.

Assim que criamos o app e queremos vinculá-lo com a aplicação, vamos ao "alurareceita", onde estão as configurações. Abriremos "settings.py" e minimizaremos nosso terminal.

Scrollaremos o código um pouco para baixo e conseguiremos observar que alguns apps já estarão instalados,pessoas' e 'receitas'. Acrescentaremos mais um, 'usuarios', que acabamos de criar. Colocaremos uma vírgula após o nome dele, assim como fizemos com os demais.

Então, criamos e registramos nosso novo app de usuários. Agora, observaremos nosso site novamente, e veremos que há o "Alura Receita", a "Home" e o campo de busca. Se digitarmos "sopa" nesse campo, aparecerá a sopa.

Gostaríamos que na nossa tela mesmo houvesse um link para cadastrar e um para login, direcionando para novas páginas. Por isso, criaremos algumas rotas para conseguir esses links.

Para começar, vamos a "usuarios", e já teremos dentro da pasta alguns itens criados por padrão do Django. Vamos gerar um novo arquivo .py. clicando no ícone de "New file". Nomearemos como "urls.py" e pressionaremos "Enter".

Temos um "urls.py" em "receitas". Então, faremos a cópia do código desse arquivo, e colaremos no "urls.py" de "usuarios", para facilitar. Assim, só faremos algumas modificações.

Apagaremos os paths, deixando apenas o primeiro, para criar nossas urls. Nossa intenção será criar uma url, por exemplo, para o 'cadastro'. Escreveremos ainda o método cadastro ao lado de views. e após name´=.

Outra url será a de 'login. Para isso, também criaremos um novo path, com path('login', views.login, name='login').

Assim que uma pessoa fizer o login, queremos que ela vá para uma determinada página. Essa página será chamada de 'dashboard'. Também terá um método dashboard em views e o name será dashboard.

Além do login, será comum nas aplicações termos a possibilidade de deslogar, com o logout para sair do site. Por isso, também colocaremos um path para o 'logout', seguindo a mesma lógica de código dos demais.

    from django.urls import path

    from . import views

    urlpatterns = [
        path('cadastro', views.cadastro, name='cadastro'),
        path('login', views.login, name='login'),
        path('dashboard', views.dashboard, name='dashboard'),
        path('logout', views.logout, name='logout'),
    ]

Assim que salvarmos, o erro de sintaxe nos alertará de que não há nas"views.py" nenhum item chamado logout. Então, precisaremos criá-lo.

Abriremos "views.py" de "usuarios" e criaremos métodos para cada uma das nossas funções. Em primeiro lugar, teremos uma função que será o cadastro(), e terá como parâmetro a requisição request, como já vimos nos módulos anteriores do curso. Inicialmente, para todas as funções usaremos o pass como retorno.

Depois, faremos uma função para nosso login(), que receberá request como parâmetro também. Usaremos o mesmo para todos os métodos.

Na sequência, haverá a função logout(). Por fim, escreveremos a dashboard().

    from django.shortcuts import render

    def cadastro(request):
        pass

    def login(request):
        pass

    def logout(request):
        pass

    def dashboard(request):
        pass

Vamos salvar o código, voltar para "views.py" e salvar também.

Porém, queremos conseguir visualizar essas páginas na nossa aplicação. Faremos isso no próximo vídeo.

### Cadastro e login

Agora que criamos nosso app de usuários e nossas views para cada url que queremos acessar, vamos em "alurareceita" e incluiremos novos paths de url.

Vamos em "url.py" onde há a inclusão dospaths de receita e incluiremos mais um, 'usuarios/'. Na url, deve ficar marcado que estamos nesse path, por isso escreveremos uma / após o nome, assim como fizemos para o 'admin/'.

    from django.contrib import admin
    from django.urls import path, include
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path('', include('receitas.urls')),
        path('usuarios/', include('usuarios.urls')),
        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Vamos salvar e agora precisaremos criar os templates das páginas, tanto do login, do cadastro e dashboard. Começaremos pensando no cadastro e login.

Todos os nossos templates estão dentro do nosso app de receitas, pois anteriormente, só tínhamos ele, então fazia sentido mantê-los ali. Nesse caso, nossa aplicação está crescendo, então não será uma boa ideia todos os templates ficarem dentro desse app.

A página de "templates" ficará agora no mesmo nível dos apps. Portanto, sempre que quisermos alterar um template ou alguma página html, não precisaremos entrar em nenhum app. Removeremos a página de "receitas" e vamos deixá-la no nível dos apps. Será perguntado se temos certeza da ação, e clicaremos em "*Move&".

Porém, como mudamos a página de templates, precisaremos ir às configurações da aplicação e dizerem que local estarão os apps. Em "settings.py" de "alurareceita" teremos um diretório dizendo onde estarão os arquivos templates, páginas html da aplicação.

Como não estaremos mais em "receitas", mas sim no mesmo nível do nosso projeto, deixaremos apenas a palavra 'templates' nas configurações, não mais 'receitas/templates'.

Se voltarmos à aplicação e atualizarmos, tudo estará funcionando corretamente, mesmo após termos feito a alteração. Vamos testar, pesquisando "bolo" na barra de busca, e o Bolo de chocolate será trazido para nós sem problemas.

Agora, já que temos a nossa pasta de "templates" com os templates da nossa aplicação e queremos vincular mais páginas relacionadas a usuários,criaremos uma nova pasta clicando no ícone de "New folder" e vamos chamá-la de "usuarios".

Dentro da pasta de "usuarios", vamos criar os arquivos "login.html" e "cadastro.html". Colocaremos um `<h1>Cadastro</h1>` na página de cadastro e um `<h1>Login</h1>` na de login para visualizarmos melhor.

Voltando à aplicação, se digitarmos "localhost 8000/login" e clicarmos "Enter", a página não será encontrada, porque criamos o método em "view.py" do app de usuário, mas não estamos pedindo para que essa página seja mostrada.

Para fazer isso, colocaremos um return e diremos para que nossa página seja renderizada, com render(). O primeiro parâmetro será a requisição, request, e o segundo será o nome do template, 'cadastro.html'.

Pediremos para o login ser renderizado também, e assim testaremos os dois, com `return render(request, 'login.html')`.

    from django.shortcuts import render

    def cadastro(request):
        return render(request,'cadastro.html')

    def login(request):
        return render(request, 'login.html')

    def logout(request):
        pass

    def dashboard(request):
        pass

Vamos salvar e voltar à aplicação. Atualizaremos a página com o endereço "localhost 8000/login" e teremos a página com o título, Buscaremos por "localhost 8000/cadastro" e da mesma forma, veremos a página do cadastro.

Porém, não fará sentido, porque como comentamos anteriormente, a intenção é que o usuário não saia da aplicação para se logar ou se cadastrar. Já temos o administrador do Django que sai da aplicação, mas nesse momento, a pessoa deverá se manter na aplicação para gerar suas receitas num ambiente com a mesma aparência na parte superior, no rodapé e assim por diante.

Para ganhar tempo, teremos disponível nas atividades da aula um link para fazer download dos arquivos de páginas "login.html" e "cadastro.html". Assim, não precisaremos nos estender falando sobre html, e focaremos no Django.

Vamos copiar esses arquivos baixados e colaremos no nosso projeto. Poderemos usar o "Ctrl + A" para selecionar tudo, e na sequência o "Ctrl + C" e o "Ctrl + V" para colar os códigos em "login.html" e "cadastro.html".

Visualizando o arquivo html por cima, estamos estendendo um arquivo base.html, indicando que temos arquivos estáticos, além dele indicar que temos arquivos para ser renderizados.

Criamos partials de busca e de menu, o que fará sentido, já que na nossa aplicação não temos partial de menu com esses links. Nosso menu mostrará apenas um link, o da Home, e o objetivo é que haja o link tanto da página do login quanto do cadastro.

Então em "partials > _menu.html", copiaremos a linha responsável pelo link da Home duas vezes. Chamaremos a Home de "Página Principal". Na segunda linha, colocaremos o título de "Cadastro", e na terceira, "Login".

Voltando na nossa aplicação, quando atualizarmos, teremos links para a Página Principal, Cadastro e Login. Se clicarmos na Página Principal, vamos para a página.

Clicando no Cadastro, veremos o formulário, com campos para digitar nome, e-mail, criar uma senha e confirmá-la, além do botão para criar uma conta.

Clicando no Login, também veremos a opção de logar com e-mail e senha criada, e o botão para acessar a conta. Caso ainda não tenhamos uma conta, há o botão para criar, que direciona para o cadastro.

Nossas duas páginas ficaram interessantes. A seguir, daremos vida a elas, pois vamos de fato criar uma conta, cadastrando com um novo usuário, e depois realizar o login. `

### Renderizando as páginas

Uma pessoa decidiu criar um formulário não vinculado ao Django admin para realizar o login de seus usuários criando duas telas: cadastro e login, com os respectivos códigos abaixo:

views.py

    def cadastro(request):
    return render(request,'usuarios/cadastro.html')

    def login(request):
    return render(request, 'usuarios/cadastro.html')

urls.py

    from django.urls import path
    from . import views

    urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    ]

usuarios/login.html

    <h1>Tela de Login</h1>

usuarios/cadastro.html

    <h1>Tela de Cadastro</h1>

Com base no código acima, podemos afirmar que:

a) Apenas a página de login será exibida.

b) A pessoa terá o resultado esperado, visualizando as duas páginas.
- Com base no código acima, não será possível visualizar as duas páginas.

c) Alternativa correta: Apenas a página de cadastro será exibida.
- _Certo! Quando chegar uma requisição para login, é possível ver que o método encontrado na views.py irá devolver como retorno a renderização de cadastro, gerando o comportamento não esperado. Sendo assim, esse código deveria ser:_

    def login(request):
        return render(request, 'usuarios/login.html')

## 02. Formulário no Django
### Requisições no Django

Agora que conseguimos visualizar nosso formulário de criação de campos, vamos preencher nossos campos, e no momento em que clicarmos no botão "Criar sua conta", a tabela "auth_user" deverá inserir esses dados e criar o novo usuário.

Depois, conseguiremos realizar o login no site e criar nossas próprias receitas.

Mas como pegaremos as informações inseridas nos campos para de fato criar um novo usuário? Pesquisaremos isso na documentação do Django.

Escreveremos "forms Django" na busca do Google e clicaremos no primeiro link da própria documentação e nele veremos uma descrição detalhada de como trabalhar com os formulários no Django.

Scrollando um pouco mais a página haverá um ponto muito importante, o get e o post. É informado que no Django são utilizados apenas esses dois métodos.

O método post nós usaremos sempre que queremos recuperar informações enviadas pela requisição e processá-las para criar algum tipo de recurso, seja, no nosso caso, um usuário, seja uma nova receita, ou até mesmo um novo produto ou cliente.

Então, para recuperar ou processar informações que estão num formulário, usaremos o verbo post do http.

No caso do get, vamos utilizá-lo quando queremos obter um determinado dado de uma requisição.

Como na situação atual desejamos processar informações e criar um novo usuário, especificaremos que nosso formulário será do tipo post.

Em "cadastro.html", na linha 27, há um form action e um method="" em branco. Nesse ponto, especificaremos method="POST".

Uma outra ação necessária será fazer com que nosso formulário de cadastro converse com a função de cadastro em "views.py" de usuário. Ou seja, precisaremos alinhar as duas informações, dizendo que quem cuida das requisições do formulário é a função.

Para isso, escreveremos que a url para a ação do form action será nossa função de cadastro, com form action="{$ url 'cadastro' %}".

Dessa forma, conseguiremos especificar que trabalharemos com as informações para a criação de um novo recurso por meio do método POST e quem cuidará das requisições será o cadastro.

Para verificar se realmente receberemos o método POST na requisição criaremos uma checagem simples no "views.py", verificando que se o request.method for == ´´POST, ocorrerá alguma ação, por exemplo, imprimir uma mensagem.

Criaremos um print 'Usuário criado com sucesso' se o método for POST. Então, assim que clicarmos em "Criar sua conta", se isso for verdadeiro, a mensagem será exibida no nosso terminal.

Para redirecionar ainda para nossa página de login, faremos um `return redirect ('login').

    def cadastro(request):
        if request.method == 'POST':
            print('Usuário criado com sucesso')
            return redirect('login')
        return render(request, 'usuarios/cadastro.html')

Vamos salvar e receberemos uma notificação relacionada à palavra redirect, pois ainda não teremos esse módulo importado, apenas o render. Para importar, bastará escrever redirect após render e uma vírgula, nos imports, e o grifo vermelho desaparecerá.

Se o método não for o POST, vamos renderizar mais uma vez a página de cadastro.

    from django.shortcuts import render, redirect

    def cadastro(request):
        if request.method == 'POST':
            print('Usuário criado com sucesso')
            return redirect('login')
        else:
        return render(request, 'usuarios/cadastro.html')

Salvaremos as modificações no terminal, assim como em "cadastro.html" e voltaremos à aplicação, na página de cadastro. Colocaremos "Gui Lima" como nome, e o e-mail "guilima@alura.com", com a senha 123, o mesmo para a confirmação.

Quando clicarmos em "Criar sua conta", veremos uma página dizendo que isso foi Proibido, e a verificação CRSF falhou. O que isso significa? Aprenderemos no próximo vídeo.

### CSRF, token e dados

Assim que clicamos em "Criar sua conta" recebemos a página do Erro 403, Proibido. Lemos ainda "Verificação CSRF falhou. Pedido cancelado".

Há também um Help, informando que a falha foi que o CSRF token foi perdido ou está incorreto. Mas o que significa CSRF?

Pesquisaremos no Google e veremos que o cross-site request forgery, em Português, significará "falsificação de solicitação entre sites", também conhecido como "ataque de um clique". Ou seja, o Django fornecerá um tipo de proteção contra esse tipo de ataque.

Para não cair nesse erro e enviar o token, pesquisaremos novamente na documentação do Django, buscando no Google por "csrf django". O site da documentação terá uma descrição bem completa do que o erro se trata e como o Django funciona quanto ao ataque de site cruzado.

É falado no tópico sobre o modo de utilizar a proteção que ela é um middleware, que utilizamos por meio de uma template tag dentro do nosso form.

Então, teremos nosso form no método post, e inseriremos csrf_token na nossa aplicação para enviar o token necessário.

Portanto, em "cadastro.html", onde teremos o form, pularemos uma linha após o método POST e colocaremos o token com {% csrf_token %}, enviando-o conforme está descrito na documentação.

Salvaremos o código e voltaremos à aplicação. Atualizaremos a página e digitaremos o e-mail e a senha para a criação da conta. Assim que clicarmos no botão para criar, desta vez, vamos para a página de login.

Voltando ao código, no "views.py", na função de cadastro. estamos verificando. Se o método for POST, imprimiremos que o usuário foi criado com sucesso( o que ainda será apenas uma mensagem para o teste) e redirecionaremos para a página de login.

Por isso, aparentemente o método foi POST em nossa tentativa, pois fomos para a página esperada. Conferiremos o terminal, e de fato haverá a mensagem "Usuário criado com sucesso". Assim, conseguimos buscar as informações que estão no nosso formulário.

Mas como visualizaremos o token? Se formos até a página e clicarmos com o botão direito do mouse e selecionarmos a opção "Inspect" ou "Inspecionar", aparecerá a aba com o código na lateral direita da tela.

Clicaremos no ícone da seta nessa seção, e veremos que no nosso formulário haverá o token e o valor que passará para cada requisição. Se atualizarmos a página e conferirmos de novo, esse value já será diferente. Essa será uma forma de proteção dos ataques.

Então, incluímos as template tags necessárias para trabalhar com o formulário, mas a intenção ainda será a de que quando preenchermos e-mail e senha e clicarmos para criar uma conta, conseguiremos de fato visualizar essas informações de usuário, enviados para "views.py".

Faremos isso de forma muito parecida com o request.method == 'POST'. No nosso formulário de cadastro, teremos uma label de nome, bem como um input que tem um name="nome". Por meio desse name conseguiremos recuperar as informações que desejamos.

Então, em "views.py" buscaremos as informações e vamos atribuí-las a uma variável chamada nome. Verificaremos a request.POST e digitaremos 'nome' entre chaves. No print exibiremos a variável nome para conferência.

    def cadastro(request):
        if request.method == 'POST':
            nome = request.POST['nome']
                    print(nome)
            return redirect('login')
        else:
            return render(request,'usuarios/cadastro.html')
        return render(request,'usuarios/cadastro.html')

Voltaremos ao cadastro e novamente digitaremos o nome "Gui Lima", e-mail "gui@alura.com" e a senha e confirmação "123". Clicaremos em "Criar sua conta" e teremos acesso ao login.

Voltaremos ao projeto com "Command + J" e veremos o nome "Gui Lima", ou seja, conseguimos obter essa informação. Sendo assim, vamos solicitar as outras informações do usuário,email, senha e senha2.

Verificaremos "cadastro.html" e veremos que na senha, o nome está diferente, pois name="password". Assim, não conseguiríamos buscá-la, pois o nome deverá ser o mesmo. Por isso. em "views,py", dentro da chave, escreveremos password.

Quanto a Confirmação de senha, no html do cadastro o nome será password2, o mesmo que usaremos dentro das chaves em nosso código também.

Exibiremos todos os valores (nome, email, senha, senha2) por meio do print, e salvaremos.

    def cadastro(request):
        if request.method == 'POST':
            nome = request.POST['nome']
                    email = request.POST['email']
            senha = request.POST['password']
            senha2 = request.POST['password2']
                    print(nome, email, senha, senha2)
            return redirect('login')
        else:
            return render(request,'usuarios/cadastro.html')
        return render(request,'usuarios/cadastro.html')

Atualizaremos a página da nossa aplicação e nos cadastraremos no formulário mais uma vez, sendo direcionados para a página do login. Abriremos o terminal e veremos todas as informações fornecidas: "Gui Lima", o nome; "gui@alura.com", e-mail; "123 123", e referentes à senha e à confirmação.

Recuperamos todos os valores do nosso formulário. A seguir criaremos algumas validações simples para de fato termos o usuário na nossa base de dados.

### Criando usuários

Agora que conseguimos recuperar os valores da nossa requisição, criaremos de fato nosso novo usuário.

Fecharemos o terminal e faremos algumas validações simples. No nosso "cadastro.html" temos para cada campo input um required, ou seja, se clicarmos no botão para criar a conta sem preencher nenhum campo, será requerido o preenchimento com a mensagem em Inglês "Please fill out this field", ou "Preencha este campo" em Português, dependendo do sistema operacional.

O mesmo acontecerá se preenchermos apenas um ou mais campos, mas deixarmos algum ou alguns deles vazios. Preencheremos todos, nome, e-mal, senha e confirmação de senha, clicaremos no botão para criar a conta e seremos direcionados para a página de login.

Entretanto, isso não será suficiente para nossa validação. Vamos digitar 3 espaços no campo de nome e clicar no botão da página, e o que acontecerá? O campo não será considerado como nulo, pois a mensagem solicitando o preenchimento aparecerá apenas relacionada ao campo seguinte, de e-mail.

Por isso, precisaremos validar esses campos no nosso back-end, pois apenas o required não será o suficiente. Vamos ao "views.py" do app de usuários e escreveremos a verificação.

Vamos começar pelo nome. Se ele for nulo, colocaremos um strip() e printaremos no terminal a mensagem 'O campo nome não pode ficar em branco'. E assim que tivermos uma mensagem de erro, redirecionaremos o usuário para o cadastro, com o return.

    def cadastro(request):
        if request.method == 'POST':
            nome = request.POST['nome']
                    email = request.POST['email']
            senha = request.POST['password']
            senha2 = request.POST['password2']
                    if not nome.strip():
                        print('O campo nome não pode ficar em branco')`
                        return redirect('cadastro')
                    print(nome, email, senha, senha2)
            return redirect('login')
        else:
            return render(request,'usuarios/cadastro.html')
        return render(request,'usuarios/cadastro.html')

Atualizaremos nosso formulário e vamos colocar 3 espaços no lugar do campo de nome, um e-mail e uma senha, e tentaremos criar a conta. Clicaremos no botão, mas continuaremos na página de criação de conta. Vamos ao nosso terminal, e agora veremos a mensagem de que o campo de nome não poderá ficar em branco.

Faremos o mesmo para o campo de e-mail, e poderemos copiar e colar o trecho de código referente ao nome para alterá-lo de acordo com o necessário. Mais para a frente no curso, vamos refatorar o código para torná-lo melhor.

Então, faremos a validação if not email.strip() e imprimiremos que o campo não poderá ficar em branco no terminal.

Também teremos que verificar o preenchimento da senha e da confirmação de senha, mas nesse caso, faremos diferente. Será mais interessante checarmos se a primeira senha será igual a segunda.

A verificação será simples, se as senhas não forem iguais if senha != senha2 vamos imprimir 'As senhas não são iguais' e vamos redirecionar para a página de cadastro.

Outra validação importante será nos certificar de que o usuário tentando realizar o cadastro já está na nossa base de dados. Caso ele já esteja, não permitiremos o cadastro, pois ele já existe.

Importaremos User do Django por meio de um modelo chamado auth.models, com from django.contrib.auth.models import User. Dessa forma, o modelo de usuários será trazido para o nosso arquivo, e conseguiremos criar o código para a verificação.

Escreveremos if User.objets.filter() e passaremos os filtros do objeto. Conferindo a tabela de usuários, nela teremos geralmente um ID, uma senha, a última vez que foi feito o login, se é um superusuário, primeiro e último nome, e-mail e mais alguns campos.

Queremos que as pessoas façam o login na aplicação pelo e-mail, então perguntaremos se o e-mail já existe, com (email-email).exists().

Caso o usuário já exista, printaremos na tela o erro 'Usuário ja´cadastrado', e redirecionaremos para a página de cadastro também.

Se o usuário não existir, vamos de fato permitir gerar o cadastro, então atribuiremos esses valores ao user com user = User.objects.create_user(). Dentro dos parâmetros, passaremos username=nome, email=email, password=senha. É importante destacar que a senha está com o nome em Inglês no auth_user, apesar de termos chamado nosso campo de senha.

Assim, criamos um objeto do nosso usuário com os devidos campos. Agora, salvaremos esse usuário na nossa base de dados com a função user.save(), e poderemos ainda printar que o usuário foi cadastrado com sucesso, por fim.

    def cadastro(request):
        if request.method == 'POST':
            nome = request.POST['nome']
            email = request.POST['email']
            senha = request.POST['password']
            senha2 = request.POST['password2']
            if not nome.strip():
                print('O campo nome não pode ficar em branco')
                return redirect('cadastro')
            if not email.strip():
                print('O campo email não pode ficar em branco')
                return redirect('cadastro')
            if senha != senha2:
                print('As senhas não são iguais')
                return redirect('cadastro')
            if User.objects.filter(email=email).exists():
                print('Usuário já cadastrado')
                return redirect('cadastro')
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            print('Usuário cadastrado com sucesso')
            return redirect('login')
        else:
            return render(request,'usuarios/cadastro.html')

Incluímos as validações, portanto, vamos ao site conferir os principais erros. Já verificamos o nome, então escreveremos "Gui Lima". Quanto ao e-mail, deixaremos apenas com espaços, e preencheremos normalmente a senha e a confirmação.

Clicaremos no botão e o cadastro não será criado, pois de acordo com a nossa alteração no código, se o e-mail não for preenchido, seremos redirecionados à tela de cadastro.

Voltaremos à aplicação e preencheremos nome e e-mail corretamente, porém dessa vez deixaremos as senhas diferentes, "123" na senha e "1234" na confirmação. Clicaremos em "Criar sua conta" e voltaremos para a página de criação.

Voltando ao código, se olharmos o terminal veremos o aviso de que as senhas não são iguais.

Atualizaremos nosso auth_user e clicaremos sobre ele com o botão direito, selecionando em seguida "View/Edit Data > All Rows" para visualizar todas as linhas. Ainda não teremos o novo usuário.

Vamos à aplicação novamente e criaremos um usuário com os dados todos sem problemas. Clicaremos em "Criar sua conta" e vamos para a tela de login.

No terminal, aparecerá a mensagem "Usuário cadastrado com sucesso", e olhando nossa base de dados, quando visualizarmos todas as linhas veremos o usuário "Gui Lima" cadastrado agora.

Assim, estamos reutilizando uma tabela do Django. No banco de dados não haverá o primeiro nem o segundo nome, pois priorizaremos o username e o e-mail.

Conseguimos cadastrar uma nova conta tendo colocado validações simples, e já somos redirecionados para a tela de login. Na sequência vamos trabalhar na realização desse login de usuário.

Mas antes, vamos tentar cadastrar o usuário com os mesmos dados mais uma vez, ou seja, preenchendo os campos de forma idêntica a que fizemos anteriormente. Clicaremos no botão e continuaremos na página de cadastro.

No terminal, aparecerá a mensagem de que o usuário já está cadastrado conforme o esperado. Então, as principais validações para a criação do usuário na nossa aplicação já estão prontas. Caso elas passem, será criado um objeto e o novo usuário será salvo na nossa base de dados.

### Exercício: Token CSRF

O middleware CSRF e a template tag `{% csrf_token %}` fornecem proteção fácil de usar contra falsificações de solicitação entre sites.

Esse token fica salvo na sessão do usuário no servidor e, quando o formulário é postado, o token enviado pelo formulário é comparado com o que se tem na sessão, lá no servidor. Sendo iguais, a requisição é aceita. Caso contrário, é recusada.

Sabendo disso, é correto afirmar que:

a) Alternativa correta: Este middleware é ativado por default no Django.
- _Certo! Por padrão, o middleware CSRF já vem ativado na configuração de MIDDLEWARE._

b) Alternativa correta: Em qualquer formulário que utilize uma requisição POST, usamos a template tag dentro do formulário.
- _Certo! Incluímos a template tag dentro do formulário, por exemplo:_
    form method="post">{% csrf_token %}

c) Este middleware não funciona com requisições POST.

## 03. Autenticação de usuários
### Login e dashboard

Criamos uma nova conta. Agora queremos efetuar o login com a conta criada.

Para isso, temos o e-mail e a senha no nosso formulário de login, e precisamos buscar essas informações na requisição. Já sabemos como fazer isso.

No formulário de login, há uma ação na linha 27. Nossa função de login deverá ser vinculada à ação, por isso, dentro das aspas de form action="" colocaremos o código Python entre chaves e símbolos de porcentagem, além de url e quem deverá cuidar do nosso formulário, 'login', ou seja `{% url 'login' % }`.

Também utilizaremos o método POST e pensando na segurança, passaremos o token de segurança `{% csrf_token % }`.

Em "views.py" faremos um procedimento muito parecido com o que fizemos no cadastro, verificaremos se o método é POST e por meio do `request.method.POST[]` traremos as informações necessárias.

Podemos copiar o código usado no cadastro para o login e fazer as alterações necessárias. Se a requisição for POST deveremos trazer o email e a senha, e para ter certeza do que passaremos para o `request.method.POST[]`, vamos visualizar o que diz o name no input. Nesse caso, teremos mesmo as palavras email e senha.

Sabendo disso, para testar se os valores virão corretamente, printaremos o email e a senha, e se isso for verdade, precisaremos ainda redirecionar o usuário para outra página após fazer o login. Vamos fazer o return redirect() e ele irá para uma página 'dashboard'.

Para conseguirmos renderizar a página, precisaremos atribuir na função dashboard. Mas ainda não temos essa página, de acordo com o nosso template de usuários, apenas o login e o cadastro. Então, vamos criá-la.

Clicaremos na pasta de usuários e clicaremos no ícone para gerar um novo arquivo, que nomearemos como "dashboard.html". Para testar, escreveremos `<h1>Dashboard</h1>`.

Em "views,py", quando recermos uma requisição para dashboard, retornaremos uma renderização, devolvendo a requisição request e pedindo para que ela seja renderizada da pasta 'usuarios/dashboard.html'.

Portanto, não estaremos efetuando o login, mas verificando se o e-mail e a senha virão corretamente e direcionando para a página de dashboard. Na função de dashboard, pedimos para que a página seja renderizada.

    def login(request):
        if request.method == 'POST':
            email = request.POST['email']
            senha = request.POST['senha']
            print(email, senha)
                    return redirect('dashboard')
        return render(request, 'usuarios/login.html')

    def logout(request):
            pass

    def dashboard(request):
        return render(request, 'usuarios/dashboard.html')

Vamos salvar, voltar à nossa aplicação e atualizar. Digitaremos "gui@alura.com" no campo do e-mail, para testar, e no campo da senha, "123". Quando clicarmos no botão "Acessar sua conta", vamos para a página de dashboard.

Voltaremos ao código e pressionaremos o atalho "Command + J" ou "Ctrl + J" para visualizar o terminal, onde estarão impressos o e-mail e a senha inseridos pelo usuário.

Lembrando que os valores que buscamos estarão sensíveis, pois se acessarmos a página e atualizarmos sem preencher nenhum campo, se clicarmos em "Acessar sua conta", vamos para a página de dashboard do mesmo jeito, e nada será impresso no nosso terminal.

Então, precisaremos garantir que o e-mail e a senha não ficarão em branco, o que faremos de forma muito simples. No login, assim que trazemos os valores, verificaremos, Se o campo email == ""ou seja, se for igual a uma string vazia, ou o mesmo para a senha, informaremos que os campos não deverão ficar em branco com um print.

Assim que houver o erro, precisaremos redirecionar o usuário para algum lugar, e será mais uma vez para a página de login, por meio do return redirect('login'). Caso contrário, os campos não estejam em branco, serão impressos e-mail e senha e o direcionamento será para a página de dashboard.

    def login(request):
        if request.method == 'POST':
            email = request.POST['email']
            senha = request.POST['senha']
            if email == "" or senha == "":
                print('Os campos email e senha não podem ficar em branco')
                return redirect('login')
            print(email, senha)
                    return redirect('dashboard')
        return render(request, 'usuarios/login.html')

    def logout(request):
            pass

    def dashboard(request):
        return render(request, 'usuarios/dashboard.html')

Voltaremos para a página e atualizaremos. Colocaremos o mesmo e-mail e senha de antes. Clicaremos no botão para acessar a conta e seremos direcionados para a página de dashboard conforme o esperado. Olharemos o terminal e os valores estarão impressos lá.

Agora deixaremos os campos sem preenchimento e clicaremos no botão para o acesso. Vamos permanecer na página de login e o terminal mostrará a mensagem de que os campos não podem ficar em branco. Portanto, conseguimos fazer a validação de que esses valores serão trazidos para nós.

Mas ainda precisaremos executar esse e-mail no banco de dados, ou seja, dizer que esse usuário com esse e-mail está tentando acessar a conta. Uma informação interessante é a de que, por segurança, o Django não nos deixará visualizar a senha dele.

Assim, como saberemos se o e-mail e a senha, toda encriptada conferem? E se conferirem, encaminharemos o usuário para uma tela de dashboard com as informações dele. Veremos isso a seguir.

### Realizando o Login

Quando digitamos os valores nos campos de e-mail e senha na nossa tela de login, acessamos a tela de dashboard e conseguimos visualizar esses valores no terminal.

Agora, queremos autenticar, ou seja, confirmar se essas informações condizem com as que temos na base de dados, e assim, permitir ou não o login dessa pessoa.

Pesquisaremos como utilizar a autenticação no Django na busca do Google por "auth django". Clicaremos no primeiro link, "User authentication in Django", ou "autenticando usuários no Django".

A descrição no site dirá que o sistema de autenticação consistirá em usuários, permissões, grupos, exatamente o que precisamos. Haverá um detalhamento de que o django.contrib.auth é um modelo que podemos utilizar para realizar nosso login.

Clicaremos para importar esse módulo, e voltaremos a nossa aplicação. Na parte dos imports do código do "views.py", escreveremos `from django.contrib import auth`, e salvaremos.

Assim, instalamos o módulo de login na aplicação e veremos quais outros itens poderemos utilizar. Ainda na documentação do Django, teremos uma página extensa sobre como usar o sistema de autenticação, falando, dentre outras coisas, sobre o User objets, campos ou atributos que já temos para nosso usuário, como username, password, email, first_name, last_name.

Todos esses campos poderão ser vistos no auth_user, ou seja, já temos todas essas informações na nossa base de dados e nosso usuário já está preparado.

Veremos na página, ainda, como criar usuários, alterar senhas e fazer a autenticação desses usuários. Algo interessante será que para fazer a autenticação usando o django.contrin.auth, de acordo com o site, devemos atribuir um authenticate ao user passando o username e password.

Porém, teremos um problema. Scrollando um pouco mais a tela, haverá o tópico sobre autenticação em Web requests com atributos muito semelhantes, username e password. Voltando à aplicação, no entanto, estamos utilizando o campo de e-mail.

Então, precisaremos dizer que temos o e-mail do usuário, mas a informação importante para logar no sistema do Django será o username, tanto que se digitarmos "localhost 8000/admin" no campo de busca do navegador, a informação pedida será a de usuário.

O sistema de login do Django, portanto, utiliza o username, mas queremos logar por meio do e-mail. De alguma forma precisaremos, em primeiro lugar, que haja uma conferência se o e-mail existe.

No código, perguntaremos se o e-mal do usuário existe de forma similar a que fizemos no cadastro, e inclusive copiaremos o código de lá. Então, se esse e-mail existir, queremos de alguma forma trazer o username correspondente.

Para isso, pegaremos o nome e atribuiremos User.objects.filter(email=email).values_list('username'). Assim, traremos o valor do nome por meio da propriedade values_list() e passaremos o 'username'.

Sendo assim, com o objeto, vamos filtrar pelo e-mail que existe, e com base nas informações do objeto, traremos o username, mas queremos apenas o nome desse usuário. Por isso, passaremos como segundo parâmetro a propriedade flat=True, e pegaremos apenas esse valor.

Para ter certeza de que ocorrerá tudo como o esperado, vamos printar o nome .

    def login(request):
        if request.method == 'POST':
            email = request.POST['email']
            senha = request.POST['senha']
            if email == "" or senha == "":
                print('Os campos email e senha não podem ficar em branco')
                return redirect('login')
            print(email, senha)
            if User.objects.filter(email=email).exists():
                nome = User.objects.filter(email=email).values_list('username', flat=True).get()
                            print(nome
            return redirect('dashboard')
        return render(request, 'usuarios/login.html')

Na aplicação, digitaremos o e-mail e a senha, clicaremos no botão de login e seremos direcionados para a página de dashboard. Abriremos o terminal e veremos que foi impresso o username "Gui Lima".

Em nossa base de dados, conseguimos atestar que o nome do username é "Gui Lima". Então, por meio desse código, por maior do que ele esteja (e vamos refatorá-lo no final), trouxemos o username.

Agora usaremos o padrão de autenticação que o Django oferece. Voltaremos à documentação e veremos que criaremos um usuário utilizando a função authenticate(), e como já importamos o auth, atribuiremos auth.authenticate() ao user.

Nos parâmetros dessa função haverá o request, o username que será igual ao nome trazido, e o password, senha, que teremos mais acima no código.

Perguntaremos, assim como mostra a documentação, se o user is not none, para nesse caso realizar o login. Ele será feito por meio da propriedade auth.login(), devolvendo a requisição e o user. Imprimiremos que o login foi realizado com sucesso e redirecionaremos a pessoa para a página de sucesso.

    def login(request):
        if request.method == 'POST':
            email = request.POST['email']
            senha = request.POST['senha']
            if email == "" or senha == "":
                print('Os campos email e senha não podem ficar em branco')
                return redirect('login')
            print(email, senha)
            if User.objects.filter(email=email).exists():
                nome = User.objects.filter(email=email).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=nome, password=senha)
                if user is not None:
                    auth.login(request, user)
                    print('Login realizado com sucesso')
                    return redirect('dashboard')
        return render(request, 'usuarios/login.html')

Atualizaremos a página da aplicação e novamente digitaremos e-mail e conta e iremos para a página de dashboard. Será que estamos logados? Voltaremos ao código, pressionaremos "Command + J", e o terminal nos mostrará a mensagem "Login realizado com sucesso", bem como os valores de e-mail e senha.

Para ter certeza se conseguimos realizar de fato o login, o que podemos fazer é colocar o nome do usuário na nossa página de dashboard. Então, vamos ao html da página e em vez de escrever apenas o título "Dashboard", escreveremos `<h1>Dashboard, olá, {{ user.username }} </h1>`. Então, teremos um código Python com duas chaves para gerar o nome.

Voltaremos à aplicação, atualizaremos a página e agora veremos "Dashboard, olá, Gui Lima" na dashboard, o que significará que estamos logados.

Entretanto, todo o nosso site estará bonito e funcional, mas quando fazemos o login, vamos para essa página em branco escrito "Dashboard, olá, Gui Lima". Queremos continuar com os mesmos layouts que já temos. É o que faremos a seguir.

### Menu, logout e dashboard

Assim que realizamos o login vemos uma página em que está escrito "Dashboard, olá, Gui Lima". Queremos manter os templates que já temos na nossa aplicação.

Então, podemos fazer com que na página de dashboard o usuário consiga visualizar as receitas que ele mesmo cria. Mais para a frente trabalharemos no formulário das receitas do usuário, mas a intenção é que a visão, ao realizar o login, seja semelhante com a que temos na página index.

Vamos à página index e copiaremos todo o html. Na sequência, vamos ao código da dashboard, deletaremos o título que tínhamos colocado e colaremos. Salvaremos, e se voltarmos na aplicação e realizarmos o login, acessaremos uma página em que nada será exibido.

Não era nosso objetivo. Quando realizarmos o login queremos mostrar o template da página, mas devemos mostrar um "Olá" e o nome do username.

Para ganhar tempo no html haverá um trecho de código disponibilizado em que importamos algumas classes, criamos um container e exibimos o Olá (( user.username}}. Colaremos o código no html da dashboard, antes da exibição da lista de receitas.

Se voltarmos e atualizarmos a página, veremos escrito "Olá Gui Lima" dessa vez, o que fará mais sentido, pois o usuário verá que está logado.

Só que ainda aparecerão os links de cadastro e login, e depois que já logamos, não interessará mais vê-los, e sim um link para criar as receitas, por exemplo.

Vamos em "partials > _menu.html" no nosso projeto e haverá três links, o da index, do cadastro e do login. São links úteis caso não estejamos logados, mas precisaremos de uma forma de verificar se o usuário esta logado ou não.

Para saber se uma pessoa está logada, usaremos o código Python com chaves e símbolos de porcentagem e verificaremos se o user está logado com user.is_authenticated. Se sim, queremos visualizar alguns links. Caso contrário, else, os links serão outros.

Outra coisa que faremos para deixar mais claro será fechar nossa verificação com {% endif %}. Então, se estamos logados, um link interessante será o da index, mas também visualizaremos outros links.

Por exemplo, queremos um link que vá direto para a dashboard, então escreveremos 'dashboard' na url, da mesma forma que temos cadastrado. O nome deste link será "Minhas receitas".

Outro link que criaremos será o de logout, pois se realizamos o login, devemos ter a opção de deslogar. O nome da url será escrito em minúsculas e o título do link com a primeira letra maiúscula.

    <ul>
        {% if user.is_authenticated %}
            <li><a href="{% url 'index' %}">Página principal</a></li>
        <li><a href="{% url 'dashboard' %}">Minhas receitas</a></li>
        <li><a href="{% url 'logout' %}">Logout</a></li>
        {% else %}
        <li><a href="{% url 'index' %}">Página principal</a></li>
        <li><a href="{% url 'cadastro' %}">Cadastro</a></li>
        <li><a href="{% url 'login' %}">Login</a></li>
    {% endif %}
    </ul>

Vamos salvar, e ir para "views.py", onde nosso método de logout não realiza nenhuma função ainda. Para o usuário conseguir se deslogar, utilizaremos o método auth.logout(), quando escrevermos auth. o próprio editor de texto sugerirá o logout.

Passaremos a requisição, único parâmetro esperado, e retornaremos um redirect para nossa página 'index'.

    def logout(request):
        auth.logout(request)
        return redirect('index')

Assim, criamos alguns links. Caso o usuário esteja logado, visualizará uns, caso não esteja logado, visualizará outros. Também possibilitamos o logout.

Atualizaremos a página estando logados, e veremos os links Página Principal, Minhas Receitas e Logout. Sempre que clicarmos em Minhas Receitas, veremos somente as receitas do próprio usuário.

Clicando na Página Principal, veremos todas as receitas da aplicação, que estarão com a flag de publicadas. Clicando no Logout, vamos nos deslogar e ser direcionados para a Página Principal.

Vamos logar mais uma vez e observar que quando acessamos a conta, teremos uma url "localhost 8000/usuarios/dashboard". Realizaremos o logout, e acessaremos mais uma vez este mesmo link.

Apesar de não estarmos logados e de não ser exibida nenhuma receita, a página mostrará um "Olá", mas o objetivo é exibir essa página de dashboard somente se a pessoa estiver logada. Caso alguém utilize o link para a dashboard sem estar logado, deverá aparecer somente nossa página de index.

Em "views.py" nós estamos sempre renderizando a página de dashboard. Caso o usuário não esteja logado (else), vamos redirecioná-lo para a página 'index'.

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')COPIAR CÓDIGO
Copiaremos o link da dashboard para garantir. Abriremos a página principal sem logar, observando que aparecerão o Cadastro e o Login. Quando tentarmos acessar o link, seremos redirecionados para a Página Principal.

Agora realizaremos o login e acessaremos a conta. A partir do momento que estivermos logados, veremos a página da dashboard com a mensagem "Oi Gui Lima" e os links para a Página Principal, Minhas Receitas e o Logout.

Vamos nos deslogar mais uma vez e novamente veremos os links de Cadastro e Login na index.

Portanto, sempre que fizermos o login visualizaremos links diferentes e conseguiremos verificar na requisição se o usuário está logado ou não.

A seguir, criaremos mais um link no menu para haver um formulário de criação de receitas, e na página Minhas Receitas serão exibidas apenas as receitas da pessoa que estiver logada.

### Menu dinâmico

Geralmente, após realizarmos o login em alguma aplicação, a exibição do menu de navegação é alterada. Por exemplo, alguns links de navegação ficam disponíveis e visíveis.

Sabendo disso, podemos afirmar que:

a) Não é possível saber se o usuário da requisição está logado.

b) Alternativa correta: É possível verificar em um template se o usuário está logado com o código {% if user.is_authenticated %}.
- _Certo! Com esse código, verificamos se o usuário está logado, criando uma sequência de if e {% else %}, exibindo os links do menu que desejamos._

c) Não podemos criar este comportamento no Django, já que só podemos realizar o login no admin.S

## 04. Formulário de receita
### Criando formulário de receita

Na nossa aplicação, assim que realizamos o login, temos a Página Principal mostrando todas as receitas; Minhas Receitas, que ainda não mostrará nenhuma receita, já que ainda não fizemos a criação; e o Logout.

Para criar as receitas, ainda não temos um caminho. Incluiremos um link "Criar receita" em Minhas Receitas, e assim vamos para um formulário que, conforme preenchido, criará minhas receitas, que aparecerão nessa página, de forma separada das receitas do site.

Para começar, vamos a "usuarios > urls.py", onde temos cadastro, login, url e logout. Criaremos um novo path e escreveremos 'cria/receita'. Quem cuidará dessa requisição será uma função em views chamada cria_receita. Também colocaremos um name='cria_receita'.

    urlpatterns = [
        path('cadastro', views.cadastro, name='cadastro'),
        path('login', views.login, name='login'),
        path('dashboard', views.dashboard, name='dashboard'),
        path('logout', views.logout, name='logout'),
        path('cria/receita', views.cria_receita, name='cria_receita')
    ]

Quando salvarmos, receberemos a notificação de que não há cria_receita em "views.py". Então vamos para esse arquivo e criaremos uma nova função cria_receita() e passaremos como parâmetro a requisição.

Vamos renderizar uma página como retorno, devolvendo a requisição. A página estará em 'usuarios/' e agora precisaremos de uma página .html para isso.

Criaremos essa página em "templates > usuarios". Vamos gerar um novo arquivo clicando no ícone de "New file", e o chamaremos de "cria_receita.html". Escreveremos como título <h1>Crie sua receita</h1>.

Voltaremos para "urls.py" e salvaremos o código. Na sequência, vamos em "views.py" e salvaremos também. Novamente, vamos para "urls.py" e salvaremos, e aquele erro quanto a views.cria_receita desaparecerá.

Assim, criamos um path novo. Mais uma vez abriremos "views.py" e vamos renderizar a página cria_receita.html que criamos, apenas com o título. Depois, veremos como torná-la mais interessante.

    def cria_receita(request):
        return render(request, 'usuarios/cria_receita.html')

Voltando à aplicação, ainda não teremos um link para o formulário de criação de receitas. Então vamos criá-lo em "templates > partials > _menu.html".

Pressionaremos "Ctrl + C" para copiar a linha de código referente ao link para o logout que o usuário verá quando estiver autenticado, e colaremos abaixo com o "Ctrl + V".

Vamos deixar o link para o logout por último e alterar a linha abaixo do link para a dashboard. Na url, escreveremos 'cria_receita'. O título para deixar visível no link será Criar receita.

    <li><a href="{% url 'dashboard' %}">Minhas receitas</a></li>
    <li><a href="{% url 'cria_receita' %}">Criar receita</a></li>
    <li><a href="{% url 'logout' %}">Logout</a></li>

Voltando na aplicação e salvando, teremos um link a mais. Clicaremos no link "Criar receita" e veremos a mensagem "Crie sua receita" que colocamos na página html.

Será que teremos que gerar o formulário do zero, pensar no html, CSS, bootstrap e Javascript para tornar nossa página interessante? Nas atividades da aula já estará disponível um trecho do código html que usaremos para o formulário.

Portanto, vamos copiar todo esse trecho, removeremos o título anterior, colaremos o código e salvaremos o novo html. Entenderemos um pouco como ele foi criado.

Assim como nas outras páginas, extendemos do 'base.html', carregamos dos estáticos, incluímos partials de busca e de _menu.html. Há uma mensagem dizendo "Crie sua receita,", com o nome do usuário na sequência.

Temos uma mensagem informando que o preenchimento de todos os campos é obrigatório e um form action chamado 'cria_receita'. Nele há um método POST sendo utilizado, e também passamos um token de segurança.

Além de tudo, há o Título da receita, Ingredientes, Modo de preparo, Tempo de preparo, Rendimento e Categoria, além da Foto. Os campos foram criados com base no nosso modelo de receitas. Se formos em "receitas > models.py", o modelo terá uma Pessoa criada ao fim do nosso segundo treinamento.

Esse modelo é vinculado com o app que criamos para manter Pessoas. Nesse caso, vamos fazer uma alteração, pois cada receita deverá ser vinculado com um Usuário.

Faremos isso adiante, mas para visualizar como ficou a criação do formulário, voltaremos à aplicação e atualizaremos a página. Já teremos um formulário bem desenvolvido.

Na página estará escrito "Cria sua receita, Gui Lima", nome do usuário com o qual nos logamos, e todos os campos que já vimos que ela teria no html. Quando submetemos a criação da receita, nossa intenção é que ela seja exibida na página de dashboard do usuário.

Na sequência, buscaremos as informações para validar, colocar nesses campos ou inputs, e depois veremos como salvar uma receita vinculando-a não mais a uma Pessoa, mas sim a um Usuário.

### Dados da requisição

Nossa intenção agora é preencher os campos do formulário e de fato criar uma receita, vinculando-a com o usuário.

Porém, se acessarmos nosso app de receitas e formos em "models.py", observaremos que existe um relacionamento da receita com o nosso app de pessoas. Fizemos um import de pessoas.models e dissemos que toda Receita terá uma Pessoa como uma ForeignKey.

Queremos alterar nosso negócio para que toda receita passe a pertencer a um usuário. Então, vamos remover o import de pessoas e importaremos de django.contrin.auth.models o User, trazendo o modelo de usuários do Django para nossa utilização.

Depois vamos alterar. Toda Receita terá uma pessoa, mas o relacionamento não virá mais do app de Pessoa, ele virá do nosso User.

    from django.contrib.auth.models import User

    class Receita(models.Model):
        pessoa = models.ForeignKey(User, on_delete=models.CASCADE)

Vamos salvar e não teremos problemas. Mas essa alteração deverá refletir em nossa base de dados, pois quando visualizamos todas as linhas no app "receitas_receitas" da base, há um vínculo com "pessoa_id", o que não é o que desejamos.

Deverá haver um relacionamento de "pessoa_id" com o "auth_user", ou seja, queremos que apareça o ID dos usuários. Para a alteração do modelo aparecer na base de dados, abriremos mais uma aba do terminal.

Na primeira aba, rodaremos o servidor. Abrindo mais uma, a (venv) deverá estar ativada. Pediremos para o Python gerar as migrações para nós, por meio do comando python manage.py makemigrations.

Pressionaremos "Enter" e será gerada uma migração. Leremos no terminal que o campo "pessoa" foi alterado, conforme a nossa solicitação. Na sequência, vamos executar a migração na base de dados com python manage.py migrate.

As aplicações serão aplicadas, e veremos um "Ok". Agora, nossas receitas estarão diretamente vinculadas a um usuário e já poderemos preencher os campos e mandar as informações.

Já teremos algumas imagens baixadas do site pixabay.com para gerar as receitas com as imagens. É possível fazer o download de novas imagens para utilizar.

Como a preocupação não será se a receita estará correta, usaremos um texto "lorem ipsum" apenas para nossos testes, copiando e colando nos campos .

Pegaremos a imagem "torta.jpg" e chamaremos nossa receita de "Torta de morango". Para os ingredientes e o modo de preparar será usado o texto copiado. Usaremos o tempo de preparo "40", diremos que ela servirá 2 pessoas e entrará na categoria "doces".

Clicaremos no botão "Criar Sua Receita" e nada acontecerá, voltaremos para a página do formulário. Voltaremos para a página de trás para não perder os dados de preenchimento dos campos, mas vamos ao código.

No "views.py", traremos as informações. Já sabemos que elas vêm da requisição por meio do método POST. Se a requisição for POST, serão trazidas.

Poderíamos também criar validação para todos os campos, e já temos uma ideia de como fazer as validações. Entretanto, para ganhar tempo, deixaremos isso para a última aula, quando fizermos a refatoração e organizarmos melhor o código.

Então, a receita terá o nome, o título dela, que chamaremos de nome_receita. Precisaremos conferir o name de cada campo no html. No caso, será realmente nome_receita, e faremos nome_receita = request.POST´['nome_receita'].

O mesmo servirá para os demais campos. O próximo será ingrediantes, depois modo_preparo e na sequência tempo_preparo, rendimento e categoria e foto_receita. Os names no html serão correspondentes.

Em foto_receita haverá uma diferença. Os demais campos serão do tipo string, pois quando colocamos um form action no html, sempre haverá também um tipo de input.

A maioria dos campos será um text, mas a foto da receita será do tipo file. Para trazer um tipo file, não escreveremos request.POST[], mas sim request.FILES[], de "arquivos" em Português, para trazermos os arquivos.

Com base nesses valores, faremos um teste printando todas essas informações para conseguirmos visualizá-las no terminal, com print(nome_receita, ingredientes, modo_preparo, tempo_preparo, rendimento, categoria, foto_receita).

Após fazer a inclusão da receita, devemos redirecionar o usuário para algum lugar, então colocaremos um return redirect() para a página de dashboard, pois fará sentido criarmos a receita e depois podermos visualizá-la.

Caso isso não aconteça e ocorra um erro, faremos um procedimento parecido com o que fizemos em cadastro, redirecionando para a própria página em que o usuário estará.

Escreveremos um else e um return redirect() para encaminhar para o próprio formulário 'cria_receita'. Ou seja, caso o preenchimento dos campos e inclusão da receita não funcione, por não ser uma requisição no método POST, o retorno vai renderizar para a página de criação de receitas.

    def cria_receita(request):
        if request.method == 'POST':
            nome_receita = request.POST['nome_receita']
            ingredientes = request.POST['ingredientes']
            modo_preparo = request.POST['modo_preparo']
            tempo_preparo = request.POST['tempo_preparo']
            rendimento = request.POST['rendimento']
            categoria = request.POST['categoria']
            foto_receita = request.FILES['foto_receita']
                    print(nome_receita, ingredientes, modo_preparo, tempo_preparo, rendimento, categoria, foto_receita)
            return redirect('dashboard')
        else:
            return render(request, 'usuarios/cria_receita.html')

Vamos salvar e voltar para a aplicação. Criaremos a Torta de morango, e novamente colaremos o texto nos Ingredientes e no Modo de preparo, com o Tempo de preparo "40", rendimento para duas pessoas e categoria "doce". Escolheremos a foto da torta e clicaremos em "Open".

Clicaremos no botão para criar a receita e seremos direcionados para a página de dashboard. Provavelmente funcionou tudo corretamente. Olharemos nosso terminal e veremos que na primeira aba recuperamos todos os valores relacionados aos campos, por isso há todo o texto lá.

Agora que trouxemos todos esses valores, precisaremos salvá-los na nossa base de dados. Será o que faremos a seguir.

### Receita de cada usuário

Para conseguirmos criar as receitas e elas ficarem registradas no nosso banco de dados, precisamos gerar um objeto para a receita, importando do modelo os atributos da classe Receita.

Em "views.py", importaremos de receitas.models o modelo de Receita. Feita a importação, faremos a criação dizendo que receita será uma Receita.objects.create(), e então passaremos as propriedades.

Observando nosso modelo, uma receita terá uma pessoa. Mas vamos nos deparar com um problema. Em nenhum dos outros campos teremos uma pessoa. Mas na requisição, haverá a pessoa que cria a receita.

Então, antes de gerar o objeto de criação da receita, encontraremos quem é o user que gera a receita. Importaremos o novo modelo do Python, from django.shortcuts, e utilizaremos o get_object_or_404, pois a intenção é obter um objeto.

No código, na linha acima da receita, escreveremos user = get_object_or_404() e passaremos algumas propriedades para ele. O primeiro será a classe User, e a segunda que precisaremos especificar será quem é o ID do objeto.

Podemos especificá-lo como pk=request.user.id. Dessa forma, trazemos o ID do usuário na requisição e atribuímos o ID para a variável user.

Voltaremos aos atributos de Receita.objects.create() e agora poderemos dizer que a pessoa criando a receita corresponde ao user, e assim conseguiremos fazer a associação.

Além do usuário, teremos os outros campos para passar. Além da pessoa que vai gerar a receita, teremos nome_receita que será igual a nome_receita, ingredientes = ingredientes, modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria e foto_receita=foto_receita.

Sendo assim, buscamos nosso user e criamos o objeto de receita. Agora o que teremos que fazer para de fato gravar a receita no banco de dados será um comando simples, receita.save(). Dessa forma a receita será registrada na base de dados também.

Para o código ficar mais claro, apagaremos nosso print, pois não precisamos mais dele, apenas buscar o usuário da receita e criar a receita em si, cuja linha de código ficou bem grande, mas depois pensaremos em como melhorar isso.

    def cria_receita(request):
        if request.method == 'POST':
            nome_receita = request.POST['nome_receita']
            ingredientes = request.POST['ingredientes']
            modo_preparo = request.POST['modo_preparo']
            tempo_preparo = request.POST['tempo_preparo']
            rendimento = request.POST['rendimento']
            categoria = request.POST['categoria']
            foto_receita = request.FILES['foto_receita']
            user = get_object_or_404(User, pk=request.user.id)
            receita = Receita.objects.create(pessoa=user,nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo,tempo_preparo=tempo_preparo, rendimento=rendimento,categoria=categoria, foto_receita=foto_receita)
            receita.save()
            return redirect('dashboard')
        else:
            return render(request, 'usuarios/cria_receita.html')

Salvaremos as informações e voltaremos a nossa aplicação. Vamos atualizar e tentar criar a "Torta de morango" novamente. Passaremos os ingredientes e o modo de preparar como o texto "lorem ipsum", definiremos o tempo de preparo de 40 min. e o rendimento para 2 pessoas, além da categoria "doce".

Escolheremos a foto "torta.jpg" e clicaremos no botão "Criar sua receita". Aparentemente ela terá sido criada, mas vamos conferir no nosso banco de dados.

No banco, teremos 4 registros de receitas. Clicaremos com o botão direito do mouse em "receitas_receita", optaremos por visualizar todas as receitas e aparecerão 5 registros, pois o banco será atualizado e a receita da Torta de morango aparecerá.

Então conseguimos armazenar a receita na nossa base de dados, mas ainda não podemos vê-la no site que estamos desenvolvendo. Nossa intenção é visualizá-la na nossa página de dashboard.

Voltaremos para "views.py" e na nossa função de dashboard(), atualmente só o que verificamos é que se o usuário tiver autenticado, vamos renderizar o dashboard. Caso contrário, vamos direcioná-lo sempre para a index.

Passaremos a exibir as receitas do usuário na dashboard caso o usuário esteja autenticado com receitas = Receita.objects.order_by(), trazendo todas as receitas. Passaremos '-date_receita' como atributo.

Queremos colocar primeiro as últimas receitas cadastradas, então adicionaremos um filtro que exibirá as receitas, que no entanto, devem ser exclusivamente do usuário criado. Então filtraremos a pessoa que tenha um id igual a determinado id.

Já sabemos como encontrar o id da pessoa que faz a requisição. Na linha acima de receitas, escreveremos id = request.user.id. Portanto, se o usuário estiver autenticado, vamos obter o id dele, que será atribuído a essa variável id.

Assim, o filtro será criado para mostrar apenas as receitas do usuário com esse id, com .filter(pessoa=id). Depois, precisaremos passar as informações para o nosso template. Atribuiremos, entre chaves 'receitas' : receitas'a dados, ou seja, tiparemos 'receitas' como do tipo receitas.

Quando retornarmos a requisição, devolvendo o request e a dashboard do usuário, passaremos dados.

    def dashboard(request):
        if request.user.is_authenticated:
            id = request.user.id
            receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)

            dados = { 
                'receitas' : receitas
            }
            return render(request, 'usuarios/dashboard.html', dados)
        else:
            return redirect('index')

Vamos salvar , voltar à aplicação e atualizar. Veremos agora a Torta de morango, criada pelo usuário Gui Lima. Conferiremos se essa receita será exibida na nossa Página Principal.

Conseguimos visualizá-la em Minhas Receitas, mas quando clicamos em Página Principal, ela não aparecerá. Isso significa que ela está visível para o usuário, mas não para toda a aplicação.

Criaremos mais uma receita para ter certeza. O título da receita será "Pão". Mais uma vez, usaremos o "lorem ipsum" para os ingredientes e para o modo de preparo. Colocaremos 60 min, no modo de preparo e o rendimento "serve 10 pessoas". A categoria será "salgado", e vamos abrir a foto do pão.

Clicaremos no botão para criar a receita e agora veremos o pão e a torta de morango na dashboard. Entretanto, na Página Principal, nenhuma das duas aparecerá.

Voltaremos para Minhas Receitas e clicaremos numa das receitas, como a Torta de morango, e nos certificaremos que conseguimos visualizar as informações referentes a ela. Funcionará da mesma forma para a receita do pão.

Se fizermos o logout, não teremos mais essas informações e veremos a Página Principal, o que não faz muito sentido. Por isso, vamos a "templates > partials > _menu.html", e tiraremos a página principal da opção de aparecer quando o usuário não estiver logado, deixando apenas o cadastro e o login.

Voltaremos à página, vamos atualizá-la, e agora o usuário que não estiver cadastrado conseguirá visualizar as receitas e até conferir informações clicando nelas, mas não verá mais o link da Página Principal.

Vamos fazer o login novamente como gui@alura.com, e quando acessarmos, conseguimos ver a Página Principal, Minhas Receitas, Criar Receitas e Logout.

### Cada receita com seu dono

Para exibir a receita de cada usuário, incluímos o seguinte código:

    id = request.user.id
    receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)

Sabendo disso, analise as seguintes informações e marque as verdadeiras:

a) Alternativa correta: Teríamos o mesmo resultado alterando essas duas linhas por receitas = Receita.objects.filter(pessoa=request.user.id).
- _Certo! O resultado seria o mesmo. Porém, da outra forma, apenas fragmentamos os passos, primeiro pegando o id do usuário da requisição, depois buscando a receita do usuário._

b) Não seria possível visualizar as receitas de cada usuário, alterando o código para:

    id = request.user.id
    todas_as_receitas = Receita.objects.order_by('-date_receita')
    receitas = todas_as_receitas.filter(pessoa=id)

c) Alternativa correta: Teríamos o mesmo resultado removendo o order_by, por exemplo: receitas = Receita.objects.filter(pessoa=id)
- _Certo! A ordenação não está alterando o resultado do filtro da ordenação. Sendo assim, teríamos o mesmo resultado._

## 05. Refatoração e mensagens
### Mensagens de sucesso e erro

Há um ponto que podemos melhorar na nossa aplicação.

Nesse momento, criaremos a conta da Ana. O nome será Ana, o e-mail será ana@alura.com, e na senha, digitaremos "123". Na confirmação de senha, porém, digitaremos "12". Clicaremos em "Criar sua conta" e continuaremos na página de criação da conta, e os campos serão limpos.

Entretanto, em nenhum momento foi exibida uma mensagem informando que as senhas não estavam iguais. Quando abrimos o terminal, vemos o print que deixamos em "usuarios > views.py" dizendo que as senhas não são iguais, gerado quando senha!= senha2.

Seria interessante podermos exibir a mensagem de erro na nossa aplicação, para o usuário conseguir identificar o problema. E caso ele conseguisse completar o cadastro e ser direcionado para a página de login, a mensagem poderia ser algo como "Seu cadastro foi realizado com sucesso".

Para descobrir como o Django trabalha com a exibição de mensagens assim, digitaremos "message django" na busca do nosso navegador. O primeiro link já será uma explicação de como funcionará esse sistema de mensagens.

O Django trará esse sistema para nossa utilização por padrão, com uma explicação bem detalhada dos níveis de mensagens e as message tags. Podemos indicar, por exemplo, que uma mensagem é de erro, e dentro da mensagem, criar nossas message tags.

Na nossa aplicação, também utilizamos o bootstrap, então conseguiremos utilizar tags do bootstrap para criar alertas. Buscaremos na internet por "bootstrap alertas" e no primeiro link teremos algumas formas de exibir as mensagens de erro e de sucesso.

A diferença entre as mensagens de erro ou sucesso será a classe delas. Na primeira, a classe utilizada será danger (perigo, em Inglês) e na segunda, success. Criaremos nossas próprias message tags para vinculá-las ao bootstrap e deixá-las com um visual interessante no momento da exibição.

Como faremos a criação, no entanto, se já temos o django.conrib.messages na nossa aplicação? Copiaremos o trecho de código responsável pela criação das tags e abriremos o "alurareceita > settings.py", onde estão as configurações.

Em MIDDLEWARE já teremos um messages, assim como em TEMPLATES há um messages.context_processors. Esses são recursos que podemos utilizar. Ao fim do código, colocaremos um comentário para identificar que essa é a parte de # Messages, e criaremos duas message tags.

Uma delas será para sucesso e outra para erro. Começaremos com messages.ERROR, e a tag que essa mensagem armazenará para nós será um nome que temos no bootstrap, 'danger'. A de sucesso será messages.SUCCESS: 'success'. Depois delas, colocaremos vírgulas, pois poderemos criar outras message tags, apesar de para nós, as duas serem suficientes.

#### Messages
    from django.contrib.messages import constants as messages
    MESSAGE_TAGS = {
        messages.ERROR: 'danger',
        messages.SUCCESS: 'success',
    }

Agora precisamos criar um template html para exibir as mensagens. Como não é um html complexo, podemos criá-lo dentro de "partials" uma nova partial "_alertas.html".

Dentro dele, em primeiro lugar verificaremos se há alguma mensagem, com `{% if messages %}` e fecharemos com o `{% endif %}`. Caso haja alguma mensagem, faremos um for(e também fecharemos com `{% endfor %}`) e assim, cada mensagem será exibida conforme o alerta do bootstrap, que variará a depender da mensagem ser de erro ou de sucesso.

Vamos copiar do site do bootstrap o código para a mensagem de erro, e colaremos no nosso arquivo; Criamos as message tags no "settings.py", então, faremos algumas alterações no código trazido.

Não exibiremos mais todo o conteúdo que diz "This is danger alert-check it out!". Em vez disso, exibiremos {{message}}. com chaves duplas. Já criamos as message tags em "settings.py" e não queremos que todas mensagens de erro venham com um alerta de danger.

Por isso, no lugar de class="alert alert-danger"colocaremos class="alert alert={{message.tags}}". Dessa forma, conseguiremos criar tanto mensagens de sucesso quanto de erro.

    {% if messages %}
        {% for message in messages %}
        <div class="alert alert-{{message.tags}}" role="alert">
            {{ message }}
        </div>
        {% endfor %}
    {% endif %}

Por enquanto, incluiremos essa partial em dois lugares em nossas páginas, primeiramente no login. Em "login.html" teremos as partials de menu, e antes da linha onde temos a classe row e começa nosso formulário digitaremos {% include 'partials/_alertas.html' %}.

Adicionaremos a partial também no cadastro, no mesmo lugar, antes da classe row, e salvaremos ambos os arquivos. Agora criaremos duas mensagens para testar, uma de erro e uma de sucesso.

Abriremos "usuarios > views.py" e teremos que importar as mensagens para o código. Importaremos de django.contrib. Já fizemos antes o import de auth, agora digitaremos uma vírgula na sequência e escreveremos messages. e vamos salvar.

Podemos colocar as mensagens de erro em vários lugares. Escolheremos dois exemplos simples. Exibiremos uma mensagem de erro quando as senhas fornecidas não forem iguais. Para tal, escreveremos messages.error() logo após a verificação if senha!- senha2 e passaremos alguns parâmetros.

O primeiro deles será o request. O segundo será a mensagem, a mesma que exibíamos no terminal, 'As senhas não são iguais'. Depois, se conseguirmos cadastrar um usuário, exibiremos uma mensagem de que o cadastro foi realizado com sucesso.

Logo após o print do cadastro, escreveremos messages.success() e passaremos a request e a mensagem 'Cadastro realizado com sucesso' para os parâmetros. Então, teremos duas mensagens, uma de erro quando as senhas forem diferentes, e uma de sucesso quando conseguirmos realizar o cadastro.

    def cadastro(request):
        if request.method == 'POST':
            nome = request.POST['nome']
            email = request.POST['email']
            senha = request.POST['password']
            senha2 = request.POST['password2']
            if not nome.strip():
                print('O campo nome não pode ficar em branco')
                return redirect('cadastro')
            if not email.strip():
                print('O campo email não pode ficar em branco')
                return redirect('cadastro')
            if senha != senha2:
                            messages.error(request, 'As senhas não são iguais')
                print('As senhas não são iguais')
                return redirect('cadastro')
            if User.objects.filter(email=email).exists():
                print('Usuário já cadastrado')
                return redirect('cadastro')
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            print('Usuário cadastrado com sucesso')
                    messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login')
        else:
            return render(request,'usuarios/cadastro.html')

Agora vamos testar. Lembrando que não colocaremos mensagens de erro e sucesso para todas as possibilidades, mas é interessante tentar fazer isso. Voltaremos à aplicação e começaremos com o cadastro.

Colocaremos o nome Ana, o e-mail ana@alura.com, a senha "123" e a confirmação "12". Quando clicarmos no botão para a criação de conta, leremos a mensagem de erro "As senhas não são iguais".

Agora tentaremos criar o cadastro colocando senhas correspondentes e quando clicarmos em "Crie sua conta" leremos "Cadastro realizado com sucesso, e teremos sido direcionados para a página do login.

Agora, a sugestão será criar as mensagens por conta própria, e será possível copiar o texto sendo exibido pelos prints para isso, e apagá-los, porque não serão mais necessários. Utilizávamos eles para nos ajudar a desenvolver nossa aplicação, mas agora podemos nos basear no próprio site. A ideia valerá tanto para o cadastro, quanto para o login.

### Refatoração e ajustes finais

Vamos melhorar um pouco a legibilidade do nosso arquivo "views.py"?

Algo que poderemos fazer será isolar algumas funções que repetimos em outras funções, para reutilizá-las. Copiaremos o trecho not nome.strip(), após o if, que verifica se um campo está vazio.

Ao fim do código, criaremos uma função chamada campo_vazio(), na qual receberemos campo como parâmetro, e retornaremos a verificação copiada. No lugar de nome, passaremos campo, ou seja, o retorno será return not campo.strip().

No nosso formulário de cadastro, em vez de fazer a verificação para o nome, para o e-mail e assim por diante, perguntaremos se campo_vazio(), e passaremos o nome do campo (por exemplo, nome) para os parâmetros.

No lugar de exibir um print, exibiremos messages.error(), devolvendo a requisição e a mensagem que já tínhamos anteriormente, Portanto, se o campo nome estiver vazio, será exibida a mensagem de erro e o usuário será redirecionado para a página de cadastro.

A função campo_vazio() servirá para o email na sequência, e também alteraremos o print para messages.error(), devolvendo um request e a nossa mensagem. Dessa forma já conseguiremos melhorar nosso código.

Teremos a validação de senha senha != senha2. Para saber se devemos removê-la e isolá-la em determinada função reutilizável, será necessário sempre analisar cada situação nos nossos projetos. Caso seja uma função que utilizamos várias vezes, ou um trecho de código que repetimos, será interessante isolar.

Porém, a legibilidade de senha != senha2 não será tão simples. Podemos tornar esse trecho de código mais compreensível criando uma função que verifica se as senhas não são iguais, senhas_nao_sao_iguais(). Receberemos a senha e senha2, e o return será a verificação.

Então, no lugar de if senha != senha2, usaremos nossa função, com if senhas_nao_sao_iguais(senha1, senha2), tornando muito mais claro o que estamos fazendo. Se não forem iguais, vamos redirecionar o usuário para o cadastro.

    def cadastro(request):
        if request.method == 'POST':
            nome = request.POST['nome']
            email = request.POST['email']
            senha = request.POST['password']
            senha2 = request.POST['password2']
            if not nome.strip():
                print('O campo nome não pode ficar em branco')
                return redirect('cadastro')
                    if campo_vazio(nome):
                messages.error(request,'O campo nome não pode ficar em branco')
                return redirect('cadastro')
            if campo_vazio(email):
                messages.error(request,'O campo email não pode ficar em branco')
                return redirect('cadastro')
            if senhas_nao_sao_iguais(senha, senha2):
                messages.error(request, 'As senhas não são iguais')
                return redirect('cadastro')
            if User.objects.filter(email=email).exists():
                print('Usuário já cadastrado')
                return redirect('cadastro')
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            print('Usuário cadastrado com sucesso')
            return redirect('login')
        else:
            return render(request,'usuarios/cadastro.html')

    // trecho do código ocultado

    def campo_vazio(campo):
        return not campo.strip()

    def senhas_nao_sao_iguais(senha, senha2):
        return senha != senha2

Assim garantimos que a leitura do código ficará muito mais clara, e isolamos essas pequenas ações em funções menores. Vamos agora testar esses valores.

Deixaremos o campo de nome vazio, usaremos um e-mail inventado e uma senha e verificação de senha iguais. Quando clicarmos no botão para criar a conta, veremos a mensagem na tela de que o nome não pode ficar em branco.

Então, preencheremos o nome como "Teste". Colocaremos um e-mail que já existe, pois temos no nosso projeto uma validação para redirecionar para o cadastro quando o e-mail do usuário já estiver cadastrado. Usaremos o gui@alura.com.br, e a senha "123", a mesma para a confirmação.

Tentaremos criar a conta e não receberemos a mensagem de erro, porque para o caso do e-mail já cadastrado, teremos apenas um print. Vamos substituí-lo pelo messages.error(), passando a requisição e a nossa mensagem.

    if User.objects.filter(email=email).exists():
        messages.error(request,'Usuário já cadastrado')
        return redirect('cadastro')

Vamos testar de novo com o nome Teste, o e-mail do Gui e a mesma senha. Agora, clicaremos no botão "Criar sua conta" e veremos na tela a mensagem "Usuário já cadastrado".

Veremos nesse momento algo que poderíamos deixar passar na nossa aplicação e ficaria confuso. Vamos colocar o nome de um usuário que já existe com o e-mail de um usuário que não existe.

Por exemplo, a Ana, que já existe na nossa aplicação se olharmos na nossa base de dados. Porém usaremos um e-mail diferente, teste@teste.com, com as senhas "123". Quando tentarmos criar a conta, teremos um erro de integridade.

Isso acontecerá, porque o auth_user_username_key utilizará sempre o nome do usuário para fazer a verificação se ele já existe ou não. Para não cairmos nesse tipo de erro, verificaremos, além da existência do e-mail, a do nome de usuário também.

Logo abaixo da verificação do e-mail, colocaremos a última verificação. Se o username=nome, ou seja, se já existir, nesse caso não permitiremos o cadastro de um usuário já cadastrado, pois dificilmente teremos um usuário com o mesmo nome e o mesmo e-mail.

Pode soar um pouco confuso porque o Django usa o username para fazer as validações, mas dessa forma evitaremos o erro de integridade.

    if User.objects.filter(username=nome).exists():
        messages.error(request,'Usuário já cadastrado')
        return redirect('cadastro')

Voltaremos à página do cadastro e colocaremos o nome "Ana" e o e-mail teste@teste.com, com senha "123". Quando tentarmos criar, não conseguiremos, e veremos a mensagem de que o usuário já estará cadastrado.

Então ficará como desafio detectar se há outras funções ou ações realizadas várias vezes, e pensar se valeria a pena isolá-las numa determinada função e apenas reutilizá-la em partes diferentes da aplicação, como campo_vazio() ou senhas_nao_sao_iguais().

Isolar funções também poderá nos ajudar em questões de legibilidade. Antes tínhamos o senha != senha2, dizendo que as senhas não eram iguais, agora se as senhas não são iguais, além da função com um nome mais legível, exibiremos uma mensagem de erro para o usuário.

Refatoramos o cadastro, agora também podemos pensar em alguns trechos do login. Por exemplo, fazemos a verificação se o e-mail e a senha estão em branco na hora do login, portanto podemos utilizar também campo_vazio(). para a validação.

Faremos if campo_vazio(email) or campo_vazio(senha), e diremos que os campos não podem ficar em branco para o usuário. Por isso, não poderemos usar o print, e vamos trocá-lo pela messages.error(), que receberá um request e a mensagem que já tínhamos na impressão.

Caso haja um erro, redirecionaremos o usuário para a página do login, deixando o código mais claro.

    def login(request):
        if request.method == 'POST':
            email = request.POST['email']
            senha = request.POST['senha']
            if campo_vazio(email) or campo_vazio(senha):
                messages.error(request,'Os campos email e senha não podem ficar em branco')
                return redirect('login')

    // trecho do código ocultado

Vamos à página de login e deixaremos o campo de e-mail vazio. Colocaremos apenas alguns espaços na senha e tentaremos nos logar. Veremos a mensagem de que os campos e-mail e senha não podem ficar em branco.

Desta vez digitaremos o e-mail a@a.com e deixaremos a senha em branco. Quando tentarmos acessar, novamente seremos alertados de que os campos e-mail e senha não podem ficar em branco.

Assim, de forma simples, conseguimos garantir um resultado melhor para nossa aplicação. Agora realizaremos o login corretamente, com o email gui@alura.com.

Vamos observar que na aplicação há um espaço grande entre as boas vindas "Olá Gui Lima" e as receitas, o que poderá ser melhorado. Entraremos em "templates > dashboard.html", onde há um padding de 0 e depois um de 80. Podemos diminuí-lo para um valor melhor, ou diminuir o mb.

Deixaremos o padding como 0, e quando atualizarmos a página já conseguiremos uma visualização melhor. Isso significa que mesmo quando terminamos uma etapa de desenvolvimento da nossa aplicação, podemos pensar em como melhorá-la.

Nesse momento já fizemos grandes avanços e conseguimos criar e visualizar as receitas, assim como visualizar a página principal da aplicação.

É importante lembrar que em "views.py", na função cria_receita(), não fizemos nenhuma validação porque não teríamos tempo de validar todos os campos durante nosso curso. Mas como já sabemos como reutilizar funções para saber se um campo está vazio, por exemplo, e redirecionar o usuário exibindo uma mensagem de erro ou uma mensagem de sucesso, poderemos deixar o sistema do nosso projeto Django muito melhor configurado.

### Mensagem não exibida

Para tornar a experiência do usuário de um site melhor, uma pessoa decidiu incluir mensagens de validações no formulário de novos usuários. Caso os dados não sejam válidos, uma mensagem de erro é exibida.

Sabendo disso, analise as afirmações abaixo e marque as verdadeiras.

a) No Django não podemos criar nossas próprias messages tag.

b) Podemos utilizar o código messages.error('O campo nome não pode ficar vazio') para exibir uma mensagem de erro informando que o campo nome está vazio.

c) Alternativa correta: Quando criamos uma partial para manter o código de alertas e mensagens, não podemos esquecer de incluir tais partials nas páginas onde queremos exibir.
- Certo! Ao criar uma mensagem de sucesso ou de erro, precisamos garantir que a partial será exibida.

### O que aprendemos?

[GitHUB]('https://github.com/alura-cursos/alura_receitas_django_parte3/tree/aula_5')

# 4. Boas práticas no Django: apps, pastas e paginação
**Fonte:** Guilherme LIma<br>
**Disponível:** <a href="https://cursos.alura.com.br/course/fundamentos-django-2" target="_blank">ALURA</a><br>
**Conteúdo:**
- Aprenda a editar, atualizar e remover objetos
- Saiba como trabalhar com formulários no Django
- Desenvolva uma boa arquitetura em seus projeto Django
- Entenda como incluir paginação no Django
- Crie uma aplicação inspirada num produto real
## 01. Deletando objetos e apps no Django Ver primeiro ### ### Introdução

[00:00] Meu nome é Guilherme Lima, eu sou instrutor da Alura e seja muito bem-vindo à esta quarta parte do treinamento "Utilizando o Django 2."

[00:07] Neste curso, o que vamos aprender? Vamos finalizar o CRUD de receitas da nossa aplicação, vamos melhorar a arquitetura do nosso código e também vamos incluir paginação no nosso site.

[00:20] Na nossa aplicação, vamos incluir aqui nas minhas receitas esses dois botões: um para editar as receitas e outro para deletar. Anteriormente, nós só conseguíamos criar. Agora vamos conseguir editar as nossas receitas, também. Além disso, na página principal, vamos adicionar esse menu de navegação aqui, para que nós tenhamos paginação no nosso site.

[00:40] Pensando em tudo isso, também vamos alterar a arquitetura do nosso site para que fique mais fácil a edição e manutenção dos nossos códigos. Vamos criar uma pasta de “apps”, aprender a trabalhar com mais de uma “view”, ter uma pasta de “views” para trabalhar com mais de uma “view” no Django, pensando em manter o nosso código de forma mais simples, conseguir dar a manutenção de forma mais simples.

[01:05] Quais são os pré-requisitos desse treinamento? É muito recomendado que você tenha feito os cursos anteriores de Django 2, - utilizando a versão 2 - para que você entenda bem onde nós paramos e para onde estamos indo na nossa aplicação.

[01:20] Fazendo esse curso, você vai aprender a trabalhar com formulários, vai aprender como manter o seu código Django mais organizado, a arquitetura do seu código Django bem dividida.

[01:31] E para quem é esse curso? Esse curso é recomendado para as pessoas que não tiveram contato com a linguagem Python para web utilizando o Django e que fizeram as outras partes do treinamento. É muito recomendado que você tenha feito as outras partes.

[01:47] Se você fez as outras partes e chegou neste curso, ele é super recomendado para você. Caso queira ver um ponto ou um tópico deste curso, você também pode.

[01:56] Então, sabendo de tudo isso, vamos começar?

### Saudações e Ambiente

Olá!
É muito bom receber você nesta quarta parte do curso. Espero que seja uma experiência de aprendizado incrível e que possamos vencer todos os desafios e continuar o desenvolvimento utilizando o Django.

Divisão das aulas
Aula	O que vamos aprender?
Deletando receitas e apps	Vamos criar um botão para deletar as receitas e remover o app de pessoas
Editando e atualizando	Vamos finalizar o CRUD de receitas possibilitando a atualização dos dados
Melhorando arquitetura do código	Vamos alterar os pacotes e arquivos para manter o código organizado
Paginação no Django	Vamos aprender como incluir paginação na página principal do site
Refatoração de código	Vamos criar uma pasta para manter nossos apps e adicionar docstrings
Preparando ambiente
Este curso é a terceira parte dos treinamentos de Django 2 da Alura. Portanto, é recomendado que você tenha feito a terceira parte do curso – Integração de modelos no Django 2: Filtros, buscas e admin.

Além disso, para conseguir acompanhar este curso, é recomendado que você tenha o Python3 instalado.

Caso necessite ajuda para instalação do Python, recomendamos os seguintes links:

Passo a passo para instalar o Python3 no Windows.

Passo a passo para instalar em outros sistemas operacionais.

Para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

    Python 3.7.4
    Django 3.0.3

O Django pode ser instalado através do comando:

    pip install Django==3.0.3

Em caso de dúvida na instalação ou durante o curso, conte sempre com o fórum da Alura!

Vamos começar?

:)

### Deletando receitas

[00:00] Vamos iniciar a nossa quarta parte do treinamento de Django? Para começar, eu tenho aqui a minha aplicação funcionando. Se eu clico aqui no suco verde, eu consigo visualizar o suco verde, e todas essas receitas que estão na página principal são as receitas que estão publicadas para que qualquer pessoa, logada ou não, possa ver.

[00:19] Além disso, eu tenho uma aba de minhas receitas, onde as receitas que eu criei só estão disponíveis para mim, então, aqui é o meu “dashboard”. O dashboard da pessoa que eu estou, que se chama Gui Lima.

[00:32] Eu consigo visualizar o pão, ou a torta de morango. Eu clico aqui, tem a torta de morango e os detalhes da torta de morango, então, nós conseguimos criar as nossas próprias receitas e deixar essas receitas visíveis apenas para nós.

[00:46] O que eu quero fazer agora é - nós conseguimos criar uma nova receita mas não conseguimos remover uma receita. Por exemplo, se eu quero alterar ou colocar uma outra receita de pão e eu não quero guardar essa receita de pão aqui, eu quero armazenar outra receita de pão. Do jeito que está a nossa aplicação, nós não conseguimos tirar essa receita, então, vamos criar uma forma de conseguirmos remover, também, as receitas da nossa aplicação.

[01:08] Nós conseguimos criar, nós trabalhamos bastante na parte 3 com formulário, como nós salvamos e criamos as nossas receitas. Agora, o que eu quero fazer é deletar algumas receitas.

[01:18] O que nós podemos fazer é colocar embaixo do nome da receita um botão escrito “deletar”. Quando clicamos, aquela receita simplesmente é removida do nosso dashboard. Vamos fazer isso?

[01:30] Então, no nosso código, o que eu vou fazer? Vamos criar primeiro esse botão. Eu vou colocar em “templates”. No template de usuário, eu vou na página de dashboard, que é onde nós estamos. Aqui, olhe: “dashboard”, que é onde eu estou vendo o meu dashboard.

[01:44] Deixe-me minimizar. Aqui, eu tenho a página de dashboard e, aqui, eu tenho o nome da receita. O que eu quero fazer? Eu quero criar embaixo do nome da receita, um botão, e esse botão vai ser um link para deletar uma receita.

[01:56] Então, eu vou colocar aqui a tag “” e a URL que eu vou utilizar através de código Python – deixe-me colocar aqui. A URL que eu vou utilizar vai ser essa aqui, olhe: "url". Nós precisamos criar uma URL que delete a receita.

[02:10] Então eu vou criar aqui, olhe: “<a href=“{% url deleta_receita %}”>”. Maravilha, mas qual receita ele vai deletar? Deixe-me colocar esse aqui entre aspas simples. Qual receita ele vai deletar? Eu preciso informar qual é a receita.

[02:25] Se nós observarmos, se eu seleciono, aqui, o “Pão”, observe no canto da minha tela. Olhe ele mostra ali "localhost:8000/10" e se eu venho na torta de morango, - "localhost:8000/9," - eu consigo pegar o ID dessa receita.

[02:38] Então eu posso falar: para cada receita, eu quero “<a href=“{% url ‘deleta_receita’ receita.id %}”>”. Então, cada receita que eu quiser deletar vai ter um ID associado a ela, para sabermos qual é a receita que queremos deletar.

[02:52] Além disso, eu quero que esse nosso link tenha uma cara de botão, então eu vou colocar aqui o 'type="button' e, para deixá-lo com um visual mais legal, nós podemos usar as propriedades do bootstrap.

[03:05] Então, eu vou colocar aqui em "class," e vou chamar o "btn btn-danger" para ficar um botão com a cara vermelha, e aqui dentro desse espaço, eu vou escrever o que eu quero exibir nesse botão. Vou colocar "Deletar."

[03:20] Vou salvar. Quando eu volto na minha aplicação e atualizo, nós recebemos uma mensagem de erro porque nós não cadastramos essa rota. Nós precisamos cadastrar essa rota na nossa aplicação, também.

[03:30] Então, venho aqui. Como estamos trabalhando com o app de usuários, eu venho em “usuarios”, venho em “urls.py”, e observe que, em “urls.py”, nós temos uma de “cadastro”, “login”, “dashboard”, “logout”, “cria/receita” e agora, eu vou ter uma para deletar a minha receita.

[03:47] Eu vou criar aqui um novo “path” – deixe-me colocar a vírgula, não posso esquecer. Vírgula, agora sim - eu vou chamar esse path de "deleta." Então, eu vou chamar aqui "deleta" e eu preciso passar o ID. Lembra que nós passamos aqui na URL? Olhe, nós vamos passar o ID da receita que queremos deletar.

[04:11] E precisamos informar esse nosso ID aqui na função que vamos deletar, também, então eu faço isso com o sinal “<”, vou escrever "int:receita_id" e fecho com o sinal “>”. Agora sim, nós passamos aqui para conseguirmos deletar essa nossa receita. Além disso, o que precisamos informar conforme o padrão que nós já vimos? Olhe, ele até nos fala.

[04:41] Além do path que nós colocamos, algum controle - que aqui no Django, chamamos de “views” - vai ter que ser responsável por realizar essa ação de deletar, então eu vou falar aqui.

[04:53] Vamos lá! Criar em “views.” E u vou criar uma função que se chama "deleta_receita," e vou dar um “name= ‘deleta receita’", também. Eu vou chamar, aqui: “deleta_receita”.

[05:14] Fechamos o nosso parênteses, não podemos esquecer, então a nossa linha ficou com essa cara. Eu vou salvar, ele vai dar uma marcação vermelha, que vai falar "não existe ninguém em “views” que se chama deleta receita." Olhe lá: “Module ‘usuarios.views’ has no deleta_receita’ member pylint(no-member)”.

[05:30] Então vamos criar: venho aqui em “views.py” de “usuarios”. Nós temos uma função de “cadastro”, uma função de “login”, uma função de “logout”, “dashboard”, “cria_receita”, “campo_vazio”, “senhas_nao_sao_iguais” e agora, eu vou criar quem? O “deleta_receita”.

[05:45] Então, eu vou colocar aqui embaixo uma nova função, “def deleta_receita” e nós vamos receber um parâmetro, que qual é? A requisição, como de costume, que já temos. A requisição, a "request" e a "receita_id," o ID da receita que nós queremos deletar, então “(request, receita_id):”

[06:10] Agora, o que nós queremos fazer é: assim que essa função for chamada, eu quero pegar essa receita e deletar. Para eu conseguir pegar essa receita, eu vou fazer o seguinte: vou chamar aqui "receita =" e vou usar a propriedade “get_object_or_ 404”. Eu quero que pegue o objeto dessa receita. Legal mas qual receita?

[06:28] Ele vai falar, assim: “qual é o modelo que estamos utilizando? Qual o objeto?” Vamos pôr objeto de “(Receita, ) aqui e quem eu quero deletar. O objeto que eu quero buscar é esse, eu vou passar a “(Receita, pk=receita_id)”.

[06:47] Tenho a receita que eu quero deletar, está armazenada aqui dentro de receita. Eu uso agora o “receita.delete”, dessa forma. Depois que essa função é executada, eu preciso direcionar a pessoa para algum lugar, então eu vou direcionar, dar um “return” ou “redirect” para a página de dashboard mais uma vez. “dashboard”, só que precisa estar entre aspas simples: 'dashboard'.

[07:17] Eu vou salvar. Salvei. Volto na minhas “urls.py”, salvo mais uma vez. Percebam que o erro já não aparece mais. O que nós fizemos? Criamos o botão, criamos esse link de "deleta_receita." Depois, registramos essa URL e a direcionamos para ser atendida pela “view.deleta_receita”, criamos em “deleta_receita” essa nossa função, que pega esse objeto que queremos deletar e depois o redireciona para a página “dashboard”. Vamos lá?

[07:54] Voltando à nossa aplicação e salvando, nós teremos um botão “Deletar” aqui embaixo. Quando passamos o mouse em cima, ele até tem uma animação. O que eu quero fazer? Eu vou deletar o “Pão”. Quando eu clicar em deletar pão, nós não temos mais a receita do pão, só a torta de morango, então dessa forma, nós conseguimos remover algumas receitas.

[08:14] Agora, nós temos quase o nosso CRUD completo e nós conseguimos criar as nossas receitas, conseguimos visualizá-las, lê-las e, agora, também conseguimos deletá-las.

### Deletando um app

[00:00] Estou logado com um usuário que tem permissão de acessar o administrador do Django e, quando eu acesso esse administrador, digito “localhost:8000/admin/”, tenho acesso ao administrador e nós conseguimos visualizar o nosso app de pessoas.

[00:12] Só que, na nossa aplicação, não estamos utilizando mais esse app. Se nós voltarmos no nosso código e abrir as divisões, a parte estrutural do nosso código, que temos o “alurareceitas”, “media”, “pessoas”, - observe que “pessoas” já tem um monte de arquivo, um monte de coisas, um “models.py” e mais. Nós temos esses dados no nosso banco de dados, também. Aqui, olhe: “pessoas_pessoa”.

[00:34] O que eu quero fazer agora é remover esse app da minha aplicação. Isso é uma tarefa que demanda bastante cuidado e vamos aprender como que conseguimos remover um app do nosso projeto.

[00:45] A primeira coisa que nós vamos fazer vai ser no nosso “alurareceita”, onde ficam as configurações do nosso site, da nossa aplicação, nós temos esse app cadastrado e instalado nesse nosso projeto.

[00:58] O que eu vou fazer vai ser tirar. Eu vou remover o app de pessoas e salvar. Quando eu salvar, se eu voltar na nossa aplicação e atualizar a página, observe que vai ter um erro e nós não vamos conseguir logar. Por quê?

[01:10] Quando abrimos o nosso terminal com o comando command+J, observe que, nas dependências, ele fala que existe uma migração que depende desse app, então nós tiramos o app dos apps instalados aqui do “alurareceita”. Só que, aqui no nosso app de receita, em “migrations”, nós temos a “0002_receita_pessoa.py”.

[01:29] Deixe-me minimizar, para visualizarmos melhor, - na “migrations”, nós temos a migração “0002_receita_pessoa.py”, ainda dependemos desse app de pessoas, e mais!

[01:36] Nós falamos para ele procurar no app de pessoas uma pessoa para vincular porque nessa “migrations”, nós temos a migração “0002_receita_pessoa.py”, o que tínhamos feito? Nós adicionamos um novo campo para dizer que toda receita vai ter algum criador ou uma criadora, uma pessoa que publicou aquela receita.

[01:52] E conforme foi aumentando e desenvolvendo a nossa aplicação, nós alteramos. Quando manter agora as pessoas na nossa aplicação, - as pessoas que publicaram as receitas - não vai ser mais o app de pessoa, e sim o nosso modelo de usuários do Django.

[02:10] Então nós vinculamos primeiro a pessoa, depois nós vinculamos com o usuário e não utilizamos mais o app de pessoa, então, o que nós podemos fazer?

[02:19] Nós temos algumas opções aqui. O que nós podemos fazer: nós removemos do apps instalados e, agora, precisamos remover todas as partes que contem vínculo com esse app. Nós vamos alterar.

[02:35] Eu vou pegar esse “field” aqui da nossa migração “0005_auto_20191219_1500.py”, vou copiar essa nossa migração, teclas “Ctrl + C”. Vamos voltar na migração “0002_receita_pessoa.py”, onde temos o vínculo com pessoa e vou alterar.

[02:48] Vou remover toda essa linha aqui até o “field”, - essas duas linhas - e vou usar as teclas “Ctrl + V”, agora utilizando do “to=settings.AUTH_USER_MODEL),”. Assim que nós salvamos, temos uma mensagem de erro no “settings” porque precisamos importar esse modelo para utilizarmos os modelos do Django.

[03:04] Então o que eu vou fazer? Aqui em cima, podemos ver que nós temos “from django.conf import settings”. Nós temos que passar isso também para o nosso “settings”, para a nossa importação.

[03:18] Salvando, o erro não acontece mais. O que precisamos fazer além disso? Nós vamos tirar esse app de pessoas, não queremos vínculo com pessoas e, no nosso caso, isso já seria suficiente da parte do nosso projeto.

[03:32] Lembrando que, se você criou vínculos nos templates, nos modelos ou em alguma outra parte da aplicação, se você deseja tirar esse app, esse vínculo com o app, é necessário que você garanta que nenhuma parte do seu projeto vai utilizar esses vínculos.

[03:50] Então nós alteramos aqui, só que temos um problema. No nosso projeto, nós alteramos na nossa base de dados, nós precisamos remover esse nosso app de pessoas também.

[04:06] Então o que eu vou fazer? Vamos fazer algo a mais. Observe que, na nossa aplicação, - deixe-me atualizar aqui - nós conseguimos visualizar. Vamos ver se conseguimos visualizar a página principal.

[04:16] Observe que, na nossa aplicação, teoricamente, tudo está funcionando. As dependências do app de pessoas não existem mais porém esses arquivos que temos na nossa base de dados são arquivos de teste, nós estamos testando. Criamos algumas receitas. Eu tenho, aqui, uma receita publicada na forma de teste.

[04:35] E nosso projeto não tem vínculo com o app de pessoas, com o nosso modelo de pessoas, só que, na nossa base de dados, ainda existe essa tabela de pessoas. O que eu vou fazer?

[04:45] Para nós conseguirmos manter o histórico das nossas migrações, podemos ver em “migrations” que nós temos um histórico: a migração “0001_initial.py”, criamos a receita. A migração “0002_receita_pessoa.py”, adicionamos o campo pessoa no nosso modelo de receita e falou que ele agora tem vínculo com o “AUTH_USER_MODEL”.

[05:04] É necessário que nós passemos essas migrações, essas alterações para o nosso banco de dados, também, então o que eu vou fazer? Eu vou abrir o meu terminal. Vou parar a minha aplicação com as teclas “Ctrl + C”. Parei a minha aplicação.

[05:17] O que eu vou fazer vai ser assim: vou deletar o meu banco de dados, “Delete Drop”. Vou dar um “OK” e ele deletou o banco de dados. Vou clicar com o botão direito aqui em cima do “Database”, vou dar um “Database...”, “Create – Database”. Com o botão direito eu dei “Create – Database”.

[05:32] Aqui no nome, eu vou chamar de “alura_receita”, o mesmo nome do banco que tínhamos anteriormente. Criei, o “alura_receita”. Se nós acessarmos o banco de dados, vamos ver que não temos nenhuma informação, nenhuma tabela nessa nossa base de dados. Por quê?

[05:47] Porque nós temos as migrações, já criamos as migrações, só que não migramos, de fato, para o banco de dados. O que eu posso fazer é falar assim: “python manage.py migrate”. Eu já tenho as migrações. Agora, eu quero que você migre com essas informações, com esses dados que eu tenho aqui.

[06:04] Quando eu aperto a tecla “Enter”, observe que ele vai subir todas as migrações que nós já tínhamos e agora, de fato, nossa tabela de pessoa não existe mais. Olhe só: se clicarmos aqui - eu vou dar um “refresh” - abrindo aqui, podemos ver que não temos mais a nossa tabela de pessoa. Nós temos, aqui, 11 tabelas.

[06:25] Então dessa forma, nós conseguimos remover um app porém nós tivemos uma perda, nós perdemos os dados da nossa aplicação. Se eu acessar aqui, observe que eu não consigo acessar a nossa loja, o nosso site, o nosso “dashboard”. Por quê?

[06:40] Quando perdemos os dados da nossa aplicação, perdemos um membro muito importante que era o “superuser”, o super usuário do Django, então, eu vou criar aqui um super usuário. – Deixe-me fechar essas informações. Agora, sim. - O que eu vou fazer agora vai ser criar um super usuário para que ele possa criar outros usuários e nós possamos criar as nossas receitas, também.

[07:03] Então, o que eu vou fazer? Eu vou dar um “python manage.py createsuperuser”. Vou atribuir um nome, vou chamar de “gui”. O endereço de e-mail vai ser “gui@alura.com” e a minha senha vai ser essa aqui. Maravilha, ele falou que a senha é curta. Eu vou manter essa senha, mesmo. Criei o meu super usuário.

[07:26] Quando eu volto para a minha aplicação, vou atualizar. Observe que não está rodando a aplicação porque eu esqueci de subir o meu servidor, “python manage.py runserver”. Agora sim, subi o servidor. Quando eu atualizar, vou conseguir visualizar a nossa aplicação.

[07:49] Vou realizar o login por aqui – “gui@alura.com” - e vou digitar a minha senha. Quando eu acesso - "Olá, Gui" - não tem nenhuma receita. Eu posso acessar o administrador porque sou superusuário, então, “localhost:8000/admin/”. Eu tenho aqui os usuários.

[08:04] Observe que agora, nós já não temos nem aquele visual no administrador aqui do Django do app de pessoas. Nós conseguimos, de fato, tirar esse app da nossa aplicação.

### ORM e deletando um registro

Patrícia está desenvolvendo uma aplicação web com Django e foi solicitada excluir o registro do seu banco de dados com id=1:

    delete from table_name where id = 1;

Para utilizar o ORM do Django e obter o resultado acima, qual comando ela pode utilizar?

a) Alternativa correta: instancia = NOMEdoObjeto.objects.get(id=1)
instancia.delete()
- _Certo! Podemos deletar a partir de uma instância do objeto através da função deletar._

b) instancia = NOMEdoObjeto.objects.get(id=1) 
instancia.deletar()

c) instancia = NOMEdoObjeto.objects.get(id=1) 
instancia.exclude()

## 02. Editando e atualizando formulários
### Dados para editar

[00:00] Na nossa aplicação, conseguimos criar receitas, deletá-las, visualizá-las mas não conseguimos editar uma receita. Por exemplo, se eu quiser alterar o nome dessa minha receita que só está "Sopa” manter todas as outras informações, eu não consigo. Nós não temos uma forma tranquila de fazer isso.

[00:18] O que eu poderia fazer, do jeito que a nossa aplicação está? Criar uma receita exatamente igual a essa com algumas alterações. Ficaria com duas receitas duplicadas, e eu viria aqui, deletaria essa receita e ficaria só com a receita que eu quero.

[00:30] Observe que, para conseguirmos atualizar as informações de alguma receita, está muito complicado, então vamos pensar em um jeito bem legal de conseguirmos editar as nossas receitas e finalizar o nosso CRUD.

[00:42] Bom, o que eu vou fazer? Nós podemos pensar essa forma de editar as receitas em dois passos. O primeiro passo é: eu vou criar uma forma de conseguir visualizar as informações da receita que eu quero editar, então aqui, eu posso criar um botão escrito "Editar".

[00:59] Quando eu clico nesse botão editar, abre um formulário parecido com esse nosso de criação de receita mas todos os campos da receita que eu quero editar estão preenchidos.

[01:10] Aqui, eu posso editar alguma informação que eu quero e aqui embaixo, eu clico no botão "Atualizar Receita". Aí sim, nós alteramos os valores na nossa base de dados.

[01:20] Então nessa primeira parte, vamos focar em buscar esse formulário, preenchendo todas as informações da receita que queremos editar. Para começar, eu vou criar aqui um botão que eu vou chamar de “Editar", para editarmos as receitas.

[01:35] Então, selecionando a nossa aplicação dentro da pasta “templates”, eu vou aqui no “dashboard.html”. Observe que no “dashboard.html”, nós temos aqui um link para deletarmos. Nós vamos ter um link parecido para nós conseguirmos editar as nossas receitas. Eu copiei e colei. Observe que nós temos aqui, agora, os dois links. Eles estão exatamente iguais e nós vamos editar esses links.

[01:59] No lugar de “deleta_receita”, o que eu quero fazer é editar a minha receita. Antes de atualizar, eu vou precisar editar a minha receita, então eu vou chamar de "“edita_receita”." Vou passar também o ID da receita que eu quero editar, vai ser do tipo botão também e no lugar do “btn-danger”, eu quero uma cor diferente. Pode ser um azul. Eu vou chamar aqui de “class=”btn-info”>”.

[02:21] E vou chamar, no lugar de deletar, esse botão de “Editar”. Quando eu salvo, o que eu preciso fazer? Nós precisamos ir na URL e cadastrar essa URL de ““edita_receita””.

[02:32] Eu vou fechar o meu “template”. Já abri em “usuarios”. Aqui na minha pasta de “urls.py, eu tenho um “path” que deleta a minha receita. Agora, eu vou ter um novo path. Eu copiei, vou colocar uma tecla “,” aqui no final, vou ter um novo path que vai editar as minhas receitas.

[02:49] Vai chamar “edita”. Eu vou receber o ID da receita que eu quero editar, só que, em “views”, quem vai ser responsável não vai ser o “deleta_receita”, vai ser o “edita_receita” e o “name”, também, eu vou chamar de “edita_receita”. Quando eu salvo, ele vai falar "Module ‘usuarios.views’ has no ‘edita_receita’ member pylint (no-member)”. Vamos criar.

[03:12] Abrindo o nosso usuários, aqui em “view.py” nós temos todos os nossos campos. – Deixe-me minimizar, só para não nos confundirmos, vamos fechando todas as nossas funções. - O que eu quero fazer agora é criar uma forma de conseguir editar as minhas receitas.

[03:30] Então, aqui dentro eu vou criar o meu novo método, que eu vou chamar de “edita_receita”, mesmo nome que nós demos para o URL. Nós vamos ter a requisição e o ID, então, nós vamos ter o “request” e vai ter, também, “receita_id”.

[03:56] Dentro do nosso “receita_id”, a primeira coisa que temos que fazer é: "quem nós estamos querendo editar?" Nós temos que saber qual é a receita que estamos querendo editar.

[04:03] Então eu vou atribuir, em “receita”, um objeto, a receita que nós estamos querendo editar: “receita=get_object_or_404” do nosso modelo de receita, -deixe-me alterar aqui, só para conseguirmos ver -eu quero buscar essa determinada receita.

[04:26] Observe que, no “deleta_receita”, o que fizemos? Nós passamos a “primary key”, ou seja, o identificador único de cada receita, e aqui, eu posso fazer a mesma coisa. Vou passar o “pk”, que vai ser o “pk=receita_id”.

[04:40] Nós já sabemos qual receita que queremos editar. O que eu preciso fazer agora? De alguma forma, passar essa receita que queremos editar para o nosso formulário que edita as receitas, então, eu vou criar aqui uma variável.

[04:52] Por exemplo: “receita_a_editar” - e essa “receita_a_editar”, eu vou criar dicionário, que eu vou chamar a chave de “{ ‘receita’: receita}” e essa receita vai ser do tipo receita que nós buscamos ali em cima.

[05:12] Agora que nós já buscamos a receita que queremos editar e criamos uma forma de passar isso para o contexto, para a nossa página HTML, nós vamos colocar aqui um “return render” - ele vai renderizar. Nós vamos devolver sempre no “render” o primeiro parâmetro, a requisição que queremos.

[05:31] Agora chegamos em uma parte importante, olhe só: nós precisamos renderizar. Lembra que eu disse que nós queremos renderizar um formulário parecido com esse nosso de criação de receita? - Opa! Aqui, eu não terminei. O “views” estava errado, eu já vou mostrar. Deixe-me salvar, aqui. Deixe-me ver se ele abre.

[05:50] Agora sim, criação de receita. Observe que eu quero esse formulário de criação de receita um pouco diferente. Só mostrando, por exemplo, a foto da receita que a pessoa quer utilizar, e o que eu quero fazer é popular todos esses campos aqui, certo? Só que eu preciso desse formulário, eu preciso desse “edita_receita”.

[06:09] Então, esse formulário de edição de receita, eu vou deixar disponível para vocês na atividade anterior. Na atividade anterior você vai ter acesso a esse nosso formulário de edição de receita.

[06:20] Então eu vou armazenar esse formulário em “templates” na pasta de “usuarios”, eu vou chamar de “edita_receita.html” e vou passar também, por contexto. Ele até fala qual é o contexto, vai ser o “receita_a_editar”.

[06:38] Salvei. O que eu vou fazer? Volto aqui em “urls.py”, salvo porque agora, nós temos esse método que edita. O que eu vou fazer agora é criar esse nosso formulário para editar as receitas.

[06:48] Então eu vou fechar aqui. – deixe-me fechar esses aqui, só para nós não nos confundirmos. - Dentro de “templates” e de “usuarios”, eu tenho “cadastro.html”, “cria_receita.html”, “dashboard.html” e “login.html”. Vou criar mais um arquivo: "New File." Aqui dentro, eu vou chamar de “edita_receita.html”, e aqui dentro, eu vou criar o meu formulário.

[07:08] Nós não vamos criar esse formulário na mão, eu vou deixar disponível para vocês todo esse código do formulário para editarmos a receita, vou copiar ele todo aqui e vou colar ele na nossa aplicação. Salvei. Vamos visualizar um pouco como esse formulário está?

[07:23] Super parecido com o que nós já vimos, incluindo as “partials”, o menu. Para ele ficar com um visual legal, está escrito "Edite aqui sua receita" e, aqui, nós temos uma parte importante do nosso formulário. Olhe só.

[07:35] Nós temos aqui um “form action”. Nós ainda não temos uma ação para esse formulário, que a ação será atualizar. Nós vamos ver no vídeo a seguir, vamos atualizar e temos aqui outras informações.

[07:48] Nós estamos indicando que o método é “post”, está passando o token de segurança e aqui, tem o “imput” de “receita_id”. Esse nosso “imput” de “receita_id”, observe que tem o “id=“receita_id”, o “class=“form-control”, o “name=“receita_id” e o “value={{receita.id}}”, o valor mesmo, o “receita.id”, e ele está com o tipo “hidden”, o tipo escondido.

[08:09] Outra coisa que nós temos aqui, também, nesse nosso formulário é - observe que todos os campos estão preenchidos. Todo lugar, nós falamos assim: olhe, valor é esse.

[08:18] No “text area”, nós falamos: "o valor do “text area” é esse aqui: “receita.ingredientes", ou “receita.” e o nome da receita, e nós fizemos isso para todos os outros campos. Vamos visualizar esse formulário na nossa aplicação?

[08:29] Então se eu acessar minhas receitas, agora nós temos um botão que edita e um botão que deleta. Eu vou clicar aqui no botão “Editar”. Aparece o nosso formulário, olhe: “Sopa”. Aqui tem os “Ingredientes”, o “Modo de preparo”, o “Tempo de preparo”, o “Rendimento”, a “Categoria dessa receita”, a “Foto utilizada” e uma outra foto que nós quisermos alterar.

[08:49] Quando eu clico aqui, em “Atualizar”, o que acontece? Não acontece nada porque no nosso “form action”, - se nós voltarmos aqui - nós não atribuímos nenhuma ação para esse nosso formulário, que é o que vamos ver no nosso próximo vídeo.

[09:00] Depois que editamos a nossa receita, nós queremos alterar esses valores no banco e é aqui que vamos começar a criar os passos para, de fato, atualizar as nossas receitas.

### Método para atualizar

[00:00] Agora que conseguimos visualizar todas as informações da receita que queremos editar, o que eu quero é alterar algum campo. Por exemplo, eu vou editar "Sopa de mandioquinha”. Alterei o título dessa receita. Quando eu clicar em “Atualizar”, eu quero voltar para a página do dashboard e visualizar, "Sopa de mandioquinha". Vamos fazer isso?

[00:19] Então eu vou clicar em "Editar" e vou deixar nessa tela. Na nossa aplicação, observe que no nosso formulário de “receita_id”, na linha 29, nós temos um “form action” que não tem nada, nós não vinculamos o nosso formulário com nenhuma ação, então nós precisamos criar uma URL que seja capaz de atender essa nossa requisição e, de fato, atualizar a nossa receita.

[00:45] O que eu vou fazer? Aqui dentro, através do "{%", eu vou colocar uma URL que vai ser capaz de atualizar nossa receita, então, eu vou chamar aqui de URL e vou chamar aqui de "form action=”{% url ‘atualiza_receita’ %}". Vou salvar.

[01:05] O que eu preciso fazer? Preciso registrar essa nova URL que eu criei, então, dentro de “usuarios”, eu venho aqui “urls.py” e – deixe-me minimizar aqui - observe que nós temos nesse nosso path, vários paths, então eu preciso colocar aqui o formulário que atualiza a receita.

[01:24] Eu vou criar um novo path, - colocar uma “,” aqui no final, não pode esquecer da vírgula, - um path que vai ser capaz de -"path(‘atualiza_receita’,)" - atualizar a receita. Quem vai ser responsável vai ser alguém em “views”, eu vou chamar essa nossa função de "atualiza_receita" e eu vou dar um name para ela, também de "name=’atualiza_receita’"

[01:56] Salvei, ele vai falar que não tem ninguém em views. Vamos em “views.py” e vamos criar essa nossa função que atualiza as receitas com "def". Então: "def atualiza_receita." Nós vamos receber como parâmetro “request” apenas para conseguirmos atualizar a nossa receita.

[02:20] O que nós vamos fazer? – Deixe-me minimizar aqui só para focarmos bastante nessa nossa função que atualiza as receitas. Eu vou colocá-la aqui embaixo, assim não vamos confundir.

[02:32] Deixe-me jogar esse aqui para cima. Essa minha função que atualiza a receita, para ela conseguir atualizar, o que nós precisamos verificar? Primeira coisa: se o método que está sendo utilizado é o método “post”, então vamos perguntar. Se o método da requisição é "if request.method == ‘POST’:", e agora sim, nós começamos a atualizar a nossa receita.

[03:06] O que eu preciso fazer agora é buscar qual é a receita que eu quero atualizar, então, observe que no nosso “edita.html”, nós temos um “imput” que está escondido com o ID da receita, então nós podemos pegar essa informação.

[03:21] Eu vou falar assim: aqui, o "receita_id = request.POST," para nós buscarmos aquela informação que está ali e eu vou chamar aqui de "receita_id." Dessa forma, nós trouxemos a informação que está nesse campo que não está sendo exibido na tela para esse nosso método.

[03:47] Nós trouxemos o “receita_id”. Agora, o que eu vou fazer? Para conseguirmos atualizar a receita, não vamos utilizar um outro “método update”, nós vamos utilizar o “método save”, também para atualizar as nossas receitas aqui no Django. É um pouco interessante isso.

[04:04] O que nós fazemos? Nós vamos alterando os campos que tem a necessidade de alterar, então, por exemplo: se eu alterei o título da receita, eu vou falar: o novo título da receita é esse e vou colocando todos os campos. Na sequência, eu dou um "Save" e ele atualiza, ele já sabe que aquela receita já existe e vai atualizar os valores.

[04:27] Para nós conseguirmos atualizar uma receita, nós não vamos utilizar um método update, o que é muito comum em outros frameworks, em outras linguagens. Nós vamos utilizar o método save, também.

[04:38] O que eu vou fazer? Eu vou chamar a receita que nós queremos atualizar de “r” e do meu modelo de receita, - "receita.objects.get" - para eu buscar essa minha determinada receita, eu vou falar: “(pk =receita_id)". Essa é a receita que eu quero editar.

[05:06] Agora, fica bem tranquilo. O que eu preciso fazer? Falo assim: “r.nome_receita = request.POST” e, aqui dentro, eu trago a informação do nome da receita que está no nosso formulário, "[‘nome_receita’]", então: "nome_receita.".

[05:30] Desta forma, nós vamos trazer todas as informações, também, então eu vou usar aqui as teclas “Ctrl + V”. Nós temos o nome da receita e também temos os “r.ingredientes”. Eu quero trazer aqui os "[‘ingredientes’]". Tenho que tomar cuidado para eu não errar na escrita.

[05:47] Nós temos, também, o “r.modo_preparo = request.POST”, - deixe-me copiar só esse trecho para ganharmos tempo - ele vai ser "[‘modo_preparo’]".

[06:07] Além do modo de preparo, nós temos o tempo de preparo. “r.tempo_preparo = request.POST”. Copiei o igual. Aqui, "request.POST['tempo_preparo']. Nós temos o rendimento, "r.rendimento", que vai ser igual, - não, vou colocar igual, quase caí na pegadinha que eu mesmo criei para mim mesmo. “r.rendimento = request.POST[‘rendimento’]”.

[06:40] E para finalizar, nós também temos a categoria. A “r.categoria = request.POST[‘categoria’]”. Maravilha.

### Atualizando receitas

[00:00] E aqui, um ponto interessante: nós chegamos na foto. Caso a pessoa inclua uma nova foto, nós atualizamos a foto; se não, nós mantemos a foto que a pessoa está utilizando. Como vamos fazer esse código?

[00:12] Nós vamos fazer uma verificação. Vou colocar aqui: "if ‘foto_receita’”. Se tiver alguma coisa dentro dessa requisição e nós pegamos aqui através do 'in request.Files', ou seja, se eu tiver alguma foto dentro de “request”, dentro dessa requisição, ele vai saber. Opa! Nós temos uma foto aqui dentro de “request.Files."

[00:45] Então, o que eu vou fazer? Se eu tiver uma foto, eu vou falar "r. foto_receita = request.Files” - não “POST”, mas sim “request.Files”, com o “F” maiúsculo, está bom? "[‘foto_receita’]". Trouxe todas essas informações. Caso tenha uma foto, eu faço isso.

[01:16] Se não tiver nenhuma foto, nós mantemos a mesma foto que nós já estávamos utilizando. No final, eu alterei todos esses valores, - olhe que interessante - dou um "r.save" e o que eu posso fazer para deixar mais legal ainda, esse nosso código é dar um “return” aqui. Deixe-me dar "return redirect( ‘dashboard’ )”.

[01:49] Então, assim nós criamos um meio de atualizar as nossas receitas. Vou salvar. Volto em “urls.py” e salvo. O que eu vou fazer agora? Vamos abrir a "MINHAS RECEITAS" Vamos ver se aqui está certinho? "Sopa de mandioquinha.", e aqui, eu coloquei “sopas". Quando eu dou “Atualizar”, nós recebemos uma mensagem estranha falando do atributo “Files” e isso eu fiz de propósito. Por quê?

[02:12] Observe que nós não escrevemos o “Files” apenas com o “F” maiúsculo, e sim com todas as letras maiúsculas, então aqui, olhe: "FILES," de arquivos, todos os arquivos com as letras maiúsculas. Salvei.

[02:27] Voltando a nossa aplicação e nós temos "Sopa de mandioquinha." Na categoria sopas, quando eu dou um “Atualizar” e agora sim: “Sopa de mandioquinha," nós conseguimos editar. Será que dá para editar mesmo? Vamos ver.

[02:38] Vou colocar aqui uma outra imagem na nossa “Sopa de mandioquinha”. Vamos ver se conseguimos editar também as nossas fotos? Eu tenho aqui o "Sopa de mandioquinha," vou colocar "Sopa de mandioquinha 2" para termos certeza disso, então eu vou alterar. Eu estou utilizando essa foto, vou utilizar essa aqui, a "sopa 2.jpg"

[02:56] Quando eu clico em "Atualizar," aparece uma outra foto e nós conseguimos editar. Eu vou tirar esse "2" da frente, agora. Vou colocar aqui "Sopa de mandioquinha." Maravilha.

[03:05] Quando eu dou "Atualizar," nós conseguimos atualizar agora, também, as nossas receitas, finalizando o nosso CRUD tanto de criação, de visualização, de editar, atualizar os nossos dados e deletar, também, as nossas receitas. Maravilha.

### Atualizando ou salvando

Para finalizar o CRUD (sigla em inglês para criar, ler, atualizar e deletar) de receitas, Marina criou uma página para editar os dados e um método, que de fato atualiza as informações no banco de dados, com o seguinte código:

    def atualiza_receita(request):
        if request.method == 'POST':
            receita_id = request.POST['receita_id']
            r = Receita.objects.get(pk=receita_id)
            r.nome_receita = request.POST['nome_receita']
            r.ingredientes = request.POST['ingredientes']
            r.modo_preparo = request.POST['modo_preparo']
            r.tempo_preparo = request.POST['tempo_preparo']
            r.rendimento = request.POST['rendimento']
            r.categoria = request.POST['categoria']
            if 'foto_receita' in request.FILES:
                r.foto_receita = request.FILES['foto_receita']
            r.save()
            return redirect('dashboard')

Analisando o código acima, podemos afirmar que:

a) Alternativa correta: Utilizamos a função save() para criar e atualizar a partir de uma instância.
- _Certo! Podemos utilizar a função save() tanto para criar um novo objeto como para atualizar a partir de uma instância, conforme mostra o código acima._

b) Caso não haja alteração na foto da receita, a foto antiga será apagada.

c) Este trecho de código irá criar uma nova receita, pois utiliza a função save().

## 03. Melhorando a arquitetura
### Refatorando a pasta template

[00:00] Vamos pensar, agora, como podemos melhorar a parte de arquitetura, como estão as nossas pastas e nossos arquivos da nossa aplicação. Para começar, na pasta "templates", observe que nós temos a “partials”, temos uma parte de “usuarios” e temos alguns arquivos soltos.

[00:18] Seria legal se pudéssemos manter a responsabilidade de cada página referente aos apps que temos, então se nós temos apps de receita, todos os templates relacionados com receita, nós podíamos manter dentro desse arquivo.

[00:33] Se temos um template relacionado com o usuário, nós podíamos manter todo template relacionado de usuário dentro do app de usuário, não é? E esses nossos outros arquivos - por exemplo, o “base.html”, - todas as páginas vão possuir, não é? Temos, aqui, o “head”, temos os códigos de Java script. Nós podíamos deixar fora, ele não faz parte de nenhuma responsabilidade nem de usuários, nem de pessoas.

[01:00] Então, o que eu vou fazer? O que eu sugiro? Vamos fazer o seguinte: eu vou criar uma pasta. Nós temos uma pasta de “partials”, nós temos uma pasta de “usuarios”. Eu vou criar uma pasta, agora de “receitas”, vou apertar a tecla “Enter”, e então, nós temos três pastas aqui.

[01:16] O que eu vou passar dentro de “receitas”? Vamos observar. Aqui nas “partials”, nós temos “partial” de “alertas.html”, de “busca.html”, do “footer.html” e do “menu.html”. Na “partial” de “receitas”, nós ainda não temos nada.

[01:28] Antes de vermos de usuários, vamos ver o “base.html”, que esse é o nosso código. Esse, nós podemos deixar aqui na raiz da nossa pasta de “templates”, mesmo. A busca – “buscar.html” - o que estamos buscando? Uma receita, então faz sentido nós o mantermos dentro de “receitas”. Pediu se eu quero mover, não quero perguntar de novo, pode mover.

[01:53] A busca, nós vamos manter aqui dentro de receitas. O “index.html” - que é a nossa página principal da aplicação, exibe o quê? Uma lista de receitas, então faz sentido mantermos esse nosso index de receitas aqui dentro, e a “receita.html”, dentro de “receita”. Essa, nós não temos nenhuma dúvida.

[02:11] Agora, o que vamos precisar fazer? Agora que alteramos o caminho dessas rotas, se formos na nossa aplicação e tentar atualizar, ele vai falar que o template não existe, então, o que eu tenho que fazer?

[02:22] Eu preciso alterar o local da página que eu quero renderizar. Eu não estou mais dentro na pasta “templates”, só digitando “buscar.html”, ou “index.html”. O que eu preciso colocar? Essa referência, “receitas/ buscar.html”, “receitas/index.html” e “receitas/receita”.

[02:43] Dentro do nosso app de receitas, vou vir em “views.py” e nós temos a nossa “index”. O “index”, vai estar dentro de “ 'receitas/index.html' “. A nossa função que exibe cada receita vai estar dentro de “ 'receitas/ receita.html' “ e a nossa função de busca, também. Buscar vai estar em “ 'receitas/buscar.html' ”.

[03:10] Se eu volto na nossa aplicação e atualizo, nós temos o nosso site aqui funcionando. Se eu clico na receita, ele exibe a receita e se eu quiser fazer uma busca, por exemplo: eu não lembro qual receita eu tenho na página principal. “Suco” e o “Bolo de chocolate”. Eu vou digitar: "suco." Exibiu o “Suco”, legal. Se eu digitar aqui "bolo," vai exibir o nosso “Bolo de chocolate”, maravilha.

[03:35] Para essa parte, para “views.py”, essas principais “views” de receita, parece que está tudo legal no nosso template. O que eu quero fazer? Agora, dentro de “usuarios”, vamos ver o que é relacionado com usuários e o que é relacionado com receitas. O “cadastro.html” de usuários. Legal.

[03:51] O “cria_receita.html”, ele não faz parte da responsabilidade de “receitas”, não é? Do nosso template de receitas. “dashboard.html”, do usuário, faz sentido. “edita_receita.html”, não, ele faz parte do escopo de receita, né?

[04:07] E aqui, nós temos o “login.html” de usuário, o “cadastro.html” de usuário e o “dashboard.html” do usuário. Legal. Vou fechar, aqui, a pasta “usuario”, quem vamos precisar alterar agora? Quem cria a receita e edita a receita, então, volto a colocar esses dois, também, vou fechar esses aqui.

[04:24] Observe que, na nossa “view.py” de receita, nós vamos precisar alterar algumas coisas, também porque temos aqueles campos de editar a receita e de atualizar a receita, eles não estão na “views.py” da receita, estão nas “views.py” de usuários. Nós vamos alterar isso nos próximos vídeos, também.

[04:42] Então, o que eu vou fazer? Aqui no nosso cadastro, “login”, “logout” e “dashboard” - isso referente ao “usuarios” – “def cria_receita(request) : ...” não é mais uma responsabilidade do nosso “usuarios/cria_receita”, vai ser responsabilidade "receitas/cria_receita”. Eu até vou copiar esse trecho aqui, só para nós alterarmos, para nós visualizarmos bem, então olhe: “cria_receita”, responsabilidade de “receitas/cria_receita”. Maravilha.

[05:11] Vamos ver da nossa outra parte. “def deleta_receita (request, receita_id):”, nós redirecionamos para o dashboard do usuário, está certo. “def edita_receita (request, receita_id):” – Opa! “usuarios", não. Não vai ser mais “ ‘usuarios/edita_receita.html’ ”. Vai ser o “receitas/edita_receita.html’ ”.

[05:25] Onde nós editamos vai ser as próprias receitas. “ def campo_vazio (campo) : ...”, “def atualiza_receita(request) : ...”, redireciona para dashboard, maravilha. Vamos ver se está certo?

[05:33] Se eu clico em "MINHAS RECEITAS" nós temos a “Sopa de mandioquinha” e se eu clicar em “Editar”, eu consigo editar. “Sopa de mandioquinha” evoluiu, versão 2.0. Clico em “Atualizar”, nós temos “Sopa de mandioquinha 2.0”, parece que está funcionando. "CRIAR RECEITA” está funcionando. Se eu venho em "MINHAS RECEITAS", todos os outros links, parecem que estão todos certos. Parece que está tudo maravilha.

[05:55] Então dessa forma, observe como nós alteramos a nossa pasta “templates”. Dentro da nossa pasta “templates”, nós temos três subpastas. Temos uma pasta só para “partials” da nossa aplicação, isso ficou bem legal, temos uma pasta de “receitas”, onde podemos buscar. Buscar o quê? Uma receita, “cria_receita.html”, “edita_receita.html”. A página “index.html” e a própria página que exibe a receita que nós queremos trabalhar, isso ficou legal.

[06:26] Na parte de “usuarios", nós ficamos com três templates: o template do “cadastro.html”, o do “dashboard.html” e o do “login.html”. Nós podemos até testá-lo, vou dar um “LOGOUT” aqui.

[06:34] Venho no cadastro. Maravilha. “LOGIN”. Vou realizar o login para vermos que está dando tudo certo: “gui@alura.com”, coloquei a minha senha. Agora sim, nós temos essa pasta dos nossos templates e a arquitetura dos nosso templates muito mais organizada.

[06:49] Na sequência, o que nós vamos fazer? Melhorar os arquivos das nossas “views”, tanto de “usuario” quanto de “receitas”.

### Refatorando as views

[00:00] Agora que melhoramos nossos templates, um ponto que podemos melhorar na nossa aplicação é o código das ““views.py””. Vamos dividir as responsabilidades para cada app.

[00:10] Para começar, vou abrir o app de “usuarios” em ““views.py”. O que eu tenho? Eu tenho o “def cadastro(request): ...” de usuários, - legal, isso faz sentido - tenho o “def login(request): ...)”, temos até as validações, os campos vazios, isso está legal. O “def logout(request): ...” faz parte de “usuarios” e o “def dashboard(request): ...” faz parte de “usuarios”.

[00:27] Agora, “def cria_receita(request):”? Isso não faz parte de usuário e “def deleta_receita(request, receita_id):” também não e “def edita_receita(request, receita_id):”, também não.

[00:33] Então, - deixe-me minimizar para conseguirmos visualizar bem - eu vou pegar esses três métodos, vou dar um “[COMMAND + X]”, vou tirar esses métodos daqui da ““views.py” de “usuarios” e vou mandar para a ““views.py” correta, a de “receitas”.

[00:48] Então, quem cria a receita, nós vamos encontrar esse código aqui na “view.py” de “receitas” – deixe-me ir minimizando - quem deleta receita, aqui na nossa ““views.py” de “receitas” e quem edita, também, na ““views.py” de “receitas”.

[01:00] Aqui em “usuario”, vamos ver. Quem atualiza a receita, - opa! Atualizar a receita também é uma responsabilidade da ““views.py” de “receitas”, então eu vou colocar "def atualiza_receita(request): ..."

[01:12] Quando eu salvo os dois campos, tanto na ““views.py” de “usuarios” quanto a “views.py” de receitas, nós podemos receber umas mensagens vermelhas. Por quê? Olhe só, eu vou abrir. Por exemplo, o “ def cria_receita(request): ...”. Nós não temos o “redirect” e o “User” importado para essa nossa “view”.

[01:37] Na nossa “views.py” de “receitas”, o que nós vamos fazer? Vamos fazer um “import” do “User”, - “[COMMAND + X]” - vou colocar aqui embaixo, - “[COMMAND + V]”, - o “import” de “User” - e nós temos aqui o “import render”, “get_list_or”, “object_4, get”. Vamos colocar a tecla “,” aqui e eu vou colocar o “redirect”.

[01:57] Fiz o “import” desses dois na “views.py” de “usuario”. Agora, nós vamos utilizar esses dois, nós enviamos mensagens, também. Vamos ver se nós estamos enviando mensagens na “receita” também, para garantirmos.

[02:10] Nós criamos uma receita, a receita foi salva, nós não estamos enviando mensagens, deletando as receitas também não e atualizando as receitas também não. Nós não estamos trabalhando com as mensagens na receita mas podemos colocar da seguinte forma: faço o “import” desse método para o nosso app de receita e consigo utilizar da mesma forma que utilizamos para os usuários – deixe-me minimizar esses dois, essas validações que nós criamos.

[02:38] Deixe-me voltar em campo, só para nós conseguirmos enxergar. Agora, sim. Agora, - deixe-me minimizar para nós vermos. - O que eu fiz? Olhe só: eu quero utilizar também as mensagens aqui na receita. Nós já temos a “partial” também, o que precisamos fazer? Incluir a “partial” nos templates que queremos. Nós já aprendemos a realizar isso, e depois do “import”, conseguir utilizar as mensagens para os nossos formulários conforme cada ação.

[03:12] Vamos testar para ver se a nossa aplicação está funcionando? Vou atualizar a página “index”. Vou colocar aqui “localhost:8000”. Quando atualiza, deu um erro. Por quê? Observe que nós colocamos a “view” no lugar certo mas como essa função, ou esse método é executado? Quando ele é executado?

[03:29] Ele é executado quando bate aquela URL e aquela URL fala "opa! Quem atende essa requisição aqui é esse método!" Nós não fizemos isso. Olhe só: nas URLs de “receitas”, nós só temos três paths: o path da nossa “index”, o que exibe a receita e o de busca. Nós não temos o path que edita, que atualiza, que estão onde? Estão no nosso app de usuário.

[03:56] Então, selecionando aqui em URLs, quem cria a receita, deleta a receita, todas essas funções, nós não vamos manter aqui. Eu vou tirar, salvar, vou deixar só o “path( ‘cadastro’...”, “path( ‘login’,...”, “path( ‘dashboard’,...” e o “path( ‘logout’,...”. Maravilha

[04:13] E no nosso URLs de receita no app de receita, nós vamos colocar uma tecla “,” e vamos usar as teclas “Ctrl + V” aqui - para essas nossas outras “views.py”, também.

[04:26] Dessa forma, parece que tudo está certo. Voltando na nossa aplicação. Agora sim, eu vou conseguir visualizar. Opa! Deixe-me ver o que eu fiz de errado, aqui. Ainda não. “views.py” de receita, “views.py” de “usuario”. Opa! Deixe-me salvar. Aqui, vou salvar.

[04:50] O nosso terminal não está rodando. Deixe-me rodar o terminal, senão fica difícil. "python manage.py runserver." Agora sim. Maravilha, estava executando o nosso terminal. Quando eu clicar para atualizar, ele vai atualizar.

[05:07] O erro que ele mostraria - que o meu terminal não estava atualizado - era que ele não encontrou o “template”, justamente por causa disso. Nós tínhamos um link, fizemos a requisição, falamos "quero ver o suco verde." Só que ele não ia abrir por quê?

[05:21] Porque, mesmo que nós tivéssemos, aqui na “views.py”, para exibir essa determinada receita, nós só conseguimos chegar e executar isso se no nosso “urlpatterns”, nós tivermos essa URL sendo direcionada para o método que nós queremos executar.

[05:39] Dessa forma, nós dividimos muito melhor a nossa aplicação, então se eu quiser buscar qualquer coisa relacionada a receita, a buscar receita, atualizar receita, eu não vou mais no app de usuários, eu vou no app de receita.

[05:49] E agora, se eu quiser algo relacionado com o dashboard do usuário, algo como o cadastro do usuário no login ou logout, eu já sei que eu preciso ir no app de usuários, então dessa forma, nós conseguimos manter o nosso código melhor.

[06:04] Repare que, à medida que o nosso código vai aumentando para o mantermos compreensível e manter cada coisa no seu lugar correto, vai garantir que nós consigamos sempre atualizar o nosso código, corrigir alguns erros, de forma muito mais fácil do que o nosso código todo espalhado e só nós sabendo mexer, que é um cenário ruim.

[06:31] É legal qualquer outra pessoa que falar "Ah! Eu preciso alterar a busca de receita." Então, ele já vai no “views.py” de “receitas”, e tem o método de busca. Vai ficar muito mais fácil.

### Modularizando as views

[00:00] Outro ponto que podemos melhorar ainda mais na nossa aplicação é modularizar as nossas “views”. Observe que a nossa “view” aqui do app de receitas possui muitas linhas e executa muitas coisas. O que podemos fazer é isolar alguns métodos para uma determinada “view”.

[00:18] Em outras palavras, o que eu quero dizer é: eu quero criar uma pasta de “views” dentro do meu app de receita onde cada “view” é responsável por uma determinada ação. Isso ficaria muito mais fácil para mantermos nossa aplicação.

[00:32] Então, a primeira coisa que eu quero fazer. Eu vou criar um folder novo, uma nova pasta, que eu vou chamar de “views”. Aqui dentro, eu vou manter todas as minhas “views”. Para começar, eu quero manter a minha “views.py” aqui dentro.

[00:44] Então eu vou pegar aqui, vou soltar aqui dentro e agora eu tenho, dentro da minha pasta de “views”, um arquivo chamado “views.py”. Só que esse arquivo está com um nome estranho, né? "views.py" não é um nome muito legal para a pasta de “views”.

[00:57] E ele deu uma outra mensagem, falou – opa! Dentro dessa pasta de “views”, eu não tenho nenhum arquivo com o nome “.models”. E faz sentido. Dentro de “views”, não tem nada. Porém, quando nós fazemos o “import” de “receitas.model”, nós temos esse arquivo funcionando. Ele consegue achar o nosso modelo de receita.

[01:19] O que eu quero fazer agora é alterar. Eu não quero chamar essa “views” de “views.py”. Eu quero chamar de "receita.py." Faz muito mais sentido. Dentro da minha “views”, do meu app de receita, eu tenho um “receita.py” para manter todo o nosso código.

[01:38] Porém, nossas URLs, o que nós fazemos? Nós fazemos um “import” assim: de onde nós estamos, queremos importar as “views”. Aqui, nós vamos mudar. nós vamos falar assim: "Das “views”, eu quero que você importe todas as coisas, importe tudo para mim."

[01:55] E aqui, vai ter uma alteração porque nós não vamos precisar mais referenciar as “views” porque – opa! Aqui faltou um “.”, desculpa, agora sim - aqui nós já estamos na pasta de “views”, ele já sabe que vai da “views” buscar o “index”, a receita.

[02:09] Então, eu vou usar as teclas “Ctrl + F”, chamar o “views”, eu quero substituir - vou dar aqui um “replace” - por nada, vou clicar nesse segundo ícone, o “Replace All” e ele vai substituir para mim.

[02:20] Quando eu salvo, ele vai dar uma mensagem de erro indicando que não vai conseguir encontrar o “index”, a “receita”, o “buscar”. Por quê? Por mais que nós tenhamos referenciado o nosso arquivo aqui dentro de “views”, é necessário que nós coloquemos um inicializador nessa nossa pasta de “views”.

[02:38] Então o que eu vou fazer? Eu vou criar um arquivo novo e vou colocar. Aqui, eu vou chamar de “init.py”. Dentro desse arquivo, – deixe-me fechar esse - aqui na pasta de “views”, o que eu quero fazer? Eu quero que ele consiga carregar a minha “receita.py”.

[03:01] Então o que eu preciso fazer é "from .receita import" e eu quero importar todas as coisas que estão dentro dessa minha “”receita.py”. Eu vou salvar, volto em URL. Quando eu salvo, o erro não é acusado mais, nós conseguimos criar uma “view” chamada “receita.py” para ser atendida aqui.

[03:27] Observe que a abstração do nosso código está ficando um pouco melhor, um pouco mais organizada, então, dentro do nosso app de receitas, nós temos uma “view” chamada “receitas.py”, e aqui dentro, nós temos os nossos métodos de receita.

[03:42] Mas e se eu quiser criar um novo método? Por exemplo, esse “def buscar(request):” aqui. Eu quero alterar o nome. Eu vou chamar de “def busca(request):, então, alterei para busca. Na minha URL, eu vou chamar também de “busca”. Agora, eu não tenho mais esse erro.

[03:59] Quando eu atualizar, ele deu até um “if buscar”. Nós podemos refaturar esse nosso código da busca aqui. Se tivermos alguma coisa na requisição para buscar, ele vai pegar o que está nessa requisição e vai nos trazer a lista das receitas que queremos exibir.

[04:16] Salvei. Deixe-me garantir que o meu terminal está sendo executado. Está sendo executado. Voltando na nossa aplicação, observe que tudo está funcionando. O “Suco verde” está exibindo o suco verde. Voltar no “Alura Receita”, o “Bolo de chocolate” está exibindo o bolo de chocolate. Maravilha.

[04:30] Se eu fizer uma busca por “suco”, eu consigo visualizar o “Suco verde”. Se eu fizer uma busca por “bolo”, eu consigo visualizar o ‘Bolo de chocolate”. Isso ficou legal. Só que eu quero fazer algo a mais. Eu quero colocar esse código de busca - que não é necessariamente ligado ao nosso app de receitas, seria legal se ele estivesse em outro lugar, se tivesse uma “view” só para essa nossa função de busca de receita.

[04:56] O que eu vou fazer? Eu vou usar as teclas “Ctrl + X”, vou apertar a tecla “Enter” duas vezes aqui, - é só salvar - e vou criar uma nova “view”. Eu tenho uma “view” aqui de receita, vou criar uma nova “view” que eu vou chamar de "busca.py"

[05:11] Nessa minha “view” de “busca.py”, eu vou fazer alguns “imports” e vou ter o código que faz a busca, de fato, então, o que eu preciso fazer? No nosso “init.py”, eu vou também realizar - aqui, eu quero também buscar.

[05:30] Então, quero buscar no “busca” todos os métodos que eu tenho aqui dentro. Eu vou chamar assim "import *”, Então, "from .busca import". Tudo o que está dentro de busca, eu quero que você importe para mim.

[05:45] Trouxe a busca para cá, o que eu preciso agora na busca é fazer os “imports” necessários para a nossa busca continuar funcionando, então, em “receita.py”, o que nós temos? Nós temos o “from receitas.models”, vamos precisar também do modelo de receita na nossa busca e precisamos também do “render” e do “redirect”. Vou copiar essa primeira linha aqui, vou voltar na nossa busca, apertar as teclas “Enter” e “Ctrl + V”, e Colei.

[06:11] Agora sim, eu tenho essa busca. Aqui no “init.py”, eu salvei. No nosso “urls.py”, o que eu vou fazer? Deixe-me usar as teclas “Ctrl + V”, só para visualizarmos melhor. Observe que, no nosso “urls.py”, nós não vamos alterar mais nada. Nós já temos a nossa busca funcionando e ele já sabe que esse método já existe, ele já buscou aqui para nós. Ele consegue encontrar.

[06:35] Assim que eu salvo, voltando para a nossa aplicação, quando eu clico aqui tudo está funcionando. “Bolo de chocolate”. Está funcionando o “Bolo de chocolate”. Vou fazer uma busca por “suco”. Pesquisar aqui, “Suco verde”. Quando eu aperto a tecla “Enter”, eu consigo visualizar.

[06:48] Então olhe só que legal o que nós fizemos: nós criamos uma pasta para manter todas as nossas “views”. Dentro dessa pasta, nós conseguimos dividir quais metas queremos em cada “view”.

[07:05] Então nós criamos uma “view” chamada “receita.py”. Dentro dessa receita, nós temos o “index”, a receita, a criação da receita, a edição da receita e isso ficou bem legal. Nós também isolamos dentro desse nosso “busca.py” só o método de busca, e para que nós consigamos referenciar esses métodos em “urls.py”, o que nós fizemos?

[07:28] Dentro de “views”, traga tudo. Ele vai ver aqui "Opa! Dentro de “views” eu tenho “init.py”. O que eu preciso trazer? Traz todas as receitas e todas as buscas”. Assim, nós garantimos que o nosso código está funcionando.

[07:39] Posso fazer o login para nós testarmos aqui dentro também com o usuário logado: “gui@alura.com”, “123”. - Opa! Falei a minha senha, não posso falar a minha senha! - Agora, sim. “PÁGINA PRINCIPAL”, as receitas estão funcionando. Eu posso navegar, olhe: “Bolo de chocolate” ou “Suco verde”, legal. Está tudo funcionando.

[07:56] Se eu venho aqui nas “MINHAS RECEITAS”, eu tenho a “Sopa de mandioquinha”, posso visualizar a “Sopa de mandioquinha”, uma receita que só eu tenho acesso porque é uma receita que eu criei, não está publicada para o site. Posso editar. Todos os outros links estão funcionando.

[08:09] Qual é a vantagem de nós utilizarmos o nosso código fragmentado, igual fizemos aqui modularizado em várias “views”? Nós isolamos a nossa aplicação. Observe que se alguém precisar alterar alguma busca do nosso app de receita, assim que a pessoa abre o app de receita, nós temos uma pasta de “views” e tem aqui “busca.py”, que é ter um método da busca.

[08:34] Ou aqui em “urls.py” - "Ah! “uero alterar algo da URL, passar alguma coisa" - está muito mais fácil de identificar: "Opa! Tem alguém em “busca.py” que é capaz de alterar."

[08:45] Então nós melhoramos o código da nossa busca, o modularizamos para uma determinada “view”, - uma específica só para realizar a busca – isolamos, também, a “receita.py”, e assim, conseguimos trabalhar com mais de uma “view” dentro de um app. Isso ficou bem legal.

### Mantendo o código organizado

Melhoramos a distribuição do código, modularizando e alinhando a arquitetura da aplicação, tanto nos templates como no app de receitas.

Sabendo disso e considerando que estamos usando o Django, podemos afirmar que:

a) Alternativa correta: É possível ter mais de uma model por app.
- _Certo! Da mesma forma que trabalhamos com mais de uma view, podemos também trabalhar com mais de um model por app._

b) Não é possível ter mais de uma view por app.

c) Alternativa correta: É possível ter mais de uma view por app.
- _Certo! Podemos dividir os métodos de uma view em vários arquivos dentro do mesmo app._

### O que aprendemos?
## 04. Paginação no Django
### Preparando o ambiente
### Importando Paginator
### Preparando o ambiente
### Paginação no template
### Faça como eu fiz na aula
### Django paginator
### Para saber mais: Admin link
### O que aprendemos?
## 05. Refatoração de código
### Pasta apps e docstring
### Faça como eu fiz na aula
### Boa qualidade de código
### O que aprendemos?
### Conclusão
### Parabéns
### Logo da alura
### SOBRE A ALURA
### DÚVIDAS FREQUENTES
### SUGIRA UM CURSO
### SUGIRA UMA FUNCIONALIDADE



