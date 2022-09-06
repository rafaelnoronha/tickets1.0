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

### Regras de Negócio
- [x] Toda operação de **CREATE/UPDATE/DELETE** deve gerar um log, um registro no modelo auditoria
- [ ] A cada tentativa de login falha, é preciso incrementar +1 no número de tentativas falhas de login no modelo de usuário
  - [ ] Caso tenha 3 tentativas falhas de login, é necessário bloquear o usuário
  - [ ] Caso o login seja efetuado, é necessário limpar o número de tentativas falhas
- [x] Não deve haver mais de uma empresa `ativa=True` e `prestadora_servico=True`
- [x] A primeira vez que o ticket for atribuido para um atendente, deve ser preenchido o campo `data_atribuicao`. Caso o tiket seja criado já com o atendente o campo `data_atribuicao` deve vir com a data da criação do ticket
- [x] Não permitir cadastrar um usuário `is_staff=true` com uma empresa `prestadora_servico=false` e vice e versa
- [x] Não permitir vincular um usuário que não possua `is_staff=True` como `atendente` há um ticket e não permitir o contrário no campo `solicitante`
- [ ] Calcular prioridade do ticket com base no `grupo` e `subgrupo`

Guias de orientação à LGPD
https://www.gov.br/governodigital/pt-br/seguranca-e-protecao-de-dados/guias/
