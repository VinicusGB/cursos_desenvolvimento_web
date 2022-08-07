# Formulários no Django 3: criando e validando dados - 8h
**Instrutor:** Guilherme Lima \
**Disponível em:** [ALURA]('https://cursos.alura.com.br/course/django-validando-formularios') \
**Conteúdo:**
 - Aprenda validar os dados de um formulário com Django;
 - Saiba como criar um formulário baseado em modelos;
 - Desenvolva na prática, um projeto com as principais convenções do Django e boas práticas de programação;
 - Entenda como trabalhar com diferentes tipos de campos em um formulário
 - Melhore a experiência dos usuários do seu site, enviando mensagens de ajuda

## **Aulas:**
### 1. Formulário com Django Forms Ver primeiro vídeo
#### Introdução

[00:00] Olá, meu nome é Guilherme Lima, e eu serei o seu instrutor neste curso de Formulários com Django. Neste curso, o que vamos aprender?

[00:07] Nós vamos aprender como gerar formulários com Django, respeitando as principais convenções e seguindo as boas práticas de programação. Vamos criar validações deste formulário e vamos ver como criamos as validações.

[00:18] Vamos trabalhar também com “ModelForm”. Eu tenho o modelo, como eu gero um formulário a partir deste modelo?

[00:23] Fazendo esse curso nós vamos criar essa aplicação aqui. Essa aplicação é um exemplo de um formulário onde nós vamos colocar alguns campos, como: origem, destino, data de ida e data de volta.

[00:34] Vamos pesquisar quais sãos os preços mais em conta desse trecho, dessa viagem que eu estou colocando aqui. Caso o formulário seja válido, nós vamos para essa página onde visualizamos os dados dessa informação.

[00:47] Caso o formulário tenha alguma informação que não seja correta, por exemplo: aqui no lugar de “São Paulo”, eu vou colocar um “São Paul0”. Coloquei um caractere numérico, se eu dou um “OK”, ele vai incluir uma validação. “Não inclua números neste campo”, então eu vou colocar aqui o “O”, por exemplo.

[01:03] Se eu coloco “São Paulo” e aqui embaixo eu também coloco “São Paulo”, então eu estou em São Paulo e quero viajar para São Paulo também, não posso. Origem e destino não podem ser iguais, então eu volto. Deixe-me colocar “Rio de Janeiro”.

[01:16] Ou, eu quero visualizar uma viagem para ontem, então eu quero viajar ontem e voltar no dia 11. Se eu clico em “OK” aqui, ele vai falar: “Data de ida não pode ser menor do que hoje”, então nós precisamos alterar isso também. Então vamos arrumar! Se o nosso formulário for válido, se tudo estiver certo, nós visualizamos essa página.

[01:33] Nós vamos criar tudo isso respeitando as principais convenções do Django e seguindo as principais convenções também de boas práticas de programação. Legal!

[01:46] Quais são os pré requisitos para esse curso? É muito importante que as pessoas que vão realizar esse curso já tenham visto os cursos anteriores da plataforma, porque assim nós teremos um caminho, uma sequência melhor.

[01:58] “Ah! Eu não fiz os cursos anteriores, eu posso realizar esse curso?” Você pode, mas é recomendado que você tenha visto os cursos anteriores de Django da plataforma.

[02:07] Então, para quem é esse curso? Se você está criando as suas primeiras aplicações com o Django e vai trabalhar com formulário, esse curso é muito importante para você.

[02:17] Se você já fez os outros cursos da plataforma de Django e quer aprofundar os seus conhecimentos, esse curso também é importante para você.

[02:23] Se você é um expert de Django, se você já trabalha muito tempo com esse framework, talvez esse curso não seja tão recomendado para você.

[02:32] Sabendo de tudo isso, vamos começar?

#### Saudações e ambiente

É muito bom receber você neste curso de Django.

Espero que seja uma experiência de aprendizado incrível e que possamos vencer todos os desafios juntos. Neste curso, vamos aprofundar nosso conhecimento utilizando o Django, trabalhando com formulários, seguindo as principais convenções do framework e boas práticas de programação.

Este curso, apesar de ser o quinto curso de Django, não é uma continuação do projeto desenvolvido nas partes anteriores. Porém, é importante que você tenha uma base de conhecimento passado nos cursos anteriores.

##### Divisão das aulas
Aula                               | O que vamos aprender?
Formulário com Django Forms        | Vamos criar um formulário baseado na classe Forms do Django
Alterando e manipulando dados      | Vamos aprender como manipular ou recuperar os dados de um formulário
Novos campos                       | Vamos criar campos para o formulário de diferentes tipos
Validações                         | Vamos aprender como incluir validar os dados de um formulário
Modelos e formulários              | Vamos criar um formulário baseado em um modelo

##### Preparando ambiente
Além disso, para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

    Python 3.7.4
    Django 3.0.3

O Django pode ser instalado através do comando:

    pip install Django==3.0.3COPIAR CÓDIGO

Para otimizar o tempo do curso, criamos esta atividade descrevendo o passo a passo para criação de um projeto Django. Os passos são:git

Crie uma pasta para manter seu código e acessando essa pasta em um terminal, crie um ambiente virtual com o seguinte comando:

    python3 -m venv ./venv

Ative seu ambiente virtual com o seguinte comando (MAC e Linux):

    source venv/bin/activate

Em caso de Windows, utilize o comando:

    venv\Scripts\activate.bat

Instale o Django nesse ambiente virtualizado:
    
    pip install django

Crie um projeto chamado setup utilizando o Django admin, para manter toda configuração de nossa aplicação:

    django-admin startproject setup .

Na pasta setup, altere no arquivo settings.py o idioma e o horário que usaremos na aplicação, incluindo as seguintes linhas de código:

    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'

No início do arquivo, adicione a importação da biblioteca os para trabalhar com os diretórios do sistema:

    import os

Para finalizar a configuração do ambiente, vamos configurar um diretório para manter os arquivos HTML incluindo a seguinte linha de código em TEMPLATES(não esqueça de criar a pasta template):

    'DIRS': [os.path.join(BASE_DIR, 'templates')],

Em caso de dúvida na instalação ou durante o curso, conte sempre com o fórum da Alura!

Vamos começar?

:)

#### Iniciando a aplicação

[00:00] Vamos iniciar então o desenvolvimento da nossa aplicação e aprender como trabalhamos com formulários aqui no Django?

[00:06] Para começarmos, na atividade anterior nós temos um passo a passo descrevendo como você instala o Django, cria um ambiente virtual e coisas que já vimos nos cursos de pré-requisitos. Legal!

[00:18] Então já fizemos algumas configurações, eu vou apertar aqui as teclas “Command + J”, o meu servidor já está rodando. Aqui em “settings.py” nós fizemos algumas configurações, dizemos que nós vamos manter todas as nossas páginas HTML nesse diretório de templates. Mudamos também o “LANGUAGE_CODE” para o português do Brasil, e o “TIME_ZONE” para a “America/Sao_Paulo”. Legal!

[00:44] Já fizemos essas configurações. Quando subimos a nossa aplicação e acessamos aqui a página principal da nossa aplicação temos essa “A instalação foi com sucesso! Parabéns!” Não é o que queremos mostrar, eu quero criar um site de busca de pesquisas de viagens mais em conta.

[01:01] Então eu quero colocar um campo de origem, um campo de destino, um campo de data de ida e data de volta, algumas informações e a classe da viagem que vamos utilizar; e quando dermos um “OK”, caso as informações desse formulário sejam válidas, eu quero exibir essas informações em uma outra tela, em um outro visual.

[01:21] Caso tenha algum campo que esteja errado, alguma validação ali que não passe, eu quero exibir uma mensagem de erro. Tudo isso nós vamos aprender no decorrer desse curso, pensando sempre na velocidade e nas principais convenções do Django para criarmos esse nosso formulário.

[01:38] Para começarmos, como eu não quero exibir essa tela, eu quero exibir uma tela com o meu formulário de passagens, então nós vamos criar esse formulário juntos. Eu vou abrir aqui o meu terminal. Teclas “Command + J”, no terminal 1 eu vou deixar rodando o meu servidor, e vou abrir um segundo terminal. Observe que eu estou com a “(venv)” ativada.

[01:57] O que eu quero fazer agora é criar um app para manter todas as informações relacionadas às passagens, então eu vou digitar assim: “python manage.py startapp” e eu vou criar um app para manter as minhas passagens.

[02:14] Criei o app. Esse app, se visualizarmos com as teclas “Command + J” para o “Command + B” para abrir aqui do lado, temos aqui agora uma parte de passagens. O que eu tenho que fazer?

[02:24] Para de fato utilizar esse app aqui dentro da nossa aplicação, eu preciso ir lá em “setup” e dizer que eu vou utilizar esse app na aplicação. Nos apps instalados, eu vou dizer que eu também vou usar o app de passagens. Vou apertar aqui a tecla “,” e vou salvar. Agora sim, nós temos esse app de passagens.

[02:49] Outra coisa que nós queremos fazer também: assim que acessamos essa URL, eu não quero exibir essa tela, eu quero exibir a tela relacionada com o app de passagens. Então aqui em “urls.py”, eu vou mudar. Ele já tem um “path” para o “admin”, esses nós vamos manter.

[03:05] Eu vou criar um novo “path”, vou chamar aqui de “path()”. Esse novo “path”, eu quero que o “localhost”, esse local aqui. Nós percebemos que estamos no “localrost8000”. Não passamos nenhuma informação, e é justamente o que queremos. Eu quero que a rota principal da minha aplicação seja relacionada com as rotas que eu tenho lá no “passagens.urls”.

[03:26] Então eu vou colocar aqui um “include('passagens.urls')”. Vou salvar, vou colocar aqui uma “,” também. Salvei. Observe que quando eu salvo, ele fala que essa variável “include”, não foi encontrada porque precisamos trazê-la também. Na linha que trazemos o nosso “path” eu vou fazer um “import” do “include” também. Quando eu salvo, o erro desaparece.

[03:55] O que eu vou fazer agora? Lá no meu app de passagens... Deixe-me fechar esses dois para não confundirmos. Aqui no meu app de passagens, observe que eu não tenho um arquivo para manter as URLs da minha aplicação. Eu vou criar esse arquivo aqui agora também.

[04:15] Então aqui no app de passagens eu vou criar um arquivo que vou chamar de “urls.py”, e dentro do “urls.py” eu vou importar do “django.urls”. Então, “from django.urls import path”, que é o que vamos utilizar. Aqui dentro do URLs eu vou colocar aqui que a “urlpatterns = [ “, onde eu vou manter todos os “paths” desse meu app de passagens.

[04:55] Então, quando eu tiver uma requisição para a minha página principal, eu quero de alguma forma conseguir visualizar uma página. Para isso, eu vou precisar criar uma “view” que vai conseguir direcionar qual é a página HTML que queremos renderizar. Para isso, temos que importar.

[05:19] Olhe só, ele falou aqui que a segunda propriedade é lá de “view”, e vamos ter que importar essa classe também. Então eu vou fazer aqui: “from.import views”. Importe tudo de “views”. Aqui eu vou trazer lá de “views”. Vou criar um método que eu vou chamar de “index” e vou dar o “name” dele também de “index”.

[05:47] Vou salvar. Ele vai marcar essa linha do “views” porque no meu módulo de “view” eu não tenho ninguém que se chama “index”, então lá em “views” nós vamos criar a nossa primeira função, o nosso primeiro método.

[06:03] Então, “def”. A nossa primeira função eu vou chamar aqui de “index”, e eu quero retornar, eu quero renderizar alguma página, então eu vou dar um “return render”, eu quero renderizar. Eu vou devolver o “request”, que é o que ele pede como primeiro argumento. O segundo argumento é a página. Que página eu quero exibir? Nós não criamos ainda.

[06:30] Eu vou criar, vou chamar a página de “index.html”. Isso precisa ser uma “streaming”, então eu vou colocar aqui “index.html”. Vou salvar, volto em “urls.py” e salvo. O erro desaparece.

[06:43] Só que agora nós temos um erro aqui no “views”. Aqui o “request” deu como que não encontramos esse parâmetro. Por quê? Eu esqueci de passar esse parâmetro aqui como argumento, nós temos do “index” ao “request”. Agora sim!

[06:58] O que eu preciso fazer agora é de fato criar essa página “index”, então essa página “index” e todas as páginas HTMLs, segundo a configuração que fizemos, vai ficar aqui nesse “folder” de “template”. Então eu vou chamar aqui de “index.html”. Se eu dou aqui um “html”, esse “html :5”, observe que ele já traz bastante coisas legais.

[07:23] Para dar o título vai ser “Passagem” e aqui eu vou colocar um `“”`, que eu vou chamar de “Passagem”, só para nós conseguirmos visualizar. Salvei. Se eu volto na minha aplicação e atualizo, ele dá uma mensagem de erro. Se abrirmos o nosso terminal, observe que criamos um app, nós não reinicializamos o nosso terminal, ele não está encontrando esse nosso app de passagens.
[07:48] Se eu fechar o meu servidor, parar o meu servidor com as teclas “Ctrl + C”. Vou limpar a tela aqui com as teclas “Ctrl + V” e vou dar mais uma vez “python manage.py runserver” e atualizar a minha página. Observe que temos lá escrito “Passagem”.

[08:08] É um começo, está melhor do que estava antes, só que o que eu quero exibir de fato é um formulário, eu não quero ter aqui só o texto de Passagem. É isso que nós vamos começar a fazer na próxima aula!

#### Django Form

[Class forms]('https://docs.djangoproject.com/pt-br/4.0/topics/forms/')

Para facilitar a validação de dados de formulários o Django possui a `class forms` que automatiza boa parte dos processos de validações de forms html.

1. Na pasta do app (passagens) cria um arquivo: `forms.py`
2. Em `forms.py`:

        from django import forms
        
        class PassagemForms(forms.Form):
            origem = forms.CharField(label='Origem',max_length=100)
            destino = forms.CharField(label='Destino',max_length=100)
    

3. Em 'views.py', fazemos o import do nossa `class form PassagemForms` e passamos como parâmetro para o render:

        ...
        from passagens.forms import PassagemForms
        
        def index(request):
            form = PassagemForms()
            contexto = {'form':form}
            return render(request,'index.html',contexto)

4. Em 'index.html', devemos apenas passar a variável 'form' passada por parâmetro na minha requisição:
        
            ...
            <body>
                <h1>Passagens</h1>
                {{ form }}
            </body>

---

[00:00] Manipular um formulário não é uma tarefa tão simples. Um formulário precisa ser renderizado em um template, ou seja, precisamos visualizar esse formulário para o cliente que fez a requisição da nossa página.

[00:12] Outra coisa: precisamos utilizar uma interface prática. O nosso formulário tem que ser claro, os dados que estão sendo pedidos, e precisamos validar esses campos, limpar os campos. Não podemos simplesmente pegar as informações que estão no formulário e salvar no banco de dados, ou realizar um outro processo adicional, ou manipular os recursos de forma diferente.

[00:33] Precisamos retornar a requisição ao servidor, para que os dados sejam salvos ou encaminhados para um outro tipo de recurso que temos na nossa aplicação.

[00:43] Pensando nisso, o Django tem uma forma para simplificarmos todas essas tarefas e automatizarmos grande parte desse trabalho, então o Django lida com três partes distintas.

[00:55] A primeira parte é: quais são os dados que queremos renderizar aqui na nossa aplicação. Depois ele nos cria aqui no HTML o nosso formulário. Terceiro: ele também recebe e processa os dados enviados por esse formulário de uma forma muito mais prática, de uma forma muito mais simples.

[01:15] Fazendo uma analogia com base no conhecimento que já temos dos outros cursos de Django. Lembra que tínhamos um objeto que relacionava uma tabela na nossa base de dados? Então, os campos de uma classe, do nosso modelo por exemplo, eram mapeados para serem os campos do banco de dados, e uma classe era mapeada para ser uma tabela na nossa base de dados.

[01:41] Falando de formulários, existe uma classe no Django que vai fazer algo semelhante, só que cada “imput” no nosso formulário vai ser representado também por um campo, e cada formulário vai ser representado também por uma classe. Isso vai ficar muito legal para trabalharmos.

[01:57] Então temos uma abstração do modelo com o banco de dados e agora temos uma abstração do formulário com a nossa página HTML. Então para renderizarmos, o que nós vamos precisar fazer?

[02:11] Vamos recuperar os dados da “view”, precisamos indicar lá na nossa “view” que nós temos um formulário para ser renderizado nesta página. Isso nós vamos fazer também. Precisamos exibir esse dado lá na nossa “index.html”, de alguma forma temos que falar: “Django, gere para mim o formulário” e ele vai nos gerar o formulário.

[02:30] Legal! Tudo isso parece muito mágico, parece muito legal, mas eu quero de fato criar esse formulário. É isso o que nós vamos fazer agora!

[02:36] Para começar, eu vou fechar essas telas aqui. Depois nós vamos abrindo conforme formos precisando. Aqui em “passagens.py” eu tenho uma série de arquivos. Tem os arquivos aqui do “admin.py”, os arquivos relacionados ao meu app, “models.py”, “urls.py”, e “views.py”.

[02:53] O que eu quero fazer agora é criar uma classe que vai ser responsável por manter todos os dados do meu formulário, então eu vou criar uma classe que eu vou chamar de “forms.py”. Esse “forms.py” eu vou precisar importar lá do Django, indicando que eu vou utilizar a classe “forms” aqui dentro desse meu “forms.py”.

[03:17] Então eu vou fazer assim: lá do meu Django, “from django import forms”, eu quero importar o “forms”. Maravilha!

[03:30] Então para começarmos, com base na analogia temos um modelo que representa algo no banco de dados, aqui nós vamos ter uma classe que vai representar um formulário lá no nosso HTML. Então ele vai ser representado também por uma classe. Essa classe vai ser o nome do nosso formulário, eu vou chamar de “passagemForms”. Legal!

[03:50] O “passafewmForms” vai receber como argumento lá do nosso “forms” o tipo “(forms.form)”. Agora sim!

[04:02] Aqui vai chegar o ponto mágico! O que vai acontecer? Cada campo do meu formulário, aqui dessa minha classe, ele vai ser representado como “imput”, lá no meu HTML. Então eu vou colocar alguns “imputs”. Eu vou colocar a origem, a origem vai ser do tipo “forms.charfield”. O que isso significa?

[04:24] Significa que eu vou poder escrever lá no meu “imput”, na minha caixa de “imput”, eu vou poder escrever uma “streaming”, uma sequência de números, e vou dar uma “label” para ele também. Ele tem aqui um argumento chamado “label”, eu vou chamar essa “label” de “Origem”. Legal!

[04:42] E eu posso passar algumas propriedades também. Por exemplo: eu vou falar que o máximo de caracteres que eu quero para esse meu campo de origem é de 100 caracteres.

[04:51] Além disso, eu vou querer o destino, “destino = forms”. Vou dar a mesma propriedade, “.Charfield”. Vou dar ali “buld” “Destino”, e vou chamar aqui a propriedade “max_length=100”. Legal! Criei esses meus dois campos aqui, eu tenho um campo de origem e tenho um campo de destino. Conforme o decorrer do curso nós vamos inserindo outros campos de tipos diferentes para visualizarmos também.

[05:23] Agora que eu criei essas minhas duas propriedades, o que eu preciso fazer? O que eu preciso fazer agora é aqui na minha “view”, eu preciso importar. Observe que eu só tenho o “render” aqui importado, então eu quero trazer esse meu “forms” aqui para a minha “view”. Como eu faço isso?

[05:36] Eu faço da seguinte forma: eu quero importar lá do meu “passagens.forms”, eu quero importar a nossa classe “PassagemForms”, então: “from passagemForms import PassagemForms”.

[05:52] O que eu preciso fazer agora? Eu vou indicar da seguinte forma: eu vou falar que o “form” vai ser do tipo “PassagemForms”. Eu vou deixar ele assim, vai ser um tipo “PassagemForms”.

[06:02] E nós aprendemos nos cursos anteriores que podemos passar algo para ser exibido aqui na nossa página através de contexto, então eu vou chamar aqui uma variável de contexto e vou falar que essa minha variável de contexto vai ser abrindo “{“.

[06:20] Ela vai ter uma propriedade chamada “form” e ela vai ser do tipo “form”, do tipo do nosso “form” ali. Para eu conseguir passar esse meu formulário com contexto, eu vou passar com um terceiro parâmetro. Ele até fala “contexto”, então eu vou passar aqui o “contexto”. Maravilha!

[06:43] Então nós criamos uma variável de contexto e encapsulamos essa variável aqui no nosso método “index”. O que eu preciso fazer agora? Vou minimizar aqui, lá no meu template “index.py”, eu quero exibir de fato esse “forms.py” lá na nossa aplicação. Para isso, o que eu vou fazer?

[07:02] Eu vou tomar o seguinte: nós temos aqui o nosso “Passagem” que é o “

” e vou colocar aqui com duas “{{}}”. Vou passar aqui o meu “form” e vou salvar. Quando eu volto na minha aplicação e atualizo, observe que agora eu tenho o “Origem” e tenho o “Destino”. Isso ficou legal.
[07:23] Em nenhum momento eu escrevi código HTML para criar esses dois campos. Mas e se eu quiser criar mais um campo? Por exemplo: aqui no meu “form” eu quero criar mais dois campos, por exemplo. Eu tenho o campo de “Origem” e tenho o campo de “Destino”, eu quero a data da ida e a data da volta. Então eu vou criar mais esses dois campos.

[07:40] Eu vou colocar aqui “data_ida”, então eu vou usar aqui da propriedade “forms”, o “DateField”, é uma data, eu quero usá-la. Eu vou deixar a “label” dele escrita como “Ida”. Vou criar a “data_volta”, e vou usar lá do “forms.DateField(label='Volta')”. Salvei, volto na minha aplicação, atualizo e nós temos mais dois campos, temos aqui o campo de ida e o campo de volta.

[08:19] Isso ficou legal, observe que a nossa aplicação não está ficando bonita. Nós vamos aprender como continuamos mantendo esse pouco código. Observe que da forma que fizemos aqui, passando o formulário por contexto e indicando apenas aqui no nosso HTML que temos o “form”, que lá dentro do contexto tem uma tag “form”, nós conseguimos criar esses quatro campos aqui, de origem, de destino, de ida e de volta.

[08:47] O que nós vamos fazer na sequência? Observe que nesse meu campo de “Origem” eu posso escrever aqui. Então eu vou escrever, por exemplo: “São Paulo”. O meu destino vai ser “Rio de Janeiro”. Eu vou no dia “10/06/2020” e vou voltar no dia “12/06/2020”. Nós não temos nenhum botão ainda para submetermos esse formulário.

[09:12] É o que vamos aprender nos próximos vídeos, além de deixar o nosso formulário com um visual um pouco mais bonito, sem dar tanta ênfase para o CSS e para o HTML. Nós vamos deixar o visual dele um pouco melhor, um pouco mais agradável para conseguirmos trabalhar, pensando nessa forma, de como nós conseguimos otimizar o nosso tempo para gerarmos um formulário bem legal.

#### Melhorando o visual

Utilizando BOOTSTRAP através do CDN na tag `<head>` do index.html

---

[00:00] Criamos o nosso formulário, só que ele está com um visual que não está bonito. Vamos melhorar o visual da nossa aplicação?

[00:05] Então eu vou utilizar o Bootstrap. Vou escrever aqui “bootstrap”. Clicando aqui nesse primeiro link, nós vamos fazer download do Bootstrap. Eu vou clicar aqui em “Download” nós e vamos utilizar ele via “CDN”, ou seja, eu vou colocar um link na nossa aplicação e nós vamos conseguir utilizar as classes do Bootstrap no nosso site.

[00:24] Então eu vou clicar aqui “Copy”. Copiei. Vou vir aqui na nossa aplicação, lá no nosso template, na nossa “index.html”. Deixe-me minimizar esses dados para nós visualizarmos melhor. No “title” eu vou apertar a tecla “Enter”, que é o texto que aparece o “title”, que está aparecendo aqui em cima “Passagem”.

[00:44] E vou apertar as teclas “Ctrl + V” para copiar aqueles dois links aqui para a nossa aplicação. Ele copiou esses dois links, assim que eu salvo e volto. Vou fechar o Bootstrap porque nós não vamos precisar mais. Quando eu atualizar observe que o visual já mudou.

[00:57] O que eu quero fazer é colocar um botão aqui, de “OK”, para a pessoa submeter os dados desse formulário. Para isso, eu vou utilizar aqui a tag do HTML “input”. Aqui em “input” ele fala o “type” que eu quero utilizar. Eu vou colocar “submit” e vou passar um “value” também para ele, um valor. O que vai estar escrito neste botão?

[01:21] Eu quero escrever nesse botão “Ok”. Assim que eu salvo volto lá e atualizo, aparece aqui um “Ok”, só que ele está estranho. Eu escrevi “submit” errado, então vou escrever tudo de novo, “submit”. Agora sim, escrevi “submit” certo e vamos ver um botão.

[01:35] Só que podemos usar as classes do Bootstrap para deixar esse botão melhor. Eu vou utilizar aqui uma classe do Bootstrap, eu vou utilizar “btn btn-success”. Salvando, voltando aqui vou dar um “OK”. Nós vamos ter um botão verde, isso ficou bem legal.

[01:53] Observe que a margem da nossa aplicação também está um pouco estranha, nós vamos melhorar a margem do nosso código também.

[02:00] Então, o que nós podemos fazer? Eu posso colocar toda essa informação dentro de uma seção, e essa seção possuir uma classe “container” para visualizarmos melhor. Então eu vou criar aqui uma “

”, vou colar e vou tirar isso aqui com as teclas “Ctrl + X”, ou “Command + X” se você estiver no Mac.
[02:19] Colei ele aqui embaixo. Toda essa parte aqui vai fazer parte de uma seção que contém uma classe do Bootstrap, que eu vou chamar de “container”. Quando eu salvar, vou voltar no nosso código e atualizar. Observe que nós já temos um visual um pouco melhor.

[02:35] O que podemos fazer também é colocarmos uma margem na nossa aplicação. Eu vou colocar aqui, por exemplo, dentro do “container” um espaço, eu vou colocar “mt-2”. Olhe só o que vai acontecer. Quando eu apertar a tecla “Enter”, ele desceu um pouco. Temos uma margem.

[02:50] Talvez isso nos seja suficiente para essa primeira parte do curso. Podemos mexer bastante no Bootstrap, editar e visualizar o nosso formulário de formas diferente da página. Do formulário em si nós vamos aprender como fazemos para manter o nosso formulário, editar o nosso formulário de maneira automática com o Django, porque isso é possível.

[03:13] O que eu quero fazer na sequência é: eu vou preencher os dados, vou escrever aqui “São Paulo”. O destino vai ser o “Rio de Janeiro”. Eu vou no dia “10/06/2020” e vou voltar no dia “12/06/2020”.

[03:30] Quando eu clicar no “OK”, eu quero ir para uma página e visualizar esses dados. Por exemplo: sua origem é São Paulo, seu destino é o Rio de Janeiro, data de ida, data de volta; e aparecerá esses valores. Isso é o que vamos fazer na sequência, no próximo vídeo.

#### Exercício: A classe forms do Django

A classe do Django Form descreve um formulário e determina como ele vai funcionar e como será exibido. Conforme vimos em aula, criamos um formulário com o seguinte código:

    class PassagemForms(forms.Form):
        origem = forms.CharField(label='Origem', max_length=100)
        destino = forms.CharField(label='Destino', max_length=100)
        data_ida = forms.DateField(label='Ida')
        data_volta = forms.DateField(label='Volta')COPIAR CÓDIGO

Sabendo disso, analise as afirmações abaixo e marque a correta:

a) Para utilizar a classe modelForm, é preciso realizar um migração do modelo e depois gerar o formulário baseado no modelo.
_Não é preciso realizar uma migração no banco de dados para criar um formulário._

b) **Alternativa correta:** Cada campo da classe Form será representado como um input no HTML.
_Certo! Cada campo criado terá um input no formulário instanciado pela view._

c) Todos os campos da classe ModelForm serão um input com tipo text no html.
_Nem todos os campos são do tipo text. Podemos criar um campo com tipo numérico, data ou email por exemplo._

#### O que aprendemos?

**Nesta aula:**
- Iniciamos a aplicação criando o app de passagens;
- Criamos um formulário utilizando o Django forms
- Melhoramos o visual do formulário exibindo incluindo o [bootstrap]('https://getbootstrap.com/').

**Projeto desenvolvido nesta aula**

Aqui você pode baixar o zip da aula 01 ou acessar os arquivos no [Github]('https://github.com/guilhermeonrails/django_forms_curso/tree/aula_1')!

**Na próxima aula**
Vamos aprender como recuperar e exibir os dados do formulário em outra página e incluir um calendário nas datas de ida e volta!

### 2. Alterando e manipulando dados
#### Exibindo dados
#### Melhorando o código
#### Widget e calendário
#### Estilizando os inputs
#### Faça como eu fiz na aula
#### Dados do formulário
#### O que aprendemos?
### 3. Novos campos e alterando o visual
#### Novos campos
#### Widget tweaks
#### Faça como eu fiz na aula
#### Para saber mais
#### O que aprendemos?
### 4. Validações
#### Clean_field
#### Exibindo mensagem de erro
#### Clean
#### Validando datas
#### Faça como eu fiz na aula
#### Clean e Clean_
#### O que aprendemos?
### 5. Modelos e formulários
#### Preparando o ambiente
#### Criando modelos
#### ModelForm
#### Formulários
#### Faça como eu fiz na aula
#### O formulário da Valentina
#### O que aprendemos?
#### Conclusão
