from typing import Dict

from flask import Response


class Comments:
    """
    A class for handling interactions with the Comments table in the
    database.
    """

    @staticmethod
    def get(comment_id: int) -> Dict[str, str]:
        """
        A function that returns the user id, comment text, and the time
        at which the comment was created at.

        Args:
            comment_id (int): id of tge comment.

        Returns:
            Dict[str, str]: A dictionary with "user_id", "comment_text",
            "created_at" keys and their corresponding values.
        """
        raise NotImplementedError

    @staticmethod
    def get_next_id() -> int:
        """
        A function to get the comment id for the new comment.

        Returns:
            int: comment id for the next comment.
        """
        raise NotImplementedError

    @staticmethod
    def add(post_id: str, user_id: str, comment_text: str) -> Response:
        """
        A function to add a comment to the Comments relation.

        Args:
            post_id (str): id of the post.
            user_id (str): id of the user.
            comment_text (str): comment.

        Returns:
            Response: success or failure.
        """
        raise NotImplementedError
