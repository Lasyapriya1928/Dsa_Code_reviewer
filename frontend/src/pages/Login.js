import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    if (!username || !password) {
      alert("Enter username and password");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          username,
          password
        })
      });

      const data = await response.json();

      if (response.status !== 200) {
        alert(data.detail || "Login failed");
        return;
      }

      localStorage.setItem("token", data.access_token);
      localStorage.setItem("username", username);

      navigate("/");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div style={styles.wrapper}>
      <div style={styles.card}>
        <div style={styles.logo}>AlgoScope</div>

        <h2 style={styles.title}>Welcome back</h2>

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={styles.input}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={styles.input}
        />

        <button style={styles.button} onClick={handleLogin}>
          Sign In
        </button>

        <p style={styles.footerText}>
          Don’t have an account?{" "}
          <span
            style={styles.link}
            onClick={() => navigate("/register")}
          >
            Register
          </span>
        </p>
      </div>
    </div>
  );
}

const styles = {
  wrapper: {
  position: "fixed",
  inset: 0,
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  background: "#0A0A0A"
},
  card: {
    width: "400px",
    padding: "45px",
    background: "#111111",
    borderRadius: "14px",
    border: "1px solid #1F2937",
    boxShadow: "0 10px 30px rgba(0,0,0,0.6)",
  },
  logo: {
    fontSize: "18px",
    fontWeight: "600",
    marginBottom: "30px",
    textAlign: "center",
    color: "white"
  },
  title: {
    marginBottom: "25px",
    fontWeight: "500",
    fontSize: "20px"
  },
  input: {
    width: "100%",
    padding: "14px",
    marginBottom: "18px",
    borderRadius: "8px",
    border: "1px solid #2A2A2A",
    background: "#0F0F0F",
    color: "white",
    fontSize: "14px",
    outline: "none"
  },
  button: {
    width: "100%",
    padding: "14px",
    borderRadius: "8px",
    border: "none",
    background: "#2563EB",
    color: "white",
    fontWeight: "500",
    cursor: "pointer",
    marginTop: "10px"
  },
  footerText: {
    marginTop: "20px",
    fontSize: "13px",
    color: "#9CA3AF",
    textAlign: "center"
  },
  link: {
    color: "#2563EB",
    cursor: "pointer"
  }
};

export default Login;