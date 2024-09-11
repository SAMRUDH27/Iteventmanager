import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

# Initialize event data
events = {
    "meetings": [],
    "training": [],
    "projectdeadlines": [],
    "internalevents": [],
    "clientpresentation": [],
    "shiftscheduling": [],
    "resources": set(),
    "conferences": [],
    "performreview": [],
    "onboardingsession": []
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
        homepage()
    elif selected == "Meeting Management":
        meetingmanagement()
    elif selected == "Employee Training":
        emptraining()
    elif selected == "Project Deadlines":
        manageproject()
    elif selected == "Internal Events":
        internalevents()
    elif selected == "Client Presentations":
        clientpresentation()
    elif selected == "Shift Scheduling":
        shiftscheduling()
    elif selected == "Resource Allocation":
        resourceallocation()
    elif selected == "Conferences":
        manageconference()
    elif selected == "Performance Reviews":
        performreview()
    elif selected == "Onboarding Sessions":
        onboardingsession()
    elif selected == "Blog":
        blogpage()

def homepage():
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


def blogpage():
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

def meetingmanagement():
    st.write('<h1 class="main-title">Meeting Management</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage and schedule meetings with employees, clients, or other stakeholders.</p>', unsafe_allow_html=True)
    meetname = st.text_input("Meeting Name")
    meetdate = st.date_input("Meeting Date")
    meettime = st.time_input("Meeting Time")
    meetparticpant = st.text_area("Meeting Participants (comma separated)")
    
    if st.button("Schedule Meeting"):
        if meetname and meetdate and meettime and meetparticpant:
            events['meetings'].append({
                'name': meetname,
                'date': meetdate,
                'time': meettime,
                'participants': meetparticpant.split(',')
            })
            st.success(f"Meeting '{meetname}' scheduled successfully!")
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



def emptraining():
    st.write('<h1 class="main-title">Employee Training</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Schedule and track employee training sessions.</p>', unsafe_allow_html=True)
    trainname = st.text_input("Training Name")
    traindate = st.date_input("Training Date")
    traintime = st.time_input("Training Time")
    trainparticipant = st.text_area("Training Participants (comma separated)")
    
    if st.button("Schedule Training"):
        if trainname and traindate and traintime and trainparticipant:
            events['training'].append({
                'name': trainname,
                'date': traindate,
                'time': traintime,
                'participants': trainparticipant.split(',')
            })
            st.success(f"Training '{trainname}' scheduled successfully!")
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



def manageproject():
    st.write('<h1 class="main-title">Project Deadlines</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage and track project deadlines.</p>', unsafe_allow_html=True)
    projname = st.text_input("Project Name")
    projdeadline = st.date_input("Project Deadline")
    
    if st.button("Set Project Deadline"):
        if projname and projdeadline:
            events['projectdeadlines'].append({
                'name': projname,
                'deadline': projdeadline
            })
            st.success(f"Project '{projname}' deadline set successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Project Deadlines</p>', unsafe_allow_html=True)
    if events['projectdeadlines']:
        for project in events['projectdeadlines']:
            st.write(f"**{project['name']}** - Deadline: {project['deadline']}")
            st.write("---")
    else:
        st.write("No project deadlines set.")



def internalevents():
    st.write('<h1 class="main-title">Internal Events</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage and track internal company events.</p>', unsafe_allow_html=True)
    eventname = st.text_input("Event Name")
    eventdate = st.date_input("Event Date")
    eventtime = st.time_input("Event Time")
    
    if st.button("Schedule Event"):
        if eventname and eventdate and eventtime:
            events['internalevents'].append({
                'name': eventname,
                'date': eventdate,
                'time': eventtime
            })
            st.success(f"Event '{eventname}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Internal Events</p>', unsafe_allow_html=True)
    if events['internalevents']:
        for event in events['internalevents']:
            st.write(f"**{event['name']}** - {event['date']} at {event['time']}")
            st.write("---")
    else:
        st.write("No internal events scheduled.")



def clientpresentation():
    st.write('<h1 class="main-title">Client Presentations</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Schedule and manage client presentations.</p>', unsafe_allow_html=True)
    presentname = st.text_input("Presentation Name")
    presentdate = st.date_input("Presentation Date")
    presenttime = st.time_input("Presentation Time")
    
    if st.button("Schedule Presentation"):
        if presentname and presentdate and presenttime:
            events['clientpresentation'].append({
                'name': presentname,
                'date': presentdate,
                'time': presenttime
            })
            st.success(f"Presentation '{presentname}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Client Presentations</p>', unsafe_allow_html=True)
    if events['clientpresentation']:
        for presentation in events['clientpresentation']:
            st.write(f"**{presentation['name']}** - {presentation['date']} at {presentation['time']}")
            st.write("---")
    else:
        st.write("No client presentations scheduled.")



def shiftscheduling():
    st.write('<h1 class="main-title">Shift Scheduling</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage employee shift schedules.</p>', unsafe_allow_html=True)
    empname = st.text_input("Employee Name")
    sdate = st.date_input("Shift Date")
    stime = st.time_input("Shift Time")
    
    if st.button("Schedule Shift"):
        if empname and sdate and stime:
            events['shiftscheduling'].append({
                'name': empname,
                'date': sdate,
                'time': stime
            })
            st.success(f"Shift for '{empname}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Shifts</p>', unsafe_allow_html=True)
    if events['shiftscheduling']:
        for shift in events['shiftscheduling']:
            st.write(f"**{shift['name']}** - {shift['date']} at {shift['time']}")
            st.write("---")
    else:
        st.write("No shifts scheduled.")



def resourceallocation():
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



def manageconference():
    st.write('<h1 class="main-title">Conferences</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage and track conferences.</p>', unsafe_allow_html=True)
    cname = st.text_input("Conference Name")
    cdate = st.date_input("Conference Date")
    
    if st.button("Add Conference"):
        if cname and cdate:
            events['conferences'].append({
                'name': cname,
                'date': cdate
            })
            st.success(f"Conference '{cname}' added successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Conferences</p>', unsafe_allow_html=True)
    if events['conferences']:
        for conference in events['conferences']:
            st.write(f"**{conference['name']}** - {conference['date']}")
            st.write("---")
    else:
        st.write("No conferences scheduled.")



def performreview():
    st.write('<h1 class="main-title">Performance Reviews</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Schedule and manage employee performance reviews.</p>', unsafe_allow_html=True)
    rname = st.text_input("Employee Name for Review")
    rdate = st.date_input("Review Date")
    
    if st.button("Schedule Review"):
        if rname and rdate:
            events['performreview'].append({
                'name': rname,
                'date': rdate
            })
            st.success(f"Review for '{rname}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Reviews</p>', unsafe_allow_html=True)
    if events['performreview']:
        for review in events['performreview']:
            st.write(f"**{review['name']}** - {review['date']}")
            st.write("---")
    else:
        st.write("No reviews scheduled.")


def onboardingsession():
    st.write('<h1 class="main-title">Onboarding Sessions</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Schedule and manage employee onboarding sessions.</p>', unsafe_allow_html=True)
    ssname = st.text_input("Employee Name for Onboarding")
    ssdate = st.date_input("Onboarding Date")
    
    if st.button("Schedule Onboarding"):
        if ssname and ssdate:
            events['onboardingsession'].append({
                'name': ssname,
                'date': ssdate
            })
            st.success(f"Onboarding session for '{ssname}' scheduled successfully!")
        else:
            st.error("Please fill in all fields.")
    
    st.write('<p class="subheader-text">Scheduled Onboarding Sessions</p>', unsafe_allow_html=True)
    if events['onboardingsession']:
        for session in events['onboardingsession']:
            st.write(f"**{session['name']}** - {session['date']}")
            st.write("---")
    else:
        st.write("No onboarding sessions scheduled.")


    main()  
