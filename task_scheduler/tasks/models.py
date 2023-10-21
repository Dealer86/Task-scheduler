from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    """
    Model for representing user tasks.

    This model represents tasks associated with a user. It includes fields
    for the user, task name, date created, and deadline.

    Fields:
        user (ForeignKey to User): The user associated with the task.
        task_name (CharField): The name of the task (up to 300 characters).
        date_created (DateField): The date the task was created (auto-generated).
        date_deadline (DateTimeField): The deadline date and time for the task.

    Methods:
        __str__: Returns the task name as the string representation of the task.

    Example Usage:
        task = Tasks(user=user_instance, task_name="Sample Task", date_deadline=datetime_instance)
        task.save()
    """
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    date_deadline = models.DateTimeField()

    def __str__(self):
        return self.task_name
