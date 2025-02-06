-- schema.sql

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    preferencias TEXT
);

CREATE TABLE actividades (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(50),
    pasos INTEGER,
    calorias FLOAT,
    distancia FLOAT,
    fecha TIMESTAMP DEFAULT NOW(),
    usuario_id INTEGER REFERENCES usuarios(id),
    CONSTRAINT unique_actividad UNIQUE (usuario_id, fecha)  -- 🔥 Restringe duplicados
);

CREATE TABLE salud (
    id SERIAL PRIMARY KEY,
    frecuencia_cardiaca FLOAT,
    calidad_sueno FLOAT,
    nivel_estres FLOAT,
    fecha TIMESTAMP DEFAULT NOW(),
    usuario_id INTEGER REFERENCES usuarios(id),
    CONSTRAINT unique_salud UNIQUE (usuario_id, fecha)  -- 🔥 Restringe duplicados
);


CREATE TABLE consultas (
    id SERIAL PRIMARY KEY,
    pregunta TEXT,
    respuesta TEXT,
    fecha TIMESTAMP DEFAULT NOW(),
    usuario_id INTEGER REFERENCES usuarios(id)
);
