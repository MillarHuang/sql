* meeting 06/04 *
Dear group,

Here's an update of what Miriam and Loes have been working on today.
- As discussed in the groupchat, we decided that the schema.py file is not necessary so we will not make and use that. That means the first to do of the list below is done.
- We created 3 new methods. We have some doubts and questions about some things, which Loes will discuss with Millar tomorrow. If you already want to take a look and leave some feedback, that is very welcome!
- We changed the name max_score to max_points. And added in the method addQuestion.

Miriam and Loes

* meeting 05/04 * 

TO DO
- L&Mir: schema.py, seperate the gradeDB.py file in the schema.py (top-half of current file, main class, bottom half of current file)
- L&Mir: finish the methods in the GradeDB.py file (main class above, methods below) 
- Mil: random_init: initalise database with random content
+ S: student_summary.ipynb
+ S: student_detail.ipynb
+ S: teacher_summary.ipynb
	provide a python notebook code in jupyter notebook. Use joint-statements to get the data out of the database to display them. -> write 3 functions for that
+ Mir&...: In a teacher summary report notebook: a chart showing distribution of
grades per each question.
+ Mir&...In a student summary report notebook: a chart showing student grades
on the top of distribution of all student grades per each question.

- L&everyone...: read me file finish
- L: schema file convert pdf

NOTES
- not sure if we need to connect the answer_id in the scores table and from the answers table. Maybe there's an arrow missing between answers and scores.
- note on schema.py is currently in theß gradeDB.py. 

AVAILABILITY
- Katrin: until (and including) thursday
- Katie: until (and including) friday





Dear group, 

here is an overview of what we did during the weekend:

schema.pptx : a powerpoint with our schema (hopefully self-explanatory); we saved it in a powerpoint so it can still be customized if needed, e.g. you can adjust the errors if you want; needs to be converted to a pdf later (note that the schema goes beyond the boundaries of the powerpoint slide, so you need to take a screenshot of the schema and create a pdf from the screenshot)

sql_database_code.ipynb : jupyter notebook file containing the SQL code to create the database GradeDB.db (we decided to use python instead of a .sql file to define the database)

GradeDB.db : database (result of running sql_database_code.ipynb) 

gradedb.py : Python file with definitions of the table classes and some of the big methods of the GradeDB class

Tester_file.ipynb : test methods on some random data

Katie and Katrin 