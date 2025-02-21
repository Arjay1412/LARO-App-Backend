# 🏀 **LARO App**
> *Find basketball teams and organize games effortlessly.*

---

## 📖 **Table of Contents**
- [🚀 Project Overview](#-project-overview)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [🌳 Branching Strategy](#-branching-strategy)
- [✍️ Commit Message Guidelines](#️-commit-message-guidelines)
- [🔄 Contribution Workflow](#-contribution-workflow)
- [✅ Pull Request Process](#-pull-request-process)
- [📅 Project Management](#-project-management)
- [📢 Contact & Support](#-contact--support)
- [📄 License](#-license)

---

## 🚀 **Project Overview**
**LARO** is a matchmaking app designed to connect basketball players and teams, making it easy to schedule and organize games. Key features include:
- Team creation and management.
- Game invites with date, time, location, and type.
- Invite sharing via links or QR codes.
- Player profiles and match history.

---

## 🛠️ **Tech Stack**
- **Frontend:** Flutter 🐦
- **Version Control:** GitHub 🗂️
- **Collaboration:** GitHub Projects & Issues 📋

---

## 📂 **Project Structure**
```plaintext
LARO-App/
├── lib/
│   ├── screens/          # App screens (home, invite, profile, etc.)
│   ├── widgets/          # Reusable components
│   ├── models/           # Data models (User, Game, Team)
│   ├── services/         # API and data handling
│   └── main.dart         # App entry point
├── assets/               # Images, fonts, and other resources
├── pubspec.yaml          # Dependencies and configurations
└── README.md             # Project documentation
```

---

## 🌳 **Branching Strategy**
We follow the **Git Flow** methodology for organized collaboration.

### 🗂️ **Main Branches:**
- `main`: Production-ready code *(No direct commits allowed)*
- `develop`: Latest stable development code *(Merge feature branches here)*

### 🛠️ **Supporting Branches:**
| Branch Type | Naming Convention          | Purpose                      |
|-------------|----------------------------|------------------------------|
| Feature     | `feature/<feature-name>`    | New features                 |
| Bugfix      | `bugfix/<bug-description>`  | Fixes for non-critical bugs  |
| Hotfix      | `hotfix/<hotfix-description>`| Urgent fixes on production  |
| Release     | `release/<version>`         | Preparing for a new release  |

#### 📌 **Examples:**
- `feature/invite-interface` - Adding invite functionalities.
- `bugfix/fix-invite-link` - Fixing broken invite link generation.
- `hotfix/crash-on-launch` - Urgent fix for app crashes.
- `release/v1.0.0` - Release branch for version 1.0.0.

---

## ✍️ **Commit Message Guidelines**
Keep commits **clear, concise, and descriptive** using the following convention:
```plaintext
<type>(<scope>): <short description>

[Optional body with detailed explanation, if necessary]
```

### ✅ **Commit Types:**
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation updates
- `style`: Code style changes (no logic changes)
- `refactor`: Code restructuring without functional changes
- `test`: Adding or modifying tests
- `chore`: Minor updates (build process, dependencies)

### 📝 **Examples:**
- `feat(invite): add date and location fields to invite interface`
- `fix(qr-code): correct QR code generation bug`
- `docs(readme): update contribution guidelines`
- `style(invite-screen): reformat layout for better readability`
- `chore(deps): update Flutter to 3.10.0`

---

## 🔄 **Contribution Workflow**
Follow these steps to contribute effectively:

### 1️⃣ **Clone the Repository:**
```bash
git clone https://github.com/LARO-App-Team/LARO-App.git
cd LARO-App
```

### 2️⃣ **Create a Branch:**
```bash
git checkout -b feature/invite-interface
```
> **Note:** Always branch off from `develop`.

### 3️⃣ **Make Changes:**
- Write clean and modular code.
- Add comments where necessary for clarity.
- Keep commits focused on one change at a time.

### 4️⃣ **Commit Your Changes:**
```bash
git add .
git commit -m "feat(invite): implement invite interface with date and time"
```
> 🔑 **Tip:** Write meaningful commit messages and avoid generic ones like `update` or `fix`.

### 5️⃣ **Push to Remote:**
```bash
git push origin feature/invite-interface
```

---

## ✅ **Pull Request Process**
### 🔀 **Creating a Pull Request:**
1. Navigate to the repository on GitHub.
2. Click **Compare & pull request** for your branch.
3. Fill out the PR template:
   - **Title:** `feat(invite): implement invite interface`
   - **Description:** Outline changes, reasoning, and test instructions.
   - **Linked Issues:** Reference related issues (e.g., `Closes #12`).
4. Set **base branch:** `develop` and **compare branch:** `feature/invite-interface`.

### 🧪 **Review Process:**
- At least **2 approvals** required.
- Reviewers should:
  - Check code readability and efficiency.
  - Verify functionality.
  - Suggest improvements if needed.

### 🏗️ **Merging:**
- Use **Squash and Merge** to keep commit history clean.
- Delete the feature branch after merging.

---

## 📅 **Project Management**
- Track progress using **GitHub Projects**.
- Use **Issues** for bugs and feature requests with appropriate labels:
  - `enhancement`, `bug`, `help wanted`, `question`
- Assign tasks to team members and set clear deadlines.

---

## 📢 **Contact & Support**
For questions or suggestions, open an [Issue](https://github.com/LARO-App-Team/LARO-App/issues) or contact the team via the designated communication channel.

---

## 📄 **License**
This project is licensed under the [MIT License](LICENSE).
