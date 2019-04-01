from pprint import pprint
import psycopg2

def create_db(database, user, password, host):
    with psycopg2.connect(database=database, user=user, password=password, host=host) as conn:
        with conn.cursor() as curs:
            curs.execute('''DROP TABLE IF EXISTS "public"."Course";
                            CREATE TABLE "public"."Course" (
                              "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (
                                INCREMENT 1
                                MINVALUE  1
                                MAXVALUE 2147483647
                                START 1
                                ),
                              "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL
                            );
                            ALTER TABLE "public"."Course" ADD CONSTRAINT "Course_pkey" PRIMARY KEY ("id");
                            
                            DROP TABLE IF EXISTS "public"."Student";
                            CREATE TABLE "public"."Student" (
                              "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (
                                INCREMENT 1
                                MINVALUE  1
                                MAXVALUE 2147483647
                                START 1
                                ),
                              "name" char(100) COLLATE "pg_catalog"."default" NOT NULL,
                              "gpa" float8,
                              "birth" timestamp(6)
                            );
                            ALTER TABLE "public"."Student" ADD CONSTRAINT "Student_pkey" PRIMARY KEY ("id");
                            ''')

def get_students(course_id): # возвращает студентов определенного курса
    pass

def add_students(course_id, students): # создает студентов и записывает их на курс
    pass

def add_student(student): # просто создает студента
    pass

def get_student(student_id): # получает студента по id
    pass

if __name__ == '__main__':
    create_db(database='postgres', user='artempakhomov', password='milk0990', host='localhost')