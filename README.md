# Django Rest Framework Starter

Este repositorio contiene un proyecto  de Django Rest Framework.

## Pasos para Iniciar

1. **Clona el Repositorio:**
    ```bash
    git clone https://github.com/moisesEscobar/backend_mb_djangorest.git
    cd backend_mb_djangorest
    ```

2. **Crea un Entorno Virtual (opcional, pero recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En sistemas basados en Unix
    # O en Windows: .\venv\Scripts\activate
    ```

3. **Instala las Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configura la Base de Datos:**
    ```bash
    python manage.py migrate
    ```

5. **Crea un Superusuario (opcional):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Inicia el Servidor de Desarrollo:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

- La API estará disponible en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- El panel de administración estará disponible en: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Recursos Adicionales

- [Documentación de la API en POSTMAN ](https://documenter.getpostman.com/view/12536131/2s9Ykn81p3)
- [Documentación de Django Rest Framework](https://www.django-rest-framework.org/)
- [Django Project](https://www.djangoproject.com/)
