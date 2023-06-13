from polls.models import Question
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
     class Meta:
         model = Question
         fields = '__all__'

# 這樣 QuestionSerializer 會依照 Question 的欄位（fields）進行資料處理、驗證以及轉換。因為所有欄位都要所以 fields 設為 __all__。