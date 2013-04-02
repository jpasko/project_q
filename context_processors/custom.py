from django.conf import settings

def domain(request):
    return {'DOMAIN': settings.DOMAIN}

def sizes_and_dimensions(request):
    return {'GALLERY_THUMBNAIL_DIMENSION': settings.GALLERY_THUMBNAIL_DIMENSION,
            'FREE_MAX_FILE_SIZE': settings.FREE_MAX_FILE_SIZE,
            'PREMIUM_MAX_FILE_SIZE': settings.PREMIUM_MAX_FILE_SIZE,
            'PROFESSIONAL_MAX_FILE_SIZE': settings.PROFESSIONAL_MAX_FILE_SIZE}
