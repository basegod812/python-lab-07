"""ЛР №7, вариант 2: SQLite, ORM SQLAlchemy, PostgreSQL."""
import os
import sqlite3
from contextlib import closing

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Session, relationship


class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")


def sqlite_demo():
    """Средние №2, №4, №7: INSERT, UPDATE и несколько таблиц."""
    with closing(sqlite3.connect(":memory:")) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(
            "CREATE TABLE groups (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
        conn.execute(
            "CREATE TABLE students (id INTEGER PRIMARY KEY, "
            "name TEXT NOT NULL, group_id INTEGER REFERENCES groups(id))")
        conn.execute("INSERT INTO groups (id, name) VALUES (?, ?)", (1, "221141"))
        conn.execute(
            "INSERT INTO students (id, name, group_id) VALUES (?, ?, ?)",
            (1, "Герман", 1))
        conn.execute(
            "UPDATE students SET name=? WHERE id=?", ("Шкловский Герман", 1))
        rows = conn.execute(
            "SELECT students.name, groups.name "
            "FROM students JOIN groups ON students.group_id=groups.id"
        ).fetchall()
        conn.commit()
        return rows


def orm_crud_demo(url="sqlite+pysqlite:///:memory:"):
    """Повышенное №2: полный CRUD через SQLAlchemy ORM."""
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        department = Department(name="Производство")
        employee = Employee(name="Герман", department=department)
        session.add(employee)
        session.commit()
        employee_id = employee.id

        found = session.scalar(select(Employee).where(Employee.id == employee_id))
        assert found is not None
        before = found.name

        found.name = "Шкловский Герман"
        session.commit()
        after = session.get(Employee, employee_id).name

        session.delete(found)
        session.commit()
        deleted = session.get(Employee, employee_id) is None

        return {"created_id": employee_id, "read": before,
                "updated": after, "deleted": deleted}


def postgres_demo():
    """Повышенное №6: подключение к PostgreSQL через psycopg2.

    DSN передаётся через переменную окружения POSTGRES_DSN.
    """
    dsn = os.environ.get("POSTGRES_DSN")
    if not dsn:
        print("PostgreSQL: соединение пропущено, укажите POSTGRES_DSN")
        return None
    import psycopg2
    with psycopg2.connect(dsn) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT current_database(), version()")
            result = cursor.fetchone()
            print("PostgreSQL:", result)
            return result


if __name__ == "__main__":
    print("SQLite:", sqlite_demo())
    print("SQLAlchemy CRUD:", orm_crud_demo())
    postgres_demo()
