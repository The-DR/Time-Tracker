# Time Tracker
## A simple, passive Django App for time logging by users & basic reports for managers.
Requirement: This is a Django App and requires a Django project with a login system configured.
- ### Users
  - Users are individuals who are tracking thier time
  - User Details: `E-Mail, Name, Nick Name, Address, Phone #`
  - Allow for multiple Users
  - Users maybe allocated to multiple projects
  - Users can access reports on themselves
  - #### Managers
    - Managers are users who can produce client, project & user reports
    - A manager must be assigned to each client
    - Managers 
- ### Clients
  - Clients are organizations who have projects/tasks being tracked by the users
  - The organization which is operating this app should be the first client
  - Client Details: `Organization Name, Organization Address, Organization Phone #, Contact Name, Contact Phone #`
  - Allow for multiple Clients
  - Clients control Time Log granularity/hour
- ### Projects, Sub-Projects, Tasks & Sub-Tasks
  - Allow for multiple Projects per Client
  - Allow for the potential sharing of Projects between Clients
  - Allow for multiple Sub-Projects per Project
  - Allow for multiple Tasks per Project / Sub-Project
  - Allow for multiple Sub-Tasks per Task / Sub-Task
- ### Time Log Entries
  - Entries must be allocated to a Project, Sub-Project, Task or Sub-Task
  - Entries track: `User, Start Time, End Time, Project, Sub-Project, Task, Sub-Task, Productivity Level`
