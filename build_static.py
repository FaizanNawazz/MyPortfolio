import os
import sys
import shutil
from pathlib import Path

# Step 1: Configure Environment Variables for static building
os.environ['USE_SQLITE'] = 'True'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Step 2: Initialize Django
import django
django.setup()

from django.core.management import call_command
from django.test import Client

def build():
    base_dir = Path(__file__).resolve().parent
    dist_dir = base_dir / 'dist'

    # Clean old dist directory
    if dist_dir.exists():
        print("Cleaning old dist directory...")
        shutil.rmtree(dist_dir)
    dist_dir.mkdir(parents=True, exist_ok=True)

    # Step 3: Run migrations
    print("Running migrations...")
    call_command('migrate', interactive=False)

    # Step 4: Run Seeding Script
    print("Seeding database...")
    import seed_portfolio
    seed_portfolio.seed_db()

    # Step 5: Collect Static Files
    print("Collecting static files...")
    call_command('collectstatic', interactive=False, clear=True)

    # Step 6: Render Landing Page HTML via Django test client
    print("Rendering index page template...")
    client = Client()
    response = client.get('/')
    if response.status_code != 200:
        print(f"Error rendering index page: HTTP {response.status_code}")
        sys.exit(1)

    html_content = response.content.decode('utf-8')

    # Step 7: Write index.html
    index_file = dist_dir / 'index.html'
    index_file.write_text(html_content, encoding='utf-8')
    print(f"Generated index.html at: {index_file}")

    # Step 8: Copy Static Directory
    static_root = base_dir / 'staticfiles'
    static_dist = dist_dir / 'static'

    if static_root.exists():
        print(f"Copying static files from {static_root} to {static_dist}...")
        shutil.copytree(static_root, static_dist)
        print("Static assets copied successfully!")
    else:
        print("Error: staticfiles directory not found!")
        sys.exit(1)

    print("Static build completed successfully in the /dist folder!")

if __name__ == '__main__':
    build()
