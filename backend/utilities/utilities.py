import mailtrap as mt
import os


def send_email(html, subject, to_email):
    """
    Envía un correo electrónico usando la API de Mailtrap.

    Args:
        html (str): Contenido HTML del correo
        subject (str): Asunto del correo
        to_email (str): Dirección de correo del destinatario
    """
    try:
        # Configurar el correo
        mail = mt.Mail(
            sender=mt.Address(
                email=f"noreply@{os.getenv('DOMAIN', 'example.com')}",
                name="RecetarioWeb"
            ),
            to=[mt.Address(email=to_email)],
            subject=subject,
            html=html,
        )

        # Crear cliente y enviar
        client = mt.MailtrapClient(token=os.getenv('MAILTRAP_API_TOKEN'))
        client.send(mail)

    except Exception as e:
        print(f"Error sending email: {e}")
