from app import app, db
from models import Devotional, Church
from datetime import date, datetime, timedelta

def seed_devotionals():
    """Add sample devotional content"""
    devotionals = [
        {
            'title': 'Walking in Faith',
            'content': '''Faith is not about having all the answers, but trusting in God's perfect plan even when we cannot see the way forward. Today, let us remember that faith requires us to step out of our comfort zone and trust in God's guidance. When we walk by faith and not by sight, we open ourselves to the miraculous ways God works in our lives. Consider the areas in your life where God is calling you to step out in faith. What fears are holding you back? Remember that God has not given us a spirit of fear, but of power, love, and sound mind.''',
            'scripture_reference': '2 Corinthians 5:7',
            'scripture_text': 'For we walk by faith, not by sight.',
            'date': date.today(),
            'author': 'Pastor John',
            'reflection_questions': 'What areas of your life require more faith? How can you trust God more deeply today?',
            'prayer_points': 'Pray for increased faith and trust in God\'s plan for your life.'
        },
        {
            'title': 'The Power of Prayer',
            'content': '''Prayer is our direct line of communication with our Heavenly Father. It is not merely asking God for things, but building a relationship with Him. Through prayer, we find peace in troubled times, strength in weakness, and guidance in confusion. Today, let us commit to making prayer a priority in our daily lives. Whether it\'s morning devotions, prayers throughout the day, or evening reflections, consistent prayer transforms our hearts and aligns our will with God\'s.''',
            'scripture_reference': '1 Thessalonians 5:17',
            'scripture_text': 'Pray without ceasing.',
            'date': date.today() + timedelta(days=1),
            'author': 'Pastor Sarah',
            'reflection_questions': 'How can you improve your prayer life? What barriers prevent you from praying more consistently?',
            'prayer_points': 'Ask God to help you develop a deeper prayer life and to show you how to pray more effectively.'
        },
        {
            'title': 'Love One Another',
            'content': '''Jesus gave us the greatest commandment: to love God with all our heart, soul, and mind, and to love our neighbor as ourselves. Love is not just a feeling; it\'s an action that requires sacrifice, patience, and forgiveness. In our daily interactions, we have countless opportunities to show Christ\'s love to others. This might mean forgiving someone who has wronged us, helping a neighbor in need, or simply showing kindness to a stranger. When we love others as Christ loves us, we become His hands and feet in this world.''',
            'scripture_reference': 'John 13:34-35',
            'scripture_text': 'A new command I give you: Love one another. As I have loved you, so you must love one another. By this everyone will know that you are my disciples, if you love one another.',
            'date': date.today() + timedelta(days=2),
            'author': 'Pastor Mike',
            'reflection_questions': 'Who in your life needs to experience God\'s love through you? How can you show love in practical ways today?',
            'prayer_points': 'Pray for the ability to love others unconditionally and for opportunities to serve those around you.'
        }
    ]
    
    for dev_data in devotionals:
        devotional = Devotional(**dev_data)
        db.session.add(devotional)
    
    db.session.commit()
    print("Sample devotionals added successfully!")

def seed_churches():
    """Add sample church data"""
    churches = [
        {
            'name': 'First Baptist Church',
            'denomination': 'Baptist',
            'address': '123 Main Street',
            'city': 'Springfield',
            'state': 'IL',
            'country': 'United States',
            'zip_code': '62701',
            'phone': '(217) 555-0123',
            'email': 'info@fbcspringfield.org',
            'website': 'www.fbcspringfield.org',
            'pastor_name': 'Pastor John Smith',
            'service_times': 'Sunday: 9:00 AM & 11:00 AM, Wednesday: 7:00 PM',
            'description': 'A welcoming community focused on growing in faith and serving our neighbors.'
        },
        {
            'name': 'Grace Community Church',
            'denomination': 'Non-denominational',
            'address': '456 Oak Avenue',
            'city': 'Springfield',
            'state': 'IL',
            'country': 'United States',
            'zip_code': '62702',
            'phone': '(217) 555-0456',
            'email': 'hello@gracecommunitychurch.org',
            'website': 'www.gracecommunitychurch.org',
            'pastor_name': 'Pastor Sarah Johnson',
            'service_times': 'Sunday: 10:30 AM, Small Groups: Various times',
            'description': 'A modern church with traditional values, focused on authentic community and practical faith.'
        },
        {
            'name': 'St. Mary\'s Catholic Church',
            'denomination': 'Catholic',
            'address': '789 Church Street',
            'city': 'Springfield',
            'state': 'IL',
            'country': 'United States',
            'zip_code': '62703',
            'phone': '(217) 555-0789',
            'email': 'parish@stmarychurch.org',
            'website': 'www.stmarychurch.org',
            'pastor_name': 'Father Michael Brown',
            'service_times': 'Saturday: 5:00 PM, Sunday: 8:00 AM, 10:00 AM, 12:00 PM',
            'description': 'A historic parish serving the Springfield community for over 100 years.'
        }
    ]
    
    for church_data in churches:
        church = Church(**church_data)
        db.session.add(church)
    
    db.session.commit()
    print("Sample churches added successfully!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_devotionals()
        seed_churches()
        print("Database seeded successfully!")