from django.utils.deprecation import MiddlewareMixin
from main.models import IPLog

class IPLogMiddleware(MiddlewareMixin):
    def get_client_ip(self, request):
        """Userning real IP manzilini olish"""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    def process_request(self, request):
        ip = self.get_client_ip(request)
        path = request.path

        obj, created = IPLog.objects.get_or_create(
            ip=ip,
            path=path,
            defaults={"count": 1}
        )

        if not created:
            obj.count += 1
            obj.save()
