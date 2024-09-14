def filter_by_pet_type(customers, pet_type):
    return [customer for customer in customers if customer['tipo_mascota'] == pet_type] # Filtrar por un tipo de mascota específico

def filter_by_service(customers, service):
    return [customer for customer in customers if customer['servicio'] == service] # Filtrar por un tipo de servicio específico

def filter_by_minimum_spent(customers, min_amount):
    return [customer for customer in customers if customer['consumo'] >= min_amount] # Filtrar por consumo de dinero mínimo en servicios
