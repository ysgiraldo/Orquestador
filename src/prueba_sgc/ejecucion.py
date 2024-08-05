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

from steps import ExtractTransformLoad, Prueba
import os
from funciones import Step

steps = [
    ExtractTransformLoad(), Prueba()
]

def main():
    orquestador = (
        "Orq 2 prueba tecnica ysgirald" \
        , steps
    )
    for step in orquestador[1]:
        step.ejecutar()

if __name__ == "__main__":
    main()