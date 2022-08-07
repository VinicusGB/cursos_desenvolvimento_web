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
#### Django Form
#### Melhorando o visual
#### Faça como eu fiz na aula
#### A classe forms do Django
#### O que aprendemos?
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
