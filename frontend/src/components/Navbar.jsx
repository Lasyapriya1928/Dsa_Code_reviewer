import React from "react";
import { Link, useLocation } from "react-router-dom";

function Navbar() {
  const location = useLocation();

  const linkStyle = (path) => ({
    marginLeft: "30px",
    textDecoration: "none",
    color: location.pathname === path ? "#ffffff" : "#9ca3af",
    fontSize: "14px",
    fontWeight: "500",
    transition: "0.2s ease"
  });

  return (
    <nav style={{
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      padding: "20px 60px",
      backgroundColor: "#111827",
      borderBottom: "1px solid #1f2937"
    }}>
      <div style={{
        fontSize: "16px",
        fontWeight: "600",
        letterSpacing: "0.5px"
      }}>
        DSA Code Reviewer
      </div>

      <div>
        <Link to="/" style={linkStyle("/")}>Home</Link>
        <Link to="/analyzer" style={linkStyle("/analyzer")}>Analyzer</Link>
        <Link to="/history" style={linkStyle("/history")}>History</Link>
        <Link to="/analytics" style={linkStyle("/analytics")}>Analytics</Link>
      </div>
    </nav>
  );
}

export default Navbar;