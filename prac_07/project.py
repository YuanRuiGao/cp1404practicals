class Project:

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        """Imported default information"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Control output"""
        return (f"{self.name}, "
                f"start: {self.start_date}, "
                f"priority {self.priority}, "
                f"estimate: ${self.cost_estimate}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare by priority"""
        return self.priority < other.priority

    def is_complete(self):
        """Determine whether it is completed"""
        return self.completion_percentage == 100
