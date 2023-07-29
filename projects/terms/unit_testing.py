class Calculator:
    
    def add_10(a):
        return a + 10
    
    def multiply_by_10(a):
        return a * 10
        
if __name__ == "__main__":
    # testing code
    assert Calculator.add_10(12) == 22          #test 1
    print("Pass test 1")
    assert Calculator.multiply_by_10(12) == 120 #test 2
    print("Pass test 2")
    try:                                        #test 3
        Calculator.add_10("asda")
        print("Fail test 3")
    except:
        print("Pass test 3")
    
    try:                                        #test 4
        Calculator.multiply_by_10("asda")
        print("Fail test 4")
    except:
        print("Pass test 4")
