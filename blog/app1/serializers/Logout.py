from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutS(serializers.Serializer):
    refresh=serializers.CharField()
    def validate(self, data):
        self.token=data["refresh"]
        return data
    def save(self, **kwargs):
        RefreshToken(self.token).blacklist()
        