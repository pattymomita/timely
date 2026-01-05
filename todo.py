"""
Module for managing a simple to-do list.

Levels for each "skill" the user adds is being tracked.
Levels do not reset but can be prompted to do so if the user chooses.
Time is converted to xp. 1200xp (20 hours) = 1 level.

Each skill has total_hours
level = total_hours / 20
Show progress_to_next_level = total_hours % 20

Feature List:
    1.Skills List
        Create/edit/delete skills

    2.Time Logging
        Add time to skills (Time tracking)
        View skill progress
        Start/stop/reset on a selected skill

    3.Progress UI
        Total time spent on each skill
        Level and progress to next level
        Current Level
        Progress bar?

    4.History Tracking
        View history of time spent on each skill

Data Model:
    Skill:
        id: double
        name: str
        total_hours: float
        created_at: datetime

    Session: 
        id: double
        skill_id: double
        start_time: datetime
        end_time: datetime
        duration_hours: float
        note: str (optional)
    
    Leveling Logic:
        level = total_hours / 20
        progress_to_next_level = total_hours % 20
        remainder_hours = 20 - progress_to_next_level
        progress_percentage = (progress_to_next_level / 20) * 100
    
 Build Order:
 Create Skills Page
 Create Profile Page
 Create Session Page 
 Manual session entry 
 Level calculation functions
 Session History Page
 Add timer start/stop functionality
 Quality of Life Improvements
 CSS Enhancements
 UI Refinements

 
 Other features to consider:
    - Reminders/Notifications for skill practice
    - Rewards system for reaching new levels
    - Streaks
    - Targets 
    - Tags/Categories for skills

How does the app handle pitfalls?
    - User forgets to stop timer: Implement notifications or auto-stop after a certain period.
    - Incorrect time entries: Allow users to edit or delete sessions.
    - Data loss: Implement regular backups and data export options.
    - Overwhelming number of skills: Allow users to archive or hide inactive skills.
    - App closed/ phone sleeps.
    - Mobile background restrictions 
    - Time zone changes

Build with React Native and SQLite for cross-platform compatibility and offline functionality


"""