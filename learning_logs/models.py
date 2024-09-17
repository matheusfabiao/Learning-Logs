from django.db import models

# Create your models here.
class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Devolve uma representação em String do modelo"""
        if len(str(self.text)) > 50:
            return self.text[:50] + ' ...'
        else:
            return self.text


class Entry(models.Model):
    """Algo específico aprendido sobre um assunto"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        """Devolve uma representação em String do modelo"""
        if len(str(self.text)) > 50:
            return self.text[:50] + ' ...'
        else:
            return self.text
