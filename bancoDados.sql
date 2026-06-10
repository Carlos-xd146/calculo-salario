CREATE TABLE
    IF NOT EXISTS ponto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        _data DATE,
        horas FLOAT
    );

INSERT INTO ponto (_data,horas)
VALUES
    ('20-05-2026', 10.5),
    ('21-05-2026', 8),
    ('22-05-2026', 9.5),
    ('23-05-2026', 12),
    ('24-05-2026', 11);

