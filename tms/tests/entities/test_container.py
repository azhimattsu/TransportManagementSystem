from tms.master.domain.valueobjects import container
from tms.master.domain.entities.container import ContainerEntity

# オブジェクトの生成


def Test_Container():
    code = container.Code("123456")
    type = container.Type(1)
    tw = container.TareWeight(3500)
    height = container.Height(86)
    size = container.Size(20)
    container1 = ContainerEntity(code, type, tw, height, size)
    print(container1)
    print(container1.code)
    print(container1.type)
    print(container1.tw)
    print(container1.height)
    print(container1.size)

# オブジェクトの比較


def Test_ContainerCompare():
    code1 = container.Code("123456")
    type1 = container.Type.TYPE_DRY
    tw1 = container.TareWeight(3500)
    height1 = container.Height.HEIGHT_HIGH
    size1 = container.Size.HEIGHT_LONG
    damage1 = container.Damage.DAMAGE_OK
    container1 = ContainerEntity(code1, type1, tw1, height1, size1, damage1)
    print(container1)

    code2 = container.Code("123456")
    type2 = container.Type.TYPE_DRY
    tw2 = container.TareWeight(3500)
    height2 = container.Height.HEIGHT_HIGH
    size2 = container.Size.HEIGHT_LONG
    damage2 = container.Damage.DAMAGE_OK
    container2 = ContainerEntity(code2, type2, tw2, height2, size2, damage2)
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
