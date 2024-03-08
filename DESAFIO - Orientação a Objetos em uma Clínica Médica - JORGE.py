class FuncionarioEspecializado():
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def realizarExames(self):
        pass

    def prescreverMedicamentos(self):
        pass

    def aplicarInjecao(self):
        pass

    def agendarConsultas():
        pass

class Atendente(FuncionarioEspecializado):
    def __init__(self, nome, especialidade):
        super().__init__(nome, especialidade)
    
    def agendarConsultas(self):
        print("Consulta agendada por", self.nome)
        print("Cargo:", self.especialidade)
        print("Consulta para o paciente x agendada.")

class Medico(FuncionarioEspecializado):
    def __init__(self, nome, especialidade, crm):
        super().__init__(nome, especialidade)
        self.crm = crm
    
    def prescreverMedicamentos(self):
        print("Remedios para o paciente x prescritos")

class Enfermeiro(FuncionarioEspecializado):
    def __init__(self, nome, especialidade, coren):
        super().__init__(nome, especialidade)
        self.coren = coren

    def realizarExames(self):
        print("Exame do paciente x realizado")

atendente1 = Atendente("Carol", "Atendente")
atendente1.agendarConsultas()