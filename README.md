# Patrón Filtro - Tubería. Guardería de mascotas
- Filtra a los clientes de una guardería por nombre, tipo de mascota, tipo de servicio solicitado y consumo mínimo (costo de los servicios)

## `data.py`
### `customers`
- Lista que contiene la información de los usuarios en forma de diccionario

## `filters.py`

### `filter_by_pet_type()`
- Filtra por tipo de mascota específico
 
### `filter_by_service()`
- Filtra por tipo de servicio específico

### `filter_by_minimum_spent()`
- Filtra por consumo de dinero mínimo en servicios

## `pipeline.py`

### `apply_pipeline()`
- Recibe la información de los clientes y aplica los filtros incluidos en una lista de filtros que recibe como argumento
- Regresa una nueva lista de usuarios con los filtros aplicados

## `main.py`
- En el main, se definen los filtros que se van a aplicar
- Se aplica el metodo `apply-pipeline` de `pipeline.py` para aplicarle los filtros a los usuarios ingresados
- Muestra el resultado del proceso de filtrado