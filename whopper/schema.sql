DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS drawing;

CREATE TABLE user (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   username TEXT UNIQUE NOT NULL,
   password TEXT NOT NULL,
   gold INTEGER DEFAULT 0
);

CREATE TABLE ticket (
   ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
   user_id INTEGER NOT NULL,
   date_obtained TEXT NOT NULL,
   numbers TEXT NOT NULL,
   redeemed INTEGER DEFAULT 0,
   winnings REAL DEFAULT 0,
   matches INTEGER
);

CREATE TABLE drawing (
   draw_id INTEGER PRIMARY KEY AUTOINCREMENT,
   draw_date TEXT NOT NULL,
   winning_nums TEXT NOT NULL,
   jackpot INTEGER NOT NULL,
   second_prize INTEGER NOT NULL,
   third_prize INTEGER NOT NULL
);