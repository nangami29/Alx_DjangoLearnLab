from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notification

@login_required
def user_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')

    data = []
    for n in notifications:
        data.append({
            "actor": n.actor.username,
            "verb": n.verb,
            "target": str(n.target),
            "timestamp": n.timestamp.strftime("%Y-%m-%d %H:%M"),
            "is_read": n.is_read
        })

    return JsonResponse({"notifications": data})
