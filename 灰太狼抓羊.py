import random

class Sheep:
    def __init__(self, name):
        self.name = name
        self.position = random.randint(1, 10)

class Wolf:
    def __init__(self):
        self.position = 0

def main():
    print("欢迎来到《灰太狼抓羊》！")
    wolf = Wolf()
    sheep_list = [Sheep("小白"), Sheep("小黑"), Sheep("小花")]

    while True:
        print("\n灰太狼位置：" + "-" * wolf.position + "灰")
        print("羊的位置：", end="")
        for sheep in sheep_list:
            print("-" * sheep.position + sheep.name, end=" ")
        print()

        move = input("\n请输入移动方向（左/右）：")
        if move == "左":
            wolf.position = max(0, wolf.position - 1)
        elif move == "右":
            wolf.position = min(10, wolf.position + 1)

        for sheep in sheep_list:
            sheep.position = random.randint(1, 10)

        for sheep in sheep_list:
            if sheep.position == wolf.position:
                print(f"\n灰太狼抓住了{sheep.name}！")
                sheep_list.remove(sheep)
                break

        if len(sheep_list) == 0:
            print("\n灰太狼成功抓住了所有羊，游戏结束！")
            break

if __name__ == "__main__":
    main()
