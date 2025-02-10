# Data Pipeline para Procesamiento de CSV en MySQL

Este proyecto implementa un **pipeline de datos** para procesar archivos **CSV** en **microbatches**, almacenarlos en **MySQL (RDS)** y calcular estadísticas en tiempo real.

## Requisitos

- Python 3.x
- MySQL en AWS RDS
- Bibliotecas: `pandas`, `pymysql`, `decimal`, `os`

## Ejecutar en GitHub Codespaces

Este proyecto está diseñado para ejecutarse en GitHub Codespaces, utilizando un contenedor de desarrollo personalizado con la carpeta `.devcontainer`.
Dentro de esta carpeta se encuentra el archivo `devcontainer.json`, que configura el entorno de desarrollo en Codespaces. Este archivo ejecuta 
automáticamente la instalación de las dependencias definidas en `requirements.txt`, por lo que no es necesario instalar ninguna librería manualmente.

### Pasos:
1. Haz clic en **"Code"** (botón verde).
2. Ve a la pestaña **Codespaces**.
3. Haz clic en **"+"** para crear un nuevo Codespace.
4. Espera a que el entorno se configure y abre `script.py`.
   
![Pipeline en ejecución](images/resultados.png)

¡Listo! Ya puedes ejecutar el pipeline sin instalar nada en tu computadora.
