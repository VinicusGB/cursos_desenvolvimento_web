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
### Certificado digital
### Características do HTTPS
### Autoridade certificadora
### Para saber mais: As chaves do HTTPS
## 03. Endereços sob seu domínio
### Endereços
### O que é um domínio na internet?
### Como funciona o DNS?
### Portas
### Porta padrão HTTP
### Recursos
### Identificando o protocolo
### Recursos na URL
### Para saber mais: URI ou URL?
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
