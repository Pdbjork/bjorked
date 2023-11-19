class LearningGoal:
    def __init__(self, goal):
        self.goal = goal

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.learning_goals = []

    def set_learning_goal(self, goal):
        # Create a new learning goal object
        new_goal = LearningGoal(goal)
        # Add the learning goal to the user's list of learning goals
        self.learning_goals.append(new_goal)

