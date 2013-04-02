from django.conf import settings

def domain(request):
    return {'DOMAIN': settings.DOMAIN}

def sizes_and_dimensions(request):
    return {'GALLERY_THUMBNAIL_DIMENSION': settings.GALLERY_THUMBNAIL_DIMENSION,
            'FREE_MAX_FILE_SIZE': settings.FREE_MAX_FILE_SIZE,
            'PREMIUM_MAX_FILE_SIZE': settings.PREMIUM_MAX_FILE_SIZE,
            'PROFESSIONAL_MAX_FILE_SIZE': settings.PROFESSIONAL_MAX_FILE_SIZE}

def account_limits(request):
    return {'FREE_IMAGE_LIMIT': settings.FREE_IMAGE_LIMIT,
            'PREMIUM_IMAGE_LIMIT': settings.PREMIUM_IMAGE_LIMIT,
            'PROFESSIONAL_IMAGE_LIMIT': settings.PROFESSIONAL_IMAGE_LIMIT}
