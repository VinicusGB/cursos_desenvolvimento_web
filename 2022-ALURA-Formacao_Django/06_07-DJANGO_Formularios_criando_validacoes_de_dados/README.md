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

[00:00] Nosso formulário hoje conta com quatro campos. Eu quero criar novos campos para esse meu formulário.

[00:05] Então eu vou fechar aqui o meu “index.html”, vou abrir aqui o meu “Passagens” e vou no “forms.py”. Observe que nós temos os nossos quatro campos aqui, o “Origem”, “Destino”, data de “Ida” e data de “Volta”.

[00:16] Eu quero criar um novo campo, eu quero criar um campo onde mostra quando eu estou fazendo essa pesquisa, então eu vou chamar de “data_pesquisa”. Eu quero que ele seja bem parecido com os nossos outros campos, eu quero que ele seja. Vou colocar aqui o “data_pesquisa = forms.DateField” também e eu vou chamar a “label” dele de... Vou escrever “label=’Data da pesquisa’ ”.

[00:47] Eu quero também que além da data e da pesquisa para esse meu campo, eu quero deixar esse campo desabilitado. Eu não quero que a pessoa consiga alterar, ela vai consiga ver, mas que não consiga alterar.

[00:57] Então eu vou colocar um a propriedade aqui chamada “disabled=“ e vou passar aqui o valor “True”. Então eu quero que seja verdadeiro, que ela não consiga alterar, e eu quero que ela veja também a data de hoje, então eu vou colocar a propriedade “initial=”. Eu quero usar a data de hoje, eu quero que ele sempre pegue a data de hoje do sistema.

[01:16] Para ele conseguir pegar a data de hoje nós vamos importar um módulo aqui, então, “from datetime import”. Eu quero importar o “datetime” e eu vou usar aqui no “initial” essa propriedade que importamos, “datetime.today”, para ele pegar a data de hoje.

[01:39] Vou salvar, voltar na nossa aplicação e atualizar. Nós temos aqui um “input”, podemos ver que é um “input” aqui. Só que não conseguimos selecioná-lo, não conseguimos alterar. Ficou legal, era o que eu queria.

[01:51] Outro campo que eu quero inserir na nossa aplicação é qual o tipo de classe que a pessoa quer viajar aqui na nossa aplicação. Então, para isso, eu vou criar uma categoria “tipos de classes” e vou selecionar esses tipos de classes. Quando a pessoa entrar na nossa aplicação, vai abrir. Quando ela clicar, não vai conseguir digitar e vai abrir uma sequência de classes que ela pode escolher, se é classe executiva, se é primeira classe e assim por diante. Então, vamos lá?

[02:18] Eu vou criar aqui um novo arquivo onde estamos mesmo e vou chamá-lo de “classe_viagem.py”. Nesse “classe_viagem.py” eu vou criar aqui uma tupla, eu vou colocar aqui “tipos_de_classe =“ e aqui entre “{}” eu vou criar uma tupla para cada classe.

[02:45] Então eu vou colocar aqui, por exemplo: eu vou deixar “1”, e vou escrever aqui que “1” vai ser a classe “{1, 'Econômica' },”. Aqui “(2, 'Executiva'),” e para finalizar a (3, 'Primeira classe')”. Vou salvar.

[03:19] O que eu preciso fazer agora? Aqui no nosso “forms” eu quero criar esse novo campo, eu quero que consigamos escolher uma dessas classes aí. Então eu vou chamar essa propriedade “classe_viagem = forms.ChoiceField()”, ou seja, nós vamos conseguir escolher o “ChoiceField”.

[03:45] Então dentro desse “ChoiceField”, eu vou passar um nome para ele também, uma “label” eu quero exibir, então eu vou chamar essa “label” de “ 'Classe do vôo' ”. Eu vou colocar uma vírgula aqui e nós vamos passar outras propriedades.

[04:11] E eu quero que o “Choice” seja igual aqueles tipos de classes que eu criei. Para isso, nós precisamos importar esse arquivo aqui para o nosso “forms”, então eu vou passar aqui “from passagens.classe_viagem import tipos_de_classe”. Aqui nós temos no “Choice” e já podemos utilizar o “tipos de classe”.

[04:38] Salvei. Vamos visualizar? Eu vou atualizar a minha aplicação. Tem aqui, olhe: “Classe de vôo”, está “Econômica”, “Executiva” e “Primeira classe”. Ficou legal, era o que eu queria também.

[04:48] Além disso, eu quero um campo de informações extras. Por exemplo: já que o nosso site é um site onde as pessoas vão pesquisar, elas vão colocar ali esses destinos, vão dar um “OK” e teoricamente teria uma busca ali em vários outros sites para ver quais são os voos mais baratos. Nós podemos colocar umas informações extras para a pessoa escrever.

[05:08] Por exemplo: eu quero viajar a noite ou quero sentar na janela, alguma coisa desse tipo, então eu vou chamar de “informacoes”. Esse “informacoes” vai ser do tipo “forms” também, e vai ser um tipo “CharField”, só que eu quero ele diferente. Nós vamos ver aqui como criamos esse “CharField” diferente.

[05:26] Por exemplo: nesse “CharField”, eu não quero que seja igual o outro, que apareça só um “input” pequeno aqui. Eu quero que tenha mais coisa, eu quero que seja uma caixa para a pessoa de fato escrever. Então nós podemos alterar esse conteúdo. Por exemplo: a “label” dele, eu vou escrever “Informações extras”, vou dar uma vírgula aqui e vou falar que o máximo de caracteres que nós vamos permitir serão “200” caracteres.

[05:55] E agora nós vamos alterar a forma como ele vai ser exibido lá no HTML, da mesma forma como colocamos o “widget date picker” para data de volta, para ele alterar como vai ser exibido. Nós vamos passar também as propriedades “widget”.

[06:12] Só que nós vamos alterar, nós não vamos usar o “date picker” aqui, nós vamos usar o “Textarea”. Eu vou colocar aqui que ele é uma função também e vou falar que ele não precisa ser obrigatório. Caso a pessoa preencha todos os outros campos e não preencha esse campo, não vai fazer diferença para a nossa aplicação.

[06:35] Então eu vou passar aqui um “required=False”. Salvei, voltando na nossa aplicação, atualizando. Alguma coisa deu errado, eu escrevi errado, é “forms.Textarea()”. Agora sim, voltando na nossa aplicação e atualizando, agora conseguimos visualizar aqui o nosso “form”, o nosso “Informações extras”. Perceba que aqui o visual já não ficou tão legal, mas depois nós vamos deixar ainda melhor esse nosso visual.

[07:13] Para finalizar, o que eu posso fazer é criar também um campo de e-mail, que é muito comum nos formulários preenchermos o e-mail. Então eu vou colocar aqui o “email” da pessoa que está fazendo essa pesquisa, então vai ser tipo “forms” também. Eu vou colocar aqui “forms.”.

[07:31] Nós já temos as propriedades “EmailField”, a “label” que eu vou utilizar vai ser “Email” mesmo. Eu vou falar também aqui que a quantidade máxima de caracteres vai ser de 150 caracteres.

[07:45] Voltando na aplicação, atualizando. Temos agora “Origem”, “Destino”, data de “Ida” e de “Volta”. Temos a “Data da pesquisa”, que não deixamos habilitado, temos aqui um “Primeira classe”, “Executiva” e “Econômica”. Eu vou deixar aqui o “Executiva”. Aqui em “Informações extras” vou escrever “ Info extra”. Tem aqui o “Email”. No “Email” eu vou colocar “gui@alura.com”.

[08:16] Quando eu clico em “OK”, olhe o que vai acontecer... Opa! Eu esqueci o “Origem” e o “Destino”! O principal eu esqueci. Vamos lá! São Paulo e vou para Minas Gerais, “São Paulo” e “Minas Gerais”. Quando eu clico em “OK”, exibe quatro informações. Por quê?

[08:35] Nós alteramos essas informações lá na nossa “index”, aqui no nosso “forms”, só que quando vamos exibir nós não alteramos, e precisamos alterar. Então aqui no “minha_consulta.html”, observe que eu tenho aqui só alguns valores. Eu quero os outros valores também.

[08:51] Então eu vou copiar esse link e vou colocar os outros campos também. Se eu não me engano, foram alguns outros campos. Então olhe: data de ida, data de volta; vamos visualizar lá. Já conseguimos ver!

[09:04] Então olhe: “Data da pesquisa”, “data_ida”, “data_volta” e “data_pesquisa”. Também temos além do “data” e da “pesquisa”, temos a classe de voo, “classe_viagem”, só para lembrarmos, “classe_viagem”, “informacoes”. Então aqui no “form” “informacoes” e o “email”.

[09:49] Então, vamos lá! “Sua data de volta é:”, não! “data_ida”, “data_volta”, “data_pesquisa”. Vou colocar “Pesquisa realizada em:”, só “Pesquisa realizada:”, já fica legal. Aqui “Classe de vôo”, “Informações extras”, “Sua data de volta é:” vai ser alterado para “Email:”. Salvei, voltando na aplicação. Eu voltei aqui só para não precisarmos preencher tudo de novo, quando eu clico em “OK”, agora nós temos todas as informações.

[10:47] “Sua origem é:” e “Seu destino é:”. “Sua data de ida é:”, “Sua data de volta é:”, “Pesquisa realizada: 03 de Março 2020 às 14:34”. Específico! “Classe de vôo: 2”, que foi o tipo que criamos lá, que vamos ver depois como alteramos isso também. “Informações extras:”, aqui eu coloquei “Info extra”, e o “Email:”.

[11:04] Legal! Então, dessa forma nós sabemos como manipular mais tipos dentro do “forms”. A coisa mais legal também, uma das coisas mais importantes é: observe que em nenhum momento eu precisei alterar o código que estamos de fato criando esse formulário. A única coisa que temos aqui, para cada campo visível, coloca o “form group” e exibe a “label e exibe o campo. Fizemos isso e agora temos o resultado. Temos um formulário com muito mais campos.

#### Widget tweaks

[Python Django Tweaks]('https://pypi.org/project/django-widget-tweaks/')
Formatação de widgets forms para renderizar no html. Facilita para adicionar conteúdo css no meu html.

---

[00:00] Assim que inserimos novos campos nós percebemos que o nosso formulário ficou todo bagunçado. Ele está bem maluco aqui!

[00:05] Então observe que temos aqui um campo mais para a esquerda que não está legal. Eu gostaria de dar um exemplo do que nós poderíamos fazer na nossa aplicação. Esse exemplo você não precisa fazer na sua casa, é só para observarmos.

[00:16] Eu vou dar um “inspect” aqui na página, vou selecionar aqui a seta do mouse e vou selecionar esse nosso campo de origem. Observe que aqui temos o HTML que foi gerado através do “form”. Eu vou editar e vou passar uma propriedade do Bootstrap, uma classe do Bootstrap para esse “input”, “class =”, e vou passar aqui o “form-control”. Vou fechando aqui a “streaming”.

[00:40] Observe como vai ficar o nosso “form-control”, nós teríamos a “label” em cima e embaixo o “input” de cada campo. Isso ficaria muito mais bonito, só que como eu passo essa propriedade, que é a “class form control” para todos os nossos campos, ou seja, lá na nossa aplicação nós temos aqui o “field”, que é o campo que nós temos.

[01:02] Só que eu quero falar assim: “todo o meu campo ‘field’ vai ser do tipo ‘form-control’. Ele vai utilizar uma classe do Bootstrap chamada ‘form-control’ ”. Ele ficaria com o visual, todos ficariam com um visual padrão. Vamos fazer isso, então?

[01:15] Para isso, nós vamos utilizar um módulo do Python. Eu vou escrever: “phyton django whitget tweaks”. Então clicando aqui nesse primeiro link nós temos aqui a documentação, como instalamos, como utilizamos essa biblioteca e como deixamos o nosso formulário de uma forma muito mais rápida e muito mais bonita.

[01:44] Então vamos instalar! Eu cliquei aqui para copiar. Havia saído da página, eu vou voltar aqui, vou fechar aqui do lado e abrir o nosso terminal. Teclas “Ctrl + L”, vou apertar as teclas “Ctrl + V” para instalar esse “whitget-tweaks”. Ele já instalou, é rápido. O que precisamos fazer?

[02:03] Lá nos nossos apps instalados precisamos colocar, precisamos falar: “olhe, nós vamos utilizar o ‘whitget-tweaks’ ”. Então eu vou minimizar aqui o nosso terminal e vou abrir aqui do lado. Então em “setup”, “setings.py”, onde temos todos os apps instalados nós vamos colocar também o que nós vamos utilizar, o “widget-tweaks”.

[02:26] Coloquei os dois, fiz o “import” dos dois, só que agora nós vamos ver se mudou. Será que só isso é suficiente para mudarmos aqui no nosso código? Não! Nós temos o mesmo código. Deixe-me fechar aqui. Observe que nós temos a mesma configuração, de alguma forma precisamos indicar lá no nosso formulário.

[02:43] Deixe-me fechar essas páginas para não ficarmos confusos, vou deixar só a página onde exibimos o nosso formulário aqui na nossa “index”. Nós precisamos indicar aqui na nossa “index” que vamos utilizar esse método do “widgets-tweaks”. E como fazemos isso?

[03:01] A primeira coisa: precisamos carregar esse módulo que instalamos aqui. Então eu vou utilizar o código Python com “{%}” e vou dar aqui o código “{% load widget_tweaks %}”. Importamos, carregou esse módulo aqui para a nossa página de links onde vamos utilizar.

[03:29] Agora o que eu quero fazer é adicionar o “form-control” para todos os meus outros campos. O que eu vou utilizar? Eu vou usar a reta transversal, a tecla “|”. Aqui eu vou colocar “{{field|add_class:'form-control'}}”. Eu vou apertar as teclas “Command + B” só para nós visualizarmos melhor.

[03:56] Então, o que eu fiz? Carreguei o “tweaks” e coloquei aqui do lado do “{{field|add_class: 'form-control'}}”. Salvei. Voltando na nossa aplicação e atualizando, nós temos aqui um visual bem melhor. Olhe só, muito melhor.

[04:13] Observe que os campos estão com um formato, eles estão bem grandes. Nós podemos alterar esse formato também. Por exemplo: eu posso criar aqui uma outra “section”. Deixe-me colar essa aqui embaixo só para fechar, então eu posso colocar aqui uma outra “section” e aqui eu posso trazer uma classe do Bootstrap, por exemplo, para alterarmos o tamanho desses nossos campos.

[04:37] Então eu vou colocar aqui o “col-8”, por exemplo. Quando atualizarmos, nós vemos que ele já diminuiu aqui. Outra coisa que podemos fazer também é colocá-lo dentro de um “container”. Eu vou colocar aqui “container”, vamos ver como vai ficar, muito melhor.

[04:56] Então temos um “container” agora para essa nossa classe. Observe que todos os outros campos ficaram com um tamanho padronizado. Além de quando selecionamos o campo, ele dá essa marcação azul também.

[05:07] Então eu vou colocar aqui: “São Paulo”, destino vai ser “Minas Gerais”. Eu vou amanhã no dia 04, e volto no dia 20, por exemplo. Aqui, a data de pesquisa nós não podemos preencher. Tipo de classe eu vou de executiva. Em informações extras eu não vou preencher nada, nós vamos ver o que ele vai fazer. Aqui no e-mail “gui@alura.com”.

[05:39] Quando eu clico em “OK” nós temos lá todas as nossas informações, e informações extras não mostrando nada. Aqui conseguimos submeter esse formulário, agora muito mais organizado.

#### Faça como eu fiz na aula

Chegou a hora de você seguir todos os passos realizados por mim durante esta aula. Caso já tenha feito, excelente. Se ainda não, é importante que você implemente o que foi visto no vídeo para poder continuar com a próxima aula, que tem como pré-requisito todo o código aqui escrito.

#### Para saber mais

Tipos de campos do fomulário e widgets
Um widget é uma representação do Django de um elemento input do HTML e a biblioteca do Forms vem com um conjunto de classes de campo diferentes.

Abaixo, segue uma lista com os tipos mais comuns:

- BooleanField | Widget* padrão: CheckboxInput
- CharField | Widget padrão: TextInput
- ChoiceField | Widget padrão: Select
- TypedChoiceField | Semelhante ao ChoiceField, porém recebe dois argumentos extras: coerce e empty_value. | Widget padrão: Select
- DateField | Widget padrão: DateInput
- DecimalField | Widget padrão: NumberInput quando Field.localize for False, senão TextInput.
- EmailField | Widget: EmailInput.
- Outros tipos: Você pode encontrar outros tipos de campos clicando [neste link]('https://docs.djangoproject.com/en/3.0/ref/forms/fields/#built-in-field-classes').

: )

#### O que aprendemos?

Nesta aula:
- Criamos novos campos no formulário como data da pesquisa, informações extras e email;
- Adicionamos a classe form-control nos campos sem duplicar o código, utilizando o widget tweaks.

Na próxima aula
Vamos aprender como incluir validações no formulário de duas formas diferentes!

### 4. Validações
#### [Clean_field]('https://docs.djangoproject.com/en/4.0/ref/forms/validation/')

A DJANGO possui um forma muito fácil de validar formulários.

1. Em forms.py devemos:

    class PassagemForms(forms.Form):
        ...
        def clean_origem(self):
            origem = self.cleaned_data['data'] # retorna o erro
            origem = self.cleande_data.get('origem')
            if any(char.isdigit() for char in origem):
                raise forms.ValidationError('Origem inválida: Não inclua número neste campo!')
            else:
                return origem

1. Em views.py:

    def revisao_consulta(request):
        if request.method == 'POST':
            ...
            if form.is_valid():
                contexto = {'form':form}
                return render(request, 'minha_consulta.html', contexto)
            else:
                print('Form inválido)
                contexto = {'form':form}
                return render(request, 'index.html',contexto)


---

[00:00] Um trabalho muito comum quando utilizamos formulário, é validar os campos. O que acontece aqui?

[00:05] Observe que eu preenchi todos os campos aqui, aparentemente eles estão corretos, porém na hora de escrever “São Paulo” eu esbarrei na letra “0”, ao invés de colocar a letra “o”. Quando eu submeto este formulário, eu dou aqui um “OK”, aparece aqui o “São Paul0” com o “0”, e não a letra “o”.

[00:21] O que eu queria fazer? Eu queria validar esse campo, eu queria não permitir que dígitos numéricos fossem permitidos aqui no campo “Origem” e que ele exibisse uma mensagem de erro para facilitar a pessoa que está mexendo no sistema. Então ele fala: “olhe, não inclua dígitos nesse campo”, por exemplo. Vamos fazer isso?

[00:39] O Django fornece duas maneiras de validarmos os campos, neste vídeo eu quero mostrar uma delas. A primeira coisa que vamos fazer vai ser acessar o nosso arquivo “forms.py”. Nesse nosso arquivo, observe que eu tenho aqui a minha classe “PassagemForms”.

[00:55] Ainda nesta classe, eu vou clicar aqui, vou apertar a tecla “Enter”. Eu ainda estou nessa classe. Perceba que eu tenho aqui um “tab”, ou quatro espaços. Eu vou criar um método para validar, para saber se eu tenho caracteres numéricos no campo de origem.

[01:10] Então eu vou criar aqui uma função “def”, essa função eu preciso nomeá-la de “clean”, “clean_” e o nome do campo que eu quero validar. Eu quero validar o campo “Origem”, então eu vou colocar aqui “clean_origem”. Como argumento, sempre quando acessamos um formulário, nós estamos instanciando essa classe “PassagemForms”.

[01:36] Então, o que eu vou fazer? Sempre quando eu quiser validar esse “Origem”, eu quero passar a instância que estiver sendo exibida lá, então eu vou passar aqui a palavra “self”. O que nós precisamos fazer agora é buscarmos o valor que está no campo de “Origem” para sabermos, para conseguirmos validar.

[01:53] Então eu vou armazenar essa informação dentro dessa variável “Origem”. Como eu consigo recuperar para validar esse campo de “Origem”? O Django fornece duas formas de conseguirmos recuperar esse valor. A primeira eu vou utilizar a instancia que eu estou, “self”, e temos uma propriedade chamada “clean data”.

[02:15] Se eu usar apenas o “clean data” e retornar o campo de “Origem” utilizando “[ ]” aqui, o que vai acontecer? Caso esse meu campo esteja vazio, esteja em branco, o Django vai retornar um “key error” para mim, e não é isso o que eu quero. Se o campo estiver em branco, eu quero receber como retorno um “none”, por exemplo, um campo vazio.

[02:38] Então, o que vamos fazer? No lugar de usar o “[ ]”, vamos utilizar o “( )” e vamos utilizar aqui na frente “cleaned_data.get”. Está bom, qual é a diferença desse aqui para o primeiro que eu tinha mostrado? A diferença é que esse, caso o campo dele esteja em branco, ele vai nos retornar um “none”, e é o que queremos. Então vamos utilizar o “cleaned_data.get”, e vamos utilizar “( )” o nome do campo que queremos validar.

[03:12] Criei aqui o meu campo. O que eu quero fazer agora é validar, eu quero de fato saber se esse campo tem ou não algum carácter numérico. Então vamos fazer isso!

[03:23] Vou criar aqui um “if”. Se algum carácter for numérico, eu vou colocar aqui “any”. Aqui eu vou buscar “char.isdigit()”. Se alguns desses dígitos for numérico, para cada letra dentro de “Origem” se algum deles for numérico eu quero exibir uma mensagem de erro. Então eu vou colocar aqui um “raise forms.ValidationError()” e aqui eu vou passar a minha mensagem de erro, eu vou passar “Origem inválida: Não inclua números”, algo desse tipo.

[04:14] Passei aqui a mensagem de erro. Caso não tenha nenhum dígito numérico, o que eu quero fazer? Eu vou colocar aqui um “else”, eu quero retornar, “return origem”, eu quero dizer, “Origem” está correto, nós podemos contar que não tem nenhum carácter numérico nesse campo.

[04:37] Salvei o meu “forms”. Agora, o que eu tenho que fazer? Observe que aqui na minha “view” eu tenho aqui. Eu verifico se é uma requisição “POST”, pego o formulário dessa requisição, depois pego ele por contexto e passo para a minha consulta.

[04:52] Em nenhum momento nós estamos verificando se o formulário é válido, e para provar isso olhe só: eu tenho aqui o meu formulário, se eu der aqui um “OK”, eu vou para a página de “minha_consulta”, onde os dados já estariam validados, e não é isso o que quero. Eu quero dar um “OK” e continuar nessa página, exibindo a mensagem de erro. Então, o que eu preciso fazer?

[05:12] Eu preciso verificar, eu peguei o formulário da requisição e já estou enviando ele por contexto. Não! Antes de enviar por contexto, eu quero verificar se esse formulário é válido. E como eu faço isso?

[05:23] Vamos perguntar se o “if form.is_valid”. Se ele for válido, se for um formulário válido, eu quero pegá-lo por contexto e mandá-lo aqui para a página de “minha_consulta”. Caso não seja, caso esse formulário não seja válido, eu quero fazer alguma coisa.

[05:46] Eu vou exibir aqui um print, por exemplo, só para visualizarmos no nosso terminal, “print(‘Form inválido’)”. Eu vou fazer o seguinte: eu vou pegar o conteúdo de contexto desse nosso formulário e vou retornar para a página, não mais de “minha_consulta”, mas para a página de “index”.

[06:08] Então, o que vai acontecer? Se o meu formulário for válido, eu vou para a página de “minha_consulta”. Se ele não for válido, eu vou pegar todo conteúdo que está neste formulário, passando ele por contexto, e vou mandá-lo de novo para a minha página de “index”. Então eu não vou conseguir visualizar a página de “minha_consulta” caso o meu formulário não seja válido.

[06:32] Estou aqui com “São Paul0” com “0” e vou dar um “OK”. Continuamos aqui em “São Paul0”, vamos ver no nosso terminal. Abrindo o nosso terminal, temos aqui um “Form inválido”.

[06:41] Legal, conseguimos um resultado que queríamos! Só que se eu colocar aqui, se eu tirar esse “0” e colocar o “o”, “São Paulo”; eu vou para o “Rio de Janeiro”. Dou um “OK”. Vamos visualizar a página de “minha_consulta”. Isso ficou legal, só que faltou um ponto: não conseguimos visualizar a mensagem de erro que criamos. É isso o que vamos fazer no próximo vídeo!

#### Exibindo mensagem de erro

Para exibir as mensagens de erro de validação de formulários devemos:

1. No index.html:

        <form>
            ...
            {{ field.errors }}
        </form>

    ou

        <form> #validando e formatando o html
            ...
            {% for error in field.errors %}
            <section class="alert alert-danger" role="alert">
                {{ field.errors }}
            </section>

        </form>

---

[00:00] Um trabalho muito comum quando utilizamos formulário, é validar os campos. O que acontece aqui?

[00:05] Observe que eu preenchi todos os campos aqui, aparentemente eles estão corretos, porém na hora de escrever “São Paulo” eu esbarrei na letra “0”, ao invés de colocar a letra “o”. Quando eu submeto este formulário, eu dou aqui um “OK”, aparece aqui o “São Paul0” com o “0”, e não a letra “o”.

[00:21] O que eu queria fazer? Eu queria validar esse campo, eu queria não permitir que dígitos numéricos fossem permitidos aqui no campo “Origem” e que ele exibisse uma mensagem de erro para facilitar a pessoa que está mexendo no sistema. Então ele fala: “olhe, não inclua dígitos nesse campo”, por exemplo. Vamos fazer isso?

[00:39] O Django fornece duas maneiras de validarmos os campos, neste vídeo eu quero mostrar uma delas. A primeira coisa que vamos fazer vai ser acessar o nosso arquivo “forms.py”. Nesse nosso arquivo, observe que eu tenho aqui a minha classe “PassagemForms”.

[00:55] Ainda nesta classe, eu vou clicar aqui, vou apertar a tecla “Enter”. Eu ainda estou nessa classe. Perceba que eu tenho aqui um “tab”, ou quatro espaços. Eu vou criar um método para validar, para saber se eu tenho caracteres numéricos no campo de origem.

[01:10] Então eu vou criar aqui uma função “def”, essa função eu preciso nomeá-la de “clean”, “clean_” e o nome do campo que eu quero validar. Eu quero validar o campo “Origem”, então eu vou colocar aqui “clean_origem”. Como argumento, sempre quando acessamos um formulário, nós estamos instanciando essa classe “PassagemForms”.

[01:36] Então, o que eu vou fazer? Sempre quando eu quiser validar esse “Origem”, eu quero passar a instância que estiver sendo exibida lá, então eu vou passar aqui a palavra “self”. O que nós precisamos fazer agora é buscarmos o valor que está no campo de “Origem” para sabermos, para conseguirmos validar.

[01:53] Então eu vou armazenar essa informação dentro dessa variável “Origem”. Como eu consigo recuperar para validar esse campo de “Origem”? O Django fornece duas formas de conseguirmos recuperar esse valor. A primeira eu vou utilizar a instancia que eu estou, “self”, e temos uma propriedade chamada “clean data”.

[02:15] Se eu usar apenas o “clean data” e retornar o campo de “Origem” utilizando “[ ]” aqui, o que vai acontecer? Caso esse meu campo esteja vazio, esteja em branco, o Django vai retornar um “key error” para mim, e não é isso o que eu quero. Se o campo estiver em branco, eu quero receber como retorno um “none”, por exemplo, um campo vazio.

[02:38] Então, o que vamos fazer? No lugar de usar o “[ ]”, vamos utilizar o “( )” e vamos utilizar aqui na frente “cleaned_data.get”. Está bom, qual é a diferença desse aqui para o primeiro que eu tinha mostrado? A diferença é que esse, caso o campo dele esteja em branco, ele vai nos retornar um “none”, e é o que queremos. Então vamos utilizar o “cleaned_data.get”, e vamos utilizar “( )” o nome do campo que queremos validar.

[03:12] Criei aqui o meu campo. O que eu quero fazer agora é validar, eu quero de fato saber se esse campo tem ou não algum carácter numérico. Então vamos fazer isso!

[03:23] Vou criar aqui um “if”. Se algum carácter for numérico, eu vou colocar aqui “any”. Aqui eu vou buscar “char.isdigit()”. Se alguns desses dígitos for numérico, para cada letra dentro de “Origem” se algum deles for numérico eu quero exibir uma mensagem de erro. Então eu vou colocar aqui um “raise forms.ValidationError()” e aqui eu vou passar a minha mensagem de erro, eu vou passar “Origem inválida: Não inclua números”, algo desse tipo.

[04:14] Passei aqui a mensagem de erro. Caso não tenha nenhum dígito numérico, o que eu quero fazer? Eu vou colocar aqui um “else”, eu quero retornar, “return origem”, eu quero dizer, “Origem” está correto, nós podemos contar que não tem nenhum carácter numérico nesse campo.

[04:37] Salvei o meu “forms”. Agora, o que eu tenho que fazer? Observe que aqui na minha “view” eu tenho aqui. Eu verifico se é uma requisição “POST”, pego o formulário dessa requisição, depois pego ele por contexto e passo para a minha consulta.

[04:52] Em nenhum momento nós estamos verificando se o formulário é válido, e para provar isso olhe só: eu tenho aqui o meu formulário, se eu der aqui um “OK”, eu vou para a página de “minha_consulta”, onde os dados já estariam validados, e não é isso o que quero. Eu quero dar um “OK” e continuar nessa página, exibindo a mensagem de erro. Então, o que eu preciso fazer?

[05:12] Eu preciso verificar, eu peguei o formulário da requisição e já estou enviando ele por contexto. Não! Antes de enviar por contexto, eu quero verificar se esse formulário é válido. E como eu faço isso?

[05:23] Vamos perguntar se o “if form.is_valid”. Se ele for válido, se for um formulário válido, eu quero pegá-lo por contexto e mandá-lo aqui para a página de “minha_consulta”. Caso não seja, caso esse formulário não seja válido, eu quero fazer alguma coisa.

[05:46] Eu vou exibir aqui um print, por exemplo, só para visualizarmos no nosso terminal, “print(‘Form inválido’)”. Eu vou fazer o seguinte: eu vou pegar o conteúdo de contexto desse nosso formulário e vou retornar para a página, não mais de “minha_consulta”, mas para a página de “index”.

[06:08] Então, o que vai acontecer? Se o meu formulário for válido, eu vou para a página de “minha_consulta”. Se ele não for válido, eu vou pegar todo conteúdo que está neste formulário, passando ele por contexto, e vou mandá-lo de novo para a minha página de “index”. Então eu não vou conseguir visualizar a página de “minha_consulta” caso o meu formulário não seja válido.

[06:32] Estou aqui com “São Paul0” com “0” e vou dar um “OK”. Continuamos aqui em “São Paul0”, vamos ver no nosso terminal. Abrindo o nosso terminal, temos aqui um “Form inválido”.

[06:41] Legal, conseguimos um resultado que queríamos! Só que se eu colocar aqui, se eu tirar esse “0” e colocar o “o”, “São Paulo”; eu vou para o “Rio de Janeiro”. Dou um “OK”. Vamos visualizar a página de “minha_consulta”. Isso ficou legal, só que faltou um ponto: não conseguimos visualizar a mensagem de erro que criamos. É isso o que vamos fazer no próximo vídeo!

#### Clean

O método clean faz a validação do formulário conforme o tipo de campo. É necessário fazer a seguinte validação:

1. Em forms.py:

            class PassagemForm():
            ...
            def clean(self):
                origem = self.cleaned_data.get('origem')
                destino = self.cleaned_data.get('destino')
                if origem == destino:
                    self.add_error('destino','Origem e destino não podem ser iguais')
                return self.cleaned_data

    ou

1. Podemos criar um arquivo para validação dos formulários, Criamos o arquivo validation.py e adicionamos as funções:

        def origem_destino_iguais(origem, destino, lista_de_erros):
            if origem == destino:
                lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'
    
        def campo_texto(valor_campo, nome_campo, lista_de_erros):
            if any(char.isdigit() for char in valor_campo):
                lista_de_erros[nome_campo] = 'Não inclua números neste campo'
        
1. Em forms.py, devemos utilizar apenas o método clean:

        def clean(self):
            origem = self.cleaned_data.get('origem')
            destino = self.cleaned_data.get('destino')
            lista_de_erros = {}
            campo_texto(origem, 'origem', lista_de_erros)
            campo_texto(destino, 'destino', lista_de_erros)
            origem_destino_iguais(origem, destino, lista_de_erros)
            if lista_de_erros is not None:
                for erro in lista_de_erros:
                    mensagem_erro = lista_de_erros[erro]
                    self.add_error(erro, mensagem_erro)
            return self.cleaned_data

---

[00:00] Vimos uma forma de validarmos cada campo do nosso formulário através deste método “clean_” e o nome do campo que queremos validar. Eu vou mostrar agora uma outra forma que podemos validar todos os campos do nosso formulário em apenas um método, que vai ser o método “clean”.

[00:14] Eu vou criá-lo aqui embaixo, “def”. Eu vou criar uma função que vou chamar só de “clean”, não vou mais especificar qual é o nome do campo que eu quero validar. Da mesma forma, nós vamos passar como um argumento a instância que tivermos na nossa página HTML.

[00:32] Para começarmos, nós vamos recuperar os valores tanto de “origem” e “destino” e de todos os outros campos da mesma forma. Então eu vou dar um “Ctrl + C” aqui, trouxe “origem”. Eu vou dar “Ctrl + V”, “Ctrl + C”, e aqui “Ctrl + V”. Trouxe aqui o campo “destino”. O que eu quero fazer agora?

[00:49] Eu quero incluir outras validações como, por exemplo, se “origem” e “destino” são iguais. E como eu vou fazer isso? Por exemplo: eu posso comparar aqui embaixo, se “origem == destino”. Se eles forem iguais, eu quero inserir uma mensagem de erro, eu quero enviar uma mensagem de erro. Como eu posso enviar essa mensagem de erro? Eu posso fazer da seguinte forma.

[01:14] Se esses dois campos forem de fato iguais, eu vou enviar essa mensagem de uma forma diferente. Eu vou fazer assim: “self.add_error”, vou colocá-lo aqui e vou falar qual é o nome do campo que eu quero deixar com uma mensagem de erro. Eu vou deixar no campo “destino” e no segundo parâmetro eu vou passar qual é de fato a mensagem de erro.

[01:44] Então eu vou falar que “origem” e “destino” não podem ser iguais. Vou salvar. Caso não tenhamos um erro, o que eu vou fazer? Eu vou retornar, vou colocar aqui um “return” nos objetos. A instância dessa minha classe “self.cleaned_data”, ou seja, eu vou retornar os valores validados, os valores verificados.

[02:16] Então eu vou voltar para a minha aplicação, vou dar aqui um “OK”. Tem aqui “São Paulo”, “Rio de Janeiro”. Legal! Deixe-me voltar, vou colocar “São Paulo” e “São Paulo”. Quando eu vir aqui e apertar em “OK” aparece “Origem e destino não podem ser iguais”. Ficou legal, só que pare para pensar no seguinte: temos o campo de “clean_origem”, “clean_destino” e o campo “clean”. O que acontece?

[02:46] Quando especificamos o “clean” para um determinado campo, ele sempre é chamado antes desse nosso método “clean”. Por exemplo: se eu colocar aqui no lugar de “São Paul0” um “0”, olhe só o que vai acontecer. Eu vou dar um “OK” e teremos aqui “Origem inválida”. Ele não fez ainda a verificação do “São Paul0” e do “São Paulo”, dos dois destinos iguais.

[03:03] E se eu colocar aqui os dois destinos como “São Paul0” e “São Paul0”, olhe o que vai acontecer. Ele vai duplicar as minhas mensagens de erro. Esse comportamento está um pouco estranho, nós não queremos mensagens de erros duplicadas. Então, o que vamos fazer?

[03:16] Vamos centralizar toda nossa verificação no método “clean”, essa é uma decisão que tomamos para esse projeto. Então, o que eu vou fazer? No lugar de manter cada verificação e cada validação, a lógica da nossa validação aqui, eu vou criar um outro arquivo para manter a lógica da nossa validação em uma outra pasta. Caso novas validações surjam, nós vamos colocando todas elas nesse arquivo de validação.

[03:45] Por exemplo: eu posso criar esse arquivo aqui dentro de “Passagem”, eu vou chamar de “validation.py”, dentro desse “validation.py” eu quero verificar se “origem” e “destino” são iguais, por exemplo. Então, como eu vou fazer isso?

[04:00] Aqui no “validation.py” eu vou criar uma função “def” e vou chamar de “origem_destino_iguais()”. O que eu vou fazer? Como argumento nós vamos fazer algo diferente. Observe que a medida que novas validações vão surgindo, que vamos inserindo, o que temos que fazer? Temos que colocar “self.add_error” e depois colocar o nome do campo que queremos que seja vinculado o erro e a mensagem do erro.

[04:32] Eu posso criar uma lista de erros, por exemplo. Eu posso fazer assim: “lista_erros”, uma lista de erros. Dentro dessa minha lista de erros eu posso fazer assim, “lista_erros = {}”. O que vai acontecer? Nós vamos inserir cada erro que tivermos nessa lista de erro, depois nós varreremos essa lista de erro para exibir as mensagens de erro.

[04:58] Então, o que eu vou fazer? Eu vou remover, esse “origem” e “destino” não podem ser iguais, vou apertar as teclas “Command + X”, vou vir aqui no meu “validation”, e essa nossa função de origem e destinos iguais. Nós vamos receber como parâmetro o campo de “origem”, e o campo de “destino”.

[05:11] Então eu vou colocar aqui “origem”, “destino”. Vou receber também a “lista_de_erros”. Então se “origem” e “destino” são iguais, eu vou atribuir na lista de erros. Vou pegar aqui “lista_de_erros” e vou atribuir nessa minha lista de erros essa mensagem aqui de “destino”, o campo “Origem e destino não podem ser iguais”.

[05:55] O que eu vou fazer? Lembra que eu preciso indicar qual é o campo que está recebendo a mensagem de erro? Para isso, eu vou colocar aqui na frente da nossa lista de erro via “[ ]”. O campo que eu tenho, eu vou colocar no campo “ 'destino' “. Olhe só que legal vai ficar! Então temos uma lista de erro onde especificamos o campo que vamos receber o erro e depois colocamos esse erro lá dentro. Legal!

[06:19] Uma outra validação que podemos colocar aqui também é para saber se temos algum carácter numérico. Então eu vou pegar esse aqui, vou passar aqui para o lado e vou criar uma outra função. Já que todas as nossas validações ficaram nesse campo, eu vou criar uma função que vou chamar aqui de “campo_tem_algum_numero”. E o que eu vou receber como parâmetro?

[06:53] Observe que verificamos se o campo “destino” e o campo “origem” tinham algum valor, então eu posso receber outros campos, então eu vou passar algumas informações. Por exemplo: o valor do campo que eu quero verificar qual o conteúdo desse campo. Eu vou passar o nome do campo “nome_campo” que eu quero verificar e vou passar também a “lista_de_erros”. O que eu vou fazer aqui? Eu vou verificar se tivermos algum carácter, algum dígito numérico no valor do campo.

[07:29] No lugar desse “raise forms”, o que eu vou fazer? Aqui eu vou colocar uma validação, vou colocar na nossa lista de erros. Qual vai ser o nome do campo aqui? Qual é o campo que eu vou utilizar? Depende, eu vou passá-lo por parâmetro, nome do campo via “string” e posso falar, por exemplo, “Não inclua números neste campo”. Vou salvar.

[08:06] Aqui eu fiz duas validações. Voltando aqui no nosso “forms”, o que eu vou fazer? Temos o campo “origem”, temos o campo “destino” e fizemos outra validação que é “origem” e “destino =”, nós pegamos para esses dois.

[08:19] Eu vou remover esses dois “clean” porque nós vamos centralizar a nossa verificação apenas no método “clean”, então temos “origem”, “destino” e temos a “lista_de_erros”. O que eu preciso fazer agora são alguns passos.

[08:29] Eu preciso verificar como eu invoco os erros que estão lá no meu “validation.py”. A primeira coisa que eu preciso fazer é trazer esses métodos que eu criei no “validation.py” aqui para dentro, então eu vou fazer assim: “from passagens.validation import”. Eu quero importar todos os métodos de validação que eu tenho lá, então eu vou colocar aqui um “*”. Dessa forma eu trago esses dois métodos de validação.

[09:00] O que eu vou fazer? Aqui vai ser algo muito legal, muito interessante, para eu conseguir validar se tem algum número no campo de “origem”, por exemplo. Eu posso trazer aqui “campo_tem_algum_numero”, ele já me trouxe. Entre parênteses eu vou passar qual é o campo que quero validar.

[09:15] Eu quero validar o campo “origem”. Ele dá qual é o nome do campo que eu estou usando, eu estou usando o campo “origem”. Para finalizar, eu vou passar a “lista_de_erro”, eu vou colocar “lista_de_erros” e vou alterar aqui também para ficar mais fácil, “lista_de_erros”. Legal!

[09:40] Fiz isso para saber se tem algum número no “origem”. Eu vou fazer agora para ver se tem algum número também no “destino”. Observe que antes eu tinha a função inteira, o método inteiro duplicado. Agora não, eu tenho uma linha para ter o mesmo resultado. Vou colocar aqui, o nome do campo é “ 'destino' ” e vou passar também a “lista_de_erro”.

[10:00] E outra coisa: eu quero saber também se a origem e o destino são iguais, então eu vou passar assim “origem_destino_iguais” e vou passar como parâmetro aqui o “origem”, vai ser “origem” mesmo. “, destino, lista_de_erros”. Outra coisa que eu posso fazer para deixar a nossa função ainda mais clara e muito melhor de entender é colocar “docstrings” nas nossas funções.

[10:25] Por exemplo essa função, o que estamos fazendo? Eu vou colocar aspas e vou fazer assim: “ “““Verifica se origem e destino são iguais””” ”. Que interessante! Quando eu passo o mouse em cima, ele já me fala aqui embaixo se “origem” e “destino” são iguais. “ ””“Verifica se origem e destino são iguais””” ”.

[10:54] O que eu estou fazendo nessa função aqui? Nesse método que criamos de validação, eu estou vendo se “ “““Verifica se possui algum dígito numérico”““ “, na nossa função quando passamos o mouse em cima, “ “““Verifique se possui algum dígito numérico”““ “, e aqui “ “““Verifique se origem e destino são iguais”““ “. Legal!

[11:26] Fiz as três verificações, tanto do “origem” como do “destino”, para ver se tem campos numéricos ou se tem dígitos numéricos, ou se o “origem” e o “destino” são iguais.

[11:37] O que eu quero fazer agora é verificar se eu tenho erro. Então eu vou perguntar se a minha “lista_de_erros” não for vazia, ou seja, se ela tiver algum erro, então eu vou colocar “is not None:”. Se ela não for vazia, significa que eu tenho erros.

[11:54] Então, o que eu preciso fazer? Para cada erro dentro da minha “lista_de_erros”, eu quero pegar a mensagem que eu tenho de cada erro. Então eu vou fazer assim: “mensagem”, eu vou criar uma variável, por exemplo: “mensagem_erro = “ e eu vou pegar a lista de mensagens que eu tenho, o conteúdo que eu tenho dos erros dessa mensagem.

[12:20] Então, “lista_de_erros” e vou pegar aqui o “(erro)” e além disso, eu vou atribuir o erro em cada um desses campos. Então, “self.add.error”. Da mesma forma que tínhamos feito anteriormente, eu vou passar aqui o “erro”, que vai ser o nome do campo, a mensagem de erro, que vai ser a mensagem de erro que criamos ali. Dessa forma conseguimos validar os nossos campos. Vamos verificar?

[12:51] Então, o que nós fizemos? Vimos se essa lista que temos é vazia. Se ela não for vazia, nós vamos pegar para cada erro dentro dessa lista de erros que criamos aqui no nosso “validation”, aqui tem a “lista_de_erros”, aqui ela não está vazia.

[13:02] Então caso esses erros aconteçam de fato, eu vou pegar a mensagem de erro de cada lista e vou adicionar pegando o erro, porque eu peguei cada um dessa lista de erro, então tem um erro em “destino”. Ele vai pegar o “destino” e vai exibir a mensagem de erro. Legal!

[13:19] Salvei. Voltando na nossa aplicação, eu vou colocar “São Paul0” e “Rio de Janeiro”, e fazemos o teste dessas validações, dei um “OK”. “Não inclua números neste campo”. Legal! Eu vou incluir número neste campo, “Rio de Janeir0”, vou colocar um “0” também. Dei um “OK”.

[13:37] “Não inclua número neste campo” e “Não inclua número neste campo”. Vou deixar “São Paulo” e aqui embaixo também “São Paulo”. Assim também, os dois iguais. Quando eu dou um “OK”, observe que a nossa mensagem não está mais duplicada. Ele fala: “Não inclua número neste campo”, “Origem e destino são iguais”. Opa! Então eu vou tirar.

[13:54] Eu vou colocar aqui São Paulo, Rio de Janeiro, só que em cima eu também vou colocar Rio de Janeiro, vamos ver o que vai acontecer, tirei o número, “origem” e “destino” não podem ser iguais”. Se eu coloco “São Paulo” e dou um “OK”, nós conseguimos passar. Submeteu o formulário certo.

#### Validando datas

[00:00] Conseguimos submeter o nosso formulário aqui, por exemplo: “São Paulo” e “Rio de Janeiro”. Se eu dou um “OK”, temos aqui o nosso formulário certo. “Sua origem é: São Paulo”, “Seu destino é: Rio de Janeiro”. Vamos fazer agora algumas validações em relação à data.

[00:12] Observe aqui que, por exemplo, não faz muito sentido eu colocar aqui a minha data de ida dia 10, e minha data de volta dia 5, não faz sentido. Como eu vou viajar no dia 10/03 e voltar no dia 05/03/2020? Vou voltar no tempo, entrar no avião e voltar no tempo. Não existe isso, precisamos validar isso também. É o que nós vamos fazer!

[00:32] O que nós vamos verificar? Se a data de ida for maior do que a data de volta, nós vamos falar uma mensagem: “Data de ida não pode ser maior do que data de volta”. Vamos fazer isso?

[00:42] Lá no nosso arquivo de validação “.py” eu vou criar uma função. Essa função eu vou chamar de “data_ida_maior_que_data_volta” e vou receber como argumento a “data_ida, data_volta, lista_de_erros”. Recebi esses três como parâmetro. Coloco aqui a minha “docstring” para ficar legal, “ ““Verifica se data de ida é maior que data de volta”““ “. Vamos criar agora essa nossa função.

[01:34] Então eu vou perguntar se “data_ida > data_volta”. O que eu quero fazer? Eu quero incluir uma mensagem de erro na nossa lista de erro, então na “lista_de_erros” eu vou ter uma mensagem que eu vou colocar esse “data_ida”, vou colocar ele aqui na data de ida. Na data de ida? É, pode ser na data de ida, só que essa data de ida aqui precisa ser uma “string”.

[02:09] Então eu vou colocar aqui a “string”, porque estamos falando do nome do campo que queremos inserir o erro. Aqui, colocando “ = “ eu vou colocar a mensagem de erro, eu vou colocar “Data de ida não pode ser maior que data de volta”. Essa data de ida e data de volta, na verdade como estamos falando “A Data de volta está maior”, eu vou alterar aqui.

[02:40] Eu vou colocar aqui “data_volta”, melhor. Salvei. Observe que interessante: eu criei uma função, criei essa função aqui. O que eu preciso fazer? Aqui no meu “forms” eu só vou chamar essa função. Então, duas coisas que eu tenho que fazer, trouxemos aqui o “origem” e o “destino”. Eu preciso também trazer a “data_ida” e a “data_volta”.

[03:07] Então eu vou trazer aqui “data_ida” e nós vamos buscar nosso formulário que se chama “data_ida”. Aqui embaixo, “data_volta”, “data_volta”, os mesmos nomes que demos aqui criando o nosso “forms”, “data_ida” e “data_volta”.

[03:29] O que eu tenho que fazer agora que eu tenho a data de ida e tenho a data de volta? É chamar aqui essa nossa verificação, “data_ida_maior_que_data_ volta”. Então quando colocamos aqui, repare que legal.

[03:46] Para auxiliarmos, precisamos passar a data de ida como argumento, “data_ida”. Precisamos passar a “data_volta” e precisamos passar também “lista_de_erros”. E temos aqui, “Verifique se data de ida é maior que data de volta”. Salvei, validation.py e salvei também.

[04:03] Voltando aqui, “São Paulo” e “Rio de Janeiro”. Não temos erros nessas verificações, só que minha data de ida é maior do que a data de volta. Vou dar um “OK” e nós temos aqui na data de volta: “Data ida não pode ser maior que data de volta”, ou, “Data de volta não pode ser menor”, podemos deixar assim também.

[04:21] Então, “Data de volta não pode ser menor que data de ida”. Vou dar um “OK” de novo só para vermos a mensagem. “Data de volta não pode ser maior que data de ida”.

[04:40] Outra coisa que podemos fazer em relação da data é, por exemplo: hoje é dia 04, eu não vou colocar erro nessa, eu vou voltar no dia 10. Legal! Estou indo no dia 04 e volto no dia 10, só que, se eu colocar que eu quero viajar no dia 03 (ontem), eu quero comprar uma passagem de ontem para voltar no dia 10. Nós temos algo muito interessante aqui agora.

[05:00] Nós temos no nosso formulário, quando fizemos essa pesquisa, a data pesquisa, então podemos verificar se a data de ida for menor do que a data da pesquisa. Se for menor, podemos falar: “Não é possível comprar passagens nessa data” ou “ A data de ida não pode ser menor que a data de hoje”, porque aqui na data da pesquisa nós sempre pegamos a data de hoje.

[05:21] Então vamos criar essa validação também para a nossa data. Nós vamos fazer algo muito parecido. Apareceu uma função que eu vou verificar se “data_ida_menor_data_de_hoje”, e como argumento nós vamos passar a “data_ida”. Nós vamos passar a “data_pesquisa”, que é a nossa data de hoje, porque já sabemos que foi garantida a nossa data de hoje. Vou passar aqui a “lista_de_erros”. Legal!

[06:06] Como argumento, eu vou colocar aqui nossa “docstring”, eu vou fazer assim: “ “““Verifica se data de ida é menos que data de hoje”““ “ e nós vamos verificar: “if data_ida < data_pesquisa:”, se for menor do que a data da pesquisa, o que eu quero fazer?

[06:39] Eu quero criar aqui a nossa lista de erros, eu quero adicionar na lista de erros no campo “data_ida” o seguinte erro: “Data de ida não pode ser menor que data de hoje”. Menor que hoje, será que dá? Acho que menor que hoje está legal.

[07:13] O que eu vou fazer aqui? Tenho o data de ida, tenho o data de volta e vou buscar também o data da pesquisa, “data_pesquisa”. Então eu apertei aqui as teclas “Ctrl + V” e vou chamar aqui “data_pesquisa = self.cleaned.data.get ('data_pesquisa')”. Nós vamos ver se está certo, “data_pesquisa”, e “data_pesquisa”. Legal!

[07:51] Eu trouxe aqui o “data_pesquisa” e o que eu tenho que fazer agora é chamar essa função, “data_ida_menor_data_hoje”. Então, vamos lá! Eu vou passar a “data_ida”, que já temos porque já buscamos. É uma das vantagens de utilizar o nosso método “cleaned”. Agora podemos comparar os campos e conseguimos todas as informações do nosso formulário, para validarmos.

[08:16] Passei a “data_ida”, vou passar o “data_pesquisa” e vou passar também a “lista_de_erros”. Salvei. Voltando na nossa aplicação, o que vamos fazer aqui? Eu quero viajar ontem para voltar no dia 10, não faz sentido. Eu vou colocar um “OK”. Deu um pequeno problema aqui, deixe-me ver.

[08:42] Acho que eu escrevi algo errado, vou abrir aqui o meu terminal, linha 28. Opa! Aqui eu fiz errado mesmo, eu esqueci de passar a propriedade “data_pesquisa”, mas eu tenho a “data_pesquisa” ali. Deixe-me voltar aqui. Então vamos ver, “origem” e “destino”, “data_ida”, “data_volta” e “data_pesquisa”. É verdade, tinha um campo a mais ali.

[09:20] Voltando aqui na nossa aplicação, vou dar um “OK”. Agora sim, “Data ida não pode ser menor que hoje”. Então estamos tentando comprar uma passagem, visualizar as passagens em conta, de ontem para voltar no dia 10, e não faz sentido. Então, dessa forma conseguimos validar também os nossos campos.

[09:39] Observe que de verificação ficou simples criarmos. Nós temos um local só onde criamos todas as nossas lógicas da validação e no nosso “forms” recuperamos os valores e só falamos ao campo que tem algum numero passar os argumentos que precisam para aquela função. Depois varre uma lista de erro exibindo essas mensagens de erro.

[10:02] Então essa é uma forma de conseguirmos validar os nossos campos, exibindo as mensagens de erro de forma legal aqui também com essa afirmação. Observe que se eu colocar, “São Paulo”, “São Paulo” também aqui, vamos ter todas essas mensagens de erro.

[10:17] Olhe: “Não inclua números nesse campo”, ou deixar a data da volta menor, eu quero comprar uma viagem para ontem, para voltar antes de ontem, então ele já nos mostra todas essas validações.

[10:27] E caso coloquemos os valores corretos, submeta o nosso formulário de forma correta, “Rio de Janeiro”, quero viajar hoje para voltar dia 10, todas as informações certas, e dou um “OK”; conseguimos submeter o nosso formulário.

#### Faça como eu fiz na aula

Chegou a hora de você seguir todos os passos realizados por mim durante esta aula. Caso já tenha feito, excelente. Se ainda não, é importante que você implemente o que foi visto no vídeo para poder continuar com a próxima aula, que tem como pré-requisito todo o código aqui escrito.

#### Clean e Clean_

Como vimos nesta aula, o Django fornece duas maneiras de adicionar regras de validação personalizadas a um formulário: criando um método chamado clean ou o método clean_<nome_do_campo>.

Sabendo disso, analise as informações abaixo e selecione as verdadeiras:

a) **Alternativa correta:** É possível validar utilizando o métodoclean_<nome_do_campo> e o clean no mesmo formulário.
- _Certo! É possível validar alguns campos de forma individual e validar todos os campos em seguida._

b) **Alternativa correta:** O método clean permite acessar e validar todos os campos no formulário.
- _Certo! Quando queremos comparar 2 campos de um formulário por exemplo, utilizando o método clean._

c) O método clean_<nome_do_campo> pode validar até 3 campos do formulário.

d) **Alternativa correta:** O método clean_<nome_do_campo> sempre é executado antes do método clean.
- _Certo! O método clean_<nome_do_campo> sempre será executado antes do método clean._

#### O que aprendemos?

##### Nesta aula:
- Iniciamos a aplicação criando o app de passagens;
- Criamos um formulário utilizando o Django forms;
- Melhoramos o visual do formulário exibindo incluindo o bootstrap.

##### Na próxima aula
Vamos aprender como recuperar e exibir os dados do formulário em outra página e incluir um calendário nas datas de ida e volta!

### 5. Modelos e formulários
#### Preparando o ambiente
#### Criando modelos

Até o momento estamos criando formulários e validações com a class Form mas podemos criar validações de formulários a partir da class Models. Que faz buscas no nosso banco de dados.

---

[00:00] Até o momento, nós criamos um formulário utilizando a classe “forms”. Se observarmos aqui o nosso “forms.py”, temos aqui o “PassagemForms”, porque estamos gerando esse formulário a partir do “forms” com todos os campos ali embaixo.

[00:15] O que vamos fazer agora é diferente. Nós queremos gerar um formulário, mas não através do “forms”, e sim de um modelo. Baseado em um modelo, eu quero gerar um formulário.

[00:26] Para não investirmos tanto tempo desenvolvendo os nossos modelos, o que nós vamos fazer? Nós vamos disponibilizar um pacote aqui chamado “models” que tem alguns arquivos que vamos inserir na nossa aplicação.

[00:40] Então eu vou pegar aqui o “passagens”. Eu tenho aqui na classe de “passagens”. Eu vou apertar as teclas “Ctrl + C” e “Ctrl + V”, nesse arquivo de “models”. Temos ele aqui também. Se você quiser copiar ou arrastar para cá, você pode também.

[00:52] Então dentro da nossa aplicação, nós temos aqui uma pasta com os modelos. Temos aqui o “init.py”, a “classe_viagem.py”, a “passagem.py” e o “pessoa.py”. Nós vamos entender cada um desses arquivos.

[01:05] Aqui o “init.py” nós temos para inicializar essas classes, esses modelos serem manipulados na hora que formos gerar essas informações no banco de dados. Como o nosso curso o foco não é banco de dados, nós vamos utilizar o SQlite apenas para exemplificar.

[01:23] Na “classe_viagem.py”, o que nós temos? Observe que temos aqui “classe_viagem.py”, nós vamos manter na nossa base de dados todas essas informações aqui, “Econômica”, “Executiva” e “Primeira classe”. Vamos exibir para as pessoas esse conteúdo, “Econômica”, “Executiva” e “Primeira classe”. Porque nós vamos gerar essas informações direto no banco de dados?

[01:48] Porque os nossos dados estão sensíveis. O que eu quero dizer com sensíveis? Se eu for aqui no “classe_viagem.py” e, por exemplo, excluir essa linha 2. Exclui. Só temos duas classes agora, ou “Econômica” ou “Primeira classe”.

[02:01] Se voltarmos na nossa aplicação e atualizarmos. Observe que aqui na “Classe de vôo”, nós vamos ter “Econômica” e “Primeira classe”. Só porque eu deletei uma linha, nós já perdemos todo o conteúdo daquele outro tipo.

[02:13] Então, para ficar mais clara essas informações, nós vamos criar um modelo, que chamamos aqui de modo “text choice”, que a partir dele vamos manipular as informações salvas no banco de dados de forma muito mais segura. Então esse é o nosso primeiro arquivo de modelo.

[02:31] Nosso segundo modelo vai ser o modelo de passagem. O que nós vamos ter nesse modelo? Origem, destino, data de ida, data de volta. Porém, diferentemente do nosso “forms”, ele sempre vai ser gerado através de um “model”, e não de um “forms”.

[02:45] Se observarmos aqui o nosso “forms.py”, observe que temos os campos aqui de forma parecida, “origem” é um “forms” que vem de “charfield”. Temos a “label” e temos o “max_legnght”. Aqui não precisamos passar o nome da “label”, nós só passamos a quantidade de caracteres que queremos, passamos as escolhas.

[03:01] Por exemplo: aqui no “classe_viagem” nós usamos o “models.TextField”, com o argumento aqui, o “choices” falando que nós vamos usar a classe de viagem “choice”, passando aqui as outras propriedades, como: “max_length” (quantidade de caracteres máximo que vamos precisar).

[03:16] Precisamos passar quando utilizamos o “choice”. Aqui o valor “default” dele vai ser o “0”. Se eu não me engano é a classe econômica. Então temos essas informações aqui do “Passagem”, agora gerando através de modelo, e não do “forms”.

[03:31] E vamos ver, por último: temos aqui também o nosso “models pessoa.py”. O que é o “pessoa”? Temos dois campos que vamos mostrar o seguinte exemplo.

[03:42] Vamos supor que eu tenha um modelo que eu não estou exibindo todos os campos que tem nesse modelo lá na minha página, ou seja, eu tenho aqui o “nome” e o “email”. Só que na nossa aplicação nós não usamos o “nome”, nós só usamos o “email”.

[03:54] Como eu não utilizo algumas informações no meu “model”? Nós vamos aprender isso através desse exemplo de “Pessoa”. Então vamos gerar um formulário para “Passagem”, vamos gerar um formulário para “Pessoa”, exibir esses dois formulários lá na nossa tela e depois nós vamos ver como não exibir alguns campos do modelo.

[04:13] Sabendo disso, sabendo como estão os nossos “models”, o que eu vou fazer? Eu vou abrir o meu terminal, vou parar aqui o meu servidor nessa parte e vou rodar o seguinte comando: “python manage.py makemigrations”. O que ele vai fazer? Ele vai gerar os scripts de migrações para criar esses conteúdos no banco de dados. Ele já criou para mim, então, “python manage.py makemigrations”.

[04:38] O segundo comando que vamos usar vai ser para de fato realizar a migração, “python manage.py migrate”. Quando eu apertar a tecla “Enter”, ele já está criando para mim toda a migração no banco de dados. Ele criou, agora nós temos na nossa base de dados esses arquivos feitos.

[04:57] No nosso próximo vídeo nós vamos aprender a como alterarmos o nosso “forms” para gerarmos um formulário baseado no nosso modelo.

#### [ModelForm]('https://docs.djangoproject.com/pt-br/4.1/topics/forms/modelforms/')

1. Em forms.py, devemos alterar class Forms para class Models, conforme a seguir:

        class PassagemForms(forms.ModelForm):
            class Meta:
                model = Passagem # Model que vou utilizar em meu forms
                fields = ['origem'] # traz campos especificos
                fields = '__all__' # traz todos os campos
                exclude = ['nome']
                labels = {'data_ida':'Data de volta'} # forma os campos para aparecer no html
                widgets = {'data_ida':DatePicker()}

---

[00:00] Eu tenho um “PassagemForms” sendo gerado a partir de um “Form” aqui, passando todos os campos. Eu quero fazer algo diferente, eu quero utilizar o modelo que eu fiz a migração na aula passada, aqui e agora. Como nós vamos fazer isso?

[00:14] A primeira coisa que vamos fazer é indicarmos que essa nossa classe “PassagemForms” não vai ser mais do tipo “Form”, ela vai ser do tipo “forms.ModelForm”. Legal!

[00:25] Outra coisa que nós vamos precisar fazer é: se eu vou utilizar o “ModelForm”, eu preciso saber qual é o modelo que eu estou querendo utilizar, eu preciso importar os meus modelos para esse arquivo. Então, “from passagens.models”. Eu quero importar “import Passagem”. Eu quero importar “ClasseViagem,” e eu quero importar também “Pessoa”. Legal!

[00:47] Trouxe os meus três modelos. O que eu preciso fazer agora? Como eu tenho um “ModelForms” para ser gerado, eu preciso indicar qual é o modelo desse “PassagemForms”, qual é o modelo que eu quero gerar o meu formulário. Para isso, nós vamos utilizar uma classe.

[01:02] Eu vou criar aqui uma classe chamada “meta”. O que essa classe “meta” vai fazer? Ela vai ser responsável por manipular as informações que estão no nosso modelo para gerar no nosso formulário. A primeira coisa que passamos de propriedade para ela é quem é o modelo que nós vamos gerar, qual é o modelo que vamos usar como base.

[01:18] Eu vou usar como base o modelo de “Passagem”. Outra coisa que vamos precisar fazer também é indicar quais são os campos que queremos exibir. Então eu vou colocar aqui a propriedade “fields” e vou passar aqui “['origem']”, para nós visualizarmos. Eu vou remover aqui “origem”, “data_ida” e “data_volta”, vou remover esses três.

[01:42] Agora, algo muito importante que eu gostaria que você fizesse também: essa “data_pesquisa” aqui eu vou comentar, eu vou colocar uma “#” aqui na frente, para só comentarmos. Essas “classe_viagem” e “informações”, essas outras propriedades, nós não vamos utilizar, então eu vou removê-las daqui. Essa aqui que comentamos nós vamos entender depois o porquê. Eu vou deixar as validações aqui embaixo mesmo. Salvei.

[02:10] Voltando na nossa aplicação, deixe-me ver se estou com o servidor rodando. Estou com o servidor rodando, eu tenho aqui o “Origem”, eu posso preencher. “Origem: São Paulo”. Se eu der um “OK”, o que vai acontecer? Dei um “OK”, ele vai exibir uma mensagem de erro. Por quê?

[02:25] Aqui só temos o campo “Origem”, mas ele está esperando o “Origem”, o “Destino”, o “Data de ida”, “Data de volta” e “Data de pesquisa”. Nós temos informações para serem exibidas aqui, validações para serem exibidas, mas não encontramos esses campos aqui no momento que fizemos validação. Então eu vou trazer o outro campo, “ 'destino' ”. Vou trazer o outro, que é “ 'data_ida' ”.

[02:53] Só que pense comigo uma coisa: eu vou abrir aqui o meu formulário em “forms”, eu tenho aqui “forms passagem”, observe comigo. Eu tenho um, dois, três, quatro, cinco, seis, sete campos que eu quero exibir no meu formulário. Pense: se eu tivesse setenta campos para exibir, eu teria que trazer todos os campos aqui. Isso é um pouco complicado.

[03:15] Pare para pensar que, quanto maior esses números de campos, mais trabalho eu vou ter para indicar todos os campos que eu tenho aqui. Por exemplo: eu trouxe esses três, se eu voltar na nossa aplicação e exibir aqui, recarregar, observe que eu já vou ter três, “origem”, “destino” e “data_ida”. Alguém já deve ter passado por esse problema e pensou: “bom, vamos criar uma forma de conseguirmos trazer todos os campos!” E existe essa forma, que eu vou mostrar agora.

[03:39] Então, se quisermos trazer um determinado campo, podemos trazer assim. Se eu quiser trazer todos os campos entre aspas simples, eu vou colocar a propriedade “ '__ all__' ”. Salvando, voltando lá na nossa aplicação e atualizando. Agora sim, nós temos todos os nossos campos. Legal!

[03:55] Maravilha, temos todos os campos aqui! Só que o “Data ida” e o “Data volta”, as “labels”, estão com nomes estranhos. Olhe só, “Origem”, “Destino”, “Data ida”, “Data volta”, “Data pesquisa”, “Classe viagem”. Não é “Classe da viagem”.

[04:10] Aqui, o pior “informacoes”, porque está o nome que demos lá no nosso modelo, na hora que criamos o nosso modelo, “informacoes”. Nós não vamos usar acento aqui, só que nessa parte aqui, principalmente nessa “label” aqui seria importante se tivéssemos escrito “Informações”. Como alteramos as “labels” da nossa aplicação através de um modelo?

[04:30] Nós vamos colocar a propriedade “label”, e através de “{ }” nós vamos indicar o nome do campo e a “label” que queremos exibir. Por exemplo: vamos visualizar aqui qual “label” queremos alterar, “Origem”, “Destino”, “Data ida” e “Data de ida”, não é, vai ficar melhor.

[04:44] Então eu vou colocar aqui “{'Data_ida'}” e o nome da “label” que eu quero exibir para ele, “{'Data de ida, 'data_volta'}”, que é o nome do meu campo e a “label” que eu quero exibir para ele “ {'Data de volta'}”.

[05:10] Salvando, voltando na nossa aplicação e atualizando. Nós temos “Data de ida”, “Data de volta”, “Data pesquisa” e “Informacoes”. Vamos alterar “Informacoes” também, porque queremos exibir escrito “Informações”. Salvando, voltando e atualizando. Ficou um erro, deixe-me ver o que eu fiz de errado aqui. Agora sim, agora deu certo. Carregando. Temos aqui “Informações”.

[05:47] “Classe viagem” pode ser “Classe da viagem”, vai ficar melhor. Então vamos alterar também! Vou colocar uma vírgula aqui do lado e vou escrever “ 'classe_viagem' : 'Classe do vôo' ”. Atualizando. Agora sim, “Classe do vôo”.

[06:19] Maravilha! Temos algo parecido com o que tínhamos antes, com as “labels” legais. Só que, outro ponto: “Data de ida” e “Data de volta”, não estamos usando o “DatePicker”. Precisamos utilizar o “DatePicker” aqui também. Como utilizamos o “DatePicker” aqui?

[06:34] Podemos fazer da seguinte forma: eu vou colocar aqui que vamos utilizar “widgets = {'data_ida'}” e nós vamos utilizar também no “ 'data_volta' “. No “data_ida” queremos utilizar o “:DatePicker(),” e no “data_volta” vamos utilizar o “:DatePicker” também, para esses dois.

[07:02] Atualizando a nossa aplicação. “Origem”, “Destino”, “Data de ida”. Legal, está aparecendo aqui! “Data de volta” está aparecendo aqui. Chegamos na “Data pesquisa”... “Data da Pesquisa”, precisamos alterar a “label” também.

[07:16] E acontece um ponto interessante, olhe só: na data de pesquisa nós queremos alterar a “label”, nós queremos colocar um valor inicial, queremos desabilitar essa propriedade. Então quando queremos de fato alterar muitas informações, muitos campos em relação à mesma parte do nosso código. O que podemos fazer?

[07:39] Vou selecionar todo ele aqui, vou colocá-lo aqui em cima. Então, na data da Pesquisa, nós vamos fazer uma manipulação dela de forma diferente. Ela vai estar antes dos nossos outros campos. Vou salvar. Se voltamos nessa aplicação e atualizamos, observe que temos aqui o “Data da pesquisa” não conseguimos alterar.

[07:59] “Data da ida”, dia 04, “Data de volta”, 11. Vou colocar aqui um formulário válido. “São Paulo”, eu quero ir para o “Rio de Janeiro”. “Informações”, eu vou deixar sem nada. Vou dar um “OK” e ele nos exibe as informações.

[08:17] Será que as nossas validações estão funcionando? As validações estão aqui embaixo, vamos colocar origem e destino iguais. “São Paulo”, “São Paulo”, “Origem e destino não podem ser iguais”. Maravilha! Vamos voltar então, para o “Rio de Janeiro”. Eu vou colocar uma data menor do que a data de hoje, vou colocar dia 03.

[08:38] Quando eu clicar em “OK”, “Data de ida não pode ser menor que hoje”. Legal! Eu vou colocar então a data no dia 04 e quero voltar no dia 01. Nossa, maior bagunça! Eu vou colocar, “Data de volta não pode ser menor que a data de ida”. Maravilha!

[08:52] Nós temos o comportamento que queríamos na nossa aplicação. Está realizando aqui as nossas validações. Se colocamos conteúdo e valores válidos, conseguimos visualizar.

[09:02] O que vamos fazer na sequência? Na sequência nós vamos criar um formulário para a pessoa e vamos exibir a propriedade do campo “Email” neste formulário aqui embaixo, assim como tínhamos anteriormente, só que agora vinculando de um modelo.

#### Formulários

[00:00] Agora que sabemos trabalhar um pouco melhor com o “ModelForms”, eu quero criar um formulário de pessoas. O que acontece é que no nosso modelo de pessoa temos o nome e o e-mail, só que eu não quero exibir no formulário o nome. Eu quero exibir apenas o e-mail, para visualizarmos na nossa aplicação, assim como tínhamos antes. Legal!

[00:18] Então, o que eu vou fazer? Eu vou criar aqui uma classe igual a que fizemos, uma classe que eu vou chamar de “PessoaForms”. Essa “PessoaForms” vai ser do tipo “forms.ModelForm” porque vamos ter um modelo vinculado. Eu vou criar uma “class” que eu vou chamar de “Meta”. Nós vamos passar algumas propriedades para essa “class Meta:”.

[00:39] Essa “class Meta” de “Pessoa” nós vamos precisar indicar quem é o modelo. O modelo dela vai ser modelo de “Pessoa”. Além disso, precisamos passar quais são os campos que vamos utilizar. Temos duas opções: podemos falar que o campo que vamos utilizar é o campo “email”. Então eu poderia fazer assim: que os campos dessa classe, o campo “email” apenas. Eu vou passar só o campo “email”.

[01:03] Ou, o que podemos fazer é pegarmos todos os campos, exceto o campo “nome”. Então eu não quero exibir o nome, eu quero exibir apenas o “email”. Eu posso fazer assim, ou posso fazer “exclude = [ 'nome']”, dessa forma ele vai trazer todos os campos, exceto o “nome”.

[01:20] Qual é a diferença do “fields”? Quando eu coloco “fields”, eu estou especificando quais são os campos que eu quero trazer. Ele não vai me trazer todos. Quando eu uso o “exclude”, ele vai trazer todos, exceto esse campo que eu marquei.

[01:31] Criamos aqui o “PessoaForms” e indicamos que vamos ter o e-mail nele. O que eu quero fazer agora é: lá no nosso arquivo “views.py” eu vou indicar que eu também, além do “PassagemForms”, eu vou utilizar também o “PessoaForms”. Aqui eu vou colocar o “pessoa_form = PessoaForms()”.

[02:04] Então na nossa “index” vamos ter além do “form”, que é o formulário de pessoa, vamos ter um formulário agora para manter as informações de pessoa, que eu vou chamar de “pessoa_form”. Então eu vou colocar uma vírgula aqui, vou chamar de “pessoa_form”, e ele vai ser do tipo “:pessoa_form”, e nós passamos por contexto.

[02:27] Passamos dois formulários por contexto, o que precisamos fazer? Lá na nossa página, lá onde mantemos o nosso código HTML, nossos arquivos HTML, no “index.html”, o que eu quero fazer? Temos logo após esse “{% endfor %}” aqui eu quero exibir as informações de “pessoa form”, então eu vou colocar aqui “{{pessoa_form}}” para nós visualizarmos.

[02:52] Lá na nossa aplicação, eu vou clicar aqui em “Passagem” só para visualizarmos. Eu não estou com o terminal rodando, deixe-me abrir meu terminal, teclas “Command + J” aqui. Estou na “venv”. Vamos abrir aqui o nosso terminal, “pyton manage.py runserver”.

[03:13] Agora sim, rodando nosso servidor. Temos aqui todas as informações e temos aqui embaixo o “Email”. Ficou legal! Aparentemente está funcionando, só que ele não está com o visual legal, não ficou com visual bonito igual tínhamos nos nossos outros campos também.

[03:28] Então, o que podemos fazer? Podemos pegar a mesma propriedade que temos aqui em cima. Para cada campo visível, eu vou copiar todas essas informações aqui, até essa nossa “div” para passar do “form-control”. Vou selecionar aqui, vou colocar aqui, e não vai ser mais do nosso “form”, vai ser do “pessoa_form”. Vou salvar essas informações.

[03:52] Voltando aqui e atualizando. Deu um erro porque eu esqueci do “end block”, nós copiamos o código aqui do “for”, e não colocamos o “endblock”, vou copiar aqui o “endblock” também. Teclas “Ctrl + C”. Embaixo dessa “div”, o “{% endfor %}”. Agora sim, atualizando temos aqui o nosso e-mail como tínhamos anteriormente, a “label” em cima e as informações embaixo.

[04:17] Vou colocar aqui a origem como “São Paulo”, vou colocar aqui “Rio de Janeiro”. “Data de ida”, vamos ver, eu vou viajar no dia 04 e vou voltar no dia 06. “Econômica”. “Email”, vamos lá, “gui@alura.com”. Quando eu der um “OK” vai para as informações, só que não está mostrando o meu e-mail. Porque não está mostrando o meu e-mail aqui?

[04:41] Olhe só que interessante: lá no nosso arquivo “views.py”, vou apertar as teclas “Command + J” para minimizar o nosso terminal. No nosso arquivo “views.py” nós trazemos as informações de “PessoaForms”, mas onde estão as informações de “PessoaForms”? Nós não trouxemos, precisamos trazer também.

[05:01] Vou apertar as teclas “Ctrl + C” aqui, um “Ctrl + V”, vou chamar esse formulário de “pessoaform”. Ele vai ser relacionado a “PessoaForms”. Trazemos ele da requisição também e passamos por contexto essas duas informações.

[05:16] Então eu vou passar essas duas informações por contexto, o nosso “forms”, que é relacionado a Passagem, e o “pessoaform”. Eu vou fazer a mesma coisa aqui embaixo também, dessa forma vamos conseguir visualizar o nosso campo “Email”. Então, vamos lá?

[05:31] Deixe-me voltar, acho que é mais rápido. Voltando. “São Paulo” e “Rio de Janeiro”. Legal! Eu tenho aqui o guia. Quando eu dou um “OK”, recebo uma mensagem de erro aqui: “pessoa_form”, eu esqueci aqui do “ _ “, eu escrevi o “pessoa form” sem o “ _ “.

[05:44] Agora sim, salvando e voltando na nossa aplicação. Voltei, tenho aqui as informações, dou um “OK”. Não conseguimos visualizar porque faltou irmos lá no nosso código HTML, no “minha_consulta” ele não vem mais de “form”, ele vem de “pessoa_form.email.value”.

[06:11] Salvando, voltando lá no nosso código, eu vou submeter de novo esse formulário. Agora sim, temos o email “guia@alura.com”.Legal!

#### Faça como eu fiz na aula

Chegou a hora de você seguir todos os passos realizados por mim durante esta aula. Caso já tenha feito, excelente. Se ainda não, é importante que você implemente o que foi visto no vídeo para finalizar este curso.

#### O formulário da Valentina

Valentina estava desenvolvendo um site com uma tela de cadastro de produtos. Alguns campos são baseados em uma classe modelos, porém outros não.

Além disso, Valentina precisa validar esses campos enviando mensagens de erro para as pessoas que irão utilizar o formulário.

Sabendo disso, analise as afirmações abaixo e marque as verdadeiras:

a) **Alternativa correta:** Para criar um formulário baseado num modelo, podemos utilizar a classe Meta para informar o nome do modelo, quais campos serão exibidos, alterar labels ou personalizar os widgets por exemplo.
- _Certo! Quando queremos configurar labels ou widgets de algusn campos, podemos utilizar a classe Meta_

b) **Alternativa correta:** Quando a classe Meta é criada, não podemos editar nenhum campo fora desta classe.

c) **Alternativa correta:** Quando optamos por validações utilizando o método clean, para que de fato essas validações sejam executadas, precisamos verificar se o formulário é válido com o seguinte código no arquivo views.py:
- _if form.is_valid(): Certo! Com esse código, as validações do método clean serão executadas._

#### O que aprendemos?

##### Nesta aula:
- Iniciamos a aplicação criando o app de passagens;
- Criamos um formulário utilizando o Django forms;
- Melhoramos o visual do formulário exibindo incluindo o bootstrap.

##### Projeto final do curso
Aqui você pode baixar o zip do projeto final do curso ou acessar os arquivos no [Github]('https://github.com/alura-cursos/django_forms_curso/tree/aula_5)'!

#### Conclusão

[00:00] Se você chegou até aqui, parabéns! Você está finalizando mais um treinamento aqui da Alura.

[00:05] Neste curso nós começamos gerando um formulário que não estava lá tão bonito, e depois ele foi melhorando, foi ficando com uma aparência melhor.

[00:12] Depois fomos inserindo validações para auxiliarmos a pessoa que vai mexer na nossa aplicação, que vai preencher o nosso formulário, incluindo ali mensagens da validação.

[00:22] Depois criamos um modelo e vinculamos, criamos um formulário a partir de um modelo. Isso ficou bem legal.

[00:29] Deixamos o nosso código com as principais convenções do Django, não repetindo código. Seguimos as boas práticas de programação e deixamos a nossa aplicação bem legal.

[00:40] Eu espero que você tenha gostado deste treinamento, espero que você tenha aproveitado bastante cada informação passada e que você aprofunde ainda mais seus conhecimentos neste incrível framework, que é o Django.

[00:52] Legal! Não se esqueça de dar a nota desse curso e falar como foi a sua experiência, essa informação é muito importante para nós aqui da Alura. Nos vemos em um próximo curso. Tchau, tchau!
