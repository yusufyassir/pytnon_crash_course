def print_modules(unprinted_designs, completed_models):
    """
    simulate printing each design, until none are left.
    move each design to completed_models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_mocels):
    """show models that have been printed"""
    print("the following models have been printed:")
    for model in completed_mocels:
        print(model)