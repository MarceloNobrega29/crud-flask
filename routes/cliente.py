from flask import Blueprint

cliente_route = Blueprint('cliente', __name__)

""""
Rota de clientes 
    - /Clientes/ (GET) - Listar clientes 
    - /Clientes/ (POST) - inserir o cliente no servidor
    - /Clientes/new (GET) - Renderizar o formulario para criar um cliente
    - /Clientes/<id> (GET) - obter dados de um cliente
    - /Clinetes/<id>/edit (GET) - renderizar um formulario para editar um cliente
    - /Clientes/<id>/update (PUT) - atualizar os dados do cliente 
    - /Clientes/<id>/delete (DELETE) - deleta o registro do usuario


"""
@cliente_route.route('/')
def lista_clientes():
    """ listar os clientes """
    return {'pagina':"lista_clientes"}

@cliente_route.route('/', methods=['POST'])
def inserir_clientes():
    """ inserir os dados do cliente"""
    pass

@cliente_route.route('/new')
def form_clientes():
    """ formulario para cadastrar um cliente """
    pass

@cliente_route.route('/<int:cliente_id>')
def detalhe_clientes(cliente_id):
    """ exibir detalhe do cliente """
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_clientes(cliente_id):
    """ formulario para editar um cliente """
    pass

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_clientes(cliente_id):
    """ atualizar informações do cliente """
    pass

@cliente_route.route('/<int:cliente_id>/delete',methods=['DELETE'])
def deletar_clientes(cliente_id):
    """ deletar informacoes cliente """
    pass