class ClassWithBugNoFail:

    def print_value(self, value):
        print(self.value)

    def set_value(self, value):
        self.value = value
    
if __name__ == "__main__":
    cls = ClassWithBugNoFail()
    cls.set_value(123)
    cls.print_value(456)
