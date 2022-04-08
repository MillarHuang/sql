 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 15:10:35 2022

@author: Katie, Loes, Miri, Katrin
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, MetaData, Boolean, Table, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base, sessionmaker, backref
import lorem
import names


Base = declarative_base()
    # Creates a base class: provides basic functionalities for all other classes
    
allocate_questions=Table('allocate_questions', Base.metadata, Column('task_id',ForeignKey('tasks.task_id'), primary_key=True), Column('question_id',ForeignKey('questions.question_id'), primary_key=True))
    # Creates associative table between tasks and questions 
 
    
 
# Create classes 
  
class Student(Base):
    __tablename__ = "students"
  
    university_id = Column(String(20),primary_key=True)
    first_name = Column(String(160))
    last_name = Column(String(160))
    email = Column(String(160))
    # one student can have many assignments, but one assignment is only given to one student (many-to-one)
    assignments = relationship('Assignment',backref='student')
    
    def __repr__(self):
        return f"Student(university_id={self.university_id}, name={self.first_name} {self.last_name}, email={self.email})"
#  Create Student class which maps to the table students. There is a one 
#  (students) to many (assignments) relationship between students and assignments. 

    
class Question(Base):
    __tablename__ = 'questions'
    
    question_id=Column(Integer,primary_key=True)
    title=Column(String)
    text=Column(String)
    max_points=Column(Integer)
    # one question can have many answers, but one answer is given to exactly one question (many-to-one)
    answers = relationship('Answer',backref='question')
    tasks = relationship('Task', secondary=allocate_questions, back_populates='questions')
    
    
    def __repr__(self):
        return f"Question(task_id={self.question_id}, title={self.text}, max_points={self.max_points})"    
# Create question class which maps to the table questions. There is a one 
# (questions) to many (allocate_questions) relationship between questions and
# allocate_questions. questions. There is a one (questions) to many (answers) 
# relationship between questions and answers
    
    
class Task(Base):
    __tablename__='tasks'
    
    task_id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    # one task can be written into multiple assignments, but one assignment consists of only one task (many-to-one)
    assignments = relationship('Assignment',backref='task')
    questions = relationship('Question', secondary=allocate_questions,back_populates='tasks')

    def __repr__(self):
        return f"Task(task_id={self.task_id}, title={self.title})"
# Create Task class which maps to the table tasks. There is a one (tasks) to 
# many (assignments) relationship between tasks and questions. There is is a 
# one (tasks) to many (allocate_questions) relationship between task ans questions
# between tasks and allocate questions.


class Assignment(Base):
    __tablename__='assignments'
    
    assignment_id=Column(Integer, primary_key=True)
    task_id = Column(ForeignKey('tasks.task_id'))
    university_id = Column(ForeignKey('students.university_id'))
    
    def __repr__(self):
        return f"Assignment(assignment_id={self.assignment_id}, task_id={self.task_id}, university_id={self.university_id}, submission={self.submission})"
# Create Assignment class which maps to the table assignments. One (assignments) 
# to one (submission). One (assignments) to one (university_id). 


class Answer(Base):
    __tablename__='answers'
    
    answer_id=Column(Integer, primary_key=True)
    submission_id = Column(ForeignKey('submissions.submission_id'))
    question_id = Column(ForeignKey('questions.question_id'))
    text = Column(String)
    
    def __repr__(self):
        return f"Answer(answer_id={self.answer_id}, submission_id={self.submission_id}, question_id={self.question_id}, text={self.text})"
# Create Answer class which maps to the table answers. One (question) to many
# (questions)    
    

class Submission(Base):
    __tablename__='submissions'
    
    submission_id = Column(Integer, primary_key=True)
    assignment_id = Column(ForeignKey('assignments.assignment_id'))
    last_modified = Column(DateTime)
    assignment=relationship('Assignment',backref=backref('submission',uselist=False))
    answers = relationship('Answer',backref='submission')
# Create Submission class which maps to table submissions. one (submission) to 
# one (assignment) relationship. one (submission) to many (answers)
    
    def __repr__(self):
        return f"Submission(submission_id={self.submission_id}, assignment_id={self.assignment_id}, last_modified={self.last_modified})"
# Create Submission class which maps to the table submissions. One (submissions)
# to many (answers)    
    

class Evaluation_Request(Base):
    __tablename__='evaluation_requests'
    
    evaluation_request_id=Column(Integer, primary_key=True)
    submission_id=Column(ForeignKey('submissions.submission_id'))
    date=Column(DateTime)
    submission=relationship('Submission',backref=backref('evaluation_request',uselist=False))
    
    
    def __repr__(self):
        return f"Evaluation_Request(evaluation_request_id={self.evaluation_request_id}, submission_id={self.submission_id}, date={self.date_id})" 
# Creates class Evaluation_Request. one (evaluation_requests) to one (submissions)
# relationship. One to one (evaluation_requests) to (evaluations)


class Evaluation(Base):
    __tablename__='evaluations'
    
    evaluation_id=Column(Integer, primary_key=True)
    evaluation_request_id=Column(ForeignKey('evaluation_requests.evaluation_request_id'))
    date=Column(DateTime)
    grade=Column(Float)
    evaluation_request=relationship('Evaluation_Request',backref=backref('evaluation',uselist=False))
    scores=relationship('Score',backref='evaluation')
    
    def __repr__(self):
        return f"Evaluation(evaluation_id={self.evaluation_id}, evaluation_request_id={self.evaluation_request_id},date={self.date},grade={self.grade})" 
# Creates class Evaluation which maps to the table evaluations. one 
# (evaluations) to many (scores) relationship. one (evaluations) to one 
# (evaluations_finished) relationship. one (evaluations) to 
# one(evaluation_request) relationship


class Score(Base):
    __tablename__='scores'
    
    score_id=Column(Integer, primary_key=True)
    evaluation_id=Column(ForeignKey('evaluations.evaluation_id'))
    answer_id=Column(Integer)
    value=Column(Integer)
    
    
    def __repr__(self):
        return f"Score(score_id={self.score_id}, evaluation_id={self.evaluation_id}, answer_id={self.answer_id},value={self.value})" 
# Creates class Score.     
    

class Evaluation_Finished(Base):
    __tablename__='evaluation_finished'
    
    evaluation_finished_id=Column(Integer, primary_key=True)
    evaluation_id = Column(ForeignKey("evaluations.evaluation_id"))
    date=Column(DateTime)
    evaluation=relationship('Evaluation',backref=backref('evaluation_finished',uselist=False))
    
     
    def __repr__(self):
        return f"Evaluation_Finished(evaluation_id={self.evaluation_id},date={self.date})" 
# Creates class Evaluation_Finished. one(evaluation) to one(evaluation_finished) relationship. 




## main class
class GradeDB:
    
    def __init__(self, filename):
        self._engine = create_engine('sqlite:///' + filename, echo=False)
        self._session_maker = sessionmaker(bind=self._engine)
        
    
    def add_student(self, _university_id, _first_name, _last_name, _email):
        
        with self._session_maker() as add_session:
            s = Student(university_id=_university_id, first_name=_first_name, last_name=_last_name, email=_email)
            add_session.add(s)
            add_session.commit()
            return s.university_id
        
    def add_question(self, _title, _text, _max_points):
        
        with self._session_maker() as add_session:
            q = Question(title=_title, text=_text, max_points = _max_points)
            add_session.add(q)
            add_session.commit()
            return q.question_id
        
    def add_task(self, _title, _text,_questions):
        
        with self._session_maker() as add_session:
            
            t = Task(title=_title, text=_text)
            add_session.add(t)
            for question in _questions:
                t.questions.append(question)
            add_session.commit()
            return t.task_id
        
    def add_assignment(self, student, task):
        
        with self._session_maker() as add_session:
            a = Assignment(university_id=student.university_id, task_id=task.task_id)
            add_session.add(a)
            add_session.commit()
            return a.assignment_id
        
    def new_submission(self):                #we don't have an input
        from datetime import date
        
        with self._session_maker() as add_session:
            ns = Submission(last_modified = date.today().strftime("%Y.%m.%d")) #submission_id: is it autogenerated and can it therefore be excluded from here?
          
            add_session.add(ns)
            add_session.commit()
            return ns.submission_id
    
    def add_answer(self, _text):
        
        with self._session_maker() as add_session:
            add_an = Answer(text = _text)
            add_session.add(add_an)
            add_session.commit()
            return add_an.answer_id
      
    
    def commit_submission(self, ns):
        
        with self._session_maker() as add_session:
            com_sub = Evaluation_Request(date = ns.last_modified)
            add_session.add(com_sub)
            add_session.commit()
            return com_sub.evaluation_request_id