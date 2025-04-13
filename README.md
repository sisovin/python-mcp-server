# Python MCP Server

The **python-mcp-server** project is a Flask-based web server designed to interact with Minecraft, likely as part of a larger system for managing Minecraft servers, plugins, or player data. Below’s a detailed overview:

---

### **Project Overview**
#### **Purpose**
- Acts as a **backend server** for Minecraft-related applications (e.g., user authentication, server management, or plugin integration).
- Provides a **web interface** (HTML/Jinja2 templates) and **API endpoints** (Flask routes) to interact with Minecraft services.

#### **Key Features**
1. **User Authentication**  
   - Login/logout functionality (likely for server admins or players).  
   - Uses Flask sessions or JWT (check `server/utils/auth.py`).  

2. **Database Integration**  
   - SQLAlchemy models (`server/database/models.py`) to store user data, server settings, or player stats.  
   - SQLite/PostgreSQL likely used (check `server/config.py`).  

3. **Web Interface**  
   - Serves HTML pages (e.g., `home.html`, `login.html`) with CSS/JS assets.  
   - Uses **Jinja2** templating for dynamic content.  

4. **API Endpoints**  
   - Flask routes (in `main.py` or separate blueprints) to handle:  
     - Player data fetching.  
     - Server commands (e.g., starting/stopping Minecraft instances).  

5. **Testing**  
   - Unit tests (`tests/`) for auth, database, and utilities.  

---

### **Technology Stack**
| Component       | Technology                |
|-----------------|---------------------------|
| Backend         | Python + Flask            |
| Database        | SQLAlchemy (SQLite/PostgreSQL) |
| Frontend        | HTML5, CSS3, JavaScript (vanilla) |
| Templating      | Jinja2                    |
| Testing         | pytest/unittest           |

---

### **Use Cases**
1. **Minecraft Server Dashboard**  
   - Admins can log in to monitor/manage servers via a web interface.  
2. **Player Stats Tracker**  
   - Stores and displays player achievements, ranks, etc.  
3. **Plugin Backend**  
   - Integrates with Minecraft plugins (e.g., for economy, permissions).  

---

### **How to Run**
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
2. Configure the server:  
   - Set secrets in `server/config.py`.  
3. Start the Flask app:  
   ```bash
   python server/main.py
   ```
4. Access the web interface at `http://localhost:5000`.

---

### **Missing Pieces (Likely Extended Elsewhere)**
- **Minecraft Plugin**: This repo is *only the server*; a Spigot/Bukkit plugin would communicate with it.  
- **Real-time Features**: No WebSocket/Socket.IO usage (would need Redis or similar for scaling).  
