# Ejemplo completo de Clean Architecture 

Se habla mucho de clean architecture y tal vez como a mi os ha pasado que no habéis llegado a entender los por qué detrás de ella.

## Explicación general

Clean architecture no es un concepto nuevo como podemos ver en https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html . 

![imagen clean architecture](README/CleanArchitecture.jpeg)

Clean Architecture es un enfoque de diseño de software que busca separar la lógica de negocio de los detalles de la implementación técnica. Su objetivo es crear una arquitectura sólida y mantenible que permita una fácil evolución y extensión del sistema con el tiempo.

La arquitectura limpia se basa en la idea de dividir el código en capas independientes de la implementación técnica, lo que permite una mayor independencia de la administración de la infraestructura y los detalles de implementación. Esto mejora la legibilidad del código y facilita la identificación de las partes de la aplicación que deben modificarse para efectuar cambios.

La arquitectura limpia se compone de cuatro capas: 
- La capa de la interfaz de usuario, que interactúa con el usuario final.
- La capa de aplicación, que se encarga de la lógica de negocio de la aplicación.
- La capa de dominio, que contiene las reglas de negocio y los modelos.
- La capa de infraestructura, que se encarga de la conexión de la aplicación con su entorno técnico.


## Estructura del proyecto 

Al igual que la descripción del sistema de capa debe especificar y describir que hace cada uno de estas, debemos trasladar a nuestro proyecto el mismo comportamiento. Para ello crearemos una serie de carpetas que contendrán la lógica de cada uno de estas capas.

### Principales carpetas

Esta seria la distribución de carpetas que contendrán nuestro proyecto.

```
├── docker -> almacenamos configuración de docker
├── docs -> almacenamos yaml o postman de nuestro proyecto
└── src -> almacenamos el código de nuestro proyecto
```

## Visión general

La estructura general del proyecto será la siguiente

```
├── domain
|   ├── core
|   ├── entities
│   └── usecases
├── infrastructure
|   ├── api
|   ├── connectors
|   ├── factories
|   ├── orm
|   ├── server
│   └── settings
├── interfaces
│    ├── controllers
│    ├── repositories
│    ├── routes
│    └── serializers
└── presentation
    └── template
```

## Visión detallada y descripción de la carpeta SRC

Cada uno estos componentes tiene una función y no deben mezclarse entre ellos. Teniendo claro donde debe de ir cada una de las lógicas que implementemos.

```
├── domain
├── infrastructure
├── interfaces
└── presentation
```

- La capa de **dominio** (Domain Layer) es la capa más interna y central de la arquitectura. Es la capa que contiene la lógica empresarial principal y las reglas de negocio del sistema. Define los objetos y los conceptos de negocio del sistema, así como las operaciones que se pueden realizar sobre ellos. Esta capa no debe depender de ninguna infraestructura externa, como bases de datos, frameworks o bibliotecas externas. En cambio, su objetivo es definir las entidades, los casos de uso y las reglas de negocio de una manera independiente de la tecnología. En resumen, ya que contiene la lógica de negocio central y debe estar completamente aislada de las preocupaciones técnicas.
- La capa de **infraestructura** es la capa más externa de la arquitectura y es responsable de interactuar con recursos externos, como bases de datos, sistemas de archivos, redes y frameworks. Esta capa es la encargada de proporcionar implementaciones concretas de las interfaces definidas en la capa de dominio.
- La capa de **interfaces** es responsable de presentar la información al usuario final y de recibir las entradas del usuario. Esta capa puede incluir interfaces de usuario (UI), APIs y otros componentes que interactúan con el usuario o con sistemas externos.
- La capa de **presentación** encarga de la creación y actualización de la interfaz de usuario, y puede incluir componentes como las vistas, los controladores de vista y otros elementos que interactúan con el usuario.

### Capa domain

```
└── domain
    ├── core
    ├── entities
    └── usecases
```

- **Core**: esta capa se encarga de almacenar todos aquellos componentes que sean comunes a todas las capas. Por ejemplo: Constantes, datos de configuración etc.
- **UseCase**: almacena los casos de uso para cada dominio de nuestra aplicación. Ejemplo: Users -> Get, Delete, Create , Update.
- **Entity**: son modelos utilizados para gestionar los datos de nuestra aplicación

### Capa infraestructura

```
└── infrastructure
    ├── api
    ├── connectors
    ├── factories
    ├── orm
    ├── server
    └── settings
```

- **API**: el conjunto de viewsets que conforma nuestra api
- **connectors**: contiene los conectores a otras APIs
- **factories**: contiene las implementaciones con las inyecciones de dependencias
- **orm**: contiene las distintas fuentes de información pertenecientes al orm como base de datos o cache
- **server**: contiene las configuraciones del servidor como por ejemplo celery
- **settings**: contiene la configuración del proyecto

### Capa interfaces

```
└── interfaces
     ├── controllers
     ├── repositories
     ├── routes
     └── serializers
```

- **controllers**: los controladores de la api
- **repositories**: contiene los respositorios estos a su vez tienen las distintas dependencias de los datasources
- **routes**: contiene los paths a las urls
- **serializers**: contiene los serializadores para los distintos dominios

### Capa presentación

```
└── presentation
```

## Autor

Fernando Salom

https://fernandosalom.es

https://www.linkedin.com/in/fsalom/

## Licencia
[MIT](https://choosealicense.com/licenses/mit/)
