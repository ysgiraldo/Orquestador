# -*- coding: utf-8 -*-

"""
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
-- Fecha Creación: 2024-08-01
-- Autores: Sofia Giraldo
-- Descripción: Ejecución y calendarización de la rutina
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
""" 

from steps import ExtractTransformLoad
import os

steps = [
    ExtractTransformLoad()
]

def main():
    orquestador = (
        "Orq 2 prueba tecnica ysgirald" \
        , steps
    )
    orquestador[1][0].ejecutar()

if __name__ == "__main__":
    main()