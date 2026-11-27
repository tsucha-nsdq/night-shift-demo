import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Book:
    title: str
    author: str = ""
    rating: int = 0  # 0 は未評価、1〜5


class Store:
    def __init__(self, path: Path):
        self.path = Path(path)

    def load(self) -> list[Book]:
        if not self.path.exists():
            return []
        return [Book(**b) for b in json.loads(self.path.read_text(encoding="utf-8"))]

    def save(self, books: list[Book]) -> None:
        self.path.write_text(
            json.dumps([asdict(b) for b in books], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def add(self, book: Book) -> None:
        if not 0 <= book.rating <= 5:
            raise ValueError("rating は 0〜5")
        books = self.load()
        books.append(book)
        self.save(books)
