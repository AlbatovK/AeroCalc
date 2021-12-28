class TheoryViewModel:

    def __init__(self, up_force, resistance, reinolds):
        self.s_1 = up_force
        self.s_2 = resistance
        self.s_3 = reinolds

    def count_up_force(self, p, v, c_y, s):
        res = 0.5 * p * v * v * c_y * s
        self.s_1.emit(res)

    def count_resistance(self, p, v, c_x, s):
        res = 0.5 * p * v * v * c_x * s
        self.s_2.emit(res)

    def count_reinolds(self, p, v, b, m):
        res = (p * b * v) / m
        self.s_3.emit(res)
