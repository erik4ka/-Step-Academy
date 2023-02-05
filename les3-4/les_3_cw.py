class Student:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.group = None

    def msg_to_group(self, text: str):
        if self.group:
            self.group.msg(text, self)


class Group:
    def __init__(self, name: str):
        self.name = name
        self.members = []

    def add(self, student: Student):
        # Добавить добавление студента в группу и добавление группы в студента
        pass

    def remove(self, id: int):
        # Добавить удаление студента из группы
        for member in self.members:
            pass

    def msg(self, text: str, src: Student = None):
        if src == None:
            src = self
        for member in self.members:
            print(f"{src.name} -> {member.name}: {text}")


Dima = Student("Dima", 1)
Anton = Student("Anton", 2)
group = Group("B2912")
