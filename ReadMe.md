# Tickets

O **tickets** será uma ferramenta para auxiliar no suporte técnico de softwares (SaaS) ou outros serviços.

## Algumas coisas importantes

### Sobre a instalação
Depois de fazer o download do projeto e instalar as dependências que estão no arquivo `requirements.txt`, você vai
precisar migrar os apps um por vez.

`python manage.py makemigrations empresa`\
`python manage.py makemigrations usuario`\
`python manage.py makemigrations ticket`\
`python manage.py makemigrations auditoria`\
`python manage.py makemigrations politica_privacidade`\
`python manage.py migrate`

### Primeiros passos
Tudo instalado e migrado agora é só cadastrar a empresa prestadora dos serviços no modelo `Empresa`
e depois cadastrar o super usuário

#### Cadastrando a Prestadora de Serviços
Acesse o shell...
```
python manage.py shell
```
Importe o modelo de ```Empresa```...
```
from empresa.models import Empresa
```
Agora copie o script abaixo substituindo os dados pelos dados da empresa que prestará os serviços...

*Obs: o único campo opcional é o ```complemento```*

```
prestadora_servico = Empresa()
prestadora_servico.cpf_cnpj = '00000000000000'
prestadora_servico.razao_social = 'Nome da Empresa'
prestadora_servico.nome_fantasia = 'Nome Fantasia Da Empresa'
prestadora_servico.logradouro = 'Rua Direita'
prestadora_servico.numero = '1995'
prestadora_servico.complemento = 'Sala 2102'
prestadora_servico.bairro = 'Centro'
prestadora_servico.municipio = 'Santa Luzia'
prestadora_servico.uf = 'MG'
prestadora_servico.cep = '12345678'
prestadora_servico.pais = 'Brasil'
prestadora_servico.telefone = '3100000000'
prestadora_servico.prestadora_servico = true
prestadora_servico.save()
```
Saia do shell...
```exit()```