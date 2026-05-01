import os
from typing import Callable, Self



class CRUD:

    db: dict[int, dict[str, str]]

    def __init__(self) -> None:
        self.db = {}
    

    def create_task(self, id:int,  task: dict[str, str] ) -> int:    
        if id in self.db :
            return 1

        self.db[id] = task
        return 0


    def get_all_tesks(self) -> list[tuple[int, dict[str, str]]]:
        return list(self.db.items())
        
    
    def get_task_by_id(self, id: int) -> dict[str, str] | None:
        return self.db.get(id)
                

    def update_task(self, id: int, new_task: dict[str,str|None] ) -> int:

        if id in self.db: 
            task:set[tuple[str, str]] = set((key, value) for key, value in new_task.items() if value is not None )

            self.db[id].update(task)
            return 0
        
        return 1
 

    def delete_task(self, id: int ) -> int:
        if id not in self.db:
            return 1
        
        confirm = Input_handler.required_input("certeza? [S|n]: ", str).lower()

        if confirm != "s":
            print("ATENCAO: operação cancelada")
            input()
            return 1

        del self.db[id]
        return 0

class Input_handler():


    @staticmethod
    def required_input[T](mensage: str, tipo:Callable[[str], T]  , err_mens: str|None = None) -> T:
        while True:
            try:
                inp = tipo(input(mensage))

                if isinstance(inp, str) and (not inp or inp.isspace()):
                    raise ValueError 

                return inp
            except ValueError:

                if err_mens is None:
                    err_mens = "tente novamente"
                print("** Erro de entrada: ", err_mens, "\n")
    
    @staticmethod
    def optional_input[T](mensage: str, tipo: Callable[[str], T]) -> T | None:
        
        try:
            inp = tipo(input(mensage))

            if isinstance(inp, str) and (not inp or inp.isspace()):
                raise ValueError 

            return inp
        except ValueError:
            return None

    



class ui_handler:

    @staticmethod
    def print_update(old_task: dict[str, str], new_task: dict[str, str | None]) -> None:

            
        old_width:int = 0
        new_width: int = 0
        key_width: int = 0

        for key in old_task:
            key_width = max(len(key), key_width)
            old_width = max(len(old_task[key]), old_width)
            new_width = max(len(new_task[key] or "" ), new_width)


        print(f"{'CAMPO':<{key_width}} {'ATUAL':<{old_width}} {'NOVO':<{new_width}}")
        print("-" * 52)

        for key in old_task:
            old = old_task[key]
            new = new_task.get(key)

            if new is None:
                new_str = "(manter)"
            elif not new:
                new_str = "..."
            else:
                new_str = new

            print(f"{key:<{key_width}} {old:<{old_width}} {new_str:<{new_width}}")

    @staticmethod
    def print_task( task: dict[str, str]) -> None:
        task_width: int = 0
        key_width: int = 0

        for key in task:
            key_width = max(len(key), key_width)
            task_width = max(len(task[key] or "" ), task_width)
        
        print(f"{'CAMPO':<{key_width}} {'VALOR':<{task_width}}")
        print("-" * 42)

        for key, value in task.items():
            valor = value if value else "..."
            print(f"{key:<{key_width}} {valor:<{task_width}}")

    @staticmethod
    def print_all_tesks(tesks: list[tuple[int, dict[str,str]]]):
        title_width: int = 0
        desc_width: int = 0
        status_width: int = 0

        for id,task in tesks:
            title_width = max(max(len(task["title"]), len("TITLE")), title_width)
            desc_width = max(max(len(task["description"]), len("DESCRIPTION")), desc_width)
            status_width = max(max(len(task["status"]) , len("STATUS")), status_width)

        print(f"{'ID':<5} | {'TITLE':<{title_width}} | {'DESCRIPTION':<{desc_width}} | {'STATUS':<{status_width}}")
        print("-" * 55)


        for task_id, task in tesks:
            print(
                f"{task_id:<5} | "
                f"{task['title']:<{title_width}} | "
                f"{task['description']:<{desc_width}} | "
                f"{task['status']:<{status_width}} | " 
            )



class Task_gen:
    id:int = 0
    
    def get_new_id(self) -> int:
        i = self.id
        self.id += 1
        return i
    
    
    def input_id(self):
        return Input_handler.required_input(
            "digite o id da task: ",int
            )

    def optional_input_status(self) -> str | None:
        opc: dict[int, str] = {
            1: "To Do",
            2: "in progress",
            3: "Completed"
        }

        print("escolha um estado da task: ")
        for key, value in opc.items():
            print(f'[{key}] - {value}')

        while True:
            state:int | None = Input_handler.optional_input("[1-3] ou deixe em branco: ", int)


            if state == None:
                return None
            
            if state in opc:
                return opc[state]
            
            print("opcao invalida ensira novamente\n")

    def required_input_status(self) -> str:

        opc: dict[int, str] = {
            1: "To Do",
            2: "in progress",
            3: "Completed"
        }

        print("escolha um estado da task: ")
        for key, value in opc.items():
            print(f'[{key}] - {value}')

        while True:
            state:int = Input_handler.required_input("[1-3]: ", int)
            
            if state in opc:
                return opc[state]
            
            print("opcao invalida ensira novamente\n")

    
    

    def input_create_task(self) -> dict[str, str]:
        task: dict[str, str] = {
            "title": "",
            "description": "",
            "status": ""
        }

        ui_handler.print_task(task)

        task["title"] = Input_handler.required_input("digite o titulo da tesk: ", str)
        clear()
        ui_handler.print_task(task)

        task["description"] = Input_handler.required_input("digite a descricao da task: ", str)
        clear()
        ui_handler.print_task(task)

        task["status"] = self.required_input_status()
        clear()
        ui_handler.print_task(task)

        input()

        return task
    
    def input_update_task(self, old_task) -> dict[str, str | None]:
        
        task: dict[str, str | None] = {
            "title": "",
            "description": "",
            "status": ""
        }

        clear()
        ui_handler.print_update(old_task, task)

        task["title"] = Input_handler.optional_input("digite o titulo da tesk ou deixe em branco: ", str)
        clear()
        ui_handler.print_update(old_task, task)

        task["description"] = Input_handler.optional_input("digite a descricao da task ou deixe em branco: ", str)
        clear()
        ui_handler.print_update(old_task, task)

        task["status"] = self.optional_input_status()
        clear()
        ui_handler.print_update(old_task, task)

        input()

        return task


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class Main():
    
    def __init__(self) -> None:
        self.task_gen = Task_gen()
        self.crud = CRUD()

    def menu(self) -> int:
        print("-" * 50)
        print("[1] - criar")
        print("[2] - listar")
        print("[3] - atualizar")
        print("[4] - deletar")
        print("[0] - sair")
        return Input_handler.required_input("escolha uma opcao [0-4]: ", int)
            
    def task_create(self) -> None:
        task = self.task_gen.input_create_task()
        id:int = self.task_gen.get_new_id()
        if self.crud.create_task(id, task):
            print("ERRO: não foi possivel criar esse item")

    def task_list(self) -> None:
        ui_handler.print_all_tesks(self.crud.get_all_tesks())
        input()
    
    def task_update(self) -> None:
        id = self.task_gen.input_id()
        task = self.crud.get_task_by_id(id)

        if task != None:
            updated_task = self.task_gen.input_update_task(task.copy())
            if self.crud.update_task( id , updated_task) == 1:
                print("ERRO: não foi possivel atualizar esse item")
        else:
            print("ERRO: não foi possivel encontrar esse item")

    def task_delete(self) -> None:
        id = self.task_gen.input_id()
        if self.crud.delete_task(id) == 1:
            print("ERRO: não foi possivel deletar esse item")

    def main(self):
        funcs = {
            1: self.task_create,
            2: self.task_list,
            3: self.task_update,
            4: self.task_delete,
            0: exit
        }

        while True:
            opc = self.menu()
            clear()

            if opc in funcs:
                funcs[opc]()
        


if __name__ == '__main__':
    clear()
    try: 
        Main().main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nsaindo...")
        exit()
    