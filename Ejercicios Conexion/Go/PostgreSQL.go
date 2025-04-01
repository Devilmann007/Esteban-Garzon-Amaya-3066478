// Instalar paquete PostgreSQL para Go
// go get github.com/lib/pq
package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/lib/pq"
)

func main() {
	connStr := "host=localhost user=postgres password=Psql2025 dbname=postgres port=5432 sslmode=disable"
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatalf("❌ Error en PostgreSQL: %v", err)
	}
	defer db.Close()
	fmt.Println("✅ Conexión PostgreSQL exitosa")
}
