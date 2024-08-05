import os
import json
import psycopg2

# Resumen
class Step:
    def getFolderPath(self):
        return os.path.join(os.path.dirname(__file__), 'static', '')

    def getStepConfig(self):

        path = self.getFolderPath() + "config.json"

        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f_in:
                json_str = f_in.read()
            
            # Se lee el archivo config.json
            cfg = json.loads(json_str)

        # Se define que llame lass variables del nombre de la clase
            cfg = cfg.get(type(self).__name__,{})
            return cfg
            
    def getSQLPath(self):
        return os.path.join(os.path.dirname(__file__), 'static', 'sql', type(self).__name__, '')

    def connectDataBase(self):
        cfg = self.getStepConfig()

        try:
            connection = psycopg2.connect(
                user= cfg["credenciales"]["user"],
                password=cfg["credenciales"]["password"],
                host=cfg["credenciales"]["host"],
                port=cfg["credenciales"]["port"],
                database=cfg["credenciales"]["database"]
            )
            cursor = connection.cursor()
            cursor.execute("SET client_encoding TO 'UTF8';")
            print("Codificación del cliente configurada a UTF8")

            # Ejemplo de ejecución de una consulta
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print(f"Versión de PostgreSQL: {record}")
            return connection, cursor
        except (Exception, psycopg2.Error) as error:
            print("Error al conectar a PostgreSQL", error)
            return None, None