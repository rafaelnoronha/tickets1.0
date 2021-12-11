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