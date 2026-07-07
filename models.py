from database import get_connection


def add_post(post_type, text, file_path, schedule_time):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO posts
        (type, text, file_path, schedule_time)
        VALUES (?, ?, ?, ?)
    """, (
        post_type,
        text,
        file_path,
        schedule_time
    ))

    conn.commit()
    conn.close()


def get_pending_posts(current_time):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM posts
        WHERE status = 'pending'
        AND schedule_time <= ?
        ORDER BY schedule_time ASC
    """, (current_time,))

    posts = cursor.fetchall()

    conn.close()

    return posts


def mark_sent(post_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE posts
        SET status = 'sent'
        WHERE id = ?
    """, (post_id,))

    conn.commit()
    conn.close()


def delete_post(post_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM posts
        WHERE id = ?
    """, (post_id,))

    conn.commit()
    conn.close()


def get_post(post_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM posts
        WHERE id = ?
    """, (post_id,))

    post = cursor.fetchone()

    conn.close()

    return post


def get_all_posts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM posts
        ORDER BY schedule_time ASC
    """)

    posts = cursor.fetchall()

    conn.close()

    return posts
