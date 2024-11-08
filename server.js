const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// Veritabanı bağlantısı
const db = new sqlite3.Database("C:\\Users\\Aydan\\OneDrive\\Masaüstü\\sqlite\\sqlite.db", (err) => {
  if (err) {
    console.error("Veritabanına bağlanırken hata oluştu:", err.message);
  } else {
    console.log("Veritabanına başarıyla bağlandı.");
    db.run(`CREATE TABLE IF NOT EXISTS users (
      Id INTEGER PRIMARY KEY AUTOINCREMENT,
      Name TEXT,
      age INTEGER
    )`);
  }
});

// Tüm kullanıcıları getir
app.get("/api/users", (req, res) => {
  db.all("SELECT * FROM STUDENTS", [], (err, rows) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    res.json(rows);
  });
});

const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
