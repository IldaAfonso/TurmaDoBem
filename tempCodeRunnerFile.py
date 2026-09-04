import json

def carregar_dados(arquivo):
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except:
        return []

def salvar_dados(arquivo, dados):
    try:
        with open(arquivo, "w") as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print("Erro ao salvar:", e)

def proximo_id(registros):
    return max((registro.get("id", 0) for registro in registros), default=0) + 1


def cadastrar_profissional():
    try:
        profissionais = carregar_dados("dados/profissionais.json")

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        cidade = input("Cidade: ")
        tipo = input("Tipo (Dentista/Psicólogo/Psiquiatra): ")

        if not all([nome, telefone, cidade, tipo]):
            print("Preencha todos os campos!")
            return

        novo = {
            "id": proximo_id(profissionais),
            "nome": nome,
            "telefone": telefone,
            "cidade": cidade,
            "tipo": tipo
        }

        profissionais.append(novo)
        salvar_dados("dados/profissionais.json", profissionais)

        print("Profissional cadastrado!")

    except Exception as e:
        print("Erro:", e)

def listar_profissionais():
    profissionais = carregar_dados("dados/profissionais.json")

    if not profissionais:
        print("Nenhum cadastrado.")
        return

    for p in profissionais:
        print(p)

def atualizar_profissional():
    try:
        profissionais = carregar_dados("dados/profissionais.json")

        id_busca = int(input("ID: "))

        for p in profissionais:
            if p["id"] == id_busca:
                p["telefone"] = input("Novo telefone: ")
                salvar_dados("dados/profissionais.json", profissionais)
                print("Atualizado!")
                return

        print("Não encontrado.")

    except Exception as e:
        print("Erro:", e)

def deletar_profissional():
    try:
        profissionais = carregar_dados("dados/profissionais.json")
        id_busca = int(input("ID: "))
        nova_lista = [p for p in profissionais if p["id"] != id_busca]

        if len(nova_lista) == len(profissionais):
            print("Não encontrado.")
            return

        salvar_dados("dados/profissionais.json", nova_lista)
        print("Removido!")
    except Exception as e:
        print("Erro:", e)     

def menu():
    while True:
        print("\n=== SISTEMA TURMA DO BEM ===")
        print("1. Cadastrar profissional")
        print("2. Listar profissionais")
        print("3. Atualizar profissional")
        print("4. Deletar profissional")
        print("5. Cadastrar beneficiário")
        print("6. Listar beneficiários")
        print("0. Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_profissional()
        elif op == "2":
            listar_profissionais()
        elif op == "3":
            atualizar_profissional()
        elif op == "4":
            deletar_profissional()
        elif op == "5":
            cadastrar_beneficiario()
        elif op == "6":
            listar_beneficiarios()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

def cadastrar_beneficiario():
    try:
        beneficiarios = carregar_dados("dados/beneficiarios.json")

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        cidade = input("Cidade: ")
        necessidade = input("Descreva sua necessidade: ")

        if not all([nome, telefone, cidade, necessidade]):
            print("Todos os campos são obrigatórios!")
            return

        prioridade, profissional_indicado = realizar_triagem(necessidade)

        profissional_encontrado = buscar_profissional_disponivel(
        cidade,
        profissional_indicado
        )
        if profissional_encontrado:
            encaminhamento = profissional_encontrado["nome"]
        else:
            encaminhamento = "Nenhum profissional disponível"
        novo = {
            "id": proximo_id(beneficiarios),
            "nome": nome,
            "telefone": telefone,
            "cidade": cidade,
            "necessidade": necessidade,
            "prioridade": prioridade,
            "profissional_indicado": profissional_indicado,
            "encaminhamento": encaminhamento
        }

        beneficiarios.append(novo)

        salvar_dados("dados/beneficiarios.json", beneficiarios)

        print("\nBeneficiário cadastrado com sucesso!")
        print(f"Prioridade: {prioridade}")
        print(f"Profissional indicado: {profissional_indicado}")

    except Exception as e:
        print("Erro:", e)        
def realizar_triagem(necessidade):

    necessidade = necessidade.lower()

    # DENTISTA
    if "dente" in necessidade or "dor de dente" in necessidade:
        return "Alta", "Dentista"

    # PSICÓLOGO
    elif "ansiedade" in necessidade or "tristeza" in necessidade:
        return "Média", "Psicólogo"

    # PSIQUIATRA
    elif "depressão" in necessidade or "crise" in necessidade:
        return "Urgente", "Psiquiatra"

    # CASOS NÃO IDENTIFICADOS
    else:
        return "Em análise", "Equipe Administrativa"        

def listar_beneficiarios():

    beneficiarios = carregar_dados("dados/beneficiarios.json")

    if not beneficiarios:
        print("Nenhum beneficiário cadastrado.")
        return

    print("\n=== BENEFICIÁRIOS ===")

    for b in beneficiarios:
        print(f"""
                ID: {b['id']}
                    Nome: {b['nome']}
                    Cidade: {b['cidade']}
                    Necessidade: {b['necessidade']}
                    Prioridade: {b['prioridade']}
                    Profissional indicado: {b['profissional_indicado']}
                    Encaminhamento: {b['encaminhamento']}
                    -----------------------------
                    """)    
def buscar_profissional_disponivel(cidade, tipo_profissional):

    profissionais = carregar_dados("dados/profissionais.json")

    for profissional in profissionais:

        if (
            profissional["cidade"].lower() == cidade.lower()
            and profissional["tipo"].lower() == tipo_profissional.lower()
        ):
            return profissional

    return None     

if __name__ == "__main__":
    menu()