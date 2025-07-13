from fastapi.testclient import TestClient

from semana_da_fisica.app import app


def test_root_deve_retornar_ola_mundo():
    '''
    Teste de 3 Etapatas
    -A: Arrange
    -A: Act
    -A: Assert
    '''
    client = TestClient(app)
    client.get('/')

    response = client.get('/')

    assert response.json() == {'message': 'Olá mundo!'}
