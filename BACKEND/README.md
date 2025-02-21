# LARO-App Backend

## 🖥️ Project Overview
LARO is a basketball matchmaking app that connects players to teams and games. This repository contains the **backend** services responsible for handling user authentication, game invitations, matchmaking, and team management.

## ⚙️ Features
- User authentication and authorization (JWT-based)
- Game and team management APIs
- Invitation system with QR code and link generation
- Secure handling of user data
- RESTful API architecture

## 🛠️ Tech Stack
- **Language:** Node.js (Express.js)
- **Database:** MongoDB
- **Authentication:** JWT & OAuth2
- **Version Control:** Git & GitHub
- **API Documentation:** Swagger

## 📦 Installation
### Prerequisites
- [Node.js](https://nodejs.org/) installed
- [MongoDB](https://www.mongodb.com/) instance (local or cloud via MongoDB Atlas)
- Git installed

### Steps
1. **Clone the repository:**  
   `git clone https://github.com/EjLaquiorez/LARO-App-Backend.git`

2. **Navigate to the project directory:**  
   `cd LARO-App-Backend`

3. **Install dependencies:**  
   `npm install`

4. **Create `.env` file:**  
   ```env
   PORT=5000
   MONGODB_URI=your_mongo_connection_string
   JWT_SECRET=your_secret_key
   ```

5. **Run the server:**  
   `npm run dev`

> 🟢 Server will run on `http://localhost:5000/` by default.

## 📂 Project Structure
```
src/
├── controllers/       # API logic
├── models/            # MongoDB models
├── routes/            # API routes
├── middleware/        # Authentication & error handling
├── utils/             # Helper functions
└── app.js             # Express app setup
```

## 📖 API Documentation
- Swagger documentation available at: `http://localhost:5000/api-docs`
- Sample endpoints:
  - `POST /api/auth/login` – User login
  - `POST /api/games/create` – Create a game invitation
  - `GET /api/teams` – Fetch teams

## 🤝 Contribution Guidelines
1. **Fork** the repo.
2. Create your **feature branch:** `git checkout -b feature/YourFeature`
3. **Commit changes:** `git commit -m 'Add YourFeature'`
4. **Push to branch:** `git push origin feature/YourFeature`
5. **Create a Pull Request** for review.

> ✨ Follow best practices: write clean, modular, and documented code.

## 📝 Commit Message Format
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Other maintenance tasks

## 🛡️ Security
- Store sensitive data in environment variables.
- Run code audits before deployment.

## 📃 License
Licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🙌 Team
Backend developed by the 11-member LARO team from Palawan State University. Contact [ejlqrz@gmail.com] for support.

---
🚀 *Building seamless basketball connections with LARO!* 🏀

