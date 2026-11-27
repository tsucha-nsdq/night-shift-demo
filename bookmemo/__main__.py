import argparse
import os
import sys
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
    d = sub.add_parser("delete", help="本を消す（タイトルが一致するものを全部）")
    d.add_argument("title")
    args = p.parse_args(argv)

    store = Store(Path(os.environ.get("BOOKMEMO_FILE", "books.json")))
    if args.cmd == "add":
        store.add(Book(args.title, args.author, args.rating))
        print(f"足した：{args.title}")
    elif args.cmd == "list":
        for b in store.load():
            stars = "★" * b.rating + "☆" * (5 - b.rating)
            print(f"{stars}  {b.title}  {b.author}")
    elif args.cmd == "delete":
        n = store.delete(args.title)
        if n == 0:
            sys.exit(f"見つからない：{args.title}")
        print(f"消した：{args.title}（{n} 冊）")


if __name__ == "__main__":
    main()
