# Site de Comunidade com Flask

Este é um projeto de site de comunidade que estou desenvolvendo usando Flask. A ideia é criar uma plataforma simples onde pessoas possam se conectar, mas por enquanto está na fase inicial com algumas páginas básicas funcionando.

## Sobre o Projeto

Este projeto foi criado para testar e aplicar diferentes conceitos de desenvolvimento web. O site tem uma estrutura bem simples: uma página inicial, uma lista de usuários, página de contato e uma área de login. A ideia é experimentar com Flask, testar integrações com Bootstrap e validar diferentes abordagens de arquitetura web.

## Tecnologias

**Backend:**

- **Flask 3.1.2** - Escolhi o Flask porque é leve, flexível e perfeito para projetos pequenos e médios
- **Flask-SQLAlchemy** - ORM para gerenciamento de banco de dados
- **Flask-WTF** - Integração com WTForms para formulários seguros
- **Flask-Bcrypt** - Criptografia de senhas para segurança dos usuários
- **Python 3.9** - Linguagem principal do projeto
- **Jinja2** - Sistema de templates que vem integrado com o Flask

**Frontend:**

- **Bootstrap 5.0.2** - Para não ter que escrever CSS do zero e garantir que o site fique responsivo
- **HTML5** - Estrutura das páginas

**Desenvolvimento:**

- **Ambiente Virtual** - Para manter as dependências organizadas
- **Werkzeug** - Servidor de desenvolvimento que vem com o Flask

## Estrutura do Código

```
Site com Flask/
├── main.py                 # Arquivo principal - ponto de entrada da aplicação
├── comunidade/             # Blueprint principal da aplicação
│   ├── __init__.py        # Inicialização do Flask app e configurações
│   ├── routes.py          # Rotas da aplicação
│   ├── forms.py           # Formulários com Flask-WTF
│   ├── models.py          # Modelos do banco de dados (SQLAlchemy)
│   ├── templates/         # Templates HTML
│   │   ├── base.html      # Template base com Bootstrap
│   │   ├── navbar.html    # Barra de navegação
│   │   ├── home.html      # Página inicial
│   │   ├── usuarios.html  # Lista de usuários
│   │   ├── contato.html   # Página de contato
│   │   └── login.html     # Tela de login
│   └── testes.py          # Arquivo de testes
└── venv/                  # Ambiente virtual
```

## Como Executar

1. Clone o repositório
2. Ative o ambiente virtual:

   ```bash
   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. Execute o projeto:
   ```bash
   python main.py
   ```
4. Acesse: `http://localhost:5000`

## O que Está Funcionando

- Navegação entre todas as páginas
- Lista de usuários (dados estáticos por enquanto)
- Layout responsivo graças ao Bootstrap
- Estrutura de templates bem organizada
- Navbar com todos os links funcionais
- Sistema de formulários com validação (Flask-WTF)
- Estrutura de blueprint para organização modular
- Modelos de banco de dados preparados (Usuario e Post)
- **Sistema de criação de conta funcional** - Usuários podem criar contas que são salvas no banco de dados
- **Criptografia de senhas** - Senhas são criptografadas usando Flask-Bcrypt antes de serem armazenadas
- **Banco de dados SQLite ativo** - Armazenamento persistente de usuários
- **Validação de formulários** - Validação de email, senha e confirmação de senha

## Objetivos Técnicos

Este projeto serve como um laboratório para testar e validar:

- **Arquitetura MVC** com Flask e templates Jinja2
- **Integração frontend/backend** usando Bootstrap e Flask
- **Estrutura de rotas** e organização de código
- **Responsividade** e experiência do usuário
- **Padrões de desenvolvimento** web modernos

## Próximas Implementações

- Validação de login com verificação de senha criptografada
- Sistema de sessões para manter usuário logado
- Perfil de usuário editável
- Sistema de posts da comunidade
- Melhorias no design
- Mais funcionalidades de comunidade

## Decisões Técnicas

**Por que Flask?**
Flask é perfeito para projetos como este - não vem com muita coisa desnecessária, é altamente customizável e permite crescer conforme a necessidade.

**Por que Bootstrap?**
Economiza tempo no frontend e garante que o site funcione bem em dispositivos móveis sem ter que escrever CSS responsivo manualmente.

**Por que templates separados?**
Facilita a manutenção e permite reutilizar código (como a navbar) em todas as páginas.

## Observações

- O banco de dados SQLite está ativo e sendo utilizado para armazenar usuários
- Senhas são criptografadas usando Flask-Bcrypt antes de serem salvas
- O sistema de criação de conta está totalmente funcional
- O sistema de login está implementado, mas ainda precisa validar a senha criptografada
- Bootstrap está configurado corretamente (CSS no head, JS no final)
- Projeto em desenvolvimento ativo
- Estrutura reorganizada em blueprint para melhor organização e escalabilidade

---

_Desenvolvido para aplicar conhecimentos em Flask e criar uma base sólida para futuras funcionalidades_
