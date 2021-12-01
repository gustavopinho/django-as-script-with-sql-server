import setup
from tasks.models import User, Task


def main():

    QUIT = "Q"
    command = ""
    while command != QUIT:
        print("Escolha uma opção:")
        print("1 - Cadastra cliente.")
        print("2 - Cadastra task.")
        print("3 - Listar tasks de um usuário")
        print("Q - Said")
        command = input("Informe uma opção: ")

        if command == '1':
            user = User()
            user.name = str(input("Informe o nome: "))
            user.save()
        elif command == '2':
            for user in User.objects.all():
                print("{0} - {1}".format(user.id, user.name))

            task = Task()
            task.user = User.objects.get(
                id=input("Informe o ID do usuário: "))
            task.name = input("Informe a descrição da task: ")
            task.save()
        elif command == '3':
            for user in User.objects.all():
                print("{0} - {1}".format(user.id, user.name))
            tasks = Task.objects.filter(
                user_id=input("Informe o ID do usuário: "))
            for task in tasks:
                print("{0} - {1}".format(task.id, task.name))
        else:
            print("Opção não encontrada.")


if __name__ == '__main__':
    main()
