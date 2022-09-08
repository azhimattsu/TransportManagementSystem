from tms.usecases.containers.containerdata import ContainerData


class ContainerGetAllResult:
    containers: list[ContainerData]

    def __init__(self, containers: list[ContainerData]):

        for value in containers:
            print(value)
            self.containers.append(value)
        print(containers)
#        self.containers = containers
