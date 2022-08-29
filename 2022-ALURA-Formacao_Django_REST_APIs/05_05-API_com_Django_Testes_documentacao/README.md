# API com Django 3: Aprofundando em testes e documentação - 8h
**Professor:** Guilherme Lima

**Disponível:** [ALURA]('https://cursos.alura.com.br/course/api-django-3-testes-documentacao')

**Conteúdo:**
- Aprenda a escrever testes automatizados nos modelos, serializers e outras partes de sua aplicação
- Entenda a importância dos testes no desenvolvimento de software
- Saiba como integrar o Swagger para gerar a documentação de sua API
- Conheça uma forma de carregar dados JSON no banco de dados, integrando os modelos
- Descubra como realizar diferentes testes no Postman

## 01. Tipos de testes
### Apresentação

[00:00] Olá! Meu nome é Guilherme Lima e eu serei o seu instrutor nesse treinamento de Django Rest, aprofundando em testes e documentação. O que vamos aprender nesse curso?

[00:109] Nesse curso vamos escrever uma série de testes automatizados para verificarmos os nossos modelos, nossos serializers, para verificarmos a autenticação de um determinado recurso, se é permitido ou não. Veremos como conseguimos escrever esses testes.

[00:23] Vamos aprender também como documentarmos a nossa API para que outras pessoas consigam utilizar. Para quem é esse curso? Esse curso é super indicado para as pessoas que fizeram o curso anterior, de pré-requisito, de Django Rest; já vimos uma pincelada de teste. Nesse curso vamos nos aprofundar nesse conceito de testes.

[00:43] Fazendo esse curso, vamos trabalhar e escrever uma série de testes: testes de autenticação, testes nos nossos modelos, testes no serializer e como executamos e escrevemos esses testes da melhor forma.

[00:56] Falando da parte da documentação da nossa API que vamos desenvolver, vamos ter um recurso de programas e vamos ver como documentar esses programas utilizando o “Swagger”.

[01:09] Então, fazendo esse curso nós vamos aprender uma série de coisas bacanas relacionadas a testes e documentação utilizando o Django Rest. Sabendo de tudo isso, vamos começar?

### Preparando o ambiente

Olá!
É muito bom receber você neste curso de API com Django 3: Aprofundando em testes e documentação.

Espero que seja uma experiência de aprendizado incrível e que possamos vencer todos os desafios juntos. Neste curso, vamos aprofundar nossos conhecimentos no Django Rest Framework e aprender como criar diferentes tipos de testes, sejam eles nos modelos, serializers e muitos outros. Vamos entender a importância dos testes e documentar nossa API com Swagger.

Carregando o projeto base do curso
Para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

        Python 3.7.4
        Django 3.1.5

O Django pode ser instalado através do comando:

        pip install Django==3.1.5

Além disso, usaremos um projeto base no qual você pode realizar o download [neste link]('https://github.com/alura-cursos/drf_teste_documentacao/archive/projeto_inicial.zip').

Após o download, abra o projeto em seu editor de código preferido e crie uma nova venv com o comando python -m venv ./venv e ative conforme seu sistema operacional.

Para sistemas MacOS ou Linux:
source venv/bin/activateCOPIAR CÓDIGO
Já no Windows:

        venv\Scripts\activate.bat

Após ativação, faça a instalação dos módulos necessários com o seguinte comando:

        pip install -r requirements.txt

Agora, execute as migrações dos modelos:

        python manage.py migrate

Para garantir que tudo deu certo, suba o servidor:

        python manage.py runserver

Na próxima atividade, vamos aprofundar ainda mais nossos conhecimentos utilizando esta incrível ferramenta de desenvolvimento.

Em caso de dúvidas durante o curso ou carregamento do projeto, conte sempre com o fórum da Alura!

:)

### Conhecendo o projeto

1. No terminal podemos carregar nossos dados com um comando:

        python manage.py loaddata programa_iniciais.json

---

[00:00] Vamos iniciar os nossos estudos, então? Para começarmos, na atividade anterior a esse vídeo temos um passo a passo de como você vai baixar o projeto base que vamos utilizar para criarmos a nossa documentação, criarmos os testes da nossa API e aprofundarmos os nossos conhecimentos com o Django Rest.

[00:17] Já segui todos os passos descritos nessa atividade e o que vou fazer agora vai ser subir o meu servidor, para nós entendemos melhor como está funcionando a nossa API. Então digito python manage.py runserver no aplicativo, com minha venv já ativada. Aperto a tecla “Enter” e vou abrir o localhost:8000.

[00:36] Temos uma API de programas. Quando eu clico, ele pede que eu tenha um usuário de acesso. Na atividade também está descrito para criar um usuário, então vou colocar meu usuário gui e minha senha que ninguém imagina que é, 123. Vou apertar a tecla “Enter” e conseguir acesso à minha API.

[00:54] Nesse projeto vamos trabalhar com uma API inspirada nos sistemas de streamers que temos, como Netflix, Amazon Prime, entre outros. Então na nossa API vamos ter um título, vamos ter um tipo, uma data de lançamento e a quantidade de likes. Essa vai ser a ideia da nossa API.

[01:14] O que vou precisar fazer? Temos nossa API e queremos testar a nossa API, além disso, se clicamos em “Filtros”, observe que temos filtros para filtrarmos só o filme ou filtrarmos apenas as séries, e tem um campo de busca em que eu consigo pesquisar pelo título.

[01:32] Todas essas informações, conseguimos observar no app “aluraflix > views.py”. Se observarmos esse teste, temos o nosso queryset de objetos, temos nossa classe de serializer e temos o filtro que eu mostrei para vocês.

[01:49] Então vamos conseguir pesquisar pelo título do programa, seja ele um filme ou uma série. Temos um campo de busca no lugar do título, um filtro para identificarmos se vai ser um filme ou uma série e temos a nossa classe de autenticação, o BasicAuthentication. Isso ficou bem bacana, só que eu tenho 0 filmes.

[02:09] Sempre quando vamos iniciar um projeto, seria legal se tivéssemos uma forma de carregarmos os dados iniciais - no nosso caso, os programas iniciais, sejam eles séries ou filmes. Existe uma forma de fazermos isso!

[02:21] Vamos imaginar que estamos desenvolvendo nossa API e que o time que cuida do banco de dados já nos passou alguns programas iniciais. Então dentro do nosso app da “aluraflix”, temos uma pasta chamada “fixtures”. Quando eu clico nela, temos o objeto JSON, que se chama “programas_iniciais.json” e dentro temos um array com vários programas.

[02:49] O primeiro programa então é aluraflix.programa- sempre identificamos o modelo que estamos trabalhando. Temos a chave primária, qual vai ser o id desse programa, os campos e seus respectivos atributos.

[03:05] Então eu tenho: ”título”: “Coisas bizarras” - é uma série, tem a data de lançamento, quantidade de likes e quantidade de dislikes. Eu tenho essa informação para todos os outros filmes e séries.

[03:17] Então tem: “Coisas bizarras”, “O Bruxo”, “Emília em São Francisco”, “Corações de lata”, “Le Le Lend”, “Saltadores Ultimato” e grandes sucessos da “aluraflix”. Qualquer semelhança com um filme real é coincidência mesmo.

[03:29] Então tenho esses programas, tenho esse arquivo JSON. Como que eu faço para carregar esses arquivos JSON na minha base de dados? Abrindo o meu terminal, vou pará-lo e, o que vou fazer? Existe um comando para eu carregar os dados, o nome é muito parecido com o que falamos mesmo: loaddata, ou seja, “carrega os dados”. Agora vou passar qual é o arquivo que eu quero carregar os dados.

[03:53] Poxa, está em JSON e vamos fazer nosso projeto utilizando o Python, o Django! Como ele vai entender do JSON para o Django, como ele nos faz essa ponte? Esse método tem essa responsabilidade. Na próxima atividade eu vou deixar um link para nós entendermos melhor como essa função funciona.

[04:14] Então, loaddata. Vou passar que eu quero carregar programas_iniciais.json. Quando eu aperto a tecla “Enter”, olhe o que vai acontecer: ele fala que foi instalado novos objetos de uma fixture(s). Então tem algo importante para eu passar para vocês.

[04:30] Observe que dentro da pasta do meu app, eu tenho uma pasta chamada “fixtures”, dentro dessa pasta eu tenho um arquivo JSON com os dados que eu quero carregar, os iniciais. Para eu conseguir carregar esses dados, eu só executo o comando loaddata do manage.py e passo o nome do arquivo JSON.

[04:50] Vamos supor que no meu modelo da “aluraflix” eu tenha, além de programas, diretores, roteiristas e várias outras classes de modelo. O que eu poderia fazer? Poderia criar um outro arquivo JSON para preencher esses modelos.

[05:08] E aqui eu faço a referência, que nesse caso é o programa - mas se fosse os diretores eu escreveria aluraflix.diretores e passaria qual é id e quais são os campos com seus dados. Para eu carregar, só passo o nome dele depois do loaddata.

[05:27] Carreguei, mas será que carregou mesmo? Vamos ver! Vou subir o meu servidor mais uma vez. Quando eu venho no programa e atualizo, temos “Coisas bizarras”, “O bruxo”, “Corações de lata”, “Resgate do soldado Carlinhos” e vários outros filmes bem legais também, “Capitão Bahia”. Filmes de sucesso da “aluraflix”.

[05:45] Qual é o nosso desafio agora? Podemos conferir, por exemplo, se eu colocar o filtro de “Série” no campo “Tipo” e enviar que eu quero ver só as séries, eu tenho: “Coisas bizarras”, “O bruxo” e “Emília em São Francisco”. Se eu coloco, por exemplo, “Filme” no campo “Tipo” e enviar, temos só os filmes: “Corações de lata”, “Le Le Lend” e “Saltadores ultimato”. Isso ficou bem bacana!

[06:08] Se eu pesquisar também, por exemplo, por “Saltadores” e dar uma busca, verei só aquele filme “Saltadores ultimato”. Isso ficou bem legal! Aparentemente a nossa API está funcionando, porém é importante que garantamos que partes diferentes da nossa API estejam funcionando. Vamos entregar o comportamento que esperamos. Por isso a importância dos testes.

[06:33] Nas próximas aulas vamos aprofundar mais ainda nesse conhecimento dos testes, a importância dele e como testamos diferentes partes da nossa API.

### Tipos de testes
### Faça como eu fiz: Fixtures
### Carregando dados iniciais
### Para saber mais: Testes automatizados
### Para saber mais: Teste funcional e de unidade
### O que aprendemos?
## 02. Testes de unidade
### Projeto da aula anterior
### Testando modelo
### Testando serializer
### Conteúdo do serializer
### Faça como eu fiz
### Uso do Set
### O que aprendemos?
## 03. Teste de integração
### Projeto da aula anterior
### Testando a autenticação
### Credenciais incorretas
### Requisições de user autenticado
### Faça como eu fiz
### Unidade ou Integração?
### O que aprendemos?
## 04. Testando a API
### Projeto da aula anterior
### Fixtures nos testes
### Preparando o ambiente: Postman
### Testando API no Postman
### Faça como eu fiz
### Função setUP
### O que aprendemos?
## 05. Documentando a API com Swagger
### Projeto da aula anterior
### Swagger
### DRF e Swagger
### Faça como eu fiz
### Detalhes do Swagger
### Projeto final do curso
### O que aprendemos?
 