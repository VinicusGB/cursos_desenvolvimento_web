# Curso de NGINX servidor Web, Proxy Reverso e API Gateway - 6h
**Professor:** Vinicius Dias

**Disponível:** [ALURA]('https://cursos.alura.com.br/course/nginx-servidor-web-proxy-reverso-api-gateway')

**Conteúdo:**Entenda qual o papel do NGINX e suas características
- Aprenda a configurar um servidor HTTP com NGINX
- Conheça o conceito de Proxy Reverso
- Configure um API Gateway
- Aprenda a configurar um Load Balancer

## 1. Conhecendo a ferramenta
### Apresentação

Introdução e explanção sobre o curso.

### Prazer, NGINX

O NGINX pode ser usado como servidor web, proxy reverso, API Gateway e Load Balancer.
- **SERVIDOR WEB:** é um servidor que recebe requisições e as _serve com arquivos estáticos, como HTML, CSS e JavaScript_;
- **PROXY REVERSO:** é um servidor que recebe requisições e as _repassa para outros servidores_.
- **API GATEWAY:** é um servidor que recebe requisições e as repassa para outros servidores, mas que _também pode fazer transformações nessas requisições_.
- **LOAD BALANCER:** é um servidor que recebe requisições e as repassa para outros servidores, mas que _também pode distribuir as requisições entre os servidores de forma inteligente_.

#### NGINX vx Apache
- O NGINX é mais leve, mais rápido e mais fácil de configurar que o Apache.
- O NGINX é mais usado em servidores com poucos recursos e de baixa prioridade.
- O Apache é mais usado que o NGINX, por isso é mais usado em servidores que precisam de alta performance.

### Exercício: Papel do servidor
Aprendemos algumas coisas neste vídeo. O que é um servidor web, como o nginx funciona, etc.

Mas na prática, via de regra, qual o papel de um servidor web?

a) Ouvir conexões udp em alguma porta configurada
- _Alternativa errada! Conexões feitas na web via de regra usam o protocolo de transporte TCP e não UDP._

b) **Alternativa correta:** Ouvir conexões tcp em alguma porta configurada
- _Alternativa correta! Um servidor web vai ficar esperando uma conexão chegar. Quando ela chegar, o servidor web faz seu trabalho, garantindo que a mensagem recebida está no formato HTTP e depois fazendo o que deve fazer segundo suas configurações._

c) Ouvir conexões tcp na porta 80
- _Alternativa errada! Nem só de porta 80 vive a web. A porta pode ser configurada._

### Instalação

[NGINX](https://nginx.org/en/download.html)

#### Windows
- [NGINX for Windows](http://nginx.org/en/docs/windows.html)
- [NGINX for Windows - Download](http://nginx.org/en/download.html) 
#### Linux
- [NGINX for Linux](http://nginx.org/en/linux_packages.html)
- [NGINX for Linux - Download](http://nginx.org/en/download.html)
#### Mac
- [NGINX for Mac](http://nginx.org/en/docs/osx_packages.html)
- [NGINX for Mac - Download](http://nginx.org/en/download.html)


### Exercicio: Localhost

Vimos no final do vídeo que ao acessar o endereço http://localhost nós vemos a página HTML configurada pelo nginx por padrão.

Mas como o nginx e o computador sabem o que significa "localhost"?

a) Através de uma configuração inacessível do sistema operacional

b) **Alternativa correta:** Através do arquivo de hosts
- _Alternativa correta! Todo sistema operacional possui um arquivo de hosts. No Linux, por padrão fica em /etc/hosts. No Mac, /private/etc/hosts. Já no Windows, C:\Windows\System32\Drivers\Etc\hosts. Esse arquivo informa ao sistema operacional que quando uma conexão for estabelecida usando algum nome, o IP correspondente deve ser usado. Para o nome localhost, temos o IP da nossa própria máquina (127.0.0.1)._

c) Através de um servidor padrão que o nginx cria chamado localhost

### O que aprendemos?

Nesta aula, aprendemos:

- Aprendemos o que é Nginx
- Vimos o propósito de um servidor web
- Aprendemos a instalar o Nginx
- Entendemos como o Nginx funciona

## 2. Servidor HTTP
### Arquivos de configuração

Acesse conf/nginx.conf:

    worker_processes  1;
    events {
        worker_connections  1024;
    }
    http {
        server {
            listen       8080;
            server_name  localhost;
            location / {
                root   html;
                index  index.html index.htm;
            }
        }
    }

### Exercicio: Caminhos dos arquivos

Vimos neste vídeo que há mais de um local onde vamos configurar arquivos do nginx.

Como saber onde está o arquivo de configuração principal?

a) Gravando o caminho em cada sistema operacional

b) Através do comando nginx -t

c) **Alternativa correta:** Através do utilitário da CLI nginx
- _Alternativa correta! Este comando nos fornece diversas informações. Ao digitarmos nginx -h uma ajuda é exibida, e lá podemos ver o caminho do arquivo de configuração._

### Criando um servidor

1. Crie um arquivo server/default.conf:
    
            server {
                listen       8080;
                server_name  localhost;
                location / {
                    root   html;
                    index  index.html index.htm;
                }
            }

### Entendendo a location

Finalmente configuramos um servidor web nosso, usando a diretiva server e dentro dela temos a diretiva chamada location.

Qual o propósito dessa diretiva location na configuração de um servidor web no nginx?

a) **Alternativa correta:** Informar qual caminho acessado cairá nas regras a seguir
- _Alternativa correta! Se definirmos um location /, tudo que começar com / (que no caso é literalmente tudo) cairá nesse conjunto de regras. Nessas regras podemos definir qual o diretório raiz do projeto, qual o arquivo padrão, regras de redirecionamento, etc._

b) Informar o caminho raiz do nosso site / sistema

c) Informar o arquivo padrão a ser carregado em nosso site / sistema

### [Sinais e comandos](https://www.nginx.com/resources/wiki/start/topics/tutorials/commandline/)

> nginx -s [signal]
  - stop — desliga o servidor
  - quit — desliga o servidor de forma mais suave
  - reload — recarrega a configuração do servidor
  - reopen — reabre os arquivos de log do servidor

> nginx -t — testa a configuração e exibe o resultado

> nginx -v — exibe a versão do nginx

> nginx -V — exibe a versão do nginx, opções de configuração e módulos compilados

### Páginas de erro

Em nosso arquivo de configuração, `nginx.conf`, temos a diretiva error_page. Ela é usada para definir qual página será exibida quando um erro ocorrer.

        error_page  404              /404.html;


### Exercicio: Valores válidos

Aprendemos a configurar páginas de erro neste vídeo através da diretiva error_page, informando códigos e um caminho.

Qual das alternativas a seguir é FALSA sobre configurações de páginas de erro no nginx?

a) Podemos redirecionar diversos erros HTTP para o mesmo caminho
- _Alternativa errada! Essa afirmação é verdadeira. Tanto é que fizemos isso na aula._

b) Precisamos informar pelo menos um código HTTP para definir a página de erro
- _Alternativa errada! Essa afirmação é verdadeira. Tanto é que fizemos isso na aula._

c) **Alternativa correta:** Precisamos definir o caminho de um arquivo existente
- _Alternativa correta! Essa afirmação é falsa pois no caminho informado ao error_page nós podemos ter um valor que corresponde a alguma diretiva location._

### O que aprendemos?

Nesta aula, aprendemos:

- Conhecemos o formato de configuração do nginx
- Configuramos nosso primeiro servidor web
- Aprendemos a lidar com a CLI do nginx
- Vimos como configurar páginas de erro

## 3. Proxy reverso
### O que é?

Um Proxy reverso é um servidor que recebe requisições e as repassa para um ou mais servidores. Ele é usado para balancear a carga de requisições entre os servidores, ou para fornecer uma interface de acesso a um conjunto de servidores.

### Exercício: Nomenclatura

Entendemos neste vídeo a ideia por trás desse nome que pode ser assustador: Proxy Reverso.

Por que o nome é Proxy REVERSO e não apenas Proxy?

a) Porque o conceito é o oposto do que um proxy faz
- _Alternativa errada! Um proxy reverso faz exatamente o que um proxy faz, mas na outra ponta da conexão._

b) **Alternativa correta:** Porque normalmente um proxy fica no lado do cliente
- _Alternativa correta! O conceito padrão de proxy é algo que fica no lado do cliente interceptando os pacotes de rede. Como nesse caso o proxy está no lado do servidor, chamamos de proxy reverso._

c) Porque podemos encaminhar requisições de forma reversa
- _Alternativa errada! Essa afirmação nem faz muito sentido para ser sincero._

### Configurando

Em `nginx.conf`:

    server {
        listen       8080;
        server_name  localhost;
        location / {
            proxy_pass http://localhost:3000;
        }
    }

### Servidor 2 em 1

Em `nginx.conf`:

    server {
        listen       8080;
        server_name  localhost;
        location / {
            proxy_pass http://localhost:3000;
        }
        location /api {
            proxy_pass http://localhost:3001;
        }
    }

### Exercício: Necessidade real

Neste vídeo nós fizemos a aplicação mais comum de um proxy reverso. Fazer com que algumas requisições sejam enviadas para um servidor de aplicação.

Por que realizar um proxy reverso e não apenas deixar o servidor de aplicação lidar com todas as requisições?

a) **Alternativa correta:** Com nginx na frente podemos responder arquivos estáticos muito mais rapidamente.
- _Alternativa correta! Esse é um dos principais motivos. O nginx é um servidor incrivelmente performático, então nós ganhamos muito ao não enviar todas as requisições para o servidor de aplicação. O nginx pode enviar diretamente os arquivos estáticos sem processar nada, além de poder definir cache, compressão, etc._

b) Com nginx na frente nosso servidor de aplicação pode ficar offline às vezes sem problemas.

c) Não há nenhum motivo real para realizar esta tarefa.

### O que aprendemos?

Nesta aula, aprendemos:

- Conhecemos o conceito de proxy reverso
- Configuramos um proxy reverso na prática
- Vimos quando se faz necessário um proxy reverso

## 4. API Gateway
### Múltiplos serviços

Microserviços são uma forma de arquitetura de software que divide uma aplicação em serviços menores e independentes. Cada serviço é executado em seu próprio processo e se comunica com mecanismos leves, normalmente uma API HTTP.

### Para saber mais: Microsserviços

O propósito deste treinamento não é ensinar o conceito ou práticas da arquitetura orientada a microsserviços, mas caso você queira conhecer este conceito, pode conferir este treinamento: https://cursos.alura.com.br/course/microsservicos-padroes-projeto

### Usando proxy_pass

Em `nginx.conf`:

    server {
        listen       8080;
        server_name  localhost;
        location / {
            proxy_pass http://localhost:3000;
        }
        location /api {
            proxy_pass http://localhost:3001;
        }
        location /auth {
            proxy_pass http://localhost:3002;
        }
    }

    server {
        listen       8081;
        server_name  localhost;
        location / {
            proxy_pass http://localhost:3003;
        }
    }

    server {
        listen       8082;
        server_name  localhost;
        location / {
            proxy_pass http://localhost:3004;
        }
    }

### Exercício: Propósito

Aprendemos neste vídeo como ter um servidor web que faz o redirecionamento para outros múltiplos servidores baseado na URL recebida.

Antes de assistir o próximo vídeo, por que você acredita que essa prática pode ser útil?

a) **Alternativa correta:** Para centralizar o acesso a múltiplos serviços em um único host
- _Alternativa correta! Dessa forma todas as requisições podem ser feitas para o mesmo servidor, facilitando a vida do cliente, dentre outras vantagens._

b) Para aumentar a performance de cada servidor

c) Não há motivo real para aplicar esta técnica

### Entendendo o conceito

#### Vantagens de um API Gateway
- Centralização de acesso
- Segurança
- Performance
- Monitoramento

#### Desvantagens de um API Gateway
- Ponto único de falha
- Complexidade
- Performance

#### Componentes de um API Gateway
- Roteamento
- Autenticação
- Monitoramento
- Cache
- Balanceamento de carga
- Logs
- Transformação de dados

### Para saber mais: API Gateway

Agora que conhecemos o conceito de um API Gateway, temos uma base melhor para esse artigo fenomenal do próprio Nginx:

[Deploying NGINX as an API Gateway, Part 1](https://www.nginx.com/blog/deploying-nginx-plus-as-an-api-gateway-part-1/)

Vale a pena a leitura.

### O que aprendemos?

Nesta aula, aprendemos:

- Entendemos o conceito de microsserviços
- Usamos proxy reverso para rotear requisições
- Aprendemos o conceito de API Gateway

## 5. Load Balancer
### Upstreams

Em `nginx.conf`:

    upstream backend {
        server localhost:3000;
        server localhost:3001;
        server localhost:3002;
    }

    server {
        listen       8080;
        server_name  localhost;
        location / {
            proxy_pass http://backend;
        }
    }

### Exercício: Significado

Conseguimos neste vídeo de forma muito simples configurar um load balancer usando a diretiva upstream.

O que significa na prática upstream nas configurações do nginx?

a) Lista de todos os servidores funcionais em nossa máquina

b) **Alternativa correta:** Um grupo de servidores
- _Alternativa correta! Através do nome definido em upstream, podemos acessar algum dos servidores deste grupo dependendo de algumas regras definidas._

c ) Um nome para um load balancer

### Configuração de logs

Em `nginx.conf`:

    http {
        log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';

        access_log /var/log/nginx/access.log main;
        error_log /var/log/nginx/error.log;
    }

### Formato de logs

Trazer apenas as informações importantes para o log é uma boa prática. Além de facilitar a leitura, também ajuda a economizar espaço em disco.

Em `nginx.conf`:

    http {
        log_format main 'Remote Addr: $remote_addr,
                         Time: [$time_local], 
                         Request:  "$request",
                         Status: $status';

        access_log /var/log/nginx/access.log main;
        error_log /var/log/nginx/error.log;
    }

### Adicionando informações

 Mas quando utilizamos load balancer, precisamos de mais informações para entender o que está acontecendo. Pois o ip que aparece no log é o do load balancer e não o do cliente.

Em `nginx.conf`:

    server {
        listen       8080;
        server_name  localhost;
        location / {
            proxy_pass http://backend;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }

    http {
        log_format main 'Remote Addr: $http_x_real_ip,
                         Time: [$time_local], 
                         Request:  "$request",
                         Status: $status,';

        access_log /var/log/nginx/access.log main;
        error_log /var/log/nginx/error.log;
    }

### Problema

Neste capítulo, após configurarmos um load balancer, fizemos algumas configurações nos logs para evitar um problema no ambiente de produção.

Que problema nós evitamos neste capítulo?

a) Não havia problema. Apenas mudamos o formato de logs

b) **Alternativa correta:** IPs incorretos nos logs de acesso dos servidores
- _Alternativa correta! Da forma como estava no primeiro vídeo, os servidores sempre realizariam o log como se o cliente fosse nosso load balancer, sem conseguirmos rastrear o IP do cliente real._

c) Informações demais nos logs de acesso

### O que aprendemos?

Nesta aula, aprendemos:

- Conhecemos o conceito de load balancer
- Aprendemos a configurar upstreams
- Vimos como funcionam os logs
- Aprendemos a enviar cabeçalhos no proxy reverso
- Colocamos informações personalizadas nos logs

### Conclusão

Aprendemos neste curso como configurar o nginx para servir arquivos estáticos, como configurar um proxy reverso, como configurar um load balancer e como configurar logs.
