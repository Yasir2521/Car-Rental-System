class FloatConverter:
    regex = r'[\d\.]+' # This regex will match any float value

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)