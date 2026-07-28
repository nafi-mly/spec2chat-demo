package domain

type ComplaintRequest struct {
	RoomNumber  string `json:"room_number" binding:"required"`
	IssueType   string `json:"issue_type" binding:"required"`
	Description string `json:"description" binding:"required"`
}

type ComplaintResponse struct {
	TicketID int    `json:"ticket_id"`
	Status   string `json:"status"`
	Message  string `json:"message"`
}
