DSA Code Reviewer

DSA Code Reviewer is a full-stack web application that analyzes Data Structures and Algorithms (DSA) code and evaluates its efficiency using machine learning and static code analysis. The system extracts structural features such as loop depth and algorithm patterns, including Dynamic Programming and Two Pointers, to classify solutions as efficient, suboptimal, or inefficient. It also provides insights such as algorithm efficiency classification, loop complexity, and code structure analytics through an interactive dashboard.

Overview
The DSA Code Reviewer is designed to help developers and students evaluate the quality and efficiency of their algorithm implementations. Users can submit their code solutions, which are then analyzed by a backend machine learning model.
Based on extracted code features, the model classifies the solution as efficient, suboptimal, or inefficient.
The platform also provides visual analytics and performance insights, allowing users to better understand their coding patterns and improve the efficiency of their algorithms.

Features
Code Analysis
The application accepts user-submitted DSA code and performs structural analysis. It extracts key features from the code, including:
Loop depth
Code patterns
Structural complexity
Machine Learning Based Evaluation
The backend machine learning model evaluates the extracted features and predicts the efficiency level of the submitted code.
Possible classifications include:
Efficient
Suboptimal
Inefficient

The model is trained on code features derived from algorithm implementations.

Analytics Dashboard
The platform provides an analytics dashboard that offers visual insights into analyzed code submissions. The dashboard includes:
Distribution of efficiency classifications
Analysis of algorithm usage patterns
Visual summaries of submitted solutions
Secure Authentication

The application includes a secure authentication system with:
JWT-based authentication
Secure password hashing using Passlib
Deployment Ready Architecture

The project is designed with a scalable architecture and includes:
A FastAPI backend for API services
A React-based frontend for user interaction
RESTful API communication between frontend and backend

Technology Stack
Frontend
React
Axios
Recharts for analytics visualization
Vercel for deployment
Backend
FastAPI
Python
JWT Authentication
Passlib for password hashing
Machine Learning
Scikit-learn
Feature extraction from code structure
Trained model stored as a .pkl file
Database
SQLite
Deployment
Vercel for frontend deployment
Render for backend deployment

System Architecture
User
↓
Frontend (React)
↓
FastAPI Backend
  • Code Feature Extraction
  • Machine Learning Model (.pkl)
  • Authentication (JWT)
↓
Database (SQLite)

Example Output
Example result returned after analyzing a submitted solution:
Code Analysis Result
Loop Depth: 2
Detected Pattern: Nested Loops
Predicted Efficiency: Inefficient
Confidence Score: 0.87

Installation
1. Clone the Repository
git clone https://github.com/your-username/dsa-code-reviewer.git
cd dsa-code-reviewer
2. Backend Setup

Navigate to the backend directory and install the required dependencies.
cd backend
pip install -r requirements.txt

Run the FastAPI server:
uvicorn main:app --reload
The backend server will run at:
http://localhost:8000

3. Frontend Setup
Navigate to the frontend directory and install the required dependencies.
cd frontend
npm install
npm start

The frontend will run at:
http://localhost:3000
Deployment

Frontend
The frontend is deployed using Vercel.

Backend
The backend is deployed using Render.

Future Improvements
Potential enhancements for the project include:
Automatic time complexity detection
Support for additional algorithm pattern recognition such as:
Sliding Window
Greedy Algorithms
Graph Algorithms
Backtracking
Code optimization suggestions for improving inefficient solutions
Leaderboard for efficient solutions and user submissions
Support for multiple programming languages

Contributing
Contributions are welcome. If you would like to improve the project, feel free to open an issue or submit a pull request.

License
This project is open source and available under the MIT License.

Author
Lasya Priya Nellutla