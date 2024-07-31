class Shape:
    def set_scale(self, scale: float) -> Shape:
        self.scale = scale
        return self

Shape().set_scale(0.5)  # This should return an instance of Shape
