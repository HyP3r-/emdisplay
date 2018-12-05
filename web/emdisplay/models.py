from django.db import models


class ConfigurationCategory(models.Model):
    """
    ConfigurationCategory
    """

    name = models.CharField(max_length=200, unique=True)


class Configuration(models.Model):
    """
    Configuration
    List of Configuration Parameters like the Path to HylaFAX
    """

    configuration_category = models.ForeignKey(ConfigurationCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    key = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)


class ParsingTemplate(models.Model):
    """
    ParsingTemplate
    Stored Parsing Templates
    """

    description = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)


class EventFields(models.Model):
    """
    EventFields
    Possible Fields like post code, location, ...
    """

    name = models.CharField(max_length=200, unique=True)


class ParsingTemplateFields(models.Model):
    """
    ParsingTemplateFields
    Regular Expressions for parsing the fax
    """

    class Meta:
        unique_together = ("event_fields", "parsing_template",)

    activated = models.BooleanField()
    event_fields = models.ForeignKey(EventFields, on_delete=models.CASCADE)
    parsing_template = models.ForeignKey(ParsingTemplate, on_delete=models.CASCADE)
    primary = models.BooleanField()
    regex = models.CharField(max_length=200)


class Event(models.Model):
    """
    Event
    Stored Events with Image
    """

    date = models.DateTimeField(unique=True)
    image = models.BinaryField()


class EventDetail(models.Model):
    """
    EventDetail
    Detail Fields of a Event parsed with the Parsing Template and linked to the matching Event Fields
    """

    class Meta:
        unique_together = ("event", "event_fields",)

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_fields = models.ForeignKey(EventFields, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)


class MessagingTemplate(models.Model):
    """
    MessagingTemplate
    Messaging Types like SMS, Mail or WhatsApp and its template
    """

    name = models.CharField(max_length=200, unique=True)
    template = models.TextField()


class Receiver(models.Model):
    """
    Receiver
    User which can receive Messages from the various Plugins
    """

    name = models.CharField(max_length=200, unique=True)


class ReceiverMessaging(models.Model):
    """
    ReceiverMessaging
    Stored Adresses of a Receiver linked to the different Message Types
    """

    class Meta:
        unique_together = ("receiver", "messaging_template",)

    address = models.CharField(max_length=200)
    messaging_template = models.ForeignKey(MessagingTemplate, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)


class FireTruck(models.Model):
    """
    FireTruck
    List of Fire Trucks and its identification
    """

    identification = models.CharField(max_length=200, unique=True)
    status = models.CharField(max_length=200)
