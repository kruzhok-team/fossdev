from importlib.util import (spec_from_file_location, 
                            module_from_spec)
import sys
spec = spec_from_file_location("module.name", "/path/to/my_package/my_module.py")
foo = module_from_spec(spec)
sys.modules["module.name"] = foo
spec.loader.exec_module(foo)
foo.MyClass()
