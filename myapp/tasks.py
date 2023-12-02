from celery import shared_task



@shared_task
def clear_session_cache(id):
    print(f"Session Cache Cleared: {id}")
    return id