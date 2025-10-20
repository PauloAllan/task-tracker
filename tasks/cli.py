import argparse
from . import __version__
from .storage import read_tasks, write_tasks, next_id
from .models import Task

def cmd_version(args):
    print(f"task-tracker {__version__}")

def cmd_add(args):
    tasks = read_tasks()
    nid = next_id(tasks)
    task = Task(id=nid, title=args.title)
    tasks.append(task.to_dict())
    write_tasks(tasks)
    print(f"Tarefa adicionada: [{task.id}] {task.title}")

def cmd_list(args):
    tasks = read_tasks()
    if not tasks:
        print("Sem tarefas.")
        return
    for t in tasks:
        status = "✔" if t.get("done") else " "
        print(f"[{t['id']}] [{status}] {t['title']}")

def cmd_done(args):
    tasks = read_tasks()
    for t in tasks:
        if t['id'] == args.id:
            t['done'] = True
            write_tasks(tasks)
            print(f"Tarefa [{t['id']}] marcada como concluída.")
            return
    print(f"Tarefa com id {args.id} não encontrada.")

def cmd_remove(args):
    tasks = read_tasks()
    new_tasks = [t for t in tasks if t['id'] != args.id]
    if len(new_tasks) == len(tasks):
        print(f"Tarefa com id {args.id} não encontrada.")
        return
    write_tasks(new_tasks)
    print(f"Tarefa [{args.id}] removida.")

def cmd_edit(args):
    tasks = read_tasks()
    for t in tasks:
        if t['id'] == args.id:
            t['title'] = args.title
            write_tasks(tasks)
            print(f"Tarefa [{t['id']}] editada.")
            return
    print(f"Tarefa com id {args.id} não encontrada.")


def main():
    parser = argparse.ArgumentParser(prog="task-tracker")
    sub = parser.add_subparsers(dest="command")


    parser_version = sub.add_parser("version")
    parser_version.set_defaults(func=cmd_version)

    parser_add = sub.add_parser("add")
    parser_add.add_argument("title")
    parser_add.set_defaults(func=cmd_add)

    parser_list = sub.add_parser("list")
    parser_list.set_defaults(func=cmd_list)

    # Novos subcomandos
    parser_done = sub.add_parser("done")
    parser_done.add_argument("id", type=int)
    parser_done.set_defaults(func=cmd_done)

    parser_remove = sub.add_parser("remove")
    parser_remove.add_argument("id", type=int)
    parser_remove.set_defaults(func=cmd_remove)

    parser_edit = sub.add_parser("edit")
    parser_edit.add_argument("id", type=int)
    parser_edit.add_argument("title")
    parser_edit.set_defaults(func=cmd_edit)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
