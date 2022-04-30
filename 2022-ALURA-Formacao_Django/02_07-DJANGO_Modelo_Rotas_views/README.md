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
