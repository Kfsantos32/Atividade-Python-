class Seriesflix:
    def __init__(self):
        self.catalog = {
            'Filmes': ['Velozes e Furiosos 10', 'Avatar 2', 'Gato de Botas 2', 'Batman' , 'Aquaman 2' ],
            'Séries': ['Friends', 'The Last of Us ', 'O Incrível Mundo de Gumball', 'Brickleberry', 'Uma Família da Pesada']
        }

    def show_catalog(self):
        print("Catálogo Seriesflix:")
        for category, titles in self.catalog.items():
            print(f"\n{category}:")
            for title in titles:
                print(title)

    def play_video(self, video):
        print(f"Reproduzindo: {video}")


def main():
    system = Seriesflix()
    while True:
        print("\nBem-vindo ao Sistema de Filmes e Séries !")
        print("Escolha uma opção:")
        print("1. Visualizar Catálogo")
        print("2. Sair")
        option = input("Opção: ")

        if option == '1':
            system.show_catalog()
            category = input("\nEscolha uma categoria (Filmes/Séries): ")
            if category in system.catalog.keys():
                title = input("Escolha um título: ")
                if title in system.catalog[category]:
                    print("\nIniciando reprodução...")
                    system.play_video(title)
                else:
                    print("Título não encontrado.")
            else:
                print("Categoria não encontrada.")
        elif option == '2':
            print("Saindo do Sistema Serieflix ...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()


# Para funcionamento do app o usuario devera escolher a opção na qual deseja (filme/série) é em seguida selecionar o nome do filme ou série desejado #