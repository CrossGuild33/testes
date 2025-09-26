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

    def listar_alunos(self):
        return list(self.matriculas.values())        
        


