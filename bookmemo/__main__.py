import argparse
import os
from pathlib import Path

from .store import Book, Store


def main(argv=None) -> None:
    p = argparse.ArgumentParser(prog="bookmemo")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add", help="本を足す")
    a.add_argument("title")
    a.add_argument("--author", default="")
    a.add_argument("--rating", type=int, default=0)
    sub.add_parser("list", help="一覧を出す")
    args = p.parse_args(argv)

    store = Store(Path(os.environ.get("BOOKMEMO_FILE", "books.json")))
    if args.cmd == "add":
        store.add(Book(args.title, args.author, args.rating))
        print(f"足した：{args.title}")
    elif args.cmd == "list":
        for b in store.load():
            stars = "★" * b.rating + "☆" * (5 - b.rating)
            print(f"{stars}  {b.title}  {b.author}")


if __name__ == "__main__":
    main()
