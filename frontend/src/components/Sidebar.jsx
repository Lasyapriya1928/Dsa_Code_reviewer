import React, { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

function Sidebar() {
  const location = useLocation();
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);

  const navItems = [
    { name: "Home", path: "/" },
    { name: "Editor", path: "/analyzer" },
    { name: "History", path: "/history" },
    { name: "Analytics", path: "/analytics" },
  ];

  const getLinkClass = (path) =>
    `sidebar-link ${location.pathname === path ? "active" : ""}`;

  const username = localStorage.getItem("username") || "User";
  const firstLetter = username.charAt(0).toUpperCase();

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("username");
    navigate("/login");
  };

  return (
    <div className="sidebar" style={{ display: "flex", flexDirection: "column" }}>

      {/* Logo */}
      <div className="sidebar-logo">
        AlgoScope
      </div>

      {/* Navigation */}
      <div className="sidebar-nav">
        {navItems.map((item) => (
          <Link
            key={item.name}
            to={item.path}
            className={getLinkClass(item.path)}
          >
            {item.name}
          </Link>
        ))}
      </div>

      {/* Push account section to bottom */}
      <div style={{ marginTop: "auto", padding: "20px", borderTop: "1px solid #1F2937" }}>
        
        <div
          onClick={() => setOpen(!open)}
          style={{
            display: "flex",
            alignItems: "center",
            gap: "12px",
            cursor: "pointer"
          }}
        >
          {/* Avatar Circle */}
          <div
            style={{
              width: "36px",
              height: "36px",
              borderRadius: "50%",
              background: "#3B82F6",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontWeight: "600",
              color: "white"
            }}
          >
            {firstLetter}
          </div>

          <div style={{ fontSize: "14px" }}>
            {username}
          </div>
        </div>

        {/* Dropdown */}
        {open && (
          <div
            style={{
              marginTop: "12px",
              background: "#111827",
              border: "1px solid #1F2937",
              borderRadius: "8px",
              padding: "12px"
            }}
          >
            <div style={{ fontSize: "13px", marginBottom: "10px" }}>
              <strong>User:</strong><br />
              {username}
            </div>

            <div
              onClick={handleLogout}
              style={{
                color: "#EF4444",
                cursor: "pointer",
                fontSize: "13px"
              }}
            >
              Logout
            </div>
          </div>
        )}
      </div>

    </div>
  );
}

export default Sidebar;