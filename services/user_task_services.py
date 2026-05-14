from sqlalchemy.orm import Session

from models.user_task import UserTaskMapping


def assign_task_to_user(db: Session, mapping):

    try:

        db_mapping = UserTaskMapping(
            user_id=mapping.user_id,
            task_id=mapping.task_id
        )

        db.add(db_mapping)

        db.commit()

        db.refresh(db_mapping)

        return db_mapping

    except Exception as e:

        print(f"Error occurred while assigning task: {e}")

        return None


def get_all_task_mappings(db: Session):

    try:

        return db.query(UserTaskMapping).all()

    except Exception as e:

        print(f"Error occurred while fetching mappings: {e}")

        return None


def get_tasks_of_user(db: Session, user_id: int):

    try:

        return db.query(UserTaskMapping).filter(
            UserTaskMapping.user_id == user_id
        ).all()

    except Exception as e:

        print(f"Error occurred while fetching user tasks: {e}")

        return None


def delete_task_mapping(db: Session, mapping_id: int):

    try:

        mapping = db.query(UserTaskMapping).filter(
            UserTaskMapping.id == mapping_id
        ).first()

        if mapping:

            db.delete(mapping)

            db.commit()

            return True

        return False

    except Exception as e:

        print(f"Error occurred while deleting mapping: {e}")

        return False