import pytest 

def pytest_generate_tests(metafunc):
    if "max_numb1er" in metafunc.fixturenames:
        # end can be retrived from command line parameters
        end = 10    
        metafunc.parametrize("max_number", range(end))
