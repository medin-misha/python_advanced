from typing import List, Optional

from flask import Flask, request

app = Flask(__name__)


@app.route(
    "/search/", methods=["GET"],
)#после сылки на страницу нужно прописать какой метод мы испрользуем methods=["GET"]
def search():
    #обращяемся к обьекту request извлекаем args.getlist("cell_tower_id" и иесли нужно type=int)
    cell_tower_ids: List[int] = request.args.getlist("cell_tower_id", type=int)

    if not cell_tower_ids:
        return f"You must specify at least one cell_tower_id", 400

    phone_prefixes: List[str] = request.args.getlist("phone_prefix")

    protocols: List[str] = request.args.getlist("protocol")

    signal_level: Optional[float] = request.args.get(
        "signal_level", type=float, default=None
    )
    date_time:list[str] = request.args.getlist("date_time")

    return (
        f"Search for {cell_tower_ids} cell towers. Search criteria: "
        f"phone_prefixes={phone_prefixes}, "
        f"protocols={protocols}, "
        f"signal_level={signal_level}"
        f"date_time={date_time}"
    )


if __name__ == "__main__":
    app.run(debug=True)
