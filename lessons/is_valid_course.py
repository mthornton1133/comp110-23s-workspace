class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        """If level is 400+ and if the prereq is one."""
        if self.level < 400:
            return False
        for x in self.prerequisites:
            if x == prereq:
                return True
            else:
                return False
    