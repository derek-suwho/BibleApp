# FaithConnect - Christian Social App

A comprehensive Christian social application designed to help believers grow in their faith through daily practices, prayer, community connection, and local church discovery.

## Features

### 🙏 Faith Growth Features
- **Daily Devotionals**: Scripture-based devotional content with reflection questions
- **Prayer Tracking**: Personal prayer journal with answered prayer tracking
- **Spiritual Profile**: Christian-specific profile fields including church affiliation, spiritual gifts, and ministry interests
- **Scripture Memory**: Verse memorization and spiritual habit tracking (planned)

### 👥 Community Features
- **Local Discovery**: Find Christians in your area based on location
- **Church Directory**: Comprehensive directory of local churches with service times and contact info
- **Community Groups**: Join Bible studies, prayer groups, and ministry teams
- **Mentorship Matching**: Connect with spiritual mentors or mentees
- **Prayer Requests**: Share and receive prayer support from the community

### 🛡️ Built with Christian Values
- Community guidelines based on Christian principles
- Privacy-focused design respecting personal information
- Content moderation ensuring appropriate, faith-building discussions
- Secure platform designed with safety in mind

## Tech Stack

- **Backend**: Python Flask web application
- **Frontend**: HTML/JavaScript with Bootstrap (responsive design)
- **Database**: SQLAlchemy with SQLite (dev) / PostgreSQL (prod)
- **Authentication**: Flask-Login with secure password hashing
- **Search**: Elasticsearch integration for content discovery
- **Deployment**: Designed for multi-environment deployment (dev/test/prod)

## Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd BibleApp
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize database and seed data**
   ```bash
   python seed_data.py
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

Visit `http://localhost:5000` to access the application.

## Project Structure

```
BibleApp/
├── app.py                 # Main Flask application
├── models.py             # Database models
├── run.py                # Development server runner
├── seed_data.py          # Sample data for development
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── templates/           # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── prayers.html
│   ├── devotional.html
│   ├── community.html
│   ├── churches.html
│   └── profile.html
├── static/              # Static assets
│   ├── css/
│   └── js/
└── CLAUDE.md           # AI assistant instructions
```

## Database Models

- **User**: Authentication and basic user info
- **UserProfile**: Christian-specific profile information
- **Prayer**: Prayer requests and answered prayers
- **Devotional**: Daily devotional content
- **Community**: Local Christian groups and Bible studies
- **Church**: Local church directory
- **SpiritualHabit**: Habit tracking for spiritual disciplines

## Key Features Explained

### Daily Devotionals
- Scripture-based content with reflection questions
- Personal note-taking and progress tracking
- Community discussion features (planned)

### Prayer Journal
- Private prayer request tracking
- Answered prayer celebrations
- Prayer type categorization
- Community prayer sharing (optional)

### Local Community Discovery
- Location-based Christian networking
- Church finder with detailed information
- Community group creation and joining
- Event discovery and RSVP

### Christian Profile Management
- Church affiliation and denomination
- Spiritual gifts and ministry interests
- Mentorship availability preferences
- Privacy controls for information sharing

## Development

### Environment Setup
- `development`: Local development with SQLite
- `test`: Testing environment with isolated database
- `production`: Live environment with PostgreSQL

### Adding New Features
1. Create database models in `models.py`
2. Add routes in `app.py`
3. Create templates in `templates/`
4. Update navigation in `base.html`
5. Test thoroughly across environments

### Database Migrations
When updating models:
1. Update the model definitions
2. Run `python -c "from app import app, db; db.create_all()"`
3. Test with seed data

## Deployment

The application is designed for deployment on platforms like:
- Heroku
- Railway
- DigitalOcean App Platform
- AWS Elastic Beanstalk

Environment variables required:
- `SECRET_KEY`: Flask secret key
- `DATABASE_URL`: Database connection string
- `ELASTICSEARCH_URL`: Search service URL (optional)

## Contributing

This is a faith-based project designed to build up the Christian community. When contributing:

1. Maintain Christian values in all features
2. Respect user privacy and safety
3. Follow existing code conventions
4. Test thoroughly before submitting
5. Keep features focused on spiritual growth and community building

## License

This project is developed for the Christian community with the goal of advancing God's kingdom through technology.

## Support

For questions, suggestions, or prayer requests related to this project, please open an issue or contact the development team.

---

*"As iron sharpens iron, so one person sharpens another." - Proverbs 27:17*