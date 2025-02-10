# Data Pipeline para Procesamiento de  archivos CSV en MySQL

Este proyecto implementa un **pipeline de datos** para procesar archivos **CSV** en **microbatches**, almacenarlos en **MySQL (RDS)** y calcular estadísticas en tiempo real.

## Requisitos

- **Python 3.x**
- **MySQL en AWS RDS**
- **Bibliotecas necesarias:** `pandas`, `pymysql`, `decimal`, `os`

## Ejecutar en GitHub Codespaces

Este proyecto está diseñado para ejecutarse en **GitHub Codespaces**, utilizando un contenedor de desarrollo personalizado con la carpeta `.devcontainer`.  
Dentro de esta carpeta se encuentra el archivo `devcontainer.json`, que configura el entorno de desarrollo en Codespaces.  

> 📌 **Nota:**  
> Este archivo ejecuta automáticamente la instalación de las dependencias definidas en `requirements.txt`, por lo que **no es necesario instalar ninguna librería manualmente**.

### Pasos para ejecutar el proyecto:
1. Iniciar sesión en tu cuenta de **GitHub.**
2. **Abre el repositorio en GitHub.**
3. **Haz clic en** `Code` (botón verde).
4. **Ve a la pestaña** `Codespaces`.
5. **Haz clic en** `+` **para crear un nuevo Codespace.**
   
   ![Crear Codespace](images/codespace.PNG)
   
6. **Espera a que el entorno se configure** (aprox. **40s** para instalar las librerías de `requirements.txt`).
   
   ![Extensiones activadas](images/extensiones.PNG)
   
7. **Abre `script.py` y revisa el código comentado.**

8. **Ejecuta el script en la terminal de Codespaces:**
   ```sh
   python3 script.py

### Resultados:

Vista general de **GitHub Codespaces** despues de ejecutar el script:

 ![Resultados](images/resultados.PNG)
