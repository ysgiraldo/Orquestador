

import pandas as pd
import numpy as np
import os
import json
import psycopg2


class ExtractTransformLoad():
    def ejecutar(self):
        # cfg = self.getStepConfigUtf8()
        cfg = self.getStepConfig()
        connection, cursor = self.connectDataBase()

        primera = cfg["primera"]
        archivo = cfg["archivo"]

        print(primera)
        print("Esta es una prueba del orquestador")
        
        files = cfg["archivo"]

        # for file in files:
        #     archivo = self.getSQLPath() + file
        #     print(archivo)
        #     # helper.ejecutar_archivo(archivo, cfg)

        with open(files, 'r') as sql_file:
                sql_query = sql_file.read()
                cursor.execute(sql_query)
                connection.commit()

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
            print("Conexión a PostgreSQL exitosa")
            return connection, cursor
        except (Exception, psycopg2.Error) as error:
            print("Error al conectar a PostgreSQL", error)
            return None, None

