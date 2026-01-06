from django_rq import job


@job
def deliver_certificate() -> None:
    print("Delivering certificate...")