import os
# import shutil

# new_directory = r"c:\Users\AdrianRares(TI)"
# os.chdir(new_directory)

# current_directory = os.getcwd()
# print(f"Direitório atual: {current_directory}")

# print(os.listdir(current_directory))

# os.mkdir(r"c:\Users\AdrianRares(TI)\Teste")

# os.rmdir(r"c:\Users\AdrianRares(TI)\Teste")

# shutil.rmtree(r"c:\Users\AdrianRares(TI)\Teste")

# os.remove("teste2.py")

# os.rename("Teste", "Teste(1)")

# if os.path.exists("main.py"):
#     print("O arquivo existe!")

# if os.name == 'posix':
#     print("Este é um sistema Unix ou Linux.")
# elif os.name == 'nt':
#     print("Este é um sistema Windows.")

# print(os.environ.items())

if os.path.isfile("main.py"):
    print(f"É um arquivo.")
else:
    print(f"Não é um arquivo ou não existe.")