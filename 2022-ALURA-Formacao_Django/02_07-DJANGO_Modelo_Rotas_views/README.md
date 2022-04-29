# Introdução ao Django: Modelo, Rotas e Views
**Fonte:** Guilherme LIma<br>
**Disponível:** <a href="https://cursos.alura.com.br/course/fundamentos-django-2" target=_blank>ALURA</a><br>
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

- Passo a passo para instalar o Python3 no Windows. <a href="https://cursos.alura.com.br/course/python-3-introducao-a-nova-versao-da-linguagem/task/22687" target=_blank>aqui</a>
- Passo a passo para instalar em outros sistemas operacionais.<a href="https://cursos.alura.com.br/course/python-3-introducao-a-nova-versao-da-linguagem/task/22688" target=_blank> aqui</a>

Além disso, para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

- <a href="https://www.python.org/downloads/release/python-374/" target=_blank>Python 3.7.4</a>
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

Aplicações Django devem usar o mínimo possível de código; elas não devem ter código padrão. Django deve aproveitar as características dinâmicas do Python, como <a href="https://pt.wikipedia.org/wiki/Introspec%C3%A7%C3%A3o_%28computa%C3%A7%C3%A3o%29" target=_blank>introspecção</a>.

Caso queira saber mais sobre filosofia do Django:

- <a href="https://docs.djangoproject.com/pt-br/2.2/misc/design-philosophies/" target=_blank>Filosofia do Django segundo a documentação oficial</a>

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

### O que aprendemos?
## 03. Links, extends e partials
### Links, urls e views
### Estendendo html
### Partials
### Faça como eu fiz na aula
### Extends, include e partials
### O que aprendemos?
## 04. Modelo e banco de dados
### Nomes de receitas dinâmicas
### Banco de dados
### Psycopg2
### Modelo de receita
### Faça como eu fiz na aula
### {{ }} e {% %}
### Models no Django
### makemigration e migrate
### Para saber mais: Models
### O que aprendemos?
## 05. Admin, parâmetros e receitas
### Django Admin
### Exibindo dados dos banco
### Parâmetro na url
### Faça como eu fiz na aula
### Ajudando alguém
### Para saber mais
### O que aprendemos?
## Conclusão
