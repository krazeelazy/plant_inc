from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=255)
    colour = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    is_local = models.BooleanField(blank=False, null=False)
    """(BooleanField) whether or not the fruit is local"""

    class Meta:
        db_table = "fruits"


    def __str__(self):
        """Returns the string representation of the object

        :return: the string representation of the object (name of the fruit) 
        :rtype: str
        """

        return self.name