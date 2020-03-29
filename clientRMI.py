import Pyro4

drive = Pyro4.Proxy("PYRONAME:exercicio.drive")
drive.upload("Arquivo1")
drive.upload("Arquivo2")
drive.upload("Arquivo3")
drive.upload("Arquivo4")
drive.delete("Arquivo1")
print (drive.listar())
