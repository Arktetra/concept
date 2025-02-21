from flask import Response, jsonify
from psycopg2.extras import DictCursor

from backend.db import get_db
from backend.models.categories import Categories
from backend.models.posts import Posts
from backend.utils import database_error


class Concepts:
    @staticmethod
    def get() -> Response:
        """
        A function to get all the concepts from the database. Concepts here
        means all the posts which are not in a category, and all the categories.
        """

        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                # get posts which are not in any categories and the
                # categories
                cursor.execute(
                    """
                    SELECT * FROM (
                        SELECT post_id, title, abstract, created_at, updated_at, 'posts' AS type
                            FROM Posts
                        WHERE category_id IS NULL
                        UNION
                        SELECT category_id, title, abstract, created_at, updated_at, 'categories'
                            AS type FROM Categories
                    )
                    ORDER BY created_at DESC;
                    """
                )
                concepts = cursor.fetchall()

                # get authors of each post
                cursor.execute(
                    """
                    SELECT Posts.post_id, user_name FROM Users
                    JOIN PostUser
                    ON Users.user_id = PostUser.user_id
                    JOIN Posts
                    ON Posts.post_id = PostUser.post_id
                    WHERE Posts.category_id is NULL;
                    """
                )
                post_authors = cursor.fetchall()

                # get authors in each categories
                cursor.execute(
                    """
                    SELECT category_id, user_name FROM Users
                    JOIN PostUser
                    ON Users.user_id = PostUser.user_id
                    JOIN Posts
                    ON PostUser.post_id = PostUser.post_id
                    WHERE Posts.category_id is NOT NULL;
                    """
                )
                category_authors = cursor.fetchall()

            data = []
            post_authors_map = {}
            category_authors_map = {}

            for post, author in post_authors:
                if post not in post_authors_map:
                    post_authors_map[post] = [author]
                else:
                    post_authors_map[post].append(author)

            for category, author in category_authors:
                if category not in category_authors_map:
                    category_authors_map[category] = [author]
                else:
                    if author not in category_authors_map[category]:
                        category_authors_map[category].append(author)

            for concept in concepts:
                if concept["type"] == "posts":
                    authors = post_authors_map[concept[0]]
                    tags = Posts.get_tags(concept[0])
                else:
                    if concept[0] in category_authors_map:
                        authors = category_authors_map[concept[0]]
                    else:
                        authors = []

                    tags = []

                data.append(
                    {
                        "id": concept[0],
                        "title": concept["title"],
                        "abstract": concept["abstract"],
                        "created_at": concept["created_at"],
                        "updated_at": concept["updated_at"],
                        "authors": authors,
                        "tags": tags,
                        "type": concept["type"],
                    }
                )

            return jsonify(data)
        except Exception as e:
            database_error(e)

    @staticmethod
    def add(
        title: str,
        abstract: str,
        content: str,
        author_ids: list[int],
        tags: list[str],
        concept_type: str,
    ) -> Response:
        if concept_type == "post":
            return Posts.add(title, abstract, content, author_ids, tags)
        elif concept_type == "category":
            return Categories.add(title, abstract)
        else:
            return jsonify({"error": f"unknown type of concept {concept_type}."}), 500
