from comunidade import app, database
from comunidade.models import Usuario

# Criar o banco (execute APENAS uma vez)
# with app.app_context():
#     database.create_all()
#     print("Banco criado!")

with app.app_context():
    usuario = Usuario.query.first()
    if usuario:
        print(usuario.username)
        print(usuario.email)
        print(usuario.senha)
    else:
        print("Nenhum usuário encontrado.")

# with app.app_context():
#     usuario = Usuario.query.filter_by(username='TESTE').first()
#     if usuario:
#         print(usuario.username)
#         print(usuario.email)
#         print(usuario.senha)
#     else:
#         print("Nenhum usuário encontrado.")


# with app.app_context():
#     database.drop_all()
#     database.create_all()
