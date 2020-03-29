import Pyro4
@Pyro4.expose
class drive(object):
  arquivos=[]
  def upload(self,file):
    self.arquivos.append(file)
  def download(self,file):
    if file in self.arquivos:
      return file
    else:
      return "Nao encontrado"
  def listar(self):
    return self.arquivos
  def delete(self,file):
    if file in self.arquivos:
      self.arquivos.remove(file)
      
daemon = Pyro4.Daemon()                
ns = Pyro4.locateNS()          
uri = daemon.register(drive)   
ns.register("exercicio.drive", uri)   
print("Ready.")
daemon.requestLoop()
