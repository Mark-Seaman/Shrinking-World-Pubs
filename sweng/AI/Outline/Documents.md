# Document File Structure

## Create Document Files

touch Overview.md
touch LearnByDoing.md
touch TeamProject.md
touch Milestones.md
touch Roles.md
touch PlanningGrid.md

touch m1/Milestone_1.md
touch m1/Lessons.md
touch m1/AI.md
touch m1/Project_1.md
touch m1/Instructor_1.md
touch m1/Team_1.md

mkdir lesson ai project instructor team


## Sample Content File

Overview.md,1
LearnByDoing.md,1,1
TeamProject.md,1,2
Milestones.md,1,3
Roles.md,1,4
PlanningGrid.md,1,5

m1/Milestone_1.md,2
m1/lesson/Lessons.md,2,1
m1/ai/AI.md,2,2
m1/project/Project_1.md,2,3
m1/instructor/Instructor_1.md,2,4
m1/team/Team_1.md,2,5

---

m1/lesson/Milestone_1.md,2

m1/lesson/Lessons.md,2,1
m1/lesson/Lesson_1.md
m1/lesson/Lesson_2.md
m1/lesson/Lesson_3.md
m1/lesson/Lesson_4.md

m1/project/Project_1.md,2,2
m1/project/Requirements.md
m1/project/Design.md
m1/project/Code.md
m1/project/Test.md

m1/ai/AI.md,2,3
m1/instructor/Instructor_1.md,2,4
m1/team/Team_1.md,2,5


## Content Directory Structure

    _content.csv
    Index.md
    Overview.md
    LearnByDoing.md
    TeamProject.md
    AIPlaybook.md
    Resources.md
    m1
        Index.md
        Milestone_1.md
        lesson
            Lessons.md
            [req, design, code, test].md
        ai
            AI.md
            [req, design, code, test].md
        project
            Project_1.md
            [req, design, code, test].md
        instructor
            InstructorSolution.md
            (Ghost Writer github)[req, design, code, test]
            (student server)
        team
            TeamSolution.md
            (student github)[req, design, code, test]
            (student server)
            
    m2
        ...
    m3 
        ...
    ...

---

    m1
        req
        design
        code
        test
