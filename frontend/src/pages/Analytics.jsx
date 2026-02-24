import React, { useEffect, useState } from "react";

function Analytics() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("https://dsa-code-reviewer.onrender.com/analytics")
      .then(res => res.json())
      .then(resData => setData(resData))
      .catch(err => console.error("Error fetching analytics:", err));
  }, []);

  if (!data) {
    return (
      <div style={{ padding: "40px", color: "#e5e7eb" }}>
        <h2>Analytics Dashboard</h2>
        <p>Loading analytics...</p>
      </div>
    );
  }

  const total = data.total_submissions;

  const patternEntries = Object.entries(data.pattern_distribution);
  const efficiencyEntries = Object.entries(data.efficiency_distribution);

  const mostPattern =
    [...patternEntries].sort((a, b) => b[1] - a[1])[0]?.[0] || "N/A";

  const mostEfficiency =
    [...efficiencyEntries].sort((a, b) => b[1] - a[1])[0]?.[0] || "N/A";

  const renderBar = (label, value, color) => {
    const percent = ((value / total) * 100).toFixed(0);

    return (
      <div style={{ marginBottom: "18px" }}>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginBottom: "6px"
          }}
        >
          <span>{label}</span>
          <span>{value} ({percent}%)</span>
        </div>

        <div
          style={{
            background: "#1f2937",
            height: "8px",
            borderRadius: "6px",
            overflow: "hidden"
          }}
        >
          <div
            style={{
              width: `${percent}%`,
              background: color,
              height: "100%",
              borderRadius: "6px",
              transition: "0.4s ease"
            }}
          />
        </div>
      </div>
    );
  };

  return (
    <div style={{ padding: "40px", color: "#e5e7eb" }}>
      <h2 style={{ marginBottom: "30px" }}>Analytics Dashboard</h2>

      {/* Summary Cards */}
      <div
        style={{
          display: "flex",
          gap: "20px",
          flexWrap: "wrap",
          marginBottom: "50px"
        }}
      >
        <div className="card">
          <h3>Total Submissions</h3>
          <p>{data.total_submissions}</p>
        </div>

        <div className="card">
          <h3>Unique Problems</h3>
          <p>{data.unique_problems}</p>
        </div>

        <div className="card">
          <h3>Most Used Pattern</h3>
          <p>{mostPattern}</p>
        </div>

        <div className="card">
          <h3>Most Common Efficiency</h3>
          <p>{mostEfficiency}</p>
        </div>
      </div>

      {/* Two Columns */}
      <div
        style={{
          display: "flex",
          gap: "60px",
          flexWrap: "wrap"
        }}
      >
        {/* Pattern Section */}
        <div style={{ flex: 1, minWidth: "350px" }}>
          <h3 style={{ marginBottom: "20px" }}>Pattern Distribution</h3>
          {patternEntries.map(([label, value], index) =>
            renderBar(
              label,
              value,
              ["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#06b6d4"][index % 6]
            )
          )}
        </div>

        {/* Efficiency Section */}
        <div style={{ flex: 1, minWidth: "350px" }}>
          <h3 style={{ marginBottom: "20px" }}>Efficiency Distribution</h3>
          {efficiencyEntries.map(([label, value], index) =>
            renderBar(
              label,
              value,
              ["#10b981", "#f59e0b", "#ef4444"][index % 3]
            )
          )}
        </div>
      </div>
    </div>
  );
}

export default Analytics;