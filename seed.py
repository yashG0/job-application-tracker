import asyncio

from database import AsyncSessionLocal
from model import Application, ApplicationStatus

applications = [
    {
        "company": "Google",
        "position": "Backend Engineer",
        "location": "Bangalore",
        "status": ApplicationStatus.applied,
        "notes": "Applied through careers portal",
    },
    {
        "company": "Amazon",
        "position": "SDE I",
        "location": "Hyderabad",
        "status": ApplicationStatus.interview,
        "notes": "Technical interview scheduled",
    },
    {
        "company": "Microsoft",
        "position": "Python Backend Developer",
        "location": "Pune",
        "status": ApplicationStatus.wishlist,
        "notes": "Need to tailor resume",
    },
    {
        "company": "Netflix",
        "position": "Platform Engineer",
        "location": "Remote",
        "status": ApplicationStatus.rejected,
        "notes": "Rejected after recruiter screening",
    },
    {
        "company": "Uber",
        "position": "Backend Engineer",
        "location": "Bangalore",
        "status": ApplicationStatus.applied,
        "notes": "Waiting for response",
    },
    {
        "company": "Atlassian",
        "position": "Software Engineer",
        "location": "Remote",
        "status": ApplicationStatus.assessment,
        "notes": "Online assessment received",
    },
    {
        "company": "Adobe",
        "position": "Python Developer",
        "location": "Noida",
        "status": ApplicationStatus.interview,
        "notes": "Round 1 completed",
    },
    {
        "company": "Oracle",
        "position": "Backend Developer",
        "location": "Bangalore",
        "status": ApplicationStatus.applied,
        "notes": "Application submitted",
    },
    {
        "company": "Salesforce",
        "position": "Software Engineer",
        "location": "Hyderabad",
        "status": ApplicationStatus.wishlist,
        "notes": "Interesting opportunity",
    },
    {
        "company": "PayPal",
        "position": "Backend Engineer",
        "location": "Chennai",
        "status": ApplicationStatus.applied,
        "notes": "Waiting for recruiter response",
    },
    {
        "company": "Zoho",
        "position": "Python Engineer",
        "location": "Chennai",
        "status": ApplicationStatus.offer,
        "notes": "Offer received",
    },
    {
        "company": "Flipkart",
        "position": "Software Engineer",
        "location": "Bangalore",
        "status": ApplicationStatus.rejected,
        "notes": "Rejected after assessment",
    },
    {
        "company": "Swiggy",
        "position": "Backend Developer",
        "location": "Bangalore",
        "status": ApplicationStatus.applied,
        "notes": "Recently applied",
    },
    {
        "company": "PhonePe",
        "position": "Software Engineer",
        "location": "Bangalore",
        "status": ApplicationStatus.assessment,
        "notes": "Assessment due next week",
    },
    {
        "company": "Razorpay",
        "position": "Backend Engineer",
        "location": "Bangalore",
        "status": ApplicationStatus.interview,
        "notes": "Final interview pending",
    },
    {
        "company": "Meesho",
        "position": "SDE I",
        "location": "Bangalore",
        "status": ApplicationStatus.applied,
        "notes": "Applied through referral",
    },
    {
        "company": "Infosys",
        "position": "Python Developer",
        "location": "Pune",
        "status": ApplicationStatus.applied,
        "notes": "Application under review",
    },
    {
        "company": "TCS",
        "position": "Backend Developer",
        "location": "Mumbai",
        "status": ApplicationStatus.interview,
        "notes": "HR round scheduled",
    },
    {
        "company": "Wipro",
        "position": "Software Engineer",
        "location": "Pune",
        "status": ApplicationStatus.wishlist,
        "notes": "Need to apply this week",
    },
    {
        "company": "Accenture",
        "position": "Associate Software Engineer",
        "location": "Hyderabad",
        "status": ApplicationStatus.applied,
        "notes": "Awaiting recruiter response",
    },
]


async def seed_data():
    all_application: list[Application] = [
        Application(
            company=data["company"],
            position=data["position"],
            location=data["location"],
            status=data["status"],
            notes=data["notes"],
        )
        for data in applications
    ]
    async with AsyncSessionLocal() as sess:
        sess.add_all(all_application)
        await sess.commit()


asyncio.run(seed_data())
