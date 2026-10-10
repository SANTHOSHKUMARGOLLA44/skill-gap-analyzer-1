# Learning Roadmap Fix

## Features

- Role-specific syllabus for 11 career roles.
- Five learning modules: Week 0, Week 1, Week 2, Week 3 and Week 4.
- Syllabus topics and weekly deliverables.
- Expandable and collapsible weekly modules.
- Completion buttons for roadmap tasks.
- Progress percentage based on completed tasks.
- Automatic regeneration when a roadmap is missing or uses an older format.

## Installation

1. Back up your project and database.
2. Add ROLE_SYLLABUS and build_role_roadmap() to app.py.
3. Update the assessment route to save the generated modules.
4. Replace the existing /roadmap route with the updated route.
5. Merge roadmap_body_fragment.html into the content block
   of templates/roadmap.html.
6. Save roadmap.css inside the static folder.
7. Restart the Flask application.

## Test

1. Sign in to the application.
2. Complete a skill assessment.
3. Open the Learning Roadmap page.
4. Expand Week 0 and Week 1.
5. Confirm that the displayed topics match the selected role.
6. Mark a task completed and confirm the status updates.
7. Refresh the page and verify that the roadmap remains available.

## Important

This patch assumes the application already contains:

- Flask authentication and login_required.
- current_student() and get_db().
- An assessments table.
- A recommendations table with the columns used by app.py.
- A toggle_task endpoint.
- The required services modules and database schema.

If your schema or route names differ, adjust the code to match them.