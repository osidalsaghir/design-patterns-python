from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):

    @property
    @abstractmethod
    def post(self) -> None:
        pass

    @abstractmethod
    def title_to_the_post(self) -> None:
        pass

    @abstractmethod
    def body_to_the_post(self) -> None:
        pass

    @abstractmethod
    def footer_to_the_post(self) -> None:
        pass


class PostBuilder(Builder):
    
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._post = Post()

    @property
    def post(self) -> Post:
        post = self._post
        self.reset()
        return post

    def title_to_the_post(self) -> None:
        self._post.add("This is title")

    def body_to_the_post(self) -> None:
        self._post.add("This is body")

    def footer_to_the_post(self) -> None:
        self._post.add("This is footer")


class Post():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Post parts: {', '.join(self.parts)}", end="")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def add_only_title(self) -> None:
        self.builder.title_to_the_post()

    def add_full_post(self) -> None:
        self.builder.title_to_the_post()
        self.builder.body_to_the_post()
        self.builder.footer_to_the_post()


if __name__ == "__main__":


    director = Director()
    postBuilder = PostBuilder()
    director.builder = postBuilder

    print("Adding title only to the post: ")
    director.add_only_title()
    postBuilder.post.list_parts()

    print("\n")

    print("Adding full post: ")
    director.add_full_post()
    postBuilder.post.list_parts()

    print("\n")

    print("Custom post: ")
    postBuilder.title_to_the_post()
    postBuilder.body_to_the_post()
    postBuilder.footer_to_the_post()
    postBuilder.post.list_parts()