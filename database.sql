BEGIN;
	CREATE TABLE "openmec_objetogasto" (
		    "codigo" varchar(30) NOT NULL PRIMARY KEY,
		    "nombre" varchar(128) NOT NULL
	)
	;
	CREATE TABLE "openmec_datos_dependencia" (
		    "id" integer NOT NULL PRIMARY KEY,
		    "datos_id" integer NOT NULL,
		    "dependencia_id" varchar(30) NOT NULL,
		    UNIQUE ("datos_id", "dependencia_id")
	)
	;
	CREATE TABLE "openmec_datos_cargo" (
		    "id" integer NOT NULL PRIMARY KEY,
		    "datos_id" integer NOT NULL,
		    "cargo_id" varchar(30) NOT NULL,
		    UNIQUE ("datos_id", "cargo_id")
	)
	;
	CREATE TABLE "openmec_datos_concepto" (
		    "id" integer NOT NULL PRIMARY KEY,
		    "datos_id" integer NOT NULL,
		    "concepto_id" varchar(30) NOT NULL,
		    UNIQUE ("datos_id", "concepto_id")
	)
	;
	CREATE TABLE "openmec_datos_funcionario" (
		    "id" integer NOT NULL PRIMARY KEY,
		    "datos_id" integer NOT NULL,
		    "funcionario_id" integer NOT NULL,
		    UNIQUE ("datos_id", "funcionario_id")
	)
	;
	CREATE TABLE "openmec_datos_rubro" (
		    "id" integer NOT NULL PRIMARY KEY,
		    "datos_id" integer NOT NULL,
		    "rubro_id" varchar(30) NOT NULL,
		    UNIQUE ("datos_id", "rubro_id")
	)
	;
	CREATE TABLE "openmec_datos_objeto_gasto" (
		    "id" integer NOT NULL PRIMARY KEY,
		    "datos_id" integer NOT NULL,
		    "objetogasto_id" varchar(30) NOT NULL REFERENCES "openmec_objetogasto" ("codigo"),
		    UNIQUE ("datos_id", "objetogasto_id")
	)
	;
	CREATE TABLE "openmec_datos" (
		    "id" integer NOT NULL PRIMARY KEY,
		    "mes" integer NOT NULL,
		    "anio" integer NOT NULL,
		    "estado" varchar(30) NOT NULL
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
	CREATE INDEX "openmec_datos_dependencia_21907e4e" ON "openmec_datos_dependencia" ("datos_id");
	CREATE INDEX "openmec_datos_dependencia_987e3449" ON "openmec_datos_dependencia" ("dependencia_id");
	CREATE INDEX "openmec_datos_cargo_21907e4e" ON "openmec_datos_cargo" ("datos_id");
	CREATE INDEX "openmec_datos_cargo_7b821f35" ON "openmec_datos_cargo" ("cargo_id");
	CREATE INDEX "openmec_datos_concepto_21907e4e" ON "openmec_datos_concepto" ("datos_id");
	CREATE INDEX "openmec_datos_concepto_f24bbc8a" ON "openmec_datos_concepto" ("concepto_id");
	CREATE INDEX "openmec_datos_funcionario_21907e4e" ON "openmec_datos_funcionario" ("datos_id");
	CREATE INDEX "openmec_datos_funcionario_22ee2d5e" ON "openmec_datos_funcionario" ("funcionario_id");
	CREATE INDEX "openmec_datos_rubro_21907e4e" ON "openmec_datos_rubro" ("datos_id");
	CREATE INDEX "openmec_datos_rubro_9c7df5dd" ON "openmec_datos_rubro" ("rubro_id");
	CREATE INDEX "openmec_datos_objeto_gasto_21907e4e" ON "openmec_datos_objeto_gasto" ("datos_id");
	CREATE INDEX "openmec_datos_objeto_gasto_3e7d1bcf" ON "openmec_datos_objeto_gasto" ("objetogasto_id");

	COMMIT;
