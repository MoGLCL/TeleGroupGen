<div align="center">

# 🤖 TeleGroupGen 🤖

**A Python script to automate Telegram group creation and messaging using GitHub Actions.**

</div>

<p align="center">
  <!-- Links updated for MoGLCL/TeleGroupGen -->
  <a href="https://github.com/MoGLCL/TeleGroupGen/actions/workflows/main.yml"><img src="https://github.com/MoGLCL/TeleGroupGen/actions/workflows/main.yml/badge.svg" alt="GitHub Actions Status"></a>
  <a href="https://www.python.org/downloads/release/python-380/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version"></a>
  <a href="https://github.com/MoGLCL/TeleGroupGen/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style: Black"></a>
  <a href="#"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
</p>

---

<details>
<summary><strong>Table of Contents</strong></summary>

- [✨ Key Features](#-key-features)
- [📝 Prerequisites](#-prerequisites)
- [🚀 Setup and Deployment](#-setup-and-deployment)
- [🛠️ Usage](#️-usage)
- [🔧 Customization](#-customization)
- [⚠️ Disclaimer](#️-disclaimer)

</details>

---

## ✨ Key Features

-   **🤖 Automatic Group Creation**: Creates a specified number of groups with custom names.
-   **✉️ Randomized Messaging**: Sends a random selection of predefined messages to each new group.
-   **🕒 Fully Automated**: Runs on a schedule with GitHub Actions for a "set it and forget it" experience.
-   **⚙️ Easy to Customize**: Cleanly structured to let you easily change script parameters.

## 📝 Prerequisites

-   A Telegram account.
-   Python 3.8 or higher.
-   Your **API_ID** and **API_HASH** from [my.telegram.org](https://my.telegram.org).

## 🚀 Setup and Deployment

Follow these steps carefully to get the automation running.

### 1. Fork & Clone the Repository
- **Fork** this repository to your own GitHub account.
- **Clone** your forked repository to your local machine:
  ```bash
  git clone [https://github.com/MoGLCL/TeleGroupGen.git](https://github.com/MoGLCL/TeleGroupGen.git)
  cd TeleGroupGen
  ```

### 2. Install Dependencies
- Install the required Python libraries:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Generate Session String
- To run on GitHub Actions, you need a session string to avoid manual logins.
<details>
<summary>Click here for steps to generate the session string</summary>

- Create a file named `generate_session.py` and add this code:
    ```python
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession

    print("--- Session String Generator ---")
    API_ID = int(input("Enter your API ID: "))
    API_HASH = input("Enter your API HASH: ")

    with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        session_string = client.session.save()
        print("\n✅ Your session string has been generated successfully! ✅\n")
        print(session_string)
        print("\nCopy this string and add it to your GitHub Secrets.")
    ```
- Run the script: `python generate_session.py`.
- You will be prompted for your credentials. After logging in, a long string will be printed. **Copy this string.**
</details>

### 4. Configure GitHub Secrets
- In your forked repository, navigate to `Settings` > `Secrets and variables` > `Actions`.
- Click `New repository secret` and add the following:
  -   `API_ID`: Your API ID.
  -   `API_HASH`: Your API Hash.
  -   `SESSION_STRING`: The session string you generated in the previous step.

## 🛠️ Usage

### Automatic Execution (GitHub Actions)
The workflow is pre-configured to run on a schedule (check the `.github/workflows/main.yml` file). You can also trigger it manually from the **Actions** tab in your GitHub repository.

### Manual Execution
To run the script locally:
```bash
python main.py
```
*(Note: Local execution relies on the same environment variables or direct authentication).*

## 🔧 Customization

Open `main.py` to easily configure the script's behavior:

-   **`NUM_GROUPS`**: Set the number of groups to create per run.
-   **`GROUP_NAME_PREFIX`**: Define the base name for the new groups.
-   **`MESSAGES`**: Edit the list of messages to be sent randomly.
-   **`USER_TO_ADD`**: **(Required)** Set the username of a user to add to each group (e.g., `'@username'`). Telegram's API requires adding at least one member.

## ⚠️ Disclaimer

> **Important:** Automating actions on any platform, including Telegram, carries risks. Misuse of this script for spamming or other malicious activities can lead to your Telegram account being limited or permanently banned.
>
> - Use this script responsibly and at your own risk.
> - This project is intended for educational or personal administrative purposes only.
