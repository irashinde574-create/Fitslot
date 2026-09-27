
# FitSlot - Gym & Sports Slot Booking System

## Problem Statement
FitSlot allows students to view and reserve gym and sports
facility slots while preventing duplicate bookings.

## Features
- Dynamic booking form
- Gym, badminton and basketball facilities
- Duplicate slot validation
- JSON bookings API
- Health check endpoint

## Technology Stack
Python, Flask, HTML, CSS, pytest, flake8,
GitHub Actions and Render.

## Run Locally
pip install -r requirements.txt
python app.py

Open http://localhost:5000

## Routes
- / : Booking dashboard
- /book : Create a booking
- /api/bookings : View booking data
- /health : Application health status

## CI/CD
GitHub Actions runs lint, tests and deployment
steps when code is pushed.
