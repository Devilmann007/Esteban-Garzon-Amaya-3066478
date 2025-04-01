

package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	// Configuración de conexión a MySQL
	dsn := "root:@tcp(localhost:3306)/ecommerce3066478"
	db, err := sql.Open("mysql", dsn)
	if err != nil {
		log.Fatalf("\u274C Error al conectar con MySQL: %v", err)
	}
	defer db.Close()

	// Verificar si la conexión es válida
	err = db.Ping()
	if err != nil {
		log.Fatalf("\u274C No se pudo establecer conexión: %v", err)
	}

	fmt.Println("\u2705 Conexión exitosa")
	fmt.Printf("\U0001F50E Tipo de objeto de conexión: %T\n", db)

	// Ejecutar la consulta para listar las bases de datos
	rows, err := db.Query("SHOW DATABASES;")
	if err != nil {
		log.Fatalf("\u274C Error al obtener bases de datos: %v", err)
	}
	defer rows.Close()

	// Imprimir bases de datos disponibles
	fmt.Println("\U0001F4C1 Bases de datos disponibles:")
	for rows.Next() {
		var dbName string
		if err := rows.Scan(&dbName); err != nil {
			log.Fatalf("\u274C Error al leer resultado: %v", err)
		}
		fmt.Printf("📌 %s\n", dbName)
	}

	// Verificar errores en la iteración
	if err := rows.Err(); err != nil {
		log.Fatalf("\u274C Error en la iteración: %v", err)
	}

	fmt.Println("\u2757 Conexión cerrada")
}
