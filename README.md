# Pruebas automatizadas API para Urban Grocers 
Urban Grocers es una aplicación de entrega de productos por catálogo y kits comestibles. Se realizaron pruebas automatizadas para el campo name en la solicitud de creación de un kit de productos en la aplicación Urban Grocers. 

# Herramientas 
- lenguajes:

  ![Static Badge](https://img.shields.io/badge/Python-%233776AB?style=for-the-badge&logo=python&logoColor=white)

- librerías:
  
  ![Static Badge](https://img.shields.io/badge/Pytest-%230A9EDC?style=for-the-badge&logo=pytest&logoColor=white) Es necesario para ejecutar las pruebas
  
  ![Static Badge](https://img.shields.io/badge/Request-%2368BC71?style=for-the-badge) Permite hacer las solicitudes HTTP a al API

# Lista de comprobación de las pruebas incluidas en la automatización para el campo Name

  | No. de prueba | Decripción | Código de respuesta esperados |
|--------------|--------------|--------------|
| 1 | Comprobar que el campo admite un caracter| 201 |
| 2 | Comprobar que el campo admite 511 caracteres| 201|
| 3 | Comprobar que el campo NO admite 0 caracteres | 400|
| 4 | Comprobar que el campo NO admite 512 caracteres | 400 |
| 5 | Comprobar que el campo admite caracteres especiales| 201|
| 6 | Comprobar que el campo admite espacios | 201|
| 7 | Comprobar que el campo admite números | 201 |
| 8 | Comprobar que la solitud marca error al enviarse sin el parametró name| 400 |
| 9 | Comprobar que el campo admite número y no string | 400 |


- Ejecuta todas las pruebas con el comando pytest create_kit_name_kit_test.py.


