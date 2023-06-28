CREATE TABLE recepcionista (
  id          NUMBER(4) PRIMARY KEY,
  nombre      VARCHAR2(30) NOT NULL,
  contraseña  VARCHAR2(30)
);

CREATE TABLE cliente (
  rut          VARCHAR2(15) PRIMARY KEY,
  nombre       VARCHAR2(30) NOT NULL,
  fono         VARCHAR2(10),
  gmail        VARCHAR2(30),
  acompañantes NUMBER(3)
);

CREATE TABLE habitacion (
  numero      NUMBER(4) PRIMARY KEY,
  nombre      VARCHAR2(30) NOT NULL,
  descripcion VARCHAR2(50)
);
CREATE TABLE pago (
  id       NUMBER(4) PRIMARY KEY,
  total    VARCHAR2(30) NOT NULL,
  fecha    DATE,
  id_fk    NUMBER(4)
);

CREATE TABLE reserva (
  id        NUMBER(4) PRIMARY KEY,
  estado    CHAR,
  rut_fk    VARCHAR2(15),
  numero_fk NUMBER(4),
  id_fk     NUMBER(4),
  FOREIGN KEY(rut_fk) REFERENCES cliente(rut),
  FOREIGN KEY(numero_fk) REFERENCES habitacion(numero),
  FOREIGN KEY(id_fk) REFERENCES pago(id)
);
