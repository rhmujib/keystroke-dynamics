"""
Report Generator - Creates JSON and HTML reports
"""

import json
from jinja2 import Template
from datetime import datetime
import os

class ReportGenerator:
    def __init__(self, config):
        self.config = config
    
    def generate_json(self, keystroke_data, analysis, typed_text=""):
        """Generate JSON report"""
        report = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'tool_version': '1.0.0',
                'privacy_settings': self.config['privacy']
            },
            'analysis': analysis,
            'raw_data': keystroke_data if not self.config['privacy']['anonymize_data'] else []
        }
        
        # Add typed text if enabled
        if self.config['privacy']['save_typed_text'] and typed_text:
            report['typed_text'] = typed_text
        
        output_path = self.config['output']['json_path']
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        return output_path
    
    def generate_html(self, keystroke_data, analysis, typed_text=""):
        """Generate HTML report"""
        
        # Prepare keystroke table data
        keystroke_table_html = ""
        if self.config['privacy']['log_actual_keys'] and keystroke_data:
            keystroke_table_html = self._generate_keystroke_table(keystroke_data[:50])  # First 50
        
        # Prepare typed text section
        typed_text_html = ""
        if self.config['privacy']['save_typed_text'] and typed_text:
            typed_text_html = f"""
            <div class="section">
                <h2>📝 Typed Text</h2>
                <div class="typed-text-box">
                    <pre>{self._escape_html(typed_text)}</pre>
                </div>
            </div>
            """
        
        template = Template('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keystroke Dynamics Report</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        h1 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 1.1em;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }
        .stat-label {
            font-size: 0.9em;
            opacity: 0.9;
            margin-bottom: 5px;
        }
        .stat-value {
            font-size: 2em;
            font-weight: bold;
        }
        .section {
            margin: 30px 0;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
        }
        .section h2 {
            color: #667eea;
            margin-bottom: 15px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background: #667eea;
            color: white;
        }
        tr:hover {
            background: #f0f0f0;
        }
        .typed-text-box {
            background: #2d3748;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 10px;
            max-height: 400px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.6;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .typed-text-box pre {
            margin: 0;
        }
        .key-display {
            font-family: 'Courier New', monospace;
            background: #e8eaf6;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.9em;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #666;
            font-size: 0.9em;
        }
        .warning-box {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
        .warning-box strong {
            color: #856404;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⌨️ Keystroke Dynamics Report</h1>
        <p class="subtitle">Generated on {{ timestamp }}</p>
        
        {% if privacy_warning %}
        <div class="warning-box">
            <strong>⚠️ Privacy Notice:</strong> This report contains actual keystroke data. 
            Keep it secure and delete when no longer needed.
        </div>
        {% endif %}
        
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Total Keystrokes</div>
                <div class="stat-value">{{ analysis.total_keystrokes }}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Typing Speed</div>
                <div class="stat-value">{{ "%.1f"|format(analysis.typing_speed) }} WPM</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Avg Interval</div>
                <div class="stat-value">{{ "%.3f"|format(analysis.avg_interval) }}s</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Session Duration</div>
                <div class="stat-value">{{ "%.1f"|format(analysis.session_duration) }}s</div>
            </div>
        </div>
        
        {{ typed_text_section|safe }}
        
        <div class="section">
            <h2>📊 Statistical Analysis</h2>
            <table>
                <tr>
                    <th>Metric</th>
                    <th>Value</th>
                </tr>
                <tr>
                    <td>Median Interval</td>
                    <td>{{ "%.3f"|format(analysis.median_interval) }} seconds</td>
                </tr>
                <tr>
                    <td>Standard Deviation</td>
                    <td>{{ "%.3f"|format(analysis.std_interval) }}</td>
                </tr>
                <tr>
                    <td>Min Interval</td>
                    <td>{{ "%.3f"|format(analysis.min_interval) }} seconds</td>
                </tr>
                <tr>
                    <td>Max Interval</td>
                    <td>{{ "%.3f"|format(analysis.max_interval) }} seconds</td>
                </tr>
                <tr>
                    <td>Rhythm Consistency</td>
                    <td>{{ "%.2f"|format(analysis.rhythm_consistency * 100) }}%</td>
                </tr>
                <tr>
                    <td>Burst Typing Detected</td>
                    <td>{{ "Yes" if analysis.burst_typing_detected else "No" }}</td>
                </tr>
            </table>
        </div>
        
        {{ keystroke_table|safe }}
        
        <div class="footer">
            <p>🔒 Privacy-Respecting | ⚖️ Ethical Use Only | 📈 Data Stored Locally</p>
        </div>
    </div>
</body>
</html>
        ''')
        
        html_content = template.render(
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            analysis=analysis,
            typed_text_section=typed_text_html,
            keystroke_table=keystroke_table_html,
            privacy_warning=self.config['privacy']['log_actual_keys']
        )
        
        output_path = self.config['output']['html_path']
        with open(output_path, 'w') as f:
            f.write(html_content)
        
        return output_path
    
    def _generate_keystroke_table(self, keystroke_data):
        """Generate HTML table of keystrokes"""
        rows = ""
        for i, ks in enumerate(keystroke_data, 1):
            key_display = ks.get('readable_key', ks.get('key', 'N/A'))
            rows += f"""
            <tr>
                <td>{i}</td>
                <td><span class="key-display">{self._escape_html(key_display)}</span></td>
                <td>{ks['interval']:.3f}s</td>
                <td>{ks['elapsed_time']:.2f}s</td>
            </tr>
            """
        
        return f"""
        <div class="section">
            <h2>🔑 Keystroke Details (First 50)</h2>
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Key</th>
                        <th>Interval</th>
                        <th>Elapsed Time</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
        """
    
    def _escape_html(self, text):
        """Escape HTML special characters"""
        return (str(text)
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))