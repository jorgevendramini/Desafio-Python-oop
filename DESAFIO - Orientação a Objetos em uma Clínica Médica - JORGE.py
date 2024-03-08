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
        print("Médico da Consulta", self.nome)
        print("Especialidade:", self.especialidade)
        print("CRM:", self.crm)
        print("Remedios para o paciente x prescritos")

class Enfermeiro(FuncionarioEspecializado):
    def __init__(self, nome, especialidade, coren):
        super().__init__(nome, especialidade)
        self.coren = coren

    def realizarExames(self):
        print("Funcionário:", self.nome)
        print("Cargo:", self.especialidade)
        print("coren:", self.coren)
        print("Exame do paciente x realizado")

atendente1 = Atendente("Carol", "Atendente")
atendente1.agendarConsultas()

medico1 = Medico("Jorge", "Cardiologista", "54556-2")
medico1.prescreverMedicamentos()

enfermeiro1 = Enfermeiro("Ana", "Enfermeira", "5558643")
enfermeiro1.realizarExames()
