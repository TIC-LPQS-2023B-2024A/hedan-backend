"""upgrade_test_session_columns

Revision ID: 84f17ee79218
Revises: cdf38d148e35
Create Date: 2024-06-16 13:09:59.527144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '84f17ee79218'
down_revision: Union[str, None] = 'cdf38d148e35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_sessions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('child_id', sa.Integer(), nullable=False),
    sa.Column('psychologist_cedula', sa.String(), nullable=False),
    sa.Column('child_age', sa.Integer(), nullable=False),
    sa.Column('scholar_grade', sa.Integer(), nullable=False),
    sa.Column('child_sex', sa.String(length=1), nullable=False),
    sa.Column('test_sender', sa.String(), nullable=False),
    sa.Column('test_reason', sa.String(), nullable=False),
    sa.Column('test_token', sa.String(), nullable=True),
    sa.Column('date_time_of_answer', sa.DateTime(timezone=True), nullable=True),
    sa.Column('answers', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('test_results', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('calculate_test_results_time_taken', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('child_id'),
    schema='questionnaires'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_sessions', schema='questionnaires')
    # ### end Alembic commands ###
