"""Initial database tables

Revision ID: 851c8410f3d2
Revises: 
Create Date: 2024-05-04 12:30:55.377466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '851c8410f3d2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('psychologist',
    sa.Column('cedula', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('sex', sa.String(length=1), nullable=False),
    sa.PrimaryKeyConstraint('cedula')
    )
    op.create_table('child',
    sa.Column('cedula', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('sex', sa.String(length=1), nullable=False),
    sa.Column('psychologist_id', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['psychologist_id'], ['psychologist.cedula'], ),
    sa.PrimaryKeyConstraint('cedula')
    )
    op.create_table('questionnaire_response',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('child_age', sa.Integer(), nullable=False),
    sa.Column('child_scholar_grade', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('reason', sa.String(length=170), nullable=False),
    sa.Column('referrer', sa.String(length=50), nullable=False),
    sa.Column('answers', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('psychologist_id', sa.String(length=10), nullable=False),
    sa.Column('child_id', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['child_id'], ['child.cedula'], ),
    sa.ForeignKeyConstraint(['psychologist_id'], ['psychologist.cedula'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questionnaire_response')
    op.drop_table('child')
    op.drop_table('psychologist')
    # ### end Alembic commands ###