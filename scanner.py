import socket
import threading
from queue import Queue
from typing import NoReturn

#establecemos como variable global la lista de ports que estan abiertos ya que abriremos varios threads y neceistamos guardar los numeros de aquellos que estan abiertos
listPorts = []

#establecemos la cola con los numeros del 0 al 500 como variable global para que todos los threads lo puedan usar
q: Queue = Queue()
for i in range(40000, 60000):
	q.put(i)

def scanPort(port: int) -> bool:
	#en caso de que el port este cerrado, nos salatara un error por lo que usamos try
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indica que queremos un socket para la intenet, no para UNIX. SOCK_STREAM indica que queremos el protocolo TCP no UDP
		conn = s.connect((target, port)) #nos conectamos al cliente con el port indicado, debemos pasar una tupla
		print(1)
		return True
	except:
		return False	

def getPort() -> NoReturn:
	#mientras que la cola no esta vacia, seguiremos cogiendo nuevos ports
	while not q.empty():
		#quitamos un elemento de la cola y lo definimos como nuestro port
		port = q.get()
		IsOpen: bool = scanPort(port)
		#pondremos un mensaje si encontramos un port abierto
		if IsOpen:
			print(f'Port {port} is Open!!!')

def main ():
	target = '192.168.1.43' #establecemos el ip del cliente al que queremos escanear

	for i in range(10):
		t = threading.Thread(target = getPort()) 
		t.start()





if __name__ == '__main__': main()