# Tickets

O **tickets** será uma ferramenta para auxiliar no suporte técnico de softwares (SaaS) ou outros serviços.

## Algumas coisas importantes

### Sobre a instalação
Depois de fazer o download do projeto e instalar as dependências que estão no arquivo `requirements.txt`, você vai
precisar migrar os apps um por vez, sugiro fazer na ordem abaixo para evitar conflitos de relacionamento entre os modelos.

`python manage.py makemigrations empresa`\
`python manage.py makemigrations prestadora_servico`\
`python manage.py makemigrations usuario`\
`python manage.py makemigrations ticket`\
`python manage.py makemigrations auditoria`\
`python manage.py makemigrations politica_privacidade`\
`python manage.py migrate`

Tudo instalado e migrado agora é só cadastrar a empresa prestadora dos serviços no modelo `PrestadoraServico` e cadastrar os usuários

> Todos os usuários que serão atendentes/funcionários da prestadora de serviço, receberão `null` no campo `empresa` do modelo `Usuario`.
> 
> Exemplo:
>```
>{
>    "empresa": null
>}
>```
