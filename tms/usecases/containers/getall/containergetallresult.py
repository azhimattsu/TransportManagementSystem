from tms.usecases.containers.containerdata import ContainerData


class ContainerGetAllResult:
    containers: list()

    def __init__(self, containers: list[ContainerData]):

        for value in containers:
            print(value)
#            self.containers.append(value)

#        self.containers = containers
