from rest_framework import serializers
# 시리얼라이저 가져오고
from .models import Post, Store # Post 모델 가져오기


# 모델을 가져와서 직렬화하겠다는거, 매개변수 모델 시리얼라이저
class PostSerializer(serializers.ModelSerializer):
    # 게시자는 변경할 수 없는 항목들
    poster = serializers.ReadOnlyField(source='poster.username')
    restaurant = serializers.ReadOnlyField(source='poster.store.store_name')
    local = serializers.ReadOnlyField(source='poster.store.store_adress')
    class Meta:
        model = Post
        # 포스트 모델에서 가져올 필드 정하기 id는 자동생성
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__' #지금은 그냥 all로 했는데 필요시 추가수정