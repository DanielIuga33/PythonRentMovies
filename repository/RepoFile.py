class RepoFile:
    def __init__(self, filename):
        self.__filename = filename
        self.__repo = self.__read()

    def __read(self):
        with open(self.__filename, "r") as f:
            lines = f.read()
        if len(lines) == 0:
            return []
        result = []
        lines = lines.split("\n")
        for line in lines:
            if len(line) > 0:
                result.append(line)
        return result

    def __write_file(self):
        with open(self.__filename, "w") as file:
            for entity in self.__repo:
                file.write(f"{entity.__str__()}\n")

    def add(self, entity):
        self.__repo.append(entity)
        self.__write_file()

    def delete(self, entity):
        self.__repo.remove(entity)
        self.__write_file()

    def update(self, entity_new, entity_old):
        self.__repo.remove(entity_old)
        self.__repo.append(entity_new)

    def get_all(self):
        return self.__read()
