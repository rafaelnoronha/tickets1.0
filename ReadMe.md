# Tickets

O **tickets** será uma ferramenta para auxiliar no suporte técnico de softwares (SaaS) ou outros serviços.

## Algumas coisas importantes

### Sobre a instalação
Depois de fazer o download do projeto e instalar as dependências que estão no arquivo `requirements.txt`, você vai
precisar migrar o app `usuarios`, se não fizer isso você terá um erro
como o descrito abaixo... 

> django.db.utils.ProgrammingError: relation "usuarios_usuario" does not exist

Para escapar desse erro, apenas crie a migração do app `usuarios` antes de tudo, olhe o exemplo abaixo...

`python manage.py makemigrations usuarios`\
`python manage.py makemigrations`\
`python manage.py migrate`
