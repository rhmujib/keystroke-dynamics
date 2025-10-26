# Keystroke Dynamics Analyzer

A secure, ethical, and privacy-respecting tool that measures keystroke dynamics to generate meaningful insights.

## Features
- Keystroke timing analysis
- JSON and HTML report generation
- Optional Telegram/Discord notifications
- Privacy-focused design
- Ethical data collection

## Installation
```bash
pip install -r requirements.txt
```

## Configuration

Edit `config.json` to customize settings:
- Session duration
- Report output paths
- Notification settings (optional)

## Usage
```bash
python main.py
```

## Ethical Guidelines

This tool is designed for:
- Personal productivity analysis
- Research purposes (with consent)
- Educational demonstrations

**DO NOT use for:**
- Unauthorized monitoring
- Privacy violations
- Malicious purposes

## Privacy

- All data is stored locally
- No automatic cloud uploads
- User has full control over data
- Clear consent mechanisms

## License

MIT License - Use responsibly and ethically
```

---

## **File 2: requirements.txt**
```
pynput==1.7.6
requests==2.31.0
jinja2==3.1.2
numpy==1.24.3
matplotlib==3.7.1
pandas==2.0.2