from sqlalchemy.orm import Session
from models.tasks_model import Task
from models.user_task import UserTaskMapping
from models.tasks_model import Task

def get_task_by_id(db: Session, task_id: int):
    try:
        return db.query(Task).filter(Task.id == task_id).first()
    except Exception as e:
        print(f"Error occurred while fetching tasks: {e}")
        return None

def get_all_task(db: Session,current_user):
    try:

        if current_user == "admin":
            return db.query(Task).all()
        
        mappings = db.query(Task).filter(
            UserTaskMapping.user_id == current_user.id
        ).all()

        task_id = [
            mapping.task_id
            for mapping in mappings
        ]

        tasks = db.query(Task).filter(
            Task.id.in_(task_id)
        ).all()

        return tasks

    except Exception as e:
        print(f"Error occurred while fetching tasks: {e}")
        return None
def create_task(db: Session, task):
    try:
        db_task = Task(
            title=task.title,
            description=task.description
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    except Exception as e :
        print(f"Error occurred while fetching tasks: {e}")
        return None



def update_task(db: Session, id: int, task,current_user):
    try : 


        db_task = db.query(Task).filter(Task.id == id).first()
       

        if db_task:
            db_task.title = task.title
            db_task.description = task.description
            
            
            db.commit()
            db.refresh(db_task)
            return db_task
        return None
    
    except Exception as e:
            print(f"Error occurred while fetching task: {e}")
            return None
        
def delete_task(db: Session, id: int):
    db_task = db.query(Task).filter(Task.id == id).first()
    try:
        if db_task:
            db.delete(db_task)
            db.commit()
            return True
        return False
    except Exception as e:
        print(f"Error occurred while fetching task: {e}")
        return False


