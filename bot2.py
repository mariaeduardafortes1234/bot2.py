def exibir_menu():
  print("\n" "+" "="* 50)
  print("Assistente Virtual - Tec Info RDS")
  print("=" * 50)
  print("Digite sua dúvida ou escolha uma opção: ")
  print("📃 'Menu' - Ver tópicos disponíveis")
  print("❓ 'Ajuda' - Como usar o assistente")
  print("🚪 'Sair' - Encerrar o atendimento\n")

def listar_topicos():
    print("📃 Tópicos disponíveis")
    print("✔️ Variáveis e tipos de dados")
    print("✔️ Estruturas condicionais (if/else)")
    print("✔️ Laços e repetição (for/while)")
    print("✔️ Listas e manipulação")
    print("✔️ Funções")
    print("✔️ Importar bibliotecas\n")

def buscar_respostas(pergunta):
    Respostas ={
        "Variável": {
            "texto": "Variáveis armazenam informações em Python, basta atribuir um valor:",
             "exemplo": "nome= 'João' \nidade = 17\naltura = 1.75"
        },
        "if":{
            "texto": "...",
            "exemplo": "..."
        }
    }