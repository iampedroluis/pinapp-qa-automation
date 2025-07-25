# Challenge de QA Automation - Login + API Testing

Este proyecto es parte de un **Challenge de Automatización QA**, el cual cubre pruebas automatizadas de interfaz gráfica con **Selenium + Python + Cucumber** (pytest-bdd) utilizando el patron de diseño POM (Pages Object Model).

 Pruebas de API utilizando **Postman** con la API pública de [Swagger Petstore](https://petstore.swagger.io/).

---

##  Tecnologías utilizadas

- Python 3.11+
- Selenium
- Pytest
- Pytest-bdd (Cucumber en Python)
- HTML Reports (pytest-html)
- Postman (con Collection y Environment incluidos)
- API pública de Swagger Petstore (User endpoint)

---

##  Estructura del proyecto

```
project/
│
├── features/
│   └── login.feature                # Archivo con escenarios Gherkin
│
├── pages/
│   └── login_pages.py              # Pages Object Models 
│
├── steps/
│   └── login_steps.py              # logica de los pasos escritos en Gherkin
│ 
├── reports/
│   └── report.html                 # Reporte HTML generado por pytest
│
├── postman/
│   ├── SwaggerPetstore.postman_collection.json
│   └── ENV_PINAPP.postman_environment.json
│
├── conftest.py                     # archivo para configurar drivers
├── pytest.ini                      # archivo para definir marcas de casos de prueba y algunos warnings
├── requirements.txt
└── README.md
```

---

##  Requisitos previos

### 1. Instalar Python

 [Descargar Python 3.11+](https://www.python.org/downloads/)

> Verifica que Python y pip estén correctamente instalados:

```bash
python --version
pip --version
```

---

### 2. Clonar este repositorio

```bash
git clone https://github.com/iampedroluis/pinapp-qa-automation.git
cd pinapp-qa-automation
```

---

### 3. Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv\Scripts\activate         # En Windows
```

---

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

##  Ejecución de pruebas

Este proyecto contiene escenarios escritos en lenguaje Gherkin y ejecutados con Pytest-BDD. 

### Ejecutar un escenario específico

markers =
    PIA_001: Prueba de registro de usuario
    PIA_002: Prueba de login de usuario

```bash
pytest -m <marca_del_test> --gherkin-terminal-reporter --html=reports/report.html --self-contained-html --capture=sys --log-cli-level=INFO -vv
```

 Esto generará un reporte visual en `reports/report.html`.

---

## Postman - API Testing

También se incluyen pruebas sobre la API pública de Swagger Petstore:

 [https://petstore.swagger.io/#](https://petstore.swagger.io/#)

### Endpoints utilizados:

- `/user`
  - Crear usuario
  - Obtener usuario por nombre
  - Actualizar usuario
  - Eliminar usuario

---

### Archivos incluidos

Dentro del directorio `postman/` encontrarás:

- `SwaggerPetstore.postman_collection.json`
- `ENV_PINAPP.postman_environment.json`

---

### Instrucciones para ejecutar en Postman

1. Descargar [Postman](https://www.postman.com/downloads/)
2. Abrir Postman
3. Importar la Collection:
   - Ir a **"File > Import"** y seleccionar `SwaggerPetstore.postman_collection.json`
4. Importar el Environment:
   - Ir a **"File > Import"** y seleccionar `ENV_PINAPP.postman_environment.json`
5. Seleccionar el Environment llamado `ENV_PINAPP`
6. Ejecutar las peticiones desde la Collection
   - Asegúrate de verificar y modificar las variables si es necesario

---

### Variables importantes

- Variables de colección: utilizadas para definir valores reutilizables.
- Variables de entorno (ENV_PINAPP): contiene valores dinámicos para base URLs, usuarios, etc.

---
## Notas adicionales

> Al ser una Api publica se necesita ejecutar mas de una vez la peticion.


---

## Contacto

Si tienes dudas o sugerencias, no dudes en contactarme.

Autor: Pedro Gutierrez 
Email: pedroluisgutierrez.dev@gmail.com
Linkedin: [Pedro Gutierrez](https://www.linkedin.com/in/pedro-luis-gutierrez-contreras) 
GitHub: [@iampedroluis](https://github.com/iampedroluis)
