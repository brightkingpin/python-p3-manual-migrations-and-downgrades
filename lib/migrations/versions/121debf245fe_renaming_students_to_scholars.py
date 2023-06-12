"""Renaming students to scholars

Revision ID: 121debf245fe
Revises: 791279dd0760
Create Date: 2023-06-06 01:41:14.959244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '121debf245fe'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    op.alter_column('students', 'name', student_name='student_name')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    op.alter_column('students', 'student_name', student_name='name')