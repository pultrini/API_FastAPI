from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    """
    Teste de 3 Etapatas
    -A: Arrange
    -A: Act
    -A: Assert
    """
    client.get('/')

    response = client.get('/')

    assert response.json() == {'message': 'Olá mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'manada',
            'password': 'password',
            'email': 'test@test.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'manada',
        'email': 'test@test.com',
        'id': 1,
    }
