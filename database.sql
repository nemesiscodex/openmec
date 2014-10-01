BEGIN;
CREATE TABLE "openmec_objetogasto" (
    "codigo" varchar(30) NOT NULL PRIMARY KEY,
    "nombre" varchar(128) NOT NULL
)
;
CREATE TABLE "openmec_dependencia" (
    "codigo" varchar(30) NOT NULL PRIMARY KEY,
    "institucion" varchar(128) NOT NULL
)
;
CREATE TABLE "openmec_cargo" (
    "codigo" varchar(30) NOT NULL PRIMARY KEY,
    "cargo" varchar(128) NOT NULL
)
;
CREATE TABLE "openmec_rubro" (
    "codigo" varchar(30) NOT NULL PRIMARY KEY,
    "monto" integer NOT NULL
)
;
CREATE TABLE "openmec_concepto" (
    "codigo" varchar(30) NOT NULL PRIMARY KEY,
    "concepto" varchar(128) NOT NULL,
    "minimo" integer NOT NULL,
    "maximo" integer NOT NULL,
    "promedio" real NOT NULL
)
;
CREATE TABLE "openmec_funcionario" (
    "documento" integer NOT NULL PRIMARY KEY,
    "funcionario" varchar(128) NOT NULL,
    "nro_matriculacion" integer NOT NULL UNIQUE
)
;
CREATE TABLE "openmec_datos" (
    "id" integer NOT NULL PRIMARY KEY,
    "mes" integer NOT NULL,
    "anio" integer NOT NULL,
    "funcionario_id" integer NOT NULL REFERENCES "openmec_funcionario" ("documento"),
    "estado" varchar(30) NOT NULL,
    "objeto_gasto_id" varchar(30) NOT NULL REFERENCES "openmec_objetogasto" ("codigo"),
    "concepto_id" varchar(30) NOT NULL REFERENCES "openmec_concepto" ("codigo"),
    "dependencia_id" varchar(30) NOT NULL REFERENCES "openmec_dependencia" ("codigo"),
    "cargo_id" varchar(30) NOT NULL REFERENCES "openmec_cargo" ("codigo"),
    "rubro_id" varchar(30) NOT NULL REFERENCES "openmec_rubro" ("codigo")
)
;
CREATE INDEX "openmec_datos_22ee2d5e" ON "openmec_datos" ("funcionario_id");
CREATE INDEX "openmec_datos_b6c7fb3f" ON "openmec_datos" ("objeto_gasto_id");
CREATE INDEX "openmec_datos_f24bbc8a" ON "openmec_datos" ("concepto_id");
CREATE INDEX "openmec_datos_987e3449" ON "openmec_datos" ("dependencia_id");
CREATE INDEX "openmec_datos_7b821f35" ON "openmec_datos" ("cargo_id");
CREATE INDEX "openmec_datos_9c7df5dd" ON "openmec_datos" ("rubro_id");

COMMIT;