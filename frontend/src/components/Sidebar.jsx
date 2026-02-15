import React from "react";
import { Link, useLocation } from "react-router-dom";

function Sidebar() {
  const location = useLocation();

  const navItems = [
    { name: "Home", path: "/" },
    { name: "Editor", path: "/analyzer" },
    { name: "History", path: "/history" },
    { name: "Analytics", path: "/analytics" },
  ];

  const getLinkClass = (path) =>
    `sidebar-link ${location.pathname === path ? "active" : ""}`;

  return (
    <div className="sidebar">
      {/* Logo / Product Name */}
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
    </div>
  );
}

export default Sidebar;