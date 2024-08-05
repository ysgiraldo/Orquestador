

import pandas as pd
import numpy as np
import os
import json
import psycopg2
from funciones import Step

"""
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
-- Fecha Creación: 2024-08-01
-- Autores: Sofia Giraldo
-- Descripción: Ejecución y calendarización de la rutina
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
"""
class ExtractTransformLoad(Step):
    def ejecutar(self):
        # cfg = self.getStepConfigUtf8()
        cfg = self.getStepConfig()
        connection, cursor = self.connectDataBase()

        primera = cfg["primera"]
        archivo = cfg["archivo"]

        print(primera)
        print("Esta es una prueba del orquestador")
        
        files = cfg["archivo"]

        for file in files:
            archivo = self.getSQLPath() + file
            print(archivo)
            # helper.ejecutar_archivo(archivo, cfg)

            with open(archivo, 'r') as sql_file:
                sql_query = sql_file.read()
                cursor.execute(sql_query)
                # connection.commit()
                results = cursor.fetchall()
                
                # Obtener los nombres de las columnas
                column_names = [desc[0] for desc in cursor.description]
        
        # Convertir los resultados a un DataFrame de pandas
        df = pd.DataFrame(results, columns=column_names)

        print(df.head())

class Prueba():
    def ejecutar(self):
        print("Esta es una prueba de la clase Prueba")
        