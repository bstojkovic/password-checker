# password-checker
A simple Python script to check if a password has been pwned.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

password-checker is a simple and secure utility that checks if a password has been found in a known data breach using the [Have I Been Pwned](https://haveibeenpwned.com/) API (`api.pwnedpasswords.com`).

This tool helps users assess the security of their passwords and avoid using compromised credentials.

## Features

- Checks passwords against the Have I Been Pwned database by using their API
- API utilizes the [k-anonymity](https://en.wikipedia.org/wiki/K-anonymity) model to ensure password privacy
