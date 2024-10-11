- Estrutura
core
    entities
        categoria
        conta
        transacao
        valor
    repositories
        categoria

- Ordem
usuário  # faz a requisição rest via app, insominia, spa, etc
run.py  # coloca a aplicação no ar, escutando as requisições
adapters.primary.rest  # configura os endpoints que receberão as requisições
services.categoria  # uma interface ???
adapters.secondary.sqlite.database  # métodos para interagir com o banco
    adapters.secondary.sqlite.model.categoria  # mapeamento das tabelas do banco
core.entities.categoria  # definição pura do dado e entidades




Aqui ficam as regras de negócio, lógica específica do problema que está sendo resolvido.
É a representação do problema real que o software está tentando resolver.
O código contido aqui, deve ser independente, não devendo ter qualquer detalhe de implementação técnica, como:
    - o banco de dados
    - a interface do usuário
    - a lógica de comunicação com serviços externos
    - etc



A arquitetura hexagonal, também conhecida como arquitetura ports-and-adapters, é um padrão de arquitetura de software que promove a separação de preocupações e a modularidade.

Os adaptadores implementam as interfaces dos ports.


Entrada (Adaptadores Primários)
Recebe dados de CLI / UI / REST / KAFKA / SOAP / etc.
Valida dados (se não tiverem válido, já retorna ao solicitante, pedindo dados corretos).
Converte em objetos de domínio (um formato compreensível para o núcleo da aplicação).

    Interfaces
    Portas permitem que o núcleo se comunique com o mundo exterior sem se preocupar com detalhes de implementação.



Adaptadores Secundários
REST / EMAIL / DATABASE
São responsáveis por adaptar os dados do núcleo da aplicação para o mundo exterior.


Portas permitem que o núcleo se comunique com o mundo exterior sem se preocupar com detalhes de implementação, isso inclue:

- interfaces para comunicar com serviços de persistência (como bancos de dados)
- interfaces para comunicar com serviços externos (como APIs)
- interfaces de UI (para interação com o usuário)

As portas (interfaces) serão implementadas pelos adaptadores (métodos).
As portas (interfaces) são definem o que a aplicação pode fazer, mas não como isso é feito. Elas são agnósticas em relação à implementação técnica (adaptadores / métodos).

