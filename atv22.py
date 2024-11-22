class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        self.contatos.append({"nome": nome, "telefone": telefone})

    def listar_contatos(self):
        for contato in self.contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")

agenda = Agenda()
agenda.adicionar_contato("Ana", "12345678")
agenda.adicionar_contato("João", "87654321")
agenda.listar_contatos()