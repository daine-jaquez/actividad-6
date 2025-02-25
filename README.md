# Activiadad #6

Daine Jaqeuz 22-1142

##  Descripción

*Caso de Estudio: Desafíos en la Implementación de un Sistema de Autenticación en Canales Alternos de entidad financiera.*

Los casos de uso para esta prueba se encuentran en la carpeta docs/casos-de-prueba.csv

## ¿Cómo iniciar el proyecto?

1. verifica la isntalacion de python `python3 --version`
2. creación de entorno vistual `python3 -m venv venv`
3. instalar Pytest `pip install pytest`
4. ejecute `pytest -v` para correr las pruebas
   

## Resultados

```
rootdir: /Documents/side/actividad-6
collected 4 items

test_auth.py::test_generate_otp PASSED                                                                                                         [ 25%]
test_auth.py::test_validate_correct_otp PASSED                                                                                                 [ 50%]
test_auth.py::test_validate_incorrect_otp PASSED                                                                                               [ 75%]
test_auth.py::test_validate_expired_otp PASSED
```
