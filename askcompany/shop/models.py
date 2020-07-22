from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100) # Charfield는 길이 제한이 있음
    desc = models.TextField(blank=True) # TextField는 길이 제한이 없음
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True) # 추가 될 때 자동 저장
    updated_at = models.DateTimeField(auto_now=True) # 업데이트 될 때마다 자동 저장
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name