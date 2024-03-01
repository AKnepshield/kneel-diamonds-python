import json
import sqlite3


def list_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            o.id AS order_id,
            o.style_id AS style_id,
            o.size_id AS size_id,
            o.metal_id AS metal_id,
            st.style AS style_style,
            st.price AS style_price,
            si.carets AS size_carets,
            si.price AS size_price,
            m.metal AS metal_metal,
            m.price AS metal_price
        FROM Orders o
        LEFT JOIN Styles st ON o.style_id = st.id
        LEFT JOIN Sizes si ON o.size_id = si.id
        LEFT JOIN Metals m ON o.metal_id = m.id
        """,
            (),
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        orders = []
        for row in query_results:
            order = {
                "order_id": row["order_id"],
                "metal": {
                    "id": row["metal_id"],
                    "metal": row["metal_metal"],
                    "price": row["metal_price"],
                },
                "style": {
                    "id": row["style_id"],
                    "style": row["style_style"],
                    "price": row["style_price"],
                },
                "size": {
                    "id": row["size_id"],
                    "size": row["size_carets"],
                    "price": row["size_price"],
                },
            }

            orders.append(dict(order))

        # Serialize Python list to JSON encoded string
        serialized_orders = json.dumps(orders)

    return serialized_orders


def delete_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        DELETE FROM Orders WHERE id = ?
        """,
            (pk,),
        )
        number_of_rows_deleted = db_cursor.rowcount

    return True if number_of_rows_deleted > 0 else False


def retrieve_order(pk):
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            o.*
        FROM Orders o
        WHERE o.id = ?
        """,
            (pk,),
        )
        query_results = db_cursor.fetchone()

        # Serialize Python list to JSON encoded string
        serialized_order = json.dumps(dict(query_results))

    return serialized_order


def post_order(order_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                    INSERT INTO Orders (metal_id, style_id, size_id)
                    VALUES (?, ?, ?)
                """,
            (order_data["metal_id"], order_data["style_id"], order_data["size_id"]),
        )

        rows_affected = db_cursor.rowcount

    return True if rows_affected > 0 else False
