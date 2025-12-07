from main import app, database
from comunidade.models import Usuario, Post

# Inicia o contexto da aplicação Flask
# with app.app_context():
#    database.create_all()  # Cria as tabelas no banco de dados
#    print("Tabelas criadas com sucesso no banco de dados.")

# with app.app_context():
#     usuario = Usuario(username='Rodrigo', email='arc@live.com', senha='123456')
#     usuario2 = Usuario(username='Camila', email='arc8@live.com', senha='123456')
#
#     database.session.add(usuario)
#     database.session.add(usuario2)
#
#     database.session.commit()
# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = Usuario.query.first()
#     print(primeiro_usuario.id)
#     print(primeiro_usuario.username)
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.senha)
#     print(primeiro_usuario.foto_perfil)
#     print(primeiro_usuario.posts)
#     print(primeiro_usuario.cursos)
#
#     usuario_teste = Usuario.query.filter_by(id=1).first()
#     print(usuario_teste.email)
#
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo='Horas Vazias', corpo='Livro sobre aproveitar o tempo, viver e ser feliz!')
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#         post = Post.query.first()
#         print(post.titulo)
#         print(post.data_criacao)
#         print(post.id_usuario)
#         print(post.autor.email)

# Deletando o banco de dados atual e criando um novo zerado
with app.app_context():
    database.drop_all()
    database.create_all()