"""create users table

Revision ID: ab3520708a52
Revises: 
Create Date: 2022-08-10 12:40:11.645850

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ab3520708a52'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'employee',
        sa.Column("id",sa.INTEGER,primary_key=True,autoincrement=True),
        sa.Column("name",sa.VARCHAR(20),nullable=False),
        sa.Column("email",sa.VARCHAR(50),nullable=False),
        sa.Column("telephone",sa.VARCHAR(50),nullable=False),
        sa.Column("salary",sa.DECIMAL(2),nullable=False)
    )

    op.create_table(
        "manager",
        sa.Column("id",sa.INTEGER,primary_key=True,autoincrement=True),
        sa.Column("name",sa.VARCHAR(50),nullable=False),
        sa.Column("departament",sa.VARCHAR(50),nullable=False),
        sa.Column("employee_id",sa.INTEGER,nullable=False)
    )
   
    op.create_foreign_key("fk_employee_id","manager","employee",["employee_id"],["id"])
    op.create_index("idx_manager_employee_id","manager",["employee_id"])

    op.create_table(
        "departaments",
        sa.Column("id",sa.INTEGER,primary_key=True,autoincrement=True),
        sa.Column("name",sa.VARCHAR(50),nullable=False),
        sa.Column("type",sa.Enum("m","d"),nullable=False),
        sa.Column("description",sa.VARCHAR(200),nullable=True)
    )

    op.create_table(
        "departaments_manager_employee",
        sa.Column("departament_id",sa.INTEGER,nullable=False),
        sa.Column("employee_id",sa.INTEGER,nullable=False),
        sa.Column("manager_id",sa.INTEGER,nullable=False)
    )
    op.create_index(
        "idx_departament_id_employee_id_manager_id",
        "departaments_manager_employee",
        ["departament_id","employee_id","manager_id"]
        )
    op.create_foreign_key("fk_departament_id","departaments_manager_employee","departaments",["departament_id"],["id"])
    op.create_foreign_key("fk_manager_employee_id","departaments_manager_employee","employee",["employee_id"],["id"])
    op.create_foreign_key("fk_manager_id","departaments_manager_employee","manager",["manager_id"],["id"])
    op.create_primary_key(
        "pk_departaments_manager_employee",
        "departaments_manager_employee",
        ["departament_id","employee_id","manager_id"])

def downgrade() -> None:
    op.drop_table("departaments_manager_employee")
    op.drop_table("departaments")
    op.drop_table("manager")
    op.drop_table("employee")
    
    
