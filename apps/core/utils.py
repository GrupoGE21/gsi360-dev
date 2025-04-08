def generate_incremental_code(model_class, order_field='created_at', prefix=None):
    last = model_class.objects.order_by(f'-{order_field}').first()
    if not last or not last.code:
        next_number = 1
    else:
        try:
            number_part = last.code
            if prefix:
                number_part = number_part.replace(prefix, '')
            next_number = int(number_part) + 1
        except (ValueError, AttributeError):
            next_number = 1
    return f"{prefix}{next_number:04d}" if prefix else f"{next_number:04d}"