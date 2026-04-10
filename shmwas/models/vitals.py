class Vital:

    def setup(self, bp, sugar, hr):
        self.bp = bp
        self.sugar = sugar
        self.hr = hr

    def to_dict(self):
        return {
            "bp": self.bp,
            "sugar": self.sugar,
            "hr": self.hr
        }