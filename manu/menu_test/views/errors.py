from django.shortcuts import render


def error_403(request, reason=None):
    return render(
        request, "403.html", status=403, context={"is_csrf": reason is not None}
    )


def error_404(request, exception=None):
    return render(request, "404.html", status=404)


def error_500(request):
    return render(request, "500.html", status=500)
