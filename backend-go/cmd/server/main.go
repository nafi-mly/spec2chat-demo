package main

import (
	"kosan-chatbot/backend/internal/handler"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	// Health check
	r.GET("/health", func(c *gin.Context) {
		c.JSON(200, gin.H{"status": "ok"})
	})

	// API routes
	api := r.Group("/api/v1")
	{
		api.POST("/complaints", handler.SubmitComplaint)
		api.GET("/complaints", handler.GetComplaints)
	}

	r.Run(":8080") // Listen on port 8080
}
