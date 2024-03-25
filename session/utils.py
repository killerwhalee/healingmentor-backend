from session.models import Multiplyer


def calculate_score(user, time_input):
    """
    Calcuate score based on user's score multiplyer.
    
    """
    
    # Import MultiplyerData
    from django.core.exceptions import ObjectDoesNotExist

    try:
        mul_obj = Multiplyer.objects.get(user=user)
    except ObjectDoesNotExist:
        mul_obj = Multiplyer.objects.create(user=user)

    # Update Multiplyer date and amount
    from datetime import datetime, time, timedelta

    time_now = datetime.now()
    time_yesterday = time_now - timedelta(days=1)

    time_pivot_yd = datetime.combine(time_yesterday.date(), time(17, 0))
    time_pivot_am = datetime.combine(time_now.date(), time(5, 0))
    time_pivot_pm = datetime.combine(time_now.date(), time(17, 0))

    # Update daily multiplyer
    if time_now > time_pivot_pm and time_now != time_pivot_pm:
        mul_obj.daily_datetime = time_pivot_pm
        mul_obj.daily_tokens = 900
    elif time_now > time_pivot_am and time_now != time_pivot_am:
        mul_obj.daily_datetime = time_pivot_am
        mul_obj.daily_tokens = 900
    elif time_now != time_pivot_yd:
        mul_obj.daily_datetime = time_pivot_yd
        mul_obj.daily_tokens = 900

    # Update hourly multiplyer
    if time_now - mul_obj.hourly_datetime > timedelta(hours=1):
        mul_obj.hourly_datetime = time_now
        mul_obj.hourly_tokens = 300

    # Calculate multiplied score
    score = 0
    tokens_required = int(float(time_input))

    # Use hourly tokens
    tokens_used = min(tokens_required, mul_obj.hourly_tokens)
    score += tokens_used * (1 / 6) * 3
    tokens_required -= tokens_used
    mul_obj.hourly_tokens -= tokens_used

    # Use daily tokens
    tokens_used = min(tokens_required, mul_obj.daily_tokens)
    score += tokens_used * (1 / 6) * 3
    tokens_required -= tokens_used
    mul_obj.daily_tokens -= tokens_used

    # Add remainder
    score += tokens_required * (1 / 6)

    # Save multiplyer object
    mul_obj.save()

    # Return result score
    return score