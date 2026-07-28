#!/bin/bash

echo "🧪 Testing Kosan Chatbot..."

# 1. Test health endpoints
echo "📡 Testing health..."
curl -s http://localhost:5000/health | jq .
curl -s http://localhost:8080/health | jq .

# 2. Test complaint flow
echo "💬 Testing complaint submission..."
curl -X POST http://localhost:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "from": "test_user_001",
    "message": "Bang, AC di kamar 405 rusak nih, udah 3 hari ga dingin"
  }' | jq .

echo ""
echo "💬 Testing follow-up..."
curl -X POST http://localhost:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "from": "test_user_001",
    "message": "Iya, tolong segera diperbaiki ya Bang"
  }' | jq .

# 3. Test get complaints
echo "📋 Getting all complaints..."
curl -s http://localhost:8080/api/v1/complaints | jq .
