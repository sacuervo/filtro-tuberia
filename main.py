from data import customers  # Importa los datos
from filters import filter_by_pet_type, filter_by_service, filter_by_minimum_spent  # Importa los filtros
from pipeline import apply_pipeline  # Importa la función de tubería

if __name__ == "__main__":
    filters = [ # Definir filtros que se van a aplicar
        (filter_by_pet_type, ('perro',)),  # Filtrar por tipo de mascota: perro
        (filter_by_service, ('corte',)),  # Filtrar por servicio: corte
        (filter_by_minimum_spent, (30,))  # Filtrar por gasto mínimo: 30
    ]

    filtered_customers = apply_pipeline(customers, filters) # Aplicar filtros a usuarios

    print("Filtered customers:") # Mostrar resultado
    for customer in filtered_customers:
        print(customer)
