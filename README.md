
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

## Live Application

FitSlot is deployed on Render.

Live URL: PASTE_YOUR_REAL_RENDER_URL_HERE

Health Check: PASTE_YOUR_REAL_RENDER_URL_HERE/health

## CI/CD

GitHub Actions runs linting and automated tests,
verifies the build, and triggers Render deployment
after successful checks on main.