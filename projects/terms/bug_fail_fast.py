class ClassWithBugFailFast:

    def print_value(self):
        print(value)

    def set_value(self, value):
        self.value = value
    
if __name__ == "__main__":
    cls = ClassWithBugFailFast()
    cls.set_value(123)
    cls.print_value()


