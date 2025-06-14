# Trash Alert App
Authors **(Universidad De Medellin)** with their respective GitHub profile: 
- Lenin Ospina (https://github.com/SkynetProyect)
- Luis Miguel Giraldo (https://github.com/hurluis)
- Jhon Edison Guerra (https://github.com/JhonEdisonG)
- Sebastian Tamayo Avendaño (https://github.com/SebastianT454)

## Overview
This project implements a web application inspired by an APK originally developed and deployed in India. Its goal is to provide a fast, 
effective communication channel between community members and local sanitation authorities to report and manage garbage accumulations in the city. 
Users (any individual in the city) can capture a photo of waste accumulation, add a brief description, and send a report. Registered sanitation workers (role: “collectors”) 
can view incoming reports and prioritize pickups based on an automated ranking determined by the backend.

## Features
- User Reporting
- Collector Dashboard
- Automated Priority Determination

## Backend
It was built using an Four-Layer Architecture with the next components Python with Flask to create APIs RESTful. It stores data in Supabase using PostgreSQL, 
and sends images to an AI service (Gemini) to determine a priority score for garbage collection.

## Frontend
Built with native HTML, CSS, and JavaScript, the frontend lets users upload photos and descriptions of waste sites and lets collectors view and manage reports. It calls the backend’s REST endpoints to submit reports, 
fetch prioritized lists, and update statuses, etc.
