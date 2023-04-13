def get_preferred_option(task_1, task_2):
    if task_1.description == "Wash Dishes" and task_2.description == "Cook Dinner":
        return "Wash Dishes"
    if task_1.description == "Cook Dinner" and task_2.description == "Wash Dishes":
        return "Wash Dishes"
    if task_1.description == "Cook Dinner" and task_2.description == "Clean Windows":
        return "Cook Dinner"
    if task_1.description == "Clean Windows" and task_2.description == "Cook Dinner":
        return "Cook Dinner"
    if task_1.description == "Clean Windows" and task_2.description == "Wash Dishes":
        return "Clean Windows"
    if task_1.description == "Wash Dishes" and task_2.description == "Clean Windows":
        return "Clean Windows"

    return "No preferred option"
