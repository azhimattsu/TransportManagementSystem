from tms.domain.valueobjects.containerdamage import ContainerDamage
from ...domain.valueobjects.containercode import ContainerCode
from ...domain.valueobjects.containerheight import ContainerHeight
from ...domain.valueobjects.containersize import ContainerSize
from ...domain.valueobjects.containertype import ContainerType
from ...domain.valueobjects.tareweight import TareWeight
from ...domain.entities.container import Container

# オブジェクトの生成


def Test_Container():
    code = ContainerCode("123456")
    type = ContainerType(1)
    tw = TareWeight(3500)
    height = ContainerHeight(86)
    size = ContainerSize(20)
    container = Container(code, type, tw, height, size)
    print(container)
    print(container.code)
    print(container.type)
    print(container.tw)
    print(container.height)
    print(container.size)

# オブジェクトの比較


def Test_ContainerCompare():
    code1 = ContainerCode("123456")
    type1 = ContainerType.TYPE_DRY
    tw1 = TareWeight(3500)
    height1 = ContainerHeight.HEIGHT_HIGH
    size1 = ContainerSize.HEIGHT_LONG
    damage1 = ContainerDamage.DAMAGE_OK
    container1 = Container(code1, type1, tw1, height1, size1, damage1)
    print(container1)

    code2 = ContainerCode("123456")
    type2 = ContainerType.TYPE_DRY
    tw2 = TareWeight(3500)
    height2 = ContainerHeight.HEIGHT_HIGH
    size2 = ContainerSize.HEIGHT_LONG
    damage2 = ContainerDamage.DAMAGE_OK
    container2 = Container(code2, type2, tw2, height2, size2, damage2)
    print(container2)

    print("check1")
    if container1.code == container2.code:
        print("OK")
    else:
        print("NO")

    print("check2")
    if container1.type == container2.type:
        print("OK", container1.type)
    else:
        print("NO")


print("TEST")
Test_Container()
Test_ContainerCompare()
