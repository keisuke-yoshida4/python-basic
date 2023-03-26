class Car:
    def __init__(self, model_name, mileage, manufacture):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacture = manufacture

    def gas(self):
        print("{0.manufacture}の{0.model_name}(燃費:{0.mileage}),アクセル全開!!".format(self))

    def breaks(self):
        print("{0.manufacture}の{0.model_name}(燃費:{0.mileage}),ブレーキ!!".format(self))


if __name__ == "__main__":
    prius = Car("A", 30, "China")
    honda = Car("B", 20, "japan")
    print(prius.mileage)

    prius.gas()
    prius.breaks()
    honda.gas()
