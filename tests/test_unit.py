from database_manager import Aluno, Academia
import pytest

@pytest.fixture
def academia():
    return Academia()

@pytest.fixture
def aluno1():
    return Aluno("Oliveira", "22000111-5", "99999-9999")

@pytest.fixture
def aluno2():
    return Aluno("Silva", "22888123-5", "77777-7777")

def test_adicionar_aluno(academia, aluno1):
    academia.adicionar_matricula(aluno1)
    assert academia.verificar_quantidade() == 1