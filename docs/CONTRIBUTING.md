# 🤝 Contributing to Invisibility Cloak

First off, thank you for considering contributing to this project! 🎉

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Screenshots/videos** if applicable
- **Environment details** (OS, Python version, OpenCV version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Include:

- **Clear description** of the enhancement
- **Use case** - why is this useful?
- **Possible implementation** approach

### Pull Requests

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development Setup


# Clone your fork
git clone https://github.com/ehsanaiverse/invisibility-cloak.git
cd invisibility-cloak

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest tests/


## Code Style

- Follow PEP 8
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

## Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and PRs

Example:
```
Add multi-color support for cloak detection

- Implement color selection UI
- Update HSV ranges dynamically
- Add tests for color detection

Closes #123
```

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community

## Questions?

Feel free to open an issue or reach out to the maintainers!

Thank you for contributing! 🚀
```