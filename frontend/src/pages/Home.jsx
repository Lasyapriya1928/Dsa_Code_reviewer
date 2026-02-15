import React from "react";
import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  return (
    <div className="page-container">
      <h1 style={{
  fontSize: "56px",
  fontWeight: "700",
  marginBottom: "20px"
}}>
  AlgoScope
</h1>

<p style={{
  fontSize: "18px",
  color: "#A1A1AA",
  maxWidth: "600px",
  marginBottom: "30px"
}}>
  Analyze. Understand. Optimize.
</p>

      <p style={{ maxWidth: "700px", marginBottom: "40px" }}>
        Analyze algorithmic code using machine learning and receive structured,
        explainable feedback on efficiency, design patterns, and optimization.
      </p>

      <button
        className="primary-btn"
        onClick={() => navigate("/analyzer")}
      >
        Start Reviewing Code
      </button>

      <div style={{
        marginTop: "80px",
        display: "grid",
        gridTemplateColumns: "repeat(3, 1fr)",
        gap: "20px"
      }}>
        <div className="card">
          <h2>Efficiency Analysis</h2>
          <p>Predict time complexity classification using trained ML models.</p>
        </div>

        <div className="card">
          <h2>Pattern Detection</h2>
          <p>Identify algorithmic patterns such as stack, recursion, or two-pointer.</p>
        </div>

        <div className="card">
          <h2>Explainable Feedback</h2>
          <p>Understand why your solution was classified the way it was.</p>
        </div>
      </div>
    </div>
  );
}

export default Home;