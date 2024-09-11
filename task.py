import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

# Initialize event data
events = {
    "meetings": [],
    "training": [],
    "project_deadlines": [],
    "internal_events": [],
    "client_presentations": [],
    "shift_schedules": [],
    "resources": set(),
    "conferences": [],
    "performance_reviews": [],
    "onboarding_sessions": []
}

# Blogs will include images as well
blogs = []

# Define the main page
def main():
    """Main IT Management System after successful login."""
    # Sidebar with menu
    with st.sidebar:
        selected = option_menu(
            "IT Event Scheduler",
            ["Home", "Meeting Management", "Employee Training", "Project Deadlines", "Internal Events", "Client Presentations",
             "Shift Scheduling", "Resource Allocation", "Conferences", "Performance Reviews", "Onboarding Sessions", "Blog"],
            icons=['house', 'check-square', 'book', 'flag', 'calendar', 'presentation', 'clock', 'cloud-upload', 'globe', 'star', 'person-plus', 'journal'],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#333"},
                "icon": {"color": "#FFFFFF", "font-size": "18px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#444"},
                "nav-link-selected": {"background-color": "#1f77b4", "color": "white"},
            }
        )

    # Custom CSS for styling
    st.markdown(r"""
        <style>
        body {
            background-color: #212121;
            color: #FFFFFF;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-size: cover;
        }
        .main-title {
            color: #1f77b4;
            text-align: center;
            font-size: 36px;
            margin-bottom: 20px;
            padding: 10px;
            background-color: #333;
            border-radius: 10px;
        }
        .info-text {
            color: yellow;
            text-align: left;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .subheader-text {
            color: #e67e22;
            font-size: 24px;
            margin-top: 20px;
            margin-bottom: 10px;
            padding: 5px 0;
            border-bottom: 2px solid #444;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            width: 100%;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #e67e22;
        }
        input, textarea {
            border-radius: 5px;
            border: 1px solid #555;
            padding: 8px;
            margin-bottom: 15px;
            width: 100%;
            background-color: #333;
            color: white;
        }
        .data-container {
            background-color: #2b2b2b;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .blog-card {
            background-color: #333;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .blog-image {
            width: 100%;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Routing for pages
    if selected == "Home":
        home_page()
    elif selected == "Meeting Management":
        meeting_management()
    elif selected == "Employee Training":
        employee_training()
    elif selected == "Project Deadlines":
        manage_projects()
    elif selected == "Internal Events":
        internal_events()
    elif selected == "Client Presentations":
        client_presentations()
    elif selected == "Shift Scheduling":
        shift_scheduling()
    elif selected == "Resource Allocation":
        resource_allocation()
    elif selected == "Conferences":
        manage_conferences()
    elif selected == "Performance Reviews":
        performance_reviews()
    elif selected == "Onboarding Sessions":
        onboarding_sessions()
    elif selected == "Blog":
        blog_page()

def home_page():
    st.write('<h1 class="main-title">Welcome to IT Event Scheduler</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage your meetings, training sessions, project deadlines, and more with ease.</p>', unsafe_allow_html=True)
    
    st.write('<p class="subheader-text">Latest Blog Posts</p>', unsafe_allow_html=True)
    if blogs:
        for blog in blogs:
            st.write(f'<div class="blog-card">', unsafe_allow_html=True)
            if blog['image']:
                st.image(blog['image'], caption=blog['title'], use_column_width=True, output_format='auto')
            st.write(f"**{blog['title']}** - {blog['date']}")
            st.write(blog['content'])
            st.write(f"</div>", unsafe_allow_html=True)
            st.write("---")
    else:
        st.write("No blog posts available.")

# Blog creation and display page
def blog_page():
    st.write('<h1 class="main-title">Blog</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Create and view blog posts about recent and upcoming events.</p>', unsafe_allow_html=True)
    
    blog_title = st.text_input("Blog Title")
    blog_content = st.text_area("Blog Content")
    blog_date = st.date_input("Blog Date", value=datetime.now().date())
    blog_image = st.file_uploader("Upload Blog Image", type=["png", "jpg", "jpeg"])
    
    if st.button("Post Blog"):
        if blog_title and blog_content:
            blogs.append({
                "title": blog_title,
                "content": blog_content,
                "date": blog_date.strftime('%Y-%m-%d'),
                "image": blog_image
            })
            st.success("Blog Post Created!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Blog Posts</p>', unsafe_allow_html=True)
    if blogs:
        for blog in blogs:
            st.write(f'<div class="blog-card">', unsafe_allow_html=True)
            if blog['image']:
                st.image(blog['image'], caption=blog['title'], use_column_width=True, output_format='auto')
            st.write(f"**{blog['title']}** - {blog['date']}")
            st.write(blog['content'])
            st.write(f"</div>", unsafe_allow_html=True)
            st.write("---")
    else:
        st.write("No blog posts available.")

# Meeting management page
def meeting_management():
    st.write('<h1 class="main-title">Meeting Management</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage and schedule meetings with employees, clients, or other stakeholders.</p>', unsafe_allow_html=True)
    meeting_name = st.text_input("Meeting Name")
    meeting_date = st.date_input("Meeting Date")
    meeting_time = st.time_input("Meeting Time")
    meeting_participants = st.text_area("Meeting Participants (comma separated)")
    
    if st.button("Schedule Meeting"):
        if meeting_name and meeting_date and meeting_time and meeting_participants:
            events['meetings'].append({
                'name': meeting_name,
                'date': meeting_date,
                'time': meeting_time,
                'participants': meeting_participants.split(',')
            })
            st.success(f"Meeting '{meeting_name}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Meetings</p>', unsafe_allow_html=True)
    if events['meetings']:
        for meeting in events['meetings']:
            st.write(f"**{meeting['name']}** - {meeting['date']} at {meeting['time']}")
            st.write(f"Participants: {', '.join(meeting['participants'])}")
            st.write("---")
    else:
        st.write("No meetings scheduled.")


# Employee training page
def employee_training():
    st.write('<h1 class="main-title">Employee Training</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Schedule and track employee training sessions.</p>', unsafe_allow_html=True)
    training_name = st.text_input("Training Name")
    training_date = st.date_input("Training Date")
    training_time = st.time_input("Training Time")
    training_participants = st.text_area("Training Participants (comma separated)")
    
    if st.button("Schedule Training"):
        if training_name and training_date and training_time and training_participants:
            events['training'].append({
                'name': training_name,
                'date': training_date,
                'time': training_time,
                'participants': training_participants.split(',')
            })
            st.success(f"Training '{training_name}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Training</p>', unsafe_allow_html=True)
    if events['training']:
        for training in events['training']:
            st.write(f"**{training['name']}** - {training['date']} at {training['time']}")
            st.write(f"Participants: {', '.join(training['participants'])}")
            st.write("---")
    else:
        st.write("No training sessions scheduled.")


# Project deadlines page
def manage_projects():
    st.write('<h1 class="main-title">Project Deadlines</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage and track project deadlines.</p>', unsafe_allow_html=True)
    project_name = st.text_input("Project Name")
    project_deadline = st.date_input("Project Deadline")
    
    if st.button("Set Project Deadline"):
        if project_name and project_deadline:
            events['project_deadlines'].append({
                'name': project_name,
                'deadline': project_deadline
            })
            st.success(f"Project '{project_name}' deadline set successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Project Deadlines</p>', unsafe_allow_html=True)
    if events['project_deadlines']:
        for project in events['project_deadlines']:
            st.write(f"**{project['name']}** - Deadline: {project['deadline']}")
            st.write("---")
    else:
        st.write("No project deadlines set.")


# Internal events page
def internal_events():
    st.write('<h1 class="main-title">Internal Events</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage and track internal company events.</p>', unsafe_allow_html=True)
    event_name = st.text_input("Event Name")
    event_date = st.date_input("Event Date")
    event_time = st.time_input("Event Time")
    
    if st.button("Schedule Event"):
        if event_name and event_date and event_time:
            events['internal_events'].append({
                'name': event_name,
                'date': event_date,
                'time': event_time
            })
            st.success(f"Event '{event_name}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Internal Events</p>', unsafe_allow_html=True)
    if events['internal_events']:
        for event in events['internal_events']:
            st.write(f"**{event['name']}** - {event['date']} at {event['time']}")
            st.write("---")
    else:
        st.write("No internal events scheduled.")


# Client presentations page
def client_presentations():
    st.write('<h1 class="main-title">Client Presentations</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Schedule and manage client presentations.</p>', unsafe_allow_html=True)
    presentation_name = st.text_input("Presentation Name")
    presentation_date = st.date_input("Presentation Date")
    presentation_time = st.time_input("Presentation Time")
    
    if st.button("Schedule Presentation"):
        if presentation_name and presentation_date and presentation_time:
            events['client_presentations'].append({
                'name': presentation_name,
                'date': presentation_date,
                'time': presentation_time
            })
            st.success(f"Presentation '{presentation_name}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Client Presentations</p>', unsafe_allow_html=True)
    if events['client_presentations']:
        for presentation in events['client_presentations']:
            st.write(f"**{presentation['name']}** - {presentation['date']} at {presentation['time']}")
            st.write("---")
    else:
        st.write("No client presentations scheduled.")


# Shift scheduling page
def shift_scheduling():
    st.write('<h1 class="main-title">Shift Scheduling</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage employee shift schedules.</p>', unsafe_allow_html=True)
    employee_name = st.text_input("Employee Name")
    shift_date = st.date_input("Shift Date")
    shift_time = st.time_input("Shift Time")
    
    if st.button("Schedule Shift"):
        if employee_name and shift_date and shift_time:
            events['shift_schedules'].append({
                'name': employee_name,
                'date': shift_date,
                'time': shift_time
            })
            st.success(f"Shift for '{employee_name}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Shifts</p>', unsafe_allow_html=True)
    if events['shift_schedules']:
        for shift in events['shift_schedules']:
            st.write(f"**{shift['name']}** - {shift['date']} at {shift['time']}")
            st.write("---")
    else:
        st.write("No shifts scheduled.")


# Resource allocation page
def resource_allocation():
    st.write('<h1 class="main-title">Resource Allocation</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage and allocate resources for projects or events.</p>', unsafe_allow_html=True)
    resource_name = st.text_input("Resource Name")
    if st.button("Add Resource"):
        if resource_name:
            events['resources'].add(resource_name)
            st.success(f"Resource '{resource_name}' added successfully!")
        else:
            st.error("Please provide a resource name.")
    
    st.write('<p class="subheader-text">Allocated Resources</p>', unsafe_allow_html=True)
    if events['resources']:
        for resource in events['resources']:
            st.write(f"**{resource}**")
            st.write("---")
    else:
        st.write("No resources allocated.")


# Conferences page
def manage_conferences():
    st.write('<h1 class="main-title">Conferences</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage and track conferences.</p>', unsafe_allow_html=True)
    conference_name = st.text_input("Conference Name")
    conference_date = st.date_input("Conference Date")
    
    if st.button("Add Conference"):
        if conference_name and conference_date:
            events['conferences'].append({
                'name': conference_name,
                'date': conference_date
            })
            st.success(f"Conference '{conference_name}' added successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Conferences</p>', unsafe_allow_html=True)
    if events['conferences']:
        for conference in events['conferences']:
            st.write(f"**{conference['name']}** - {conference['date']}")
            st.write("---")
    else:
        st.write("No conferences scheduled.")


# Performance reviews page
def performance_reviews():
    st.write('<h1 class="main-title">Performance Reviews</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Schedule and manage employee performance reviews.</p>', unsafe_allow_html=True)
    review_name = st.text_input("Employee Name for Review")
    review_date = st.date_input("Review Date")
    
    if st.button("Schedule Review"):
        if review_name and review_date:
            events['performance_reviews'].append({
                'name': review_name,
                'date': review_date
            })
            st.success(f"Review for '{review_name}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Reviews</p>', unsafe_allow_html=True)
    if events['performance_reviews']:
        for review in events['performance_reviews']:
            st.write(f"**{review['name']}** - {review['date']}")
            st.write("---")
    else:
        st.write("No reviews scheduled.")


# Onboarding sessions page
def onboarding_sessions():
    st.write('<h1 class="main-title">Onboarding Sessions</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Schedule and manage employee onboarding sessions.</p>', unsafe_allow_html=True)
    session_name = st.text_input("Employee Name for Onboarding")
    session_date = st.date_input("Onboarding Date")
    
    if st.button("Schedule Onboarding"):
        if session_name and session_date:
            events['onboarding_sessions'].append({
                'name': session_name,
                'date': session_date
            })
            st.success(f"Onboarding session for '{session_name}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Onboarding Sessions</p>', unsafe_allow_html=True)
    if events['onboarding_sessions']:
        for session in events['onboarding_sessions']:
            st.write(f"**{session['name']}** - {session['date']}")
            st.write("---")
    else:
        st.write("No onboarding sessions scheduled.")


    main()  
