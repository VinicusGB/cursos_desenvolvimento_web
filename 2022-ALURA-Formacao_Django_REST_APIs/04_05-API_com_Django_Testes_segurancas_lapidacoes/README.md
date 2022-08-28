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
### Projeto da aula anterior
### Caching
### Para saber mais: args e kwargs
### Instalando o Redis
### Integrando Django e Redis
### Faça como eu fiz
### Definindo cache
### O que aprendemos?
## 03. Limitando ações no Viewset e Permissões
### Projeto da aula anterior
### Internacionalização - i18N
### Alterando mensagens padrões
### Content Negotiation
### Faça como eu fiz
### Negociação de conteúdo
### O que aprendemos?
## 04. Testes
### Projeto da aula anterior
### Cenário de Teste
### Testando GET e POST
### Testando PUT e DELETE
### Faça como eu fiz
### Função setUp
### O que aprendemos?
## 05. Segurança
### Projeto da aula anterior
### Pensando em segurança
### Pote de mel
### Acesso não autorizado
### Faça como eu fiz
### O que aprendemos?
### Parabéns
### Conclusão
### Logo da alura
### SOBRE A ALURA