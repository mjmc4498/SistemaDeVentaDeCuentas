# Sistema de Gestión y Pago de Cuentas

Este es un sistema web completo desarrollado con Python y Django que permite la gestión de cuentas o facturas y su pago por parte de los usuarios. La aplicación cuenta con un panel de administración para gestionar las cuentas y una interfaz pública para visualizarlas y pagarlas.

## ✨ Características Principales

- **Panel de Administración Seguro:** Gestiona (crea, lee, actualiza, elimina) todas las cuentas desde el panel de administrador incorporado de Django.
- **Vista Pública de Cuentas:** Las cuentas con estado "Pendiente" se muestran públicamente en una interfaz limpia y moderna.
- **Proceso de Pago Simulado:** Los usuarios pueden "pagar" las cuentas. Una vez pagada, la cuenta se marca como "Pagada" y desaparece de la lista pública.
- **Interfaz Moderna y Responsiva:** La interfaz de usuario está construida con **Bootstrap 5**, asegurando que se vea bien en cualquier dispositivo.
- **Confirmación de Pago:** Se utiliza JavaScript para mostrar un modal de confirmación antes de procesar un pago.
- **Listo para Desplegar:** El proyecto está configurado con Gunicorn y WhiteNoise, listo para ser desplegado en producción.

---

## 🚀 Guía de Despliegue y Uso

Esta guía cubre tanto la instalación local como el despliegue en un servidor de producción.

### 1. Instalación en un Entorno Local

Sigue estos pasos para ejecutar el proyecto en tu máquina.

#### Prerrequisitos
- Python 3.8 o superior
- `pip` (gestor de paquetes de Python)

#### Pasos de Instalación
1.  **Clona el Repositorio:**
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd <NOMBRE-DEL-DIRECTORIO>
    ```

2.  **Crea y Activa un Entorno Virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplica las Migraciones:**
    ```bash
    python manage.py migrate
    ```

5.  **Crea un Superusuario:**
    Necesitarás un administrador para acceder al panel de gestión.
    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicia el Servidor de Desarrollo:**
    ```bash
    python manage.py runserver
    ```
    El proyecto estará corriendo en `http://127.0.0.1:8000/`.

---

### 2. Despliegue en un Servidor (Hosting/Producción)

Esta es una guía genérica para desplegar la aplicación en un servicio como Heroku, DigitalOcean, AWS, o cualquier VPS.

#### a. Configuración del Proyecto para Producción

Antes de desplegar, es crucial configurar el proyecto para un entorno de producción.

1.  **Clave Secreta (`SECRET_KEY`):**
    Nunca uses la clave secreta de desarrollo en producción. Genera una nueva y cárgala desde una **variable de entorno**.
    *   **Ejemplo en `settings.py`:**
        ```python
        import os
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'tu-clave-secreta-por-defecto-para-desarrollo')
        ```

2.  **Modo de Depuración (`DEBUG`):**
    El modo de depuración **NUNCA** debe estar activo en producción.
    *   **Ejemplo en `settings.py`:**
        ```python
        DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
        ```
    En tu servidor de producción, establece la variable de entorno `DJANGO_DEBUG` a `False`.

3.  **Hosts Permitidos (`ALLOWED_HOSTS`):**
    Añade el dominio de tu sitio web a esta lista.
    *   **Ejemplo en `settings.py`:**
        ```python
        ALLOWED_HOSTS = ['tudominio.com', 'www.tudominio.com']
        ```

4.  **Base de Datos:**
    Es muy recomendable usar una base de datos más robusta como PostgreSQL en producción. La configuración se cargaría también desde variables de entorno.

#### b. Configuración de Archivos Estáticos (WhiteNoise)

Este proyecto está pre-configurado para usar `WhiteNoise` para servir archivos estáticos eficientemente.

*   **Añadir Middleware:** Asegúrate de que el middleware de WhiteNoise esté en `settings.py`, justo después del `SecurityMiddleware`.
    ```python
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        # ... otros middlewares
    ]
    ```

*   **Recolectar Archivos Estáticos:** Antes de iniciar el servidor, ejecuta este comando:
    ```bash
    python manage.py collectstatic
    ```

#### c. Configuración del Servidor de Aplicaciones (Gunicorn)

`Gunicorn` es el servidor WSGI que ejecutará tu aplicación Django.

*   **Iniciar el servidor con Gunicorn:**
    ```bash
    gunicorn core_project.wsgi:application
    ```
    Puedes configurar el número de `workers` y el `bind` (IP y puerto) según tu servidor:
    ```bash
    gunicorn --workers 3 --bind 0.0.0.0:8000 core_project.wsgi:application
    ```
    Normalmente, esto se gestiona con un servicio como `systemd` en un VPS para que se ejecute automáticamente.

---

### 3. Uso del Sistema

1.  **Accede al Panel de Administración:**
    -   Ve a `https://tudominio.com/admin/`.
    -   Inicia sesión con tus credenciales de superusuario.
    -   En la sección "Payments", haz clic en "Cuentas" para ver la lista de facturas.
    -   Usa el botón "Add cuenta" para crear una nueva factura. Rellena el título, el monto y asegúrate de que el estado sea "Pendiente" para que aparezca en la página pública.

2.  **Visualiza y Paga Cuentas:**
    -   Ve a la página de inicio `https://tudominio.com/`.
    -   Verás las tarjetas de todas las cuentas pendientes.
    -   Haz clic en "Pagar ahora" y confirma en la ventana emergente.
    -   La página se recargará con un mensaje de éxito, y la cuenta pagada ya no estará visible.
