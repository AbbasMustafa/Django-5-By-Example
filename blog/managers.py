from django.db import models

class PublishedManger(models.Manager):
    def __init__(self, Status) -> None:
        super().__init__()
        self.Status = Status

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=self.Status.PUBLISHED)