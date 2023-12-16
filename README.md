
---

# Mailing

Welcome to the Mailing repository! This project focuses on creating and managing email drafts using the Gmail API. It's a Python-based application that simplifies the process of composing and saving drafts in your Gmail account.

## Features

- **Create Email Drafts**: Easily create email drafts with a subject, recipient, and body.
- **Gmail API Integration**: Uses the Gmail API to interact with your Gmail account.
- **Token-based Authentication**: Securely authenticates with your Google account to access Gmail services.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Google API client libraries

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/remmover/mailing.git
   ```
2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

### Configuration

- Set up your Google API credentials and download the `credentials.json` file.
- Place the `credentials.json` file in the root directory of the project.
- Create file `.env` and update the variables with your specific settings.

### Usage

To create a new email draft:

```python
from main import create_email_draft

create_email_draft('Subject', 'recipient@example.com', 'Email body text')
```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the [MIT License](LICENSE).

---
