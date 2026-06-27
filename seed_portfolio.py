import os
import django

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from bio_app.models import Bio
from education_app.models import Education
from skills_app.models import Skill
from experience_projects_app.models import ProjectExperience

def seed_db():
    print("Clearing existing data...")
    Bio.objects.all().delete()
    Education.objects.all().delete()
    Skill.objects.all().delete()
    ProjectExperience.objects.all().delete()

    print("Seeding Bio...")
    Bio.objects.create(
        name="Faizan Nawaz",
        job_title="MERN Stack Developer",
        profile_picture="/static/portfolio/images/mainpic.JPG",
        description="A 21-year-old MERN stack developer specializing in the development of dynamic and interactive dashboards, associated with Webwaves Media. Passionate about building modern, responsive, and performance-driven web applications."
    )

    print("Seeding Education...")
    Education.objects.create(
        degree="BS in Computer Science (Ongoing)",
        institution="University of Management and Technology, Lahore",
        duration="2023 - Present",
        description="Ongoing degree with a focus on Software Engineering, Database Systems, Operating Systems, and Algorithms."
    )

    print("Seeding Skills...")
    skills = [
        {"name": "React", "category": "Frontend", "proficiency": 95},
        {"name": "Node.js", "category": "Backend", "proficiency": 90},
        {"name": "Sass", "category": "Styles", "proficiency": 85},
        {"name": "Unity 3D", "category": "Game Dev", "proficiency": 80},
        {"name": "C#", "category": "Languages", "proficiency": 80},
        {"name": "C++", "category": "Languages", "proficiency": 85},
        {"name": "Cybersecurity tools (Kali Linux, Nmap)", "category": "Security", "proficiency": 75},
    ]
    for s in skills:
        Skill.objects.create(**s)

    print("Seeding Experience & Projects...")
    projects = [
        {
            "title": "Front-End Intern | Creative Techniks",
            "item_type": "experience",
            "description": "• Engineered and deployed responsive user interfaces utilizing React.js and utility-first CSS frameworks (Tailwind CSS / Bootstrap), increasing cross-device compatibility and improving mobile load times by 25%.\n• Collaborated with UX/UI design and backend engineering teams to translate high-fidelity Figma mockups into structured, reusable frontend components, accelerating project delivery schedules by 15%.\n• Optimized website performance and user experience by identifying and fixing layout bugs, performance bottlenecks, and cross-browser display issues across major platforms.\n• Integrated RESTful APIs to fetch and render dynamic content, implementing client-side form validations and state management to guarantee smooth, latency-free user interactions.",
            "technologies": "HTML, CSS, Bootstrap, Tailwind CSS, JavaScript, React.js",
            "duration": "Jun 2023 - Sep 2023",
            "link": ""
        },
        {
            "title": "Software Engineering Fellow | Headstarter AI",
            "item_type": "experience",
            "description": "• Architected and developed 5+ full-stack web applications leveraging React.js, Node.js, Express, and databases, following agile development methodologies from concept to production.\n• Integrated advanced AI APIs and services (such as OpenAI, LLMs, and vector search engines) to implement key features like intelligent chatbot tools, search queries, and dynamic content feeds.\n• Partnered with cross-functional teams of engineering fellows to conduct code reviews, resolve merge conflicts, and manage project lifecycles using Git and agile tracking tools.\n• Enhanced frontend application performance by optimizing state management (using Context API or React hooks) and API calls, achieving a 30% reduction in client-side load time.",
            "technologies": "React, APIs, Node.js, Express, JavaScript, Git",
            "duration": "July 2024 - Oct 2024",
            "link": ""
        },
        {
            "title": "Retail Management System",
            "item_type": "project",
            "description": "A Microsoft SQL Server database lab project designed to manage sales transactions, inventory tracking, and employee scheduling. Features complex stored procedures and triggers for data integrity.",
            "technologies": "Microsoft SQL Server, SQL, DB Schema Design",
            "duration": "Database Lab Project",
            "link": "https://github.com/FaizanNawazz/Retail_Management_System"
        },
        {
    "title": "INoteBook",
    "item_type": "project",
    "description": "Developed a full-stack note-taking application using MongoDB, Express.js, React, and Node.js. Implemented user authentication with JWT, CRUD operations for notes, and a responsive UI with Bootstrap. Features include real-time updates, form validation, and secure API endpoints.",
    "technologies": "MongoDB, Express.js, React, Node.js, Bootstrap",
    "duration": "Personal Project",
    "link": "https://github.com/FaizanNawazz/inotebook"
  },
        {
            "title": "3D Horror Game",
            "item_type": "project",
            "description": "An atmospheric 3D horror game developed using the Unity engine and the Universal Render Pipeline (URP). Implemented custom post-processing, interactive physics, and pathfinding AI.",
            "technologies": "Unity 3D, C#, URP, Interactive Physics",
            "duration": "Game Jam / Personal Project",
            "link": "https://github.com/FaizanNawazz"
        },
        {
            "title": "NewsMonkey",
    "item_type": "project",
    "description": "Developed a responsive news application using React.js that fetches and displays real-time news articles across multiple categories.",
    "technologies": "React.js, React Router, Bootstrap, RESTful APIs (NewsAPI)",
    "duration": "Personal Project",
    "link": "https://github.com/FaizanNawazz/NewApp"
        }
    ]
    for p in projects:
        ProjectExperience.objects.create(**p)

    print("Data seeding completed successfully!")

if __name__ == '__main__':
    seed_db()
