# Diseño

## Arquitectura del Sistema

```mermaid
flowchart LR
    CLIENTE[Cliente Web / Navegador]
    DJANGO[Backend Django]
    DB[(Base de Datos)]
    AUTH[Servicio de Autenticación]

    AUTH --> DJANGO
    DB --> DJANGO
    DJANGO <--> CLIENTE
```

| Componente                | Descripción                                                            |
| ------------------------- | ---------------------------------------------------------------------- |
| Cliente Web / Navegador   | Interfaz desde la que el usuario accede al sistema y envía solicitudes |
| Backend Django            | Gestiona la lógica de negocio y el flujo de datos del sistema          |
| Base de Datos             | Almacenamiento persistente de la información                           |
| Servicio de Autenticación | Gestión de usuarios, sesiones y control de acceso                      |

## Modelo de Datos

```mermaid
erDiagram
    USER

    PROFILE

    SUBJECT

    LESSON

    ENROLLMENT {
        date enrolled_at
        float mark
    }

    USER ||--|| PROFILE : has
    USER ||--o{ SUBJECT : teaches
    SUBJECT ||--o{ LESSON : contains

    USER ||--o{ ENROLLMENT : enrolls
    SUBJECT ||--o{ ENROLLMENT : enrolled_in
```

## Diagramas

```mermaid
classDiagram
    class User {
        +int id
        +string username
        +string email
        +string firts_name
        +string last_name
        +string password
        +login()
        +signup()
        +logout()
        +leave()
    }

    class Profile {
        +int id
        +enum role
        +string bio
        +string avatar
        +edit_profile()
    }

    class Subject {
        +int id
        +int code
        +string name
        +request_certificate()
        +enroll_subjects()
        +unenroll_subjects()
    }

    class Lesson {
        +int id
        +string title
        +string content
        +add_lesson()
        +delete_lesson()
        +edit_lesson()
    }

    class Enrollment {
        +int id
        +date enrolled_at
        +float mark
        +edit_marks()
    }

    User "1" -- "1" Profile : has
    User "1" -- "0..*" Subject : teaches
    Subject "1" -- "0..*" Lesson : contains
    User "1" -- "0..*" Enrollment : enrolls
    Subject "1" -- "0..*" Enrollment : enrolled_in

```

## Decisiones de Diseño

- Django permite pasar del concepto al producto rápidamente gracias a su filosofía de "pilas incluidas". Ya trae integradas funciones que en otros frameworks requieren librerías externas.

- Al usar el sistema de plantillas de Django para el frontend, mantienes toda la lógica en un solo lenguaje (Python), evitando la complejidad de gestionar un framework de JavaScript (como React o Vue) si el proyecto no lo requiere estrictamente.

- Es mucho más sencillo desplegar y escalar una única aplicación que gestionar microservicios independientes.

- Python es reconocido por su sintaxis clara, lo que facilita que otros desarrolladores lean el código. Además, cuenta con un ecosistema de librerías inmenso para futuras expansiones (análisis de datos, IA, etc.).
