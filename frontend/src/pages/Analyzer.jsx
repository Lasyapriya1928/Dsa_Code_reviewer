import React, { useState } from "react";
import Editor from "@monaco-editor/react";
import { motion } from "framer-motion";

function Analyzer() {

  const [code, setCode] = useState("");
  const [result, setResult] = useState(null);
  const [problemName, setProblemName] = useState("");
  const [loading, setLoading] = useState(false);

  const analyze = async (shouldSave) => {

    if (!problemName.trim()) {
      alert("Enter Problem Name");
      return;
    }

    if (!code.trim()) {
      alert("Enter Python Code");
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      const token = localStorage.getItem("token");

      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
          code,
          problem_name: problemName,
          save: shouldSave
        })
      });

      if (response.status === 401) {
        alert("Session expired. Please login again.");
        localStorage.removeItem("token");
        window.location.href = "/";
        return;
      }

      const data = await response.json();
      setResult(data);

    } catch (error) {
      console.error("Error:", error);
    }

    setLoading(false);
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "100%" }}>

      {/* Header */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "flex-end",
          marginBottom: "24px",
        }}
      >
        <div>
          <div style={{ fontSize: "22px", fontWeight: "600" }}>
            Python Analysis Engine
          </div>

          <div style={{ fontSize: "13px", color: "#A1A1AA" }}>
            Analyze algorithmic efficiency and patterns
          </div>

          <input
            type="text"
            placeholder="Enter Problem Name"
            value={problemName}
            onChange={(e) => setProblemName(e.target.value)}
            style={{
              marginTop: "12px",
              padding: "8px 12px",
              borderRadius: "6px",
              border: "1px solid #222",
              background: "#111",
              color: "white",
              width: "260px"
            }}
          />
        </div>

        {/* Buttons */}
        <div style={{ display: "flex", gap: "12px" }}>
          <button
            className="secondary-btn"
            onClick={() => analyze(false)}
            disabled={loading}
          >
            {loading ? "Analyzing..." : "Analyze"}
          </button>

          <button
            className="primary-btn"
            onClick={() => analyze(true)}
            disabled={loading}
          >
            {loading ? "Saving..." : "Save"}
          </button>
        </div>
      </div>

      {/* Main Layout */}
      <div style={{ display: "flex", flex: 1, gap: "20px" }}>

        {/* Monaco Editor */}
        <div
          style={{
            flex: 2,
            border: "1px solid #222",
            borderRadius: "8px",
            overflow: "hidden",
          }}
        >
          <Editor
            height="100%"
            defaultLanguage="python"
            theme="vs-dark"
            value={code}
            onChange={(value) => setCode(value || "")}
          />
        </div>

        {/* Results Panel */}
        <div style={{ flex: 1 }}>
          <div className="card" style={{ height: "100%" }}>

            {!result && !loading && (
              <div style={{ color: "#A1A1AA" }}>
                Run analysis to view results.
              </div>
            )}

            {loading && (
              <div style={{ color: "#A1A1AA" }}>
                Processing...
              </div>
            )}

            {result && !result.error && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.25 }}
              >

                <div style={{ marginBottom: "18px" }}>
                  <div style={{ fontSize: "12px", color: "#A1A1AA" }}>
                    Efficiency
                  </div>
                  <div style={{ fontWeight: "600", color: "#3B82F6" }}>
                    {result.predicted_efficiency}
                  </div>
                </div>

                <div style={{ marginBottom: "18px" }}>
                  <div style={{ fontSize: "12px", color: "#A1A1AA" }}>
                    Pattern
                  </div>
                  <div>
                    {result.predicted_pattern}
                  </div>
                </div>

                <div>
                  <div style={{ fontSize: "12px", color: "#A1A1AA" }}>
                    Explanation
                  </div>

                  <ul style={{ paddingLeft: "18px" }}>
                    {Array.isArray(result.explanation) &&
                      result.explanation.map((e, i) => (
                        <li key={i}>{e}</li>
                      ))}
                  </ul>
                </div>

              </motion.div>
            )}

            {result && result.error && (
              <div style={{ color: "red" }}>
                {result.error}
              </div>
            )}

          </div>
        </div>

      </div>
    </div>
  );
}

export default Analyzer;