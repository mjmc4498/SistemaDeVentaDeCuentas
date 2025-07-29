# Sistema de Gestión y Pago de Cuentas

Este es un sistema web completo desarrollado con Python y Django que permite la gestión de cuentas o facturas y su pago por parte de los usuarios. La aplicación cuenta con un panel de administración para gestionar las cuentas y una interfaz pública para visualizarlas y pagarlas.

## ✨ Características Principales

- **Panel de Administración Seguro:** Gestiona (crea, lee, actualiza, elimina) todas las cuentas desde el panel de administrador incorporado de Django.
- **Vista Pública de Cuentas:** Las cuentas con estado "Pendiente" se muestran públicamente en una interfaz limpia y moderna.
- **Proceso de Pago Simulado:** Los usuarios pueden "pagar" las cuentas. Una vez pagada, la cuenta se marca como "Pagada" y desaparece de la lista pública.
- **Interfaz Moderna y Responsiva:** La interfaz de usuario está construida con **Bootstrap 5**, asegurando que se vea bien en cualquier dispositivo (escritorio, tablet, móvil).
- **Confirmación de Pago:** Se utiliza JavaScript para mostrar un modal de confirmación antes de procesar un pago, mejorando la experiencia de usuario y evitando acciones accidentales.
- **Listo para Desplegar:** El proyecto incluye un archivo `requirements.txt`, lo que facilita su despliegue en cualquier servicio de hosting compatible con Python/Django.

## 🚀 Puesta en Marcha (Desarrollo Local)

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### Prerrequisitos

- Python 3.8 o superior
- `pip` (gestor de paquetes de Python)

### 1. Clona el Repositorio

```bash
git clone <URL-DEL-REPOSITORIO>
cd <NOMBRE-DEL-DIRECTORIO>
```

### 2. (Opcional pero recomendado) Crea un Entorno Virtual

Es una buena práctica trabajar dentro de un entorno virtual para aislar las dependencias del proyecto.

```bash
# Para Windows
python -m venv venv
venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala las Dependencias

El archivo `requirements.txt` contiene todas las librerías de Python necesarias.

```bash
pip install -r requirements.txt
```

### 4. Aplica las Migraciones de la Base de Datos

Este comando creará la base de datos (un archivo `db.sqlite3`) y las tablas necesarias.

```bash
python manage.py migrate
```

### 5. Crea un Superusuario

Necesitarás un usuario administrador para acceder al panel de gestión. Sigue las instrucciones en la consola para crear tu usuario.

```bash
python manage.py createsuperuser
```

### 6. Inicia el Servidor de Desarrollo

```bash
python manage.py runserver
```

¡Y listo! El proyecto estará corriendo en `http://127.0.0.1:8000/`.

## 🛠️ Uso del Sistema

1.  **Accede al Panel de Administración:**
    -   Ve a `http://127.0.0.1:8000/admin/`.
    -   Inicia sesión con las credenciales del superusuario que creaste.
    -   Dentro de la sección "Payments", puedes añadir, modificar o eliminar "Cuentas".

2.  **Visualiza la Página Pública:**
    -   Ve a `http://127.0.0.1:8000/`.
    -   Aquí verás todas las cuentas que has creado con el estado "Pendiente".

3.  **Realiza un Pago:**
    -   Haz clic en el botón "Pagar ahora" de cualquier cuenta.
    -   Confirma la acción en la ventana emergente.
    -   La página se recargará y la cuenta pagada ya no estará en la lista.

## 🔧 Tecnologías Utilizadas

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript
- **Framework CSS:** Bootstrap 5
- **Base de Datos (desarrollo):** SQLite3
