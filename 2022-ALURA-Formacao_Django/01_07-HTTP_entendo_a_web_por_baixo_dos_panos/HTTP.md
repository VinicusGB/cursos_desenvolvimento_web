# HTTP: Entendo a web por baixo dos panos - 14 horas

**Professor:** Fábio Pimentel<br>
**Disponível:** <a href="https://cursos.alura.com.br/course/http-fundamentos" target="blank">ALURA</a><br>
**Conteúdo:**
- Torne-se um programador web completo
- Entenda os detalhes do protocolo HTTP
- Saiba quando usar GET e POST
- Estude sobre segurança na web e o HTTPS
- A web stateful e a web stateless
- Conheça as melhorias do HTTP/2

## 01. O que é HTTP?

### O que é HTTP
    Primeiramente temos que ter em mente o modelo Cliente-Servidor.
    O modelo Cliente-Servidor consiste em o cliente(navegador web) faz solicitação para o servidor.
    Para ocorrer a comunicação entre as partes(Cliente-Servidor) necessitamos de regras de comunicação. Essas regras de comunicação são chamadas de protocolos de comunicação.
    O HTTP(HyperText Transfer Protocol) é um Protocolo de Transferência de Texto.

### Exercício: Objetivo do treinamento
    Olá Aluno!
    
    Neste treinamento, vamos falar sobre a "sigla" mais importante da internet: o HTTP. O objetivo é entender o protocolo HTTP detalhadamente. Quanto mais o desenvolvedor souber sobre este protocolo, melhor, pois ele é utilizado em todas aplicações web.
    
    No entanto, não focaremos em como essas aplicações são criadas e funcionam internamente. Para isso, existem várias plataformas, como PHP, .NET ou Java (entre muitas outras) que não abordaremos. Temos treinamentos dedicados para conhecer estas plataformas.
    
    Resumindo, nosso foco será o protocolo HTTP!
    
    Falamos tanto sobre essa sigla, mas você sabe qual é o significado do HTTP?
    
    a) High Text Transmission Protocol
    b) Heavy Transmission Text Protocol
    c) Help Text Transfer Protocol
    d) Alternativa correta: Hypertext Transfer Protocol
> No mundo de TI, temos muitas siglas e abreviações! O que menos importa é decorar esses nomes, mas é preciso entender o que há por trás. Nesse treinamento vamos focar nos principais conceitos do protocolo HTTP, aquilo que realmente importa para o desenvolvedor.

### Exercício: Modelo Client-Sever
    O protocolo HTTP segue o modelo Client-Server. O que o navegador (como Chrome ou Firefox) representa nesse modelo? O cliente ou o servidor?
    
    a) Alternativa correta: Cliente
        Exato, nós que estamos utilizando o navegador somos o cliente da Alura, que nos fornece o conteúdo, logo ela é o servidor.
    b) Servidor
    c) Nem um, nem outro.
        
> Nesse modelo, o navegador representa o cliente. É importante saber que nem só navegadores dominam o protocolo HTTP. Ainda veremos mais sobre isso neste curso.

### Exercício: Papel do HTTP entre Cliente e Servidor
    O cliente inicia a comunicação e o servidor responde. No entanto, qual é o papel do HTTP entre o cliente e o servidor?
    
    a) Definir uma estrutura de dados
    b) Definir o melhor algoritmo de pesquisa
    c) Alternativa correta: Estabelecer regras de comunicação
        Exatamente, o HTTP foi feito para estabelecer regras de comunicação entre o modelo Cliente-Servidor que funciona na Web.
    d) Comprimir os dados
       
> Se você compreende este texto, é porque você sabe português! Para que alguém consiga se comunicar com você, esse alguém deverá usar o português (supondo que você desconheça outro idioma, é claro). Isso significa que, sua regra (protocolo) de comunicação com o mundo é a língua portuguesa, que define a forma com que as informações devem chegar até você (através do vocabulário, regras de gramática e etc). Uma outra pessoa que conheça português irá usar do mesmo formato, já que vocês possuem um idioma em comum.

> Na internet, como já vimos, o idioma mais comum é o HTTP. Ele é responsável por definir a forma de como os dados são trafegados na rede através de várias regras. Portanto, todo mundo que conhece o idioma HTTP poderá receber e enviar dados e participar dessa conversa!
    
### Para saber mais: Peer-To-Peer
    Você já usou torrent para baixar algum arquivo na internet? Caso sim, aproveitou um outro modelo de comunicação, o P2P ou Peer-To-Peer!
    
    O modelo Cliente-Servidor não é o único modelo de comunicação na rede, nem sempre o mais adequado. Por exemplo, imagine que precisemos contar as letras de 20 palavras. No caso do modelo Cliente-Servidor, quem fará esse trabalho é o servidor, certo? E se precisar contar as letras de 1 milhão de palavras? Muito trabalhoso para o servidor, não?
    
    O modelo Cliente-Servidor tenta centralizar o trabalho no servidor, mas isso também pode gerar gargalos. Se cada Cliente pudesse ajudar no trabalho, ou seja, assumir um pouco da responsabilidade do servidor, seria muito mais rápido. Essa é a ideia do P2P! Não há mais uma clara divisão entre Cliente-Servidor, cada cliente também é servidor e vice-versa!
    
    Isto é útil quando você precisa distribuir um trabalho ou necessita baixar algo de vários lugares diferentes. Faz sentido?
    
    Usando algum aplicativo de Torrent, o protocolo utilizado não é o HTTP, e sim o protocolo P2P, como BitTorrent ou Gnutella.

### Exercício: Para saber mais: Outros protocolos
    O HTTP não é o único protocolo de comunicação que existe. Aliás, existem milhares de protocolos no mundo de TI, no entanto o HTTP é de longe o mais popular.
    
    Na lista abaixo, há um item que não representa um protocolo para internet.
    
    Qual é exatamente? Pesquise se for necessário.
    
    a) FTP
    b) Alternativa correta: SQL
        SQL (Structured Query Language) não é um protocolo para internet, e sim uma linguagem de consulta para banco de dados.
    c) BitTorrent
        Além de ser um protocolo, também é um aplicativo para troca de arquivos na internet.
    d) SMTP
    
> Um banco de dados cuida dos dados de uma aplicação, é parecido com uma planilha de Excel. O SQL ajuda muito a acessar esses dados.
    
> Um banco de dados não se preocupa em como os dados serão visualizados, ele só administra os dados! Aqui na Alura, o banco de dados guarda informações sobre os usuários, cursos, perguntas, respostas, etc.
    
### Para saber mais: Arquitetura da Alura

    Agora já sabemos que existe um cliente, o navegador, como Chrome e Firefox, e um servidor, a Alura. Para definir as regras de comunicação entre cliente e servidor, existe o protocolo HTTP.
    
    Também já sabemos que o servidor usa alguma plataforma, como PHP, Java, .Net ou outros. Qual plataforma realmente é utilizada? Não é tão fácil de descobrir, pois o HTTP, de propósito, não está focado em alguma plataforma específica e esconde isso de nós. Bom, eu não vou esconder nada e vou contar para vocês que a Alura usa a plataforma Java e o servidor concreto se chama Tomcat.
    
    Também já falamos que o SQL é uma linguagem para consultar o banco de dados. Alura usa SQL para acessar o banco de dados MySQL.
    
    Com essas informações já temos uma breve ideia da arquitetura da Alura!
    
> Cliente  <--- HTTP ---> Servidor Java  <--- SQL ---> Banco de dados

    Visualizando:
<center><img src="https://s3.amazonaws.com/caelum-online-public/http/arquitetura_alura.png"></center>


#### Opinião do instrutor
    Há arquiteturas muito mais complexas, mas a grande maioria usa o protocolo HTTP no topo. O protocolo HTTP garante a conectividade. Isso quer dizer que o protocolo HTTP funciona em todos os lugares, sem ter problemas com firewalls e outras regras de segurança. Nós podemos nos conectar sem maiores problemas com qualquer servidor no mundo!            
    
## 02. A web segura - HTTPS
### A versão segura do HTTP
    Quando fazemos uma solicitação ao servidor o navegador obtem uma resposta do servidor. Para verificar as solicitações do navegador e respostas do servidor utilizamos as "Ferramentas para Desenvolvedor" do navegador.
> F12 --> Aba: NETWORK --> Requisição: signin --> Headers: FormData 

    O HTTPS é o protocolo HTTP + SSL(Secure Sockets Layer)/TLS(Transport Layer Security) uma camada de segurança para transferência dos dados.

### Exercício: Enviando dados com HTTP
    O que acontece com nossos dados quando usamos HTTP , ou seja sem a letra S ao final?
    
    a) Alternativa correta: Os dados são transportados em texto puro para o servidor, visível para qualquer um.
        Exato, nossos dados são enviados em texto puro, ficando visível para qualquer um que consiga interceptar nossa conexão!
    b) Os dados são criptografados, para impedir a visualização por intermediários.
    c) Usamos automaticamente um certificado digital para provar a identidade de um site.
        
> Quando usamos HTTP, os dados são enviados em texto puro. O que pode ser perigoso, já que assim deixamos os dados abertos para intermediários.
    
### Funcionamento do HPPPS

    Para que o navegador confie neste protocolo HTTP é necessário uma identificação/certificado digital.
    O certificado digital possui uma chave pública que criptografa a informação enviado pelo navegador. O servidor possui uma chave privada que descriptografa a informação.
    - web segura
    - certificado digital(identidade)
    - chvaes(pública e privada)

### Certificado digital
    Quando precisamos informar nossos dados a algum servidor, queremos ter certeza que este servidor realmente representa a entidade em questão. Queremos confiar em quem estamos fornecendo nossos dados!

    Um certificado digital prova uma identidade para um site, onde temos informações sobre o seu domínio e a data de expiração desse certificado.

    Além disso, o certificado ainda guarda a chave pública que é utilizada para criptografar (cifrar) os dados que são trafegados entre cliente e servidor.

### Exercício: Características do HTTPS

    Sobre as características do HTTPS, selecione todas as opções abaixo que estejam corretas:

    a) Alternativa correta: A chave privada fica apenas no lado do servidor.
        Exato, a chave privada é utilizada para descriptografar os dados que foram criptografados com a chave pública, por isso ela é importante e deve ficar apenas em posse do servidor.
    b) HTTP significa usar um certificado digital do servidor.
    c) Alternativa correta: O certificado prova a identidade e tem validade.
        Correto, todo certificado tem uma data validade e serve para provar a identidade entre o cliente e o servidor.
    d) Alternativa correta: O certificado guarda a chave pública.
        Perfeito, é no certificado digital que encontramos a chave pública utilizada para criptografar os nossos dados.

> Lembrando o HTTP não utiliza criptografia nenhuma e é inseguro! Para deixar a web segura devemos usar o HTTPS sempre.

### Exercício: Autoridade certificadora

    Qual é a finalidade das autoridades certificadoras?

    a) Alternativa correta: Garantir que podemos confiar naquele certificado (identidade).
        Exato, a principal função de uma entidade certificadora é garantir que os certificados que estão sendo utilizados podem ser confiados.
    b) Importar/Exportar chaves publicas do servidor.
    c) Usada para registrarmos nomes de domínio (DNS).
    d) Realizar a criptografia dos dados da requisição.

> Essa garantia é feita através de uma assinatura digital. A autoridade certificadora (CA) assina digitalmente o certificado! Como na vida real, existem também no mundo digital: assinaturas!

> Uma autoridade certificadora (CA - Certificate Authority) é um órgão que garante ao navegador e ao usuário que a identidade de um servidor (por exemplo o servidor da Alura) é realmente válida. Portanto, podemos trocar informações com este sem riscos!

### Para saber mais: As chaves do HTTPS

    Aprendemos no vídeo que o HTTPS usa uma chave pública e uma chave privada. As chaves estão ligadas matematicamente, o que foi cifrado pela chave pública só pode ser decifrado pela chave privada. Isso garante que os dados cifrados pelo navegador (chave pública) só podem ser lidos pelo servidor (chave privada). Como temos duas chaves diferentes envolvidas, esse método de criptografia é chamado de criptografia assimétrica. No entanto, a criptografia assimétrica tem um problema, ela é lenta.

<center><img src="https://s3.amazonaws.com/caelum-online-public/http/cripto-assimetrica.png"></center>

    Por outro lado, temos a criptografia simétrica, que usa a mesma chave para cifrar e decifrar os dados, como na vida real, onde usamos a mesma chave para abrir e fechar a porta. A criptografia simétrica é muito mais rápida, mas infelizmente não tão segura. Como existe apenas uma chave, ela ficará espalhada pelos clientes (navegadores) e qualquer um, que tem a posse dessa chave, pode decifrar a comunicação.

<center><img src="https://s3.amazonaws.com/caelum-online-public/http/cripto-simetrica.png"></center>

    Agora, o interessante é que o HTTPS usa ambos os métodos de criptografia, assimétrica e simétrica. Como assim? Muita calma, tudo o que aprendemos é verdade! Só faltou o grande final :)

    No certificado, vem a chave pública para o cliente utilizar, certo? E o servidor continua na posse da chave privada, ok? Isso é seguro, mas lento e por isso o cliente gera uma chave simétrica ao vivo. Uma chave só para ele e o servidor com o qual está se comunicando naquele momento! Essa chave exclusiva (e simétrica) é então enviada para o servidor utilizando a criptografia assimétrica (chave privada e pública) e então é utilizada para o restante da comunicação.

    Então, HTTPS começa com criptografia assimétrica para depois mudar para criptografia simétrica. Essa chave simétrica será gerada no início da comunicação e será reaproveitada nas requisições seguintes. Bem-vindo ao mundo fantástico do HTTPS :)

## 03. Endereços sob seu domínio
### Endereços

#### URL
> - HTTP://WWW.ALURA.COM.BR
>
>       protocolo:  HTTP
>       domínio:    WWW.ALURA.COM.BR
>       raiz:       COM / BR / ORG / NET / ...
>       sub-domíno:        COM / GOV / EDU / ...
>

> - HTTP://172.217.29.68
>
>       ip:        172.217.29.68 (DNS)
>

### Exercício: O que é um domínio na internet?

    Falamos bastante sobre o domínio nessa aula, mas o que é um domínio (ou domain name) e qual a sua importância?

    a) O domínio é o endereço que digitamos no navegador para acessar o site. Para isso, precisamos registrá-lo no servidor de domínios do Google.
    b) Domínio é permitir uma conexão segura com o site Web de forma que o servidor garante a integridade do serviço. Falamos que o serviço foi acessado de forma dominante.
    c) Alternativa correta: O domínio é o nome do site na Web. Ele facilita a navegação do usuário, que não precisa lembrar o IP de cada site.
        Alternativa correta, o domínio é o nome do site na web e serve para facilitar a navegação do usuário, que acaba não precisando lembrar o IP de cada site.
    d) Domínios eram uma forma primordial de acesso à Internet antes da popularização dos navegadores modernos. Atualmente não são mais usados e o comum é acessar pelo nome de acesso (Access Name).

### Exercício: Como funciona o DNS?

    Qual é o objetivo ou a função do DNS (Domain Name System ou servidor de domínios)?

    a) Alternativa correta: O DNS tem como função realizar a tradução do nome de um domínio para o endereço de IP correspondente.
        O DNS realiza a tradução do nome de um domínio para o endereço de IP. Existem vários servidores DNS no mundo e é fundamental para a nossa web o funcionamento deles.
    b) O DNS é um protocolo usado no acesso remoto a uma caixa de correio eletrônico.
    c) O DNS serve para transferir arquivos pela internet de forma rápida e versátil.
    d) O DNS é usado para permitir o acesso seguro em redes inseguras, sendo muito usado para realizar o acesso remoto em outros computadores.

### Portas

> HTTP:     80<br>
> HTTPS:    443

    As portas de comunicação abertas no servidor.

### Exercício: Porta padrão HTTP

    Veja o endereço abaixo:

> http://www.alura.com.brCOPIAR CÓDIGO

    Qual é a porta utilizada?

    a) 443
    b) 8080
    c) 3000
    d) Alternativa correta: 80
        Correto e como ela é o padrão você pode omiti-la no endereço.

> Como as portas padrões são conhecidas pelo navegador, elas podem ser omitidas ao escrevermos uma URL.

> Vários protocolos definem a sua porta padrão como por exemplo o FTP que usa 21 ou SSH que usa 22.

### Recursos

> HTTPS:WWW.ALURA.COM.BR:443/COURSE/INTRODUCAO-HTML-CSS
>
>       protocolo:  HTTPS
>       domínio:    WWW.ALURA.COM.BR
>           raiz:                 BR
>           sub-domínio:      COM
>       porta:      443
>       recursos:   COURSE/INTRODUCAO-HTML-CSS
>
- URL são endereços da WEB
- Uma URL começa com o protocolo(http://) seguido pelo domínio(www.alura.com.br)
- Após o domínio é especificado o caminho para um recurso(course/introducao-html-css)
- Um recurso é algo concreto que queremos acessar

### Exercício: Identificando o protocolo

    Veja a URL abaixo:

>    smb://server/download/videos/http.mp4

    Nesse exemplo, como se chama o protocolo?

    a) http
    b) server
    c) ftp
    d) smb
        Correto, o protocolo especificado na URL se chama smb (aquilo que vem antes do ://)

> O protocolo especificado nessa URL se chama smb.

> Lembrando que a URL sempre começa com o nome do protocolo:

<center><img src="https://s3.amazonaws.com/caelum-online-public/http/http-url.png"></center>

> - O protocolo smb realmente existe e é a abreviação de Server Message Block. Ele é utilizado para compartilhar arquivos dentro de uma rede local.

### Recursos na URL

    Veja a URL a seguir:

>    http://g1.globo.com/index.html

    Qual é o nome do recurso?

    a) g1.com.br
    b) Alternativa correta: /index.html
        Alternativa correta, o recurso é aquilo que vem depois do domínio/.
    c) g1.globo.com/index.html
    d) http
    e) g1

> No início da web, os recursos, na grande maioria, eram arquivos com a extensão .html ou .htm. Até hoje existem vários recursos que são arquivos na web. Mas reparem que a Alura não funciona dessa maneira. Em nenhum momento você acessa um arquivo no Alura. Por exemplo, para ver um curso, você usa a URL:
>>https://cursos.alura.com.br/course/introducao-html-css

Isso é um pouco mais legível e possui a vantagem que a URL não diz nada a respeito do formato. A URL não fica amarrada ao formato HTML.

### Para saber mais: URI ou URL?

    Muitas vezes, desenvolvedores usam a sigla URI (Uniform Resource Identifier) quando falam de endereços na web. Alguns preferem URL (Uniform Resource Locator), e alguns misturam as duas siglas à vontade. Há uma certa confusão no mercado a respeito e mesmo desenvolvedores experientes não sabem explicar a diferença. Então, qual é a diferença?

    Resposta 1 (fácil): Uma URL é uma URI. No contexto do desenvolvimento web, ambas as siglas são válidas para falar de endereços na web. As siglas são praticamente sinônimos e são utilizadas dessa forma.

    Resposta 2 (mais elaborada): Uma URL é uma URI, mas nem todas as URI's são URL's! Existem URI's que identificam um recurso sem definir o endereço, nem o protocolo. Em outras palavras, uma URL representa uma identificação de um recurso (URI) através do endereço, mas nem todas as identificações são URL's.

    Humm ... ficou claro? Não? Vamos dar um exemplo! Existe um outro padrão que se chama URN (Uniform Resource Name). Agora adivinha, os URN's também são URI's! Um URN segue também uma sintaxe bem definida, algo assim urn:cursos:alura:course:introducao-html-css. Repare que criamos uma outra identificação do curso Introdução ao HTML e CSS da Alura, mas essa identificação não é um endereço.

<center><img src="https://s3.amazonaws.com/caelum-online-public/http/http-uri-urn-url.png" ></center>

    Novamente, a resposta 2 vai muito além do que você realmente precisa no dia a dia. Normalmente URL e URI são usados como sinônimos.

## 04. O cliente pede e o servidor responde
### Modelo Requisição e Resposta

    Cada requisição é única. Não guarda informações de requisições anteriores.
    Sessão é uma validação de login de um usuário, chave e valor, sendo um cookies. Cookies são pares de chave e valor.
    - O protocolo HTTP segue o modelo REQUEST-RESPONSE
    - Uma requisição precisa ter todas as informações para o servidor gerar a resposta
    - HTTP é STATELESS!(Não mantém informações entre requisições)
    - As plataformas de desenvolvimento usam sessões para guardar informações entre requisições

### Exercício: O HTTP e o estado das requisições

    Qual das informações abaixo é verdadeira?

    a) O HTTP guarda o estado das requisições no navegador do usuário. Por consequência, a segunda requisição sempre será feita para o mesmo destino da primeira.
        O HTTP faz uso de comunicação sem estado (stateless), isto é, a cada nova requisição é necessário passar todas as informações necessárias ao servidor.
    b) Alternativa correta: Uma requisição sempre deve ser enviada com todas as informações necessárias, o que faz uma requisição ser sempre independente das demais.
    c) A letra s na sigla HTTPS significa stateless. Usamos HTTPs para trabalharmos com um protocolo sem armazenamento de estado.
        O S de HTTPS significa secure, que indica que é uma implementação do HTTP, mas utilizando uma camada adicional de segurança.

> Todas as informações necessárias sempre devem estar contidas na requisição que será enviada, tornando-a independente das demais.

### Exercício: Sessão HTTP

    O que é uma sessão HTTP?

    a) É o número gerado para identificar o cliente.
    b) É o tempo entre requisição e resposta.
    c) É o número gerado para identificar o servidor.
    d) Alternativa correta: É o tempo que o cliente utiliza um web app.

> Uma sessão HTTP nada mais é que um tempo que o cliente permanece ativo no sistema! Isso é parecido com uma sessão no cinema. Uma sessão, nesse contexto, é o tempo que o cliente usa a sala no cinema para assistir a um filme. Quando você sai da sala, termina a sessão. Ou seja, quando você se desloga, a Alura termina a sua sessão.

### O que é um cookie?

Vimos no vídeo o uso de um cookie para gravar um número, aquele Session ID. Mas o que é um cookie? Pesquise!

#### Opinião do instrutor

    Quando falamos de Cookies na verdade queremos dizer Cookies HTTP ou Cookie web. Um cookie é um pequeno arquivo de texto, normalmente criado pela aplicação web, para guardar algumas informações sobre usuário no navegador. Quais são essas informações depende um pouco da aplicação. Pode ser que fique gravado alguma preferência do usuário. Ou algumas informações sobre as compras na loja virtual ou, como vimos no vídeo, a identificação do usuário. Isso depende da utilidade para a aplicação web.

    Um cookie pode ser manipulado e até apagado pelo navegador e, quando for salvo no navegador, fica associado com um domínio. Ou seja, podemos ter um cookie para www.alura.com.br, e outro para www.caelum.com.br. Aliás, um site ou web app pode ter vários cookies!

    Podemos visualizar os cookies salvos utilizando o navegador. Como visualizar, depende um pouco do navegador em questão:

> No Chrome: Configurações -> Privacidade -> Configurações de conteúdo... -> Todos os cookies e dados de site... -> Pesquisar alura

> No Firefox: Preferências -> Privacidade -> remover cookies individualmente -> Pesquisar alura

### Login e Senha

    Quando estamos autenticados em algum sistema, como a Alura, é necessário sempre enviar o e-mail e senha a cada requisição?
    
#### Opinião do instrutor

    Quando enviamos uma requisição HTTP, todos os dados para que ela seja respondida devem ser enviados. Mas e o e-mail e a senha? Quando o login é feito, a Alura tem certeza de que um usuário existe e gera uma identificação quase aleatória pra esse usuário, lembra? E esse número fica salvo em um arquivo especial, chamado cookie, que é gerado e enviado por cada site :)

### EXercício: Comunicaçõ em HTTP

Qual dessas alternativas é verdadeira?

    a) Em HTTP o servidor sempre envia uma requisição ao cliente para poder alterar algo na tela.
    b) Alternativa correta: Uma comunicação com HTTP sempre é iniciada pelo cliente que manda uma requisição ao servidor esperando por uma resposta.
    c) Quando trabalhamos com HTTP, a comunicação é sempre iniciada pelo lado do cliente que envia uma requisição ao servidor em busca de uma resposta. Mas em alguns casos, o servidor também pode enviar uma requisição ao cliente.

> É importante lembrarmos que a comunicação sempre começa com o cliente: é ele quem pede as informações. O servidor responde apenas o que foi requisitado e nunca inicia a comunicação :)

> No HTTP: Request -> espera -> Resposta

## 05. Depurando a requisição HTTP
### Depurando o método HTTP

    Depurando uma requisição

>   Ferramenta de Desenvolvedor: F12 -> Aba: Network -> Requisição:site -> Aba: Headers -> Categoria: General
 - nome: nome da requisição
 - status: selecionar para mais detalhes

### Console no Firefox e Internet Explorer

    Para abrir o console no Mozilla Firefox basta apertar a tecla F12, ou CTRL + SHIFT + I. Ele também pode ser acessado pelo menu: Ferramentas -> Desenvolvedor web -> Exibir/Ocultar ferramentas**.

<center><img src="https://s3.amazonaws.com/caelum-online-public/http/firefox-console.png"></center>

    No Microsoft Internet Explorer basta apertar a tecla F12 ou ir pelo menu de configuração: F12 Ferramentas do desenvolvedor.

<center><img src="https://s3.amazonaws.com/caelum-online-public/http/iexplorer-console.png"></center>

<center><img src="https://s3.amazonaws.com/caelum-online-public/http/iexplorer-console-aberto.png"></center>

    No Safari basta usa o atalho COMMAND + SHIFT + C .

### Exercício: Analisando _Request_ e _Response_ 1

    Abaixo há um exemplo de uma requisição e resposta, usando a ferramenta telnet. Através dele, acessamos www.caelum.com.br na porta padrão 80.

<center><img src="https://s3.amazonaws.com/caelum-online-public/http/telnet-http.png"></center>

    O telnet estabelece apenas uma conexão TCP (protocolo de rede que roda abaixo do HTTP) e permite que enviemos dados em cima dessa conexão, através do terminal. Uma vez a conexão estabelecida, basta escrever no terminal e os dados serão enviados automaticamente para o servidor. Para o servidor realmente entender os dados, devemos respeitar a sintaxe do protocolo HTTP!

    Nesse exemplo digitamos no terminal:

>    GET / HTTP/1.1<BR>
>    HOST: www.caelum.com.br<br>

    E a resposta do servidor segue logo abaixo:

>    HTTP/1.1 200 OK<br>
>    Content-Type: text/html; charset=utf-8<br>
>    Vary: Accept-Encoding,User-Agent<br>
>    Content-Language: pt-br<br>
>    Date: Mon, 01 Jun 2015 21:00:20 GMT<br>
>    Server: Google Frontend<br>
>    Cache-Control: private

    Agora, baseado nesses dados, qual foi o método HTTP e código da resposta?

    a) HTTP e 1.1
    b) HOST e 200
    c) GET e 1.1
    d) Alternativa correta: GET e 200

> O método HTTP é GET e o código da resposta é 200.

> Lembrando que o método define a ação ou intenção da requisição HTTP (GET é igual a receber). O código da resposta dá uma dica ao cliente se a requisição foi um sucesso ou não, e qual foi o problema em caso de falha. O código 200 significa que tudo deu certo!

### Depurando os códigos de resposta HTTP

>   Ferramenta de Desenvolvedor: F12 -> Aba: Network -> Requisição:site -> Aba: Headers -> Categoria: General
 - nome: nome da requisição
 - status code:
   - 2XX: Successful responses
      - 200: ok, sucesso na solicitação
   - 3XX: Redirection messages
      - 301: moved permanently, novo endereço de requisição
   - 4XX: Client error responses
      - 404: not found, recurso não localizado
   - 5XX: Server error responses
     - 500: internal server error, erro interno no servidor

### Exercício: Código de sucesso

    Qualquer resposta HTTP possui um número que informa sobre o status da requisição.

    Qual dos códigos abaixo indica que a requisição foi bem sucedida?

    a) 100
    b) 404
    c) 300
    d) Alternativa correta: 200

> O código 200 significa OK, ou Sucesso, que não houve nenhum problema no processamento da requisição e ela foi bem sucedida.

> Existem mais códigos que começam com 2xx. No entanto 200 é de longe o mais utilizado, principalmente no desenvolvimento de uma aplicação web.

> Na documentação oficial, se diz a respeito da classe de códigos que começam com 2xx:<br>
>  - 2xx - Resposta bem sucedida!
    Essa classe de códigos de status indica que a ação solicitada pelo cliente foi recebida, compreendida, aceita e processada com êxito.

    A tabela completa de mensagens HTTP pode ser vista em: https://www.w3schools.com/tags/ref_httpmessages.asp.

### Exercício: Problema no servidor

    Vimos que há diversos códigos HTTP. Vendo os códigos abaixo, qual deles representa algum problema gerado no servidor?

    a) 302
    b) 402
    c) Alternativa correta: 500
    d) 301

> A classe 5xx significa que houve algum problema no servidor.

> Por exemplo: 500 - Internal Server Error, ou outro famoso: 503 - Service Unavailable.

> O código 500 acontece com frequência quando estamos desenvolvendo uma aplicação web e, ao testar, percebemos que erramos algo na lógica que gerou um problema no servidor.

### Exercício: Recurso não encontrado

    Abra uma nova aba no navegador e tente acessar: http://g1.globo.com/algo-que-nao-existe

    Qual foi o código da resposta?

    Obs: Você precisa depurar a requisição HTTP para descobrir o código da resposta.

    a) 500
    b) 405
    c) 200
    d) Alternativa correta: 404

> 404 é o código clássico que indica que o recurso não foi encontrado. Em geral, a classe 4xx indica que o cliente errou algo na requisição.

> Segue um outro exemplo da classe 4xx, tente acessar: https://s3.amazonaws.com/caelum-online-public/http/qq.png
> -  Nesse caso o código de resposta é 403(não permitido): o cliente não tem a permissão.

### Exercício: Analisando _Request_ e _Response_ 2

    Repare os cabeçalhos da requisição e resposta:

<center><img src="https://s3.amazonaws.com/caelum-online-public/http/telnet-http-302-v2.png"></center>

    Seguem 4 afirmações:

    1) O código da resposta é 302.

    2) O recurso solicitado é /cursos/.

    3) O cliente não recebeu a resposta.

    4) O servidor está pedindo um redirecionamento.

    Avalie as afirmações e escolha a resposta correta:

    a) Alternativa correta: Apenas as afirmativas 1 e 4 são verdadeiras.
    b) Todas as afirmativas são verdadeiras.
    c) Apenas as afirmativas 1, 2 e 4 são verdadeiras.
    d) Apenas as afirmativas 2 e 3 são verdadeiras.

> 1) O código da resposta é 302.
> - Correto, o código aparece na resposta. O código 302 significa Movido Temporariamente.
> 2) O recurso solicitado é /cursos/.
> - Errado, pois na requisição aparece: GET /treinamento HTTP/1.1.
> 3) O cliente não recebeu a resposta.
> - Errado, pois foi enviada sim uma resposta para o cliente.
> 4) O servidor está pedindo um redirecionamento.
> - Correto, na resposta aparece o cabeçalho Location, que define o redirecionamento para http://www.caelum.com.br/cursos/.


> Portanto, as afirmativas 1 e 4 são verdadeiras.

### Exercício: Classes de códigos

    Já vimos 3 classes do protocolo HTTP: 2xx, 4xx e 5xx.

<center><img src="https://s3.amazonaws.com/caelum-online-public/http/classe-http-1.png"></center>

    Para que existem os códigos 3xx?

    a) Alternativa correta: Redirecionamento.
    b) Comunicação unidirecional.
    c) Erro no intermediário.
    d) Virus encontrado.

> A classe do código 3xx é relacionada com o redirecionamento.

> Nesse caso, o cliente (navegador) deve tomar medidas extras para concluir o pedido. Normalmente são utilizados os códigos 301 ou 302, junto com o cabeçalho de resposta Location.

> Por exemplo, veja a requisição, tentando acessar a Alura através do protocolo HTTP (sem S):
> > GET / HTTP/1.1<br>
  > HOST: www.alura.com.br<br>
>
> Na resposta, recebemos o código 301 e o cabeçalho Location para enviar uma nova requisição, usando o protocolo HTTPS:
> > HTTP/1.1 301 Moved Permanently<br>
    Server: nginx/1.6.2<br>
    Date: Tue, 02 Jun 2015 19:37:44 GMT<br>
    Content-Type: text/html<br>
    Content-Length: 184<br>
    Location: https://www.alura.com.br/<br>

### Para saber mais: Mais códigos HTTP

HTTP é o protocolo mais utilizado na internet e há muita documentação disponível. Segue um link que explica os códigos HTTP de forma divertida: <a href="https://httpstatusdogs.com/" target="_blank">httpstatusdogs</a> ou se você preferir gatos <a href="https://http.cat/" target="_blank">httpcats</a>

    Espero que goste :)

    #### Opinião do instrutor

    Além de se aprender de forma divertida com os cachorrinhos, você pode conferir uma documentação mais completa e detalhada neste link: https://httpstatuses.com/

## 06. Parâmetros da requisição
### Exercício: A qual grupo eu pertenço?

    Com base na família de erros que você aprendeu no curso, marque a alternativa correta:

    a) 
    200, 203, 207 -> Respostas de Sucesso
    500, 502, 503 -> Mensagem de redirecionamento
    300, 201, 302 -> Respostas de erro do cliente
    401, 404, 405 -> Respostas de erro do servidor


    b) 
    200, 203, 207 -> Respostas de Sucesso
    401, 404, 405 -> Mensagem de redirecionamento
    300, 201, 302 -> Respostas de erro do cliente
    500, 502, 503 -> Respostas de erro do servidor

    c) Alternativa correta
    200, 203, 207 -> Respostas de Sucesso
    300, 301, 302 -> Mensagem de redirecionamento
    401, 404, 405 -> Respostas de erro do cliente
    500, 502, 503 -> Respostas de erro do servidor

### Paraâmetros na requisição com métodos GET e POST

- GET: Receber dados. Passagem de parâmetros pela URL

- POST: Submeter dados. Passagem de parâmetros no corpo da requisição

- DELETE: Remove um recurso.

- PUT: Atualizar um recurso.

### Exercício: Testando parâmetros de requisição

    Vamos testar o envio de parâmetros através da requisição, fazendo uma busca no Google pela palavra Alura.

    Para isso, na URI do Google, vamos enviar na requisição o parâmetro q com o valor Alura. Ou seja: 
>    google.com.br/search?q=Alura

    Ao entrar nessa URI, qual método HTTP foi usado?

    a) Outro método.
    b) POST.
    c) Alternativa correta: GET.

> Resposta correta: GET<br>
> Quando passamos os parâmetros da requisição na URL, estamos fazendo uso do método GET. O que é super útil quando precisamos repetir a requisição com os mesmos parâmetros :)

### Exercício: Enviando parâmetros de forma correta

    Vimos que podemos enviar parâmetros em uma URL. Então, qual é a forma correta de enviá-los?

    a) http://calculadordeimc.com.br/&peso=44&altura=1.50
    b) http://calculadordeimc.com.br/?peso=44,altura=1.50
    c)     Alternativa correta: http://calculadordeimc.com.br/?peso=44&altura=1.50
    d) http://calculadordeimc.com.br/&peso=44?altura=1.50

> Quando enviamos parâmetros na URL, devemos iniciar pelo ?, o nome do parâmetro e um =, para separar o nome do parâmetro do seu valor:
 - ?nome_do_parametro=seu_valor
 - Quando usamos mais do que, um parâmetro devemos usar & para separá-los:
   - ?nome_do_parametro=seu_valor&nome_do_outro_param=valor

### Exercício: Qual é o método HTTP?

    Veja os dados da requisição:

> AQUI /vendas?ano=2014 HTTP/1.1<br>
> HOST: www.vendasfuturas.com.br

    Qual método HTTP devemos colocar no lugar de AQUI para a requisição funcionar corretamente?

    a) POST
    b) PUT
    c) Alternativa correta: GET
    d) DELETE

> GET é normalmente usado para pesquisas, mas isso depende um pouco de como a plataforma e o desenvolvedor usam esse método. Na vida real, vocês vão encontrar muitos exemplos que usam requisições do tipo GET, não só para pesquisas.
> - O protocolo HTTP define que o GET deve ser utilizado apenas para acessar os dados, mas HTTP, como protocolo, não pode impedir o desenvolvedor de fazer algo diferente. Por exemplo, veja a requisição a seguir:

>    GET /vendas/remove?id=53 HTTP/1.1<br>
>    HOST: www.vendasfuturas.com.br

>    Usamos GET, mas repare que o nome do recurso muda a intenção do método HTTP. O recurso se chama /vendas/remove, ou seja, queremos apagar a venda com a identificação 53, usando o método GET!

>    O protocolo HTTP define apenas algumas regras entre cliente e servidor. O que o servidor realmente faz depende da implementação, ok?

>    OBS: Se tiver com código 500 na cabeça, abra uma pergunta no fórum :)

### Exercício: Por que POST?

    Seguem os dados da requisição para efetuar o login na plataforma Alura:

>    POST /signin/ HTTP/1.1<br>
>    HOST: https://www.alura.com.br<br>
>    Content-Type: application/x-www-form-urlencoded<br>
>    email=nico.steppat%40caelum.com.br&senha=totalmentesecreta

    Por que foi utilizado o método POST?

    a) Foi utilizado POST. Mas como não há diferença, poderíamos usar GET.
    b) Usamos POST para deixar os parâmetros explícitos na URL.
    c) Usamos POST para definir o recurso.
    d) Alternativa correta: Usamos POST para incluir os parâmetros no corpo da requisição.

>    Utilizando o método GET, tanto o login quanto a senha seriam passados como parâmetro na URL, coisa que não queremos que aconteça. O método POST deixa os parâmetros no corpo da requisição, assim evita que informações importantes, como a senha, fiquem explícitas na URL.

> Usando o método GET, a URL ficaria:
> - GET /signin/?email=nico.steppat@caelum.com.br&senha=totalmentesecreta HTTP/1.1<br>
    HOST: https://www.alura.com.br

> Logo, o POST foi utilizado para que se enviasse os valores do formulário no corpo da requisição.
  
### Para saber mais: Parâmetros na URL

    Como, por exemplo, podemos enviar uma requisição usando o método GET para carregarmos a página que exibe informações sobre o usuário de número 2? Devemos passar o parâmetro id com o valor 2. Como por exemplo:

>    http://meusite.com.br/usuario?id=2

    Uma outra forma de fazer seria passar os valores na própria URL! Veja o exemplo:

>   http://meusite.com.br/usuario/2

    Mas tem um probleminha, não estamos dizendo explicitamente que o valor 2 realmente representa o id. Quando um parâmetro irá receber um certo valor, devemos combinar com o servidor (com o desenvolvedor da aplicação). Neste caso, foi combinado que o parâmetro recebido seria equivalente ao id passado antes.

    Vamos ver um exemplo prático, em um serviço que retorna informações sobre um endereço de um determinado CEP? Acesse a URL:
>   http://viacep.com.br/ws/20040030/json

    A resposta será todas as informações do CEP da Caelum Rio, como complemento, número e bairro, formatadas em JSON. Isso significa que foi combinado com o servidor, que o primeiro valor passado depois de ws deve ser o CEP e logo após, o formato em que os dados deverão chegar. No nosso caso, JSON. Tudo bem? :)

    Experimente agora trocar para o CEP de sua casa e para outro formato de dados, como por exemplo, XML.

### Para saber mais: Outros métodos HTTP e Web Services

    Já falamos bastante sobre os métodos (ou verbos) HTTP, GET e POST. Esses dois são utilizados na grande maioria das aplicações web, e fazem parte do dia a dia do desenvolvedor, no entanto existem diversos outros métodos.

    Se o GET foi criado para receber dados, e o POST para adicionar algo no servidor, será que não existe algo para apagar e atualizar?

    A resposta é sim, e os métodos se chamam DELETE e PUT.

    Novamente esses métodos normalmente não são utilizados quando se trata de uma aplicação web, e são mais importantes quando o assunto é Web Services.

    Agora vem a pergunta, você já ouviu falar de Web Services?

#### Opinião do instrutor

    Quando falamos de um Web Service, sempre usamos o protocolo da web, ou seja o HTTP.

    Um Web Service disponibiliza uma funcionalidade na web, através do protocolo HTTP. As funcionalidades variam muito e dependem muito da empresa e do negócio dela, mas por exemplo, na Alura temos um Web Service que traz todas as informações de um curso (nome, capítulos, exercícios, etc). O Google ou Facebook possuem muitos Web Services para acessar um usuário, ver os posts dele, interesses, etc. Muitas vezes esses serviços são pagos.

    O importante é que sempre usamos o protocolo HTTP. A grande diferença de um Web Service é que os dados não vem no formato HTML, e sim em algum formato independente da visualização, como XML ou JSON.

    Temos um pequeno exemplo de um Web Services que usamos em um dos treinamentos presenciais. Tente acessar: http://argentumws.caelum.com.br/negociacoes

    Repare que recebemos dados sobre negociações, mas o formato é XML. Isso é um Web Service! É a tarefa do cliente ler os dados e apresentar para o usuário final. O cliente não precisa ser o navegador (e normalmente não é), pode ser um celular ou uma aplicação Desktop.

## 07. Serviços na web com REST
### Serviços Web-REST

    Os serviços Web-REST são aplicações que fazem request para o servidor e obtém com response objeto JSON ou XML, não HTML.
    
> Aplicação<br>
> GET: http://site.com/api/restaurantes<br>
> Accept: application/json

> Servidor<br>
> Status Code: 200<br>
> Content-type: application/json

### Exercício: Métodos HTTP

    No desenvolvimento Web, para requisição e envio de dados através de formulários, quais são os métodos HTTP que são mais utilizados pelos desenvolvedores no dia a dia?

    a) Alternativa correta: GET e POST
        Correto, GET e POST são de longe os métodos mais utilizados.
    b) DELETE e PUT
    c) PUT e POST
    d) GET e HEAD

>    Os métodos GET e POST são de longe os métodos mais utilizados no desenvolvimento web, mas porque isso?
> -    A resposta está no próprio HTML. Por padrão, as páginas HTML fazem apenas requisições do tipo GET ou POST. Para o tipo POST especificamente, precisamos fazer uso da tag form, configurando o atributo method como POST, ao invés do seu valor padrão que é GET. O outro caso é quando usamos a tag a que cria um link de uma página para outra, fazendo com o que o navegador execute uma requisição do tipo GET.

> Para fazer requisições usando métodos como PUT ou DELETE, precisamos fazer com código JavaScript.

### Exercício: Sobre o HTTP

    Leia abaixo as afirmações sobre o protocolo.

    Marque todas as afirmações verdadeiras:

    a) HTTP sempre deve ser utilizado em conjunto com HTML.
    b) Alternativa correta: Requisições HTTP podem ser enviadas através de qualquer aplicativo/software que entenda o protocolo.
        - Afirmação correta , o HTTP não depende do navegador. Aliás, o tempo todo o nosso celular usa o HTTP para enviar requisições através de aplicativos!
    c) Alternativa correta: HTTP é totalmente independente do formato dos dados.
        Afirmação correta pois HTTP não depende de um formato especifico!
    d) HTTP não possui cabeçalhos para indicar o formato.
    e) Alternativa correta: HTTP pode trafegar tanto dados binários quanto dados textuais.
        Afirmação correta pois HTTP pode trafegar dados binários como imagens e dados textuais como HTML ou CSS!

### Exercício: Sobre o formato

    O protocolo HTTP envia dados em texto puro e já estudamos sobre as implicações disso em questões de segurança. Vimos inclusive como o HTTPS lida com isso.

    Em alguns momentos se faz necessário avisar na própria requisição um formato específico esperado para a resposta.

    De que forma podemos especificar o formato que esperamos que seja devolvido?

    a) Pelo cabeçalho Content-Type.
        O cabeçalho Content-Type, como o próprio nome sugere, traz informações sobre o tipo de conteúdo que está sendo trafegado. Logo se formos enviar através do HTTP um conteúdo JSON podemos especificar isso através dele. Ele, portanto, não tem relação com o formato esperado na resposta.
    b) Pelo cabeçalho Accept-Type.
        Accept-Type não é um cabeçalho válido para o HTTP.
    c) Somente por um parâmetro na requisição já que o HTTP não lida com formatos específicos além de texto. Exemplo: /restaurantes?format=json.
        Especificar como parâmetro na requisição é até usado em algumas serviços, embora existe sim como definir via cabeçalho HTTP esse formato.
    d) Pelo cabeçalho Accept-Language.
        Accept-Language é um cabeçalho que podemos usar para definir a linguagem usada.
        Usa-se o seguinte formato:
        Accept-Language: <linguagem-localização(opcional)>
        Como em:
            Accept-Language: en, Accept-Language: en-US(inglês americano) e Accept-Language: pt-BR(português brasileiro)COPIAR CÓDIGO
    e) Alternativa correta: Pelo cabeçalho Accept.
        Através dele podemos usar algum formato específico como:
            Accept: text/html, Accept: text/css, Accept: application/xml, Accept: application/json, Accept:image/jpeg e Accept: image/*
            
            Ou até mesmo não definir nenhum formato específico colocando:
        
            Accept: */*

>    A resposta correta é usando o cabeçalho Accept.
>
>    Através dele podemos usar algum formato específico como:
>
> - Accept: text/html, Accept: text/css, Accept: application/xml, Accept: application/json, Accept:image/jpeg e Accept: image/*<br>

    Ou até mesmo não definir nenhum formato específico colocando:

> - Accept: */*

### O que é REST?

> URI + METHOD<br>

> - pede todos os restaurantes
> http://alurafood.com/api/restaurante - GET<br>
> - adiciona um restaurante
> http://alurafood.com/api/restaurante - POST<br>
> - atualiza o restaurante 1
> http://alurafood.com/api/restaurante/1 - PUT/PATCH<br>
> - remove o restaurante 1
> http://alurafood.com/api/restaurante/1 - DELETE<br>

    O REST(REpresentational State Transfe) é a solicitação de request por meio do URI + METHOD. Muito utilizado por Web-Services.
    - È um padrão arquitetural para comunicação entre aplicações
    - Aproveita da estrutura que o HTTP proporciona
    - Recursos são definidos via URI
    - Operações com os métodos do HTTP (GET/POST/PUT/DELETE)
    - Cabeçalhos (ACCEPT/CONTENT-TYPE) para especificar a representação (JSON, XML, ...)

### Exercício: Solicitando um recurso

    Veja a seguinte URL:

>    http://alura.com.br/cursos/23/exercicios
    
    Supondo que você esteja acessando esse recurso através de uma requisição HTTP GET com o cabeçalho Accept: application/xml, o que se espera que aconteça?

    a) Na resposta recebemos 23 exercícios do curso XML.
        Errado, 23 é o identificador do curso.
    b) Ao receber a requisição o servidor vai remover os exercícios do curso 23.
    c) Na resposta recebemos todos as informações sobre o curso 23 excluindo os exercícios.
    d) Alternativa correta: Na resposta recebemos os exercícios do curso 23 no formato XML.
        Correto, pois GET tem a semântica de receber dados e o formato foi definido por meio do cabeçalho Accept.

>    Resumindo, ao enviar um HTTP GET:
>
>    http://alura.com.br/cursos/23/exercicios
>
>    Devemos receber os exercícios do curso 23 no formato XML.

>    É importante mencionar que isso é o esperado, mas o que realmente acontece depende da implementação do servidor. O protocolo HTTP define uma semântica, mas o servidor pode ou não obedecê-la! Também pode ser que o servidor atenda um formato como JSON, mas não trabalhe com XML.

### Idenficando um recurso

    Sabemos que o domínio da Alura é:

>    cursos.alura.com.br

    Você entrou na equipe de desenvolvedores da Alura e precisa definir o recurso para atualizar uma parte do exercício com a id 3 do curso http. Qual método HTTP e qual URL você escolheria?

    a) DELETE e http://cursos.alura.com.br/cursos/http/exercicios/3
    b) Alternativa correta: PATCH e http://cursos.alura.com.br/cursos/http/exercicios/3
        Correto, PATCH é utilizado para atualização parcial do recurso que foi definido expressivamente: /cursos/http/exercicios/3
    c) GET e http://cursos.alura.com.br/http/3
    d) PATCH e http://cursos.alura.com.br/exercicio/3
        Errado, pois o recurso não especifica o nome do curso.

> Apesar do PATCH fazer parte da especificação e atender corretamente a essa questão, o método mais utilizado para essa finalidade é o PUT.

### Para sber mais: tipos de dados

    Em alguns cabeçalhos do HTTP devemos especificar algum formato. Os formatos são chamados na documentação de MIME types. E na definição do cabeçalho usamos a seguinte estrutura: tipo/subtipo. São tipos conhecidos:

>    text, image, application, audio e video

    E alguns subtipos:

>    text -> text/plain, text/html, text/css, text/javascript<br>
>    image -> image/gif, image/png, image/jpeg<br>
>    audio -> audio/midi, audio/mpeg, audio/webm, audio/ogg, audio/wav<br>
>    video -> video/mp4<br>
>    application -> application/xml,  application/pdf<br>
    
>    Para conhecer outros formatos aceitos você pode acessar aqui:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types

## 08. HTTP2 - Por uma web mais eficiente
### HTTP2 - Dados binários, GZIP ativo e TLS

    Mudanças em relação HTTP 1.0:
    - HEADERS REQUEST/RESPONSE: BINÁRIOS + HPACK(COMPRESSÃO) + TLS(SEGURANÇA-CRIPTOGRAFIA), ANTES TEXTO PURO
    - CONTENT-TYPE: GZIP(COMPRSSÃO) +TLS(SEGURANÇA-CRIPTOGRAFIA), ANTES TEXTO PURO

### Exercício: Motivos por trás do HTTP/2

    Dado o que vimos neste capítulo, aponte quais dos motivos abaixo foram importantes quando decidiram criar uma nova versão do protocolo HTTP, que já estava tão concretizado e estabelecido na Web.

    a) Alternativa correta: Com o crescimento do número de dispositivos móveis conectados a Web, é cada vez mais importante que a quantidade de dados trafegada seja a menor possível, afinal este tipo de dispositivo não costuma ter uma conexão com muita banda larga. O protocolo HTTP/2 traz diversas tecnologias para diminuir o tamanho das requisições.
        Correto, o HTTP/2 possui diversas tecnologias de compactação de sua requisição. Isto acaba sendo muito útil para clientes móveis, visto que a maioria das redes mobile ainda não são de grande qualidade.
    b) Como o número de dispositivos conectados a internet aumentou bastante com a entrada dos dispositivos móveis e o inicio da Internet das Coisas, o protocolo HTTP/1.1 não estava mais sendo adequado para ser utilizado em tantas conexões, visto que ele tem um limite teórico de conexões simultâneas.
    c) Alternativa correta: Por padrão, no protocolo HTTP versão 1.1 não é necessário o uso da camada de segurança TSL/SSL. Como hoje em dia trafegamos muitos dados críticos na Web, como senhas, logins e dados bancários, um protocolo atualizado que faz uso dessa segurança parece quase uma necessidade.
        Correto, com o HTTP/2 o uso de HTTPS acaba sendo obrigatório, e esta é uma das grandes vantagens do uso desta nova atualização do protocolo.

> Apesar do protocolo HTTP/1.1 ter sido de extrema importância para a Web ao longo de vários anos, como toda boa tecnologia, é necessário um update. A nova versão do HTTP veio para adequar este protocolo tão famoso a um mundo onde temos muito mais dados sendo trafegados na rede, e a velocidade de acesso e segurança do usuário se tornam bastante importantes.

### Exercício: A tecnologia HPACK

    Para que serve a tecnologia HPACK implementada no protocolo HTTP/2 ?

    a) Para comprimir o corpo da resposta, reduzindo consideravelmente o tamanho da mesma.
    b) Para comprimir a requisição como um todo, deixando ela mais leve.
    c) Alternativa correta: Para comprimir os Headers da comunicação HTTP, deixando-os mais leves.
        Exato, a tecnologia HPACK é especialista em comprimir os Headers da requisições/respostas HTTP, deixando as mais leves.
    d) Para deixar os dados trafegados em binário, dificultando a interpretação em caso de dados interceptados.

> O HPACK é uma tecnologia especializada em comprimir os Headers das comunicações HTTP/2. Como toda requisição HTTP acompanha algum header por padrão, uma tecnologia de compressão embutida no protocolo é demasiadamente útil para economizar dados trafegados.

### Exercício: Comparações entre versões

    Selecione as afirmativas verdadeiras sobre as versões 1.1 e 2.0 do protocolo HTTP:

    a) O HTTP/2 é muito pouco adotado, já o HTTP/1.1 está presente em toda a Web.
    b) Alternativa correta: No HTTP/1.1 o Gzip não é nativo do protocolo, no HTTP/2 ele já vem por padrão.
        Correto, o Gzip vem nativamente no protocolo HTTP/2.
    c) Alternativa correta: No HTTP/2 o uso do HTTPS é obrigatório, no HTTP/1.1 não.
        Correto, o HTTP/2 reforça bastante o uso do HTTPS, ao contrário do HTTP/1.1 em que isto era opcional. Apesar de não ser obrigatório em sua especificação, os browsers não suportam o HTTP/2 sem HTTPS, o que acaba fazendo com que o seu uso seja exclusivo em modo criptografado.
    d) Alternativa correta: No HTTP/2 os dados são trafegados em binário, no HTTP/1.1 eles são trafegados como texto.
        Correto, uma das principais mudanças é que agora no HTTP/2 os dados são trafegados em binário e não mais em texto puro.

### HTTP2 - Cabeçalhos Stateful

>   GET /
>   host: WWW.CAELUM.COM.BR<br>
>   user-agent: MOZILLA/5.0 (MACINTOSH: INTEL MAC OS X 10.12; RV:34.0)<br>
>   accept: TEXT/HTML, APPLICATION/SHTML+XML, APPLICATION/XML/Q=0.9,*/*;Q=0,8<br>
>   accept-language: PT=BR,PT;Q=0,8,EN-US;Q=0.5,EN;Q=0,3
>   accept-encoding: GZIP, DEFLATE

>   GET /principal.js

>   GET /imagens/logo.png
>   host: WWW.CAELUM.COM.BR<br>
>   accept: IMAGE/PNG,IMAGE/*;Q=0.8,*/*;Q=0,5<br>

    Com o HTTP2 não é necessário enviar os HEADERS em todas as requisições.

### Exercício: Os cabeçalhos que mantêm estado

    Como a tecnologia de Headers Stateful pode nos ajudar a economizar dados?

    a) Alternativa correta: Como trafegamos apenas os headers que mudam de uma requisição para outra, acabamos por economizar uma boa quantidade de dados, pois não precisamos enviar headers que mudam poucas vezes a todo momento, como o Accept.
        Correto, os Headers Stateful permitem que apenas os cabeçalhos que mudem sejam enviados a cada requisição, economizando muita banda que seriam cabeçalhos repetidos.
    b) Como os Headers Stateful mantêm estado, o servidor consegue gerenciar melhor as conexões com múltiplos clientes, fazendo com que dados não sejam enviados para os clientes errados, economizando-se dados por evitar falhas.
    c) Com essa tecnologia os clientes sabem mais facilmente os estados dos servidores, e podem ou não enviar determinados headers de acordo com o número de requisições simultâneas que o servidor estiver lidando, trazendo assim uma economia de dados.

> Quando estamos utilizando Headers Stateful, simplesmente colocamos nas requisições os cabeçalhos que se alteraram entre uma e outra, trazendo uma enorme economia de dados, visto que toda requisição HTTP possui um cabeçalho e que, muitas vezes, no HTTP/1.1, cabeçalhos repetidos eram trafegados em todas as requisições.

### HTTP2- Server Push

    HTTP 1.0
---
    CLIENTE             |           SERVIDOR
    index.html          ->          
                        <-
    eslilo.css          ->
    jquery.js           ->
    principal.js        ->
    logo.png            ->

    eslilo.css          <-
    jquery.js           <-
    principal.js        <-
    logo.png            <-

    HTTP 2.0
---
    CLIENTE             |           SERVIDOR
    index.html          ->          
                        <-
    eslilo.css          <-
    jquery.js           <-
    principal.js        <-
    logo.png            <-

### Exercício: O Server PUsh

    O que é o Server Push no HTTP/2?

    a) O servidor acompanha o histórico de páginas do usuário e tenta prever qual página ele irá requisitar, enviando-a previamente para ele, tornando assim o carregamento mais rápido.
    b) O servidor guarda um identificador específico para cada cliente, e faz o "push" dos dados com determinada configuração, que é personalizada para atender melhor a conexão de cada um dos clientes.
    c) Alternativa correta: O servidor pode empurrar para o clientes certos recursos antes mesmo de serem solicitados, pois ele consegue analisar o HTML e ver o que mais é preciso para carregar a página fazendo com que não seja necessário gastar tempo pedindo todos os outros recursos.

>    Correto, o servidor pode empurrar certas respostas para o cliente antes mesmo delas serem requisitadas.

### HTTP2 - Multiplexação

    KEEP-ALIVE: Tempo de conexão com o servidor por via de protocolo TCP/IP.
    - No HTTP 1.0 são 4 a 8 conexões simultâneas por domínio com requisições síncronas (serial)
    - No HTTP 2.0 com requisições assíncronas (paralela) MULTIPLEXING

### HTTP2 - Resumo

- Atua sobre o que já se conhece de HTTP
- Headers binários ecompimidos(HPACK)
- GZIP padrão na resposta
- Multiplexing(Requisição e resposta são paraleals)
- Headers Stateful(Mandamos apenas os cabeçalhos que mudam)
- Server Push(O servidor manda os recursos que são necessários antes do usuários requisitar)
