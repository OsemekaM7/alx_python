import importlib.machinery

def main():
    loader = importlib.machinery.SourceFileLoader("variable_load_2", "variable_load_2.py")
    module = loader.load_module()
    
    if hasattr(module, 'a'):
        a_value = getattr(module, 'a')
        print(a_value)
    else:
        print("'a' not found in the imported module")

if __name__ == "__main__":
    main()