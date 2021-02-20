class PriorityMixin:
    @property
    def priority_human(self):
        """Humanized priority for sample."""
        return REV_PRIORITY_MAP[self.priority]

    @priority_human.setter
    def priority_human(self, priority_str: str):
        self.priority = PRIORITY_MAP.get(priority_str)

    @property
    def high_priority(self):
        """Has high priority?"""
        return self.priority > 1

    @property
    def low_priority(self):
        """Has low priority?"""
        return self.priority < 1
