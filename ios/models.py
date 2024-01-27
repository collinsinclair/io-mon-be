from django.db import models


# Create your models here.
class Input(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Name of input (could be player, book, or specific instrument.",
    )

    def __str__(self):
        return self.name


class Output(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Name of output (e.g. keys monitor, SL monitor, main, etc.)",
    )
    inputs = models.ManyToManyField(Input)

    def __str__(self):
        return self.name


class Request(models.Model):
    REQUEST_CHOICES = ((1, "More"), (-1, "Less"))
    output = models.ForeignKey(Output, on_delete=models.CASCADE)
    input = models.ForeignKey(Input, on_delete=models.CASCADE)
    value = models.IntegerField(choices=REQUEST_CHOICES)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_value_display()} {self.input} in {self.output} ({self.created_at.isoformat()})"
