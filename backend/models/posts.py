from flask import Response, jsonify
from psycopg2.extras import DictCursor

from backend.db import get_db
from backend.models.tags import Tags
from backend.utils import database_error


class Posts:
    """
    A class for handling interactions with the Posts table in the
    database.
    """

    @staticmethod
    def get(id: int) -> Response:
        try:
            conn = get_db()
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT * FROM Posts
                    WHERE post_id = (%s)
                    """,
                    (id,),
                )
                post = cursor.fetchone()

                cursor.execute(
                    """
                    SELECT user_name FROM Users
                    JOIN PostUser
                    ON Users.user_id = PostUser.user_id
                    WHERE PostUser.post_id = (%s)
                    """,
                    (id,),
                )

                authors = cursor.fetchall()

            data = {
                "title": post["title"],
                "abstract": post["abstract"],
                "content": post["content"],
                "created_at": post["created_at"],
                "updated_at": post["updated_at"],
                "authors": authors,
            }
            return jsonify(data)

        except Exception as e:
            return database_error(e)

    @staticmethod
    def get_next_id() -> int:
        """
        A function to get the post id for the new post.

        Returns:
            int: returns a post id.
        """

        try:
            conn = get_db()
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT post_id FROM Posts
                    ORDER BY post_id DESC
                    LIMIT 1;
                    """
                )
                post_id = cursor.fetchone()

                post_id = post_id[0] if post_id else 1

            return post_id + 1
        except Exception as e:
            return database_error(e)

    @staticmethod
    def get_tags(post_id: int) -> list[str]:
        """
        A function that returns the tags associated with a post given the post id.

        Args:
            post_id (int): id of the post.

        Returns:
            list[str]: tags associated with the provided post id.
        """
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT tag_name FROM PostTag
                    JOIN Tags
                    ON PostTag.tag_id = Tags.tag_id
                    WHERE post_id = (%s);
                    """,
                    [post_id],
                )

                result = cursor.fetchall()

                tags = [r for row in result for r in row] if result else []

            return tags
        except Exception as e:
            database_error(e)

    @staticmethod
    def add(
        title: str, abstract: str, content: str, author_ids: list[int], tags: list[str]
    ) -> Response:
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                post_id = Posts.get_next_id()

                cursor.execute(
                    """
                    INSERT INTO Posts (post_id, title, abstract, content)
                    VALUES (%s, %s, %s, %s)
                    """,
                    [post_id, title, abstract, content],
                )

                for author_id in author_ids:
                    cursor.execute(
                        """
                        INSERT INTO PostUser (post_id, user_id)
                        VALUES (%s, %s)
                        """,
                        [post_id, author_id],
                    )

                for tag in tags:
                    Tags.add(tag)

                    cursor.execute(
                        """
                        INSERT INTO PostTag (post_id, tag_id)
                        VALUES (%s, %s)
                        """,
                        [post_id, Tags.get_id(tag)],
                    )

                conn.commit()

            return "", 201
        except Exception as e:
            return database_error(e)
