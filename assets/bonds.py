class Bond:
    def __init__(self, t, fv):
        self.time_to_maturity = t
        self.face_value = fv

    def __repr__(self):
        return f"{self.time_to_maturity} Year Bond with Face Value of {self.face_value}"

    def get_payoff(self, **kwargs):
        return self.face_value