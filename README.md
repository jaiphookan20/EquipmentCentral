# EquipmentCentral

EquipmentCentral is a centralized platform that connects equipment hirers with rental operators across Australia, making equipment rental discovery and comparison simple and efficient.

## Overview

EquipmentCentral bridges the gap between equipment hirers and rental operators, with a special focus on increasing visibility for small and medium-sized rental businesses. The platform offers comprehensive search capabilities, detailed equipment listings, and streamlined quote request management.

## Tech Stack

### Frontend
- React 18
- Vite
- TailwindCSS
- Modern JavaScript (ES6+)

### Backend
- Flask (Python)
- PostgreSQL with PostGIS for location-based queries
- Redis for session management and caching
- Gunicorn for production deployment

## Key Value Propositions:

For Hirers: Simplify discovery of equipment rentals by location, type, brand, and price.

For Operators (especially SMEs): Increase visibility, compete equitably with larger players, and gain an additional sales channel.

2. Problem Statement
Hirers' Pain Points:
Difficulty finding local equipment rental operators due to SEO dominance by large players.

Time-consuming process to compare prices, terms, and availability across multiple platforms.

Lack of granular search/filtering capabilities for specific equipment needs.

Operators' Pain Points:
Limited online visibility for small/mom-and-pop rental businesses.

Inability to efficiently market equipment inventory and pricing.

Manual processes for handling quote requests.

4. Core Features & Functionality
4.1. Hirer-Facing Features
a. Search & Filter Interface

Search by Suburb/Postcode: Display all operators within a selected radius (default: 10km, 25km, 50km).

Granular Equipment Filters:

Equipment Type (e.g., excavators, generators, scaffolding).

Equipment Subtype (e.g., mini-excavators, diesel generators).

Brand, Model, Year, and Condition (new/used).

Rental Price Range (daily/weekly rates).

Operator Ratings/Reviews.

Map Integration: Visualize operator locations and equipment availability.

b. Operator & Equipment Listings

Operator Profile:

Business name, contact details, operating hours, service areas.

List of available equipment with images, descriptions, rental rates, and terms (e.g., minimum hire period, deposits).

Customer reviews and ratings.

Equipment Details:

Specifications (e.g., weight, power output, dimensions).

Availability status (updated manually by operators).

c. Request for Quote (RFQ) System

Hirers can submit RFQs for specific equipment, specifying:

Hire duration.

Delivery/pickup preferences.

Custom requirements (e.g., attachments, insurance).

Operators receive RFQs via email/platform notifications and respond directly.

Hirers manage all RFQs in a centralized dashboard.

d. Notifications & Alerts

Notify hirers when a requested equipment becomes available.

Reminders for pending RFQ responses.

4.2. Operator-Facing Features
a. Equipment Inventory Management

Dashboard: Upload/update equipment listings (manual entry or CSV upload).

Fields: Name, type, brand, model, description, images, rental rates, terms.

Availability Calendar: Mark dates when equipment is unavailable.

b. RFQ Management

View and respond to RFQs via the platform.

Track RFQ status (pending, accepted, declined).

c. Profile Management

Customize business profile (logo, description, service areas).

Highlight promotions or seasonal offers.

4.3. Admin Panel Features
User Management: Approve/reject operator registrations.

Content Moderation: Review equipment listings for accuracy.

Analytics Dashboard: Track metrics like user engagement, RFQ conversion rates, and operator performance.

System Configuration: Manage pricing tiers (if subscription-based), radius settings, and SEO rules.

5. Non-Functional Requirements
Performance:

Search results load within <2 seconds for 10,000+ concurrent users.

Security:

GDPR/APPA compliance for user data.

Secure payment gateway integration (future phase).

Scalability:

Cloud-based architecture to handle regional expansion.

Usability:

Mobile-responsive design.

Intuitive UI for non-tech-savvy operators.

Reliability:

99.9% uptime SLA.

6. User Stories & Scenarios
Hirer Story:
“As a construction manager in Sydney, I want to find all mini-excavator rentals within 20km of my suburb, compare prices, and request quotes from 3 operators in one place so I can finalize a hire within an hour.”

Operator Story:
“As a small equipment rental business in Melbourne, I want to list my inventory on the platform to reach new customers without investing in expensive SEO.”

7. Assumptions & Dependencies
Operators will manually update equipment availability (no real-time sync required initially).

Compliance with Australian consumer and privacy laws.

Google Maps API integration for location-based search

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.8+
- PostgreSQL 13+
- Redis 6+

### Frontend Development
bash
cd frontend
npm install
npm run dev

### Backend Development
bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python run.py

## Environment Setup

### Frontend Environment Variables
Create a `.env` file in the frontend directory:
```frontend/README.md
VITE_API_URL=http://localhost:5000
```

### Backend Environment Variables
Create a `.env` file in the backend directory:
```frontend/README.md
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://user:password@localhost/equipmentcentral
REDIS_URL=redis://localhost:6379
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Project Link: [https://github.com/yourusername/equipmentcentral](https://github.com/yourusername/equipmentcentral)