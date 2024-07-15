# __init__.py

from .process_pdf import process_pdf

def main():
    import sys
    if len(sys.argv) > 1:
        process_pdf(sys.argv[1])
    else:
        print("Usage: python -m your_module_name <path_to_pdf>")

if __name__ == "__main__":
    main()
