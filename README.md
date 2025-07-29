# 🧪 Proyecto de Pruebas Urban Grocers – Creación de un kit para el usuario o usuaria

Este proyecto automatiza la prueba de creación de un "kit" para un usuario o usuaria dentro del sistema, validando distintos escenarios usando `pytest`. El kit no es una tarjeta, sino un recurso específico asociado al usuario.

## 📖 Fuente de documentación

La documentación oficial de la API se encuentra en:

```
<la URL del servidor lanzado>/docs/
```

Una vez allí, dirígete a:

- **Main.Kits → Crear un kit**  
Para conocer los detalles sobre el endpoint utilizado en este proyecto.

Este proyecto también sigue la convención de documentación **[apiDoc](https://apidocjs.com/)** para documentar los endpoints utilizados en las pruebas.

## 🧰 Tecnologías y técnicas utilizadas

- **Python 3.x** – Lenguaje principal del proyecto.
- **pytest** – Framework de pruebas para automatizar casos positivos y negativos.
- **requests** – Librería HTTP para interactuar con la API.
- **apiDoc** – Generador de documentación para las solicitudes de la API.
- **Funciones reutilizables** – Se usan funciones como `get_new_user_token()`, `post_new_client_kit()`, etc., para mantener un código limpio y modular.

## 📋 Descripción del flujo

1. Se crea un nuevo usuario o usuaria mediante una solicitud `POST`.
2. Se obtiene y guarda el token de autenticación (`authToken`).
3. Se realiza una solicitud para crear un kit personal para el usuario o usuaria usando ese token.
4. Se ejecuta una lista de comprobación de pruebas (positive y negative cases).

## ✅ Lista de comprobación de pruebas

| Nº | Descripción | Cuerpo de prueba | Código esperado |
|----|-------------|------------------|------------------|
| 1 | Longitud válida mínima (1) | `{ "name": "a" }` | 201 |
| 2 | Longitud válida máxima (511) | `{ "name": "..." }` | 201 |
| 3 | Longitud no válida (0) | `{ "name": "" }` | 400 |
| 4 | Longitud no válida (>512) | `{ "name": "..." }` | 400 |
| 5 | Caracteres especiales | `{ "name": "!№%@"," }` | 201 |
| 6 | Espacios en el nombre | `{ "name": " A Aaa " }` | 201 |
| 7 | Números en el nombre | `{ "name": "123" }` | 201 |
| 8 | Parámetro no enviado | `{}` | 400 |
| 9 | Tipo de dato incorrecto (número) | `{ "name": 123 }` | 400 |

**Nota:** Algunos resultados pueden dar `FAILED`, esto es normal y esperado en ciertos escenarios de prueba negativa.

## 🗂 Estructura del proyecto

```
urban_grocers_kit/
│
├── configuration.py              # URLs base y configuración general
├── data.py                       # Datos de prueba y cuerpos de solicitud
├── sender_stand_request.py      # Funciones para enviar solicitudes POST
├── create_kit_name_kit_test.py  # Archivo principal de pruebas
├── .gitignore                   # Archivos que no deben incluirse en control de versiones
└── README.md                    # Este archivo
```

## ⚙️ Requisitos

- Python 3.x
- `pytest`
- `requests`

Instalación de dependencias:
```bash
pip install pytest requests
```

## 🚀 Ejecución de pruebas

Desde PyCharm, puedes ejecutar las pruebas fácilmente sin usar la terminal:

1. En la barra de navegación has clic en el boton "Run"
2. Asegurate de tener seleccionado "current File" para que se corran todas las pruebas

Esto ejecutará todas las pruebas definidas en el archivo utilizando `pytest` integrado en PyCharm.

Asegúrate de que tu entorno virtual esté configurado correctamente como intérprete del proyecto (puedes verlo en la esquina inferior derecha o en `File > Settings > Python Interpreter`).


## 🔍 Estructura de funciones

- `get_new_user_token()` – Crea un nuevo usuario y devuelve el token de autenticación.
- `post_new_client_kit(kit_body, auth_token)` – Crea un kit para el usuario usando el token.
- `get_kit_body(name)` – Devuelve una copia modificada del cuerpo base del kit.
- `positive_assert(kit_body)` – Para pruebas que esperan código 201.
- `negative_assert_code_400(kit_body)` – Para pruebas negativas que esperan código 400.