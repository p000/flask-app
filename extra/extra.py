#author Pushpahas

class Extra(object):
    @staticmethod
    def add(a, b):
        try:
            sum = a + b
			return sum
        except Exception as e:            
            return e