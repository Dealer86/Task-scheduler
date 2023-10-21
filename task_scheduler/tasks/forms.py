from django.forms import ModelForm
from .models import Tasks
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class TaskForm(ModelForm):
    """
    A form for creating and updating task entries.

    This form is used to create and update task entries in the Tasks model.

    Attributes:
        model (Tasks): The model associated with the form.
        fields (list): The fields to include in the form.
        widgets (dict): Custom widgets for form fields.

    Fields:
        task_name (CharField): The name of the task.
        date_deadline (DateTimeField): The deadline date and time for the task.

    Example Usage:
        form = TaskForm()
    """
    class Meta:
        model = Tasks
        fields = ['task_name', 'date_deadline']
        widgets = {
            "date_deadline": DateTimePickerInput,
        }
