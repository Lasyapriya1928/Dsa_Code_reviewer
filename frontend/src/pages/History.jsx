import React, { useEffect, useState } from "react";

function History() {
  const [submissions, setSubmissions] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const token = localStorage.getItem("token");

        const response = await fetch("http://127.0.0.1:8000/history", {
          headers: {
            "Authorization": `Bearer ${token}`
          }
        });

        // 🔐 If unauthorized
        if (response.status === 401) {
          alert("Session expired. Please login again.");
          localStorage.removeItem("token");
          window.location.href = "/";
          return;
        }

        const data = await response.json();

        // 🛡 Safety check
        if (Array.isArray(data)) {
          setSubmissions(data);
        } else {
          setSubmissions([]);
        }

      } catch (err) {
        console.error(err);
      }
    };

    fetchHistory();
  }, []);

  const formatDate = (iso) => {
    return new Date(iso).toLocaleString("en-IN", {
      dateStyle: "medium",
      timeStyle: "short"
    });
  };

  return (
    <div style={{ padding: "40px" }}>

      {/* Header */}
      <div style={{ marginBottom: "30px" }}>
        <h2 style={{ marginBottom: "6px" }}>Submission History</h2>
        <div style={{ color: "#9CA3AF", fontSize: "14px" }}>
          Review your previous algorithm analyses
        </div>
      </div>

      {/* Table Card */}
      <div
        style={{
          background: "#111111",
          borderRadius: "10px",
          border: "1px solid #1F2937",
          padding: "20px"
        }}
      >
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr style={{ textAlign: "left", color: "#9CA3AF" }}>
              <th style={{ paddingBottom: "14px" }}>Problem</th>
              <th>Efficiency</th>
              <th>Pattern</th>
              <th>Saved On</th>
            </tr>
          </thead>

          <tbody>
            {Array.isArray(submissions) && submissions.map((item) => (
              <tr
                key={item.id}
                onClick={() => setSelected(item)}
                style={{
                  cursor: "pointer",
                  borderTop: "1px solid #1F2937",
                  transition: "background 0.2s ease"
                }}
                onMouseEnter={(e) =>
                  (e.currentTarget.style.background = "#1A1A1A")
                }
                onMouseLeave={(e) =>
                  (e.currentTarget.style.background = "transparent")
                }
              >
                <td style={{ padding: "14px 0", fontWeight: "500" }}>
                  {item.problem_name}
                </td>

                <td style={{ color: "#3B82F6", fontWeight: "500" }}>
                  {item.predicted_efficiency}
                </td>

                <td style={{ color: "#D1D5DB" }}>
                  {item.predicted_pattern || "—"}
                </td>

                <td style={{ color: "#9CA3AF", fontSize: "14px" }}>
                  {formatDate(item.timestamp)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {/* If no submissions */}
        {Array.isArray(submissions) && submissions.length === 0 && (
          <div style={{ marginTop: "20px", color: "#9CA3AF" }}>
            No submissions yet.
          </div>
        )}
      </div>

      {/* Code Preview Section */}
      {selected && (
        <div
          style={{
            marginTop: "40px",
            background: "#0B0F19",
            borderRadius: "10px",
            border: "1px solid #1F2937",
            padding: "25px"
          }}
        >
          <div
            style={{
              marginBottom: "18px",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center"
            }}
          >
            <div>
              <div style={{ fontSize: "16px", fontWeight: "600" }}>
                {selected.problem_name}
              </div>
              <div style={{ fontSize: "13px", color: "#9CA3AF" }}>
                {formatDate(selected.timestamp)}
              </div>
            </div>

            <button
              onClick={() => setSelected(null)}
              style={{
                background: "transparent",
                border: "1px solid #374151",
                padding: "6px 12px",
                borderRadius: "6px",
                color: "#D1D5DB",
                cursor: "pointer"
              }}
            >
              Close
            </button>
          </div>

          <pre
            style={{
              background: "#111827",
              padding: "20px",
              borderRadius: "8px",
              overflowX: "auto",
              fontSize: "14px",
              lineHeight: "1.6",
              color: "#E5E7EB"
            }}
          >
            {selected.code}
          </pre>
        </div>
      )}
    </div>
  );
}

export default History;