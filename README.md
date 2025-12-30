# Dead Code Detector (Basic)

A lightweight static analysis tool that spots "unreachable code" appearing immediately after `return`, `throw`, `break`, or `continue` statements in Python, JavaScript, and Java.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Logic Based**: Checks for statements that immediately follow a control-flow exit at the same indentation level.
*   **Multi-Language**: Works with indentation-sensitive (Python) and brace-style languages (JS/Java/C++).
*   **Zero Dependencies**: Pure Python implementation.

## Usage

```bash
python run_detector.py [path]
```

### Examples

**1. Scan Project**
```bash
python run_detector.py src/
```

**2. Detects**
```javascript
function demo() {
  return true;
  console.log("I am dead"); // <--- Flagged
}
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
