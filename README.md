# ⌨️ Keystroke Dynamics Analyzer

A secure, ethical, and privacy-respecting cybersecurity research tool that analyzes keystroke dynamics - the unique timing patterns in how you type. This tool captures keystroke intervals, performs behavioral analysis, and generates comprehensive reports for security research, biometric authentication studies, and personal productivity insights.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## 🎯 Features

- **System-Wide Monitoring**: Captures keystrokes across all applications
- **Behavioral Biometrics**: Analyzes typing speed, rhythm, and consistency
- **Detailed Reports**: Generates JSON and HTML reports with visual statistics
- **Privacy-Focused**: Local storage only, full user control
- **Optional Notifications**: Telegram/Discord integration for remote monitoring
- **Ethical Design**: Explicit consent, transparent operation, easy to disable

## 🔐 Cybersecurity Applications

### Defensive Security
- **Biometric Authentication**: Use typing patterns as a behavioral identifier
- **Continuous Authentication**: Verify user identity throughout sessions
- **Anomaly Detection**: Identify unusual typing patterns indicating account compromise
- **Security Research**: Study keystroke dynamics for improved authentication systems

### Educational & Research
- **Ethical Hacking Education**: Understand keylogger functionality safely
- **Behavioral Analysis**: Research human-computer interaction patterns
- **Forensics Training**: Learn keystroke analysis techniques
- **Security Awareness**: Demonstrate attack vectors in controlled environments

## 📋 Requirements

- Python 3.7 or higher
- Windows, macOS, or Linux
- Administrator/root privileges (for system-wide keyboard monitoring)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/rhmujib/keystroke-dynamics.git
cd keystroke-dynamics-analyzer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Settings
Edit `config.json` to customize:
- Session duration
- Privacy settings (key logging on/off)
- Output paths
- Notification preferences

## 💻 Usage

### Basic Usage
```bash
python main.py
```

### Quick Test (30 seconds)
1. Run the tool
2. Type a sentence or two
3. Press **ESC** to stop early
4. Check `reports/` folder for your results

### Full Session
1. Run the tool
2. Work normally (type emails, code, documents, etc.)
3. Session automatically stops after configured time
4. View generated reports

## 📊 What It Analyzes

- **Typing Speed**: Words per minute (WPM)
- **Keystroke Intervals**: Time between key presses
- **Rhythm Consistency**: How steady your typing pattern is
- **Burst Detection**: Identifies rapid typing sequences
- **Statistical Metrics**: Mean, median, standard deviation of intervals

## 📁 Output Files

### JSON Report (`reports/keystroke_data.json`)
Contains raw data, complete analysis, and optionally captured text:
```json
{
  "metadata": {...},
  "analysis": {
    "typing_speed": 52.3,
    "total_keystrokes": 250,
    "avg_interval": 0.234
  },
  "typed_text": "...",
  "raw_data": [...]
}
```

### HTML Report (`reports/keystroke_report.html`)
Beautiful visual dashboard with:
- Statistics cards
- Typed text display
- Keystroke timing table
- Analysis summary

## ⚙️ Configuration

### Privacy Settings
```json
{
  "privacy": {
    "log_actual_keys": true,    // Record what keys are pressed
    "anonymize_data": false,     // Show full data in reports
    "save_typed_text": true      // Save complete typed text
  }
}
```

### Session Settings
```json
{
  "session": {
    "duration_minutes": 5,       // Session length
    "min_keystrokes": 20         // Minimum keys for analysis
  }
}
```

### Notifications (Optional)
```json
{
  "notifications": {
    "enabled": true,
    "telegram": {
      "bot_token": "YOUR_BOT_TOKEN",
      "chat_id": "YOUR_CHAT_ID"
    },
    "discord": {
      "webhook_url": "YOUR_WEBHOOK_URL"
    }
  }
}
```

## 🔒 Privacy & Ethics

### Ethical Use Guidelines
This tool is designed for:
- ✅ Personal typing analysis and improvement
- ✅ Authorized security research
- ✅ Educational demonstrations (with consent)
- ✅ Biometric authentication development

**DO NOT use for:**
- ❌ Unauthorized monitoring of others
- ❌ Privacy violations
- ❌ Malicious surveillance
- ❌ Data theft

### Privacy Features
- Explicit consent required before starting
- All data stored locally on your machine
- No automatic cloud uploads
- User has full control to stop anytime (ESC key)
- Easy deletion of all collected data
- Optional anonymization modes

## 🛡️ Security Considerations

### On macOS/Linux
You may need to grant accessibility permissions:
- **macOS**: System Preferences → Security & Privacy → Privacy → Accessibility
- **Linux**: May require running with `sudo`

### Antivirus Warnings
Some antivirus software may flag this tool as it uses keyboard monitoring APIs. This is a false positive - the source code is fully transparent and open for inspection.

## 📚 Project Structure

```
keystroke-dynamics-analyzer/
├── README.md
├── requirements.txt
├── config.json
├── main.py                    # Entry point
├── keystroke_logger.py        # Captures keystrokes
├── data_processor.py          # Statistical analysis
├── report_generator.py        # JSON/HTML reports
├── notification_handler.py    # Telegram/Discord
├── utils.py                   # Helper functions
└── reports/                   # Generated reports
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is intended for educational, research, and authorized security testing purposes only. Users are responsible for ensuring compliance with all applicable laws and regulations. Unauthorized monitoring of computer systems is illegal in many jurisdictions.

**USE RESPONSIBLY AND ETHICALLY.**

## 🐛 Troubleshooting

### Common Issues

**"No module named 'pynput'"**
```bash
pip install pynput
```

**Permission Denied (macOS/Linux)**
```bash
sudo python main.py
```

**Insufficient Data Error**
- Make sure to type at least 20 keystrokes before stopping

**Reports Not Generated**
- Check that the `reports/` directory exists
- Verify file permissions

## 📧 Contact

For questions, issues, or collaboration:
- Open an issue on GitHub
- Email: your.email@example.com

## 🌟 Acknowledgments

- Built with Python and pynput
- Inspired by behavioral biometrics research
- Created for ethical cybersecurity education

---

**Remember: With great power comes great responsibility. Use this tool ethically and legally.** 🔐