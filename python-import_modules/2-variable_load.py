import importlib.util

def main():
    spec = importlib.util.spec_from_file_location("variable_load_2", "variable_load_2.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if hasattr(module, 'a'):
        print(module.a)
    else:
        print("'a' not found in the imported module")

if __name__ == "__main__":
    main()
