![Static Badge](https://img.shields.io/badge/release-v1.0-blue?style=flat)
![Static Badge](https://img.shields.io/badge/Windows-passing-brightgreen?style=flat&logo=Windows)
![Static Badge](https://img.shields.io/badge/Linux-passing-brightgreen?style=flat&logo=Linux)
![Static Badge](https://img.shields.io/badge/macOs-passing-brightgreen?style=flat&logo=macOs)
![Static Badge](https://img.shields.io/badge/License-GPL--3.0-orange?style=flat)

# KeyLogger-Python

This is a simple keylogger implemented in Python. Please note that this tool is intended for educational and research purposes only. **Do not use it for illegal activities :)**.

## Requirements

To use this keylogger, you need to install the `keyboard` package. You can install it using pip:

```
pip install keyboard
```

You will also need to create an app password if you use Gmail. You can have more information at this [link](https://support.google.com/accounts/answer/185833).
Remeber that you will have to enable 2FA.

## Keylogger Configuration Parameters

This script allows you to configure various parameters for the keylogger functionality.

### Keylogger Configuration

- **FILE_NAME**: Specifies the name of the output file where the keylogger logs will be saved.
- **TIME_INTERVAL**: The time interval (in seconds) for saving the keylogger file. Adjust it to save the file more or less frequently.
- **CLIENT_NAME**: Represents the name assigned to this device for identification within the keylogger system.
- **BLACKLIST**: List of keys that will not be saved by the keylogger.
- **SPECIAL_KEYS**: Mapping of special keys and their representations in the log file.

### Email Settings

- **SEND_BEFORE_EXIT**: Determines whether to send the file before exiting the program.
- **SEND_INTERVAL**: The time interval (in seconds) for sending the file via email. Set to 0 to disable sending based on time interval.
- **SEND_FILE_SIZE**: The maximum size (in bytes) of the file before sending it via email.
- **RESET_WHEN_SEND**: Specifies whether to reset the file after sending it.

### Email Service Configuration

- **EMAIL**: Email address that will receive the keylogger file.
- **EMAIL_SENDER**: Email address that will send the keylogger file. Leave blank to use the same email as the receiver.
- **EMAIL_SENDER_PASSWORD**: Password or app password for the email sender's account.

### Special configuration

- **EVENT_TYPE**: Specifies whether to save the key when it's pressed ("down") or released ("up").
- **SMTP_SERVER**: SMTP server address for sending emails.
- **SMTP_PORT**: Port number for the SMTP server.


Modify these parameters according to your requirements to customize the behavior of the keylogger.


## Disclaimer

**This project is intended for educational and research purposes only. The author does not condone any illegal use of this software. Be responsible and respect the privacy and rights of others.**
