-- ****************************************************
--  BASE DE DATOS: escuela
--  Tablas: alumno y materia (5 campos cada una)
--  Ejecutar en phpMyAdmin -> pestaña SQL -> Continuar
-- ****************************************************

CREATE DATABASE IF NOT EXISTS escuela;
USE escuela;

-- OJO: borra las tablas viejas (la de clase solo tenia 2 campos y datos repetidos)
DROP TABLE IF EXISTS alumno;
DROP TABLE IF EXISTS materia;

-- ===== TABLA ALUMNO (5 campos) =====
CREATE TABLE alumno (
    id_alumno       VARCHAR(15)  NOT NULL PRIMARY KEY,   -- cedula
    nombre_alumno   VARCHAR(50)  NOT NULL,
    apellido_alumno VARCHAR(50)  NOT NULL,
    edad_alumno     INT          NOT NULL,
    correo_alumno   VARCHAR(80)  NOT NULL
);

-- ===== TABLA MATERIA (5 campos) =====
CREATE TABLE materia (
    id_materia       VARCHAR(10) NOT NULL PRIMARY KEY,   -- codigo
    nombre_materia   VARCHAR(60) NOT NULL,
    profesor_materia VARCHAR(60) NOT NULL,
    creditos_materia INT         NOT NULL,
    horario_materia  VARCHAR(40) NOT NULL
);

-- ===== DATOS DE EJEMPLO =====
INSERT INTO alumno (id_alumno, nombre_alumno, apellido_alumno, edad_alumno, correo_alumno) VALUES
('1127044901', 'nelson',  'perez',     20, 'nelson@correo.com'),
('1110324411', 'luisa',   'gomez',     19, 'luisa@correo.com'),
('836654321',  'juanito', 'rodriguez', 18, 'juanito@correo.com');

INSERT INTO materia (id_materia, nombre_materia, profesor_materia, creditos_materia, horario_materia) VALUES
('MAT101', 'Matematicas',   'Carlos Ruiz',  4, 'Lunes 7:00-9:00'),
('PRO201', 'Programacion',  'Ana Torres',   5, 'Martes 14:00-17:00'),
('BDD301', 'Base de datos', 'Jorge Silva',  4, 'Miercoles 10:00-12:00');


-- ****************************************************
--  "JUGAR CON EL RUN DEL SQL" (probar una por una)
-- ****************************************************
-- SELECT * FROM alumno;
-- SELECT * FROM materia;
-- SELECT nombre_alumno, edad_alumno FROM alumno WHERE edad_alumno >= 19;
-- SELECT * FROM alumno ORDER BY apellido_alumno ASC;
-- SELECT COUNT(*) AS total_alumnos FROM alumno;
-- SELECT * FROM materia WHERE creditos_materia > 4;
-- SELECT * FROM alumno WHERE nombre_alumno LIKE 'l%';
-- UPDATE alumno SET edad_alumno = 21 WHERE id_alumno = '1127044901';
-- DELETE FROM materia WHERE id_materia = 'MAT101';
