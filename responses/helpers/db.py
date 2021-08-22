from typing import List, Tuple

def get_user(conn ,phone_number: str) -> Tuple[str, List[str], str]:
    """
    Get user info from db.
    """
    with conn.cursor() as cur:

        # Get user info from db.
        cur.execute("SELECT * FROM users WHERE phone_number = %s", (phone_number,))
        usr = cur.fetchone()
        if usr is None:
            return None
        return usr

def set_user(conn, phone_number: str, options: List[str], t: str) -> None:
    """
    Set user info in db.
    """
    with conn.cursor() as cur:

        # Get user info from db.
        cur.execute("UPSERT INTO users (phone_number, options, t) VALUES (%s, %s, %s)", (phone_number, options, t))
    conn.commit()
    return None