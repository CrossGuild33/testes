class Aluno:
    def __init__ (self, nome, identidade, cel):
        self.nome = nome
        self.identidade = identidade
        self.cel = cel

    def __str__(self):
        return f"Aluno(nome={self.nome}, identidade={self.identidade}, cel={self.cel})"    

class Academia:
    def __init__(self):
        self.matriculas = {}

def adicionar_matricula(self, aluno):
    if aluno.nome not in self.matriculas:
        self.matriculas[aluno.nome] = aluno
    else:
        print(f'{aluno.nome} já está matriculado')

def verificar_quantidade(self):
    return len(self.matriculas)        

novo_aluno1 = ("Oliveira", "22000111-5", "99999-9999")
novo_aluno2 = ("Silva", "2222222222l", "99998-8888")
    
lista_alunos = novo_aluno1, novo_aluno2

academia = Academia()
adicionar_matricula(lista_alunos)
print(academia.verifica)

