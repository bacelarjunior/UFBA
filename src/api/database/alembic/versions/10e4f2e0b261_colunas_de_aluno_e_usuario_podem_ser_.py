"""Colunas de aluno e usuario podem ser duplicadas para possibilitar soft-delete

Revision ID: 10e4f2e0b261
Revises: 7b60b08c6475
Create Date: 2024-06-17 13:16:02.924767

"""

from typing import Sequence, Union

from alembic import op

from src.api.database.models.aluno import Aluno
from src.api.database.models.professor import Professor
from src.api.database.models.solicitacoes import Solicitacao
from src.api.database.models.tipo_usuario import TipoUsuario
from src.api.database.models.usuario import Usuario

# revision identifiers, used by Alembic.
revision: str = "10e4f2e0b261"
down_revision: Union[str, None] = "7b60b08c6475"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_alunos_cpf", table_name="alunos")
    op.create_index(op.f("ix_alunos_cpf"), "alunos", ["cpf"], unique=False)
    op.drop_index("ix_alunos_matricula", table_name="alunos")
    op.create_index(op.f("ix_alunos_matricula"), "alunos", ["matricula"], unique=False)
    op.drop_index("ix_alunos_telefone", table_name="alunos")
    op.create_index(op.f("ix_alunos_telefone"), "alunos", ["telefone"], unique=False)
    op.drop_index("ix_usuarios_email", table_name="usuarios")
    op.create_index(op.f("ix_usuarios_email"), "usuarios", ["email"], unique=False)

    op.bulk_insert(
        TipoUsuario.__table__,
        [
            {
                "titulo": "ALUNO",
                "descricao": "Aluno description",
                "id": 3,
                "created_at": "2024-06-17 00:00:00",
                "updated_at": "2024-06-17 00:00:00",
                "deleted_at": None,
            },
            {
                "titulo": "PROFESSOR",
                "descricao": "Professor description",
                "id": 2,
                "created_at": "2024-06-17 00:00:00",
                "updated_at": "2024-06-17 00:00:00",
                "deleted_at": None,
            },
            {
                "titulo": "COORDENADOR",
                "descricao": "Coordenador description",
                "id": 1,
                "created_at": "2024-06-17 00:00:00",
                "updated_at": "2024-06-17 00:00:00",
                "deleted_at": None,
            },
        ],
    )
    op.bulk_insert(
        Usuario.__table__,
        [
            {
                "nome": "Prof Fred Durão",
                "email": "fred_professor@ufba.br",
                "senha_hash": "$2b$12$jagLVP7tdNJQ0y/V97yTGe5I7gcVFn8tb79LgBMShlfbYGZZ0qyBq",  # noqa
                "new_password_token": None,
                "tipo_usuario_id": 2,
                "id": 1,
                "created_at": "2024-06-17 00:00:00",
                "updated_at": "2024-06-17 00:00:00",
                "deleted_at": None,
            },
            {
                "nome": "Aluno Fred Durão",
                "email": "fred_aluno@ufba.br",
                "senha_hash": "$2b$12$UkAuRH33KQCtXszd93ujhO994KdVA8BOAyvtaO4zDxlys54g.ruai",  # noqa
                "new_password_token": None,
                "tipo_usuario_id": 3,
                "id": 2,
                "created_at": "2024-06-17 00:00:00",
                "updated_at": "2024-06-17 00:00:00",
                "deleted_at": None,
            },
            {
                "nome": "Coord Fred Durão",
                "email": "fred_coordenador@ufba.br",
                "senha_hash": "$2b$12$WGZL3R1KnQaZUMBs27Cw.e/YXYHgcEQ0iFQI59EaddLd./DRJkTlm",  # noqa
                "new_password_token": None,
                "tipo_usuario_id": 1,
                "id": 3,
                "created_at": "2024-06-17 00:00:00",
                "updated_at": "2024-06-17 00:00:00",
                "deleted_at": None,
            },
        ],
    )
    op.bulk_insert(
        Professor.__table__,
        [
            {
                "usuario_id": 1,
                "id": 1,
                "created_at": "2024-06-17 00:00:00",
                "updated_at": "2024-06-17 00:00:00",
                "deleted_at": None,
            },
            {
                "usuario_id": 3,
                "id": 2,
                "created_at": "2024-06-17 00:00:00",
                "updated_at": "2024-06-17 00:00:00",
                "deleted_at": None,
            },
        ],
    )
    op.bulk_insert(
        Aluno.__table__,
        [
            {
                "cpf": "851.711.570-81",
                "telefone": "(71) 99999-9999",
                "matricula": "123456",
                "lattes": "http://lattes.cnpq.br/6271096128174325",
                "curso": "MESTRADO",
                "data_ingresso": "2024-06-17 00:00:00",
                "data_qualificacao": "2025-06-17",
                "data_defesa": "2026-06-17",
                "orientador_id": 1,
                "usuario_id": 2,
                "id": 1,
                "created_at": "2024-06-17 00:00:00",
                "updated_at": "2024-06-17 00:00:00",
                "deleted_at": None,
            }
        ],
    )
    op.bulk_insert(
        Solicitacao.__table__,
        [
            {
                "aluno_id": 1,
                "professor_id": 1,
                "status": "PENDENTE",
                "id": 1,
                "created_at": "2024-06-17 00:00:00",
                "updated_at": "2024-06-17 00:00:00",
                "deleted_at": None,
            }
        ],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_usuarios_email"), table_name="usuarios")
    op.create_index("ix_usuarios_email", "usuarios", ["email"], unique=True)
    op.drop_index(op.f("ix_alunos_telefone"), table_name="alunos")
    op.create_index("ix_alunos_telefone", "alunos", ["telefone"], unique=True)
    op.drop_index(op.f("ix_alunos_matricula"), table_name="alunos")
    op.create_index("ix_alunos_matricula", "alunos", ["matricula"], unique=True)
    op.drop_index(op.f("ix_alunos_cpf"), table_name="alunos")
    op.create_index("ix_alunos_cpf", "alunos", ["cpf"], unique=True)
    # ### end Alembic commands ###
    op.execute("DELETE FROM solicitacoes WHERE id = 1")
    op.execute("DELETE FROM alunos WHERE id = 1")
    op.execute("DELETE FROM professores WHERE id IN (1, 2)")
    op.execute("DELETE FROM usuarios WHERE id IN (1, 2, 3)")
    op.execute("DELETE FROM tipo_usuario WHERE id IN (1, 2, 3)")
