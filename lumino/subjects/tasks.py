from django_rq import job
from weasyprint import HTML
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from subjects.models import Enrollment


@job
def deliver_certificate(base_url, student) -> None:
    enrollments = Enrollment.objects.filter(student=student)
    
    html_content = render_to_string(
        'subjects/subject/certificate_pdf.html',
        {
            'student': student,
            'enrollments': enrollments,
        }
    )

    HTML(string=html_content, base_url=base_url).write_pdf(f'media/certificates/{student.username}_grade_certificate.pdf')
    
    email = EmailMessage(
        subject='Grade Certificate',
        body=f'<h3>Hello {student.first_name} here is your grade certificate.</h3>',
        to=[f'{student.email}'],
    )
    email.content_subtype = 'html'
    email.attach_file(f'media/certificates/{student.username}_grade_certificate.pdf')
    email.send()