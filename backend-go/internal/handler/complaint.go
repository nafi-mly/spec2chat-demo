package handler

import (
	"kosan-chatbot/backend/internal/domain"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

func SubmitComplaint(c *gin.Context) {
	var req domain.ComplaintRequest

	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	// Mock response - nanti diganti dengan logic real
	response := domain.ComplaintResponse{
		TicketID: int(time.Now().Unix()) % 10000,
		Status:   "CREATED",
		Message:  "Complaint submitted successfully",
	}

	c.JSON(http.StatusOK, response)
}

func GetComplaints(c *gin.Context) {
	// Mock data
	complaints := []map[string]interface{}{
		{
			"ticket_id": 1001,
			"room":      "405",
			"issue":     "AC rusak",
			"status":    "PENDING",
		},
		{
			"ticket_id": 1002,
			"room":      "302",
			"issue":     "Air mati",
			"status":    "COMPLETED",
		},
	}
	c.JSON(http.StatusOK, complaints)
}
