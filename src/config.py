from pymongo import MongoClient
import certifi

certificado=certifi.where() 

MONGO='mongodb+srv://bbaqueroalonso:brayanbaquero@cluster0.7hl6pdy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'


def Conexion ():
    try:
        Client= MongoClient(MONGO,tlsCAFile=certificado)
        bd = Client["bd_bibliografia"] 
        print('conexion exitosa')
    except ConnectionError:
        print('error de conexion')
    return bd


Conexion()
