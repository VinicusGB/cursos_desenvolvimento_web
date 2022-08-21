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

Quando queremos exibir as informações de um formulário em outra página devemos usado no método class forms, temos:

1. Em `views.py`, devemos criar um novo método:
    
    ...

    def revisao_consulta(request):
        if request.method == 'POST':
            form = PassagemForms(request.POST)
            contexto = {'form':form}
            return render(request,'minha_consulta.html',contexto)

1. Em `urls.py`, devemos criar uma nova rota:
    
    ...
    
    path('minha_consulta',views.revisao_consulta,name='minha_consulta')
    
1. Em `index.html`, devemos na criar um tag form:
    
        ...
        <form action="{% url 'minha_consulta' %}" method="post">
            {% csrf_token %}
            {{ form }}
        </form>

1. Em `minha_consulta.html`, devemos recuperar apenas o valores do forms:
        
        ...
        <section>
            <h1>Passagem</h1>
            <p>Sua origem é: {{ form.origem.value }}</p>
            <p>Seu origem é: {{ form.destino.value }}</p>
            <p>Sua origem é: {{ form.data_ida.value }}</p>
            <p>Sua origem é: {{ form.data_volta.value }}</p>

---

[00:00] Assim que eu clico no botão “OK”, eu quero visualizar todos os dados que eu preenchi aqui do “Origem”, “Destino”, “Ida e Volta”; em uma outra tela, com uma descrição diferente. Por exemplo: sua origem é São Paulo, seu destino é Rio de Janeiro e assim por diante. Vamos fazer isso?

[00:16] Para começar, eu vou precisar cadastrar essa nova URL, então eu vou ter uma nova URL, eu vou ter uma nova página. Essa página eu posso chamar de “minha_consulta”. Então, supondo que eu coloquei os dados aqui do meu formulário e que todos os dados são válidos, eu quero ir para essa página. Então eu vou chamar essa página aqui.

[00:36] Vou dar um “path”, eu vou chamar essa minha página de “minha_consulta” e quem vai ser responsável por cuidar dessa requisição vai ser alguém lá de “views”, que eu vou chamar de “revisao_consulta”, por exemplo. O “name” que eu vou dar para essa página é “minha_consulta”.

[01:08] Salvei. Ele vai falar: “opa! Em ‘views’ não tem ninguém!” Vamos lá em “views”. Temos aqui em “views” a nossa função “index” e vamos ter também uma nova função, um novo método agora para a “minha_consulta”. Então eu vou chamar aqui de “revisao_consulta”. Vamos receber como argumento a nossa requisição e aqui vamos precisar verificar algumas coisas.

[01:36] Observe que tem um ponto bem interessante: nós criamos um “form” no Passagem, aqui no nosso template, na nossa “index”, nós criamos um “form”. Só que para conseguirmos de fato pegar as informações desse “forms” e passarmos para a nossa outra página, para a página de consulta, supondo que os campos e que os dados desse meu formulário são válidos, eu preciso indicar que isso aqui é um formulário, eu preciso indicar qual é o método HTTP que nós vamos utilizar.

[02:05] E tudo isso nós aprendemos nos outros cursos, nós já sabemos. Então eu vou colocar aqui o “form”, a ação, quem vai ser responsável por atender esse formulário. Quem vai estar vinculado com esse formulário vai ser a URL de “minha_consulta”, então eu vou colocar aqui a URL que nós criamos. Deixe-me só visualizar aqui no nome para nós não ficarmos confusos. A URL que nós vamos vincular com esse formulário é o “minha_consulta”.

[02:31] Então aqui eu vou colocar o “name” que nós utilizamos, “minha_consulta”. Nós sabemos que o “minha_consulta”, eu vou remover essa tag que fecha o “forms”, eu vou colocá-la aqui embaixo só para visualizarmos melhor e vou colocar aqui todo esse conteúdo, que é o formulário. O nosso botão de “input”, um pouco para lá para deixarmos indentado o nosso código.

[02:58] Então, o que acontece agora? Olhe só, nós temos um formulário, nós indicamos qual é a URL que vamos utilizar. Nós precisamos passar qual é o método que vamos utilizar do HTTP, nós vamos utilizar o método “POST”.

[03:10] O que não podemos esquecer agora é o “token” de segurança. Então eu vou passar aqui o “csrf_token”, porque queremos manipular as informações deste formulário em outro lugar.

[03:24] Então, o que eu vou fazer agora? Eu vou verificar se o “request.method == 'POST' :” , ou seja, nós temos um requisição “POST” vindo para a “revisao_consulta”. O que eu quero fazer? Eu quero de fato buscar as informações que estavam naquele formulário e conseguir visualizar essas informações naquela página que nós criamos.

[03:50] Então eu vou utilizar assim: para eu buscar informação do formulário, eu vou chamar aqui o “form = PassagemForms()”, só que aqui eu quero buscar o “PassagemForms”, não instanciar um novo “PassagemForms”. Eu quero buscá-lo dessa requisição “POST”.

[04:07] Então eu faço da seguinte forma: “request.POST”. Então trouxemos esse formulário por requisição. Eu vou fazer algo bem parecido com isso aqui, eu vou até usar uma cola aqui. Então, o que eu vou fazer? Eu trouxe o formulário que veio da requisição “POST”, com todos os dados que ele tem, coloquei ele em uma variável de contexto e vou agora exibi-lo em uma página. Qual página?

[04:29] Se observarmos aqui, nós ainda não temos uma página, nós só temos a página “index”. Eu vou criar uma nova página, que eu vou chamar de “minha_consulta.html”, ela vai ser super parecida com a “views”. Eu vou copiar aqui todo o código da “view”. Teclas “Ctrl + V”, vou copiar todo o código da “view” sem o nosso “form”. Eu quero exibir o resultado da passagem.

[04:55] Então eu vou colocar aqui uma tag “

”, por exemplo, e vou falar: “Sua origem é:” e quero exibir agora o valor da origem. Como eu consigo buscar lá do meu formulário o que eu escrevi no meu campo ‘Origem’? Da seguinte forma:

[05:15] Eu vou utilizar “{{“, duas porque agora de fato eu não quero só processar a informação, eu quero exibir, então eu vou utilizar aqui “{{form.origem}}”. Eu quero a mesma coisa para os outros campos também, não só para origem. Eu quero para “Origem”, para o “Destino”, para a “Data de Ida” e “Data de Volta”.

[05:32] Então, “Seu destino é:”, “Sua data de ida é:” e “Sua data de volta é:”. Aqui eu só altero, “Seu destino”. Aqui é um ponto importante também, no lugar de usar “Data de Ida”, eu preciso usar o mesmo nome que eu tenho lá no meu “forms”, então vamos visualizar só para não ficarmos confusos, “data_ida”. Então eu vou aqui na “minha_consulta”, vou colocar a “data_ida”, e aqui eu tenho “data_volta”.

[06:06] Salvando essas informações eu volto aqui na “view”, salvo minha “view”. Então, renderizando não a página “index”, renderizando agora o “minha_consulta.html”, passando por “contexto”.

[06:21] Voltando na aplicação, quando eu atualizar aqui, não temos nenhum dado. Vou colocar aqui. Então eu tenho: “São Paulo”, meu destino é “Rio de Janeiro”, eu vou viajar no dia “10/06/2020” e vou voltar no dia “12/06/2020”.

[06:42] Quando eu aperto em “OK”, observe que exibimos as informações, só que elas estão em um campo “input”, então eu posso colocar: “São Paulo - São Paulo”. Vai ficar um pouco estranho, eu não queria exibir “São Paulo - São Paulo”, eu não queria exibir um campo “input”, eu queria exibir apenas o valor. Como que eu exibo apenas o valor daquele campo?

[06:59] Lá no “minha_consulta” eu vou alterar, ao invés de exibir sua “Origem”, “form.origem”, “form.origem.value”, e vou fazer isso para todos os outros campos também, “.value” para o de baixo também e para o último também.

[07:17] Então em todos os meus campos, eu quero só o valor deles. Quando eu volto e atualizo, ele pergunta se eu quero mandar essa requisição mesmo. Eu quero, e nós temos aqui não mais um campo “input”, mas temos aqui agora um campo de apenas o valor que tínhamos naqueles “inputs”.

[07:36] Vamos voltar? Observe que para eu voltar está um pouco ruim também, eu tenho sempre que manipular na URL. No próximo vídeo nós vamos melhorar isso também.

[07:43] Eu vou colocar um outro destino. Agora eu estou em “Minas Gerais”, eu quero ir para o “Rio de Janeiro”, eu vou no dia “10/08/2020” e vou voltar no dia “15/08/2020”. Quando eu aperto em “OK”, nós temos um resultado legal. Minas Gerais, com as datas e todas as outras informações certas.

[08:14] No próximo vídeo nós vamos melhorar um pouco a navegação da nossa tela. Lembrando que essa página que criamos de “minha_consulta” vai ser a página onde teremos um formulário válido.

#### Melhorando o código

[00:00] Sempre que eu submeto um formulário, quando eu dou aqui um “OK”, nós vamos para uma página onde podemos visualizar os dados. Nós estamos aprendendo a manipular os dados de um formulário. Ficou legal, só que eu quero voltar para a outra página através de um navbar, eu quero clicar em um link aqui de um menu e voltar para essa página aqui.

[00:16] Para isso, nós podemos usar um navbar do próprio Bootstrap. Eu vou digitar aqui “navbar bootstrap” e vou clicar aqui nesse primeiro link no “Navbar - Bootstrap” e vou copiar aqui essas duas primeiras linhas, porque eu só quero um link, eu não preciso de todos os outros links aqui do navbar.

[00:32] Voltando lá no nosso código, na página do “minha_consulta” aqui do nosso “container”, embaixo dessa seção de “container” eu vou colocar o navbar. Vou fechar aqui a tag “ ”. Eu quero que esse navbar fique escrito “Passagem” e que sempre que eu clicar nele, voltar para a página “index”, para a nossa página principal.

[00:54] Eu vou usar o código Python aqui para fazermos isso com “{” e “%”. Vou digitar “url” para ser direcionado para a página de “index”. Voltando na nossa aplicação quando eu atualizar... Deixe-me voltar aqui porque já preenchemos.

[01:09] Agora sim, deixe-me ver. Vou atualizar essa página e nós teremos aqui o “Passagem”. Tem aqui o “Passagem”, essa “Passagem” não vamos precisar mais. Eu vou tirar, vou salvar e assim que eu atualizar, nós vamos ficar só com esse formulário aqui.

[01:25] Então temos os dados e temos aqui o “Passagem”. Quando eu clico no “Passagem”, nós voltamos para a página principal. Na página principal está escrito “Passagem” com “”, eu não queria isso, eu queria manter na página principal esse mesmo layout que temos aqui. Então, o que eu vou fazer?

[01:40] Para não ficarmos copiando código, duplicando código, nós podemos compartilhar o código HTML com outras páginas também. Nós já vimos isso lá no nosso primeiro treinamento.

[01:49] Então eu vou criar um arquivo para manter códigos que serão usados em todas as páginas HTML, eu vou chamar de “base.html”. Nesse código eu vou manter todo nosso “head”, o “body” e todo esse conteúdo aqui. Vou até copiar essa parte aqui da “section” também, vou apertar as teclas “Ctrl + C” nessa parte. Vou copiar do “minha_consulta”, é melhor porque já temos o navbar.

[02:13] Então eu vou copiar aqui todo esse código, “Ctrl + C”, venho aqui no “base.html”, vou colocar ele com as teclas “Ctrl + V”. Nós queremos inserir todo o conteúdo da nossa página aqui embaixo, seja ela os nossos parágrafos ou o nosso próprio formulário. Então, o que eu vou fazer? Eu vou copiar só a parte final, fechando a “section” aqui e fechando aqui o “body”. Nós vamos colocar partes de outros códigos aqui dentro.

[02:44] Então eu vou colocar aqui através de código com “{” e “ %” também, e vou indicar que aqui tem um bloco de código aqui que eu quero inserir. Então, “block content”. Nós precisamos indicar onde esse bloco termina. Então eu vou colocar aqui o “endblock” e vou salvar. Não vou mais precisar desse final de trecho e não vou precisar mais de todo esse código aqui. Nós vamos manter só esse nosso código aqui.

[03:15] Selecionando tudo e apertando as teclas “Command + [” nós vamos empurrando o nosso código para o lado e agora temos esse código aqui. Deixe-me voltar um só para mantermos assim. Legal, salvei!

[03:27] Só que eu preciso indicar que nessa página aqui e na nossa página “index”, eu vou tirar isso aqui também. Nós vamos deixar só as coisas relacionadas nesta página, nós não queremos conteúdo de outras páginas aqui também. Então, selecionando tudo e apertando as teclas “Command + [” nós conseguimos voltar o nosso código.

[03:46] Então temos aqui o formulário e aqui temos o trecho da nossa outra página. Assim, escrevemos o navbar uma vez só que nós indicamos. Nós vamos inserir um bloco de código aqui e temos que mostrar isso nas outras páginas também. Então, como eu vou fazer?

[04:02] Eu vou dizer que esse código que eu tenho aqui precisa ser uma herança, eu preciso herdar desse “base.html”, então com “{” e “%“ eu vou digitar aqui “{% extends “base.html” %}”, para herdarmos de “html”. Eu vou indicar que o trecho de código que queremos inserir, o bloco de código que queremos inserir “html” é esse aqui.

[04:36] Então eu vou colocar aqui um “{% block content %}” para indicar que esse trecho de código acaba em algum lugar. Vou colocar aqui no final “{% endblock %}” e vou salvar. Esse mesmo comportamento, eu quero na minha consulta também. Aqui embaixo eu também tenho um “{% endblock %}”. Legal!

[05:11] Voltando na nossa aplicação. Então, o que fizemos? Nós indicamos que temos um conteúdo para inserir, nas outras páginas nós herdamos esse código HTML e inserimos aqui as tags do Djang”, do “block content” e do “end content”. Vamos ver na nossa aplicação, se houve alguma alteração?

[05:34] Vou clicar aqui em “localhost:8000” apenas para visualizarmos. Quando eu aperto a tecla “Enter”, ficou ali um “Passagem”, que eu esqueci de tirar aqui do nosso “index”. Vou tirar esse “” aqui, não vai ter mais. Nós temos apenas o “form”. Observe que o nosso código agora vai ficar muito mais limpo, vai ficar bem melhor para trabalharmos.

[05:50] Então eu tenho “Passagem”. Quando eu clico no “Passagem”, nós sempre vamos para a nossa página principal. Se eu preencher aqui, eu estou no Rio de Janeiro, eu quero ir para Minas Gerais, e eu vou no dia 10 e vou voltar no dia 20, por exemplo, e clico em “OK”. Observe que temos aqui o mesmo comportamento. Dessa forma nós evitamos código duplicado nas nossas páginas de HTML e vai ficar mais limpo para trabalharmos aqui no nosso “form” também.

[06:12] Observe que todo nosso formulário, todo o formulário gerado aqui, “Origem”, “Destino”, esses “inputs” e o “ok”; se apertarmos com o botão esquerdo e colocar aqui “inspect”, nós vamos ver que existe uma série de código HTML gerado aqui. Todo código que foi gerado da nossa aplicação, todo esse código aqui, foi gerado.

[06:36] Nós não escrevemos nenhuma “label” direto nas tags HTML, nós utilizamos o “Django Forms”. Todo “form” é gerado através desse código, e estamos exibindo depois, buscando, ou não, os valores deste formulário aqui nessa outra página de “minha_consulta”.

#### Widget e calendário

[Tempus Dominus Django]('https://pypi.org/project/django-tempus-dominus/')

        pip install django-tempus-dominus

1. Em `settings.py`, temos que:

        ...
        INSTALLED_APPS = [
            ...,
            'tempus_dominus',
            ...
        ]

        TEMPUS_DOMINUS_LOCALIZE = True #Para funcionar conforme a localização

1. Em `forms.py`, temos que:

        import tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

        class PassagemForms(form.Form):
            ...
            data_ida = forms.DateField(label='Ida',widget=DatePicker())
            data_volta = forms.DateField(label='Volta', widget=DatePicker())

1. Em `base.html`, temos que adicionar a tag do BootStrap e Java Script e:

        <head>
            {{ form.media }}
        </head>

---

[00:00] Assim que eu preencho o meu formulário, o meu campo de ida e o meu campo de volta, que deveriam ser a data, eu posso colocar algo diferente. Por exemplo: na ida eu vou escrever “Ida” e na volta eu vou escrever “Volta”. Quando eu clico em “OK”, observe o que acontece, fica “Sua origem é: São Paulo”, “Seu destino é: Rio”, “Sua data de ida é: ida” e “Sua data de volta é: volta”. Não é esse comportamento que eu queria para a nossa aplicação.

[00:21] Eu gostaria que esse campo aqui de ida e de volta, quando nós clicarmos neles, fosse exibido um calendário onde a pessoa escolhe, seleciona ali a data que ela quer viajar e a data que ela quer voltar. Vamos fazer isso?

[00:33] Nós vamos utilizar um módulo chamado “tempus-dominus-django”. Nesse primeiro link aqui “django-tempus-dominus”. Nós vamos abrir essa biblioteca. Temos aqui como utilizar essa biblioteca e vamos seguir o passo a passo dessa documentação.

[00:51] Nessa linha aqui, observe que temos uma notícia que essa biblioteca não vai receber mais atualizações e ele não garante também que vai funcionar no Django 3. Nós aqui da Alura fizemos os testes dessa biblioteca e vamos ter o comportamento que estamos querendo na versão do Django 3. Nós testamos e ele está funcionando nessa versão também.

[01:11] E ele falou que talvez no futuro ele pode voltar a utilizar esse módulo também no Django, desse módulo o “tempus-dominus-django” também pode acontecer isso de ter alteração, ou não. Então como testamos e funcionou, tivemos o comportamento que queríamos, vamos utilizar ele.

[01:28] Então a primeira coisa que temos que fazer é instalarmos. Eu vou copiar essa linha aqui, “pip install django-tempus-dominus”. Copiei essa linha, lá na nossa aplicação o terminal 1 está rodando o meu servidor. Vou abrir o terminal 2. Deixe-me fechar esses dois porque conseguimos visualizar melhor.

[01:47] Eu vou apertar as teclas “Ctrl + V”, “pip install”. Quando eu aperto a tecla “Enter”, observe que esse módulo já foi instalado. Ele fala depois também para adicionarmos o “tempus_dominus” lá nos apps instalados.

[01:59] Então, o que eu vou fazer? Abrindo aqui a nossa aba de navegação, aqui no nosso “setup” em “settings.py”, onde dizemos todos os apps que nós temos instalados, vamos colocar também o “tempus_dominus” aqui e vamos salvar.

[02:18] Vamos ver seguindo a documentação para vermos o que nós precisamos fazer também. Ele fala aqui sobre a localização. Aqui é um ponto importante, nós não queremos exibir o calendário da nossa página em inglês, então pense: a nossa aplicação tem “Origem” e “Destino” escritos na língua portuguesa. Quando clicamos no calendário, aparece o calendário em inglês. Não é o que queremos, nós queremos mostrar o calendário em português. Ele dá aqui uma dica.

[02:43] Ele fala que se você deixar o “tempus_dominus” com o “localize”, você vai poder configurar para a língua que você estiver utilizando na aplicação, e é o que queremos. Então eu vou copiar essa variável aqui, “TEMPUS_DOMINUS_LOCALIZE”. Lá na última linha, aqui eu vou apertar as teclas “Ctrl + V” e vou falar que eu quero utilizar. Então eu vou falar que eu quero utilizar a localização de idioma para esse nosso calendário. Então eu deixei como “true”.

[03:14] O que precisamos fazer também? Vamos ver... Ele fala aqui sobre o padrão do que vamos utilizar. Agora, olhe só: lá no nosso “forms” ele fala para alterarmos, nós vamos colocar essa propriedade “widget” aqui no nosso formulário. O que é essa propriedade “widget”, na verdade? O que ela faz?

[03:34] “Widget” é a representação que vamos utilizar no nosso “imput” lá no HTML, então é como o Django vai criar esse “imput” no HTML. Então a primeira coisa que temos que fazer é importarmos.

[03:45] Nós vamos utilizar apenas, para a nossa aplicação, o “DatePicker”, então eu vou copiar do “tempus_dominus”, que já instalamos via “pip install”. Nós vamos importar o “DatePicker”.

[03:56] Então eu vou lá no meu “forms”. Vou fechar aqui. Vou em “setup” aqui no nosso “Passagens”, no “forms.py” nós vamos importar esse “DatePicker”. Deixe-me minimizar aqui só para visualizarmos melhor. Observe que trouxemos o “DatePicker”, só que nenhum momento nós passamos esse “DatePicker” para a data de Ida e para a data de Volta. Nós queremos alterar a forma como ele vai mostrar esses campos.

[04:22] Então, o que ele fala? Existe essa propriedade “widget-DatePicker” que vamos utilizar. Então, o que eu vou fazer? Eu vou colocar aqui do lado do “label”. Se eu colocar “widget”, observe que ele já aparece aqui para mim. Eu vou apertar a tecla “Enter”, vou escrever “DatePicker” e vou colocar aqui para executar essa nossa função. Vou fazer o mesmo também para a data de volta, “widget=DatePicker” função, abre parênteses e fecha parênteses. Legal, vou salvar!

[04:53] Vamos ver qual o outro passo que precisamos fazer. Ele fala também que é necessário que utilizemos o JQuery para exibirmos esse nosso calendário. Então eu vou copiar essas duas linhas, porque as duas linhas que nós copiamos lá no nosso “base.html”, aqui no nosso template no “base.html”, essas duas linhas são referentes ao Bootstrap que copiamos.

[05:18] Agora eu quero utilizar também o JQuery para conseguir exibir o nosso calendário conforme a documentação que ele passa aqui. Uma outra coisa: ele também coloca essa tag aqui, “included” essa tag do “form.media”. Então, “{{ form.media }}”. Vou apertar as teclas “Ctrl + C”.

[05:37] Ainda aqui no nosso arquivo de meta, deixe-me minimizar para nós visualizarmos melhor. Eu vou colar ela aqui. Então, o que fizemos? Trouxemos o JQuery para cá e passamos essa tag “form.media” aqui na nossa tag do “head”. Legal, trouxe isso! Depois temos outras opções aqui para exibir. Vamos ver como ficou na nossa aplicação.

[05:59] Vou atualizar. Ele ficou bem grande aqui, olhe a data de ida, ficou bem grande. A data de volta ficou bem grande também. Nós já vamos arrumar isso. Então, “Origem”, vamos lá! Vamos passo a passo.

[06:09] Eu vou colocar aqui “São Paulo” e “Destino: Rio”. Na data de ida, quando eu clicar, aparece aqui um calendário já em português, olhe só, “março 2020”. Então eu vou viajar no dia 10 e vou voltar no dia 25. Aperto em “OK” e ele nos mostra, “Sua origem é: São Paulo”, “Seu destino é: Rio”, “Sua data de ida é: 10/03/2020” e “Sua data de volta é: 10/03/2020”.

[06:36] Observe que nesse campo, por mais que eu escreva, sempre quando eu volto, eu não tenho mais aquele campo, eu não tenho mais aquele valor escrito. Sempre quando eu altero, ele já nos cria essa validação no nosso HTML.

[06:54] Ficou legal! Tivemos um comportamento, está exibindo o calendário já em português, tudo isso ficou bem bacana. Só que o que eu quero fazer agora é não deixá-lo tão grande assim, está desproporcional o “Origem”, o “Destino”, o “Ida” aqui e “Volta”. Eles estão desproporcionais com a nossa aplicação.

[07:14] O que podemos fazer é: lá no nosso formulário... Deixe-me fechar aqui. Voltando aqui no nosso template onde estamos exibindo o nosso formulário nesse “form action” e vou criar uma seção.

[07:25] Então eu vou criar aqui uma nova seção. Vou incluir todo o nosso formulário nessa seção, apertar as teclas “Ctrl+ X” e vou passá-lo aqui em baixo para fechar a nossa seção. Legal!

[07:39] O que eu vou fazer? Nessa seção eu vou importar uma classe para determinar o tamanho dele. Então eu vou colocar aqui “col-8”, só para testarmos. Opa! Eu esqueci da palavra “class” aqui. Agora sim, vou colocar aqui “col-8” e vou tirar esses outros campos daqui. Vamos ver como vai ficar? Voltando aqui na nossa aplicação. Legal!

[08:11] O que nós vamos fazer na sequência é melhorarmos a exibição do nosso formulário, porque ele ficou todo desproporcional aqui. Nós vamos aprender como é que fazemos isso no próximo vídeo.

#### Estilizando os inputs

[00:00] Assim que eu preencho o meu formulário, o meu campo de ida e o meu campo de volta, que deveriam ser a data, eu posso colocar algo diferente. Por exemplo: na ida eu vou escrever “Ida” e na volta eu vou escrever “Volta”. Quando eu clico em “OK”, observe o que acontece, fica “Sua origem é: São Paulo”, “Seu destino é: Rio”, “Sua data de ida é: ida” e “Sua data de volta é: volta”. Não é esse comportamento que eu queria para a nossa aplicação.

[00:21] Eu gostaria que esse campo aqui de ida e de volta, quando nós clicarmos neles, fosse exibido um calendário onde a pessoa escolhe, seleciona ali a data que ela quer viajar e a data que ela quer voltar. Vamos fazer isso?

[00:33] Nós vamos utilizar um módulo chamado “tempus-dominus-django”. Nesse primeiro link aqui “django-tempus-dominus”. Nós vamos abrir essa biblioteca. Temos aqui como utilizar essa biblioteca e vamos seguir o passo a passo dessa documentação.

[00:51] Nessa linha aqui, observe que temos uma notícia que essa biblioteca não vai receber mais atualizações e ele não garante também que vai funcionar no Django 3. Nós aqui da Alura fizemos os testes dessa biblioteca e vamos ter o comportamento que estamos querendo na versão do Django 3. Nós testamos e ele está funcionando nessa versão também.

[01:11] E ele falou que talvez no futuro ele pode voltar a utilizar esse módulo também no Django, desse módulo o “tempus-dominus-django” também pode acontecer isso de ter alteração, ou não. Então como testamos e funcionou, tivemos o comportamento que queríamos, vamos utilizar ele.

[01:28] Então a primeira coisa que temos que fazer é instalarmos. Eu vou copiar essa linha aqui, “pip install django-tempus-dominus”. Copiei essa linha, lá na nossa aplicação o terminal 1 está rodando o meu servidor. Vou abrir o terminal 2. Deixe-me fechar esses dois porque conseguimos visualizar melhor.

[01:47] Eu vou apertar as teclas “Ctrl + V”, “pip install”. Quando eu aperto a tecla “Enter”, observe que esse módulo já foi instalado. Ele fala depois também para adicionarmos o “tempus_dominus” lá nos apps instalados.

[01:59] Então, o que eu vou fazer? Abrindo aqui a nossa aba de navegação, aqui no nosso “setup” em “settings.py”, onde dizemos todos os apps que nós temos instalados, vamos colocar também o “tempus_dominus” aqui e vamos salvar.

[02:18] Vamos ver seguindo a documentação para vermos o que nós precisamos fazer também. Ele fala aqui sobre a localização. Aqui é um ponto importante, nós não queremos exibir o calendário da nossa página em inglês, então pense: a nossa aplicação tem “Origem” e “Destino” escritos na língua portuguesa. Quando clicamos no calendário, aparece o calendário em inglês. Não é o que queremos, nós queremos mostrar o calendário em português. Ele dá aqui uma dica.

[02:43] Ele fala que se você deixar o “tempus_dominus” com o “localize”, você vai poder configurar para a língua que você estiver utilizando na aplicação, e é o que queremos. Então eu vou copiar essa variável aqui, “TEMPUS_DOMINUS_LOCALIZE”. Lá na última linha, aqui eu vou apertar as teclas “Ctrl + V” e vou falar que eu quero utilizar. Então eu vou falar que eu quero utilizar a localização de idioma para esse nosso calendário. Então eu deixei como “true”.

[03:14] O que precisamos fazer também? Vamos ver... Ele fala aqui sobre o padrão do que vamos utilizar. Agora, olhe só: lá no nosso “forms” ele fala para alterarmos, nós vamos colocar essa propriedade “widget” aqui no nosso formulário. O que é essa propriedade “widget”, na verdade? O que ela faz?

[03:34] “Widget” é a representação que vamos utilizar no nosso “imput” lá no HTML, então é como o Django vai criar esse “imput” no HTML. Então a primeira coisa que temos que fazer é importarmos.

[03:45] Nós vamos utilizar apenas, para a nossa aplicação, o “DatePicker”, então eu vou copiar do “tempus_dominus”, que já instalamos via “pip install”. Nós vamos importar o “DatePicker”.

[03:56] Então eu vou lá no meu “forms”. Vou fechar aqui. Vou em “setup” aqui no nosso “Passagens”, no “forms.py” nós vamos importar esse “DatePicker”. Deixe-me minimizar aqui só para visualizarmos melhor. Observe que trouxemos o “DatePicker”, só que nenhum momento nós passamos esse “DatePicker” para a data de Ida e para a data de Volta. Nós queremos alterar a forma como ele vai mostrar esses campos.

[04:22] Então, o que ele fala? Existe essa propriedade “widget-DatePicker” que vamos utilizar. Então, o que eu vou fazer? Eu vou colocar aqui do lado do “label”. Se eu colocar “widget”, observe que ele já aparece aqui para mim. Eu vou apertar a tecla “Enter”, vou escrever “DatePicker” e vou colocar aqui para executar essa nossa função. Vou fazer o mesmo também para a data de volta, “widget=DatePicker” função, abre parênteses e fecha parênteses. Legal, vou salvar!

[04:53] Vamos ver qual o outro passo que precisamos fazer. Ele fala também que é necessário que utilizemos o JQuery para exibirmos esse nosso calendário. Então eu vou copiar essas duas linhas, porque as duas linhas que nós copiamos lá no nosso “base.html”, aqui no nosso template no “base.html”, essas duas linhas são referentes ao Bootstrap que copiamos.

[05:18] Agora eu quero utilizar também o JQuery para conseguir exibir o nosso calendário conforme a documentação que ele passa aqui. Uma outra coisa: ele também coloca essa tag aqui, “included” essa tag do “form.media”. Então, “{{ form.media }}”. Vou apertar as teclas “Ctrl + C”.

[05:37] Ainda aqui no nosso arquivo de meta, deixe-me minimizar para nós visualizarmos melhor. Eu vou colar ela aqui. Então, o que fizemos? Trouxemos o JQuery para cá e passamos essa tag “form.media” aqui na nossa tag do “head”. Legal, trouxe isso! Depois temos outras opções aqui para exibir. Vamos ver como ficou na nossa aplicação.

[05:59] Vou atualizar. Ele ficou bem grande aqui, olhe a data de ida, ficou bem grande. A data de volta ficou bem grande também. Nós já vamos arrumar isso. Então, “Origem”, vamos lá! Vamos passo a passo.

[06:09] Eu vou colocar aqui “São Paulo” e “Destino: Rio”. Na data de ida, quando eu clicar, aparece aqui um calendário já em português, olhe só, “março 2020”. Então eu vou viajar no dia 10 e vou voltar no dia 25. Aperto em “OK” e ele nos mostra, “Sua origem é: São Paulo”, “Seu destino é: Rio”, “Sua data de ida é: 10/03/2020” e “Sua data de volta é: 10/03/2020”.

[06:36] Observe que nesse campo, por mais que eu escreva, sempre quando eu volto, eu não tenho mais aquele campo, eu não tenho mais aquele valor escrito. Sempre quando eu altero, ele já nos cria essa validação no nosso HTML.

[06:54] Ficou legal! Tivemos um comportamento, está exibindo o calendário já em português, tudo isso ficou bem bacana. Só que o que eu quero fazer agora é não deixá-lo tão grande assim, está desproporcional o “Origem”, o “Destino”, o “Ida” aqui e “Volta”. Eles estão desproporcionais com a nossa aplicação.

[07:14] O que podemos fazer é: lá no nosso formulário... Deixe-me fechar aqui. Voltando aqui no nosso template onde estamos exibindo o nosso formulário nesse “form action” e vou criar uma seção.

[07:25] Então eu vou criar aqui uma nova seção. Vou incluir todo o nosso formulário nessa seção, apertar as teclas “Ctrl+ X” e vou passá-lo aqui em baixo para fechar a nossa seção. Legal!

[07:39] O que eu vou fazer? Nessa seção eu vou importar uma classe para determinar o tamanho dele. Então eu vou colocar aqui “col-8”, só para testarmos. Opa! Eu esqueci da palavra “class” aqui. Agora sim, vou colocar aqui “col-8” e vou tirar esses outros campos daqui. Vamos ver como vai ficar? Voltando aqui na nossa aplicação. Legal!

[08:11] O que nós vamos fazer na sequência é melhorarmos a exibição do nosso formulário, porque ele ficou todo desproporcional aqui. Nós vamos aprender como é que fazemos isso no próximo vídeo.

#### Dados do formulário

Pensando em otimizar o trabalho com formulário, o Django realiza as principais ações, dentre elas:

Preparar e estruturar os dados que serão exibidos no formulário
Criação do html do formulário que será renderizado
Recebimento e processamento dos dados enviados pelo formulário
Em relação ao recebimento e processamento dos dados enviados pelo formulário, analise as afirmações abaixo e marque as verdadeiras:

a. **Alternativa correta:** Para exibir um formulário na página html, podemos passar a instância do formulário como contexto, como ilustra o código abaixo:

    return render(request, 'index.html',{'form': form})

    Certo! Após passar o formulário como argumento da função render, para exibir este formulário, podemos utilizar o seguinte código na página html:

    {{ form }}

b. **Alternativa correta:** Para recuperar os dados de um formulário enviados por uma requisição post, podemos utilizar o seguinte código:

    form = NOME_DO_FORMULARIO(request.POST)

    Certo! Desta forma, os dados enviados pelo formulário na requisição do cliente, serão atribuídos na variável form.

c. Para exibir apenas o valor de um campo do formulário em outra página, podemos utilizar o seguinte código:

    {{ form.nome_do_campo}}

#### O que aprendemos?

##### Nesta aula:

- Aprendemos como manipular as informações do Formulário, exibindo os dados em outra página;
- Evitamos código duplicado nos arquivos HTML criando o arquivo base.html;
- Alteramos o visual do formulário adicionando widget e classes do bootestrap.

##### Projeto desenvolvido nesta aula
Aqui você pode baixar o zip da aula 02 ou acessar os arquivos no [Github]('https://github.com/guilhermeonrails/django_forms_curso/tree/aula_2')!

Na próxima aula
Vamos criar campos de tipos diferentes no nosso formulário!

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
