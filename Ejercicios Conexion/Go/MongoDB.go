// Instalar paquete MongoDB para Go
// go get go.mongodb.org/mongo-driver/mongo
// go get go.mongodb.org/mongo-driver/bson

package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

func main() {
	// Configurar contexto con timeout
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	// Conectar a MongoDB
	client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://localhost:27017"))
	if err != nil {
		log.Fatal("❌ Error de conexión:", err)
	}
	defer client.Disconnect(ctx)

	fmt.Println("✅ Conexión exitosa")
	fmt.Printf("🔎 Tipo de objeto de conexión: %T\n", client)

	// Listar bases de datos
	databases, err := client.ListDatabaseNames(ctx, bson.M{})
	if err != nil {
		log.Fatal("❌ Error al listar bases de datos:", err)
	}
	fmt.Println("📁 Bases de datos disponibles:", databases)

	// Acceder a la base de datos y colección
	db := client.Database("ecommerce3066478")
	collection := db.Collection("Clientes1")

	// Documento a insertar
	documento := bson.D{
		{Key: "Nombre", Value: "Fernanda"},
		{Key: "Correo", Value: "fernanda.lopez@example.com"},
		{Key: "Telefono", Value: "3129876543"},
		{Key: "Direccion", Value: "Calle 45 #67-89"},
		{Key: "Creado_desde", Value: "Go"},
	}
	

	// Insertar documento
	resultado, err := collection.InsertOne(ctx, documento)
	if err != nil {
		log.Fatal("❌ Error al insertar documento:", err)
	}
	fmt.Printf("📌 Documento insertado con ID: %v\n", resultado.InsertedID)

	fmt.Println("❗ Conexión cerrada")
}