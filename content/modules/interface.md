Title: Interface Design Case Studies
Date: 2018-02-15

# Designing a teacher portal for a school information system

<img src="{filename}/resources/teacher_portal_cutout.jpg" style="width:300px;">

Chris's school purchased a mediocre information system to 
manage all the school's information about students, parents, teachers, schedules, attendance, etc. 
The system could be configured to provide various views of information; Chris was tasked with
designing the teacher portal. This isn't exactly design for learning, but it is a very good example of 
using design thinking to understand how users understand a problem.

## Design Process

We first conducted an extensive survey of teachers' technology usage at school. We asked about how teachers
accessed various kinds of information, which technologies they used for various tasks, what their pain points
were, and much more. Some nuggets:

- Teachers got way too much email. Often over 100 emails per day.
- Many teachers used email to keep static documents like the school schedule. This caused a lot of problems
  when updated versions were sent out.
- Many teachers created elaborate work-arounds to manage all the school's information. These worked, but were
  not effective at keeping records up-to-date. For example, some teachers would print out the contact info for all
  their students. This would usually note get updated when a student moved, the parents got divorced, etc.
- Teachers were often frenzied in the morning as they started the school day.
- Teachers had trouble accessing information about individual students, including parent contact info and health info. 
- The school has a complex schedule, which made it hard for teachers to find out where students would be
  at a particular time and to see their attendance in other classes on a particular day. This was a safety issue.

After the initial wireframes were created (the link below shows the final wireframes), we did further user testing 
by asking teachers to interact with the mock wireframes to accomplish particular tasks. This helped us reorganize
the interface to make it fit teachers' mental models of the information architecture.

## Goals

The design of the teacher portal fell within a larger design goal of organizing the school's information so that
there was one system for each kind of information. In particular, email was for ephemeral and time-sensitive
information and the teacher portal was for static information and information that needed to be kept up-to-date.

The [Teacher Portal Wireframe]({filename}/resources/teacher_portal.pdf) is the final proposed interface. The document is annotated
with specific design goals. Chris used a web app called [Balsamiq](https://balsamiq.com/) to create these.

---
# Student Journalism 

<img src="{filename}/resources/student_journalism.png" style="width:100%">

Chris is working with a local high school journalism program to develop a mobile application to distribute their content. 
They have had a thriving journalism program for several decades, but in the last eight years, the amount of user engagement
and discussion has substantially dropped off. Furthermore, not all of the student body feels represented by student journalism.
While usage of this app does not necessarily take place within the classroom, the design goals for the app are explicitly 
learning-related, framed in terms of participation in a literacy community and identity development.

## Design Process

- Chris recruited a group of student journalists. 
- Over a period of six months, we conducted many interviews with students from the school.
- We sifted through all the interviews for themes and important nuggets. 
- We used these to develop several initial concepts for the app. We went through several iterations, 
  generating dozens of ideas. 
- We built a prototype app and conducted a two-week field trial.
- We interviewed users after the field trial about the app, and observed users using the app.
- We again sifted through the interviews and observations, surfacing three main goals.
- The final app is scheduled to be released in spring 2018, over two years after the initial project meetings!

## Goals

- Express student voice 
- Feel membership in the student body
- Help the student body talk about stuff that’s hard to talk about

The [App Wireframe]({filename}/resources/student_journalism.png) is the final interface design, annotated with specific user experience
goals. It was created using [Sketch](https://www.sketchapp.com/).

--- 
# Interactive storytelling

<img src="{filename}/resources/unfold.png" style="width:500px;">

How might computational literacy interact with textual literacy? Using a programming language called Ink, Chris developed a web app 
for reading and writing interactive fiction.

## Design process

Three iterations of design-based research are documented in this [IDC Work-in-progress paper]({filename}/resources/interactive_fiction.pdf). 

## Goals
For the third iteration of the webapp, Chris adopted a method of user stories to describe how people might interact with the app. 
Here are the [user stories](https://docs.google.com/document/d/1vKE_lJJ7Ejh7eBIO67vPMMEwZvcby0QCukPeE01_hU4/edit?usp=sharing) guiding 
the third iteration of the app. [Here's a spreadsheet keeping track of the individual features](https://docs.google.com/spreadsheets/d/12_HCN-2-A6KpTlgqIM2wNo8l5lGB2R-g2pNloqtjSv0/edit?usp=sharing) which make up the stories.
(See how they're organized according to model, view, UI, etc? This makes it much more efficient to plan my development work.)

Here's [unfold.studio](http://unfold.studio), the current iteration of the app. It's in active use in a computer science curriculum.


