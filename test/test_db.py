from sqlalchemy import select

from semana_da_fisica.models import User


def test_create_user(session):
    user = User(username='davi', email='davi@mail.com', password='pass2ord')
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'davi@mail.com'))

    assert result.username == 'davi'
