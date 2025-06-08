# Security Policy

## ⚠️ Important Security Notice

BlenderMCP executes arbitrary Python code within Blender. This poses significant security risks:

1. **No Authentication**: Currently, the server accepts connections without authentication
2. **Code Execution**: Any connected client can execute Python code in Blender
3. **Local Network Exposure**: The addon listens on all interfaces (0.0.0.0)

## Recommended Security Measures

### For Production Use
- **DO NOT** expose the Blender port (9876) to the internet
- Use firewall rules to restrict access to trusted IPs only
- Run in isolated environments or containers
- Monitor for suspicious activity

### Planned Security Improvements
- [ ] Authentication token support (v0.3.0)
- [ ] Connection whitelist/blacklist
- [ ] Code execution sandboxing
- [ ] Rate limiting
- [ ] Audit logging

## Reporting Security Vulnerabilities

Please report security vulnerabilities by:
1. **DO NOT** create public issues for security problems
2. Email: yukitsuroka@users.noreply.github.com
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fixes (if any)

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.2.x   | :white_check_mark: |
| < 0.2   | :x:                |

## Known Security Issues

1. **Unauthenticated RCE**: Any process on the local machine can connect and execute code
   - Mitigation: Use firewall rules, run in isolated environment
   - Fix planned: v0.3.0

2. **No Input Sanitization**: Python code is executed as-is
   - Mitigation: Only use with trusted AI clients
   - Fix planned: Future version