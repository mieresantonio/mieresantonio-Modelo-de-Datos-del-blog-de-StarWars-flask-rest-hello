from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = "Usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }


class Favorito(db.Model):
    __tablename__ = "Favoritos"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("Usuarios.id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey("Planetas.id"), nullable=True)
    character_id: Mapped[int] = mapped_column(ForeignKey("Personajes.id"), nullable=True)


class Planeta(db.Model):
    __tablename__ = "Planetas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    clima: Mapped[str] = mapped_column(String(100))
    poblacion: Mapped[str] = mapped_column(String(100))
    terreno: Mapped[str] = mapped_column(String(100))


class Personaje(db.Model):
    __tablename__ = "Personajes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    altura: Mapped[str] = mapped_column(String(100))
    especie: Mapped[str] = mapped_column(String(100))
    genero: Mapped[str] = mapped_column(String(100))


