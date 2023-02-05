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
        self.name: str = name
        self.members: list[Student] = []

    def add(self, student: Student):
        self.members.append(student)
        student.group = self

    def remove(self, id: int):
        for member in self.members:
            if member.id == id:
                member.group = None
                self.members.remove(member)
                break

    def msg(self, text: str, src: Student = None):
        if src == None:
            src = self
        for member in self.members:
            if not member.id == src.id:
                print(f"{src.name} -> {member.name}: {text}")


Dima = Student("Dima", 1)
Anton = Student("Anton", 2)
group = Group("B2912")

group.add(Dima)
group.add(Anton)

Dima.msg_to_group("Privet vsem")
