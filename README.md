# KleeNet Discord Bot

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Branch: Beta](https://img.shields.io/badge/Branch-Beta-yellow)](https://github.com/LuxObsidian/Discord-KleeNet/tree/beta)

---

## **Overview**
KleeNet is a fun Discord bot that interacts with a specific user (`@Kleemann`) while keeping server interactions controlled.  
All fun commands can be triggered by anyone, but they **only respond if the target user is present**.

The bot is designed for safe development using a **Beta branch workflow** before merging changes into Main.

---

## **Features**

- **Fun commands for `@Kleemann`:**
  - `/klee` – playful greeting  
  - `/zahlen` – humorous donation reminder  
  - `/geruch` – funny warning about proximity  

- **Cooldown system:**  
  - Individual cooldowns per command to prevent spam  

- **Secure logging:**  
  - Command usage and errors logged locally  
  - Logs readable only by the bot user  

- **Modular structure:**  
  - Commands in separate files automatically loaded from `commands` folder  

---

## **Installation**

1. **Clone the repository:**

```bash
git clone https://github.com/LuxObsidian/Discord-KleeNet.git
cd Discord-KleeNet