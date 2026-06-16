# tasks.py - Gerenciador de tarefas simples

tasks = []

def list_tasks():
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⬜"
        print(f"{i}. {status} {task['name']}")

def add_task(name):
    tasks.append({"name": name, "done": False})
    print(f"Tarefa '{name}' adicionada!")

def complete_task(index):
    if index < 1 or index > len(tasks):
        print("Índice inválido.")
        return
    tasks[index - 1]["done"] = True
    print(f"Tarefa '{tasks[index - 1]['name']}' concluída! ✅")

def remove_task(index):
    if index < 1 or index > len(tasks):
        print("Índice inválido.")
        return
    removed = tasks.pop(index - 1)
    print(f"Tarefa '{removed['name']}' removida.")

if __name__ == "__main__":
    add_task("Comprar leite")
    add_task("Estudar Python")
    add_task("Fazer exercícios")
    print("\n--- Lista de tarefas ---")
    list_tasks()
    print("\n--- Completando tarefa 1 ---")
    complete_task(1)
    list_tasks()
    print("\n--- Removendo tarefa 2 ---")
    remove_task(2)
    list_tasks()
