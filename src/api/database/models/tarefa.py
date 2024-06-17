from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.api.database.models.entity_model_base import EntityModelBase


class Tarefa(EntityModelBase):
    __tablename__ = "tarefas"

    nome: Mapped[str] = mapped_column(String(255), nullable=False)
    descricao: Mapped[str] = mapped_column(String(255), nullable=False)
    data_prazo: Mapped[date] = mapped_column(Date, nullable=False)
    data_ultima_notificacao: Mapped[date] = mapped_column(Date, nullable=True)
    data_conclusao: Mapped[date] = mapped_column(Date, nullable=True)

    aluno_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("alunos.id"), nullable=False, unique=False, index=True
    )
    aluno: Mapped["Aluno"] = relationship(  # noqa: F821
        "Aluno", back_populates="tarefas"
    )
