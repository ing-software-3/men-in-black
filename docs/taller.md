# Taller - Métodos HTTP y Códigos de Estado

Identificar los principales métodos HTTP y los códigos de respuesta utilizados en servidores y APIs REST.

## Métodos HTTP

Complete la tabla consultando la función de cada método.

| Método | Función              | Ejemplo                   |
| ------ | -------              | -------                   |
| GET    | obtener / Get        | get list user             |
| POST   | enviar / Post        | post new user             |
| PUT    | actualizar / update  | put user dates            |
| DELETE | eliminar / delete    | delete user of database   |

## Códigos HTTP

| Código | Nombre                  | Significado                       |
| ------ | ------                  | -----------                       |
| 200    |  OK                     | Exitoso                           |
| 201    |  Created                | Creado con exito                  |
| 202    |  Accepted               | Solicitud recibida                |
| 204    |  No content             | Respuesta sin contenido           |
| 206    |  Partial Content        | Respuesta con contenido parcial   |
| 226    |  IM Used                | Aplicacion y uso de peticion GET  |
| 300    |  Multiple Choice        | Respuesta con multiples opciones  |
| 301    |  Moved Permanently      | URI del recurso cambiada          |
| 302    |  Found                  | URI cambiada temporalmente        |
| 304    |  Not Modified           | Respuesta no modificada           |
| 306    |  Unused                 | Respuesta no usada mas, reservada |
| 400    |  Bad request            | Datos invalidos                   |
| 401    |  Unauthorized           | Requiere autorizacion             |
| 403    |  Forbiddent             | No tienes autorizacion            | 
| 404    |  Not found              | EL recurso no existe              |
| 406    |  Not Acceptable         | negociacion de contenido vacio    |
| 408    |  Request Timeout        | desconexion por no uso servidor   |
| 409    |  Conflict               | peticion genera Conflicto         |
| 423    |  Locked                 | Recurso solicitado esta bloqueado |
| 500    |  Internal Server error  | Error del servidor                |