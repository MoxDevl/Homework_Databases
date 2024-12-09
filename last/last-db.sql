CREATE TABLE log(
    user_id TEXT,
    "time" TEXT NOT NULL,
    bet REAL,
    win REAL,
    PRIMARY KEY (
        user_id,
        "time"
    )
);

CREATE TABLE users(
    user_id TEXT PRIMARY KEY,
    email TEXT,
    geo TEXT
);