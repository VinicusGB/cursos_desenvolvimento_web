https://github.com/VinicusGB/cursos_dev_web# HTTP: Entendo a web por baixo dos panos - 14 horas

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

> #### URL
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
### O HTTP e o mestado das requisições
### Sessão HTTP
### O que é um cookie?
### Login e Senha
### Comunicaçõ em HTTP
## 05. Depurando a requisição HTTP
### Depurando o método HTTP
### Console no Firefox e Internet Explorer
### Analisando _Request_ e _Response_ 1
### Depurando os códigos de resposta HTTP
### Código de sucesso
### Problema no servidor
### Recurso não encontrado
### Analisando _Request_ e _Response_ 2
### Classes de códigos
### Para saber mais: Mais códigos HTTP
## 06. Parâmetros da requisição
### Revisando o capítulo anterior
### A qual grupo eu pertenço?
### Paraâmetros na requisição com métodos GET e POST
### Testando parâmetros de requisição
### Enviando parâmetros de forma correta
### Qual é o método HTTP?
### Por que POST?
### Para saber mais: Parâmetros na URL
### Para saber mais: Outros métodos HTTP e Web Services
## 07. Serviços na web com REST
### Serviços Web-REST
### Métodos HTTP
### Sobre o HTTP
### Sobre o formato
### O que é REST?
### Solicitando um recurso
### Idenficando um recurso
### O que aprendemos?
### Para sber mais: tipos de dados
### Outros links
## 08. HTTP2 - Por uma web mais eficiente
### HTTP2 - Dados binários, GZIP ativo e TLS
### Motivos por trás do HTTP/2
### A tecnologia HPACK
### Comparações entre versões
### HTTP2 - Cabeçalhos Stateful
### Os cabeçalhos que mantêm estado
### HTTP2- Server Push
### O Server PUsh
### HTTP2 - Multiplexação
### HTTP2 - Resumo
### Considerações finais
