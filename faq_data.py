faq_responses = {
    "timings": "The institute is open from 9:00 AM to 5:00 PM, Monday to Saturday.",
    "fees": "The tuition fee is $1000 per semester. Additional fees apply for hostel and library.",
    "contact": "You can contact the administration at contact@institute.edu or call +1-234-567-890.",
    "address": "The institute feels located at 123 Education Lane, Knowledge City, State, Country.",
    "courses": "We offer B.Tech in CSE, ECE, ME, and Civil Engineering. We also strictly offer B.Sc in Physics and Mathematics.",
    "admissions": "Admissions are currently open for the academic year 2024-25. Visit our website to apply.",
    "library": "The library is open from 8:00 AM to 8:00 PM. Students can borrow up to 3 books at a time.",
    "hostel": "Separate hostels are available for boys and girls. Fees are $500 per semester.",
    "transport": "Bus service is available from all major points in the city. Monthly pass costs $50.",
    "placements": "Our average package is $80,000 per annum. Top recruiters include Google, Microsoft, and Amazon.",
    "sports": "We have a football ground, cricket pitch, basketball court, and indoor gymnasium.",
    "events": "The annual tech fest 'Technova' is held in March. Cultural fest 'Sanskriti' is in October.",
    "exams": "End-semester exams are scheduled for December and May.",
    "results": "Results are published on the student portal within 30 days of exams.",
    "holidays": "The institute remains closed on public holidays and Sundays. Check the academic calendar."
}

def get_answer(question):
    """
    Returns the answer based on the most specific (longest) keyword match.
    """
    question = question.lower()
    
    # Extended aliases for better accuracy
    aliases = {
        # Time/Schedule
        "time": "timings", "hours": "timings", "open": "timings", "schedule": "timings",
        # Money/Fees
        "cost": "fees", "price": "fees", "tuition": "fees", "fee": "fees",
        "payment": "fees", "dues": "fees",
        # Contact
        "email": "contact", "phone": "contact", "call": "contact", "number": "contact",
        "help": "contact", "reach": "contact",
        # Location
        "location": "address", "where": "address", "map": "address", "place": "address",
        # Academics
        "program": "courses", "branch": "courses", "stream": "courses", "subjects": "courses",
        "degree": "courses",
        # Admissions
        "apply": "admissions", "join": "admissions", "enroll": "admissions", "registration": "admissions",
        # Facilities
        "book": "library", "reading": "library",
        "accommodation": "hostel", "dorm": "hostel", "living": "hostel", "residence": "hostel",
        "hostel fees": "hostel", # Precise match for hostel fees
        "bus": "transport", "shuttle": "transport", "commute": "transport",
        "transport fees": "transport", # Precise match for transport fees
        # Career
        "job": "placements", "career": "placements", "salary": "placements", "package": "placements",
        "recruiters": "placements", "companies": "placements",
        # Other
        "gym": "sports", "play": "sports", "game": "sports",
        "fest": "events", "party": "events", "function": "events",
        "test": "exams", "midsem": "exams", "endsem": "exams",
        "score": "results", "grade": "results", "gpa": "results",
        "vacation": "holidays", "off": "holidays", "leave": "holidays"
    }
    
    # Combine all patterns (direct keys and aliases)
    # We map "pattern" -> "final_key"
    all_patterns = {}
    for k in faq_responses:
        all_patterns[k] = k
    for alias, key in aliases.items():
        all_patterns[alias] = key
        
    # Sort patterns by length descending to match "hostel fees" before "fees"
    sorted_patterns = sorted(all_patterns.keys(), key=len, reverse=True)
    
    for pattern in sorted_patterns:
        if pattern in question:
            key = all_patterns[pattern]
            return faq_responses[key]
            
    return "I'm sorry, I couldn't find an answer to that. Try asking about timings, fees, courses, placements, etc."
