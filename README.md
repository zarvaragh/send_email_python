# send_email_python

Send HTML and attachment emails from Python using Gmail SMTP with TLS encryption.

## Requirements

```bash
pip install secure-smtplib  # stdlib smtplib is included in Python
```

No external packages needed — uses Python's built-in `smtplib`, `email`, and `ssl` modules.

## Setup

Gmail requires an **App Password** (not your regular account password):

1. Enable 2-Factor Authentication on your Google account
2. Go to **Google Account → Security → App Passwords**
3. Generate a password for "Mail" → copy it
4. Paste it as `SENDER_PASSWORD` in the script

## Usage

```python
SENDER_EMAIL = "you@gmail.com"
SENDER_PASSWORD = "your_16_char_app_password"
RECEIVER_EMAIL = "recipient@example.com"
```

Run:
```bash
python email.py
```

## How it works

- Connects to `smtp.gmail.com:587`
- Upgrades to TLS via `STARTTLS` with a secure SSL context
- Attaches an image (`imgName.jpg`) alongside the text body