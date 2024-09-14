def apply_pipeline(customers, filters):
    for filter_func, args in filters: # Recorrer una lista con filtros
        customers = filter_func(customers, *args)
    return customers
