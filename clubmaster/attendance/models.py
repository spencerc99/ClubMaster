from django.db import models
from django.core.validators import RegexValidator
from organizations.models import Organization

class Member(models.Model):
    """
    This is a model that represent a member in the club.
    """
    COLLEGES = (
        'McMurtry', 'Martel', 'Brown',
        'Duncan', 'Jones', 'Lovett',
        'Will Rice', 'Hanzen', 'Sid Rich',
        'Baker', 'Wiess'
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField(blank=True)
    college = models.CharField(max_length=10)
    grad_year = models.IntegerField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def to_json(self):
        """
        This will take the current member and return the jsonified version of self.
        :return: model_json
        """
        model_json = {'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email,
                      'phone_number': self.phone_number, 'college': self.college, 'grad_year': self.grad_year,
                      'organization': self.organization.name}
        return model_json

    def to_list(self):
        """
        This will take the current member and return a list of all the attributes in order except organization
        """
        return [self.first_name, self.last_name, self.email, self.phone_number, 
                self.college, self.grad_year]


class Event(models.Model):
    """
    This is a model that represents an Event of an organization.
    """
    name = models.CharField(max_length=64)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=140)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def to_json(self):
        """
        This will take the current event and return the jsonified version of self.
        :return: model_json
        """

        model_json = {'event_name': self.name, 'start_time':self.end_time, 'location': self.location,
                      'description': self.description, 'organization': self.organization.name}
