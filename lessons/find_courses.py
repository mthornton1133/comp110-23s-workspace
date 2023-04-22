class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

def find_courses(classes: list[Course], prereq: str) -> list[str]:
    final_list: list[str] = []
    for x in classes:
        if x.level > 400 and prereq in x.prerequisites:
            final_list.append(x.name)
    return final_list